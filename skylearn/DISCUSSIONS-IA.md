# skyLearn Discussions: research, audit and information architecture

You asked the right question: *learners can discuss the course and post doubts — so how does an
admin use this?* The answer turns out to change what the screen is. The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. Who posts here, and why

Not a community. The people writing are CNAs, caregivers and housekeepers: hourly, time-pressured,
often on a phone between shifts, many with English as a second language. **Nobody in that job
browses a forum for pleasure.** If they type something it is because they are stuck, or because the
training has just told them to do something that does not match the floor.

Which means almost every post is one of four things, and the administrator's job is **different for
each**:

| What arrives | What the admin should do |
|---|---|
| A question about the content | Answer it |
| The **same** question, from several people | **Fix the lesson.** Do not answer it again |
| A question about the system | Answer it, or fix the help |
| Not a question at all | Route it to a named person, today |

The screen being replaced — a search box over a list, with a New Discussion button — can tell you
none of that. It is a forum viewer. **For an administrator, Discussions is a triage queue.**

## 2. Audit of the screen being replaced

**It is a reader, not a worklist.** Search, a list, and a compose button. Nothing surfaces what is
unanswered, what is repeated, or what is urgent. The admin's only route to their job is reading
every thread.

**Nothing measures time.** In a compliance course, a question like *"the video says two people but
our lift needs three — which is right?"* going unanswered for nine days is a person who has stopped
waiting and asked a colleague instead. That is how a bad practice spreads. There is no clock on the
screen.

**The most valuable signal in the product is discarded.** Discussions is the **only place learners
tell you the training is unclear**. Everywhere else the product measures whether they finished.
Here they say why they could not. A list sorted by recency throws that away.

**The empty state is a dead end.** *"No discussions found. Start a new discussion to get the
conversation going."* An empty forum in a compliance LMS is normal, and telling an administrator to
start a conversation with themselves is not the fix. If nobody is asking, either discussions are
off on every course, or the courses are clear, and the screen should say which.

**Compose is the primary action.** The amber button is *New Discussion*. An administrator's first
job here is almost never to start a thread; it is to answer one.

## 3. The rebuild: one queue, one row per thing

The first version of this screen had **four sections** — escalations, unanswered, asked-more-than-
once, and everything — each a defensible view of the same 16 posts. Sumit's reaction to reading it
was *"exhausted"*, and the measurement backs him up:

> **43 visible items for 16 posts.** Every post appeared **three times**: once in its category,
> once in the unanswered list, once in the full list. 27,402 characters of markup.

The analysis was not the problem. The sections were. Four true things about a post do not need four
places on the page; they need one row that says all four.

**So: one list. Each post appears exactly once. The row carries its own classification.**

| | |
|---|---|
| **43 items → 9 rows** by default | |
| 27,402 → 10,789 chars of markup | a third |
| Every post rendered 3× → **1×** | |

The biggest single saving is that **a group of people asking the same question is now ONE row**,
not four rows plus a summary card. The row says *"4 people asked this"* and carries both group
actions.

Sorting is by what it costs to ignore: escalations, then groups (most leverage — one lesson fix
answers everybody), then singles oldest-first.

### And the coloured edges went too

Each row carried a coloured bar down its left side — red for an escalation, amber for a group —
next to a tag that already said *Needs a person* in red, with a red icon. Sumit's note was that the
alert already covers it, and he is right: that is the same fact three times, in the same colour, an
inch apart.

The classification lives in the tag and only there. The one visual treatment left on a row is
dimming for answered ones, which is a different job — it de-emphasises rather than classifies, and
those rows only appear in search results anyway.

### And then the filters went too

The rebuild shipped with three chips: **Needs you / Answered / All**. Sumit asked whether "Needs
you" was needed at all. It was not, and checking why turned up a bug:

- **"All" only ever appended.** The list is already sorted with everything outstanding first, so
  the first nine rows of *All* were byte-identical to *Needs you*. The chip added two answered rows
  at the bottom and nothing else.
- **A chip for the default state is not a filter, it is a label.** *Needs you* was selected on
  arrival and was where you wanted to be.
- **The chips broke search.** Search ran *after* the chip filtered, so searching from the default
  view for a question somebody had already answered returned **"Nothing matches" for a post that
  exists**. Looking up a past answer is the main reason to search a discussion board.

So there are no chips. **The page is the worklist**, and the answered ones are something you look
up rather than browse:

- Default: the things that need you, nothing else.
- **Search spans everything**, answered included, and says so: *1 result across all 11 discussions,
  answered ones included.*
- One quiet line under the list: *2 answered discussions not listed. Search finds them.*

That is one screen with one job and one escape hatch, instead of one screen with three modes.

### An answered group leaves the queue

A defect the rebuild's own verification caught: a group whose questions had all been answered was
still sitting in *Needs you*, because answering does not make the lesson any clearer. That is true
but useless — **a worklist that cannot be emptied stops being read.**

It now moves to *Answered*, keeps the *Fix the lesson* button, drops *Answer all*, and changes what
it says:

> *4 people asked this, answered* · *answered, but the lesson still made 4 people ask*

The content signal survives without blocking the queue.

## 3b. What each row does

Three kinds, in order of what it costs to ignore them.

### Not a question (4)

Some of what arrives is an incident report, a staffing problem or a supervisor contradicting the
policy, posted in the only box the person had. From the sample:

> *"Someone was hurt doing a transfer last month on our floor and nothing changed. Is this course
> the response?"* → Director of Nursing
> *"My charge nurse told me we do not need the gait belt for short transfers. The course says
> always."* → Director of Nursing
> *"There is only one of us on nights so a two-person transfer is not possible."* → Scheduling
> *"We do not have the medium sling the course shows."* → Facilities

These need a named human today, not a reply in a thread. In this sector, getting that wrong is how
an injury becomes a citation. Each is matched by what it says and routed accordingly, and the post
**stays visible here too**, so nobody thinks it vanished.

### Waiting for an answer (14)

Oldest first, with the age in amber past three days and red past seven. A question nobody answered
is somebody unsure about something they are required to know.

### Asked more than once (2)

**This is the finding the old screen threw away.** When several people ask the same thing about the
same lesson, the lesson is unclear:

> **4** people asked the same thing about **Safe Resident Handling**, lesson 3.
> Between them the questions have been open 25 days, and none has an answer.

The primary action on that card is **Fix the lesson**, not Reply. Answering four people
individually treats a content defect as a support queue, and the fifth person will ask tomorrow.
*Answer all 4 at once* exists beside it, because the questions are still owed an answer today.

And the card does not disappear when you answer them. It changes what it asks for:

> *All answered. The lesson is still the one that made 4 people ask, so the next person to reach it
> will ask too.*

### Everything, newest first

The client's original list, kept, with the search.

## 4. A bug the verification caught, twice

*Answer all 4 at once* first filtered on course and lesson only. Five posts share Safe Resident
Handling lesson 3, and the fifth is *"there is only one of us on nights so a two-person transfer is
not possible"* — the staffing escalation. **Pressing the button would have closed it with a stock
answer**, taking it off the queue that was about to route it to Scheduling. The filter now matches
the topic as well, and the simulation asserts that the fifth post is untouched.

## 5. Verified

Headless, since the preview renderer has been dead for this project.

- 14 unanswered from 16 posts, oldest at 11 days
- 2 clusters found by traversal: 4 on Safe Resident Handling lesson 3, 3 on CPR and First Aid
- 4 posts routed, to three different people, by what they say rather than by a tag
- Escalations render above the queue, the queue above the clusters, the plain list last
- Answering a cluster clears exactly 4 from the queue, leaves the escalation routed, and turns the
  cluster card into the "still unclear" state
- Class audit clean in both directions
- After the rebuild: 16 posts produce 11 queue entries and 9 rows by default; every post appears
  exactly once; answering a group of 4 drops *Needs you* from 9 to 8 and leaves the staffing
  escalation on the same lesson untouched

## 6. Open questions

1. **Who is the routing target in a real customer?** *Director of Nursing*, *Scheduling* and
   *Facilities* are placeholders. These need to be roles the customer configures, and probably a
   notification rather than a hand-off inside the LMS.
2. **Should the escalation rules be visible and editable?** They are currently a fixed list of four.
   A customer will want to add their own, and will want to know why a post was flagged.
3. **Are discussions on by default per course?** If they are off everywhere, this screen is empty
   for a reason nobody can see from here.
4. **Who else can answer?** Right now this is an administrator's screen. The instructor who taught
   the session is usually the better answer, and the LPN on the floor is often the fastest.
5. **Does anything close the loop back to the learner?** If a question causes a lesson to be
   rewritten, the four people who asked should be told.
