# skyLearn Dashboard: research, audit and information architecture

Why Home > Dashboard holds this content rather than the content it replaces. The visual
contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What the product is actually for

From the product positioning: skyLearn is "more than an LMS, a workforce development and
competency platform", sold to senior living and healthcare operators against Relias,
HealthStream, Cornerstone and Absorb. Its thesis is one sentence:

> **Competency, not just completion.**

Everything it charges for follows from that: AI course generation from a facility's own
documents, 50-state compliance mapping, automatic certification tracking, and a three-axis
competency assessment at hire, day 90 and each quarter.

Two consequences for a dashboard:

1. **A completion count is the competitor's metric.** If the landing screen leads with courses
   and completions, it is a Relias dashboard with a new skin. The screen has to lead with
   compliance risk and competency, because that is the ground the product chose to fight on.
2. **The buyer and the user are different people.** The frontline CNA lives on a phone between
   shifts and needs three assigned courses, not a dashboard. This screen is for the
   training or compliance director: multi-community, multi-state, accountable for survey
   readiness. It is an administrator's operational dashboard and should be designed as one.

## 2. Who this screen is for

**Primary: the Administrator.** A director of training or compliance, signed in as an admin. Opens
this screen once or twice a day for two minutes. Wants to know, in order:

| Question | Block that answers it |
|---|---|
| Are we survey-ready right now? | Compliance rate KPI |
| What is going to bite us this month? | Expiring, overdue, competency KPIs |
| What is actually broken today? | Needs attention |
| Is it getting better or worse? | Compliance trend |
| Where is it worst? | Compliance by community |
| Is competency real, or just completions? | Competency by domain |
| Who do I chase first? | Learners at risk |

**Secondary: Facility Administrator**, who cares about one community and reaches it by scoping.
The community scope switcher exists for them, and the ranked community list doubles as their
way in.

## 3. Audit of the screen being replaced

Not a style critique. These are the reasons the screen could not do its job.

**It measured the software, not the workforce.** Total Courses 5, Active Learners 6,
Completions 2. A director does not need to be told how many courses exist. None of the three
headline numbers changes a decision, and none has a denominator, a period or a target, so
none can be read as good or bad.

**It said the same three facts five times.** "Total Courses 5, 4 active, 1 drafts" is restated
by Course Distribution (Active 4, Drafts 1) and again by Total Enrollments 8, which is restated
by Enrollment Status (4 + 2 + 2). Five widgets, three facts. That is why a full page still felt
empty.

**Its charts were not charts.** Course Distribution was a two-bar chart of 4 and 1, which is a
sentence pretending to be a visualisation. Enrollment Status was a legend with no graphic
attached to it.

**Quick Actions duplicated the sidebar.** Courses, Learners, AI Generator and Reports were all
already one click away in the left nav, at the same depth. Four tinted tiles bought nothing and
occupied the most valuable block on the page, the top of the right column.

**Needs Attention had the right instinct and the wrong content.** It is the best idea on the
old screen. But an unpublished draft course is not an exception worth a banner; an expired CPR
certification is. And the row's only affordance was an unlabelled chevron.

**Recent Enrollments was a feed, not a worklist.** Sorted by recency, it shows the same thing
forever and never demands action. "Enrolled, 0%" states one fact twice.

**Colour carried no meaning.** Amber did brand duty on the CTA and status duty on the Drafts
bar, the In Progress dot, the Enrolled badge and the attention banner. The same three
enrollment states were coded two different ways in two adjacent widgets: grey and amber badges
in one, blue, orange and green dots in the other.

**Typography had no ratio.** The page title, the section headings and the card titles were
within a step or two of each other, so the page had no single entry point. KPI labels were
11px tracked caps, a decade-old tic.

**No scope, no period, no freshness.** A multi-community, multi-state product with no
indication of which communities, over what window, as of when.

**The sidebar was a feature list.** Fifteen items across two groups, one of them ("Tools") a
junk drawer holding a flow (AI Course Generator), two settings-level features (Gamification,
Discussions) and four sub-screens. The 4 POINTS chip put a learner gamification score in an
administrator's global header.

## 4. What replaced them

Four KPIs, chosen because each one changes what the director does that morning.

| KPI | Why it earns the slot |
|---|---|
| **Compliance rate** 92.4% | The survey-readiness number. Top-left, largest type. |
| **Required courses overdue** 57 | Today's backlog, and the biggest single driver of the rate. |
| **Certifications expiring in 30 days** 23 | The only forward-looking number. These learners are compliant today and will not be next month. |
| **90 day competency pass rate** 78% | The product's own thesis, measured. Completion cannot substitute for it. |

Then the exception worklist. **Needs attention lists four real compliance exceptions and each
one filters the table at the bottom of the page.** That is the spine of the screen: the
exception tells you the size of the problem, one click turns it into the list of people it is
happening to. Nothing else on the page is a shortcut to somewhere else.

Then trend and breakdown. The compliance trend carries an explicit 95% target line, because a
rate without a target cannot be judged. The community list is sorted **worst first** and marks
the same target on every bar, because on an exception dashboard the ranking that matters is
the one you have to fix.

Then competency by domain, scored against the pass threshold of 75, using the product's own
three axes: knowledge and compliance, standards and communication, judgment and people skills.
Judgment sits at 71 and is badged below threshold. This is the block that makes the screen
skyLearn's rather than any LMS's.

**What was cut and why.** Course counts, enrollment status and the quick-action tiles are gone
outright: two were inventory, one was navigation. Recent enrollments is gone because a feed
sorted by recency never needs anyone's attention; the worklist sorted by days past due always
does.

## 5. Sample data

One dataset, six communities, and every figure on the screen derives from it. Identities are
placeholders.

- 1,284 learners across 6 communities in 6 states.
- 98 at risk = 7 expired certifications + 57 overdue required courses + 34 stalled onboardings.
  Compliant 1,186, so the rate is 92.4%.
- 23 certifications expiring within 30 days. These learners are compliant today, which is why
  they are counted separately from the 98.
- 156 ninety-day checks due this quarter, 122 passed, so 78%.
- Domain scores are the learner-weighted mean of the six communities: 84 / 79 / 71.

Scoping to a community recomputes every one of these from the same rows. Stock values roll up
exactly. Period deltas are rates and do not sum across scopes, which is also true of the real
system.

## 6. Navigation

Fifteen items became nine. The rule applied is the DS one: primary nav is top-level
destinations, aim for five to eight, hard ceiling nine.

```
Dashboard          this screen
Courses            catalogue, drafts, versions, AI generation
Learners           people, enrollment requests
Certifications     credentials, expiry, renewals, state mapping
Sessions           instructor-led and blended
Groups             audiences and requirements
Recognition        points, badges, leaderboard
Discussions        the question queue
```

**Trimmed to eight, 2026-08-18** (client decision). `Assessments`, `Automations`, `Reports` and
`Content library` are gone from the sidebar: none had a screen behind it, and with them present the
list reached thirteen items, which overflowed the sidebar and pushed the two real destinations,
Recognition and Discussions, below the fold. They were only visible after scrolling, which read as
them being missing.

The nine-item ceiling in this section was not the problem. **Placeholders counting toward it was.**
An item in the nav is a promise that something is there.

Where the removed items went:

| Was a nav item | Now |
|---|---|
| AI Course Generator | A flow, launched from the Create course dialog. Not a destination. |
| Groups | A tab inside Learners. |
| ILT Sessions | Renamed Sessions, since blended and virtual belong there too. |
| Enrollment Requests | A queue inside Learners. |
| Grading Hub, Surveys | Tabs inside Assessments. Both are assessment work. |
| Discussions, Messages | Course-level features and a notification surface, not places. |
| Gamification | Configuration. It belongs in Settings, with its learner-facing effects on the learner portal. |
| Files Library | Renamed Content library and kept, since AI generation makes source documents a first-class asset. |

**The points chip stays in the header** (client decision, 2026-08-17), reversing an earlier call
to drop it. The argument for dropping it was that gamification is a learner motivator and does
not belong in an administrator's chrome. The argument that wins is that the administrator is
also a learner: a Director of Training carries their own HIPAA and safety requirements, and the
chip is their own standing in that, not a report about anyone else. It is set as a `.presence`
pill rather than the original green badge, because green is the success status colour here and
a score is not a status. It is a `<span>` with no hover, so it does not read as clickable.

**Community scope moved from the header to the filter bar** to make room. This is the better
home regardless: scope and comparison period are the two halves of one question, "what am I
looking at, and over what window", and every block on the page reads from both. Keeping them
together also means the page's filter state is in one place rather than split across two
regions.

## 7. Open questions for the client

1. **Is 95% the real compliance target**, and is it set per organisation, per state, or per
   requirement type? The trend line and every community bar are drawn against it.
2. **Is 75 the real competency pass threshold**, and is it uniform across the three domains?
3. **Does "at risk" include learners with a certification expiring inside 30 days?** Here it
   does not: they are compliant today and are counted separately. That is a policy decision,
   not a design one.
4. **Should the dashboard scope default to all communities or to the viewer's assigned
   community?** A regional director and a facility administrator want opposite defaults.


## 8. This is the administrator's dashboard

Confirmed 2026-08-17. The header identity reads **Administrator** on every screen, and the create
flow defaults to an administrator who can publish directly rather than an instructor who submits
for review.

An instructor gets their own dashboard, which is a separate module: they do not need compliance
rates across six communities, they need their own drafts, the notes an admin sent back, and what
they are teaching next. The nav they see will be shorter too. Nothing in this file should be
reused for it without checking that first.
