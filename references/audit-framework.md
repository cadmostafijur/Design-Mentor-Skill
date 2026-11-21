# Audit Framework

For screenshot analysis, "improve this", and full UX audits.

## Contents
1. Before you start
2. Audit process
3. Severity scale
4. Finding format
5. Accessibility checklist
6. Common problems by product type

---

## 1. Before you start

- Confirm what you actually have: screenshot(s), live URL you can access, code, Figma data, or only a description. Audit only what's available; name what's out of scope ("I can't assess interaction states, load time or keyboard behavior from a static screenshot").
- Establish the screen's job and the user's goal. A finding only matters relative to that goal.
- Match feedback to the stage. For an early concept, focus on concept, flow and hierarchy and skip pixel polish. For pre-launch, focus on states, accessibility, consistency and edge cases. Ask about the stage only if you can't tell.
- From screenshots, colors and sizes are estimates. Say "appears to be ~3:1, verify with a contrast checker" rather than stating an exact ratio.

## 2. Audit process

Pass through the interface in this order — earlier layers have bigger impact:

1. **First impression & purpose** — what draws the eye in the first 2 seconds (is it the right thing)? Within 5 seconds, is it clear what this is and what to do?
2. **Information architecture & flow** — is content organized by user need? Are the steps logical? Any dead ends?
3. **Visual hierarchy** — does emphasis match importance? Is there one clear primary action?
4. **Layout & spacing** — alignment, grid, consistent spacing, grouping by proximity.
5. **Typography** — scale consistency, readability, line length, contrast.
6. **Color** — semantic and consistent use; accent restraint; contrast.
7. **Components & consistency** — same pattern for same purpose; states present.
8. **Interaction & feedback** — affordances, loading/error/empty/success states, undo.
9. **Accessibility** — checklist below.
10. **Responsive** — what happens on other sizes (if evidence available; otherwise recommend).
11. **Content** — labels, microcopy, error messages, jargon.

Also note **strengths** — what works and should be preserved.

## 3. Severity scale

| Severity | Meaning | Example |
|---|---|---|
| **Critical** | Blocks task completion or excludes users; legal/accessibility risk | CTA invisible on mobile; form unusable by keyboard; text 2:1 contrast |
| **High** | Significant friction, errors or drop-off on a core task | Ambiguous pricing; no error message on failed payment |
| **Medium** | Noticeable inefficiency or confusion; hurts trust/polish | Inconsistent button styles; cluttered dashboard header |
| **Low** | Cosmetic / minor inconsistency | 4px misalignment; mixed icon styles |

Prioritize with **impact × frequency × effort**: quick wins (high impact, low effort) first.

## 4. Finding format

```
### [#] Short title — Severity
**Observed:** what is visible/true (location on screen).
**Why it matters:** user impact, tied to the goal or a principle/heuristic/WCAG criterion.
**Recommendation:** specific change (values, tokens, copy, pattern).
**Effort:** low / medium / high
```

End an audit with:
- **Top priorities** — the 3–5 changes to make first, in order.
- **What's working** — keep these.
- **Validate** — what to test with users or check with tools.

For an "improve this" request, follow findings with the revised design: updated layout/wireframe and specs.

## 5. Accessibility checklist (WCAG 2.2 AA essentials)

**Perceivable**
- [ ] Text contrast ≥4.5:1 (large ≥3:1); UI components & focus indicators ≥3:1 (1.4.3, 1.4.11)
- [ ] Information not conveyed by color alone (1.4.1)
- [ ] Images have meaningful alt text; decorative images are hidden (1.1.1)
- [ ] Text resizes to 200% / reflows at 320px width without loss (1.4.4, 1.4.10)
- [ ] Captions/transcripts for media (1.2)

**Operable**
- [ ] Everything works by keyboard; no traps (2.1.1, 2.1.2)
- [ ] Visible focus indicator; focus not obscured by sticky headers (2.4.7, 2.4.11)
- [ ] Logical focus order matching visual order (2.4.3)
- [ ] Target size ≥24×24px (2.5.8); practical default 44px
- [ ] No drag-only interactions without an alternative (2.5.7)
- [ ] Skip link; descriptive page titles; meaningful link text (2.4.1, 2.4.2, 2.4.4)
- [ ] Motion can be paused/reduced; nothing flashes >3/s (2.2.2, 2.3.1)

**Understandable**
- [ ] Visible labels for inputs, not placeholder-only (3.3.2)
- [ ] Errors identified in text with suggestions (3.3.1, 3.3.3)
- [ ] Consistent navigation and component behavior (3.2.3, 3.2.4)
- [ ] Don't ask users to re-enter info already provided (3.3.7); accessible authentication — no cognitive tests without alternative (3.3.8)

**Robust**
- [ ] Semantic HTML first; ARIA only to fill gaps; correct name/role/value for custom widgets (4.1.2)
- [ ] Status messages announced via live regions (4.1.3)

### Testing sequence

Recommend this order, and say which steps you could actually do yourself and which the user still needs to do:

1. **Automated scan** (axe DevTools, Lighthouse, WAVE). It catches only around 30–40% of issues, so passing it doesn't mean the page is accessible.
2. **Keyboard only:** Tab and Shift+Tab through everything; Enter/Space activate; Esc closes; focus always visible and in logical order; no traps.
3. **Screen reader:** VoiceOver (macOS/iOS), NVDA (Windows), TalkBack (Android). Check headings, landmarks, labels, and that dynamic updates are announced.
4. **Contrast:** compute every text/background and UI pair (`python scripts/contrast.py "#fg" "#bg"`), including hover, disabled-looking and placeholder text.
5. **Zoom & reflow:** 200% browser zoom and a 320px-wide viewport, with no loss of content or horizontal scrolling.
6. **Reduced motion and forced colors** (Windows High Contrast).

### Accessibility report format

| # | WCAG criterion | Issue (location) | Severity | Fix |
|---|---|---|---|---|

Contrast table:

| Pair (fg / bg) | Used for | Ratio | Required | Result |
|---|---|---|---|---|

Then **Priority fixes** (in order) and **Needs manual testing** (what couldn't be verified from the material given).

## 6. Common problems by product type

**SaaS dashboard:** KPI cards without context (no comparison, period or target); charts chosen for looks over the question; everything same weight; no "what should I do next"; filters that reset; tables without sort/sticky headers.

**Landing page:** vague headline (says what it is, not what it does for me); multiple competing CTAs; social proof buried; no product visuals; long forms; slow hero media.

**E-commerce:** low-quality/insufficient product images; price, shipping and returns hidden until checkout; forced account creation; unclear stock/size; checkout with distractions; error messages that clear the form.

**Admin panel:** dense tables with no hierarchy; destructive actions next to common ones; no bulk actions; poor empty/permission states; cryptic system terms.

**Mobile app:** small tap targets; key actions out of thumb reach; hamburger hiding primary destinations; no offline/slow states; keyboard covering inputs.

**Forms/onboarding:** asking for too much upfront; no progress indicator for multi-step; unclear password rules shown only after failure; no save/resume.
