# skyLearn Assign: research and information architecture

Module 5. Why `assign.html` is a resolution screen rather than a list of plus buttons.

---

## 1. What the existing screens do

Two tabs on Edit Course. **Users** is a flat alphabetical list of every person in the organisation
with a `+` on each row. **Groups** is the same shape with one group in it, under a column headed
OPTIONS, with pagination reading "1 to 1 of 1".

Three problems:

- **One click per person.** For a tenant with 1,284 learners that is not a workflow.
- **Assignment has no shape.** No due date, no repeat, no notification. But a course with no due
  date can never be overdue, and *overdue* is exactly what a survey looks at. The existing screen
  cannot produce the thing the dashboard reports on.
- **A COMPLETION DATE column that is empty on every row**, and a `+` that says nothing about what
  it will do.

## 2. Assignment is rarely per person

In a compliance product you assign by **role** ("all CNAs"), by **community** ("everyone at Cedar
Ridge"), or by **group**. Individual assignment is the exception, for one person catching up.

So the screen leads with role, community and group, and keeps people as the fourth tab. It opens
with the course's required roles already ticked, because that is the answer nine times out of ten.

## 3. The hard part is who it resolves to

Picking an audience is easy. Knowing who actually receives it is not, and getting it wrong either
double-assigns someone or silently misses them. So the right-hand rail resolves the selection live
and **names every person the system decided to leave out, and why**.

Eight outcomes, each visible with a count and a reason:

| Bucket | What happens | Why |
|---|---|---|
| Will be assigned | assigned | They do not have the course |
| Re-assigned, expired | assigned | Passed once, certificate lapsed. This is the case that must not be skipped. |
| Not required for the role | assigned, flagged | Housekeeping and administrators can take it, but it is written for clinical staff |
| Already assigned | skipped | Nobody gets it twice |
| Already overdue | skipped | Chase the existing assignment rather than stacking another |
| Completed and still valid | skipped | Their certificate is untouched |
| On leave | skipped, with an override | Two people, and a checkbox to include them |
| Deactivated | always skipped | They cannot sign in |

Every selected person lands in **exactly one** bucket, and that is asserted: 44 people in, 44
accounted for.

## 4. Edge cases the dummy data makes real

44 learners across 6 roles, 6 communities and 7 groups, built so none of this is hypothetical:

- **Overlap.** 5 people are in both Care Givers and Night Shift. Selecting both gives 26, not 31.
  A person picked by role *and* by group is still one person.
- **An empty group.** Weekend Relief has no members, resolves to nobody, and disables the button
  rather than reporting success on zero people.
- **3 expired certificates**, which are the reason re-assignment exists.
- **3 already assigned, 2 already overdue, 3 completed and current** — three different reasons to
  skip that would all look identical if the screen only counted.
- **2 on leave and 2 deactivated**, which behave differently: leave is an override, deactivated
  is not.
- **4 non-clinical staff**, allowed but flagged, because silently assigning clinical training to
  a housekeeper is a data-quality problem nobody notices for a year.

## 5. Due date and repeat are part of assigning, not settings

Both live on this screen because they are properties of *this assignment*, not of the course. The
same course assigned to new hires and to annual refreshers has two different due dates and two
different repeats. That is also why time options were removed from the course in module 2.

**Assign automatically to anyone who joins these roles later** is on by default. Without it, every
new hire needs a human to remember, which is the failure the dashboard's "onboarding stalled"
count is measuring.
