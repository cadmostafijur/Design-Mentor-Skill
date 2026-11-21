# Design Systems & Handoff

## Contents
1. Scope it to the team
2. Token architecture
3. Token starter set
4. Component specification
5. State matrix
6. Core component checklist
7. Developer handoff template

---

## 1. Scope it to the team

A two-person startup needs tokens + 10–15 core components documented in code. A multi-product org needs governance, versioning and contribution rules. Ask (or infer) team size and stack before producing a 40-page system nobody will maintain. Default: lean foundations + core components, extensible later.

### Three jobs: create, audit, extend

- **Create:** foundations → tokens (§2–3) → core components (§4–6).
- **Audit** an existing system or codebase. Run `python scripts/token_audit.py <src>` for evidence, then look for:
  - hardcoded colors, spacing and font sizes that bypass tokens
  - near-duplicate values (e.g. #1e293b, #1f2937 and #222 all used as "dark text"), which should be merged
  - naming drift (`btn-primary` vs `PrimaryButton` vs `button--main`; tokens named by appearance)
  - duplicate or near-duplicate components (three modal implementations)
  - missing states (§5) and accessibility gaps (focus, contrast, labels)
  - undocumented components and usage rules
  Report as findings with severity, then a consolidation plan (merge map: old value → token).
- **Extend:** a new pattern must use existing tokens, compose from existing primitives where possible, follow existing naming, and document why it exists and what it trades off. If no existing token fits, propose the new token explicitly rather than hardcoding a value.

## 2. Token architecture

Three layers. Components reference semantic tokens, never primitives directly — that's what makes theming (dark mode, brands) a token swap instead of a rewrite.

```
Primitive   →  Semantic                →  Component
blue-600       color-action-primary       button-primary-bg
gray-900       color-text-primary         input-text
space-4        space-inset-md             card-padding
```

Naming: `category-property-variant-state`, e.g. `color-bg-surface-raised`, `color-border-danger`, `color-text-on-action`. Name by purpose, not appearance (`color-text-muted`, not `color-gray-text`).

## 3. Token starter set

Adjust values to the brand; keep the structure. Example as CSS custom properties:

```css
:root {
  /* Primitives — neutrals */
  --gray-0:#ffffff; --gray-50:#f8fafc; --gray-100:#f1f5f9; --gray-200:#e2e8f0;
  --gray-300:#cbd5e1; --gray-400:#94a3b8; --gray-500:#64748b; --gray-600:#475569;
  --gray-700:#334155; --gray-800:#1e293b; --gray-900:#0f172a;
  /* Primitives — brand (replace) */
  --brand-50:#eff6ff; --brand-100:#dbeafe; --brand-500:#3b82f6;
  --brand-600:#2563eb; --brand-700:#1d4ed8;

  /* Semantic — color */
  --color-bg-canvas: var(--gray-50);
  --color-bg-surface: var(--gray-0);
  --color-bg-subtle: var(--gray-100);
  --color-border-default: var(--gray-200);
  --color-border-strong: var(--gray-300);
  --color-text-primary: var(--gray-900);
  --color-text-secondary: var(--gray-600);   /* 7.6:1 on white */
  --color-text-muted: var(--gray-500);       /* 4.8:1 on white — min for text */
  --color-action-primary: var(--brand-600);  /* 5.2:1 with white text */
  --color-action-primary-hover: var(--brand-700);
  --color-focus-ring: var(--brand-500);
  --color-danger: #dc2626; --color-danger-subtle: #fef2f2;
  --color-success: #15803d; --color-success-subtle: #f0fdf4;
  --color-warning: #b45309; --color-warning-subtle: #fffbeb;

  /* Typography */
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  --text-xs: 0.75rem;  --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.125rem; --text-xl: 1.25rem;  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem; --text-4xl: 2.25rem;
  --leading-tight: 1.25; --leading-normal: 1.5;
  --weight-regular: 400; --weight-medium: 500; --weight-semibold: 600;

  /* Spacing (4px base) */
  --space-1:4px; --space-2:8px; --space-3:12px; --space-4:16px; --space-5:20px;
  --space-6:24px; --space-8:32px; --space-10:40px; --space-12:48px; --space-16:64px;

  /* Radius, elevation, motion */
  --radius-sm:4px; --radius-md:8px; --radius-lg:12px; --radius-full:9999px;
  --shadow-sm: 0 1px 2px rgb(15 23 42 / .06);
  --shadow-md: 0 4px 12px rgb(15 23 42 / .08);
  --shadow-lg: 0 12px 32px rgb(15 23 42 / .12);
  --duration-fast:120ms; --duration-base:200ms; --duration-slow:320ms;
  --ease-out: cubic-bezier(.2,.8,.2,1);

  /* Breakpoints (reference; use in media queries) sm 640 · md 768 · lg 1024 · xl 1280 */
}
```

Offer JSON (W3C Design Tokens format: `{"color":{"text":{"primary":{"$value":"{gray.900}","$type":"color"}}}}`) or a Tailwind `theme.extend` block when that matches the user's stack.

Radius guidance: pick one personality and apply it consistently — sharp (2–4px) for serious/data tools, medium (6–8px) for general SaaS, soft (12–16px) for consumer/friendly. Nested radius = outer radius − padding.

## 4. Component specification

For each component, document:

```
Component:    Button
Purpose:      Trigger an action. Not for navigation (use Link).
Anatomy:      [icon-leading?] label [icon-trailing?]
Variants:     primary · secondary · tertiary/ghost · destructive
Sizes:        sm 32px · md 40px · lg 48px height (touch: ≥44 on mobile)
Tokens:       bg color-action-primary, text color-text-on-action, radius-md,
              padding space-2/space-4 (md), text-sm weight-medium
States:       default · hover · focus-visible · active · disabled · loading
Behavior:     loading keeps width, shows spinner, disables re-submit;
              icon-only buttons require aria-label + tooltip
Content:      verb + noun, sentence case, ≤3 words ideally
Accessibility:<button> element; focus ring 2px offset 2px, ≥3:1;
              disabled uses aria-disabled when it must stay focusable
Do / Don't:   One primary per view · Don't use two primaries side by side
```

## 5. State matrix

Most design gaps are missing states. Check every interactive component against:

| State | Visual | Notes |
|---|---|---|
| Default | base tokens | |
| Hover | slightly darker/raised | pointer devices only |
| Focus-visible | 2px ring, ≥3:1 contrast | keyboard; never remove outlines without replacement |
| Active/pressed | darker, maybe scale .98 | |
| Selected/checked | brand color + non-color indicator (check, weight) | |
| Disabled | reduced contrast, no pointer | explain why if not obvious (tooltip/helper text) |
| Loading | spinner/skeleton, preserve layout | |
| Error | danger border + icon + message | |
| Success | brief confirmation | |
| Read-only | looks like text, still selectable | |

And for data views: **empty (first use / no results / cleared), loading, partial, error, permission denied, overflow (long text, many items, huge numbers)**.

## 6. Core component checklist

Foundations first, then: Button, Link, Input, Textarea, Select/Combobox, Checkbox, Radio, Switch, Form field (label + help + error wrapper), Card, Modal/Dialog, Drawer/Sheet, Toast, Alert/Banner, Tooltip, Tabs, Table, Pagination, Badge/Tag, Avatar, Dropdown menu, Navigation (top/side/bottom), Breadcrumb, Empty state, Skeleton, Spinner/Progress.

## 7. Developer handoff template

```
# [Screen / Component] — Handoff Spec

## Overview
Purpose, user story, link to design file (if provided), status.

## Layout
- Container: max-width, padding per breakpoint, grid columns
- Regions in order (DOM order = reading order = focus order)

## Tokens used
Colors, type styles, spacing, radius, shadows — by token name.

## Components
Each instance: component + variant + size + props; any new component spec'd per §4.
Props table for new components:
| Prop | Type | Default | Values / notes |

## Motion
| Element | Trigger | Property | Duration | Easing | Reduced-motion fallback |

## States & behavior
- Loading: skeleton for X; button spinner for Y
- Empty: copy + illustration? + action
- Error: inline vs. banner; retry behavior
- Validation: when it runs, messages
- Truncation: lines, ellipsis, tooltip/expand
- Interactions: what each click/tap/keyboard action does

## Responsive
| Breakpoint | Changes |
|---|---|
| <640 | ... |
| 640–1023 | ... |
| ≥1024 | ... |

## Accessibility
- Landmarks & headings (h1… order)
- Roles/ARIA for custom widgets
- Labels for icons/inputs
- Focus order, focus management on open/close (modals trap and return focus)
- Keyboard: Tab, Enter/Space, Esc, arrows where applicable
- Live regions for async updates (toasts, errors)
- Reduced motion

## Content
Final copy strings, including errors and empty states.

## Edge cases
Long names, zero/huge values, missing images, slow network, permissions.

## Open questions
```
