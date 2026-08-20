# skyLearn, the learner side: research and the dashboard

The first learner screen, rebuilt from research rather than from the admin dashboard shrunk down.
The visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The finding that settled the design

The live screen's empty state says **"Browse the catalog to enroll in a course."**

Counted across the roster every other screen uses:

| | |
|---|---|
| Learners | **44** |
| With **zero** courses assigned | **0** |
| With something outstanding | 28 |
| With something overdue | 10 |
| With a lapsed certificate | 4 |

**That empty state is written for nobody.** Training in this product is *pushed* — Groups
audiences and requirement sets assign it — so a CNA never browses a catalogue to find HIPAA
training. The one instruction the screen gives is the one thing that is not the learner's job.

### And two of the three numbers are the administrator's

*Courses Enrolled*, **Completion Rate**, *Avg Score*. A completion rate is an oversight metric:
useful to somebody comparing six communities, meaningless to one CNA who needs to know whether
she can finish something before her break ends.

**Avg Score is worse than meaningless.** Seven of the 44 have never been assessed, and the screen
would show them **0** — which reads as failure when it is absence. That is the same defect already
fixed on the learner record, where it is written down as *"Not assessed is not zero"*.

## 2. What a learner actually opens this for

> **What do I have to do, and can I do it now?**

Counted, there are **five** answers to that, not one:

| | | |
|---|---|---|
| 4 of 44 | a lapsed certificate | **stops them working unsupervised** |
| 9 of 44 | something past its date | |
| 15 of 44 | courses to do, none late | |
| 2 of 44 | a certificate lapsing within 30 days | |
| 14 of 44 | nothing at all | |

So the screen needs five good states. The live one has a single empty state that fits none of
them. This version renders all five, each headed by **one answer in a sentence** rather than three
cards — and the prototype carries a switcher across the top so all five can be judged, using a
real person from the roster for each rather than a flattering example.

### Minutes, not counts

Median outstanding work is **2 courses per person**; the worst is 8. *"2 courses"* tells a CNA
nothing. *"45 minutes"* tells her whether it happens on this break or gets put off again, so every
item and every section total is in minutes.

### The consequence, in words, at the top

For the four with a lapsed certificate the headline is not a red badge, it is the sentence:

> **You cannot work unsupervised until this is renewed.**
> Your *Safe Resident Handling* certificate has run out. Renewing it is one course, about 35
> minutes, and it clears as soon as it is signed off.

### Encouragement last

Progress, points, badges and competency sit at the bottom. They are motivation, not instruction,
and putting them at the top buries the thing to do. Competency shows **Not assessed** where there
is no check, never a zero.

## 3. Verified

Headless, since the preview renderer has not responded for this project.

- All five states render, tag-balanced, no `undefined` / `NaN`
- Every state has a real person behind it, and the five cohorts sum to **44 = the whole roster**
- **The work list reconciles for all 44**: items = `required − done`, late items = `overdue`
- No *completion rate* anywhere; never-assessed shows as *Not assessed*
- Class audit clean both directions, brace balance 0, the role switcher works
- 21 pages parse and serve 200

### A bug the reconciliation caught

The lapsed-certificate headline read *"Your **Infection Prevention** certificate has run out"* —
about a course that issues no certificate. The work list was generated independently of the
`expired` flag, so the headline named whichever course happened to sort first. All four affected
people got a confident, wrong sentence about their own compliance.

Fixed by making the data coherent rather than patching the text: a lapsed certificate now
guarantees its renewal course is in the work list, sorted first, and the headline reads that item
specifically. All four now correctly name *Safe Resident Handling*.

## 4. Open questions

1. **"My Progress" and "Dashboard" are both in your learner nav** and appear to answer the same
   question. One of them is probably the other's detail view.
2. **The header said "Administrator" on the learner screen.** Fixed here, but it suggests the role
   is not threaded through the live app either.
3. **Can a learner do anything about a lapsed certificate at 3am?** *Ask about this* posts to their
   record. Whether that reaches anyone out of hours is an Automations question.
4. **Is the catalogue reachable at all for these people?** If everything is assigned, the
   Catalogue nav item may be for a different kind of customer than a senior-living operator.
