# skyLearn Messages: research, and why there is no inbox

You asked whether we need this before building anything. The answer we landed on: **the
conversation is needed, the inbox is not.** The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The evidence

### The empty inbox has a one-line cause

The compose dialog asks for **"Recipient user ID (UUID)"**.

You have to paste a UUID to write to somebody. No name, no search, no picker. Nobody —
not an administrator, and certainly not a CNA between shifts — knows another user's UUID. It is a
developer placeholder that shipped.

The inbox is not empty because people do not want to talk. **It is empty because nobody can
address a message.** Same class of finding as the Grading Hub having no producer: the screen was
correct about its own emptiness.

Meanwhile every one of the 44 people already has a work email address in the roster.

### Five places something can already arrive

| | |
|---|---|
| The bell, top right | unread count on every page, currently 3 |
| Discussions | a learner asks, an admin answers, per course |
| Automations | reminders and escalation ladders, by email and in-app |
| Grading Hub | refer and approve, each stating who is told |
| Surveys | the app asks, the person answers |

Messages would have been the sixth, and the one competing directly with the email people
actually read.

### But the need is real, and narrow

Three conversations have nowhere to go today, and all three are about **one person's record**:

- *"You have failed the transfer check twice — is something going on?"*
- *"I cannot do the lifting course, I hurt my back."*
- *"Your competency check is Thursday at 2pm, day room."*

None can sit in a per-course public thread. Discussions cannot hold them. Automations only ever
speaks system → person.

### The argument that decided it

A free-text private channel inside a healthcare app **will** attract resident detail. Somebody
will type a name and a diagnosis into it. This product *teaches HIPAA*; giving it an unmonitored
channel with no retention policy is a real hazard, not a hypothetical one. Discussions at least
has moderation and escalation routing. A direct message has neither.

## 2. What it became

> **No inbox. The conversation lives on the record it is about.**

A fifth tab on the learner record, beside Overview, Courses, Certifications and Transcript.
Same pattern the last three modules landed on: attach it to the thing it concerns.

That buys four things a standalone inbox could not:

| | |
|---|---|
| **Addressing** | you are already looking at the person, so there is nobody to look up |
| **Context** | the thread sits next to their overdue courses and competency scores |
| **Retention** | it is part of the training record, and goes wherever that goes |
| **Visibility** | the panel says so: *anyone who can open this learner can read it* |

### Nobody faces a blank page

Threads open themselves from what already happened. A referral out of the review queue writes the
first message, quoting the domain and the score against the threshold:

> **Sumit Awinash** · Administrator · *from the review queue*
> Referred back to training after the ninety day check. Judgment and people skills came out at
> 61, against a threshold of 75.

**25 of 44 records** have a thread on that basis — 23 referred plus 10 overdue, overlapping. The
remaining 19 are quiet because nothing has happened to them, which is the honest reason for an
empty state.

The review queue's own opener is marked as such, because *the system said this* and *a person
said this* are different facts.

## 3. Verified

Headless, since the preview renderer has not responded for this project.

- **220 renders** — all 44 learner records × 5 tabs — every one tag-balanced, no `undefined` /
  `NaN` / `[object Object]`
- Thread seeding reconciles with the roster: 25 records, exactly the union of *referred* and
  *overdue*
- The composer is labelled and Send starts disabled; the quiet-record empty state renders
- Class audit clean both directions; the two duplicate selectors are `@media` overrides
- Brace balance checked across all 17 pages
- All 17 pages parse and serve 200; nav unchanged at 12 items plus Help

## 4. Out of scope, at your call

**PHI handling.** We agreed to leave it this pass. Written down so it is not lost: the panel
says the thread is kept with the training record rather than being private mail, which is
honest but is not a control. Whoever owns compliance should decide whether the composer needs a
warning, whether anything watches for resident detail, and what the retention period is. That
decision belongs with them, not with this screen.

## 5. Open questions

1. **Can a learner start a thread?** Today the admin does, and the learner replies. *"I hurt my
   back"* is a conversation the learner needs to open, and there is no learner-side surface here.
2. **Who is notified when something is written?** It lands on the record silently. That probably
   wants an Automations rule, which is the module that already owns telling people things.
3. **Is the learner record the only place a thread belongs?** A session has the same shape —
   *"you missed the CPR session, here is the next one"* — and it is not on anyone's record yet.
4. **Nothing can be edited or withdrawn.** For a training record that is arguably correct, but it
   should be a decision rather than an omission.
