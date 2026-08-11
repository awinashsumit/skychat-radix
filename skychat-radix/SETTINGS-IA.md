# Settings: information architecture

Why the settings nav is shaped the way it is. Written down because the three problems
below are easy to reintroduce, and because two of the fixes look like regressions if you
do not know the reasoning.

---

## The organising principle: scope

Every settings screen answers one question first: **does this change affect only me, or
everyone in the instance?** Users get this wrong constantly in admin tools, and the cost is
high, someone sets a "default theme" expecting their own screen to change, or changes their
own language expecting the whole team to follow.

So the rail is grouped by scope, not by feature:

```
YOU
  Account            profile, tenant/instance, my theme, my language
THIS INSTANCE
  People and roles   members, platform admins, roles
  Agents
  Connections
  Branding           accent, logos, favicon, SEO, defaults for new members
  Voice
  Analytics
SUPPORT
  Help and support
```

Instance-scoped panes additionally open with a `.callout.is-info` naming the instance, so
the blast radius is stated on the screen rather than inferred from the nav.

---

## Problem 1: duplicated content

**What was wrong.** Brand customisation and SEO metadata appeared twice, once under General
and again under System Settings > Appearance. Theme and language also appeared twice.

**The subtlety.** These are two different kinds of duplication and they need opposite fixes.

- Brand, logos, favicon, SEO are **instance-only**. There is no personal version of a company
  logo. Two copies of one setting is a genuine defect: whichever screen you edit, the other
  is now lying to you. Fixed by deleting one, they live in **Branding** only.
- Theme and language **legitimately exist at both scopes**. "My theme" and "the theme new
  members start with" are different settings that happen to use the same words. Fixed by
  labelling, not deletion: Account says "Applies to your account only", Branding says
  "Defaults for new members" and "Does not change the theme of existing members".

The general rule: if a control has one true value, it gets one home. If it has a personal
value and an instance default, it appears twice with each copy stating its scope.

## Problem 2: missing pagination

25 members and 9 admins rendered as unbounded lists. Both tables now use the design system
`.pagination` at 10 rows per page, showing range and total ("1 to 10 of 25") plus page
position ("Page 2 of 3"). Search filters the whole set, not the current page, and resets to
page 1, otherwise filtering while on page 3 lands you on an empty screen.

## Problem 3: misleading nomenclature

**"System Settings"** suggested infrastructure, servers, or technical configuration. It
actually held people management, branding, and voice persona, none of which are "system"
in the sense a reader expects. The label was also doing container duty for four unrelated
subjects, which is why it needed a vague name in the first place.

It is gone. Its contents were promoted to their own rail entries under **This instance**,
named for what they contain: People and roles, Branding, Voice.

Other renames:
- General → **Account**. "General" is a bucket name, it tells you nothing.
- Agent Management → **Agents**. "Management" is filler, every settings pane manages something.
- Users → **Members**, and the second tab is **Platform admins**. "Users" and "Admins" as
  sibling tabs implied they were mutually exclusive; they are different scopes entirely
  (instance membership vs platform privilege).
- Admin Status column → **Access**, values "Instance admin" / "Member". "Status" implies
  a lifecycle state like active/suspended.

## Problem 4 (not raised, but load bearing): nav depth

The original nested three levels: rail → tab bar → sub-tab bar (Settings > System Settings >
Users > Instance Users). Three levels of horizontal tabs inside a modal makes the current
position hard to hold, and the back path ambiguous.

Now it is at most two: rail → one tab bar, used only where a single subject genuinely splits
(People and roles → Members / Platform admins / Roles). Nothing nests below that.

---

## Smaller UX fixes carried in the same pass

- **Role names were amber text** on white, which fails contrast. They are `.badge` now, so
  the role reads as a value rather than a link, and carries its own background.
- **Two buttons per row** ("Assign Role" and a red "Remove") on every row of a 25 row table
  is a wall of destructive affordances. The frequent action stays visible; Remove moved into
  a row overflow menu.
- **Removal now confirms.** Removing a member or deleting a role is irreversible and was a
  single click. Both route through `.alert-dialog` naming the specific person or role, and
  stating what survives ("Their chat history is kept", "Members holding it fall back to
  Viewer").
- **System roles cannot be edited or deleted**, so they render without the overflow menu
  rather than with a disabled one.
- **Create Role's submit is disabled until the name is non-empty**, rather than accepting a
  blank role.

---

# Agents

## What the old screens did, and what changed

### Problem 1: three save buttons for one agent

The old detail view split across Overview and Configuration tabs and carried **three
separate save buttons**: "Save Changes" on Overview, "Save Changes" on Model Configuration,
and "Save Settings" on Agent Settings. Nothing stated which button covered which fields, and
switching tabs with unsaved edits lost them silently.

Now: **one save per agent**, in a sticky bar that appears only when something is unsaved,
with Discard beside it. Edits are staged on a draft copy and compared against the saved
record, so the bar is a truthful dirty-indicator rather than a permanently-lit button.

One deliberate exception. The **enable switch applies immediately** and is not part of the
draft. Enabling an agent is a live state change with consequences for other people, not a
document edit you stage. Mixing it into "unsaved changes" would imply you could stage it and
walk away, which is not what happens.

### Problem 2: header cards that only restate the form

Each section was two cards: a header card ("Basic Information: Update the agent's name,
description, and icon") followed by a second card holding the fields. The header card carried
no information the form below did not already make obvious, and cost roughly 120px each.
Each section also had an eyebrow repeating the agent name that was already the page title
directly above.

Both are gone. Sections are a title, one line of purpose only where it earns its place, then
the fields.

### Problem 3: button variant used to encode agent state

Enabled agents had a solid amber "Configure"; disabled agents had a ghost one. That puts two
meanings on one control, breaks the "one solid CTA per view" rule (six solid amber buttons on
one screen), and makes Configure look unavailable on exactly the agents you most need to go
configure. Now Configure is always the same surface button, and the toggle is the only signal
of enabled state, supported by the card dimming.

### Problem 4: create was two screens for three prefilled fields

Template picker, then a form where name, description, and icon were already filled from the
template. Most runs were: click template, click Create. Now both are on **one screen**:
template as radio cards at the top, details below updating live as you pick. You can see what
the template did and adjust in place.

### Problem 5: no way to find anything

Six agents and growing, no search, no way to see at a glance which were live. Added search
and an All / Enabled / Disabled filter.

### Problem 6: drag-only reordering excludes keyboard users

"Drag to prioritize models" was the only way to reorder, which is unusable by keyboard and
screen-reader users. Rows are still draggable, and every row also has labelled up and down
buttons that do the same job. The grip is `tabindex="-1"` so the accessible control is the
one in the tab order.

## Integrity guards the old design left open

These are states the original UI let you reach and then behaved incoherently in.

- **Disabling the default agent.** The default is cleared and the picker says so, instead of
  leaving new chats pointed at an agent nobody can open.
- **Only enabled agents appear in the default picker**, so the pairing cannot be created in
  the first place.
- **Hiding the model that is the default.** The default moves to the first still-visible
  model and announces it. A hidden model's Default radio is disabled, so the contradiction
  cannot be re-created by hand.
- **Deleting an agent confirms**, names the agent, and states what survives.
- **Create is disabled until a template is chosen and name and description are non-empty**,
  rather than accepting a blank agent.
- **New agents start disabled**, stated in the create bar, so creating one never silently
  exposes an unconfigured agent to everyone.

## Second pass: document agents, and making a "vast" area navigable

The document-agent screens added Knowledge and Documents tabs, which changed the shape of the
problem. Notes on what that forced.

### Tabs came back, but only where they are earned

The first pass made agent detail one scrolling page with stacked sections. That was right for
three short forms. It is wrong once Documents exists, because Documents is a searchable,
filterable, paginated table of potentially hundreds of files and does not belong on a shared
scroll with a name field.

So detail has a tab bar again, with one rule: **the tab bar renders only when the agent type
has more than one tab's worth of content.** A General Knowledge agent has Setup alone and gets
a plain page with no tabs. This is what stops the old design's near-empty Configuration tab
(a header card and a single toggle) from ever existing.

Depth is still two levels. The rail is level one; the list-to-detail move is a drill-down that
replaces the pane and has an explicit back, not a level you hold in your head.

### Capabilities are data, not markup

Agent types genuinely differ: General Knowledge has models and instructions but no documents,
Document agents have knowledge and documents but (in the current product) no model picker.
The old design expressed this by hiding tabs, with nothing saying why.

There is now one `CAPS` map keyed by template. It decides which tabs appear and which sections
render. Sections a type cannot use are **removed rather than disabled**, since a disabled
control invites you to work out how to enable it when the answer is "you cannot, not for this
type".

The values match what the current screens expose. If document agents should have instructions
or a model picker, that is a one-line change in `CAPS`, not a hunt through markup. Worth
confirming with product whether their absence is a decision or a gap.

### The real problem: no sense of readiness

Getting a working document agent takes roughly seven stops across three panes: create it, find
it, add a source, set a schedule, sync, check documents, enable it, then grant a role access.
Nothing told you where you were in that sequence, and a half-built agent looked identical to a
working one apart from a toggle.

Each agent now carries a **derived readiness state**, computed from its actual configuration
rather than stored:

| State | Condition | Level |
|---|---|---|
| Needs a source | type uses knowledge, zero sources | warning |
| Sync failed | any source in error | danger |
| Off | configured but not enabled | info |
| Live | enabled and healthy | success |

It shows as a badge on the grid card and as a callout at the top of the detail with a button
that jumps to the tab that fixes it. That is the single change that most makes this area
navigable: the settings stop being a flat pile and become a sequence with a visible finish line.

### Knowledge and Documents are one subject at two zoom levels

Sources are what is connected; documents are what came in. As sibling tabs, answering "did my
sync work and what did it bring?" meant bouncing between them. The source's document count is
now a link that opens Documents with that source's filter already applied.

### Smaller fixes in the knowledge and documents screens

- **"Failed" was body text**, the same weight as "Last synced" and the doc count, despite
  meaning the agent is answering from stale or missing data. It is a `.badge` now, with a
  `.callout.is-danger` carrying the actual reason. The old screen said "Failed" and nothing else,
  which is not actionable.
- **"Set Schedule" was a solid amber CTA inside a card**, competing with the page's real primary
  action. Source actions are now uniform secondary buttons.
- **Removing a source was a bare trash icon.** It confirms, and states how many documents stop
  being used.
- **Search needed a separate Search button, and "Filters" was an unlabelled mystery button.**
  Search is live, and source and status filters are visible selects.
- **"Showing 5 of 5" with Previous/Next** gave no page position. It uses the same pagination as
  every other table here: range, total, and page N of M.
- **A source with no schedule said "Schedule not set"** without saying what that implies. It now
  reads "No schedule", and the schedule dialog explains that manual sync is the only update path.

---

# Connections

## The insight that shapes this screen

A connection is **shared infrastructure**. Agent knowledge sources read through it. That
relationship was invisible in the old design and it is the reason the area felt disconnected:
the agent screens showed a source failing with "The access token expired", but the token
belongs to a *connection*, and the Connections list said nothing at all. You could only
discover a broken connection by opening an agent that depended on it.

The dependency is now modelled (`source.connId`) and surfaced in both directions: a connection
row counts the agent sources reading through it, and its detail lists them with a link to open
the agent.

## Problem 1: no health anywhere

The list showed a name, a duplicate description, and two buttons. Nothing about whether the
credentials still work, which is the only thing that actually goes wrong with a connection.

Each connection now carries **Connected / Not working / Not tested**, shown as a badge in the
list and the detail header. A failed connection explains itself in a callout with the reason
and how many agent sources are affected. Testing updates the state and clears the callout.

## Problem 2: description duplicated the name

Both rows read "Sharepoint Dev / Sharepoint Dev". The old UI rendered a description field that
in practice repeated the title, so the row carried no information beyond the name.

The row now shows what actually distinguishes one connection from another: **type, target
(site URL or impersonated account), and usage count**. Description is optional, and the hint
says to describe what lives there rather than restating the name. Two connections of the same
type to different sites are now told apart at a glance.

## Problem 3: the secret field lied about its state

Configuration showed "Azure Client Secret *" as an empty required field on a connection that
was already working. That reads as "not set", and saving the form would plausibly blank a
working credential.

A stored secret now renders as **"Stored. It is never shown again."** with a Replace button
that swaps in an empty field on demand. You can see it is set, you cannot read it back, and
you cannot clear it by accident.

## Problem 4: three steps for two decisions

Step 1 picked between two options. Step 2 was two text fields. Step 3 was the credentials.
Step 2 did not earn a screen, and its Description was marked required while the same field was
optional when editing the same record later.

It is **two steps**: what you are connecting (type plus name plus optional description), then
the credentials. Same pattern as agent creation, where the type choice and what it prefills sit
together. The step indicator is two segments rather than a "Step 2 of 3" label plus a bar doing
the same job twice.

## Problem 5: Test Connection had no relationship to anything

It sat above Save with no stated connection between them, and its result was not recorded. You
could test, fail, and save anyway, with nothing anywhere remembering that.

Testing now **writes the connection's status and last-tested time**, so the result is durable
and visible in the list. The create wizard's action bar says why to test before saving: you find
the problem here rather than inside an agent later.

## Problem 6: deleting shared infrastructure was a bare trash icon

No confirmation, and no indication that other things depended on it. Deleting the Lighthouse
connection would have silently broken the Senior Living Policies agent.

Delete now confirms, **names the dependent agents**, and states the consequence: they stop
syncing until pointed at another connection. When nothing depends on it, it says that too, so
the safe case is equally clear.

## Smaller fixes

- **Every connection used the same database icon**, even though the Add flow already drew
  SharePoint and Google Drive differently. Type icons are consistent everywhere now.
- **Credential forms are generated from a per-type definition** (`CONN_TYPES`), so adding a
  connector is a data change, not a new hand-built form that can drift from the others.
- **Save follows the same sticky-bar pattern** as agents: one save, appearing only when dirty,
  with Discard beside it.

---

# Analytics

## The correctness bug first

The old Overview showed **Avg Response Time 6.3s, up 48.7%, coloured green with an up
arrow**. Response time rising is bad. The design bound delta colour to *direction* rather
than to *meaning*, so every metric where lower is better read inverted. An admin scanning
that row would conclude latency was improving while it was degrading by half.

The design system has the same assumption baked in: `.sc-delta.is-up` is green,
`.is-down` is red. So the fix could not just be applied at the call site. Colour is now bound
to meaning (`.is-good` / `.is-bad` / `.is-flat`), each metric declares whether higher is
better, and the arrow carries direction independently.

## Percentages on tiny numbers are noise dressed as signal

"Total Messages 7, +250.0%" means it went from 2 to 7. At that volume a percentage is
meaningless precision, and one extra conversation swings it by triple digits.

Below a sample-size floor the comparison is stated in absolute terms instead ("+5 vs
previous"), and a callout says why percentages are absent. The floor is on **sample size, not
on the metric's own magnitude**: an average response time of 3.5s is a small number but may sit
on thousands of observations.

## Pie charts were the wrong tool three times over

- **Messages by Agent Type was a pie with one slice at 100%.** A whole card to say "everything
  came from the only agent".
- **Topic Distribution had two slices at 14% each.** Pies are poor at comparing similar
  magnitudes, which is exactly what that chart was being asked to do.
- Each pie sat beside a **Breakdown list repeating the same numbers**, so the data was encoded
  twice and neither encoding was sufficient alone.

All three are now sorted horizontal bars carrying their own label and value. Bars compare
near-equal values accurately, degrade to a single row without looking broken, and fold the
legend back into the chart.

## The line chart invented data

Messages Over Time drew a smoothed spline through daily integer counts. Smoothing interpolates
values between points that never existed, and with counts of 1 and 2 the curve bulged above and
below every real observation. The x-axis also spaced irregular dates evenly (7/17, 7/26, 7/28,
8/10, 8/11), which distorts time itself.

It is a **column per day** now, with every day in the range present including zeros, so quiet
periods are visible rather than collapsed away.

## Brand amber was used as a data colour

The line and bars were `--accent-9`. The design system reserves amber for identity and CTAs
precisely so it can mean "this one, selected" in a chart. Series now use `--chart-1..8`.

## Three tabs became one page

Overview held three KPIs and two charts, Agents held a single chart, Prompts and Topics held a
chart and a table. The Agents tab did not earn a tab. More importantly, comparing "which agent"
against "which topic" meant switching tabs and holding the first set of numbers in your head.
One scrolling page: headline numbers, activity, breakdowns, then the question list.

## What was added, and why

The old screens measured **volume** thoroughly and **quality** not at all, even though the chat
already collects thumbs up and down on every answer.

- **Answers rated good** turns that existing signal into the one number that says whether this
  thing is working, with the rated-sample size beside it so the percentage can be judged.
- **Active people is now stated against the member count** ("17, 68% of 25 members"). Three
  unique users means nothing without the denominator; adoption does.
- **The questions table gained a rating filter.** "Rated poor" is the actionable list: these are
  the questions where the answer disappointed someone, and each is a candidate for better
  instructions or a missing knowledge source. Sorting questions by count alone tells you what is
  popular, not what is broken.

## What was removed

- Both pie charts and their duplicate legend lists.
- The Agents and Prompts tabs as separate destinations.
- Percentage deltas when the sample cannot support them.

## Verification note

The low-volume callout fires below 20 messages in a range. The demo dataset carries 58 messages
in its smallest window, so that state does not appear in the current screens, though it is the
state the original screenshots were actually in.

---

# Help and support

## The pane was named for a job it did not do

"Help and Support" contained a ticket queue and nothing else. Someone opening it because they
are stuck gets a table of past requests, not an answer. The four things people actually arrive
with are: *how do I do this*, *is it broken for everyone*, *I need a human*, and *what happened
to my ticket*. Only the last two were served.

Self-serve now comes first: four documentation entry points, and a system status line. Raising
a request is below that, and the copy says plainly that it is the slower path. Deflect before
escalate is not just cheaper for support, it is faster for the person asking.

## Status was unreadable, which broke the one column people scan

Every status rendered as the **same amber badge with a warning icon**, so "Done" and "To Do"
were visually identical, and a completed ticket carried an alert glyph. Amber is also reserved
for brand in this system, so every row looked like it needed attention.

Each state now has its own meaning: To do neutral, In progress blue, Done green, Blocked red.

## Nine columns squeezed the only one that mattered

Ticket, App, Subject, Reporter, Assignee, Status, Priority, Created, Updated. In a modal-width
table that is why the subject truncated to "skyAdvisor demo is empty, no..." while Reporter got
a full column on a list of *your own* requests.

Four columns now: Request (subject, with ticket ID and app beneath), Status, Priority, Last
activity. Reporter, assignee and created moved into the detail, where they are read once rather
than scanned. **Created and Updated were both relative dates that mostly agreed**; only last
activity earns list space.

## Priority was plain text with no rank

"Medium", "Low" in body text gave an ordinal value no visual order. It is carried by weight and
colour on the word itself rather than a badge, so Urgent reads hot without giving Low the same
presence a badge would.

## Filters were missing the question people actually ask

Only free-text search existed, so "what is still open on my plate" meant reading every row. The
list now defaults to **open requests raised by me**, with both filters adjustable. A default
that answers the common question beats a neutral default that answers none.

## The create flow was two dialogs for four options

Step one offered four choices under two group headings, one of which covered a single item.
Step two was a title and description. The escape hatch was a full-width button reading
"skip - General request", which competed with the type cards and was written in three registers
at once.

One dialog now: four type cards, title, description. Choosing a type states the priority it
starts at, so the consequence of the choice is visible at the moment of choosing rather than
discovered later in the queue.

## Smaller fixes

- **The subtitle read "Manage your preferences and settings"**, which was on every pane in the
  original and described none of them.
- **The detail was a drawer sliding over the settings modal**, a modal over a modal. It is a
  drill-down with a back link, matching agents and connections.
- **Timestamps were relative only.** "3 months ago" is useless for referencing a ticket, so
  relative times now carry the absolute date, and the detail states it outright.
- **The reply box had a permanent dropzone larger than the reply field.** Attachments collapsed
  to a button; the reply is the primary act.
- **Status and priority in the detail header sit with the identity**, not beside the actions,
  per the affordance rule established for connections.

---

# The save model

Two questions kept coming up on every editable screen: *how do I do this*, and *is it saved*.
The second one had no answer at all on two panes, so it is settled here for the whole app.

## Two models, and the rule for choosing

**Immediate.** A single atomic control whose effect is instantly visible and reversible: my
theme, my language, the tenant I am working in, an agent's enable switch, assigning a role.
Applied on change and confirmed by a toast, because an instant save with no feedback is
indistinguishable from nothing happening.

**Staged.** A form. Edits are held against a snapshot and committed by one save bar that
appears only when something actually differs, with Discard beside it. A half-typed grounding
rule must not be live for everyone while you are still typing it.

The dividing line is whether the change stands alone. **An object's lifecycle state sits in
the header and is immediate; its settings sit in the body and are staged.** That is why an
agent's enable switch applies at once while its name and instructions wait for Save.

## What was broken

Branding had four editable controls and Voice had three, and **neither pane had any save
affordance whatsoever**. You could set an accent colour, write a meta description, or define
the voice persona, and nothing would happen, with no indication that nothing had happened.
Agents and Connections already had save bars, so the app was silently inconsistent about the
single most important promise a settings screen makes.

Both panes now use the same `stagedForm()` helper as everything else, so the behaviour is
identical rather than merely similar: same bar, same wording, same Discard, same dirty check.

## The upload control

The old control was two unlabelled buttons reading **Light** and **Dark**. Problems, in order
of severity:

- **Nothing said it uploaded anything.** No icon, no verb, no affordance.
- **"Light" and "Dark" already mean theme modes in this app**, on the Account pane. The same
  two words meant two unrelated things on adjacent screens.
- **No preview and no set/unset state.** There was no way to tell whether a logo was already
  configured, so the only safe action was to re-upload and hope.
- **Favicon used a third pattern** ("Upload" with an icon) for the same job.

Each variant is now its own labelled drop target that shows what is in it: an empty tile reads
"Add", a filled one shows the actual image with the filename on hover and a remove control. The
caption below states the variant plainly ("Light mode", "Dark mode", "All themes"). Uploads are
real, using FileReader, so the preview is the file you picked and the size limit is enforced at
selection rather than on submit.

Because uploads are staged like every other field on the pane, discarding removes an image you
added but had not saved.
