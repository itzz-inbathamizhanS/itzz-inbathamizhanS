#!/usr/bin/env python3
"""Keep the profile's "Now" line and Work cards in step with real activity.

* Now: the public repo you pushed to most recently, with its latest commit.
* Work: every project in data/projects.json as a linked card; new public repos
  created on or after `auto_add_after` are added automatically from their
  GitHub description. The current project moves to the front and gets the sage
  "now" mark.

Local test: MOCK_REPOS=repos.json MOCK_COMMITS=commits.json python scripts/update_profile.py
"""
import base64, datetime as dt, io, json, os, re, sys, urllib.request
from html import escape as esc
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "scripts", "fonts")
DATA = os.path.join(ROOT, "data", "projects.json")
README = os.path.join(ROOT, "README.md")
CARDS = os.path.join(ROOT, "assets", "cards")

cfg = json.load(open(DATA, encoding="utf-8"))
USER = cfg["user"]
BASE = f"https://github.com/{USER}/"

# ---------------------------------------------------------------- GitHub data
def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}",
                                 headers={"Accept": "application/vnd.github+json",
                                          **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def repos():
    if os.environ.get("MOCK_REPOS"):
        return json.load(open(os.environ["MOCK_REPOS"], encoding="utf-8"))
    return api(f"users/{USER}/repos?per_page=100&sort=pushed&type=owner")

def last_commit(repo):
    if os.environ.get("MOCK_COMMITS"):
        return json.load(open(os.environ["MOCK_COMMITS"], encoding="utf-8")).get(repo)
    try:
        c = api(f"repos/{USER}/{repo}/commits?per_page=1")[0]
        return {"message": c["commit"]["message"], "date": c["commit"]["author"]["date"]}
    except Exception:
        return None

# ---------------------------------------------------------------- card design (matches DESIGN.md)
T = {"dark":  dict(fg="#E6EDF3", muted="#8B949E", accent="#9FB8A6", rule_op=".22"),
     "light": dict(fg="#1F2328", muted="#59636E", accent="#4A6B55", rule_op=".32")}
CW, CH, PAD = 640, 194, 44
DESK = dict(name=42, line=26, name_y=72, line_y=114, gap=1.3)
PHONE = dict(name=50, line=44, name_y=66, line_y=120, gap=1.15)

def metrics(path):
    f = TTFont(path); c = f.getBestCmap(); h = f["hmtx"]; u = f["head"].unitsPerEm
    return lambda text, size: sum(h[c.get(ord(ch), c[ord("?")])][0] for ch in text) * size / u

F600, F500, F400 = (os.path.join(FONTS, f"hind-madurai-latin-{w}-normal.woff2") for w in (600, 500, 400))
W600, W500, W400 = metrics(F600), metrics(F500), metrics(F400)

def sub(path, text):
    f = TTFont(path, recalcTimestamp=False)   # no timestamps: same input, same bytes, no empty commits
    o = subset.Options(); o.flavor = "woff2"
    s = subset.Subsetter(o); s.populate(text=text); s.subset(f)
    b = io.BytesIO(); f.flavor = "woff2"; f.save(b)
    return base64.b64encode(b.getvalue()).decode()

def wrap(text, width, size, max_lines=2):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if W400(trial, size) <= width or not cur:
            cur = trial
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    if len(lines) > max_lines:                      # long description: keep two lines, end with an ellipsis
        lines = lines[:max_lines]
        while lines[-1] and W400(lines[-1] + "…", size) > width:
            lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else lines[-1][:-1]
        lines[-1] += "…"
    return lines

def plain(name):
    return name.replace("Ṛ", "R")                    # Hind Madurai has no Ṛ: the dot is drawn

def card_layer(cls, name, line, now, tx, x1, t, L):
    shown = plain(name)
    now_size = max(L["name"] * .5, 40 if L is PHONE else 0)
    size = L["name"]
    while tx + W600(shown, size) + (W500("now", now_size) + 22 if now else 0) > x1 - 4 and size > 20:
        size -= 2
    lines = wrap(line, x1 - tx - 6, L["line"])
    dot = ""
    if "Ṛ" in name:
        k = name.index("Ṛ")
        rx = tx + W600(shown[:k], size) + W600("R", size) * 0.42
        dot = f'<circle cx="{rx:.1f}" cy="{L["name_y"] + size * .14:.1f}" r="{size * .055:.1f}" fill="{t["fg"]}"/>'
    now_txt = (f'<text x="{tx + W600(shown, size) + 18:.1f}" y="{L["name_y"]}" font-family="G" font-weight="500" '
               f'font-size="{now_size:.0f}" fill="{t["accent"]}">now</text>') if now else ""
    spans = "".join(f'<tspan x="{tx}" dy="{0 if k == 0 else L["line"] * L["gap"]:.1f}">{esc(l)}</tspan>' for k, l in enumerate(lines))
    return (f'<g class="{cls}"><text x="{tx}" y="{L["name_y"]}" font-family="N" font-weight="600" font-size="{size}" '
            f'letter-spacing="-.01em" fill="{t["fg"]}">{esc(shown)}</text>{dot}{now_txt}'
            f'<text x="{tx}" y="{L["line_y"]}" font-family="L" font-weight="400" font-size="{L["line"]}" fill="{t["muted"]}">{spans}</text></g>')

def card(i, p, theme, last_row, fonts):
    t = T[theme]; now = p.get("_now", False)
    left = i % 2 == 0
    x0, x1 = (0, CW - PAD) if left else (PAD, CW)
    tx, d = x0 + 2, 0.2 + i * 0.09
    stroke = f'stroke="{t["fg"]}" stroke-opacity="{t["rule_op"]}" stroke-width="2"'
    rules = f'<line class="rule" style="animation-delay:{d:.2f}s" x1="{x0}" y1="1" x2="{x1}" y2="1" pathLength="1" {stroke}/>'
    if last_row:
        rules += f'<line class="rule" style="animation-delay:{d + .3:.2f}s" x1="{x0}" y1="{CH - 1}" x2="{x1}" y2="{CH - 1}" pathLength="1" {stroke}/>'
    pulse = (f'<circle class="pulse" cx="{x1 - 12}" cy="58" r="6" fill="{t["accent"]}"/>'
             f'<circle cx="{x1 - 12}" cy="58" r="6" fill="{t["accent"]}"/>') if now else ""
    edge = x1 - (30 if now else 0)
    layers = card_layer("desk", p["name"], p["line"], now, tx, edge, t, DESK) + card_layer("phone", p["name"], p["line"], now, tx, edge, t, PHONE)
    css = (f"@font-face{{font-family:N;src:url(data:font/woff2;base64,{fonts['N']}) format('woff2');font-weight:600}}"
           f"@font-face{{font-family:G;src:url(data:font/woff2;base64,{fonts['G']}) format('woff2');font-weight:500}}"
           f"@font-face{{font-family:L;src:url(data:font/woff2;base64,{fonts['L']}) format('woff2');font-weight:400}}"
           ".phone{display:none}@media (max-width:300px){.desk{display:none}.phone{display:inline}}"
           "@keyframes draw{to{stroke-dashoffset:0}}"
           "@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}"
           "@keyframes pulse{0%{transform:scale(1);opacity:.5}70%,100%{transform:scale(3);opacity:0}}"
           ".rule{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1s cubic-bezier(.16,1,.3,1) both}"
           ".rise{animation:rise .8s cubic-bezier(.16,1,.3,1) both}"
           ".pulse{transform-box:fill-box;transform-origin:center;animation:pulse 2.6s cubic-bezier(.16,1,.3,1) 2s infinite both}"
           "@media (prefers-reduced-motion:reduce){.rule,.rise,.pulse{animation:none}.rule{stroke-dashoffset:0}.pulse{opacity:0}}")
    alt = f"{p['name']}: {p['line']}" + (" (current)" if now else "")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}" role="img" aria-label="{esc(alt)}">'
           f'<style>{css}</style>{rules}{pulse}<g class="rise" style="animation-delay:{d + .15:.2f}s">{layers}</g></svg>\n')
    return svg, alt

# ---------------------------------------------------------------- text helpers
def md_escape(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"([\\`*_\[\]#|])", r"\\\1", s)

def nice_date(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{d.day} {d.strftime('%b %Y')}"

def replace_block(text, tag, body):
    new, n = re.subn(rf"<!--{tag}-->.*?<!--/{tag}-->", lambda _m: f"<!--{tag}-->\n\n{body}\n\n<!--/{tag}-->", text, flags=re.S)
    if n != 1:
        sys.exit(f"README is missing the <!--{tag}--> … <!--/{tag}--> markers")
    return new

# ---------------------------------------------------------------- main
def main():
    all_repos = repos()
    public = [r for r in all_repos if not r.get("fork") and not r.get("archived") and not r.get("private") and r["name"] != USER]
    known = {p["repo"].lower() for p in cfg["projects"]} | {s.lower() for s in cfg.get("skip", [])}

    # 1. add new projects
    added = []
    for r in sorted(public, key=lambda r: r["created_at"]):
        if r["name"].lower() in known or r["created_at"][:10] < cfg["auto_add_after"]:
            continue
        desc = (r.get("description") or "").strip()
        if not desc:
            print(f"skip {r['name']}: add a GitHub description and it will appear next run")
            continue
        entry = {"repo": r["name"], "name": r["name"], "line": desc.rstrip(".")}
        if r.get("homepage"):
            entry["live"] = r["homepage"]
        cfg["projects"].append(entry); added.append(r["name"]); known.add(r["name"].lower())
    if added:
        with open(DATA, "w", encoding="utf-8") as fh:
            json.dump(cfg, fh, ensure_ascii=False, indent=2); fh.write("\n")
        print("added:", ", ".join(added))

    # 2. current project = most recent push
    current = max(public, key=lambda r: r["pushed_at"]) if public else None
    projects = [dict(p) for p in cfg["projects"]]
    if current:
        for p in projects:
            p["_now"] = p["repo"].lower() == current["name"].lower()
        projects.sort(key=lambda p: not p["_now"])          # current project first

    # 3. Now line
    if current:
        entry = next((p for p in cfg["projects"] if p["repo"].lower() == current["name"].lower()), None)
        name = entry["name"] if entry else current["name"]
        what = cfg.get("now_lines", {}).get(current["name"]) or (entry["line"] if entry else (current.get("description") or "")).strip().rstrip(".")
        what = what[:1].lower() + what[1:] if what and not what[:2].isupper() else what
        live = (entry or {}).get("live") or current.get("homepage")
        line = f"[**{md_escape(name)}**]({BASE}{current['name']})" + (f", {md_escape(what)}." if what else ".")
        if live:
            line += f" [Live console]({live})" if name == "Aran" else f" [Live]({live})"
        c = last_commit(current["name"])
        if c:
            msg = c["message"].strip().splitlines()[0][:80]
            line += f"  \n<sub>Last commit {nice_date(c['date'])} · {md_escape(msg)}</sub>"
        now_md = line
    else:
        now_md = None

    # 4. Work cards
    text = "".join(p["name"] for p in projects)
    lines = "".join(p["line"] for p in projects)
    fonts = {"N": sub(F600, plain(text) + "?"), "G": sub(F500, "now"), "L": sub(F400, lines + "…?")}
    os.makedirs(CARDS, exist_ok=True)
    keep, cells = set(), []
    n = len(projects)
    for i, p in enumerate(projects):
        slug = re.sub(r"[^a-z0-9-]+", "-", p["repo"].lower()).strip("-")
        last_row = i >= n - (1 if n % 2 else 2)
        for theme in ("dark", "light"):
            svg, alt = card(i, p, theme, last_row, fonts)
            path = os.path.join(CARDS, f"{slug}-{theme}.svg"); keep.add(path)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(svg)
        cells.append(f'<a href="{BASE}{p["repo"]}"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/{slug}-dark.svg">'
                     f'<img src="./assets/cards/{slug}-light.svg" alt="{esc(alt)}" width="50%" align="top"></picture></a>')
    for f in os.listdir(CARDS):
        full = os.path.join(CARDS, f)
        if f.endswith(".svg") and full not in keep:
            os.remove(full)

    readme = open(README, encoding="utf-8").read()
    if now_md:
        readme = replace_block(readme, "now", now_md)
    readme = replace_block(readme, "work", "<p>" + "".join(cells) + "</p>")
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(readme)
    print("now:", current["name"] if current else "-", "| cards:", n)

if __name__ == "__main__":
    main()
