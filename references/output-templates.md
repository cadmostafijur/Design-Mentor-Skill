# Output Templates

Use as scaffolding; drop sections that don't apply. Shorter is better when it loses nothing.

## Design from scratch

```
## Summary
[2–3 sentences: what we're designing, for whom, the core approach]

**Assumptions:** [list — invite correction]

## Design direction
[Visual + UX direction in 2–4 sentences, and why it fits the audience]

## User flow
[Entry → steps → success, incl. key unhappy paths]

## Screen layout — [Screen name]
[Text wireframe, top to bottom; mark primary action and emphasis]

## Key components
[Component — variant — purpose — states]

## Tokens (starter)
[Color roles, type scale, spacing — or reference to design system]

## Responsive behavior
| Breakpoint | Layout changes |

## Accessibility
[Specific requirements]

## Next steps
[What to validate / decide / design next]
```

## Text wireframe conventions

```
┌──────────────────────────────────────────────┐
│ [Logo]   Nav · Nav · Nav          [Sign in] │  ← header 64px
├──────────────────────────────────────────────┤
│ H1: Value proposition (text-4xl)             │
│ Supporting line (text-lg, secondary)         │
│ [■ Primary CTA]  [□ Secondary]               │  ← one primary
│ Product screenshot                           │
├──────────────────────────────────────────────┤
│ Logos strip (social proof)                   │
└──────────────────────────────────────────────┘
```
Legend: `■` primary button, `□` secondary, `[ ]` input, `▾` select, `☐` checkbox, `⋯` overflow menu. Annotate sizes/tokens on the right with `←`.

A structured list works too when boxes get unwieldy:
```
1. Header — logo left, 4 nav links, "Sign in" (ghost) + "Start free" (primary) right
2. Hero — H1 / subhead / primary CTA / product image (60% width on desktop, below text on mobile)
```

## Audit / improvement

```
## Summary
[Overall assessment in 2–3 sentences + the single biggest issue]

**Scope:** [what was reviewed; what couldn't be assessed]

## Top priorities
1. ...
2. ...
3. ...

## Findings
### 1. [Title] — Critical
**Observed:** ... **Why it matters:** ... **Recommendation:** ... **Effort:** ...

## What's working
- ...

## Revised design (if "improve" was requested)
[Updated wireframe/spec]

## Validate
- ...
```

## Design system

```
## Summary & principles
[3–4 principles tied to the product, e.g. "Data first: chrome recedes"]

## Foundations
Color (primitive + semantic table with contrast) · Typography scale · Spacing · Radius · Elevation · Motion · Breakpoints

## Tokens
[Paste-ready CSS / JSON / Tailwind]

## Components
[Spec per component: purpose, anatomy, variants, sizes, tokens, states, a11y, do/don't]

## Usage rules
[When to use what; governance light]
```

## Mentorship answer

```
[Direct answer in 1–2 sentences]

**Why:** [the principle]

**Example:** [before → after, concrete]

**When to break it:** [nuance — for intermediate/senior]

**Try this:** [small exercise or next step]
```
