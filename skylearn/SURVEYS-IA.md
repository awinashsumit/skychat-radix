# skyLearn Surveys: research, and what it became

You asked whether this module is needed. **Yes — nothing else in skyLearn asks anyone what they
think.** But the model was wrong in a way that guaranteed it would collect nothing, and the two
rows on the live screen prove it. The visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The evidence

### Two rows, three faults

| | | |
|---|---|---|
| **HIPAA Training** | active, **0 questions**, 0 responses | live with nothing to ask |
| **HIPAA Quiz** | draft, 1 question, 0 responses | a *quiz*, in the survey tool |

**An empty survey could be published**, because Status was a dropdown you set *before* writing a
question. **A quiz was built here**, and `course-create.html:873` already marks correct answers
(`o.ok ? 'Correct' : 'Mark correct'`) while `learners.html` carries `PASS = 75` across three
competency domains — so those answers scored nothing. And **both sat at zero responses.**

### Zero responses was not a mystery

The screen had no Assign, no Send, no attachment. Status flipped draft → active and nothing
happened. Meanwhile the roster holds **428 course completions**; a survey firing on completion
would have collected around 128 replies at a normal 30% rate.

**The audience was never the problem. There was no delivery.**

### But the gap it fills is real

Swept across all 14 pages: no screen collects an opinion or a rating. Discussions captures
*unsolicited* questions. Competency checks measure *knowledge*. `sessions.html` credits hours and
never asks whether the hour was any good. Nobody is ever asked *was that useful?*

And the definition was already on record — from removing Survey from the course builder's Add
menu, [`CREATE-COURSE-IA.md:232`](CREATE-COURSE-IA.md):

> Survey is feedback about a course, collected after it. It is not part of the course.

That settles both halves: surveys are real, **and** they belong attached to something rather than
standing alone with a status you flip by hand.

## 2. What it became

> **A survey attaches to a course, a session or a schedule. The attachment is the delivery, and
> the status is read off it.**

### Status is derived, never chosen

```js
function status(s) {
  if (blockers(s).length) return 'draft';    // no questions, or attached to nothing
  if (!s.sent)            return 'waiting';  // ready, nobody has come through yet
  return s.closed ? 'closed' : 'open';
}
```

The bug that motivated this is now impossible by construction. Carried over as they are, both of
your rows correctly read **draft** — *HIPAA Training* blocked by *"needs at least one question;
needs something to attach to"*. Asserted headlessly: no survey with zero questions can reach a
sendable state.

### Response rate, not response count

*0 responses* out of nought and out of forty are different facts, and the count alone hides which
one you have. Every card shows a rate with a real denominator — the number who finished the
course or attended the session, not the headcount:

- After HIPAA Training — **23 of 38, 61%**
- After an instructor-led session — **16 of 22, 73%**

Asserted: replies never exceed the number asked, and the number asked never exceeds the audience.

### The editor says who will be asked, before you save

Same idea as Automations: *"38 people will be asked — 38 have finished HIPAA Training. Each is
asked as they come through, and has 14 days to reply."* Unattach it and it reads *"0 people can
be asked — this needs something to attach to. Until then it stays a draft; the old screen would
have let you mark it active anyway."*

### Results are distributions, not averages

A mean of 3.0 on a five-point scale is either everybody shrugging or half the room delighted and
half furious, and only one of those needs your afternoon. Every scale question shows all five
bars. On an *agreement* scale the order carries meaning so the sequential ramp does too — palest
disagree to darkest agree. On an unordered choice list shade would imply a ranking that is not
there, so those stay on one step.

Free text is shown as quotes with the role and community attached, because *"I still do not know
who to call at night"* from a CNA at Lakeside Manor is an action and an anonymous average is not.

### One survey that is not about a course

The annual staff survey attaches to a schedule and goes to all 44. That is why this stays a
module rather than a field on a course.

## 3. Left out on purpose

- **Quizzes.** Out of scope this pass, at your call. Anything with a right answer belongs in the
  course builder, where it already exists and already feeds the 75 threshold. Revisit separately.
- **A form builder.** Three question types — agreement 1–5, pick one, own words. The hint says
  four or five questions is plenty, because response rate falls off a cliff after that.

## 4. Verified

Headless, since the preview renderer has not responded for this project.

- Every view renders tag-balanced with no `undefined` / `NaN`: the list, five results screens,
  three new-survey states and five edit states
- **No survey with zero questions can leave draft** — asserted, not just observed
- Rates reconcile: replies ≤ asked ≤ audience, on every survey
- The preview counts before commit: 38 attached, 0 unattached
- Every control labelled (7 controls, 7 labels); the original dialog had 3 fields and no delivery
- Class audit clean in both directions; no duplicate selectors outside `@media`
- All 16 pages parse and serve 200; nav byte-identical across all of them

### Two more design-system fixes

- **`.kstrip` / `.kcell` hoisted into `dashboard.css`.** The KPI strip lived in `reports.html`'s
  page CSS and `surveys.html` reached for it — which is the definition of a shared component.
  Without the hoist the strip would have rendered unstyled.
- **A brace-balance check caught my own bad edit.** Hoisting with a line-oriented regex split a
  multi-line `@media` block, leaving the opener in `dashboard.css` and the closer in
  `reports.html`. Both files were broken; neither would have shown a JS error. Depth counting
  found it in one pass.

## 5. Open questions

1. **Anonymity.** Quotes carry role and community. At a small community that is identifying, and
   people answer honestly only when they believe it is not. What is the threshold — suppress
   free text below five responses?
2. **Does a survey chase?** Automations could nudge non-responders, but a nudge about an optional
   survey competes with a nudge about overdue mandatory training. The compliance one should win.
3. **Where do results surface?** They belong as a Reports tab; today they live only here.
4. **The quiz overlap**, deferred above.
5. **Sessions have no feedback loop at all** — `sessions.html` credits hours and never asks about
   the instructor. The survey exists here; wiring it into the session close-out is a separate pass.
