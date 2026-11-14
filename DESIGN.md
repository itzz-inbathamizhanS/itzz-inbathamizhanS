---
name: Inbathamizhan S
description: A GitHub profile that names him in Tamil first, as a quiet ghost behind the Latin name, then lists the work as a calm two-column index of linked cards.
colors:
  fg-dark: "#E6EDF3"
  muted-dark: "#8B949E"
  amber-dark: "#E3B341"
  fg-light: "#1F2328"
  muted-light: "#59636E"
  amber-light: "#9A6700"
typography:
  ghost:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "158px"
    fontWeight: 600
  display:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "100px"
    fontWeight: 600
    letterSpacing: "-1.6px"
  title:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "56px"
    fontWeight: 600
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "31px"
    fontWeight: 400
  label:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "30px"
    fontWeight: 500
  status:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "28px"
    fontWeight: 500
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "26px"
    fontWeight: 400
rounded:
  cell: "2px"
spacing:
  grid-cell: "10px"
  grid-pitch: "14px"
  card-gutter: "44px"
  text-inset: "2px"
  handle-gap: "14px"
components:
  project-card:
    textColor: "{colors.fg-dark}"
    typography: "{typography.title}"
    width: "640px"
    height: "250px"
  project-card-description:
    textColor: "{colors.muted-dark}"
    typography: "{typography.body}"
  project-card-status:
    textColor: "{colors.amber-dark}"
    typography: "{typography.status}"
  banner-name:
    textColor: "{colors.fg-dark}"
    typography: "{typography.display}"
  banner-identity:
    textColor: "{colors.muted-dark}"
    typography: "{typography.label}"
  banner-handle:
    textColor: "{colors.muted-dark}"
    typography: "{typography.mono}"
  handle-square:
    backgroundColor: "{colors.amber-dark}"
    size: "12px"
  grid-cell:
    backgroundColor: "{colors.fg-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-busiest:
    backgroundColor: "{colors.amber-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
---

# Design System: Inbathamizhan S

## Overview

**Creative North Star: "Inbam"**

He is named in his own language first. The banner sets இன்பத்தமிழன் as a quiet, full-width ground behind the Latin name, at a whisper of the text colour, and the Latin name, identity line and handle sit over it. The work follows as a calm two-column index: eight linked cards, each a hairline rule, a title and one plain sentence. Nothing is boxed, filled or shadowed; GitHub's own page shows through every image.

The system lives entirely inside committed SVG and PNG files, because GitHub's sanitizer strips every stylesheet and script from the README. Each image carries its own subset fonts, its own dark and light twin, its own phone layer and its own motion. One amber marks what is live: the handle, the project he is building now, and his busiest days. Secondary tones are never new hues; they are the theme's text colour at a lower opacity.

Motion arrives once and settles: the Tamil ghost slides in slowly, the grid and the small web fade in together, the name and identity rise, then each card's rule draws across in reading order with its text rising after it. Afterwards only Aran's amber dot keeps pulsing.

**Key Characteristics:**
- Tamil name first, as a full-width ghost (fg at 7% dark, 6% light) behind the Latin name.
- Transparent images on GitHub's unpainted grounds, in matched dark and light twins.
- Hind Madurai throughout; JetBrains Mono only for the handle.
- One amber, reserved for what is live or current.
- Hairline rules instead of boxes; flat, no shadows.
- Once-only entrance motion with a single loop, and reduced-motion fallbacks in every SVG.

## Colors

GitHub's own text greys plus one warm amber, each defined twice (dark theme, light theme) and swapped with `<picture>` and `prefers-color-scheme`; the page ground itself is never painted.

### Primary
- **Live Amber** (amber-dark / amber-light): the only accent. The 12-unit square before the handle, Aran's lowercase "now" and its pulsing dot, and the busiest days (fourth quartile) in the contribution grid, at full opacity. The light twin is a deeper ochre so it holds contrast on white.

### Neutral
- **GitHub Ink** (fg-dark / fg-light): the Latin name and card titles at full strength. Every quieter tone in the system is this ink at an opacity: the Tamil ghost (.07 dark, .06 light), the grid steps (.06, .14, .26, .42), the corner web (.25), and the card rules (.28 dark, .40 light).
- **GitHub Slate** (muted-dark / muted-light): the identity line, the handle and card descriptions.

### Named Rules
**The Unpainted Ground Rule.** No image paints a background. Every SVG and PNG is transparent so it sits on whatever ground GitHub serves (dark, dimmed, light, high-contrast) without a seam.

**The One Amber Rule.** Amber marks only what is live: the handle square, the current project's "now" and dot, and the busiest grid days. A second accent, or amber used for decoration, breaks the system.

**The Opacity, Not Hue Rule.** Quieter tones are the theme ink at an opacity, never a new grey or a new colour. That is what lets one file read on every GitHub ground.

## Typography

**Display Font:** Hind Madurai (Tamil and Latin), subset and embedded as woff2, with sans-serif fallback
**Body Font:** Hind Madurai
**Label/Mono Font:** JetBrains Mono, for the handle only (ui-monospace fallback)

**Character:** One family carries both scripts, so the Tamil and Latin names read as the same voice at two volumes; the monospace handle is the single nod to code.

Sizes are SVG user units; they scale with the image's rendered width (banner 1280 wide, cards 640 wide).

### Hierarchy
- **Ghost** (600, 158): the Tamil name, edge to edge across the banner at fg .07 / .06, aria-hidden.
- **Display** (600, 100, -1.6px tracking): the Latin name over the ghost's lower half, set 5 units left of the column edge as an optical overshoot.
- **Title** (600, 56, -0.01em): card titles. A title that would overflow shrinks to fit (two long titles run at 72 instead of 80 in the phone layer).
- **Body** (400, 31): card descriptions in muted, at most two lines (line advance 54.3 at the phone size of 46).
- **Label** (500, 30): the identity line, with the Tamil run in Hind Madurai Tamil 500.
- **Status** (500, half the title size: 28, or 40 in the phone layer): Aran's lowercase "now" in amber, on the title baseline.
- **Mono** (JetBrains Mono 400, 26): the handle.

### Named Rules
**The Tamil First Rule.** The Tamil name comes before the Latin one, in reading order and in motion: it is the ground the Latin name sits on.

**The Embedded Type Rule.** Every SVG embeds its own subset woff2 fonts as base64. GitHub serves images through `<img>`, which loads no external fonts. A glyph missing from the subset is drawn, not substituted: DHṚTI's underdot is a circle (r 3.1 at 56) because Hind Madurai has no U+1E5A.

## Layout

The README column (~830 px desktop, ~350 px phone) is the only grid. Images are full width or exactly half.

- **Banner** (1280 × 430, `width="100%"`): handle top-left (amber square at x 0, text 14 units after it); Tamil ghost at y 205; Latin name baseline y 300; identity line y 362 with "Team Iravora Void" right-aligned at x 1156 to clear the web; contribution grid in the top-right (18 weeks × 7 days, origin 1034,40, pitch 14, cell 10, ending at the right edge); the small web in the bottom-right 100 × 100 corner.
- **Project cards** (640 × 250, `width="50%" align="top"`): two per row, written back to back with no whitespace between the links so the pair never wraps. The 88-unit gutter is built into the art: left-column cards rule from x 0 to 596 with text at x 2; right-column cards rule from 44 to 640 with text at 46. Title baseline y 96, description y 150; the last row also carries a bottom rule at y 249.
- **Toolbox**: one sourced PNG strip (976 × 64, displayed at 488 for 2×).

### Phone layer
Media queries inside an SVG respond to the image's rendered width, not the viewport. Each file carries a `.desk` and a `.phone` group:
- Banner at `max-width: 520px`: handle and identity rise to 52, the amber square to 22, and "Team Iravora Void" moves to its own line (y 420); the Tamil run leaves the identity line.
- Cards at `max-width: 300px`: title 80 (shrinking to fit), status 40, description 46 wrapped to at most two lines.

### Named Rules
**The Half-Width Pair Rule.** Cards are exactly 50% wide, paired with no whitespace between them, and carry their own gutter inside the art. Never rely on Markdown spacing for layout.

**The Rendered-Width Rule.** Phone legibility is solved inside each SVG with a width media query keyed to that image's own rendered size; there is no page CSS to do it.

## Elevation & Depth

Flat. No shadows, no fills, no boxes. The only depth is typographic: the Tamil ghost at a whisper of the ink sits behind the full-strength Latin name, and the grid and web recede at low opacity.

### Named Rules
**The Flat Paper Rule.** Nothing casts a shadow or sits in a panel. Separation comes from hairline rules, opacity and space.

## Shapes

Square and hairline. Rules are 2-unit straight lines with butt ends. Grid cells are 10-unit squares with a 2-unit corner; the handle mark is a sharp 12-unit square. The one curved form is the small spider web: five radial spokes and four sagging spiral threads, 1-unit strokes at ink .25, confined to the banner's bottom-right corner.

## Components

### Project Card
Quiet and typographic: a rule, a title, one sentence.
- **Rule:** 2-unit hairline across the top, ink at .28 (dark) / .40 (light); bottom rule on the last row only.
- **Title:** Title style in ink; **Description:** Body style in muted, at most two lines.
- **Link:** the whole card is one `<a>` to its repo; the `<img>` alt is "Title: description".
- **Motion:** the rule draws across (1 s, `stroke-dashoffset` on `pathLength="1"`), the text rises 10 units after it (0.8 s, +0.15 s); cards stagger 0.09 s in reading order from 0.20 s.

### Current Project Card (Aran)
The same card plus the system's only status: lowercase "now" in amber at half the title size on the title baseline, and a 7-unit amber dot at the card's right edge (584, 76) whose ring pulses (scale 1 to 3, opacity .5 to 0, 2.6 s, starting at 2 s). The ring is the one infinite animation in the profile; with reduced motion the ring is hidden and the static dot stays.

### Banner
Handle, Tamil ghost, Latin name, identity line, live grid and web, as one transparent 1280 × 430 image with dark and light twins.
- **Motion:** ghost slides in from -28 units (2.2 s); grid and web fade in as one group (1.6 s, from 0.5 s); handle, name and identity rise 12 units (0.9 s at 0.15, 0.35, 0.55 s). All use `cubic-bezier(.16,1,.3,1)`; nothing loops.

### Contribution Grid
GitHub's own graph, redrawn: 18 weeks, Sunday on top, rewritten daily by `scripts/update_grid.py` (GitHub Action) as static rects between `<!--grid-->` and `<!--/grid-->` in both banner files. Levels: none .06, first quartile .14, second .26, third .42 of the ink; fourth quartile in amber at full opacity. The cells carry no per-cell animation.

### Handle Mark
A sharp 12-unit amber square before `@itzz-inbathamizhanS` in JetBrains Mono, muted.

### Toolbox Strip
A single sourced PNG of 13 skill-icons logos (MIT, licence committed beside it), dark and light variants, with its provenance in a `tEXt` chunk. The logos are the only icons in the system.

### Named Rules
**The One Loop Rule.** Entrance motion plays once and settles; Aran's pulse is the only loop. Every animated SVG ends with a `prefers-reduced-motion` block that removes the animation and leaves the final state visible.

**The Grid Contract Rule.** The `<!--grid-->` markers, the grid origin (1034, 40), pitch 14, cell 10, radius 2 and the five-level palette live in both banner SVGs and in `scripts/update_grid.py`. Change one, change both.

**The One Link Per Image Rule.** An image can carry one link and no hotspots; every project is its own image, linked to its repo.

## Do's and Don'ts

### Do:
- **Do** ship every visual as a transparent SVG or PNG pair (dark and light) inside `<picture>` with `prefers-color-scheme`, with real alt text on the `<img>`.
- **Do** embed subset Hind Madurai (and JetBrains Mono for the handle) as base64 woff2 inside each SVG, and draw any glyph the subset lacks.
- **Do** derive quiet tones from the theme ink at an opacity: ghost .07/.06, grid .06/.14/.26/.42, web .25, rules .28/.40.
- **Do** keep amber for what is live: handle square, the current project's "now" and pulse, and the busiest grid days.
- **Do** solve phone legibility inside each SVG with a media query on its own rendered width (banner 520, cards 300).
- **Do** keep animated elements few and grouped (the grid and web fade as one group), with a reduced-motion fallback in every file.
- **Do** keep the grid markers and geometry in step with `scripts/update_grid.py`.

### Don't:
- **Don't** paint a background, box, panel or shadow behind any content; GitHub's ground always shows through.
- **Don't** add a second accent colour or a new grey; use the ink at an opacity.
- **Don't** add a second loop; Aran's pulse is the only one.
- **Don't** add tags, eyebrows or labels above titles; the lowercase "now" on the baseline is the only status.
- **Don't** add icons outside the Toolbox strip, or turn the corner web into a character.
- **Don't** rely on page CSS, scripts, hover states, image maps or external fonts; none survive GitHub's sanitizer or `<img>`.
- **Don't** put whitespace between paired card links; it breaks the two-column row.
