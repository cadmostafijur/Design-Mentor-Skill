# UX Methods

Pick the lightest method that answers the question. Most teams don't need a full research program — they need the right next step.

## Contents
1. Choosing a research method
2. Proto-personas
3. Jobs to be done & journeys
4. Information architecture
5. User flows
6. Usability heuristics
7. Reducing cognitive load
8. Forms
9. UX writing

---

## 1. Choosing a research method

| Question | Method | Effort |
|---|---|---|
| What problems do users have? | 5–8 user interviews | Medium |
| Can users complete this task? | Moderated usability test, 5 users per round | Medium |
| Which version performs better? | A/B test (needs traffic) | Medium–high |
| Where do users drop off? | Funnel analytics, session recordings | Low |
| How do users group our content? | Open/closed card sort | Low–medium |
| Can users find X in our nav? | Tree test | Low |
| What do users think at scale? | Survey (after you know what to ask) | Low |
| Quick sanity check, no users available | Heuristic evaluation, competitor review | Low |

Five users per usability round find most major issues; iterate and test again rather than testing 20 at once.

When the user has no data, say what you're assuming and propose the cheapest validation (e.g. "run 5 unmoderated tests on the checkout prototype before building").

## 2. Proto-personas

Personas without research are hypotheses. Label them **proto-personas** and keep them short and behavioral — demographics rarely drive design decisions.

```
Name / role:        Ops Manager Priya (label, not a stereotype)
Context:            Manages 40-person warehouse team, desktop at work, phone on floor
Goal:               Know by 9am which orders are at risk today
Frustrations:       Data spread across 3 tools; finds problems after customers do
Behaviors:          Checks dashboard 5–10×/day in short bursts; exports to Excel weekly
Tech comfort:       Moderate; power user of spreadsheets
Design implication: Lead with exceptions, not totals; mobile view = alerts only
Validate by:        Interviews with 5 ops managers; analytics on dashboard visit frequency
```

The **design implication** line is the point — a persona that doesn't change a decision isn't useful.

## 3. Jobs to be done & journeys

**JTBD statement:** *When [situation], I want to [motivation], so I can [outcome].*
e.g. "When a shipment is delayed, I want to see which customers are affected, so I can contact them before they complain."

**Journey map** columns: Stage → User actions → Thoughts/questions → Emotion (+/−) → Pain points → Opportunities.
Keep to 4–7 stages. The value is in the opportunities row; tie each to a design change.

## 4. Information architecture

- Start from user tasks and content inventory, not the org chart.
- Use user vocabulary for labels (validate with card sorting or search logs). Avoid internal jargon and clever names.
- Breadth vs. depth: prefer broader, shallower navigation (5–9 top-level items, ≤3 levels) over deep trees.
- Every page should answer: Where am I? What can I do here? Where can I go next?
- Global nav for primary destinations; local nav/tabs for sections; breadcrumbs for deep hierarchies; search when content > ~100 items.
- Group settings by user intent (Profile, Notifications, Billing, Security), not by system.

Sitemap notation (text):
```
Home
├── Projects
│   ├── Project detail
│   │   ├── Overview / Tasks / Files / Settings (tabs)
├── Reports
├── Team
└── Settings (Profile · Notifications · Billing · Security)
```

## 5. User flows

Describe flows as steps with decisions and system responses. Always include the unhappy paths that matter (validation errors, empty data, permission denied, network failure, abandonment/return).

```
[Entry: pricing page CTA]
 → Sign-up form (email, password)  — or "Continue with Google"
     ✗ email exists → inline: "Account exists. Log in?" (link)
 → Verify email (can skip; banner reminds later)
 → Onboarding Q (1 question: role) — skippable
 → Empty dashboard with 1 primary action: "Create first project"
     + sample project option for exploration
[Success: first project created — activation metric]
```

Reduce steps by: deferring non-essential data, using smart defaults, social sign-in, saving progress, and merging screens that ask related questions.

## 6. Usability heuristics (Nielsen, condensed)

1. **Visibility of system status** — show loading, saving, progress, success.
2. **Match the real world** — user language, familiar conventions.
3. **User control & freedom** — undo, cancel, back, exit flows easily.
4. **Consistency & standards** — internal consistency and platform conventions.
5. **Error prevention** — constraints, defaults, confirmation for destructive actions.
6. **Recognition over recall** — show options; don't make users remember from screen to screen.
7. **Flexibility & efficiency** — shortcuts, bulk actions, saved filters for experts.
8. **Aesthetic & minimalist design** — every element competes for attention; remove what doesn't help.
9. **Help users recover from errors** — plain-language message, cause, and how to fix.
10. **Help & documentation** — contextual help at the point of need.

## 7. Reducing cognitive load

- **Progressive disclosure:** show the common 80%, tuck advanced options behind "More options".
- **Chunking:** group related fields/info; 3–7 items per group.
- **Defaults:** pre-select the most common/safest option.
- **Hick's law:** fewer choices at decision points (pricing: 3 tiers, highlight one).
- **Fitts's law:** frequent/important targets are bigger and closer.
- **Familiar patterns** over novel ones unless novelty is the product.
- **Remove decisions:** autofill, remember preferences, infer from context.

## 8. Forms

- Single column; labels above fields; no placeholder-as-label.
- Ask only what's needed now. Mark optional fields ("optional") rather than every required field with asterisks when most are required.
- Right input type (`email`, `tel`, `numeric` keypad), autocomplete attributes, input masks for structured data.
- Validate on blur (not on every keystroke), re-validate on change once in error; summarize errors at top on submit and move focus to the first error.
- Error text: what's wrong + how to fix ("Enter a date after today"), placed below the field, linked via `aria-describedby`.
- Button label states the outcome ("Create account", not "Submit").

## 9. UX writing

- Clear > clever. Front-load the key word. Sentence case.
- Buttons: verb + noun ("Save changes", "Delete project").
- Empty states: what this is, why it's empty, the action to fill it.
- Errors: no blame, no codes alone, no "Oops!". Say what happened and what to do.
- Confirmations for destructive actions name the object and consequence: "Delete 'Q3 Report'? This can't be undone."
