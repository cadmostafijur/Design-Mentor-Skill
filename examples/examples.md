# Worked Examples

Condensed to show the expected depth and judgment, not the full length of a real answer.

---

## Example 1 — Design from scratch (SaaS dashboard)

**User:** "Design a dashboard for a small-business invoicing app."

**Response (condensed):**

> **Summary:** A "what needs my attention" dashboard for owners who check finances a few times a week. It leads with money owed and overdue invoices, not vanity totals.
>
> **Assumptions:** Users are non-accountant owners of 1–20 person businesses; desktop-first with a lightweight mobile view; existing brand color unknown, so I've used a neutral palette with one blue accent. Tell me if any of these is wrong.
>
> **Direction:** Calm and trustworthy: mostly neutral, one accent for actions, semantic red/amber only for overdue/at-risk. Comfortable density, because these users aren't analysts.
>
> **Layout (desktop ≥1024):**
> ```
> Sidebar (240px): Dashboard · Invoices · Clients · Payments · Reports · Settings
> Main
> 1. Header: "Good morning, Sam" · [■ New invoice]
> 2. Attention strip: "3 invoices overdue · $4,820" [Send reminders] (amber banner, only if > 0)
> 3. Summary row (3 stats, not 4 decorative cards):
>    Outstanding $12,400 | Overdue $4,820 (danger text) | Paid this month $8,950 (+12% vs last month)
> 4. Cash-flow chart: paid vs. invoiced, last 6 months, bar chart, 2 series
> 5. Two columns: Recent invoices table (5 rows, status badge + text) | Upcoming due (next 7 days)
> ```
> **Why not a KPI-card grid:** the owner's question is "who owes me and what should I do," so the overdue amount carries an action and leads the page.
>
> **States:** first-use empty state ("Create your first invoice" + sample-data toggle); loading skeletons; chart with <2 months data shows a message instead of a misleading trend.
>
> **Responsive:** <1024 the sidebar collapses to an icon rail; <640 a bottom tab bar (Dashboard, Invoices, +New, Clients, More), the summary stacks, the chart becomes a simple paid/outstanding bar, and tables become cards.
>
> **Accessibility:** status badges carry text ("Overdue"), not color alone; chart has a data-table alternative; amounts use tabular numerals; contrast ≥4.5:1 for all text.
>
> **Next steps:** validate the "attention first" priority with 5 owner interviews; decide whether to send reminders in bulk or one by one.

---

## Example 2 — Screenshot audit (no screenshot attached)

**User:** "Here's my landing page, what's wrong with it?" *(no image or URL attached)*

**Response:**

> I don't see a screenshot or link attached, so I can't review the page itself yet. Could you attach a screenshot (full page, desktop and ideally mobile) or share the URL? If it helps in the meantime, tell me the product and audience and I'll give you the five issues I most often find on landing pages like yours, so you can check them yourself.

*(It doesn't make up findings about a page it hasn't seen.)*

---

## Example 3 — Audit finding format

> ### 1. Primary CTA competes with three other buttons — High
> **Observed:** The hero has "Start free trial," "Book a demo," "Watch video" and "See pricing," all filled buttons in different colors.
> **Why it matters:** With four equal choices, none of them stands out (Hick's law). Visitors who are ready to start have to stop and decide, and this is likely suppressing trial sign-ups, the stated goal.
> **Recommendation:** Keep "Start free trial" as the only filled primary button (brand-600). Make "Book a demo" a secondary outline button, turn "Watch video" into a text link with a play icon under the product image, and move "See pricing" to the nav.
> **Effort:** Low

---

## Example 4 — Design system (fragment)

**User:** "Create a color and type system for our fintech app, React + Tailwind."

> **Principles:** Trust through restraint · Numbers are the hero · State is always explicit.
>
> | Semantic token | Light | Dark | Contrast on surface |
> |---|---|---|---|
> | text-primary | gray-900 #0f172a | gray-50 #f8fafc | 17.9:1 / 17.1:1 |
> | text-secondary | gray-600 #475569 | gray-400 #94a3b8 | 7.6:1 / 6.9:1 |
> | action-primary | blue-600 #2563eb | blue-500 #3b82f6 | 5.2:1 (white text) |
> | positive | green-700 #15803d | green-400 | text + ▲ icon |
> | negative | red-600 #dc2626 | red-400 | text + ▼ icon |
>
> Type: Inter with `font-variant-numeric: tabular-nums` for all amounts; scale 12/14/16/20/24/32/40 (ratio ≈1.25).
> Then a `tailwind.config.js` `theme.extend` block mapping these semantic names, and Button/Input/Amount component specs with full state matrices.

---

## Example 5 — Flow audit (condensed)

**User:** "Here's our trial sign-up: landing → form (name, company, role, team size, phone, email, password) → verify email → tour → dashboard. Too many people drop off."

> **Flow audit:** 5 screens and 7 inputs before the user sees any value.
> - Name, company, role, team size, phone: none of these is needed to create an account. Ask for role later in one optional onboarding question, and drop phone entirely (it's a known drop-off point and sales can ask later).
> - Email verification blocks access to the product. Let users in right away and remind them with a banner.
> - The forced 6-step tour gets skipped anyway. Replace it with an empty dashboard that has one primary action and a sample-data option.
>
> **Result:** 2 screens and 2 inputs to reach the dashboard (was 5 screens, 7 inputs). Mermaid diagram and step table follow.
> **Validate:** track completion at each step before and after the change; an A/B test is worthwhile if traffic is above about 1k sign-ups a month.

---

## Example 6 — Mentorship (beginner)

**User:** "How much space should I put between things? My designs look messy."

> Use a spacing scale based on 8 (8, 16, 24, 32, 48, 64) and only use those values. Messy layouts usually come from random gaps like 13px here and 22px there.
>
> **Why:** Our eyes group things that sit close together (proximity). If the spacing is consistent, the groups are easy to read. If it's random, everything looks loosely related.
>
> **Rule of thumb:** put less space inside a group than between groups. Label to input: 8. Field to field: 16–24. Section to section: 48–64.
>
> **Example:** A card with 12px padding, 20px between the title and body, and 10px between buttons → change it to 16 / 8 / 16. The title now clearly belongs to its body, and the card looks calmer.
>
> **Try this:** Take one screen you've designed, change every gap to the nearest value on the 8-point scale, and compare the two versions side by side.
