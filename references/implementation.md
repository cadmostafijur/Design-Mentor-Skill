# Design → Code

For building UI from a design (Figma, screenshot, wireframe or spec), reviewing UI code for design quality, and keeping the design consistent with what's actually in the codebase.

## Contents
1. Read the project's design context first
2. Getting the source design
3. Build workflow
4. Code quality rules
5. Verify by rendering
6. Anti-generic check
7. Persisting decisions (DESIGN.md)

---

## 1. Read the project's design context first

If you're working in a codebase, look for existing decisions before proposing new ones. Inventing a second palette next to an existing one is the most common way a design system falls apart.

- `DESIGN.md`, `PRODUCT.md`, `docs/design*`, a `README` section on UI
- Token sources: `tailwind.config.*`, `@theme` blocks (Tailwind v4), `tokens.json`, `:root` custom properties, `theme.ts`
- Component library in use (shadcn/ui, MUI, Chakra, Radix, Headless UI…) and the local `components/` folder
- Fonts already loaded; icon set already used

Reuse what exists. Propose a change only when there's a reason (contrast failure, missing state, inconsistency), and say so explicitly. For a quick read on how consistent the current code is, run `python scripts/token_audit.py <src-dir>`.

## 2. Getting the source design

- **Figma link + Figma tools available** (e.g. a Figma MCP server): pull the frame structure, auto layout, variables and component names from it. Exact values from Figma beat values estimated from a screenshot.
- **Figma link, no tool access:** say you can't open it, and ask for a screenshot or exported specs. Don't pretend to have read it.
- **Screenshot only:** estimate values, snap them to the 4/8px grid and the type scale, and list the values you're unsure about.
- **Wireframe or description:** commit to a direction first (see SKILL.md §3), then build.

## 3. Build workflow

1. **Tokens before markup.** Pull colors, type sizes, spacing, radii and shadows into CSS custom properties or the theme config. Round odd values to the grid. Map them to the existing tokens where they match.
2. **Map layout, don't trace pixels.** Auto layout becomes flexbox, two-dimensional arrangements become CSS Grid, and absolute positioning is only for decoration and overlays.
3. **Componentize repetition.** Repeated blocks become components; Figma variants become props (`variant`, `size`), not copy-pasted markup.
4. **Semantic HTML.** One `h1`, headings in order, landmarks (`header`, `nav`, `main`, `footer`), `<button>` for actions and `<a>` for navigation, `<label>` on every input, meaningful `alt`.
5. **Add the states the design left out.** Mockups rarely show hover, focus-visible, active, disabled, loading, error, empty or overflow states. Add them, and list what you added.
6. **Responsive.** Mobile-first media queries; `clamp()` for fluid type and spacing instead of many breakpoints; check at 360, 768, 1024 and 1280px; no horizontal scroll at 360px.
7. **Motion last and minimal.** Animate `transform` and `opacity` only, at 150–300ms, and add a `prefers-reduced-motion` fallback.
8. **Verify** (§5), then **document deviations**: anything you changed from the design and why (e.g. "raised muted text from #9ca3af to #6b7280 for 4.8:1 contrast").

## 4. Code quality rules

- No hardcoded colors or spacing in components; everything references tokens.
- Font sizes in `rem`; line-height unitless.
- Every interactive element has a visible `:focus-visible` style with ≥3:1 contrast.
- Touch targets ≥44px on mobile (padding counts toward it).
- Class and component names describe function (`.price-total`), not appearance (`.big-blue`).
- Use `font-variant-numeric: tabular-nums` on numbers that align or change.
- Images have explicit dimensions or aspect-ratio (prevents layout shift); use `loading="lazy"` below the fold.
- Long text is handled: `min-width: 0` on flex children, truncation or wrapping decided deliberately.
- Dark mode, if supported, swaps semantic tokens and doesn't override components one by one.

## 5. Verify by rendering

Code that hasn't been looked at isn't finished. If you can run it, render the page (dev server, a browser tool, or a screenshot) and compare it with the design at mobile and desktop widths. Check:
- Hierarchy matches the design (squint test)
- Spacing rhythm and alignment
- All states reachable (tab through it with the keyboard)
- Contrast of actual rendered pairs: `python scripts/contrast.py "#fg" "#bg"`
- No overflow or horizontal scroll at 360px

If you can't render, say so plainly and list what the user should check.

## 6. Anti-generic check

Before calling a design or build done, scan for the tells of a design nobody made decisions about, and replace each with a choice that fits the product:

- Purple/blue gradient hero on white, gradient text on headings
- A centered row of three identical cards with emoji or gradient icons
- A row of four KPI cards with no comparison, target or time period
- The same shadow, radius and card treatment on every element
- Glassmorphism or blur with no layering reason
- Every section the same width, alignment and background (no rhythm)
- Lorem ipsum, "Feature One", "John Doe", or vague copy ("Unlock your potential")
- Icon + heading + two lines of text repeated as the only content pattern
- Decorative motion on scroll with no meaning
- Several equally loud CTAs

The fix usually isn't more decoration. It's a clearer hierarchy, real content, and one deliberate visual idea carried through the page.

## 7. Persisting decisions (DESIGN.md)

When you set up or change a product's design direction in a codebase, offer to write a short `DESIGN.md` so future sessions and teammates build on the same decisions instead of starting over. Template in `output-templates.md`. Keep it under ~80 lines: principles, direction, tokens (or a link to them), component conventions, do/don't, open decisions.
