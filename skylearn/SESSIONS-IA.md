# skyLearn Sessions: research, audit and information architecture

Instructor-led training. Why the schedule and the session detail hold what they hold. The
visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What an ILT session is for in this product

Most of skyLearn is online. Sessions exist for the competencies that cannot be: a Hoyer lift
transfer, a two-person assist, CPR, a fire drill, a medication pass watched by a supervisor,
dementia de-escalation practised on a colleague. You cannot certify any of those from a video.

That has one consequence which shapes the whole module:

> **The attendance record is the compliance artefact.**

For an online course the system knows who finished, because it watched them. For a session it
knows nothing until a human says who was in the room. Until that happens the training did not
occur, as far as Ohio, Texas, Florida or a state surveyor is concerned. **An unmarked session is
not an administrative loose end, it is a hole in the record.**

So the module is not "a calendar with a roster". It is a worklist whose unit of work is
*closing a session*, and every design decision below follows from that.

## 2. Who this is for

**The training coordinator**, the same administrator as the dashboard. Their three jobs, in the
order the screen supports them:

| Job | Where it lives |
|---|---|
| Close out what already happened | Attendance due group, pinned to the top |
| Run what is happening today | Today group, in-progress status, attendance table |
| Fill and protect what is coming | Seats column, seats-at-risk KPI, waiting list |

The instructor is a secondary user who needs one session, on a phone, in a room. That is a
separate surface and is not designed here.

## 3. Audit of the screen being replaced

Not a style critique. These are the reasons it could not do the job.

**Status was a stored word, not a fact.** The one session on the screen finished on 6 August and
still called itself `scheduled` on 17 August. Nothing anywhere said its attendance was eleven
days overdue. A backlog that the system cannot see is a backlog that never gets worked.

**`Mark Completed` was the primary action and it was always enabled.** It sat in the header,
amber, next to Edit, on a session where not one of the three learners had been marked. Pressing
it would have closed a session with no attendance record: the exact outcome the module exists to
prevent, one click away, styled as the recommended thing to do.

**Attendance was a tick and a cross with no third state.** Once you looked away you could not
tell "absent" from "nobody has been through this yet". There was no "excused", which is the
common real case, and the bulk buttons were disabled with no explanation of what would enable
them.

**`COURSES · ALLOTTED TO NO-SHOWS`** is a good mechanism written as a database column. It means
*if you do not turn up, you get the online version instead.* Nobody reading that heading would
know that.

**The date was ambiguous and the time was a machine artefact.** The list said `6/8/2026`, which
in a US-facing product reads as 8 June; the session was 6 August. The detail said the class ran
`02:32 PM – 06:30 PM`. Nobody schedules a class at 2:32. That is the moment the record was
created, saved as the schedule.

**`(UTC)` on an in-person class in California.** Seven hours out for every person who has to
attend it.

**A list is the wrong default for a temporal object.** No grouping, no today, no this week.
Nothing said what was happening now, next, or already missed.

**`3 / 50` was a number pair with no consequence.** Nothing flagged that an instructor was about
to teach a nearly empty room, and there was no waiting list for the sessions where the opposite
is true.

**Filters counted their own options.** `All Sessions (1)` and `All Modes (1)` show how many
choices the dropdown has, which reads as a result count.

**An instructor was also a registrant.** Anjali Deshmukh taught the session and appeared on
its roster. Nothing noticed.

**Hours did not exist anywhere.** The single most valuable output of a session in a state that
counts hours was absent from both screens.

## 4. What replaced them

### The schedule

The schedule is the toolbar and the table, nothing above them.

**Status describes the session, not the coordinator's to-do list.** The first pass got this
wrong. It put *Attendance due* in the status column, which is a task wearing a status badge, and
the row then said the same thing three times over: an amber group banner, the badge, and
`11 days ago, not recorded` under the time. Sumit called out both the repetition and the label.
He was right on both counts, and the second point is the more interesting one.

The lifecycle is now the standard one every ILT system uses:

| Status | Means |
|---|---|
| **Scheduled** | Booked, has not started |
| **In progress** | Running right now |
| **Ended** | The clock ran out. Not the same as completed. |
| **Completed** | Attendance marked and hours credited |
| **Cancelled** | Called off, with a reason |

**The default view is the worklist, not the archive.** Completed and cancelled sessions are
history and sit behind the Status filter. That is what keeps the statuses actually on screen down
to **Scheduled and In progress**, which is the pair Sumit asked for, plus **Ended** for the case
that made this module necessary.

*Ended* is the one word worth defending. Sumit's proposal was two statuses only. But a session
whose clock ran out with no record is neither scheduled nor in progress, and calling it
*Scheduled* eleven days later is precisely the bug the module exists to fix. *Ended* states a
fact about the session and leaves the task to the button beside it.

**Rows are in plain chronological order.** Once history is filtered out by default, the sessions
that owe a record are simply the oldest rows, so they lead the table without a pinned banner
putting them there. Group headers are dates and nothing else. The backlog is now signalled once,
by the only thing that can act on it: **the row's control becomes a solid `Take attendance`
button**, always visible, where every other row shows a chevron on hover.

**One control per row.** Three hover icons became one, matching the learners table. Reminders and
duplication live on the session itself, where there is room to say what they will do.

### One session

**`Mark completed` left the header.** It is the action that credits the hours, so it now lives at
the foot of the attendance table, with the evidence, and it is **disabled until every learner is
marked**. Disabled it explains itself:

> *3 still unmarked. Closing now would record them as neither present nor absent, which is the
> same as no record at all.*

Enabled it states the consequence before you commit:

> *Closing credits 8.0 hours to 2 learners and issues Fancy. The 1 no show gets enrolled in HIPAA
> Training, due seven days from the session date.*

**Attendance has three states plus unmarked.** Present, no show, excused. Unmarked rows carry an
amber edge, so the outstanding work is visible down the side of the table at a glance. Pressing
the same state again clears it. **Mark everyone present** is offered as the standing shortcut,
because the real-world flow is *mark the room, then flag the exceptions*, not twenty individual
decisions.

**The no-show rule is a sentence:** *If someone does not attend, they are enrolled in HIPAA
Training online, due seven days after this session.*

**The screen reads its own data and says what it finds.** On the original session it raises three
things nobody asked it to:

- Anjali Deshmukh is teaching this session and is also on the roster → *Remove from the roster*
- It finished 11 days ago and nobody has been marked, 12.0 hours are uncredited
- It starts at 2:32 PM, which is not on a quarter hour: check the schedule was not saved from the
  moment the record was created

The last one is a rule, not a hardcoded note. Any session whose start is off a quarter hour
raises it.

**Times are local and named.** `2:32 PM – 6:30 PM PT`, with the community's state carried on the
place. **Dates are spelled with the month in words**, everywhere, because `6/8/2026` was wrong by
two months.

**Hours are rounded once, at the source.** 2:32 to 6:30 is 3.97 hours. If the card rounds to 4.0
and the close-out multiplies 3.97, two learners come to 7.9 and the arithmetic on screen looks
broken. Caught in verification, fixed in `hrs()`.

**Waiting lists exist**, with *move up* enabled only when a seat is actually free.

**Cancelling requires a reason**, because the reason is what the learners are told.

### New session

**A session is an instance of a course that already exists.** Nothing is authored here: the
course, its content and its hours were written in Create course. This only says *when, where and
who*. That is a scheduling job, and scheduling jobs are short, so it is **a dialog, not a
stepper** — the four-step stepper in Create course would be pure overhead for seven fields.

The fields are in the order the decision is actually made: course, then date and times, then mode,
instructor, place and seats.

**The panel under the fields is the point of the screen.** A blank form asks the coordinator to
already know everything. This one answers, live, the three questions that decide whether the
session is worth booking:

> *23 learners are overdue on Safe Resident Handling, 14 of them at Lakeside Manor.*
> *2.0 hours, credited to Safe Resident Handling. Runs during the day shift.*
> *No evening or night session for this course in the last 90 days. Staff on those shifts cannot
> attend a class they are required to take.*

Three domain problems are checked here rather than left to memory:

**Double booking.** The instructor and the room are both checked against every other session that
overlaps. *Priya Raghavan is already teaching Medication pass observation, 7:00 AM to 9:00 AM.*
These **warn, they do not block**: a room genuinely does get split between two halves of a group,
and a coordinator who is told and proceeds meant it.

**Shift coverage.** Senior living runs 24 hours. A class at nine in the morning trains the day
shift and nobody else, and "training is always scheduled when I am asleep" is the oldest complaint
in the sector. The dialog reports which shifts a course has not been taught to in 90 days, derived
from the schedule rather than typed. And the fix is one press: **Also schedule for evening shift /
night shift** creates the same class at 3:00 PM and 11:00 PM, same room, same length. One dialog,
three shifts covered.

**A room is physical.** A skills lab has one lift, which is why it holds 16 and the training room
next door holds 50. Booking a hands-on course into a room with no equipment, or 40 people into a
16-person lab, is flagged.

Only genuinely invalid data is refused: no course, or an end time before the start.

On create it opens the new session, so the obvious next step, assigning the learners who are
overdue, is one click away.

### Removed: the KPI row and the calendar view

Both shipped in the first pass and **Sumit removed both**. Recorded here rather than quietly
dropped, because the reasoning may need revisiting rather than repeating.

The KPI row was four cards: sessions this week, attendance not recorded, seats at risk, and hours
credited. Two of them doubled as filters. The argument for them was that *three unmarked sessions*
is a count an administrator can ignore whereas *sixty-two uncredited hours* is not.

Nothing was lost that the screen cannot still say. **The backlog is not hidden**: overdue sessions
are pinned to the top of the table under their own amber group header, which is a stronger signal
than a number in a card, and the Status filter still isolates them. The compliance framing, hours
uncredited until attendance is marked, now lives where the work is done, in the close-out bar at
the foot of each session's attendance table. If the count is wanted back later, the dashboard is
the honest home for it: that screen is already the organisation-wide exception view, and Sessions
is a worklist.

The calendar was a month grid, on the argument that room and instructor conflicts are spatial
questions. If scheduling conflicts turn out to be a real complaint, the answer is more likely a
conflict warning at the point of booking than a second view of the same twenty rows. The
day-grouped schedule already answers *what is happening today*, which is the question this screen
is actually opened for.

## 5. Sample data

Twenty sessions across August and early September 2026, all derived from the same 44-person
roster as the assign and learners screens, so a name means the same person everywhere.

**The session from your screenshots is kept exactly as it was recorded** — the 2:32 PM start, the
`CA` location, the `Fancy` certificate, the instructor on his own roster. The new screen is worth
judging on what it makes of real data, not tidy data.

The other nineteen cover the cases the single-session screen could not show: a class running
right now, a full room with three people waiting, a session with nobody booked at all, one at
2 of 16 seats four days out, a cancellation with a reason, and five properly closed sessions
whose present-counts are what add up to the 218 hours in the KPI.

## 6. Verified

Headless, since the preview renderer has been dead for this project and every visual check has
come from your screenshots.

- Phase computed from the clock: the original session reads *Attendance due, 11 days*; the 8am
  class today reads *In progress* at 9:40; the 2pm class today still reads *Scheduled*
- Close-out disabled at 0 of 3 marked, enabled at 3 of 3, crediting 8.0 hours and enrolling the
  one no show
- Overdue attendance leads the table by date order alone, with no pinned banner, and the Status
  filter still isolates those 3 sessions
- The phrase "Attendance due" appears nowhere; each row states the backlog once, as an action
- 7 chevrons plus 3 Take attendance buttons across the 10 rows on page one
- Every detail state renders: overdue, running, empty, cancelled, closed, waitlisted
- Class audit clean in both directions. It found `.stack-4`, which did not exist in the design
  system and which `course-create.html` had quietly reinvented locally. Added to `dashboard.css`.

## 7. Open questions

1. **Who is allowed to close a session?** The instructor who taught it, the coordinator, or
   either? It writes compliance hours, so it may want to be the narrower of the two.
2. **Can attendance be edited after closing?** *Reopen* exists here, but a surveyor may expect an
   amendment trail rather than a silent edit.
3. **Does an excused absence still trigger the online fallback course?** Currently no. That is a
   policy decision.
4. **Are session hours capped per requirement?** If somebody attends the same Hoyer lift class
   twice, do they earn 4 hours or 2?
5. **Should over-booking be allowed?** Every operator over-books ILT against a known no-show
   rate. Right now capacity is hard.
