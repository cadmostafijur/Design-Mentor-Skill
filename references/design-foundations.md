# Design Foundations

Concrete defaults. Deviate when the product has a reason to, and say so.

## Contents
1. Visual hierarchy
2. Typography
3. Spacing & layout
4. Color & contrast
5. Responsive design
6. Touch, pointer & interaction
7. Motion

---

## 1. Visual hierarchy

Hierarchy is created by (strongest → weakest): **size, weight, color/contrast, position, whitespace, grouping**. Use as few levers as necessary — changing size *and* weight *and* color for one element usually means something is fighting.

- One primary action per view. Secondary actions are visually quieter (outline/ghost/text), destructive actions are separated and confirmed.
- Squint test: blur the screen; the first two things you notice should be the most important content and the primary action.
- F-pattern for text-heavy pages, Z-pattern for sparse marketing layouts; dashboards read top-left first — put the most decision-relevant data there.
- De-emphasize labels, emphasize values (e.g. in data displays, the number is larger/darker than its caption).

## 2. Typography

**Type scale.** Pick one ratio and stick to it.

| Use case | Ratio | Example scale (base 16px) |
|---|---|---|
| Dense apps, dashboards | 1.125–1.2 (Major second / Minor third) | 12, 14, 16, 18, 20, 24, 30 |
| General product / content | 1.25 (Major third) | 13, 16, 20, 25, 31, 39 |
| Marketing, editorial | 1.333–1.5 | 16, 21, 28, 38, 50, 67 |

Round to whole pixels or a 4px grid. Most products need 5–7 sizes total.

**Defaults**
- Body: 16px web (14px acceptable in dense data UIs for secondary text), 17pt iOS, 16sp Android.
- Line height: body 1.4–1.6; headings 1.1–1.3; tight UI labels 1.2–1.3.
- Line length: 45–75 characters (≈ `max-width: 65ch`).
- Weights: 2–3 per family (e.g. 400, 500/600, 700). One family is usually enough; two max (e.g. a display face + a UI face).
- Letter-spacing: slightly negative for large headings (−0.01 to −0.02em), slightly positive for small all-caps labels (+0.04 to +0.08em).
- Use tabular numerals for tables, prices and changing numbers.
- Sentence case for UI labels and buttons reads faster than Title Case or ALL CAPS.

**Reliable UI families:** Inter, IBM Plex Sans, Source Sans 3, Roboto, SF Pro / system-ui, Geist. Avoid decorative faces for UI text.

## 3. Spacing & layout

**Base unit.** 4px base with an 8px rhythm is the most flexible:
`0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128`

- **Proximity rule:** space inside a group < space between groups. (e.g. label→input 4–8px, field→field 16–24px, section→section 32–64px.)
- Padding inside components scales with size: small button 8×12, medium 10×16, large 12×20.
- Card padding: 16px mobile, 20–24px desktop. Don't wrap everything in cards — use whitespace and dividers for grouping where a container adds nothing.

**Grids**
| Breakpoint | Columns | Gutter | Margin |
|---|---|---|---|
| Mobile (<640) | 4 | 16 | 16 |
| Tablet (640–1023) | 8 | 24 | 24–32 |
| Desktop (≥1024) | 12 | 24–32 | auto, max content width 1200–1440 |

Content width: reading content 640–720px; app layouts can go full-width but cap line lengths inside.

**Density.** Offer comfortable (default) vs. compact for data-heavy tools; table row height ≈ 48px comfortable, 36–40px compact.

## 4. Color & contrast

**Structure a palette by role, not by hue:**
- **Neutrals** (9–11 steps): backgrounds, surfaces, borders, text. Most of the UI.
- **Brand/primary** (one hue, 9–11 steps): primary actions, focus, selected states, key links.
- **Semantic:** success (green), warning (amber), danger (red), info (blue) — each with a subtle bg, border and strong text variant.
- **Data viz:** separate categorical palette (6–8 distinguishable hues, colorblind-tested), plus sequential/diverging scales.

**Proportion:** roughly 60–70% neutral, 20–30% secondary surfaces, 5–10% accent. If the accent is everywhere it stops meaning "act here".

**WCAG 2.2 AA contrast**
| Element | Minimum ratio |
|---|---|
| Body text (<24px regular / <18.66px bold) | 4.5:1 |
| Large text (≥24px, or ≥18.66px bold) | 3:1 |
| UI component boundaries, icons, focus indicators, chart elements needed to understand | 3:1 against adjacent colors |
| Disabled controls | exempt (but keep them perceivable) |

AAA (7:1 body) is worth targeting for long-form reading or low-vision audiences.

- Never rely on color alone — pair with icon, text, pattern or position (errors need a message, not just a red border).
- Grey text on colored backgrounds often fails; check it.
- Dark mode is not inverted light mode: use dark greys (#0f–#1a range) not pure black, reduce saturation of accents, express elevation with lighter surfaces instead of shadows, re-check every contrast pair.

## 5. Responsive design

Common breakpoints (adapt to content, not devices): `sm 640, md 768, lg 1024, xl 1280, 2xl 1536`.

For each layout, specify what happens per breakpoint:
- **Navigation:** sidebar → collapsible rail → bottom tab bar (≤5 items) or hamburger drawer.
- **Grids:** 4 → 2 → 1 columns; define the order cards stack in.
- **Tables:** prioritize columns; on mobile convert to stacked cards or keep horizontal scroll with a sticky first column. Never shrink text to fit.
- **Forms:** multi-column → single column; keep labels above inputs on mobile.
- **Actions:** primary CTA can become a sticky bottom bar on mobile for long pages/checkout.
- **Modals:** become full-screen sheets on mobile.
- Design mobile first for consumer products; design desktop first for complex B2B tools, then define the mobile subset of tasks.

## 6. Touch, pointer & interaction

- Touch targets: ≥44×44pt (Apple), ≥48×48dp (Material); WCAG 2.2 AA minimum 24×24 CSS px with spacing. Use 44px+ as the practical default.
- Spacing between adjacent targets ≥8px.
- Thumb zone: primary mobile actions in the bottom half of the screen.
- Hover is an enhancement only — nothing essential may depend on hover.
- Feedback timing: <100ms feels instant; 100ms–1s show a state change (button pressed/spinner in button); >1s show progress/skeleton; >10s show determinate progress and allow leaving.
- Optimistic UI for low-risk actions (likes, toggles); confirm or allow undo for destructive ones (undo beats "are you sure?" for reversible actions).

## 7. Motion

Motion should explain (where something came from/went), give feedback, or direct attention. Otherwise skip it.

| Type | Duration | Easing |
|---|---|---|
| Micro (hover, toggle, press) | 100–150ms | ease-out |
| Small transitions (dropdown, tooltip) | 150–250ms | ease-out in / ease-in out |
| Larger (modal, drawer, page) | 250–400ms | standard ease-in-out |

- Animate `transform` and `opacity`, not layout properties.
- Respect `prefers-reduced-motion`: replace movement with fades or remove it.
- No auto-playing parallax, looping decorative animation, or content that flashes >3 times/second.
