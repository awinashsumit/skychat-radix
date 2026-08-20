# skyLearn Automations: research, and what it became

You asked whether this module is needed at all. The short answer: **yes, but not for what it
was doing.** The visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The evidence

### The screen's own number

**Rules (0). Execution Logs (0).** Nobody has ever made one.

### Seven of the plausible rules already exist

A generic trigger → action engine sounds useful until you check what the app already does.
Every one of these works today, declaratively, without a rule:

| A rule would do | Already done by |
|---|---|
| New hire → assign onboarding | Groups audience rule + requirement set; `assign.html` *"assign automatically to anyone who joins these roles later"* |
| Role change → assign that role's courses | Groups audiences are rules on `role`, so membership updates itself |
| Annual renewal → reassign | requirement sets carry `renew: 'Every year'`; assign has auto-repeat |
| Completion → issue certificate | `certificate.html` auto-issues |
| Completion → award points and badges | `recognition.html` rules |
| Session attended → credit hours | `sessions.html` close-out |
| Question posted → route to an owner | `discussions.html` escalation |

The dialog's flagship action was **Assign Course** — the one thing the app already does, in two
places.

### Why that is worse than redundant

Assignment decides who is compliant. Two ways to assign means **two sources of truth for
who-must-do-what**. When Reports says somebody is non-compliant, nobody can tell whether Groups
or an automation rule put that course on their list — and the compliance report cannot tell you
either. In a product whose output is evidence for a regulator, that is a defect, not a feature.

### What is genuinely missing

| Gap | Existed? |
|---|---|
| Overdue → remind the learner | **No** |
| Still overdue → tell their manager | **No** |
| Certificate expiring → warn somebody | **No** — the dashboard counts it, nobody is told |
| Monthly → email the compliance summary | **No** — raised as an open question in [`REPORTS-IA.md`](REPORTS-IA.md) §5 |
| Finish course A → schedule B | **No** |
| Failed a competency twice → flag the trainer | **No** |

**Every gap is remediation or notification. None is assignment.** The app is excellent at
deciding who must do what, and silent about telling anyone they haven't.

## 2. What it became

> **The app already decides who must do what. This decides who gets told when they haven't.**

Seven rules ship, three running. The old empty state said *"create your first rule"* to a blank
page and got zero rules; these are the six gaps above, ready to switch on.

The **ladder** is the object: a watched situation, then who hears about it and when.

```
Chase overdue training
Straight away  → tell the learner by email
Day 7          → tell the learner by email and in the app
Day 14         → tell their manager by email          ← escalation, marked in red
```

An escalation is only an escalation if it reaches somebody other than the person already
ignoring you, so steps that leave the learner are marked differently.

### Every rule shows its reach before you commit

The old dialog could not tell you who a rule would write to. Every rule card and the editor
now carry a live count from the real roster — *9 people right now* — with names, updating as
you change the scope. Turning a rule on tells you in the toast how many people will hear from
it immediately.

### The cohorts are disjoint, and that is enforced

Written the obvious way — `overdue` means `p.overdue > 0` — somebody who is **both lapsed and
overdue matches two rules and is told twice about one problem.** The per-rule cap cannot catch
it, because it is one message from each of two rules.

So every watch is defined through `stateOf()`, the same precedence the Learners screen uses:

```js
overdue:  { match: p => stateOf(p) === 'overdue' }
expired:  { match: p => stateOf(p) === 'expired' }
```

Asserted headlessly: **5 cohorts, 20 people covered, 0 overlaps.** One person, one state, one
chain. It also means a rule can never claim somebody is overdue while their learner record
calls them lapsed.

### Ohio, Texas and Florida count hours

A reminder that says *"3 courses outstanding"* is the wrong sentence for a regulator that counts
hours. The preview says so: *"7 of them are in FL, OH, TX, where the regulator counts hours
rather than courses."*

### A cap, because six overdue courses should not be six emails

Every rule defaults to at most one message per person per week, and the field says why.

## 3. What was deliberately left out

- **Assign Course.** Groups owns assignment. The only assignment-shaped rule is *after a course
  is completed, schedule another* — sequencing, which a flat requirement list genuinely cannot
  express, and which can only follow a completion so it cannot become a parallel assignment
  system.
- **Arbitrary conditions.** Not a query builder. Seven named situations the app already knows
  about, because a rule engine that can express anything is a rule engine nobody audits.

## 4. Verified

Headless, since the preview renderer has not responded for this project.

- Both tabs and all seven watch types render, tag-balanced, no `undefined` / `NaN`
- Reach reconciles with the roster: overdue 9 = 9, lapsed 4 = 4, against `stateOf()`
- **0 overlaps** across the five cohorts — nobody can be messaged by two rules
- Scope only ever narrows: 9 → 3 at Lakeside Manor, 9 → 1 for CNAs, 9 → 0 for both
- Every control in the dialog is labelled (7 inputs, 7 labels); the old dialog had none
- Save is gated on a name
- Class audit clean in both directions; no duplicate selectors outside `@media`
- All 14 skyLearn pages parse and serve 200; nav byte-identical across all of them

### Seven more design-system defects fixed at source

The class audit found six shell classes — `.hdr-search`, `.hu-id`, `.hu-name`, `.hu-role`,
`.nav-tail`, `.pt-num` — defined **identically on all 13 pages and absent from
`dashboard.css`**, plus `.sr-only` in the same state. All hoisted into the DS, 91 duplicate
declarations removed. Same drift as `.stack-3` and `.stack-4` before them.

## 5. Open questions

1. **Nav is now ten items plus help.** `UI-CHECKLIST.md` §20 says nine fit and thirteen did not.
   Ten needs a check against the viewport before more is added.
2. **Who is "their manager"?** The roster has no reporting line. Today it would fall to the
   community's administrator, which is a guess.
3. **Should a learner be able to snooze?** A nudge nobody can turn down becomes noise people
   filter out, and then the escalation is the first real signal.
4. **Quiet hours.** Nothing stops a rule emailing a night-shift CNA at 04:00.
5. **What happens to in-flight ladders when a rule is edited?** Somebody on day 7 of the old
   version is currently undefined.
