# skyLearn: UI Checklist (Radix flavour)

The verification contract for the screens built so far. Sections 1 to 10 cover
**Home > Dashboard** (`index.html`); section 11 covers **Courses > New course**
(`course-create.html`) and adds only what is new, since 1 to 8 apply to every screen.

Values bind to `../tokens.css`; no literals except the two documented below.

Why the dashboard holds this content rather than the content it replaced is in
[`DASHBOARD-IA.md`](DASHBOARD-IA.md). Read that before removing anything here.

---

## 1. Grid and layout

- [x] Archetype is **KPI Overview** from the DS layout rules: KPI row, then two `.split-2`
      rows, then a full-width table. No bespoke grid.
- [x] App shell untouched: header `56px`, sidebar `256px`, content `1fr`. Sidebar collapses to
      `0` on the rail toggle.
- [x] Vertical order answers four questions in order: **Am I safe** (KPI row), **what is
      broken** (Needs attention), **is it improving and where is it worst** (trend, by
      community), **who do I act on** (worklist). Nothing on the page fails to answer one.
- [x] Every row is a 2:1 `.split-2`. The heavier column is always the one that carries the
      decision; the 1fr column carries the breakdown that explains it.
- [x] **Cards in a row share one height** (`align-items: stretch`, page-local override). The DS
      default `start` leaves the shorter card floating beside a hole. Stretching turns that
      hole into card padding, which is what reads as a considered grid rather than a stack of
      loose boxes.
- [x] Pairing is by height as well as meaning: 4 exception rows sit beside 3 score rows, the
      chart sits beside 6 community rows. A mismatched pair was the first draft and it left
      250px of dead canvas.
- [x] Content is left-aligned throughout. The only centred block is the `.empty-state` the
      worklist falls back to when a filter matches nothing.
- [x] Breadcrumbs present (`Home > Dashboard`), footer present.
- [x] Responsive: KPI row 4 -> 2 -> 1, splits collapse to one column at 1024px, gaps drop from
      `--space-5` to `--space-4` at the same breakpoint.

## 2. Spacing and density

- [x] Every margin and padding on the Radix scale (`--space-1`..`--space-9`). No off-scale px.
- [x] **Internal <= external.** Card padding is `--space-5` (24px), so the gutter between cards
      is lifted to `--space-5` too. The DS ships `.kpi-row` / `.split-2` at `--space-4` (16px)
      against 24px card padding, which inverts the rule; the page overrides both gaps to 24px.
      This is a fix, not a deviation, and it belongs upstream in `dashboard.css`.
- [x] Sections separated by `.stack-5` (24px). Elements inside a card by `--space-2`/`--space-3`.
- [x] Exception rows `--space-3` vertical padding, hairline separated. Community rows
      `--space-2` with a `--space-1` gap, so the denser list stays scannable at six items.
- [x] Table row height **48px**, one height for the whole table (the DS §4 literal). Header 40px.
- [x] Filter bar is a flush `.card` (`padding: 0`) wrapping `.filter-bar`, so the strip's own
      `--space-3`/`--space-4` padding is the only padding in play.

## 3. Type ramp (Inter, Radix sizes)

Hierarchy comes from the ramp and the two-step text split, never from an invented size.

| Role | Token | Size / line | Weight |
|---|---|---|---|
| Page H1 (one per page) | `--fs-7` | 28 / 36 | Bold |
| Page description | `--fs-3` | 16 / 24 | Regular |
| KPI value | `--fs-8` | 35 / 40 | Bold |
| Card title (`.panel-title`) | `--fs-4` | 18 / 26 | Bold |
| Exception count | `--fs-5` | 20 / 28 | Bold |
| Body, labels, table cells | `--fs-2` | 14 / 20 | Regular / Medium |
| Meta, deltas, subs, axis | `--fs-1` | 12 / 16 | Regular |

- [x] Adjacent steps in use run at a **1.17 to 1.29 ratio** (12 / 14 / 16 / 18 / 20 / 28 / 35).
      That is the Radix ramp, unmodified. Nothing is set below 12px.
- [x] **The H1 outranks every card title by two full steps** (28 vs 18). In the screen this
      replaces, the section headings were within a hair of the page title, so the page had no
      single entry point. One H1, and it wins.
- [x] KPI value at 35 is the largest type on the page and sits top-left, per the DS rule that
      the primary metric takes the largest type and highest contrast.
- [x] `.sc-label` reserves two lines (`min-height: calc(var(--lh-2) * 2)`) so all four KPI
      values land on one baseline no matter how long the label runs. Without it the four
      headline numbers stagger, which is the single most visible way a KPI row looks amateur.
- [x] Numerals that get compared are `font-variant-numeric: tabular-nums`: KPI values, exception
      counts, community percentages, competency scores, the days-past-due column.
- [x] No all-caps micro labels except `.nav-section`, which is DS chrome. The replaced screen
      set every KPI label in 11px tracked caps.

## 4. Colour and theming

- [x] Every colour is a `var(--...)` token. Two documented literals only: the `#242424` dark app
      bar inside `dashboard.css`, and `#fff` for identity text on it, scoped to `.hu-name`.
- [x] **Amber is brand and identity only**: the Create course CTA, the active nav pill, focus
      rings, the row-hover tint. It never encodes a status.
- [x] Status uses red / orange / blue / green with a label beside it every time:
      Expired = `.is-danger`, Overdue and Onboarding stalled = `.is-warning`,
      Expiring soon = `.is-info`, positive deltas = `--success-text`.
- [x] Text and icons on solid amber are `--accent-contrast` (dark), never white.
- [x] Avatars are never amber. Learner avatars take a deterministic chart hue from their
      initials, so the same person is the same colour on every render.
- [x] Charts use `--chart-1` and the target markers use `--fg-subtle`. Amber is not a series.
      A community bar turns `--warning-solid` only when it is genuinely below the 95 target,
      and the target tick is drawn on the same track so the colour is never the only cue.
- [x] Dark theme verified, not assumed: cards separate from the canvas, hairlines still read,
      the segmented track stays recessed against its raised pill, and both bar hues clear the
      dark track.

## 5. Elevation (one strategy for the whole page)

- [x] **Every in-flow surface is a bordered `.card` or `.table-wrap`.** Not one raised card,
      no mixing. `.table-wrap` and `.card` resolve to the same border, radius and background,
      so the worklist reads as the same kind of surface as everything above it.
- [x] Shadows are reserved for surfaces that float: `.popover` notifications `--shadow-4`,
      `.dialog` `--shadow-5`, `.toast` `--shadow-4`. Each keeps its crisp 1px ring layer.
- [x] Inputs, the scope dropdown and surface buttons carry an **inset 1px ring**, not a CSS
      border, so focus swaps the ring with zero layout shift.
- [x] Radii on the Radix scale: cards and the table `--radius-4`, dialog `--radius-5`, buttons
      and rows `--radius-3`, badges `--radius-2`, tracks and avatars `--radius-full`.
- [x] Z-order, highest last: scope menu and notification popover `1200`, overlay `1000`,
      toasts `1400`. A toast confirms an action taken from inside the dialog, so it outranks it.

## 6. Component states

Every interactive element defines rest / hover / active / focus-visible / disabled.

- [x] **Exception rows** are `<button aria-pressed>`: hover `--gray-3`, selected `--row-accent`,
      focus a 2px `--focus-ring`. Pressing one filters the worklist; pressing it again clears.
- [x] **Community rows** behave identically and set the page scope, which keeps the header
      switcher and the ranked list as two views of one piece of state rather than two controls.
- [x] **Scope dropdown** is a DS `.dropdown` with `aria-expanded`, a `.dropdown-menu` of
      `.list-item`s, a leading check on the selected row, and a menu whose right edge tracks
      the trigger's. Verified closing on all five paths: outside click, Esc, picking an
      option, re-clicking the trigger, and at rest on load. No native `<select>` on the page.
- [x] **Anything toggled with `[hidden]` has a matching `[hidden] { display: none }` rule.**
      `[hidden]` is a user-agent rule, so any author `display` on the element beats it and the
      element never hides. This bit `.btn`, `.tag` and `.dropdown-menu` on this screen alone;
      the last one shipped a scope menu that could not be closed. Grep for `.hidden =` and
      confirm each target has the escape hatch.
- [x] **Segmented range** syncs `aria-selected` with `.is-active` and re-renders the trend and
      every delta. It is a real control, not a styled label.
- [x] **Create course dialog** opens focused, traps nothing it should not, closes on Esc, scrim
      click and Cancel, restores focus to the trigger, and keeps its primary disabled until a
      source is chosen. Cancel is `.btn-surface`; the only amber solid in the dialog is the
      one that commits.
- [x] Table rows are not clickable and do not pretend to be: no cursor change, no hover-only
      action. The worklist is a read-and-act list, and the act happens in Learners.
- [x] Search debounces at 160ms and filters the worklist, which is exactly what its placeholder
      promises. A control that promises more than it does is the failure this project has
      already shipped twice.

## 7. Motion

- [x] Micro-interactions 120ms (`background-color` on rows and buttons). Toast entry 200ms
      ease-out, 4px rise plus fade.
- [x] No chart entry animation. A compliance figure that counts up is a figure you cannot read
      for the first second.
- [x] `prefers-reduced-motion` neutralises everything through the DS stylesheet.

## 8. Content and accessibility

- [x] **Every figure on the page derives from one dataset**, so the KPI row, the exception
      list, the community panel, the competency scores, the notifications and the worklist
      cannot disagree. Stock values roll up exactly: six communities sum to 1,284 learners,
      98 at risk, 7 expired plus 57 overdue plus 34 stalled. Period deltas are rates and
      therefore do not sum across scopes, which is true of the real thing too.
- [x] **The worklist never overstates its sample.** It says "Showing 8 of 98 at risk" and names
      where the rest live. Filtering to an exception restates the denominator for that
      exception.
- [x] Status is never colour alone: every badge carries a word, every below-target score carries
      a "Below threshold" badge, every delta carries an arrow and a sentence.
- [x] Deltas encode **good or bad in the colour and direction in the arrow, and the two are
      allowed to disagree**. Fourteen fewer overdue learners is a down arrow and a green
      delta. The DS `.is-up` / `.is-down` names direction, so it would force them to agree and
      paint an improvement red. Page-local `.is-good` / `.is-bad` say what they mean.
- [x] Icons: Lucide only, stroke 1.75, `currentColor`. 18px in nav and tiles, 16px on buttons,
      14px on deltas, 36px in the empty state.
- [x] No emojis. No em-dashes.
- [x] Contrast: text at or above 4.5:1, UI glyphs at or above 3:1. Amber text is `--accent-11`,
      never step 9.
- [x] Charts carry `role="img"` with a label; decorative sparklines are `aria-hidden`. The
      search input has a visually hidden label. Icon-only buttons carry `aria-label`.
- [x] The worklist empty state is the one centred block, and it appears only when a real filter
      combination has no rows.

## 9. Information architecture

- [x] Primary nav is **nine destinations**, inside the 5 to 9 rule. The screen it replaces had
      fifteen across two invented groups, one of which ("Tools") was a junk drawer.
- [x] No single-item sections. The old "Home" group wrapped one item and is gone; Dashboard is
      simply the first row.
- [x] **Actions are not destinations.** "AI Course Generator" was a nav item; it is a flow, and
      it now lives inside the Create course dialog as a starting point.
- [x] Sub-features are tabs inside their parent, not nav rows. See `DASHBOARD-IA.md` for where
      each of the six removed items went.
- [x] Header controls are not duplicated in the sidebar, and nav items are not duplicated as
      shortcut tiles in the content. The replaced screen spent its best real estate, the top of
      the right column, on four tiles that linked to four nav items at the same depth.
- [x] **Header holds identity and status only; page filters live with the page.** Points, the
      notification bell, the theme toggle and the account are shell. Community scope sits in the
      filter bar next to the comparison period, because the two together define what every block
      below is showing. Splitting filter state across the header and the body was the earlier
      arrangement and it made the scope easy to miss.
- [x] The points chip is a `.presence` pill, not a green badge. Green means success in this
      system and a score is not a status. It carries no hover and is not a button, because it
      does not do anything when clicked.

## 10. Deferred, by design

Not gaps found in a pass. Scoped out on purpose, so a later contributor does not restore them
without the reasoning.

- **Sidebar links other than Dashboard are inert.** This is a module-by-module build and the
  other modules are not designed yet. They are the only inert controls on the page, they are
  confined to the shell, and each one lands as its module ships.
- **Content pipeline tiles** (drafts awaiting review, assessments awaiting grading) are not on
  this dashboard. They are authoring chores, not workforce risk, and every other block here
  answers a compliance or competency question. A tile whose only action is to open a module
  that does not exist would be a dead control in the most valuable column on the page. They
  belong on Courses and Assessments respectively.
- **Role and state filters** are not in the filter bar. Community scope carries state already,
  and a second filter that silently changes six blocks needs a filter summary and a reset
  pattern that should be designed once, for every module, rather than invented here.
- **Drill-through from a worklist row to a learner record.** The row shows everything needed to
  triage; opening the record is the Learners module's job. Rows therefore do not look clickable.

---

# 11. Courses > New course (`course-create.html`)

Sections 1 to 8 above apply unchanged. This section records only what this screen adds.
The reasoning is in [`CREATE-COURSE-IA.md`](CREATE-COURSE-IA.md).

## 11.1 Two shapes, and why

- [x] **A stepper for building, a status for going live.** Four build steps (Start, Content,
      Settings, Compliance) each need the one before it, so a stepper is honest. Approval can
      move backwards, and a stepper cannot express that, so Draft / In review / Approved / Live
      is a separate status strip with a "Changes requested" badge.
- [x] The stepper is a **real DS component** added to `dashboard.css`, not a page-local hack,
      with a comment stating when it may and may not be used. skyCRM and skyChat can take it.
- [x] **No step is a slice of a form.** A long form cut into pages is the failure mode this
      screen was reviewed against. Settings is the closest to that risk and earns its place
      because it is the last thing an admin approves.
- [x] Only completed steps are navigable, and the cursor and hover underline appear only on
      those. The affordance arrives with the ability.

## 11.2 Progressive disclosure

- [x] **One required field in the entire flow**: the course title. Everything else has a
      default or is computed.
- [x] Duration is never asked for. It is summed from the modules and shown in the rail.
- [x] Status is never asked for. A course being created is a draft, so the control is gone.
- [x] The contextual payload for a chosen source (drop zone, library list) opens **under the
      chosen card**, not on a new screen, so the choice and its consequence stay together.

## 11.3 Delight, measured against the brief

- [x] The AI path **fills the form** and the screen becomes a review rather than a blank form.
- [x] Generation shows **named work ticking off**, not a spinner: reading the document, finding
      topics, writing modules, writing questions, checking Ohio. Each row moves from pending to
      doing to done with a check.
- [x] The pulse animation is the only looping motion on the screen, and
      `prefers-reduced-motion` collapses the whole sequence to 60ms per step.
- [x] The compliance step names the **specific missing topics** and offers a one-click fix that
      really adds a module and really flips the requirement to Covered.
- [x] The summary rail fills in as you go and reports how long the draft took.
- [x] No confetti, no congratulation copy, no step counter greeting on every course.

## 11.4 Roles and the approval loop

- [x] The primary button's label is derived from role and status, never hardcoded: *Continue*,
      then *Submit for review* for an instructor or *Publish course* for an admin.
- [x] Submitting **locks the content**. `locked()` gates editing, module removal and gap fixes,
      and is asserted for all five statuses.
- [x] An instructor who submitted early can **recall**, rather than being stuck.
- [x] Requesting changes writes a **specific note built from the real compliance gaps**, shown
      to the instructor as a warning callout at the top of the screen. A rejection that says
      only "needs work" is not shippable.
- [x] **No role switch on screen.** An earlier draft had a Signed-in-as toggle in the page
      header; it was a prototype control standing in for authentication, and it looked like a
      product feature. Role now comes from the URL, which is where it comes from in the real
      product too. The admin path is reached by its real entry point, the dashboard's review
      queue, which lands on a course genuinely awaiting approval.

## 11.5 No dead controls

- [x] Every trigger on the screen does something: the three source cards, the drop zone, the
      library picks, module add and remove, all three Settings dropdowns, the gap fix buttons,
      the role switch, Back, Continue, Save and exit, Approve, Request changes, Recall, Publish.
- [x] The Settings dropdowns are backed by real option lists with a selected check, Esc to
      close and outside-click to close. An earlier draft rendered them as triggers that opened
      nothing; that was caught in review and fixed.
- [x] Source and library cards are `<button role="radio">` inside a `role="radiogroup"`, not
      bare labels, so they are focusable and operable by keyboard.

## 11.6 Consistency with the dashboard

- [x] Same shell, same header, same nav. The sub-screen **highlights its parent** (Courses) per
      the DS rule, with a `Home > Courses > New course` breadcrumb.
- [x] **The dashboard's Create course dialog was deleted.** It asked "how do you want to build
      it", which is exactly what step 1 asks, so the same question was put twice with a modal
      in between. The CTA now goes straight to the create screen.
- [x] **Courses waiting for your review** was added to the dashboard's Needs attention, which
      reverses an earlier decision to leave it out. It is a link with a chevron, not a filter
      button, because it navigates rather than filters.
- [x] Inline styles are data-driven only. Exactly one remains, the selected-check opacity in
      the settings menu, where the value is the state.

## 11.7 Verification status

- [x] JavaScript parses; every handler is reachable from a rendered trigger.
- [x] Flow logic asserted headlessly: gate messages on step 1, generated totals (6 modules,
      18 questions, 25 minutes), Ohio coverage (4 of 6, the correct two missing), gap closing,
      and `locked()` across all five statuses.
- [ ] **Not visually verified.** The preview renderer was unavailable for this session, so the
      screen has not been seen rendered. Layout, the stepper connectors, dark theme and the
      1080px rail collapse all need an eye before this is called done.

## 12. Sessions

Applied on `sessions.html`. New rules this module surfaced.

- [ ] **A status that describes time is computed, never stored.** "Scheduled" on a class that
      finished eleven days ago is how a compliance backlog stays invisible. Derive the phase from
      the clock and the data, and let the stored field hold only what a human chose (open,
      cancelled, completed).
- [ ] **The button that writes a permanent record is disabled until the record is complete**, and
      says what is missing. Never style an irreversible, under-evidenced action as the
      recommended one.
- [ ] **Two states are not enough for anything a human fills in by hand.** Tick and cross cannot
      express "not looked at yet". Every marking control needs an unmarked state that is visible
      in the row, not just in the control.
- [ ] **A rule is a sentence.** `COURSES · ALLOTTED TO NO-SHOWS` is a column name. "If someone
      does not attend, they are enrolled in HIPAA Training online, due seven days after this
      session" is the same fact, readable.
- [ ] **Dates carry the month in words.** `6/8/2026` is 8 June to half the world and 6 August to
      the other half. Never render a bare numeric date in a UI a person has to act on.
- [ ] **Times carry the place's timezone, not the server's.** `(UTC)` on an in-person class in
      California is wrong for everyone who has to attend it.
- [ ] **Round a derived quantity once, at the source.** If the card rounds 3.97 to 4.0 and the
      total multiplies 3.97, the arithmetic on screen contradicts itself.
- [ ] **A temporal list is grouped by time and the worklist is pinned above the calendar.** Sort
      by what is costing something, not by what is next.
- [ ] **Filters do not count their own options.** `All Modes (1)` reads as one result.
- [ ] **A status column says what a thing *is*, never what you owe it.** "Attendance due" is a
      task; "Ended" is a status. Tasks belong in the row's action, where they can be pressed.
- [ ] **Say a thing once per row.** If a group header, a badge and a cell subline all carry the
      same fact, two of them are noise. Count the repeats before adding the third signal.
- [ ] **One control per row.** A rack of hover icons makes the reader decode glyphs. Use the
      single chevron the other tables use, and promote it to a real button only for the rows that
      owe work.
- [ ] **Default a worklist to open items.** Filtering history out by default is what keeps the
      visible status set small enough to read at a glance.
- [ ] **Match the form to the job, not to the module next door.** Authoring earns a stepper;
      scheduling is seven fields and earns a dialog. Copying the heavier pattern is not consistency.
- [ ] **A create form should brief the user, not interrogate them.** If the system knows who is
      waiting for this, what it will clash with, or who it will exclude, say so live, before the
      button is pressed. A blank form assumes the user already knows everything.
- [ ] **Warn on judgement, block only on invalid data.** A double-booked room may be deliberate;
      an end time before the start never is.
- [ ] **Class audit, both directions, every module.** This one found `.stack-4` missing from the
      design system, which `course-create.html` had been working around with a local copy.

## 13. Groups

Applied on `groups.html`. New rules this module surfaced.

- [ ] **A saved set of people is a rule, not a list, unless a rule genuinely cannot describe it.**
      A list is a photograph of the day it was taken. In anything compliance-shaped, a list that
      silently goes stale is people who quietly stopped being assigned mandatory training.
- [ ] **If both kinds exist, the kind is visible on every row**, and a drifted list says by how
      much, in people, where it lives. "3 members" is a count with no denominator; "9 people who
      match this are not on it" is the fact.
- [ ] **The most consequential choice is the first question in the dialog, with the safe option
      as the default.** If the form cannot express the choice at all, every object it creates is
      the wrong kind by construction.
- [ ] **Show what nothing is pointed at.** A rule with no audience, an audience nothing uses, a
      person no rule covers. Zero rows is not empty, it is a finding.
- [ ] **Never ask an administrator to invent a machine identifier.** Generate the key from the
      name and hide it unless someone goes looking.
- [ ] **Two dialogs of the same shape are worded identically or they are one dialog.** Caps
      labels against sentence case, and four different placeholder styles, on one screen.

## 14. KPI cards

Applied on `courses.html` and `learners.html`. The card now lives in `dashboard.css` as `.kpi`,
not in two page stylesheets.

- [ ] **Label, then value, then what changed.** A number means nothing until you know what it
      counts, so the eye should not land on "1,984" before it lands on "Total enrollments".
- [ ] **One colour per card at most, on the last line, only where it points somewhere.** Four
      accent colours across four cards do not say four kinds of thing; they say a palette was
      available. This is the single biggest tell of a generated-looking layout.
- [ ] **No icon that repeats the label.** A book beside "Total courses" carries no information.
      Drop the tile and the padding does the work instead.
- [ ] **No uppercase tracked labels.** Called out in the dashboard audit as a decade-old tic,
      then shipped anyway on the next two screens. Sentence case.
- [ ] **No decorative left edge.** A coloured bar on the side of a card is ornament unless the
      colour is categorical, and here it never was.
- [ ] **Every card has all three lines.** If a card has no third line, either write an honest one
      or the set is not parallel. Never pad it with `&nbsp;`.
- [ ] **A component used on two pages belongs in the design system.** These two copies had
      already drifted apart in padding, icon size and label case before anyone noticed.

## 15. White canvas

`--color-page` is `#ffffff` in light mode. The page, the sidebar and every table header are the
same white as the cards on them.

- [ ] **Panels are told apart by their hairline, not by a tint.** Every card, table and panel
      already carried `1px var(--border-subtle)` (`#d9d9d9`), which is what does the separating
      now. Anything given a flat grey fill *instead of* a ring will disappear on this canvas.
- [ ] **Four things stay grey, and none of them is a page background:**
      the **table header band** (see §16); **hover states**, which need somewhere to go;
      **control tracks** (segmented, progress, spin-button prefix, question badge), which are the
      groove a control sits in; and the **certificate preview stage**, because the certificate
      itself is white paper and a white stage would erase it.
- [ ] **Dark mode is untouched.** Only the light-mode token changed; `--color-page` stays
      `--gray-1` in dark.

## 16. Table density

- [ ] **Row height follows the number of lines in the cell.** Almost every table here carries two
      lines per row, a name over an email or a title over a category. 48px left them touching;
      64px is the fix, and height is the cheapest legibility there is.
- [ ] **The table gutter matches the card gutter.** 24px. A table inset less than the card around
      it reads as cramped however tall the rows are.
- [ ] **The header is a tinted band, not white.** It is a legend inside a white card, not a page
      background, so it can hold the one grey left in the app and separate labels from data
      without a heavy rule. This is the exception to §15, and the only one.
- [ ] **Caps are allowed on a column header and nowhere else.** §14 rules out uppercase tracked
      labels on KPI cards, where they decorate a number that is already the largest thing on the
      card. A column header is a persistent legend for everything beneath it; at 12px, caps plus
      tracking is what lets it recede and stay scannable at the same time.
- [ ] **Narrow columns opt out of the gutter.** A 44px checkbox column cannot carry 24px of
      padding on each side. Set its padding explicitly rather than letting the default overflow it.

## 17. Reviewing generated output

Applied on `ai-generate.html`. Anything a model produces and a person signs off on.

- [ ] **Reviewing is not authoring.** Authoring scales with what you write; reviewing scales with
      what you read. A form is the right shape for the first and the wrong shape for the second.
- [ ] **Generated output arrives looking finished.** Every field is filled and none of it is
      evidence of correctness. If the screen does not do a first pass, the reviewer reads
      everything (nobody does) or publishes unread (everybody does).
- [ ] **The screen finds the faults, by traversal, not by being told.** Write the checks against
      the known failure modes of the generator, and let them fire on real output.
- [ ] **Publish waits for the queue**, and the button says how many things are outstanding.
      Never make "ship the unreviewed thing" the enabled primary action.
- [ ] **Accepting records a decision, it does not delete the finding.** The list is the audit
      trail; going quiet is the opposite of what it is for.
- [ ] **Group findings by kind.** Twenty rows is a wall a reviewer scrolls past. Four kinds with
      counts is a worklist they finish.
- [ ] **Show the artefact as the artefact.** If the output is a deck, render slides. Reviewing a
      deck as stacked text inputs means the reviewer never sees what the learner sees, which is
      the entire question.
- [ ] **One render function for the thumbnail and the full size.** A separately drawn thumbnail
      can lie about its slide.
- [ ] **Carry provenance.** Which pages of the source a lesson came from, and which pages ended up
      in nothing. Summarising is lossy and the loss is invisible unless something counts it.
- [ ] **Two ways of making the same object are framed the same way.** Creating a course by hand
      and generating one both live in the app shell. A full-bleed editor for one of them makes the
      product feel like two products.
- [ ] **An active tab is dark text under a brand-coloured rule, never brand-coloured text.**
      `#a05a00` is the brightest step of the Skypoint amber ramp that clears 4.5:1 on white, and
      it reads brown. Put the bright amber on the 2px underline, where it carries no text
      contrast, and leave the label near-black and semibold. The DS `.tab-nav-item` already did
      this; two page-local tab styles had drifted.
- [ ] **An inline element silently ignores `width`, `height`, `overflow` and vertical margin.**
      A `<span>` given a box does not error, it just renders at content size and spills. The slide
      thumbnails shipped this way: each slide drew at full size, overflowed its frame and dragged
      its caption to a different baseline. If a class sizes a box, the element carries
      `display: block` or sits inside a flex or grid parent, which blockifies it. Sweep for it:
      find every class used on a `<span>` whose rule sets width/height/overflow, and check it
      declares a display or its wrapper is a flex container.
- [ ] **Scale a preview by real numbers, not by eye.** Frame width divided by page width is the
      transform. 128 / 400 = .32. An inline `transform: scale(.34)` with `width: 294%` beside it is
      two guesses that have to agree, and they did not.
- [ ] **A column of stacked spans is a flex column, not spans you remembered to set
      `display: block` on.** This bug has now shipped four times in this project on four different
      classes. Put `display: flex; flex-direction: column` on the *container* and the children
      cannot run together, whoever writes them next. Audit for it by finding any rule with
      `flex: 1` and `min-width: 0` that is not itself a column.
- [ ] **Content is left aligned, like every other screen.** A centred max-width column inside a
      left-aligned app reads as a different page. The exception is a waiting state, which has
      nothing to align to.
- [ ] **A waiting state centres on the whole area, not on the content column.** It has nothing to
      align to, so a max-width column leaves it visibly off to one side.
- [ ] **Check supplied artwork for a backing rect.** An exported SVG often carries an opaque
      canvas-coloured rectangle, which shows up as a grey square on any other surface.
- [ ] **Paired header actions are one flex child, not two.** In a `space-between` header, two
      loose buttons spread across the row and the secondary one lands in the middle.
- [ ] **A waiting state says what it is doing and what it found.** The wait is the same length
      either way; only one version leaves the user knowing what they are about to review.

## 18. Incentives

Applied on `recognition.html` and `recognition-settings.html`. Anything that hands out points, badges, levels or rank.

- [ ] **Check that a reward can be reached, in the units the user actually accrues.** 64 badges on a
      doubling ladder ending at "complete 128 courses" is 29 of 56 tiers that nobody reaches before
      the median learner leaves. Divide the threshold by the real annual rate and compare it to real
      tenure before shipping the ladder.
- [ ] **Check a reward set for badges that say the same thing.** Two rules that award to the same
      people are one badge written twice, and it is invisible until you compute the overlap. Test
      every pair: identical is always a defect; strictly-implied usually is; and a badge almost
      everybody holds separates nobody.
- [ ] **Never award a badge for nearly doing the thing.** "Within two courses of a complete set"
      went to 33 people, 17 of whom had not finished.
- [ ] **A tiered ladder needs a number that keeps climbing.** A yearly required set resets, so
      tiers built on it run off the end of a career. Count-based tiers belong on lifetime totals or
      nowhere.
- [ ] **Show how many people hold each reward today.** A badge nobody holds is either set too high
      or rewarding something that is not happening, and both are worth knowing on day one rather
      than in year two.
- [ ] **State the economy on the screen that sets it.** Put "what a normal year earns" next to the
      rules. It is the only way anyone notices that a daily login pays 365 and a completed course
      pays 10.
- [ ] **Never reward presence or volume.** Logins and upvotes measure neither learning nor
      competence, and both are trivially gamed.
- [ ] **One rule per outcome.** Three independent level rules with all three switched on produced a
      column reading "132 points, Level 1" above "117 points, Level 2".
- [ ] **Rank over a window, and publish only the top.** Two properties make an individual board
      safe, and most boards have neither. **All-time** ranks tenure: a new joiner can never catch
      somebody who started five years ago. **Publishing everybody** names the people at the bottom,
      and where most of the board sits near zero that is the whole point of it. A rolling period
      plus a top-N cut fixes both; everyone below sees their own position privately.
- [ ] **Preview a ranking against real data before shipping it.** A derivation that looks fine in
      the abstract produced a ten-way tie at the top here, and only the preview showed it.
- [ ] **Configuration and consequence are separate destinations.** What you set once at setup and
      what you read every week are different jobs. Collapsing tabs into one long page is the same
      mistake rotated ninety degrees: the wall moves from horizontal to vertical.
- [ ] **A reading surface should answer "is this working", not just "what happened".** Put the
      metric next to the outcome it is supposed to drive. If the top of the leaderboard is not the
      top of the compliance report, the points are paying for the wrong thing, and only a screen
      showing both can say so.
- [ ] **If you cannot explain a concept in one sentence, delete it rather than document it.**
      A level was an unnamed number restating points, on a product whose badge ladder was already a
      level system. Two mechanisms for one idea; the nameless one went.
- [ ] **Anything a person can grant by hand keeps a visible record, with the reason.**
- [ ] **One master switch, not one per tab plus one per row.** If a feature needs five tabs of
      switches, the tabs are the problem.
- [ ] **Pluralise through a map, not `+ 's'`.** "13 persons" shipped on five screens here. And
      once the noun is right, check the verb: fixing it exposed "2 people is covered" and "12 people
      has booked" at three call sites.
- [ ] **Prefer the raster when the asset is finished artwork.** Transcribing an exported SVG by
      hand loses whatever you did not notice — here an inner shadow, which changed the gold. A PNG
      cannot drift from the source and has no ids to keep unique. Give it `width`/`height` so the
      layout does not reflow while it loads.
- [ ] **Paging is a view of the list, not the list.** Anything that judges the whole set — totals,
      tiers, cross-checks — must read the full collection, or the numbers silently change meaning
      to "on this page".
- [ ] **When an icon carries the meaning, the word moves to the accessible name.** Dropping visible
      "Gold / Silver / Bronze" labels is fine; dropping them from the `aria-label` is not.
- [ ] **Inlined SVG artwork needs per-instance ids.** Gradients, filters and clip paths in an
      exported asset carry document-wide ids; render it twice and every copy references whichever
      the browser saw first.
- [ ] **Reproduce baked-in text as real text.** Label paths in an exported badge cannot wrap, cannot
      be read aloud, and cannot take a different course name.
- [ ] **A ranking with real ties needs a real tie rule before it needs a medal graphic.** Row
      position hands out places arbitrarily when several people share a score. Use standard
      competition ranking (equal scores share a place; the next place skips the count that tied)
      and say so on screen when a tie changes how many medals are handed out.
- [ ] **Decorative colour (medals, rank) is a literal swatch, not an accent token.** Reusing the
      brand colour for a medal makes the medal look like the product's own chrome. Give it an
      explicit light/dark pair, the same discipline as any other illustration colour.
- [ ] **A fact does not go in settings.** A badge with nothing to configure — awarded automatically,
      no threshold to tune — belongs on the reading surface only. Putting it in settings implies a
      knob that does not exist.
- [ ] **Reuse the one existing dataset rather than inventing a second answer to the same question.**
      A badge's holder count and another screen's roster describing the same fact must be able to
      disagree only if one of them is wrong. Point both at the same array.
- [ ] **A hand-awarded point needs a reason, and the reason is shown to the recipient.** Points
      that arrive unexplained read as a bug.

## 19. Discussions

Applied on `discussions.html`. Any screen where users write to you.

- [ ] **Count the rendered items against the underlying records.** Four defensible views of the
      same data on one page rendered 43 items for 16 posts, each appearing three times. If the
      ratio is above 1:1, the sections are duplicating, not organising.
- [ ] **One signal per fact, per row.** A red tag reading "Needs a person" beside a red icon
      beside a red edge is one fact stated three times. Pick the one that carries words and drop
      the rest. Colour used only to restate a label is decoration.
- [ ] **A record belongs to exactly one row; the row says which kind it is.** Classification goes
      in a tag on the row, not in which section the row sits in. Otherwise every additional
      classification multiplies the page.
- [ ] **A group of related records is one row, not N rows plus a summary card.**
- [ ] **Filters narrow one list. Sections add lists.** Reach for filters — then check the filter
      earns its place too.
- [ ] **A control for the default state is a label, not a filter.** If one option is always
      selected on arrival and a second is just the sum of the others, only the third is doing work.
- [ ] **Search runs across everything, not inside the current filter.** Scoping search to the
      selected tab makes the app claim "nothing matches" about records it holds. If the filter and
      the search disagree, the search wins.
- [ ] **A worklist must be emptiable.** An item that stays in the queue after you have done the
      thing it asked for trains people to stop reading the queue. Move it, and change what it says.
- [ ] **Ask what the *reader* of this screen has to do**, not what the writers were doing. A forum
      index serves the people posting. An administrator needs a queue: what is unanswered, what
      repeats, what is not a question at all.
- [ ] **Repetition is a content defect, not a support queue.** Several people asking the same thing
      about the same lesson means the lesson is unclear. Offer the fix as the primary action; the
      individual answers are the secondary one.
- [ ] **A card for a systemic problem does not disappear when you handle the symptoms.** It changes
      what it asks for. Answering four people does not make the lesson any clearer.
- [ ] **Some of what arrives is not the thing the box was for.** Incident reports, staffing
      problems and policy conflicts get posted wherever there is a text field. Detect them, route
      them to a named person, and leave them visible so nobody thinks they vanished.
- [ ] **Put a clock on anything waiting for a human.** Unanswered is not a state, it is a duration.
- [ ] **When one action operates on a group, check exactly what is in the group.** "Answer all 4"
      matched a lesson rather than a question and would have swallowed a fifth post that needed
      escalating.

## 20. Navigation

- [ ] **Every page carries a byte-identical sidebar.** Order, labels, the active item, and which
      item holds `nav-tail`. Six pages here had drifted: three still said *Gamification* after the
      rename, and five carried a `Settings` divider the other seven did not.
- [ ] **An item in the nav is a promise that something is there.** Four of thirteen items had no
      screen behind them. Placeholders are not free: they pushed the two newest real destinations
      below the fold, where they read as missing rather than as unscrolled.
- [ ] **`margin-top: auto` sinks its own item *and everything after it*.** Put it on the last item
      only. On the pages where it sat on a divider, four items went to the bottom of the sidebar
      together.
- [ ] **Check a nav against the viewport, not against the ceiling.** Nine items fit; thirteen did
      not, and nothing in the markup says so. Count how many are visible without scrolling.
      Measured properly since, from `dashboard.css` rather than by eye: items are `min-height:
      36px`, the sidebar has **no gap** and 12px of padding, so *n* items come to `24 + 32 + 36n`.
      Fifteen items is **596px**, which clears a 768px viewport (704px after the header). An
      earlier note here said 540px for eleven; that used an estimated 40px item and a 2px gap
      that does not exist. Read the stylesheet, do not estimate the row height.

## 21. Reports

Applied on `reports.html`. The module was rebuilt **as the existing screens**, at your
instruction, after two re-architectures were rejected. What follows is what that rebuild
enforced; §21b records the research those rejections overruled, so nobody re-derives it
from scratch and quietly changes the module back.

- [ ] **Rebuilding "as it is" still means fixing the execution.** Same tabs, same rail,
      same drill-downs, same numbers — and every dead control wired, every search box
      actually filtering, every empty state written.
- [ ] **A search box that renders but filters nothing is worse than no search box.** Seven
      tables here had one. All seven now narrow on name and on category.
- [ ] **Filtering to nothing needs an empty state that names the query.** An empty table
      with text still in the box reads as broken. Say what was searched, offer to clear it.
- [ ] **A record must agree with itself.** The strip at the top of a drill-down counts the
      rows the tab below is about to list — not the roll-up carried down from the table you
      clicked. Opening a learner used to show *3 assigned* above a list of one.
- [ ] **Two views of one relation read from one list.** `ENROLL` is the single source; the
      learner's Courses tab and the course's Users tab are both filters over it, so they
      cannot disagree. Assert it in both directions.
- [ ] **Transcribe the source numbers, do not recompute them.** When the brief is "the same
      screenshots", a figure you derived that differs by one is a bug, not an improvement.
- [ ] **Carry a source contradiction across visibly; do not silently pick a side.** These
      screens say 11 course assignments in one place and 9 in another. Both are kept, and
      [`REPORTS-IA.md`](REPORTS-IA.md) §4 says so plainly.
- [ ] **A `role="tablist"` owes you a `role="tabpanel"`.** Half the roles is half a promise:
      add `aria-selected` on the tabs and `aria-controls` pointing at a real panel.
- [ ] **Check tag balance on generated markup, on every state.** String-concatenated HTML
      fails silently. 11 tabs, 7 learners × 5 sub-tabs, 18 courses × 2 sub-tabs, plus both
      no-match states — all parsed.
- [ ] **A stripe of dividers set by `+` breaks when the grid reflows.** `.kcell + .kcell`
      draws a rule down the middle of column one at the two-column breakpoint. Re-state it
      as `:nth-child` inside the media query.
- [ ] **One `h1` per page.** A panel inside a tab gets an `h2`, however much it looks like a
      page of its own.
- [ ] **CSS written before the markup will describe markup that never gets built.** Every
      defect on the first learner drill-down came from this: the stylesheet was written from
      the screenshots, the render functions hours later, and nobody reconciled them.
      `.d-back` was styled as a 40px icon square but rendered as a text button, so the label
      escaped the box. `.d-n h1` never matched, because the name rendered as a `<span>`.
      `.ring-v { fill }` never applied, because the value rendered as an HTML `<span>`
      outside the SVG instead of a `<text>` inside it.
- [ ] **Assert every descendant selector against rendered output, not against the template.**
      `.foo bar` with no `<bar>` under `.foo` is a rule that silently does nothing, and it is
      invisible to a plain class audit — which passed clean on this file while the screen was
      broken. Render every state, concatenate, and check each descendant rule matches.
- [ ] **An SVG `<circle>` fills black unless told not to.** Setting only `stroke` gives you a
      solid disc, not a ring. `fill: none` and an explicit `stroke-width` both belong on the
      element, and the `viewBox` has to match the size the CSS gives the wrapper.
- [ ] **Text inside an SVG is sized in user units, not pixels.** Check the widest label
      against the shape that has to contain it before trusting it fits.
- [ ] **Rotate column headers only when you are out of horizontal room.** Rotation is a
      trade: it buys narrow columns and costs height, legibility and complete labels. With six
      courses the matrix had room to spare, and the rotation was spending 210px of header to
      show truncated titles. Horizontal, wrapped, two-line labels came in at 62px and read
      straight.
- [ ] **A status that has an order should be drawn as one.** Not enrolled &rarr; enrolled &rarr;
      in progress &rarr; complete is a ramp, not four unrelated hues. Drawn on `--seq-*` it
      reads as *how far along* at a glance and needs no legend to decode.
- [ ] **A sparse matrix needs its totals more than its cells.** At 24% density the grid is
      mostly empty, so the row and column summaries are doing the work: per-learner
      *2 of 3* with a bar, per-course *1/3* in the header, and a headline count of what is
      outstanding. The cells become the detail behind the answer rather than the answer.
- [ ] **Sort a matrix by what you want people to act on.** Alphabetical makes you read all of
      it to find who to chase. Worst-first puts them in the first row.
- [ ] **Draw the empty state of a cell.** A blank cell reads as a rendering gap; a small grey
      dot reads as *checked, nothing there*. Same information, one of them trusted.
- [ ] **A width on a table cell is a suggestion until `table-layout: fixed`.** Under the
      default auto layout the browser stretches columns to fill the container, so a matrix
      declared at 62px rendered at 240px: 97px rows, chips marooned in whitespace, and every
      course title still truncated. Fixed layout plus `width: max-content` made the same
      markup dense and readable without touching the design.
- [ ] **Diagonal headers have arithmetic.** A label rotated by θ needs `W·sin(θ)` of header
      height. At −55° a 128px header buys 156px of label; at −45° it buys 181px. Choosing the
      shallower angle bought 25px of title back *and* made the text easier to read.
- [ ] **Sticky cells lose collapsed borders.** A `position: sticky` first column needs its own
      `background` and a `box-shadow` edge, or the boundary vanishes as the grid scrolls under it.
- [ ] **A legend swatch should be the thing it explains.** Ours were bare squares overridden
      to 20px while the real cells carried a tick at 24px — close enough to look like a bug.
- [ ] **When the brief is "match this screen", transcribe it — do not reconstruct it from a
      description.** My learner drill-down was invented: five strip cells instead of six, the
      strip below the tabs instead of above, a text back button instead of an icon, no role
      badge, no print stamp, and an Overview that bore no relation to *Activity (Last 90 Days)*
      plus a Progress ring. Every one of those was visible in a screenshot I already had.
- [ ] **A printable artefact keeps its palette in both themes.** The infographic is a poster,
      like a certificate or an earned badge — a document whose colours change with the UI theme
      is not the same document. Pin the hexes and say why in a comment.
- [ ] **Fifth occurrence of run-together siblings.** `.prog-t` held a `<b>` and three
      `<span>`s with no column, so a whole card rendered as one paragraph. The fix is always
      `flex-direction: column` on the *parent*, never `display: block` on each child — and
      the sweep is: for every container with two or more inline children, does it stack or is
      it horizontal on purpose?

## 21b. Overruled, and why it is written down

Research from the two rejected passes. **Not applied** — the client's design is the spec.
Kept because the findings were measured, not asserted, and because the next person to open
this module will otherwise measure them again.

- Five screens showed the same five columns at different scopes; scope is a control, not a
  screen.
- 18% completion on the Overview against 5% on Course Reports, same eighteen courses,
  nothing saying which question either answers.
- Of 48 timeline events, nine were one person bulk-editing eight courses in an afternoon.
  That is an audit trail, not analytics.
- Export sat on its own tab, away from the nine things it exports.
- Six of eleven views duplicated Learners, Courses, Groups or the dashboard.

And the lesson from the *replacement*, which failed for the opposite reason — 972 words and
two charts on landing, 120 words before the first number:

- [ ] **A correct screen that nobody wants to read is not a correct screen.** "Boring,
      confused about what to do, too much to read" is a design verdict, not a preference.
- [ ] **Removing a duplicate chart is not the same as needing no chart.** Cutting an
      Overview that restated the dashboard was right; replacing it with 880 table cells and
      no graphics was not.
- [ ] **Flag a concern once, then build what was asked.** Three reversals in this app now.
      The doc is the right place for the argument; the screen is not.

## 22. Automations

Applied on `automations.html`. Any screen that acts on people's behalf.

- [ ] **Before building a rule engine, list what the app already decides declaratively.** Seven
      of the plausible trigger&rarr;action pairs here already worked through Groups audiences,
      requirement sets, certificate issuance and recognition rules. The engine's flagship action
      duplicated all of them.
- [ ] **Two ways to assign is two sources of truth for who is compliant.** In a product whose
      output is evidence, nobody being able to say *why* a course is on somebody's list is a
      defect. Assignment has one owner; everything else can react to it.
- [ ] **Cohorts a rule acts on must be disjoint, and you must assert it.** Written the obvious
      way, somebody both lapsed and overdue matched two rules and was told twice about one
      problem &mdash; and a per-rule rate cap cannot catch it, because it is one message from
      each of two rules. Define every cohort through the same precedence function the rest of
      the app displays, then assert zero overlap.
- [ ] **Show the reach before the commit.** A dialog that writes to real people and cannot say
      how many, or which, is not finished. The count and the names update as the scope changes.
- [ ] **An escalation must reach somebody other than the person ignoring you.** Mark those steps
      differently; a ladder of three messages to the same inbox is not a ladder.
- [ ] **Cap the volume, and say why in the field.** Six overdue courses should not be six emails.
- [ ] **An empty state that says "create your first" gets zero.** After all this time the live
      screen had none. Ship the rules people actually need, switched off, and let the job be
      *review and enable* rather than *invent from nothing*.
- [ ] **Name the module after the job, not the technology.** "Automations" invites people to
      rebuild assignment logic that already exists; the subtitle and the field hints have to
      work harder because of it.
- [ ] **A local rule that thirteen pages define identically belongs in the DS.** Six shell
      classes and `.sr-only` were in exactly that state &mdash; 91 duplicate declarations, none
      in `dashboard.css`. Third occurrence after `.stack-4` and `.stack-3`; check for it when a
      new page copies a shell.

## 23. Surveys

Applied on `surveys.html`. Any screen that collects something from people.

- [ ] **A status you set by hand is a promise the product cannot keep.** The live screen let a
      survey be marked *active* with zero questions, because Status was a dropdown you chose
      before writing one. Derive it instead &mdash; from whether it has questions and whether it
      is attached &mdash; and the bug becomes impossible rather than merely discouraged.
- [ ] **If a thing has to reach people, the model must say how.** Two surveys, zero responses,
      and no Send anywhere on the screen. The audience was never missing: 428 course completions
      were sitting there. Attachment *is* delivery; without it a survey is a document nobody
      posts.
- [ ] **A count without a denominator hides which problem you have.** *0 responses* out of nought
      and out of forty are different facts. Show the rate, and make the denominator the thing the
      survey is attached to rather than the headcount.
- [ ] **Distributions, not averages.** A mean of 3.0 on a five-point scale is either everybody
      shrugging or half the room delighted and half furious, and only one of those needs your
      afternoon.
- [ ] **A ramp on an ordered scale, one step on an unordered list.** Agreement runs disagree to
      agree, so shade can carry it. A list of unrelated options has no *more*, so shading it
      implies a ranking that is not there.
- [ ] **Quote free text with enough context to act on it, and then worry about anonymity.**
      "I still do not know who to call at night" from a CNA at Lakeside Manor is an action; the
      same line unattributed is a mood. Both facts matter, and the tension between them is a real
      open question, not an oversight.
- [ ] **When a tool is used for the wrong job, the tool people wanted is usually missing or
      hidden.** Somebody built a quiz in the survey module while the course builder already had
      one that feeds the competency threshold. That is a discoverability failure, not a user
      error.
- [ ] **Balance braces after any regex surgery on CSS.** Hoisting a rule with a line-oriented
      pattern split a multi-line `@media` block, leaving the opener in one file and the closer in
      another. Neither file throws; both are broken. Counting depth finds it in one pass, and it
      belongs next to the class audit.

## 24. Grading Hub

Applied on `grading.html`. Any screen that is a queue of decisions.

- [ ] **A queue with no producer stays empty forever.** Before styling an inbox, find what fills
      it. `course-create.html` contains the words `grade`, `grading` and `essay` exactly zero
      times &mdash; there is no assignment unit, so 0 Pending was correct and permanent.
- [ ] **If a number is displayed, something has to be able to enter it.** Competency scores were
      shown on the learner record and printed on the dashboard, and no screen in the product
      let anybody put one in. The number arrived from nowhere.
- [ ] **One idea, one vocabulary.** The two halves of this screen used Pending/Graded/All against
      Pending/Approved/Rejected for the same state. Keep the queue states identical and let only
      the decision verbs differ &mdash; a course is not *passed* and a person is not *approved*.
- [ ] **Do not count a state you cannot filter to.** *Returned* had a KPI card and no tab.
- [ ] **Sort a queue by age and say the worst out loud.** "The oldest has been there 41 days"
      is the sentence that makes somebody open it. Alphabetical makes you read all of it.
- [ ] **Draw the threshold on the control, not in a footnote.** A pass mark you have to remember
      is a pass mark people get wrong. Put it on the track, at its actual position.
- [ ] **Gate the decision the data forbids.** Pass is disabled while any domain is below the
      threshold, so nobody can pass somebody the compliance report will later fail. Assert it at
      the boundary, including the one-domain-below case.
- [ ] **State the consequence next to the button.** "Refer sends Dana back to Safe Resident
      Handling and tells their manager" &mdash; an action whose effect is invisible gets clicked
      twice and trusted once.
- [ ] **An empty filter beats a dead tab.** Submissions renders as a real filter returning zero,
      which is honest and keeps the shape for when the producer exists.

## 25. Messages

Applied on `learners.html`. Any screen that lets one person write to another.

- [ ] **Read the placeholder before believing the feature works.** *"Recipient user ID (UUID)"*
      is the whole explanation for an empty inbox: nobody can address a message, so nobody sent
      one. A field nobody can fill is a feature nobody has.
- [ ] **Count the places something can already arrive before adding another.** Five here &mdash;
      the bell, Discussions, Automations, Grading Hub, Surveys &mdash; and a sixth would compete
      with the email people actually read.
- [ ] **A free-text private channel in a healthcare product is a PHI surface.** Somebody will
      type a resident's name into it. An app that teaches HIPAA should not ship an unmonitored,
      unretained channel without that being a decision somebody made on purpose.
- [ ] **Attach the conversation to the record it is about.** It solves addressing (you are
      already looking at the person), context, retention and visibility in one move, and it is
      the same answer Surveys and Automations landed on.
- [ ] **Say who can read it, in the panel.** "Anyone who can open this learner can read it" is
      the sentence that stops somebody treating a training record as private mail.
- [ ] **Open the thread from something that already happened.** A referral writes the first
      message, quoting the score and the threshold, so 25 of 44 records arrive with context
      instead of a blank box. An empty state should mean *nothing has happened*, not *we gave
      you nowhere to start*.
- [ ] **Mark what the system said.** "From the review queue" on an automatic opener &mdash;
      the system saying something and a person saying it are different facts and should not
      look identical.

## 25b. Script order

- [ ] **`defer` on a shared script breaks any inline code that uses it.** A deferred script runs
      *after* the document is parsed; an inline `<script>` runs *during* parsing. Adding
      `<script src="charts.js" defer>` and then calling `Chart.area()` inline threw a
      `ReferenceError` on the first line of `render()` &mdash; so every JS-filled panel on the
      admin dashboard came up blank while its static headings stayed put. Use a classic script
      tag when inline code depends on it, and say why in a comment.
- [ ] **A blank panel under a present heading means the render threw, not that the data is
      empty.** Static markup survives a JavaScript error; everything built in JS does not. That
      shape &mdash; headings yes, content no &mdash; is a thrown exception until proved otherwise.
- [ ] **A harness that loads dependencies itself cannot catch a loading-order bug.** Mine eval'd
      `charts.js` before the page and passed happily while the real page was broken. Check the
      order statically &mdash; is the provider present, non-deferred, and earlier in the document
      than its first use &mdash; and separately assert the panels actually fill.
- [ ] **A stub that returns an object for every id hides the commonest runtime crash there is.**
      A browser returns `null` from `getElementById` for an element that is not there, so
      `$('x').addEventListener(...)` throws and every statement after it in that block never
      runs. My stub answered every id with a fake node, so it passed while the real page was
      dead from the first line of `render()`. Make the stub return `null` for ids absent from the
      markup, and it finds the bug in one pass.
- [ ] **One throw kills everything later in the same block.** Appending new wiring to the end of
      an existing `<script>` means it inherits every earlier failure. That is why the dashboard
      going blank and the role switcher going dead were one bug, not two.
- [ ] **Standardising shared markup can delete something a page depended on.** Propagating one
      nav across twenty pages dropped `id="railBtn"` from the sidebar toggle, and the only page
      that wired it threw on load. Diff what the standard version *removes*, not just what it adds.
- [ ] **A control on twenty pages and wired on one is a dead control nineteen times.** The rail
      collapse was exactly that. Shell behaviour belongs to the shell: give it the id everywhere
      and wire it everywhere, or take it out.
- [ ] **Model shared script scope when simulating a page.** Browsers give every top-level
      `<script>` one lexical scope, so a `const` in the first block is visible in the third.
      Running each block through its own `eval` invents `X is not defined` errors that do not
      exist, which is its own way of wasting an afternoon.

## 26. Enrolment, reference files, and the coach

Applied on `grading.html`, `files.html`, `coach.html`.

- [ ] **A fourth queue of decisions is not a fourth screen.** Enrolment requests have the same
      shape as competency checks and course reviews &mdash; something waiting on a person, with
      an age and two verbs. It became a `KIND` in the existing queue, not a module.
- [ ] **A repository earns its place by being pointed at.** "Upload, organize and share files"
      with no folders, no permissions and no link back to what uses a file is a drawer. Every row
      here says what points at it, who can see it, and when it was last touched &mdash; and the
      two documents nothing points at are surfaced rather than quietly kept.
- [ ] **Say what replacing something will affect.** "The 3 places pointing at it will pick up the
      new version" is the sentence that makes a shared file safe to edit.
- [ ] **An AI answer with no source is worse than no answer in a compliance product.** Somebody
      will act on it. Every reply names the lesson it came from, in the course the learner picked.
- [ ] **Distinguish "not in the material" from "not my job".** They look similar and they are
      not: the first is a content gap that belongs in Discussions with everyone else's, the
      second is a care decision that needs the charge nurse this shift.
- [ ] **Test a safety filter in both directions, and use stems.** The first draft matched
      `\btablet\b`, so *"can I give her tablets early"* fell through to the content-gap branch.
      Twelve clinical phrasings must route to a person and ten ordinary training questions must
      not &mdash; assert both, or the filter is decoration.
- [ ] **Put a learner screen where learners are.** The coach sat in the admin Tools group above a
      My Learning section. An administrator does not need coaching on a course they assign.

## 27. Sign in

Applied on `signin.html`, and to the View As menu on all 27 shell pages.

- [ ] **Read the copy on a screen before rebuilding its layout.** The supplied sign-in carried
      *"Continue wirh Google"* twice, another product's name in the terms line, and a
      `@gmail.com` example on a workforce where all 44 people are `firstname.lastname@skypoint.ai`.
      None of those are design problems and all of them ship.
- [ ] **A heading and its primary button must be the same screen.** *"Start Creating Today &mdash;
      bring your courses to life"* above a button reading **Sign In** is a sign-up and a sign-in
      fused. Counted, 40 of the 44 people who open this will never create anything, so it is a
      sign-in and the sentence under it says what they came for.
- [ ] **Consumer SSO is a compliance defect, not a convenience.** An Apple ID is a credential the
      organisation never issued and therefore cannot revoke when somebody leaves. One button, the
      account IT already manages &mdash; and the reason is printed on the screen rather than assumed.
- [ ] **Say what to do, not what went wrong.** No *invalid credentials*. An empty email asks for
      *"the address your rota and payslips go to"*; the forgotten-password link says the
      administrator resets it **and why** &mdash; the account is the organisation's, not the
      learner's.
- [ ] **Sign in should land you where the header can already take you.** The prototype has three
      roles and a View As switcher. Signing in picks one of the same three, so there is one
      mechanism, not two. Sign out sits under a rule in that menu and gets no radio dot: it is not
      a fourth thing you can look as.
- [ ] **Check contrast in both themes when the colour comes from the sequential ramp.** The ramp
      inverts &mdash; `--seq-4` is the panel's lightest colour in light and among its darkest in
      dark. A `seq-2 -> seq-4` wash measured 5.48:1 in light and **2.52:1** in dark, and no page
      persists a theme today, so nothing would have caught it. Hold a gradient to two adjacent
      steps and put the saturation in the decoration: floor 6.44:1 in both.
- [ ] **Use `--seq-on-light` for text on `seq-1..4`, never a hex.** The token is the ramp's own
      answer to the question and flips with it; a hardcoded brown does not.
- [ ] **Match text colour to what is behind it, not to the theme.** The corollary, and it points
      the other way. The panel now carries a fixed photographic render, which stays light in dark
      mode &mdash; so its copy is plain `#fff` over a scrim, and a theme-aware token there would be
      wrong half the time. Ramp behind it, use the ramp's token; picture behind it, the picture wins.
- [ ] **Measure a scrim under each block of copy, not against the image's brightest pixel.**
      Solving for the brightest pixel is a bound, not a measurement, and it answers a question
      about colour when the failure is about position. Here it green-lit 9.83:1 while the heading
      actually sat at **3.64:1** &mdash; the gradient had thinned to half by the height the heading
      occupies, and the lit desk is directly behind it. Sample the real pixels under each block, at
      several panel shapes, because `object-fit: cover` moves the crop.
- [ ] **Hold a scrim flat through the copy, then fade.** A gradient that starts fading at the
      bottom edge is thinnest exactly where the largest text sits. `.84 -> .82` held to 32%, then
      out by 68%, keeps the whole band at 9.82:1 and still leaves the top of the picture clear.
- [ ] **Ship a hero as a photograph, not a PNG.** The supplied render was a 1.7&nbsp;MB PNG, on the
      one screen shown before anything is authenticated. JPEG q80 is 244&nbsp;KB with the smooth
      wall gradient intact; q70 saves another 36&nbsp;KB and starts to band where the light falls.
- [ ] **Put the palette's nearest colour behind the image.** `--seq-1` under the `<img>` means the
      moment before the JPEG paints is a warm panel, not a white flash.
