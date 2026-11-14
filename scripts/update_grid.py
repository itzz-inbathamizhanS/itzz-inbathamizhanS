#!/usr/bin/env python3
"""Refill the banner's activity grid with real GitHub contributions (last 18 weeks).

Columns are weeks (oldest on the left), rows are weekdays (Sunday on top),
the same layout as GitHub's own contribution graph. The busiest days get the
sage accent; quieter days step up in opacity of the text colour.
"""
import json
import os
import re
import sys
import urllib.request

USER = os.environ.get("GH_USER", "itzz-inbathamizhanS")
WEEKS, GX, GY, PITCH = 18, 1034, 30, 14   # grid ends at the banner's right edge (1280)

PALETTES = {
    # (colour, opacity): drawn in the theme's own text colour so the grid reads on every GitHub ground
    "assets/banner-dark.svg":  {"none": ("#E6EDF3", ".06"), "q1": ("#E6EDF3", ".14"), "q2": ("#E6EDF3", ".26"),
                                "q3": ("#E6EDF3", ".42"), "q4": ("#9FB8A6", "1")},
    "assets/banner-light.svg": {"none": ("#1F2328", ".06"), "q1": ("#1F2328", ".14"), "q2": ("#1F2328", ".26"),
                                "q3": ("#1F2328", ".42"), "q4": ("#4A6B55", "1")},
}
LEVEL = {"NONE": "none", "FIRST_QUARTILE": "q1", "SECOND_QUARTILE": "q2", "THIRD_QUARTILE": "q3", "FOURTH_QUARTILE": "q4"}
QUERY = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar { weeks { contributionDays { weekday contributionLevel } } }
    }
  }
}"""


def fetch_weeks():
    """Return the last WEEKS weeks as a list of 7-item lists of contribution levels."""
    if os.environ.get("GRID_JSON"):  # local testing without the API
        with open(os.environ["GRID_JSON"], encoding="utf-8") as fh:
            return json.load(fh)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get("errors"):
        sys.exit(f"GitHub API error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"][-WEEKS:]
    grid = []
    for week in weeks:
        days = ["NONE"] * 7
        for day in week["contributionDays"]:
            days[day["weekday"]] = day["contributionLevel"]
        grid.append(days)
    while len(grid) < WEEKS:
        grid.insert(0, ["NONE"] * 7)
    return grid


def cells(grid, pal):
    out = []
    for r in range(7):
        for c in range(WEEKS):
            colour, opacity = pal[LEVEL.get(grid[c][r], "none")]
            out.append(
                f'<rect x="{GX + c * PITCH}" y="{GY + r * PITCH}" width="10" height="10" rx="2" '
                f'fill="{colour}" fill-opacity="{opacity}"/>'
            )
    return "".join(out)


def main():
    grid = fetch_weeks()
    for path, pal in PALETTES.items():
        with open(path, encoding="utf-8") as fh:
            svg = fh.read()
        new, n = re.subn(
            r"<!--grid-->.*?<!--/grid-->",
            lambda _m: f"<!--grid-->{cells(grid, pal)}<!--/grid-->",
            svg,
            flags=re.S,
        )
        if n != 1:
            sys.exit(f"Grid markers not found in {path}")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
    print("Grid updated for", USER)


if __name__ == "__main__":
    main()
