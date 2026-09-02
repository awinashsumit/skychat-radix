# Employee service portal, Home

The record for `index.html`. The shape of this screen is a client decision; read this before
changing it.

---

## 1. Where the design came from

The client designed this screen and shared it on 2026-08-25. It is built here as designed:

- **Greeting row** across the top: brand mark, "Good morning, Anita" with the org and date
  beneath, and the search field on the right. No hero band, no separate top bar.
- **Left column**, the work: **Needs your attention**, then **With someone else**.
- **Right column**, the context: **Development** (onboarding progress plus mandatory courses),
  **My onboarding**, **My courses**, **Next shifts**, and **Raise a request**.
- **Full width**, under both columns: **My requests**.

Styling is the shared Radix-Design System. The reference's teal maps onto the Skypoint amber
accent and its navy card onto the system's inverted surface, so the screen themes correctly
instead of being pinned to one palette.

Two earlier passes are superseded and should not be reinstated: a full archetype-driven redesign
(reverted at the client's request), and the client's original hero-band layout.

## 2. The badge problem, and how this design solves it

Status pills used to sit in the trailing actions area next to the row's button. They matched it
in height, radius and soft tint, so the two read as a button pair, and a status that looks
clickable invites a click that does nothing. `UI-CHECKLIST.md` 8 already forbade this.

The client's design fixes it with **two changes working together**:

1. **Position.** The pill moves into the row's meta line, beside the ticket id. It is no longer
   in the actions area at all.
2. **Type.** UPPERCASE micro-caps at 12px with letter-spacing (`.badge.is-caps`). Every button on
   the page is 14px sentence case, so the two cannot be confused at a glance.

Either change alone helps; together they close it. The uppercase idiom is not new to the system,
`.list-item.is-header` already uses it.

**One colour on the page, and it marks the one overdue thing.** `OVERDUE` is `.is-danger`;
every other status is `.badge.is-outline`, a white pill with a hairline ring. Ranking is carried
by which badge is coloured and which row holds the single `.btn-solid`, not by giving five
statuses five hues.

Amber never carries a status. Where the reference tints "Willow" and "Open" with its accent, this
build separates them by weight and contrast instead, because amber is brand identity in this
system.

## 2a. My requests, and the split rail cards

The client's design folded it into the foot of the Raise a request card as a single 14px line,
"My requests / 4 open of 14", above the two recent rows. At that size, inside another card's
footer, it read as a footnote rather than a section, and the client reported it as missing
(2026-08-25). It is now a card of its own, last in the right column.

The three counts from the original screen (14 total, 4 open, 10 closed) are back, carried by the
system's `.summary-strip` rather than three separate stat cards. Same numbers, one component, and
it fits the rail width.

**Full width** (2026-08-25). Moved out of the rail entirely, below both columns, matching the
client's original screen: three counts (14 / 4 / 10) beside the two recent requests.

**One card, title inside** (2026-08-25, second pass). The first attempt built it the way the
reference draws it, as a bare section heading above four free-standing cards. That made it the
only block on the page not shaped like the others: every other section is one card carrying its
own title. It is now a single `.card` with a `.card-title` inside, and the four boxes are inset
`--gray-2` blocks within it, the same idiom `.na-row` uses inside "Needs your attention". Same
content and the same four-box arrangement, one consistent container.

The count numbers are `--fs-6` (24px), not the reference's ~36px: they are secondary counts at the
foot of the page and should not out-size the H1. The three count blocks are the one place on the
page where content is centred rather than left-aligned.

**My onboarding and My courses are separate cards** (2026-08-25), not one "Development" card.
Splitting them also let the onboarding note ("Three left. One is yours, two are with IT and
Facilities.") and each course's due date come back, both of which the merged card had squeezed out.

Column heights at 1440 are now 771px left and 873px right, close enough that neither column looks
stranded.

## 2b. Column symmetry and the inverted-card link

**Both columns run to the same height** (2026-08-25). The grid items stretch and the cards inside
each column carry `flex-grow`, so whichever column is shorter absorbs the surplus. It is
self-balancing rather than a hard-coded height, so it survives content changes in either column.

The surplus lands in the **rows** (`.na-row`, `.wse-row` also grow), not as a dead band under the
last one, so a stretched card reads as a relaxed list rather than a card with a gap at the bottom.
At 1440 both columns measure 877px.

**skySchedule** joins skyLearn as a cross-app link, on the Next shifts card.

**Next shifts is a plain card** (2026-08-25). It was built on the system's inverted surface,
following the reference's navy card, and the client called it correctly: an inverted card reads as
a highlight, and this section carries no more weight than My courses directly above it. Every card
in both columns now resolves to one background, so the rail is four peers.

Today is still marked, by contrast and weight (`--fg-high` Medium against `--fg-low`), the same way
the page already separates Open from Closed. That was already the mechanism, because amber could
not survive the inverted card, so dropping the inversion cost nothing.

Three earlier contrast fixes existed only to keep text legible on that inverted surface and are now
moot: the `--gray-8` muted text, the `--fg-on-inverted` treatment of today's location, and the
`--accent-3` link colour. The rules were removed with the surface rather than left behind as dead
CSS; the link is back on the standard `.link` colour.

## 2c. Link colour: a recorded exception

All four links (`Open the full queue`, `skyLearn`, `skySchedule`, `Open the full list`) are
`--accent-9`, the brand amber, at the client's instruction (2026-08-25). Logged here as an
exception because it is the one place on this screen that knowingly fails AA.

| Colour | On a white card | AA needs |
|---|---|---|
| `--accent-9` #ffb31c (shipped) | **1.79:1** | 4.5:1 |
| `--accent-11` #a05a00 (previous) | 5.31:1 | 4.5:1 |

There is no brighter amber that passes: the two are the same hue, and step 11 is simply that hue
at the lightness text requires. Anything light enough to read as yellow is too light to read as
text on white. This is the identical finding `tokens.css` records against the accent scale, where
`--accent-11` was changed away from the brand amber for exactly this reason, and which
`UI-CHECKLIST.md` 8 logs as resolved.

Scoped to light only, and to `.link` on this page. Dark is untouched: `--accent-11` is `#ffca16`
there, already reads as yellow, and passes. The global token is untouched, so skyLearn and skyCRM
are unaffected.

To revert, delete the `:root[data-theme="light"] .link` rule.

## 3. Contrast corrections

Measured in both themes rather than eyeballed (`rules.md` 14). Four failures were found and fixed
at source:

| Element | Was | Measured | Now |
|---|---|---|---|
| Portal tile counts | `--fg-subtle` | 3.60 light, 4.15 dark | `--fg-low` |
| "Closed" request state | `--fg-subtle` | 3.79 light, 4.15 dark | `--fg-low` |
| "Solved" badge | `--success-text` on `--success-bg` | 4.21 light | `--green-12`, scoped to light |
| Today's location | `--accent-9` | 1.54 dark | contrast + weight, no hue |

The `--fg-subtle` pair is the exact failure `rules.md` 14 warns about: the tertiary step falls just
under AA at small sizes. The amber one only appeared in dark, on the since-removed inverted card,
and is recorded because it is the reason Today is marked by weight rather than by hue.

> The "Solved" row is a defect in the **shared** token pair, not in this page: green-11 on green-3
> measures 4.21:1 in light (dark is fine at 7.86:1). It is patched locally here because fixing
> `--success-text` at source would change every success badge and callout in skyLearn and skyCRM,
> which is a separate piece of work.

> Tooling note: `getComputedStyle` returned stale backgrounds after a live `data-theme` toggle,
> reporting `.btn-surface` as white-on-white in dark. Measure dark by loading a copy with
> `data-theme="dark"` set in the markup, not by flipping the attribute at runtime. This is the
> same quirk recorded at the end of `UI-CHECKLIST.md` 9.

## 4. Deviations from the reference, and why

| Reference | Here | Why |
|---|---|---|
| Teal accent, navy card | Amber accent, `--color-inverted` card | The system's brand hue, and an inverted surface that flips with the theme rather than a hard-coded dark. |
| Rounded geometric typeface | Inter | The system's type is locked. |
| Two shifts listed | Three | Saturday 24 Aug is real data. The row pattern takes N rows; dropping one loses a shift, which is not a design choice. |
| Em dashes throughout | Commas and periods; en dash for time ranges | House style. |
| No menu or account control | Same | Flagged, not invented. The previous header bar carried a Menu button and the user avatar; this design has neither, so there is currently no way to reach navigation or sign out. |

## 5. Local CSS

The system's app-shell grid assumes a sidebar, which this screen does not have, so the page builds
its own greeting row and two-column body. Everything is token-bound. The only literals are two
component dimensions the reference sets deliberately, the 44px brand mark and the 48px search
field, plus the 1280px content width and two breakpoints.

Cards sit on a tinted canvas, so they are `.is-raised`, and the canvas drops to `--gray-1` in dark
so the `--gray-2` cards still separate from it (one elevation strategy per screen).

## 6. Checks run

- Zero inline styles, zero raw hex, zero em dashes, one H1.
- Every text and badge colour measured against its actual background in both themes. No failures.
- Dark verified from a fresh load, not a runtime toggle.
