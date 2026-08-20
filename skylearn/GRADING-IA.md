# skyLearn Grading Hub: research, and what it became

The screens read 0 Pending, 0 Graded, 0 Returned, and *No submissions found.* That is not a
seeding problem. **It is correct, and it always will be**, until somebody builds an assignment
unit. The visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The evidence

### There is nothing to grade

In `course-create.html`, the file that defines what a course can contain:

| word | occurrences |
|---|---|
| `grade` | **0** |
| `grading` | **0** |
| `essay` | **0** |
| `assignment` | 2 — both meaning *course assignment*, as in "learners see this name in their assignment list" |
| `submission` | 2 — both meaning *an instructor submitting a course for admin review* |

There is no unit type that produces learner work for a human to mark. A course is video, reading
and auto-marked questions. **The Grading Hub was a queue with no producer.**

### Meanwhile, thirty decisions are outstanding and have no queue

From the same 44-person roster every other screen uses:

| | |
|---|---|
| Never assessed for competency | **7** |
| Assessed and **below the 75 threshold** | **23** |
| Courses submitted for approval | **3** |
| **Waiting on a person** | **33** |

The dashboard already prints *"N of M ninety day checks passed. Pass threshold 75."* and
`learners.html` shows each learner's three domain scores. **Nothing anywhere let you enter one.**
The number arrived from nowhere, and nobody could see who was owed a check.

The failures cluster, which is itself worth knowing: **23 below on *Judgment and people skills***,
11 on *Standards and communication*, 5 on *Knowledge and compliance*.

### In senior living the thing needing a person is a check-off, not an essay

The catalogue asks people to *do* things: *Applying a Wrist Restraint: A Competency-Based…*,
*Safe Lifting and Transfers*, *Safe Resident Handling*, *CPR and First Aid*. A preceptor watches
and signs. That is the regulated judgement in this domain, and it was invisible.

### Two vocabularies for one idea

The screens split into Assignments and Activities, and the two branches used different words for
the same thing: **Pending / Graded / All** against **Pending / Approved / Rejected**. *Returned*
was counted in a KPI card you could not filter to. The Activities tab also repeated its own name
as an `h2` with a second subtitle, and the KPI cards appeared on one tab but not the other.

## 2. What it became

> **One inbox for everything waiting on somebody's judgement, oldest first.**

Three kinds of work, one shape, one vocabulary — **Waiting** and **Decided**:

| Kind | Yes | No |
|---|---|---|
| Competency check | Pass | Refer |
| Course review | Approve | Send back |
| Submission | Accept | Return |

The decision verbs differ because a course is not "passed" and a person is not "approved", but
the queue states do not. *Submissions* renders as an empty filter today rather than a dead tab —
the shape is there for when an assignment unit exists.

### This is where a competency score is entered

The gap the research found. Three domain sliders, and **the 75 threshold is drawn on the track**
rather than left in a footnote — a number you have to remember is a number people get wrong.

**Pass is disabled while any domain is below 75.** Asserted: 72/68/61 blocks, 80/80/80 allows,
80/74/80 blocks. You cannot pass somebody through a threshold the compliance report will later
say they failed.

### Age is the sort, and the headline

*"33 waiting on a decision. The oldest has been there 41 days."* Anything past 21 days turns red.
A queue sorted alphabetically makes you read all of it to find the one that matters.

### Every decision states its consequence

Buttons whose effect is invisible get clicked twice and trusted once:

> Pass is unavailable while 3 domains are below 75. Refer sends Dana back to *Safe Resident
> Handling* and tells their manager.

> Approving publishes it and tells Priya Raghavan. Sending it back returns it to draft so they
> can edit, and nobody else sees it.

The course panel also surfaces what review is *for*: one of the three has **5 objectives stated,
3 covered**, flagged before you approve rather than after it reaches 44 people.

## 3. Verified

Headless, since the preview renderer has not responded for this project.

- Queue reconciles with the roster: 7 never assessed and 23 below threshold, both derived, both
  matching `PEOPLE` exactly
- **No person appears in the queue twice**, and no duplicate ids
- Sorted oldest first, asserted across the whole list — 41 days down to 3
- Every filter and every state renders tag-balanced, with no `undefined` / `NaN`: 4 kind filters,
  3 state filters, both competency panels, all 3 course panels
- Pass gating asserted at the boundary, including the one-domain-below case
- Deciding clears the item: waiting 33 → 32, outcome recorded, scores written
- Class audit clean both directions; brace balance checked on all 17 pages
- All 17 pages parse and serve 200; nav byte-identical, 12 items plus Help

## 4. On the name

Kept as **Grading Hub**, matching your product — the same call you made for Automations. It is
worth saying once that the name now describes the one thing the module does not do: nothing here
is graded. *Review queue* is what it is. Not worth a rename on its own, but if the module is ever
renamed, that is the reason.

## 5. Open questions

1. **Who is allowed to pass somebody?** A competency sign-off is a regulated act. Today any
   admin can. It probably needs a named assessor, and their name on the record.
2. **Should a referral create the re-check automatically?** Refer sends them back to training;
   nothing schedules the second attempt.
3. **Is 75 right, and is it one threshold or three?** Still unanswered from
   [`REPORTS-IA.md`](REPORTS-IA.md) §5. *Judgment and people skills* fails 23 of 37 assessed —
   either the workforce has a real problem there or that domain is scored differently.
4. **Does an assignment unit get built?** If it does, this queue already has the shape for it.
5. **The 90-day clock is invisible.** Passing "starts the next ninety day clock" but nothing
   shows when checks fall due, so the queue only fills once they are late.
