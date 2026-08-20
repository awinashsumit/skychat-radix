# skyLearn AI Course Generator: research, audit and information architecture

Three stages in one file: source, generating, review. The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What this flow is actually for

The screens call the last stage *Review: Test*, and that word is the whole module. Everything
after the generate button is a **review** task, not an authoring task, and those are different
jobs with different shapes:

| Authoring | Reviewing |
|---|---|
| You know what you want; the screen helps you type it | The screen has an opinion already; you are checking it |
| Blank fields are the starting point | Filled fields are the starting point |
| Effort scales with what you write | Effort scales with what you **read** |
| Done when you stop | Done when you are **satisfied** |

The screens being replaced are built as authoring. Every stage after generation is a form: title,
objectives, content, then six slides of stacked text inputs, then the quiz. It is a competent
authoring UI pointed at a job that is not authoring.

> **A generated course arrives looking finished.** Every lesson has a title, every slide has a
> heading, every question has four plausible options, and none of that is evidence that any of it
> is correct.

So the reviewer has two options, and both are bad: read all thirty-seven slides and eighteen
questions, which nobody does, or publish unread, which everybody does. **The job of this module is
to make the first pass so the reviewer does not have to.**

## 2. Audit of the screens being replaced

**Publish is enabled on unreviewed AI output.** `Save Draft` is greyed out and `Publish Course` is
amber and live, on a screen where not one slide has been opened. The one mistake this flow can
make is the recommended action. (Same defect class as `Mark Completed` on the sessions module.)

**Nothing is flagged, so everything reads as equally finished.** Six lessons, thirty-seven slides,
eighteen questions, and no signal about which of them is weak. Generated material has predictable
faults, and none of them are surfaced.

**One expanded lesson is roughly 1,800px of form.** Screenshot 5 is a single lesson: title,
objectives, content, then six slides each with a type dropdown, a voiceover box and three or four
fields, then the quiz. There is a `Collapse` button at the bottom, which tells you how far you
scrolled. Six of those in a unit is unnavigable.

**The output is a deck, and it is never shown as a deck.** Slides are reviewed as `Heading`,
`Bullets (4)`, `Voiceover Script` in stacked text inputs. The reviewer never sees what the learner
will see, on a screen whose whole purpose is judging whether what the learner sees is any good.
The system can clearly render them: there is a template preview on the first screen.

**Nothing connects the course back to the document.** This was generated from a 24 page PDF.
Nothing says which pages a lesson came from, and nothing counts the pages that ended up in no
lesson at all. Summarising is lossy, and the loss is invisible.

**Quiz answers are marked but not checkable.** Green ticks show which option is right. The
reviewer's actual question is *is this question fair, and is that answer right according to the
source*, and neither is answerable here.

**Two different things are both called a template.** `Content Template` on the generator screen,
`Video template` on the review screen.

**Video generation is opt-out, pre-selected, and below the fold.** Six toggles, all on, at the
bottom of the Overview tab, above a `Generate Media (6)` button. Generating video for six lessons
is the slowest and most expensive thing this product does.

**The generating state is a bar filling against nothing.** One sentence that never changes for
what is presumably thirty to ninety seconds.

**Unit tabs do not scale.** Three units fit the bar. Eight will not, and the `+` that adds a unit
sits inside the row that navigates between them.

## 3. What replaced them

### Framing

**The same shell as Create course**: header, sidebar, breadcrumbs, content column. The first pass
put this flow in a full-bleed editor with no sidebar, on the argument that reviewing is a task
with a start and an end and the nav is a way to abandon it half done. Sumit overruled it, and the
stronger argument is his: **creating a course and generating one are the same job, so framing them
differently makes the app feel like two products.** Recorded here rather than dropped, because the
focus argument still applies to genuinely modal work if any turns up later.

The tabs and the two course-level actions share one line inside the content column, so the review
stage still reads as a single object without needing its own chrome.

### Source

One card for the source, one for the settings, and a real preview of the slide template rendered
by the same function that draws the slides later, so the preview cannot lie about the output.
`Lessons at most` carries the hint a first-time user needs: *a 24 page document usually makes 5 to
8*. The footer says what pressing the button does: **nothing is published, the draft opens for
review first**.

### Generating

Uses the supplied animation, and replaces the fake progress bar with the six things it is actually
doing. As each step lands it reports **what it found**:

```
✓ Reading Stellar Data Centre Exit Plan.pdf        24 pages
✓ Finding the themes                                3 units
✓ Drafting lessons                                  6 lessons
✓ Writing slides                                   37 slides
✓ Writing quiz questions                           18 questions
✓ Checking its own work              14 things to look at
```

The wait is the same length. It stops being empty, and by the end the reviewer already knows the
shape of what they are about to check — including that last line, which sets the expectation that
this is not finished work.

### Review

The course title, the Draft badge and the two course-level actions are one header row; the unit
tabs sit beneath it. The counts (3 units, 6 lessons, 37 slides, 18 questions) are **one line of
prose, not four KPI cards** — they are context for the queue, not numbers anybody acts on, and the
queue should be the first thing on the page.

**A queue called *Before you publish*, and `Publish` waits for it.** The button reads
`14 things to check first` and is disabled until each is fixed or accepted. Accepting does not
delete the finding; it marks it reviewed and leaves it visible, because the point is that somebody
decided, not that the list went quiet.

Findings are **grouped by kind**, not listed individually. Twenty separate rows is a wall a
reviewer scrolls past; four kinds with counts is a worklist they can finish:

> 5 questions give the answer away
> 1 objective is promised and never taught
> 6 lessons have slides that would play in silence
> 2 gaps between the document and the course

**Every finding is discovered by traversing the output**, not written into the data:

| Check | Why it is the right check |
|---|---|
| The correct option is markedly the longest | The most common artefact in generated multiple choice. A test-wise learner picks the long one without reading the question. It fires on the client's own question 1. |
| An option nobody could choose | *"An external consultant not mentioned"* is from the client's own screen. It makes a four-option question a three-option one. |
| Slides with no voiceover script | The video would sit on that slide in silence, which is only discoverable today by generating the video. |
| An objective never covered by a slide | The lesson promises something it does not teach. |
| A lesson with no source pages | It came from somewhere other than the document. |
| Pages of the document in no lesson | Pages 13–17 are in nothing. Summarising is lossy and the loss is otherwise invisible. |

**Slides are shown as slides.** A thumbnail strip, one selected slide rendered at size, and its
fields beside it. Same `canvas()` function draws the thumbnail and the full slide, so a thumbnail
can never misrepresent its slide. Silent slides are marked in the strip, so the gap is visible
without opening anything. This is what turns 1,800px of form into something a person can scan.

**Provenance on every lesson.** A `pages 1–4` chip in the collapsed row, and `no source` when
there is none.

**Rewrite this lesson** exists, because when a generated lesson is wrong the honest options should
not be *retype it* or *delete it*.

## 4. Verified

Headless, since the preview renderer has been dead for this project.

- 3 units, 6 lessons, 37 slides, 18 questions, matching the screens
- 14 findings, all by traversal: 5 quiz, 6 voiceover, 1 objective, 2 source
- The two quiz heuristics fire on the intended cases and stay quiet otherwise, including on the
  four evenly-sized date options, which are fine
- Pages 13–17 identified as covered by nothing
- `Publish` disabled at 14 open, reading `14 things to check first`, and becoming `Publish course`
  once the queue is cleared
- Every stage and every unit renders; class audit clean in both directions
- The supplied animation had a full-bleed `#f0f0f0` backing rect, which is why it sat in a grey
  square. Removed at the file, so the art is transparent on any surface.
- Two copy bugs caught in verification: the grouped labels read *"2 parts of the document is not
  accounted for"* and *"5 questions would be answered without reading it"* at counts other than
  one. Both fixed.

## 5. Open questions

1. **Where does this live?** It is reached from `Courses` as *Generate with AI*, beside *Create
   course*. `DASHBOARD-IA.md` §6 argued it is a flow rather than a destination, and the sidebar is
   already at ten items. If it wants to be a nav item, something else should leave.
2. **Video generation is not built here.** It should be opt-in, at publish time, with the time and
   cost stated, rather than six pre-selected toggles below the fold. What does it actually cost?
3. **Should a reviewer be able to accept a whole class of finding?** Right now yes, one press for
   all five quiz problems. That is fast and it may be too fast.
4. **Does an accepted finding need a reason?** For a surveyor, *who accepted this and why* is a
   better record than *it was accepted*.
5. **Can the source document be re-read after editing?** If someone fixes page 14 of the PDF,
   nothing re-runs.
