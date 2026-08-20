# skyLearn Gamification: research, audit and information architecture

You said there is too much information, that some of it repeats, and that the badges do not make
sense. All three are right, and the badges are the sharpest of them. The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What gamification is for in *this* product

Gamification in a consumer app exists to make people come back. **In a compliance LMS for senior
living it exists for one thing: getting required training finished before it is due, without a
manager chasing it.**

That single sentence decides everything else. If a rule does not make required training more
likely to be done on time, it is not earning its place. Two consequences:

- **Never reward presence.** A caregiver logging in is not training.
- **Never reward volume.** Two hundred and fifty-six discussion posts is not competence.

And one about the audience. Direct-care staff in senior living are hourly, time-pressured, and the
sector's turnover is famously close to a hundred percent a year. **Any reward that takes years to
reach is a reward for tenure, not for effort**, and most of the people it is shown to will never
see it.

## 2. Audit of the screens being replaced

### The badge ladder is mostly unreachable, and this is arithmetic

Sixty-four badges, seven categories, eight tiers each, on a doubling ladder ending at *complete 128
courses*, *pass 256 tests* and *post 256 discussion posts*.

A CNA has **12 required courses a year**. Working that through, at a **two-year median tenure**:

| Category | Years to reach each tier |
|---|---|
| Learning | 0.1 · 0.2 · 0.3 · 0.7 · 1.3 · **2.7** · **5.3** · **10.7** |
| Test | 0.2 · 0.3 · 0.7 · 1.3 · **2.7** · **5.3** · **10.7** · **21.3** |
| Perfectionism | 0.2 · 0.3 · 0.7 · 1.3 · **2.7** · **5.3** · **10.7** · **21.3** |
| Survey | 0.3 · 0.5 · 1.0 · **2.0** · **4.0** · **8.0** · **16.0** · **32.0** |
| Certification | 0.7 · 1.3 · **2.7** · **5.3** · **10.7** · **21.3** · **42.7** · **85.3** |

**Twenty-nine of the fifty-six are out of reach before the median learner leaves.** *Certification
Grandmaster* asks for 128 certificates, which is eighty-five years of renewals. *Survey
Grandmaster* asks for 128 surveys from a facility that runs about four a year.

That is what "doesn't make any sense" is, measured.

### The level column contradicts itself, on the client's own screen

Levels can upgrade every N points **or** every N completed courses **or** every N badges, with all
three switched on and nothing saying which wins. The leaderboard shows the result:

> **132 points → Level 1.  117 points → Level 2.**

The *upgrade every 3000 points* rule has **never fired** — the highest score in the organisation is
132 — so the level column is being driven by one of the other two rules while sitting next to a
points column it contradicts, in a table sorted by points.

### The leaderboard ranks twenty named people, and fourteen of them are at zero

Top score 132. **Fourteen of the twenty rows sit on nine points or fewer**, four of them on one.
That is not a competition; it is a published list of who has spent the most unpaid time in the app,
with fourteen colleagues named at the bottom of it. In a sector with this turnover and these
margins, that is a retention problem wearing a trophy icon.

The name in first place is **"Senior Living"**, which is not a person. Nothing noticed.

### The points economy has never been checked against itself

*Each login, 1 pt.* At one a day that is **365 points a year for opening the app and closing it**,
against 10 for finishing a course. **Logging in beats completing every required course a CNA has.**
No screen anywhere showed the two numbers together, which is how it survived.

*Each upvote on discussion comments, 1 pt* pays a learner for what other people do, which two
learners can arrange between themselves in a minute.

### The repetition you spotted

- **Two levels of the same switch.** An *Enable X System* master toggle on every tab, plus a toggle
  on every row inside it.
- **The same 64 badges on two screens.** The Badges tab shows eight icons per category; *System
  Badges* shows the same set again with names and thresholds. Neither is the place you would edit
  them.
- **The leaderboard's display options** re-list points, badges, levels, courses and certificates,
  which are the subjects of the other four tabs.
- **`Reset to Defaults` and `Save Settings` on every tab**, with nothing saying whether they act on
  the tab or the whole feature.
- **Two buttons, `Award Points` and `Adjust Points`**, with no stated difference.
- **`Badge ID (Optional)`** asks a training director to type a badge's internal identifier.

### And it is five tabs for one feature

Points, Badges, Levels, Leaderboard, Award Points. Five destinations, each a list of switches, for
a single question: *what do learners earn, and who sees it.*

## 3. The split: two destinations, not one screen

The first attempt at this collapsed all five tabs onto a single page. Sumit's response was that it
was the same mistake rotated: **the wall moved from horizontal to vertical.** He was right, and the
principle it was missing is the oldest one in settings design:

> **Configuration and consequence are different jobs, done at different times, often by different
> people. They are not sections of one screen.**

- **What earns points, and which badges exist**, is set once at setup and then almost never touched.
- **Who is doing well, and is any of this working**, is read weekly.

Putting them together meant the thing you read weekly sat underneath six things you set once. So:

| | |
|---|---|
| **Recognition** (`recognition.html`) | The surface. Leaderboard, who holds which badge, and every point given by hand. In the nav. |
| **Recognition settings** (`recognition-settings.html`) | Configuration. The five earn rules and the six badges. One button away, and one visit a year. |

### And the surface earns its own screen, because it can answer a question nothing else could

Not *who is winning*. **Is this working.** The board now carries each learner's compliance state
beside their points, and says so when the two disagree:

> **3 of the top 10 are not up to date.** Sofia Grandi is 1 course short and still ranks 3rd. If
> the top of this board is not the top of your compliance report, the points are paying for
> something other than getting training done.

That is computed by traversal, and none of the six screens this replaces could have produced it,
because points and compliance never appeared in the same table.

**Points given by hand now leave a record**, with the reason, on the surface. A manual award is the
one part of this system a person can abuse; previously it was a form with no visible outcome
anywhere.

## 4. What replaced them

**One screen.** No tabs. The order is the order of the decision: is it on, what earns points, what
badges exist, how levels work, and only then whether anyone else can see it.

**Off by default**, and the switch says what learners get when it is on: *their own points, badges
and level, visible only to them.*

**Five earn rules, all tied to compliance outcomes.** Finished on time (10), finished late (2, still
credit, but less or on-time means nothing), passed a competency check (15), attended an
instructor-led session (15), renewed a certificate before it lapsed (20). Login and upvote are gone.

**The economy states itself.** *A CNA who finishes all 12 required courses on time, passes four
competency checks, attends two sessions and renews two certificates earns 250 points a year.* With
the comparison directly underneath: the removed login rule paid **365**. Seeing those two numbers
together is what makes the old configuration obviously wrong, and no previous screen ever put them
in the same place.

### Three badges, three different questions

The first replacement had six, and Sumit read the holder counts and found two defects in it. Both
were real, and measurable:

**"On time, every time" and "First year done" awarded to the same 16 people, and always would.**
`overdue` counts what is *currently* late, so anybody who has finished their set has zero by
definition. Two rules that can never disagree are one badge written twice.

**"Steady" was (nothing overdue) AND (nothing lapsed)**, and the second half is exactly the
"Current" badge. A compound of two others wearing a third name.

**"Nearly there" went to 33 people, 17 of whom had not finished.** A badge for almost doing the
thing.

What is left asks three different questions:

| Badge | | Held by |
|---|---|---|
| **Set complete** | Did you finish what you must? | 16 of 44 |
| **All current** | Are your credentials in date? | 40 of 44 |
| **Competent** | Can you actually do the job? | 14 of 44 |

**And none of them is another way of counting courses.** Sumit asked whether badges should be based
on the number of courses completed. They should not, and the reason is structural: **the required
set resets every year.** A ladder needs a number that keeps climbing; twelve courses a year, every
year, does not. That is also why the original 64-badge ladder ran off the end of a working
lifetime — it was built on a number that never grows.

### The set now checks itself

Sumit found those two defects by reading. The settings screen now finds them by running, so the
next badge anybody adds gets the same test:

- **Two badges awarding to exactly the same people** is always a defect, and says so:
  *"…award to exactly the same 16 people, and always will. That is one badge written twice."*
- **A badge held by almost everybody** separates nobody: *"All current is held by 40 of 44."*
- **An implication** is reported only when it is not explained by the badge above being nearly
  universal, because otherwise everything is inside it and the note is noise.

When there is nothing to say it says so, which is a reassurance the previous set never earned.

### Levels are gone

Sumit could not work out what a level was for, and took that as evidence no user would either. That
is the right test, and the answer is not to explain it better.

**A badge is a level with a name on it.** The set this replaces had eight tiers per category —
Newbie, Grower, Adventurer, Explorer, Star, Superstar, Master, Grandmaster — which is a level system
wearing badge icons, and then a separate *Levels* tab **on top of it**. Two mechanisms for one idea,
and the one nobody could explain was the unnamed number.

A level also communicated nothing. *Level 2* does not tell a learner what to do next, and does not
tell a director anything the compliance report does not already say. **On time, every time** does
both. So the badges are the levels, and they say what you did to earn them. Three currencies became
two.

**The leaderboard is off by default, and it ranks three ways: communities, roles, or individual
learners.**

The first pass offered only teams. Sumit asked whether individuals were gone, and he was right to:
the harm in the original was never *ranking individuals*, it was **all-time** and **publishing the
bottom**. Both are fixed, and then an individual board is fine:

- **A rolling 90 days, not all time.** Somebody who joined in March can win it. On an all-time board
  they can never catch somebody who joined in 2019, which makes it a tenure ladder with a trophy on
  it.
- **Everybody, ten to a page.** An earlier pass showed only the top 10 and named nobody else, to
  avoid publishing a list of who is at the bottom. Sumit chose the full roster with pagination
  instead, and that is what ships. The privacy argument is recorded here rather than in the UI: if
  a customer ever objects to the whole roster being ranked by name, the cut-off is the lever.

**Paging is a view of the board, not the board.** Everything that judges the board — the medal
tiers and the compliance check — reads the full ranking, so *13 people hold a medal* and *3 of the
13 are not up to date* say the same thing on page 1 and page 4. Slicing first would have made both
numbers silently mean "on this page".

**Award points is a dialog, not a tab.** No Badge ID. One number instead of two buttons, because
the sign is the difference between awarding and adjusting. And **the reason is required**, because
the learner sees it and points that arrive without one read as a mistake.

## 5. Medals and course badges

Sumit proposed two changes to the surface once the badge set was sound: **Gold, Silver and Bronze
for the top three on the leaderboard**, and **a generic badge for everyone who completes a
particular course**, in the tile style of a reference image (icon, name, on a card of its own).

### Medals go by score, not by position

The rule Sumit set: **gold to everybody on the top score, silver to everybody on the next distinct
score, bronze to everybody on the one after that, and nothing below.** Ties never get broken; they
widen a tier.

A first pass used standard competition ranking (1, 1, 1, 1, 5, …), which has a real failure on this
data: four learners are tied at 75 points, so gold went to four people and **silver and bronze were
never awarded at all**. Ranking by distinct score fixes that — all three medals are always handed
out as long as three different scores exist.

The trade is that a wide tie widens a tier. On the current roster:

| Tier | Score | People | Medal |
|---|---|---|---|
| 1 | 75 | 4 | Gold |
| 2 | 65 | 8 | Silver |
| 3 | 55 | 1 | Bronze |
| 4 | 50 | 7 | none |

So **thirteen people hold a medal, not three**, and the board says so rather than letting it look
like an error:

> *13 people hold a medal this period rather than three, because a medal goes to everybody on a
> score rather than to a position. Gold 4, silver 8, bronze 1.*

Worth watching: a tier is only as tight as the scoring is granular. Silver covering eight people is
a symptom of the 90-day score bunching, not of the medal rule.

Below bronze the cell shows the plain tier number, quietly, because the point of the column is the
three medals.

**The medal is the trophy alone.** The words *Gold*, *Silver* and *Bronze* were on the page in a
first pass and are gone: three coloured, numbered trophies in a narrow column do not need naming
twice. The word moved to the icon's `aria-label`, because a numbered trophy is unreadable to a
screen reader without it.

Medals only appear when ranking individuals. Ranking communities or roles still shows a plain
number, because a medal implies a person earned something, not a group's rate.

The glyphs are three supplied assets: one trophy shell, three fills (`#FFAA04`, `#9E9E9E`,
`#FF6E04`) and a baked-in numeral each. They are kept as literal two-path markup rather than being
recoloured through the `currentColor` pattern the rest of the file uses, because they are finished
artwork rather than UI icons — and nothing tints them from CSS, so they are identical in both
themes.

### Course badges: one common badge, awarded automatically

**Not a setting.** There is nothing to tune, only a fact to display, so it lives entirely on the
surface and is absent from `recognition-settings.html`'s controls.

The artwork is the supplied **Common Badge**: a single gold design used for every course, with the
course name on the plate beneath it. An earlier pass tinted a hexagon per course category; the
supplied asset replaces that, and one badge for all courses is the simpler rule anyway — the course
name is what varies, so the artwork does not need to.

**It is the PNG, not a rebuilt SVG.** A first attempt transcribed the source SVG inline and the
gold came out visibly wrong: the shield carries a drop shadow *and* an inner shadow, and only the
drop shadow survived the transcription. Raster removes the whole class of problem — there is no
transcription to drift, and no per-instance gradient and filter ids to keep unique. It is also
**the same image in both themes**, which is right: a badge is an object, not chrome, so it does not
restate itself per theme the way a token-backed surface does.

**The plate is real text**, not the paths in the source file, so a long course name wraps and a
screen reader can read it. The `<img>` carries its intrinsic 308×318 so the row does not reflow
while it loads.

**The count is not invented.** `Preventing Falls in Senior Living` and `HIPAA Privacy and Security`
are the only two courses in this prototype with a real per-learner completion record — the same
`ALREADY` roster the Learners and Assign screens already use to avoid double-enrolling somebody.
Reusing it means the badge's holder count (10 of 44, 8 of 44) can never disagree with what those
other two screens say about the same fact. A full build needs an enrollment table across the whole
catalogue; inventing a second, parallel dataset here to cover the other ten courses would have
recreated the exact problem this rebuild keeps finding, two screens quietly disagreeing about the
same person.

## 6. Verified

Headless, since the preview renderer has been dead for this project.

- 29 of 56 badge tiers on the old ladder shown unreachable inside a two-year tenure, by arithmetic
- 5 earn rules, down from 9; login and upvote absent
- 250 points a year for a model CNA, against 365 for the removed login rule
- All 6 badges held by at least one real person in the roster
- Level spread 28 / 16 across the population; a full required set is exactly one level
- The leaderboard preview names no individual when ranking teams, and cuts at the top 10 of 44 when
  ranking people
- Medal tiers confirmed against the real data: gold 4, silver 8, bronze 1, and the fourth score
  group correctly gets nothing
- Rendered glyph counts match the tiers exactly, and the medal precedes the learner name in the row
- All 16 svg ids across the two course badges are unique, so the artwork cannot cross-reference
- `plural()` was rendering "13 persons" on five screens. Fixed with an irregular map, which then
  exposed three verb-agreement breaks ("2 people is covered", "12 people has booked"); all fixed
- Course badge holder counts (10 and 8) match `learners.html`'s `ALREADY` roster exactly, not a
  second invented number
- The individual scores spread from 75 down to 4 across 12 distinct values. The first derivation
  sliced the year into twelfths, rounded almost everybody to one course, and produced a ten-way tie
  at the top; the preview is what exposed it, which is the argument for previews
- Both states render, the award dialog carries no Badge ID field, class audit clean both directions

## 7. Open questions

1. **Should this be on at all?** It is off by default and the screen does not push. If nobody at
   Skypoint can name what it is for beyond "engagement", that is an answer.
2. **Do points need to mean anything outside the app?** A points balance that buys nothing is a
   number. If it converts to something real, the amounts here should be set against that.
3. **Who may award points by hand, and is there a ceiling?** Right now any administrator, any
   amount.
4. **Does a leaderboard, even a team one, sit right with your customers' HR policies?** Ranking
   teams is safer than ranking people, but it is still ranking.
5. **Where does this live in the nav?** It is a settings-level feature and sits at the tail, above
   Help; on the dashboard it is under the existing Settings divider. The other nine screens do not
   have that divider, which is a nav inconsistency worth resolving separately.
