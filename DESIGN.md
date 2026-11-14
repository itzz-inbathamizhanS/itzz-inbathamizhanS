---
name: Inbathamizhan S
description: A GitHub profile drawn as one living spider web, with Aran at the hub and every project caught on its threads.
colors:
  amber-dark: "#E3B341"
  amber-light: "#9A6700"
  ink-dark: "#E6EDF3"
  ink-light: "#1F2328"
  tag-dark: "#8B949E"
  tag-light: "#59636E"
  silk-dark: "#8B949E"
  silk-light: "#8C959F"
  seed-silk-dark: "#3D444D"
  seed-silk-light: "#C8D1DA"
  ground-dark: "#0D1117"
  ground-light: "#FFFFFF"
  grid-none-dark: "#161B22"
  grid-q1-dark: "#2A313C"
  grid-q2-dark: "#57606A"
  grid-q3-dark: "#8B949E"
  grid-none-light: "#EFF2F5"
  grid-q1-light: "#D1D9E0"
  grid-q2-light: "#8C959F"
  grid-q3-light: "#59636E"
typography:
  display:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "84px"
    fontWeight: 600
    letterSpacing: "-1.2px"
  headline:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "54px"
    fontWeight: 600
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "46px"
    fontWeight: 600
    letterSpacing: "-0.01em"
  label:
    fontFamily: "Hind Madurai, sans-serif"
    fontSize: "30px"
    fontWeight: 500
    letterSpacing: "0.08em"
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "28px"
    fontWeight: 400
rounded:
  cell: "2px"
  hairline: "1px"
spacing:
  grid-cell: "10px"
  grid-pitch: "14px"
  banner-inset: "64px"
  label-cutout: "16px"
  tile-width: "430px"
  tile-height: "260px"
components:
  web-name:
    textColor: "{colors.ink-dark}"
    typography: "{typography.title}"
  web-name-light:
    textColor: "{colors.ink-light}"
    typography: "{typography.title}"
  web-name-hub:
    textColor: "{colors.ink-dark}"
    typography: "{typography.headline}"
  web-tag:
    textColor: "{colors.tag-dark}"
    typography: "{typography.label}"
  web-tag-light:
    textColor: "{colors.tag-light}"
    typography: "{typography.label}"
  web-tag-now:
    textColor: "{colors.amber-dark}"
    typography: "{typography.label}"
  web-tag-now-light:
    textColor: "{colors.amber-light}"
    typography: "{typography.label}"
  web-node-hub:
    backgroundColor: "{colors.amber-dark}"
    size: "18px"
  web-node-hub-light:
    backgroundColor: "{colors.amber-light}"
    size: "18px"
  web-dew:
    backgroundColor: "{colors.amber-dark}"
    size: "7px"
  banner-name:
    textColor: "{colors.ink-dark}"
    typography: "{typography.display}"
  banner-name-light:
    textColor: "{colors.ink-light}"
    typography: "{typography.display}"
  banner-identity:
    textColor: "{colors.tag-dark}"
    typography: "{typography.mono}"
  banner-identity-light:
    textColor: "{colors.tag-light}"
    typography: "{typography.mono}"
  banner-handle-mark:
    backgroundColor: "{colors.amber-dark}"
    size: "12px"
  banner-handle-mark-light:
    backgroundColor: "{colors.amber-light}"
    size: "12px"
  grid-cell-none:
    backgroundColor: "{colors.grid-none-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q1:
    backgroundColor: "{colors.grid-q1-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q2:
    backgroundColor: "{colors.grid-q2-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q3:
    backgroundColor: "{colors.grid-q3-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q4:
    backgroundColor: "{colors.amber-dark}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-none-light:
    backgroundColor: "{colors.grid-none-light}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q1-light:
    backgroundColor: "{colors.grid-q1-light}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q2-light:
    backgroundColor: "{colors.grid-q2-light}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q3-light:
    backgroundColor: "{colors.grid-q3-light}"
    rounded: "{rounded.cell}"
    size: "10px"
  grid-cell-q4-light:
    backgroundColor: "{colors.amber-light}"
    rounded: "{rounded.cell}"
    size: "10px"
---

# Design System: Inbathamizhan S

## Overview

**Creative North Star: "The Web He Spins"**

The profile is one spider web drawn in silk on GitHub's own ground. Aran sits at the hub in the only warm colour on the page; every other project is caught on a thread, named in Hind Madurai (the typeface named for his city) with a tracked uppercase tag beneath it. There are no cards, borders, panels or shadows. Structure is thread: radials, rings and the nodes where they meet. The banner above it is the same world at rest: his name, his handle, a real contribution grid and a small web seed spinning in the corner.

Everything is an image, because GitHub's sanitizer strips CSS and scripts from the page. Each visual is an SVG (or a sourced PNG) with its fonts subset and embedded, swapped between dark and light through `<picture>` and `prefers-color-scheme`. The images carry no background of their own: the README sits on whichever GitHub ground the visitor uses (dark `#0D1117`, light `#FFFFFF`, and the dimmed and high-contrast variants), so every drawn colour has to hold on all of them.

Motion is the web being built once, then two quiet loops: the hub breathing and a single dew drop travelling one thread. Every animated element has a `prefers-reduced-motion` fallback that leaves the finished web standing still.

**Key Characteristics:**
- One web, one hub, one warm accent; everything else is cool grey silk and ink.
- Thread is the only structure: no boxes, cards, borders, halos or shadows.
- Labels are cut out of the silk with an SVG mask, so threads stop short of the type instead of running through it.
- Silk is translucent grey so the same file reads on every GitHub ground.
- The 3x3 mosaic is one scene viewed through nine windows; each window is one link.
- Build-once motion, then only two loops, always with a reduced-motion fallback.

## Colors

Cool, almost colourless silk and ink on GitHub's own ground, with one amber that marks what is live.

### Primary
- **Hub Amber** (`amber-dark` / `amber-light`): the hub of the web, its NOW tag, the travelling dew point, the banner's handle square, the banner's one-pass sweep over the grid, and the grid's busiest days (fourth quartile). The light value is a deeper ochre so it holds contrast on white.

### Neutral
- **Ink** (`ink-dark` / `ink-light`): project names in the web and the banner name. GitHub's own primary text colours, so the images sit in the page as if typeset by it.
- **Tag Grey** (`tag-dark` / `tag-light`): uppercase area tags under each project and the banner's mono handle and identity lines.
- **Silk** (`silk-dark` / `silk-light`): every radial, ring and node ring in the web. Always drawn with stroke opacity, never solid: dark radials at .30 and rings at .19; light radials at .48 and rings at .32. Node rings are full-strength silk at 2px.
- **Seed Silk** (`seed-silk-dark` / `seed-silk-light`): the solid 1px hairline of the banner's corner web seed.
- **GitHub Grounds** (`ground-dark` / `ground-light`): never painted by the system; recorded so contrast is checked against them.
- **Grid Greys** (`grid-none-*` to `grid-q3-*`): the contribution grid's first four levels. These values are owned by `scripts/update_grid.py`, which rewrites the grid daily; change them there, not in the SVG.

### Named Rules
**The One Warm Thing Rule.** Amber marks only what is live or current: the hub, NOW, the dew, the handle square, the sweep, the busiest days. No project name, tag, thread or heading is ever amber.

**The Translucent Silk Rule.** Web threads carry their grey through stroke opacity, not a mixed solid, so one file reads on dark, dimmed, high-contrast and light grounds alike.

**The Script Owns the Grid Rule.** The grid palette lives in `update_grid.py`; any colour change to the grid is made in the script and both banners together.

## Typography

**Display Font:** Hind Madurai 600 (fallback sans-serif), subset and embedded
**Label Font:** Hind Madurai 500, tracked uppercase
**Mono Font:** JetBrains Mono (fallback ui-monospace, SFMono-Regular, Menlo), banner only

**Character:** A humanist Tamil-heritage sans for the names, set tight and confident; the same family, smaller, wider-tracked and in capitals for tags. Mono appears only where the content is literally a handle or an identity line.

Sizes are SVG user units. The web scene is 1290 wide and the banner 1280 wide; both scale to the README column (about 830px desktop, about 350px phone), so 46 units renders near 30px on desktop and 12.5px on a phone.

### Hierarchy
- **Display** (600, 84, tracking -1.2px): the banner name, once.
- **Headline** (600, 54, -0.01em): Aran at the hub. It must outrank every satellite.
- **Title** (600, 46, -0.01em): each project name on the web.
- **Label** (500, 30, 0.08em, uppercase): the area tag under each name (THREAT INTEL, FORENSICS, NOW). Sits 40 units below its name; NOW sits 38 below the hub name.
- **Mono** (400, 28): the banner handle `@itzz-inbathamizhanS`, the identity line and the team line.

README prose, headings and lists are GitHub's own type and are not restyled.

### Named Rules
**The Phone Floor Rule.** Names never go below 46 units and tags never below 30 in a 1290-wide scene; at phone width that is the smallest legible size, so new labels shorten rather than shrink.

**The Mono Is Data Rule.** JetBrains Mono is for the handle and identity lines in the banner only. Tags on the web are Hind Madurai, because mono there would be costume, not data.

**The Embedded Glyph Rule.** Fonts are subset to the glyphs used. When the subset lacks a mark (the underdot in DHṚTI), it is drawn as geometry in the label's ink (a 2.6-unit dot), never left out silently and never pulled from a system font.

## Layout

The page is GitHub's single README column. The system controls three images inside it, in order: banner, web, toolbox.

- **Banner:** 1280 x 320, full column width. Content inset 64 units from the left. Handle and its 12-unit amber square top-left; name on the baseline at 192; identity line bottom-left and team line bottom-right at 266. The contribution grid sits top-right at (968, 56): 18 weeks by 7 days, 10-unit cells on a 14-unit pitch. The web seed hangs from the top-right corner.
- **Web mosaic:** one 1290 x 780 scene drawn once, cut into a 3x3 grid of 430 x 260 tiles, each tile the same scene seen through its own `viewBox` window. Tiles are placed inline in one `<p>` at `width="33.33%" align="top"` with no whitespace between tags, so the seams close. Hub centre at (645, 390). Every project tile links to its repo, the centre tile is Aran, and the bottom-right tile is the unlinked growing corner.
- **Toolbox:** a sourced skill-icons strip (MIT), 976 x 64 at 2x, shown at width 488.

Labels hang above their node (name baseline 70 units above, tag 30 above) or below it for nodes on the lower half; edge labels anchor start or end at 20 units from the scene edge so nothing clips at a seam.

## Elevation & Depth

None. The system is flat: no shadows, no glows behind type, no blur, no layering of surfaces. Depth comes only from thread weight and opacity (radials 1.4 and 1 units alternating, heavier than rings) and from the hub's amber pulse ring expanding outward.

### Named Rules
**The Cut, Not Covered Rule.** Type sits on the web by masking the silk away beneath it (a 16-unit stroked cutout around each label, 7.5 around each node, 13 around the hub). No halos, no background rects, no boxes.

## Shapes

Lines with round caps, circles and a few tiny squares. Nodes are open rings (6.5 radius, 2-unit stroke in silk); the hub is a solid amber disc (radius 9). Rings are not circles but sagging polygons drawn with quadratic curves between radials, as real orb webs sag. The only rectangles are data: grid cells (10 units, 2 corner radius), the 12-unit handle square, and the 2-unit sweep bar.

## Components

### Web Node
Catch point for a project. Open ring, silk stroke, popped in as its ring passes. Name above (Title), tag below the name (Label), both cut out of the silk.

### Hub
Aran. Solid amber disc with a second amber disc pulsing out to 3.4x and fading (2.6s, looping). Name in Headline, NOW in amber Label. Drawn first, before any thread.

### Dew
A single amber drop (radius 3.5) that travels one radial from the hub to the growing corner every 8 seconds, masked by the silk so it disappears behind labels. The only moving thing after the web is built, apart from the hub pulse.

### Contribution Grid
GitHub's activity calendar in miniature, five levels, busiest days in amber with two glow cycles. Cells scale in along a diagonal (delay 0.3s + 0.03s per row and column). Rewritten daily between the `<!--grid-->` markers by `.github/workflows/update-grid.yml`.

### Banner Handle Mark
A 12-unit amber square before the handle that blinks three times (1.1s, stepped) and then stays lit.

### Motion grammar
- **Web build:** radials draw out from the hub (1.1s each, staggered 0.10s to 0.62s), rings spiral in from outermost (1.2s each, from 0.75s, 0.16s apart), nodes pop and labels rise as their ring passes (1.55s to 2.07s). Easing `cubic-bezier(.16,1,.3,1)`.
- **Loops:** hub pulse (2.6s, from 2.2s) and dew (8s, from 3s). Nothing else loops.
- **Banner:** lines rise 10 units and fade in (0.8s, `cubic-bezier(.2,.7,.2,1)`, staggered 0.12s); cursor blinks 3 times; sweep crosses the grid once (6s, from 1.8s); busiest cells glow twice; seed web draws once (0.7s per thread).
- **Reduced motion:** every animation class is switched off and the drawn state is forced (`stroke-dashoffset:0`); the pulse and dew are hidden.

## Do's and Don'ts

### Do:
- **Do** keep every visual an SVG or PNG under `assets/`, in a dark and a light file swapped by `<picture>` and `prefers-color-scheme`; GitHub strips CSS and scripts from the page.
- **Do** subset and embed every font as base64 inside the SVG; images in `<img>` cannot load external fonts.
- **Do** give each image exactly one link and real alt text; an image cannot carry several hotspots.
- **Do** draw silk with stroke opacity (dark .30 radials / .19 rings; light .48 / .32) and test on dark, dimmed, high-contrast and light grounds.
- **Do** cut labels out of the silk with the mask; keep names at 46 units or more and tags at 30 or more in the 1290 scene.
- **Do** keep amber for the hub, NOW, the dew, the handle square, the sweep and the busiest grid days.
- **Do** give every new animation a `prefers-reduced-motion` fallback that leaves its finished state visible, and keep animated groups few.
- **Do** preserve the `<!--grid-->` markers and change the grid palette in `scripts/update_grid.py`.

### Don't:
- **Don't** add boxes, cards, panels, borders, halos, background rects or shadows; structure is thread.
- **Don't** colour a project name, tag or thread amber, or introduce a second accent.
- **Don't** use mono outside the banner's handle and identity lines.
- **Don't** add loops beyond the hub pulse and the dew, or motion that does not show something true.
- **Don't** draw the web as a character; it stays a plain web shape.
- **Don't** design hover states; GitHub cannot show them.
