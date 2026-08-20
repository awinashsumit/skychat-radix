# skyLearn Reports: the screens as they are, rebuilt

You asked twice for a re-architecture of this module and rejected both. The third
instruction was the one that stuck:

> No.. didn't liked it. just redesign the screens as it is. Use the same screenshots for reports

So this is not a redesign of the information architecture. It is the **existing Reports
module rebuilt in the Radix flavour** — same tabs, same rail, same drill-downs, same
numbers — with the design-system defects fixed and the interactions actually wired.
The visual contract is in [`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What was kept

Everything. The shape of the module is unchanged:

| | |
|---|---|
| **Five tabs** | Overview, Training Matrix, Timeline, Export, Custom Reports |
| **Six report types in the right rail** | User, Course, Group, Activity, Compliance, Overdue |
| **Rail behaviour** | clicking one **adds a tab**, so the bar grows from 5 to 11 |
| **Two drill-downs** | a learner opens five sub-tabs, a course opens two |

The period switcher (All time / Today / Yesterday / Week / Month / Year / Period), the
stat line, the area chart with three series, the coloured event badges on the timeline,
the nine export cards, the empty Custom Reports state with **Create with AI** — all
present, in the same places. The matrix is the one exception: same data, redesigned at
your request (§2).

## 2. What changed

Only the execution.

### The numbers are the screenshots' numbers

7 learners, 11 course assignments, 2 completed, 2 in progress, 0% avg score.
18 courses, 9 assigned learners, 2 completed learners, 7 in progress, 5% avg completion.
18% completion rate and 3 certificates on the Overview. 48 timeline events. Nine exports.
Every figure on every strip is transcribed from the screens rather than recomputed.

### Under them, one enrollment list

The two drill-downs used to be able to disagree, because each built its own list. Now
`ENROLL` is the single relation and both read it:

```js
const forUser   = n => ENROLL.filter(e => e.u === n);
const forCourse = c => ENROLL.filter(e => e.c === c);
```

Verified: for every learner and every course, if A appears in B's list then B appears in
A's. The course side reconciles exactly — all 18 courses match their stated assigned and
completed counts.

### The training matrix, redesigned

The rebuilt-as-is version was rejected, and it deserved to be. Measured, the grid was
**24% dense** &mdash; 10 filled cells out of 42 &mdash; so three quarters of the screen was
empty, and the diagonal headers were spending 210px of height to show truncated titles.

| | before | after |
|---|---|---|
| Header | rotated &minus;45&deg;, 210px, truncated | horizontal, wrapped, 62px, complete |
| Rows | 82px | 46px |
| Status colour | blue / green / amber | one ordered ramp, `--seq-2/4/6` |
| Empty cell | blank | a small grey dot, so it reads as checked |
| Row totals | none | *2 of 3* with a bar |
| Column totals | none | *1/3* under each course |
| Sort | as entered | worst first |
| Headline | none | *8 courses still outstanding* |

The two changes that matter most are not cosmetic. **Status is ordered** &mdash; not enrolled,
enrolled, in progress, complete &mdash; so it belongs on a single-hue ramp rather than three
unrelated colours; one glance now reads *how far along*. And **at 24% density the totals are the
report**: the cells are the detail behind the answer, not the answer.

### The learner record, rebuilt from the screens you sent

My first version of this drill-down was invented rather than transcribed, so it was wrong
in almost every particular. Rebuilt against the six screens:

| | |
|---|---|
| Header | icon-only back button, name with a **LEARNER** badge, email beneath, **Export CSV** right |
| Strip | **six** cells, above the tabs — completed courses, in progress, total courses, avg score, points, level |
| Overview | *Activity (Last 90 Days)* chart, with a **Progress Overview** ring card beside it |
| Courses | Course / Progress / Score / Enrolled on / Completed, with `ENROLLED` pills |
| Gamification | three small cards sized to their content, then the badges empty state |
| Infographic | the poster: blue hero, five-stat strip, Training time, Performance, Badges, Compared to others |
| Transcript | title, the print stamp, **Download all (PDF)**, a *Courses* section, empty state |

The course record now uses the same chrome, so the two drill-downs are one component with
different tabs rather than two designs.

The infographic keeps its own blue-and-orange palette in both themes, deliberately. It is a
printable artefact like a certificate, not an app surface, and a poster that changes colour
with the UI theme is not the same document.

### The chart is drawn, not an image

Three area series over a 15-point axis, in SVG, with the grid, the labels and the legend
generated from the same data. Course completions in brand amber, enrollments grey, logins
blue.

Correctly named, it is an **overlapping area chart with linear interpolation** — not
stacked (each series runs from its own zero, so they must not be read as summing) and not
smoothed. An earlier draft of this doc called it smoothed; the points are joined with
straight segments, which is the honest reading of discrete daily counts.

Three overlapping series is the practical limit, and this is a multi-series chart of
*unordered* categories, so it stays on the categorical palette rather than the sequential
ramp — see [`CHARTS.md`](../CHARTS.md) §3.

### The interactions work

| | before | after |
|---|---|---|
| Search boxes | rendered, filtered nothing | filter every table, on name and on category |
| No-match state | an empty table | an empty state naming the query, with **Clear search** |
| Pagination | static "1 - 7 of 7" | the house pager, driven by the filtered count |
| Theme toggle | in the header, unwired | wired |
| Export buttons | inert | all 15 acknowledge |
| Tab bar | — | `role="tablist"`, `aria-selected`, `aria-controls` onto a real `role="tabpanel"` |

### Two design-system defects fixed at source

Both were in `dashboard.css`, so both are fixed for every page, not patched here.

- **`.table .cell-sub` was declared twice**, one line apart, with different colours. The
  first was dead. Removed.
- **`.stack-3` did not exist** — the DS had `.stack-4` and `.stack-5` only, so this page
  had reinvented it locally. Added to the DS and the local copy deleted. This is the same
  class of drift that `.stack-4` had in `course-create.html`.

## 3. Verified

Headless, since the preview renderer has not responded for this project — stopped and
restarted cleanly, still times out, console empty.

- All 11 tabs render, plus 7 learners × 5 sub-tabs and 18 courses × 2 sub-tabs
- **Tag balance checked on every one of those views**, and on the static document
- No `undefined`, `[object Object]` or `NaN` in any output
- Search narrows on all seven tables; a no-match search renders the empty state
- Timeline filters: 18 / 4 / 4 / 10 rows, none empty
- All seven period chips set an active state
- Class audit clean **in both directions** — no markup class without a rule, no page rule
  without markup
- No duplicate selectors outside `@media` overrides
- Every id the JS reaches for exists in the markup; every input has a label
- All 13 skyLearn pages and all shared assets serve 200 at `?v=79`

## 4. One contradiction carried over, not invented

The source screens disagree with themselves and I have kept both numbers rather than
quietly picking one:

> **User Reports says 11 course assignments. Course Reports says 9 assigned learners.**

Sumit Awinash's row shows 3 assigned; the course tables only account for 1 of them. The
other two belong to courses that do not appear in the course-side counts. His drill-down
now shows what is actually known about him rather than inheriting the 3, so no single
screen contradicts itself — but the two top-level strips still differ, because that is
what the screenshots say.

The same is true of **18% completion rate on the Overview against 5% avg completion on
Course Reports**. Different questions, same eighteen courses, and neither screen says
which is which.

Worth resolving in the real product. Not worth me resolving on your behalf here.

## 5. Open questions

Still unanswered from earlier modules, and all of them touch this screen:

1. Is 95% the real compliance target, and 75 the pass threshold?
2. How are certificates versioned when a course changes?
3. What happens to in-flight learners when a live course is edited?
4. Should a report be schedulable? Emailing the same summary monthly is the genuinely
   repetitive part of this job.
5. Is a PDF needed? Print works, but a surveyor packet usually wants a signature block.
