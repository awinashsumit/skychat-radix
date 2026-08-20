# skyLearn Courses list: research and information architecture

Module 4. Why `courses.html` counts what it counts.

---

## 1. The summary row did not add up

The screen being replaced showed four cards:

```
TOTAL COURSES 19    ACTIVE 16    DRAFT 2    TOTAL ENROLLMENTS 9
```

**16 + 2 = 18.** The missing course is Archived, a status the summary row never names. A count
that does not reconcile is worse than no count, because the reader stops trusting the screen and
cannot tell which number is wrong.

Two further problems in four cards:

- **They repeat the table.** Total, Active and Draft are all visible by looking down the Status
  column, and all three are already offered as filters underneath.
- **Total Enrollments is a different unit.** It counts people, in a row of course counts, so the
  eye compares 19 courses with 9 people.

## 2. The KPI row stays as the client has it

A first pass replaced the four cards with exception counts (not reviewed in a year, never
assigned, missing a state topic, drafts) on the argument that a list screen should surface what
needs attention. **The client asked for the original four back, and they are back**: Total
courses, Active, Draft, Total enrollments, with the same coloured left edge and tinted icon tile.
Replacing them was not what was asked for.

The one change is a single line under the total: *including 1 archived*. That is the smallest
thing that closes the arithmetic hole without touching the four cards or their design. Remove the
line and the numbers stop reconciling again.

The exception counts are still computed and still drive the row-level flags under each course
title. They are no longer a summary row. If they are wanted as quick filters they belong in the
toolbar beside Status and Category, not in place of the KPIs.

## 3. Column changes

| Was | Now | Why |
|---|---|---|
| Units | **Modules** | The word settled in module 2. "Units" is dead terminology. |
| Category (own column) | Second line under the title | Frees the title from truncating at 40 characters while Category, Units and Created had fixed width to spare. |
| Enrollments | **Learners** | Shorter, and it names people rather than an event. |
| **Created** | **Last updated** | Created never changes and tells you nothing after week one. For compliance content, when it was last reviewed is the number that carries risk. Shown as a date plus "over a year ago", and the relative line turns amber once it is stale. |

Row flags appear under the title where they apply: *misses a required topic*, *never assigned*.
A fact you can act on belongs next to the thing it describes, not only in a summary card.

## 4. Pagination, which was missing entirely

**First attempt was wrong.** Rows per page was rendered as three buttons, `10 20 50`, sitting
inside the pagination bar. In that position three numbers read as page numbers, so clicking 50
looked like jumping to page 50 and instead made the table taller. Reported, accurately, as
"the pagination is odd, it's expanding".

Now:

- **Rows per page is a dropdown**, matching Status and Category, so it reads as a setting.
- **Real numbered page buttons**, windowed as `1 2 3 … 9` so a long list never grows a hundred
  of them, with the current page solid and marked `aria-current`.
- The range and total sit between the two, and previous/next bracket the numbers.

Sortable headers on Modules, Learners and Last updated, defaulting to most recently updated
first. 24 seeded courses, so pagination genuinely engages rather than being a control that never
fires.

## 5. Other decisions

- **Row actions appear on hover**, matching the module rows in the course builder, and are
  reachable on keyboard focus and always visible on touch.
- **Archive replaces delete.** A course with completion records cannot be deleted without
  destroying evidence, so the destructive action archives and the toast says how many learners
  keep their records.
- **Duplicating produces a draft with no learners**, so a copy can never quietly become live
  training that somebody is assigned to.
- **Bulk actions live in a bar that replaces the toolbar when rows are selected**, which is what
  explains the checkbox column. The old screen had a permanently disabled Bulk Assign button and
  nothing said why.
- **Create course is the single amber CTA**, and it opens the create flow from module 2.

## 6. Navigation correction

Courses in the sidebar previously pointed at the create screen, because the list did not exist.
It now points here, and the create screen is a sub-screen that highlights Courses as its parent
with a `Home > Courses > New course` breadcrumb, per the design system's rule for sub-screens.
