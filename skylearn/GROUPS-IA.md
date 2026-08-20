# skyLearn Groups: research, audit and information architecture

You asked two questions: **do we need this**, and if so **what is the right way to show it**.
The answer is different for each of the two tabs. The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. The short answer

| Tab | Verdict |
|---|---|
| **User groups** | **Not as built.** A hand-made list of people is a liability in a compliance product. Keep the tab, change what a group *is*. |
| **Course groups** | **Yes, and it is far more important than the screen suggests.** It is not a convenience for bundling courses. It is the definition of what every person is required to hold, which is where every compliance number in the product comes from. |

## 2. Why a hand-made list of people is a liability here

The screen shows one group: **Care Givers, 3 members**, made 25 March, untouched since.

There are **12 caregivers** in the roster. That group is missing **9 people** today. Nobody
did anything wrong; the list was accurate the day it was made, and then somebody was hired,
somebody transferred and somebody changed role, and the list did not notice.

That is the problem in one line: **a list is a photograph of the day it was taken.** In a
scheduling tool a stale list is an annoyance. In a product whose entire pitch is *are we
survey-ready*, a stale list is a group of people who quietly stopped being assigned mandatory
training, and nothing anywhere told anyone.

The alternative is not exotic. Every audience worth having in senior living is already an
attribute the system holds: **role** (CNA, LPN, Med Tech, Caregiver, Housekeeping),
**community** (six of them), and through the community, **state**, which is what determines the
compliance rules in the first place. *Role is Caregiver* is not merely easier to make than a
list of twelve names, it is **correct tomorrow**, which the list is not.

**Fixed lists are still allowed.** A fall prevention committee is a real thing that no rule
describes, and so is a named set of people put on a corrective action after a survey. They are
kept. They are just never the default, and they never pretend to be a role.

## 3. Why course groups are the most important object in the product

The dashboard reports a **92.4% compliance rate**. A learner record says **9 of 12 required**.
The sessions screen credits **hours toward the annual in-service requirement**.

None of those numbers can exist until something states that *a CNA must hold these twelve
courses, worth twelve hours, renewing every year*. Across seven modules of this redesign, that
definition has had no home. **This is it.**

Presented as *"bundle courses together and assign the whole set"*, it reads as a shortcut for
saving clicks. It is not a shortcut. It is the rule the whole product is measured against, which
is why the tab is now called **Requirements** and why every row carries who must hold it, how
often it renews, and how many of them actually do.

The proof that this is the right model: the twelve courses in *CNA annual in-service* match the
`12 required` on every CNA's learner record. Fifteen for LPNs, ten for caregivers, fourteen for
med techs. Verified, not asserted.

## 4. Audit of the screen being replaced

**Three zeros as a headline.** *Total Groups 0, Total Courses 0, Total Assignments 0.* On the
User Groups tab the third is still 0 with a group present, which is the most useful fact on the
page and it is styled as a statistic rather than a problem: a group that nothing assigns to is a
group doing nothing.

**"Total Courses" on a groups screen is ambiguous.** Courses inside groups, or courses in the
system? Two different numbers, one label.

**Two dialogs for the same shape, worded four different ways.** *Create Course Group* uses
`NAME`, `DESCRIPTION`, `KEY` in caps; *Create Group* uses `Name *`, `Description`, `Group Key` in
sentence case. Placeholders read *"e.g. New Hire Onboarding"* against *"Enter group name"*, and
*"Optional stable key, e.g. onboarding"* against *"e.g., dept-engineering"*. One of them marks
the required field with an asterisk and the other does not.

**`Key` is a developer field on an administrator's screen.** A stable identifier for an
integration is a real need, but a training director should never be asked to invent one. It
should be generated from the name and only surfaced if someone goes looking.

**The dialog cannot express the only decision that matters.** *Name, Description, Key* offers no
way to say "everyone who is a caregiver". Every group the screen can make is a fixed list,
because a fixed list is the only kind there is.

**"Members 3" is a count with no denominator.** Three out of what? The number that matters is
the nine who are missing, and it is not on the screen.

**The empty state is a full page of nothing.** Three zero cards, a search box over no rows, and a
bookmark icon. Nothing tells a first-time administrator what a course group is *for*.

## 5. What replaced them

### Audiences

Every row states **how it stays up to date**, because that is the difference between a group that
is right tomorrow and one that is quietly wrong:

- **Rule** — *Role is Caregiver.* Evaluated every time it is read. Hire someone this afternoon
  and it already includes them.
- **Fixed list** — *chosen by hand, 25 Mar 2026.*

And every drifted list says so, in people, on its own row:

> **Care Givers** · chosen by hand, 25 Mar 2026
> ⚠ 9 people who match "Role is Caregiver" are not on it

with one control at the top to convert them all. The **Used by** column names the requirements
that point at an audience, so an audience nothing uses admits it rather than sitting there
looking maintained.

### Requirements

Columns are the four questions a requirement has to answer: what is in it, **who must hold it**,
how often it renews, and **how many of them are up to date**. Two findings sit above the table,
neither of which the original screen could have surfaced:

> **1 requirement applies to nobody:** "New hire onboarding". It was written, and then never
> pointed at anyone, so it has never asked anything of anybody.

> **2 people are covered by no requirement at all:** Tara Sullivan (Administrator), Owen
> Fitzgerald (Administrator). They cannot fail an audit, because nothing was ever asked of them.

That second one is the whole reason this screen deserves to exist. A compliance rate of 92.4%
counts the people somebody remembered to write a rule for. Everyone else is invisible, and
being invisible reads as being fine.

### The create dialogs

**The kind is the first question, and the rule is the default.** Two radio cards, *A rule*
(recommended) and *A fixed list*, with the consequence spelled out on each. Choosing a rule
shows the count live: *16 people match today, and it will keep matching as people join and
leave.* Choosing a list warns using the system's own evidence: *a hand-made caregiver list on
this system is already 9 people out of date.*

**The requirement dialog refuses to create one with no audience**, naming the existing orphan as
the reason. That is the one field the original dialog did not have, and its absence is why the
Assignments column reads 0.

Name and description survive. **Key does not appear**: it is generated from the name.

## 6. Verified

Headless, since the preview renderer has been dead for this project.

- Drift is computed, not written: the client's own group resolves to 3 of 12, missing 9, and
  names *Role is Caregiver* as the rule that would have been right
- Adding a CNA to the roster grows the *All CNAs* rule to 17 and leaves the fixed list at 3
- Requirement course counts match the learners screen exactly: CNA 12, LPN 15, Caregiver 10,
  Med Tech 14
- One orphaned requirement and two uncovered people, both found by traversal rather than typed
- Both tabs and both dialogs render; class audit clean in both directions

## 7. Open questions

1. **Should Groups be a top-level nav item at all?** It is now, because that is where you have
   it, but it takes the sidebar to ten and `DASHBOARD-IA.md` §6 argued for a ceiling of nine.
   The tidier split is **Audiences as a tab inside Learners** and **Requirements as a tab inside
   Certifications**, which is where the state mapping already lives.
2. **Who may edit a requirement?** It changes what thousands of people are measured against, and
   right now it is one dialog away for any administrator.
3. **What happens to people already assessed when a requirement changes?** Adding a thirteenth
   course to the CNA set instantly makes 16 people non-compliant. Is that correct, or does the
   change apply from the next renewal?
4. **Do requirements need to vary by state within a role?** A CNA in Ohio and a CNA in Texas are
   both "All CNAs" here, but their state hour rules differ.
5. **Is `Key` needed by a real integration?** If so it should be generated and shown read-only,
   not typed by a training director.
