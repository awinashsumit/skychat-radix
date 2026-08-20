# skyLearn Learners: research and information architecture

Module 6. Why `learners.html` lists people rather than enrollments.

---

## 1. The screen was called Learners and listed enrollments

Nine rows, seven people. Nikhil Raut appeared twice, Devendra Joshi twice, because the unit of
the table was a **learner-course pair**, not a learner.

That makes the obvious question unanswerable. "How is Nikhil doing?" needs you to find his rows,
scan across, and add up in your head. For a director with 1,284 staff, it cannot be done at all.

The KPIs counted enrollments too, so the header and the table agreed with each other and both
answered a question nobody asked.

## 2. Two columns were empty on every row

`Score` and `Due Date` were dashes in 9 of 9 rows. A column blank for every record is not a column,
it is a promise the product has not kept.

**And `Overdue` read 0.** Not because nobody was late, but because no enrollment carried a due
date, so nothing could ever be overdue. The one number a survey asks about was structurally
incapable of being non-zero. That is why due dates were made part of assigning in module 5 rather
than an afterthought.

## 3. One row per person, worst first

Every learner resolves to exactly one state, ordered the way a surveyor cares about them:

| State | Test |
|---|---|
| Certificate lapsed | any expired certification. They cannot work unsupervised. |
| Overdue | any required course past its due date |
| Courses outstanding | assigned work not finished, nothing late yet |
| Expiring soon | compliant, but a certificate lapses within 30 days |
| Compliant | everything current |

The default sort is that order, so the people who need action are the first thing on screen. The
44 states partition the roster exactly, which is asserted, so the KPIs cannot drift from the table
the way the old ones did.

## 4. Not assessed is not zero

The old learner page showed **0% average score** and a **0.0% donut**. Both were false: the learner
had never been assessed. Reporting an un-taken assessment as zero is the difference between "we do
not know" and "they failed", and on a competency record that difference matters.

Seven of the 44 have no competency check yet. They read **not assessed**, and the average is taken
over the 37 who have one, with the card saying so.

## 5. The learner record

The old record led with an Activity chart that was a flat line at 1 with a single blip, a donut
reading 0.0%, and tabs for Gamification and Infographic. None of it answers a question anyone has.

Four tabs now:

- **Overview** — what is outstanding, in the order a surveyor would ask, and the three competency
  domains against the pass threshold. If nothing is outstanding it says so plainly.
- **Courses** — their required training, complete and not.
- **Certifications** — what they hold and when it lapses.
- **Transcript** — every completion with hours and score, exportable. **This is the document a
  survey actually asks for**, so it is a first-class tab rather than the last one.

Points and levels are gone from the record. Gamification is a learner motivator; it is not part of
a compliance history, and a surveyor reading "Lv 1, 69 points" learns nothing.

## 6. Enrolling

**Enroll learners is the page's primary action, and the dialog is the client's**, field for field:

| Field | |
|---|---|
| Course | required, "Select a course" |
| Learner IDs | required, comma-separated IDs or email addresses |
| Due date | optional deadline for course completion |
| Mandatory | mark this as a required course |

Two passes got this wrong before it was left alone. The first replaced the action with a link to
the assign screen, on the argument that enrolling and assigning are the same operation from two
directions. The second brought the action back but swapped the Learner IDs box for a searchable
picker, on the argument that a paste-emails field is a developer's form. **Both were changes the
client had not asked for, and the client preferred the original.** It is restored exactly.

What was kept is behaviour, not chrome. The field parses what its own hint promises, tolerating
spacing and a trailing comma, and matching either an email or a full name. The result then
reports what actually happened rather than claiming a clean run:

> *2 enrolled on Preventing Falls in Senior Living. 1 already had it, skipped. 1 not recognised.
> Due 17/09/2026, marked required.*

Silently dropping a mistyped address, or enrolling somebody twice, are the two ways this dialog
can lose data. Neither is visible in the form, so both are reported in the result.

**Bulk enrolment by role, community or group lives on the assign screen** from module 5. It is a
different job with a different shape, and it stays there rather than being folded into this dialog.
