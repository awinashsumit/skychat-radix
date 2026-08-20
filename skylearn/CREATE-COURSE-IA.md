# skyLearn Create Course: research and information architecture

Module 2. Why `course-create.html` is shaped the way it is. The dashboard's reasoning is in
[`DASHBOARD-IA.md`](DASHBOARD-IA.md); the shared visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What was wrong with the screen this replaces

One page, roughly twenty controls, six collapsible sections all expanded at once. Only
**Course Title** was marked required.

That last fact is the diagnosis. The system already knew that nineteen of the twenty fields were
optional, and still gave them equal weight, equal size and equal position. The user had to work
that out by reading all of them.

Specific problems:

- **It asked for settings before the thing existed.** Certificate duration, gamification level,
  intro video and price are properties of a course. There was no course yet.
- **Status was a dropdown set to Draft.** A course you are creating is always a draft. Offering
  the choice implies you could create a live course, which you cannot.
- **Duration was a number input.** Asking a human to guess how many minutes a course takes, when
  the system can add it up from the content, is asking the user to do the computer's job.
- **Collapsing did nothing.** All six sections were open, so the accordion was decoration.
- **No sense of what came next.** Fill this in, then what? The screen ended in "Save and Select
  Users", which mixed saving with assigning.

## 2. What the flow actually is

Talking it through surfaced a fact the old screen hid completely: **courses go through an
approval.** An instructor builds one, an admin reviews it, and only then does it reach learners.
Admins can also publish their own work directly.

That changes the object. A course is not a form submission. It is a document with a life, closer
to a contract than to a settings page.

So the screen is two shapes, deliberately:

**A stepper, for building.** Four steps, each genuinely needing the one before it.

1. **Start** — title, delivery, and where the content comes from
2. **Build** — the modules and their content
3. **Settings** — certificate, price, gamification level, category
4. **Compliance** — which state requirements are covered

**A status, for getting it live.** Draft, In review, Approved, Live.

The split matters. A stepper only moves forward, and approval does not: an admin can send a
course back. Modelling "changes requested" as a step would need an arrow pointing backwards
through a control that cannot express one. It is a status, shown as its own strip above the
stepper, with a badge when the course has been sent back.

> Reference points, for the record. Tripadvisor's checkout is a fair wizard: sequential, ends in a
> transaction, done once by a stranger, and it keeps a summary rail visible throughout. ProDeal's
> contract flow is fair too, and its last steps are process states rather than forms, which is
> exactly the pattern the approval needs. The third reference, a guest-house form cut into six
> pages where step three held two fields, is what we avoided: ceremony without logic.

## 3. Where the twenty fields went

| Field | Now |
|---|---|
| Course title | Step 1. The only required field in the whole flow. |
| Course type | Step 1, as Delivery. It changes what the later steps mean, so it belongs early. |
| Status | **Deleted.** Carried by the lifecycle strip instead. |
| Duration | **Deleted as an input.** Summed from the modules and shown in the rail. |
| Description, Category | Drafted by AI from the document. Category is editable in step 3. |
| Thumbnail, Template | Defaults. Editable on the course after it exists. |
| Course code, Price, Gamification level, Certificate, Hide from catalogue | Step 3. |
| Intro video | Content, not settings. Belongs with the modules in step 2. |
| Time options | **Moved out of the course entirely.** When someone must finish is a property of
  the assignment, not of the course. The same course assigned to two roles can have two
  deadlines. |

**Price and gamification level are kept** at the client's request (2026-08-17). Price carries a
hint that it applies to external CE only, and a note stands: if no one ever sells a course, the
field should leave the product rather than sit at zero forever.

## 4. Delight, and what it means here

The ask was for "wow". For a compliance director between two other tasks, wow is not
illustration. Four things carry it:

1. **The form fills itself.** Drop a policy PDF and the modules, questions, description and
   duration come back written. The screen becomes a review, not a blank form. Checking finished
   work feels good; filling twenty empty boxes does not.
2. **The work is visible.** Not a spinner. A short list that names each real task and ticks it
   off: reading the document, finding topics, writing modules, writing questions, checking Ohio.
   Same twenty seconds, completely different feeling.
3. **The compliance check.** After building, the screen says *this covers 4 of the 6 topics Ohio
   requires, and post-fall assessment is missing*. One click adds a module for the gap. That is
   the product doing the expert's job, and nothing else in the category does it.
4. **The rail.** A summary card that fills in as you go: title, modules, questions, length,
   coverage, and how long the draft took to build. You watch the course become real.

Explicitly avoided: confetti, congratulation copy, a step counter that greets you on every
course. The user builds twenty of these a year.

## 5. Two roles, one screen

**The instructor** walks the four steps and ends on *Submit for review*. The course locks, and
they can recall it if they submitted too early.

**The admin** sees the same four steps and ends on *Publish course*, because they approve their
own work. When they open a submitted course they get a review bar with *Approve* and *Request
changes*.

Requesting changes writes a real note, and the note is specific because it is generated from the
compliance gaps rather than from a blank text box. The instructor sees it at the top of the
screen, edits, and resubmits. That is the loop, and it is why the lifecycle is a status.

**There is no role switch on screen.** A first draft put a Signed-in-as toggle in the page header
so both halves of the loop could be walked. It was cut: a prototype control that looks like a
product feature teaches the wrong thing about the product. Role comes from the URL, exactly as it
comes from the session in the real thing.

**The default is Administrator** (client direction, 2026-08-17). Every screen in this prototype is
the administrator's, so the create screen opens as one too: publish directly, no submission step.
The instructor half of the approval loop is reached with `?role=instructor`, and the reviewing-admin
half from the dashboard's review queue, which opens a course already submitted.

## 6. Consequence for the dashboard

Building this proved a dashboard decision wrong. `DASHBOARD-IA.md` argued for cutting a "drafts
awaiting review" tile, on the grounds that authoring chores are not workforce risk and that a tile
pointing at an unbuilt module would be a dead control.

With a real approval step, reviewing submitted courses is a genuine admin task with a real
destination. **Courses waiting for your review** now sits in Needs attention. It is rendered as a
link with a chevron rather than a filter button, because it navigates instead of filtering, and
the affordance should say which.

**The Create course dialog was also deleted.** It asked which source to start from, then handed
off to a create screen whose first step asks the same thing. One question, asked twice, with a
modal in between. The dashboard CTA now opens the create screen directly.

## 7. Still open

1. **Does price have any real use?** See above.
2. **Can more than one admin review**, and does it need a named reviewer or a queue anyone can
   pick from?
3. **What happens to a live course when it is edited?** Does it need re-approval, and do learners
   mid-course get the old version or the new one? This is the next real decision, and it affects
   whether the lifecycle needs a "revising" state.
4. **The instructor dashboard** is confirmed as a separate module. The nav in this file is the
   admin's; an instructor should see fewer items and no compliance rollups.

---

## 8. The build step is a builder, not a list (2026-08-17)

The client walked through the product's real authoring flow: fill a metadata form, save, land on
an empty course page, click "Add First Unit", fill a second form, click "Save and back to units",
repeat. Six modules cost twelve page changes, and you never see the course as a whole while you
write it.

Four things were broken, and they are worth recording because they are easy to rebuild by
accident.

1. **Three screens, three mental models.** A form with a tab, then a hub with five tiles, then a
   form again with the tiles still present but inert. Nothing carried across.
2. **Management tools shown before there is anything to manage.** A course with zero modules
   offered *Users and Progress: 0 learners* and *Reports: view analytics*.
3. **Three words for one thing.** "0 units", "Add First Unit", "Add Content Unit".
4. **The AI generator was a separate nav item.** The product's headline feature was not offered
   at the moment a course is created, which is the only moment it matters.

**Decisions taken.**

- **"Module" is the only word.** A module contains a lesson or a quiz. Three nouns, no synonyms.
- **Step 2 is a two-pane builder**: outline on the left, editor on the right, saving as you type.
  No "save and back", no empty landing page, no leaving the screen. The outline stays visible so
  the whole course is in view while one piece is edited. Same surface for both paths, full when
  the AI wrote it and near-empty when it did not.
- **The five management tiles do not belong on the build path.** Users, progress, files, rules
  and reports are for running a live course. They become a course page that exists after
  publishing. That is the next module.

## 9. Completion tracking

The client left this to us. The three options are not alternatives, they are different kinds of
evidence, which matters in a product sold on surviving a survey:

| Option | What it proves |
|---|---|
| A checkbox | Someone clicked. Weakest. |
| A question | Someone knew the answer. This is competency. |
| A timer | Someone spent the time. This is **seat time**, which several states mandate in hours. |

So it is **set once at course level**, defaulted to *a question*, and overridable on a single
module from the builder rather than asked fresh on every one. Setting a course to checkbox-only
raises a warning in both Settings and Compliance, because a checkbox will not defend a
state-required course in front of a surveyor.

## 10. Visibility, and why it is wired to compliance

The old per-module "Active" toggle hid a module from learners. Three changes:

- **Renamed to visibility**, because "Active" does not say what it does.
- **Hidden entirely while the course is a draft.** Nothing is visible to learners yet, so the
  control would be six switches that do nothing. It appears once the course is live.
- **Moved onto the module row** in the outline as an eye, with hidden modules dimmed and labelled,
  so what learners actually get is legible at a glance rather than six clicks away.

And the part that makes it worth doing: **a hidden module does not count toward compliance
coverage.** Each module carries the requirement it satisfies, and coverage is computed from
modules that are present *and* visible. Hide the post-fall module and Ohio drops from 6 of 6 back
to 5, and the warning returns. Two features that would otherwise be unrelated now cannot be used
to accidentally hide your way out of compliance.

---

## 11. The content section, designed for people who are not confident with software

The client's constraint, stated plainly: the authors **are not expert computer users**. They are
training directors and senior nurses who were handed the LMS. They use email and Word, they are
interrupted constantly, and they are afraid of breaking something. That constraint decides
everything below.

Also settled: **"Activity" and "Assignment" were invented by AI**, not requirements. They are cut
rather than designed around.

### The problem with the existing Add menu

Fifteen item types in six groups, offered at the moment the author is least able to choose. Worse,
several are not content at all:

- **SCORM / xAPI / cmi5 and iFrame** are file formats and embed mechanics. Nobody in this audience
  knows those words, and they should never have to.
- **Survey** is feedback about a course, collected after it. It is not part of the course.
- **ILT** is a *delivery mode*, already chosen in step 1. A live session inside a self-paced
  course's content list is a modelling error.
- **Section** is a container, not a sibling of the things inside it.

### What replaced it: three fixed parts, no choices

A module has the same three parts every time, in the same order, with the same headings:

1. **What learners read** — a text box, already holding what the AI wrote
2. **Pictures, video and files** — one drop target
3. **Questions** — with the correct answer marked

There is **no content-type menu, no block palette, and no module type**. Not a shorter menu: no
menu. Every module looks identical, so there is exactly one layout to learn and the author can
never assemble a wrong one.

This is a deliberate departure from both references. Udemy picks one type per lecture, Eduverse
builds a lesson from blocks. Both are good for confident authors and both make the author
responsible for structure. For a policy turned into compliance training, the words carry it, media
supports it, and questions check it. Fixed order is the feature.

### One drop target, no formats

There is a single "Drop a file here" for everything. A PDF, slides, an image, an MP4 or a training
package all go to the same place, and the product reports what it found in ordinary words:
*Document*, *Picture*, *Video*, *Training package*. **Format detection instead of format
selection.** That single decision deletes six of the fifteen menu items.

### Other choices that follow from the constraint

- **Autosave, with "Saved" visible.** No save button to forget, no lost work after an interruption.
- **Undo, not confirm.** Deleting a module offers *Undo* in the toast for six seconds. A confirm
  dialog stops the person who was right; undo rescues the person who was wrong and costs the first
  person nothing.
- **Drag is never the only way.** Move up and Move down buttons sit under the outline. Drag defeats
  trackpads, touch and unsteady hands, and this audience has all three.
- **AI is phrased as the job, not the technology.** "Make it shorter", "Use simpler words", "Write
  questions for me". Not "Generate" or "AI Assistant".
- **The gate messages say what to do**, not what is invalid: "Every module needs a name", "Add at
  least one question, or completions will not prove anything."

### Questions became real

The earlier build stored question text only, which is a list of prompts, not a knowledge check.
Each question now carries three or more answers with the correct one or more marked, which is both
what a learner needs and what the completion-evidence argument in §9 depends on.

### Taken from the references

- **Udemy**: the picker opens *in place*, never on a new page, and "add from library" sits beside
  upload.
- **Eduverse**: AI at the point of work rather than as a separate nav item, and a review nudge
  after generation, since AI output must be checked before a surveyor sees it.

Not taken: bulk edit, bulk upload, section summaries, plan upsell banners, and sections themselves.
Compliance courses are short and flat. If a ninety-day onboarding curriculum ever needs grouping,
modules become the group and nothing has to be renamed.

## 12. One step at a time (client direction, 2026-08-17)

The client walked through Udemy's curriculum editor on video and named it the best way for any
person to create a course. What makes it work is not its list of content types; it is the
**interaction discipline**: everything happens inside the list, in place, one small decision at a
time. Click "+ Curriculum item" and a picker opens right there. Name the lecture inline. The row
appears. Click "+ Content" on the row and the panel opens inside the row. You are never taken to
another page and never asked two things at once.

The two-pane builder from §11 showed the whole module at once. Good for an expert scanning; too
much at once for this audience. Rebuilt as a **single-column accordion**:

- The course is a flat list of module cards. Click a card to open it in place; click again to
  close. One open at a time.
- **Adding a module asks one thing: its name**, in an inline row inside the list, exactly where
  the module will appear. Enter commits, Escape cancels. The new module opens with just the
  writing box ready.
- Inside an open module, the three parts from §11 are unchanged, but **empty parts are single
  "+" buttons** ("+ What learners read", "+ A picture, video or file", "+ Questions"), and the
  editor for a part appears only when asked for. This is Udemy's "+ Description / + Resources"
  pattern exactly. A part with content is always shown.
- After AI generation the list lands **collapsed**: six named rows with their counts. That is
  the review view; open the one you want to change.

**What was deliberately not copied.** Udemy's type groups (Role play, Coding & labs, Practice
test) are its catalogue for technology courses; none of those exist in fall-prevention training.
The fixed three-part module from §11 survives unchanged underneath the new interaction. Sections
also remain out: at six modules the list is its own overview, and Udemy needs sections because
its courses run to hundreds of lectures.

## 13. Sections are in (client decision, 2026-08-17, reversing §11 and §12)

Twice this document argued sections out: compliance courses are short, the flat list is its own
overview, Udemy only needs sections at hundreds of lectures. The client asked for sections in the
Udemy walkthrough and asked again after the accordion shipped without them. **Two direct requests
outrank a designer's tidiness argument, and the earlier sections of this document were wrong to
keep overriding the first one.** Recording that plainly so the next reader sees the decision and
its history, not a clean story.

The shape is Udemy's: **a course is sections, a section is modules, a module is its three parts.**

- Every course has at least one section. The AI generates them ("Understanding the risk",
  "Preventing falls on your shift", "When a fall happens") the same way it generates modules.
- The section name is always editable in place and reads as a heading until touched.
- Adding a section immediately opens the inline add for its first module, so an empty section
  never sits around as a dead box. A section can only be removed while empty, and only when it is
  not the last one.
- **Move up and Move down cross section boundaries**: at the top of a section, another press moves
  the module into the section above. The buttons alone can reach any position, so drag remains a
  shortcut, never a requirement. Dropping onto a module adopts that module's section.
- Modules of a section stay contiguous in the flat list, so every total, the compliance
  derivation and the review flow are untouched by grouping.

## 14. The empty-state illustration (client artwork, 2026-08-17)

The client supplied `Building Light.svg` and `Building Dark.svg` for the build step's empty state,
replacing the book tile. Verified before use: **same 35 paths, byte-identical geometry**, 16 fills
differing between the two.

Per rules.md §14 they are **not shipped as two files**. They are merged into one inline SVG:

- The 19 paths whose fill differs by theme carry a class (`il-blob`, `il-screen`, `il-frame`,
  `il-stand`, `il-base`, `il-ground`, `il-chrome`) and flip under `:root[data-theme="dark"]`.
  Both themes render exactly what the client drew; the theme toggle drives it.
- The 16 identical paths (skin, hair, clothes, the cream notes) keep their literal fills. They are
  artwork, and artwork is the documented exception to the no-raw-hex rule.
- **The amber is the one fill bound to a token.** The client used `#FFB31C`, which is `--accent-9`
  exactly, so `il-brand` reads the token and the illustration will follow the brand if it ever
  moves rather than drifting away from it.
- The DS empty-state draws a tinted tile behind its icon; `.empty-art.is-ill` cancels it, because
  this artwork carries its own background blob and would otherwise sit in a box.

Should more art arrive in this set, the same merge applies: verify the geometry matches, class the
differing fills, bind anything that is exactly a token.

## 15. Row actions on hover (client direction, 2026-08-17)

Udemy reveals a lecture's actions on hover: rename, delete, a contextual "+ Content" or
"+ Questions", and the drag handle. Adopted, with three changes made because our authors are not
confident computer users and hover-only controls are the classic way to strand them.

**What appears on hover of a collapsed module row**

- **A contextual "+"** naming the module's actual gap: "+ Text" when nothing is written, then
  "+ Questions" when there is no check, then nothing once the module is complete. It opens the
  module with only that part revealed and the cursor already in it. One click from noticing a gap
  to filling it.
- **Rename**, which turns the row itself into a text box. No need to open the module to fix a
  typo. Enter keeps, Escape restores, clicking away keeps, because a non-expert who clicks
  elsewhere means "I'm done", not "throw it away".
- **Copy**, which duplicates the whole module (text, files, questions) directly below the
  original and in the same section. The copy deliberately does **not** inherit the module's
  `covers` claim: one module satisfies a state requirement, and two both claiming it would make
  the compliance count a lie.
- **Delete**, with the same undo toast as the in-body delete. Available even on the last module,
  because undo makes a guard unnecessary and the step gate already blocks a course with none.

**The three changes from Udemy's version**

1. **They also appear on keyboard focus.** `:focus-within` reveals them, so tabbing through
   reaches every action. Hover-only would make them unreachable without a mouse.
2. **They are permanently visible where there is no hover.** `@media (hover: none)` pins them on,
   so a touch user is not hunting for a state that cannot occur.
3. **They are hidden once the card is open**, because the expanded body already carries rename,
   move, and delete. Showing both would put two delete buttons on one module.

The principle is the same one applied to drag versus the move buttons: **hover is a shortcut, and
every action it exposes is still reachable without it.** Nothing lives only behind a hover.

## 16. The Continue deadlock (found 2026-08-17)

Reported as "Continue is not working". The gate logic was correct at every step, but one of the
gates created a trap.

Step 2 refused to continue without **at least one question**. The way to say a course does not
need questions is Settings, where completion can be set to a checkbox or a timer. **Settings is
step 3.** So an author building a policy acknowledgement had to reach a setting that step 2 would
not let them reach, and the message told them to add a question they did not want.

The question requirement is now **advice, not a gate**, and the advice names the remedy: "You can
add them now or set completion to a checkbox in Settings." The compliance step still warns when
checkbox-only completion is paired with a state-required course, which is the place that judgement
actually belongs.

The general rule this produced: **never block a step on a condition whose remedy lives further
along the flow.** Anything that fails that test is advice.

Blocked reasons are also styled differently from advice now. A reason you cannot continue is
`--warning-text` and medium weight; a suggestion stays a quiet hint. They previously looked
identical, which made a hard stop read as a note.

## 17. One complete course, for reviewing rather than building

Every entry point started a course from nothing, so there was no way to look at a finished one.
`?course=falls` loads a complete course: title, delivery, source document, three sections, six
written modules with a file and eighteen answered questions, settings chosen (FALL-101, State of
Ohio certificate valid 12 months), and **two Ohio topics still missing**, so the compliance step
has something real to say rather than a clean bill of health that teaches nothing.

It opens on step 1 with all four steps already unlocked, so any step can be inspected in any
order, and the module list starts collapsed because a finished course is something you review
before you edit.

The course list's edit action points here, which is the honest route: editing an existing course
should show that course.

**A bug this exposed.** `?status=review` set the modules but never the sections, so four of the
six modules belonged to sections that did not exist and simply did not render. The reviewing
admin was looking at a two-module course. Both paths now go through one `loadSample()`, so they
cannot drift apart again.

## 18. Publishing gets a screen, not a toast

Publishing was a three-second toast. It is the end of the whole job, so it now gets a moment,
built from the client's `Complete Light.svg` / `Complete Dark.svg` — merged into one inline SVG
the same way as the empty-state art: 37 elements, identical geometry, 20 fills classed and
flipped by theme, 17 kept literal as artwork.

The reference (Eduverse) shows a rocket, confetti in the heading, and a **sales page link**. Three
changes for this product:

- **No confetti and no emoji in the heading.** It reads as unserious on a HIPAA or fall-prevention
  course, and the copy rules already forbid emoji.
- **A sales page link is meaningless here.** This is internal compliance training; nobody buys it.
  The genuine next step is assigning it, so the primary action is **Assign it to learners**, going
  to the screen built in module 5.
- **It reports what was actually made** rather than only saying "everything is set": sections,
  modules, questions, minutes, and Ohio topics covered. All five read from the same course data,
  so the screen cannot congratulate you on a course that is not there.

**And it tells the truth about compliance.** A course published with gaps says so, and names them:
*"It went live still missing post-fall assessment and documentation and reporting. A surveyor
counts topics."* Only a course with no gaps gets "survey-ready". A success screen that celebrates
an incomplete course is worse than no success screen, because it teaches the author that finishing
the wizard is the same as being compliant.

Three ways out, in order of what is most likely wanted: assign it, keep editing, back to courses.
Escape closes it.
