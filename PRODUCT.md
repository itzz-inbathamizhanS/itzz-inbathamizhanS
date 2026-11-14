# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

GitHub profile README (`README.md` in the `itzz-inbathamizhanS/itzz-inbathamizhanS` repo), rendered by GitHub's Markdown sanitizer. No CSS or JavaScript survives on the page; every visual is an SVG or PNG committed under `assets/`, swapped for dark and light themes with `<picture>` + `prefers-color-scheme`. SVG animation (CSS keyframes inside the SVG) plays because GitHub serves the images through `<img>`. A GitHub Action (`.github/workflows/update-grid.yml` → `scripts/update_grid.py`) rewrites the banner's activity grid daily from real contribution data.

## Users

Everyone who lands on the profile, weighted equally:
- recruiters and hiring teams checking him for internships and security roles;
- hackathon judges and teammates who just saw one of his projects;
- the wider security and open-source community.

They arrive from a link (a repo, a LinkedIn post, a hackathon submission) and skim for under a minute, often on a phone, in GitHub's dark or light theme.

## Product Purpose

Inbathamizhan S's front door on GitHub. In about 20 seconds a visitor should (1) remember him as distinct, (2) open his projects, and (3) know how to contact him. Success is all three, not one at the expense of the others.

## Positioning

A third-year B.Tech CSE student at KARE (Madurai) who builds working security systems across unusual ground for a student: post-quantum cryptography (Q-CAPS, DHṚTI), forensics (Hybrid DFIR), deception and threat defence (Q-Lure, Kavach), zero-trust networks, and data protection for Indian banks (Aran, current). Most were built at hackathons with his team, Iravora Void.

## Operating Context

GitHub profile page beside the pinned repos and the contribution graph; also opened from the GitHub mobile app. Images scale to the README column (~830 px desktop, ~350 px phone). Links work only on whole images or text; an image cannot carry several hotspots.

## Capabilities and Constraints

- Only Markdown + sanitized HTML (`<picture>`, `<img>`, `<a>`, `<p align>`, `<sub>`, `<br>`, tables). No custom CSS, hover states, scripts, iframes or image maps.
- SVGs render inside `<img>`: no external fonts or images, so fonts are subset and embedded as base64; animation must be CSS inside the SVG, kept to a few animated elements (dozens of separately animated groups dropped pixels in testing).
- The activity grid lives between `<!--grid-->` markers in both banner SVGs and is rewritten by the Action; any banner redesign must keep that contract or update the script with it.
- Commits go straight to `main`, credited to Inbathamizhan S, with no AI attribution lines.

## Brand Commitments

Kept by explicit choice (do not drop):
- intro line, his own words: "A 3rd-year CSE student venturing into Cybersecurity with a growing technisoul.";
- the real contribution grid in the banner and its daily refresh;
- a quiet spider-web motif (nod to his Spider-Verse side; plain web shape, never a character);
- the Toolbox as a row of logos (skill-icons, MIT), not names;
- the closing quote, exactly: "If it is meant to be, it will happen ❤️✨!!!";
- name "Inbathamizhan S", handle `@itzz-inbathamizhanS`, "B.Tech CSE · KARE · Madurai, India", "Team Iravora Void";
- every project row links to its repo.

Tried and rejected (do not bring back): a recognition/awards timeline, an animated Aran data-flow strip, a pixel-art portrait from his photo, the banner tagline "Defensive security, post-quantum cryptography, forensics.", hover effects that cannot exist on GitHub.

Voice: minimal, plain, no buzzwords, no emoji except in his quote. He asked for "minimal, unique, newer, animated".

## Evidence on Hand

- Repos: Aran (current; live console aran-console.vercel.app), Q-CAPS, DHṚTI (`dhriti`), Hybrid DFIR (`HybridDFIR`), Q-Lure (`QLure`), Kavach (`kavach`), Zero-trust campus (`zero-trust-smart-campus-ns3`), The Amazing Web (`the-amazing-web`), IterEV, Mugamoodi.
- Experience: Cybersecurity Engineer Intern, RGreen Technologies (May–Jul 2026, ISO/IEC 27001 work); Technical Supporter, KARE ACM-W (Jun 2025–May 2026).
- Certifications: (ISC)² CC, Palo Alto Networks Certified Cybersecurity Apprentice, Google IT Support, IBM Java Developer, MongoDB Java Developer Path.
- Contact: LinkedIn linkedin.com/in/inbathamizhans, email itzz.inba05@gmail.com.
- No photo, logo or personal mark exists; none may be invented. Hackathon results exist (LinkedIn) but he chose not to show them.

## Product Principles

1. Remembered, then explored, then contacted: the first image earns memory, the work earns clicks, contact is never more than one scroll away.
2. Real over decorative: every moving thing shows something true (his activity, his work), never motion for its own sake.
3. Quiet by default: one accent, one signature motion, room to breathe; minimal is the brief, not a phase.
4. Works in both GitHub themes and on a phone without a single broken or illegible pixel.

## Accessibility & Inclusion

Every image carries real alt text; animation respects `prefers-reduced-motion` inside the SVGs; text inside images stays legible at phone width (≈350 px column) and meets contrast in both themes.
