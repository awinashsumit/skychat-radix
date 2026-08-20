# SkyChat Redesign: UI Checklist (Radix flavor)

The verification contract for the SkyChat redesign. Every item is checked against
`index.html` + `skychat.css` before the screen is called done. Values bind to
`tokens.css`; no literals except the documented ones.

---

## 1. Grid & layout

- [x] App shell: 2 columns. Sidebar `288px` fixed, content `1fr`. Sidebar collapses to `0`
      (animated) below 1024px or on toggle.
- [x] Top bar: `64px` tall, hairline bottom border (`--border-subtle`), white surface.
- [x] Reading column: messages and composer share ONE max-width, `768px`, centered as a
      column; text inside stays left-aligned.
- [x] Hero (empty state) is the only centered block, per the empty-state exception.
- [x] All gutters and paddings on the Radix space scale (`--space-1`..`--space-9`), 4/8px
      rhythm. No off-scale px.
- [x] Sidebar canvas `--gray-2`, chat canvas `--color-panel-solid` (white), separated by a
      1px `--border-subtle` line, matching the skyAgent rail-vs-canvas split.

## 2. Type ramp (Inter, Radix sizes)

- [x] Inter loaded via Google Fonts; weights 400 / 500 / 700 only. The one exception is the
      logo wordmark, which is set in the brand serif via `--font-brand` and scoped to
      `.sc-brand-name`, so no UI text can inherit it.
- [x] One H1 per view: greeting `t-8` Bold (35/40) on Home; conversation title `t-3` Medium
      in the top bar on Chat (the H1 of that view).
- [x] Message body `t-3` (16/24) - long-form reading size.
- [x] UI labels and buttons `t-2` Medium (14/20). Section labels `t-1` Medium uppercase.
- [x] Meta rows, timestamps, hints `t-1` (12/16). Nothing below 12px.
- [x] Hierarchy carried by weight + the `--fg-high` / `--fg-low` two-step split, not by
      inventing sizes. No size off the `t-1`..`t-9` ramp.

## 3. Spacing & density

Density target: a working chat app, not a marketing page. Rows and blocks stay tight enough
that a full conversation list reads at a glance.

- [x] Composer internal padding `--space-3`/`--space-4`; gap between composer and message
      list `--space-5`.
- [x] Message blocks separated by `--space-5` (24px); elements inside a block by
      `--space-2`/`--space-3` (internal <= external).
- [x] Sidebar: CTA / search / groups separated by `--space-3`; conversation rows sit flush
      (no gap), so the group label is the only vertical break.
- [x] Conversation row: 32px tall, 32px pitch. This is the density benchmark, one row per
      32px with no gap; anything looser makes the history list feel padded.
- [x] Chip rows wrap with `--space-2` gaps; message action buttons `--space-1`.

## 4. Color & theming

- [x] Every color is a `var(--...)` token; zero raw hex outside inline SVG art.
- [x] Amber is brand only: New Chat CTA, active sidebar pill, send button, knowledge chip,
      assistant spark tile, focus rings. Status uses red / green / orange / blue.
- [x] Text and icons on solid amber are `--accent-contrast` (dark), never white.
- [x] Avatars are never amber: user "SA" uses a deterministic chart hue (`.c6`).
- [x] Logo mark is inline SVG whose fills are accent tokens (`--accent-3` bubble, `--accent-9`
      dots), so it re-tints per theme instead of shipping two raster files. Its geometry is
      artwork and therefore exempt from the radius scale.
- [x] Dark theme works by flipping `data-theme`; both themes read from the same step roles.

## 5. Elevation (one strategy per plane)

- [x] In-flow surfaces (composer, inputs, chips, toolbar buttons) separate with **inset 1px
      hairline rings** (`--border-ui` / `--border-subtle`), not shadows, not CSS borders on
      inputs.
- [x] Floating surfaces only get shadows: menus/popovers `--shadow-4`, dialogs `--shadow-5`,
      toasts `--shadow-4`. Every shadow keeps its crisp 1px ring layer.
- [x] **One z-index scale, no literals.** Ordered by what can be summoned from what:
      drawer 100 < overlay 1000 < nested dialog 1100 < menu 1200 < tooltip 1300 < toast 1400.
      A menu opens from inside a dialog and a toast confirms an action taken anywhere, so
      both must outrank the overlay. Tokens live in one block in `skychat.css`; never
      hardcode a z-index elsewhere.
- [x] The composer floats over scrolling content via a **gradient scroll fade**, not a shadow,
      so the border strategy stays pure.
- [x] Focus swaps the inset ring to `--accent-8` with zero layout shift.
- [x] Radii on the Radix scale: composer `--radius-5`, menus `--radius-4`, buttons/chips/
      toggles `--radius-3`, small icon actions `--radius-2`. No pill-shaped (`--radius-full`)
      controls; only avatars are circular.

## 6. Component states (micro-interaction inventory)

Every interactive element defines: rest / hover / active / focus-visible / disabled.

- [x] **Buttons** (solid, soft, surface, ghost, icon): hover fill step +1, pressed scale
      `0.98`, focus ring `--focus-ring` 2px offset, disabled `--gray-3` + `--fg-disabled`.
- [x] **Send button**: disabled until input has text; enabling animates fill from gray to
      amber (150ms); hover `--accent-10`.
- [x] **Sidebar history rows**: hover `--gray-3`; ellipsis action appears on hover/focus;
      selected row = soft `--accent-3` tint with `--fg-high` text (only one). Deliberate
      deviation from the DS "active nav = solid amber pill" rule, see the note in §9.
- [x] **Composer**: focus-within ring swap to `--accent-8`; textarea autogrows (max 5 lines);
      Enter sends, Shift+Enter breaks line.
- [x] **Toggles** (Search / Think): pressed = `--accent-3` fill + `--accent-11` text + inset
      `--accent-7` ring, `aria-pressed` synced.
- [x] **Suggestion / follow-up chips**: hover raises border to `--border-strong` + bg
      `--gray-2`; click fills or sends.
- [x] **Menus** (model, knowledge, history context): highlighted row solid amber + dark text;
      selected row shows leading check; danger row (Delete) hovers red with white text.
- [x] **Copy / feedback actions**: tooltip on hover (300ms delay); copy shows a toast;
      thumbs latch on (soft tint) when selected.
- [x] Keyboard: Esc closes any open overlay; outside click closes; focus visible on
      every control.
- [x] **Share dialog**: `.overlay` + `.dialog`, left-aligned title with a close icon-btn,
      body in `--fg-low`, a read-only `.sc-share-item` summary, right-aligned footer with
      soft Cancel + one solid amber CTA carrying dark text. Opens focused on the CTA, traps
      Tab, closes on Esc / scrim click / Cancel, and restores focus to the trigger.
- [x] **Memory**: clearing memory confirms with a toast, not a silent state change.
- [x] **Settings modal**: fixed rail + scrolling pane, rail item selected with the soft
      `--accent-3` tint (secondary list, same rule as the conversation rows). Rows are
      hairline-separated rather than boxed, so one floating surface carries one elevation.
      Theme mode is driven by a single `setTheme()` so the cards and the top-bar toggle
      cannot disagree. Closes on Esc / scrim / X and restores focus to the trigger.

## 7. Motion & animation

- [x] Micro-interactions 120-160ms; standard state changes 200ms; overlays 150ms in /
      120ms out; view switches 250ms.
- [x] Entering = ease-out, exiting = ease-in, same-element = ease-in-out.
- [x] Menus/popovers scale from `0.96` + fade, transform-origin at the anchor edge.
- [x] New messages enter with 4px rise + fade (200ms ease-out).
- [x] Loading indicator: the assistant sparkle mark itself. Star stays steady and legible
      while the plus and dot twinkle in and out (1.4s, overshoot to 1.3 then settle), dot
      staggered 280ms behind the plus. Replaces the three-dot bounce so a given state has
      exactly one animation. SVG accents need `transform-box: fill-box` to scale about their
      own centre rather than the user-space origin.
- [x] Sidebar collapse animates width 200ms ease-in-out; labels fade first.
- [x] Toasts slide up + fade, auto-dismiss 2.4s.
- [x] `prefers-reduced-motion`: all transforms/animations neutralized (opacity-only or none).

## 8. Content & accessibility

- [x] Status/state never by color alone (toggle state has pressed styling + aria;
      memory event has icon + label).
- [x] **Appearance matches affordance.** Read-only state uses `.sc-status` (dot + label) and
      sits in the identity block. A filled `.badge` is never placed in an actions area beside
      a button: matching size, shape, and soft tint make the two read as a button pair, and a
      status that looks clickable invites a click that does nothing. A header's actions area
      holds actions only.
- [x] Icons: Lucide only, stroke 1.75; 18px nav, 16px buttons; `currentColor`. The one
      filled glyph is the assistant sparkle (brand mark, not UI chrome): star and dot take
      a fill, the plus stays stroked since a cross reads as line work.
- [x] No emojis, no em-dashes in UI copy.
- [x] Contrast: text >= 4.5:1, UI glyphs >= 3:1 (step-11 on step 1-3 backgrounds,
      `--accent-contrast` on amber-9).
- [x] Buttons carry `aria-label` when icon-only; menus use `aria-expanded` +
      `role="menu"`; composer textarea labelled.

- [x] **Every editable surface declares its save model, and there are only two.**
      *Immediate* for a single atomic, instantly-visible, reversible control (my theme, an
      agent's enable switch), always confirmed by a toast, because a silent instant save is
      indistinguishable from nothing happening. *Staged* for forms, via the shared
      `stagedForm()` helper: one save bar, shown only when something actually differs, with
      Discard. Lifecycle state lives in the header and is immediate; settings live in the
      body and are staged. No pane may have editable fields and no save affordance.
- [x] **An upload says it uploads, and shows what it holds.** Each asset variant is its own
      labelled drop target: "Add" when empty, the real image preview when set, filename on
      hover, remove control. Variant captions never reuse words that mean something else
      elsewhere in the app.
- [x] **Accent secondary is for accent-flavoured actions, not for negations.** Cancel,
      Discard, and Back are dismissals and use the neutral `.btn-surface`. Spending brand
      colour on the least important action in a dialog both dilutes the accent and puts two
      amber buttons side by side, which is the competition the one-solid-CTA rule exists to
      prevent. `.btn-soft` is now used only in its `.is-danger` form.

- [x] **Accent icons use `--accent-9`; accent text uses `--accent-11`.** Step 11 is the dark
      text step and stays dark wherever it colours words (kb chip, links, badges, the "Add"
      label). Icons take the brand amber: the assistant sparkle is a brand mark, and brand
      marks are exempt from contrast rules; the tile icons and active nav glyph always sit
      beside a label that carries the meaning. An icon that IS the only signal (the menu
      selection check) stays on step 11.

> **Resolved:** light-mode `--accent-11` had been set to the brand amber `#FFB31C`, identical
> to step 9. Step 11 is the low-contrast *text* step, so for a warm hue it must be dark. Every
> use of it as text or an icon measured 1.59:1 on `--accent-3` and 1.79:1 on white. Fixed at
> source in `tokens.css` to `#a05a00`, which measures 4.71:1 and 5.31:1. Brand amber is
> untouched at step 9, so solid CTAs, the active nav pill, and the logo are unchanged.

## 9. Parity with skyAgent (similar, not a clone)

- [x] Adopted: New Chat as the sidebar solid CTA; grouped history (Pinned / Today /
      Yesterday); greeting hero with composer directly beneath; suggestion chips; hint line
      under composer; off-white rail on white canvas.
- [x] Kept SkyChat's own: model selector in the top bar; conversation title + timestamp
      centered in the top bar; voice / memory / share actions; knowledge-base selector in
      the composer; follow-up question chips; response meta row (kb, model, latency);
      memory-updated divider.
- [x] Dropped from old SkyChat: amber user avatar (brand-only rule), double "Conversation
      History" heading, orphan single-item "Chats" accordion.
- [x] **Adopted from Claude's app shell** (client feedback, 2026-08-11, extended 2026-08-12
      after the first pass read too sparse against the reference):
      - A persistent nav-shortcut row above search (`.sc-nav-item`, "Agents"), styled at the
        same row height as `.sc-chat-item` so it reads as one list rather than the app-shell
        `.nav-item`, which goes solid amber active and would fight the soft tint the history
        list already uses.
      - An outer "Recents" eyebrow above Today/Yesterday, matching Claude's terminology.
        Kept the Today/Yesterday/Earlier sub-grouping rather than flattening to it, since
        temporal orientation is more useful here than Claude's own flat list, not less.
      - A real "View all" toggle: past 6 non-pinned conversations, older rows collapse and
        the button expands/re-collapses them. Pinned items are exempt (pinning is a
        deliberate choice, never buried), and a freshly sent message is always item 0 of
        Today, i.e. always inside the cap, so sending never hides the conversation you are
        looking at. A search query overrides the cap outright rather than hiding an older
        match.
      - A clickable account row in the footer opening straight to Settings > Account, now
        with a chevron — honest to add only once the row actually does something on click.

- [ ] ~~**Chat / Cowork / Code tab bar**~~ — **removed 2026-08-20 at client request.** It
      shipped as a sidebar segmented control (below), became a two-item Chat / Work switch in
      the top bar during the ChatGPT-shell pass, and is now gone entirely along with everything
      it gated: the approval chip, the project context strip under the composer, the Work task
      list, and the alternate greeting and placeholder. `currentMode` and `setMode()` no longer
      exist — there is one mode, so nothing needs to branch on it. Kept below as the record of
      what was built and why, in case the mode ever returns.

      Removing it exposed a latent bug worth keeping in mind: `syncComposerShape()` treated
      `scrollHeight > 30` as "multiline", but an empty textarea measures 40px, so the test was
      always true and the composer never returned to its pill once you typed. Work mode had
      been forcing the expanded state anyway, which hid it.

      That whole mechanism is now moot — see the composer entry below.

- [x] **Composer is one shape, always** (client reference, 2026-08-20). It was a pill that
      swapped to a box on typing; it is now permanently the box, so nothing reflows under the
      cursor as you type. `syncComposerShape()`, the `.is-expanded` class, and the pill rules
      are all deleted — with a single shape there is no state to track.
      - Grid is fixed at `"input input" / "plus tools"`, `--radius-6` (16px, the closest
        on-scale value to the reference's corners), `--space-3` padding, `min-height: 132px`.
      - Measured against the reference: height/width **0.217** vs the reference's **0.220**;
        text inset 20px from the box edge in both.
      - `min-height` rather than a fixed height, so short input sits in a stable box (two
        lines still measure 132px) and long input grows to the 200px textarea cap.
      - The **Chat / Cowork toggle** was held back on the first pass and added on the next
        instruction — see below.

- [x] **Chat / Cowork, in the composer** (client reference, 2026-08-20). The mode pair sits in
      the composer's control row beside `+`, not in the top bar. It changes what that control
      does, so it belongs with it, and the earlier top-bar placement left the switch far from
      the thing it switched.
      - Reuses the DS track+pill idiom (`.sc-cmode`), sized to the composer's 26px control row
        rather than the 28px top-bar row.
      - **Cowork adds a context strip** attached under the composer. The composer squares off
        its bottom corners (`.has-ctx`) so the two read as one control, not a panel with
        something stuck beneath it.
      - The strip carries the two decisions a multi-step run needs up front: **which project**
        it works in, and **how much it may do unattended** (Manually approve / Automatically
        approve / Skip all approvals). Both are per-run, which is why they are here and not in
        a settings pane.
      - **Skip all approvals is the only one that confirms back.** It is the single choice with
        a blast radius, so it gets a toast; the other two are silent, per the immediate-save
        rule. Consistent with the analytics colour rule — weight follows consequence.
      - Cowork swaps the four suggestion chips for **Ideas for you**, three named jobs as quiet
        rows, and drops the greeting's second line, since the composer placeholder already asks
        the question. Chat keeps chips, subtitle, and "Message skyChat".
      - Mode, project, and approval all survive the move into a conversation — the composer is
        one instance relocated between slots, so there is no second copy to keep in sync.

      Original entry (client feedback, confirmed explicitly 2026-08-12 after the first pass
      held it back — see above). Reused the DS `.segmented` track+pill verbatim (same component
      as Analytics' date range and the Agents status filter), stretched to the sidebar's full
      width, rather than a bespoke tab component.
      - **Chat** is the whole real app: unchanged.
      - **Cowork** and **Code** are real destinations, not decoration. Each swaps the
        Chat-only sidebar content (nav shortcut, search, recents) for one honest line
        ("Cowork is not part of skyChat yet.") and swaps the main pane for the same
        `.empty-state` pattern already used for Settings panes awaiting their design. The
        model picker and the voice / clear-memory top-bar actions hide too, since they are
        Chat-specific controls with nothing to act on. The theme toggle and rail-collapse
        stay, since those are shell-wide, not Chat-specific.
      - Returning to **Chat** delegates to the existing `goHome()` / `goChat(activeChat)`
        rather than re-deriving their hidden-state logic, so the exact conversation (title,
        thread scroll position, active sidebar row, Share button) is restored byte-for-byte,
        not just "some chat view." Verified: open a conversation, switch to Cowork, switch
        back — same conversation, not Home.
      - This is the second time an inert-looking control was almost shipped in this app
        (after the dead composer "Agents" toggle, §10): a tab that looked clickable and did
        nothing would have been the same mistake at a much more visible spot.

> **Documented deviation: the selected conversation row.** The DS hard rule says an active
> sidebar item is a solid `--accent-9` pill. That rule is written for *primary navigation*,
> where one loud marker orients you across a handful of destinations. This sidebar is
> conversation history: a long, growing, homogeneous list where a saturated amber bar reads
> as an alert rather than a cursor, and fights the message content for attention. The DS
> anticipates this and allows secondary lists (`.tree`, `.pane-folder` in the three-pane
> archetype, which is the mail/chat archetype this screen belongs to) to use the soft
> `--accent-3` selected tint instead. We take that path, and pair the tint with `--fg-high`
> text rather than `--accent-11`, which also sidesteps the amber-on-cream contrast caveat
> noted in §8. Selection is therefore carried by two cues, fill plus text contrast, exactly
> the model Claude's own sidebar uses.

## 10. Deferred, by design

Not gaps found during a pass — features scoped out on purpose, so a future contributor does not
"fix" them into existence without the context.

- **Automatic agent routing.** Client feedback (2026-08-11) was to eventually have skyChat pick
  the right agent for a message itself, using the composer's agent chip only as a fallback or
  override rather than the primary mechanism. Manual selection (the `#kbBtn` chip) is the whole
  mechanism today. Auto-routing needs real classification behaviour to demo honestly, which is
  out of reach for a static prototype, so it is documented here rather than faked with a toggle
  that does nothing. When it is built, the chip's role changes from *the* selector to an
  *override*, which likely means restating its default label (e.g. "Auto" versus a pinned
  agent name) rather than just adding a setting.
- **Removed rather than deferred:** a second, inert "Agents" toggle used to sit beside the
  working agent chip in the composer (`aria-haspopup="menu"` with no menu ever wired to it).
  Two adjacent controls that both look like agent selection, only one of which worked, was worse
  than one. It is gone; the sidebar's "Agents" shortcut covers the "browse agents" need instead.

## 11. Navigation: where a surface is allowed to live

Settled 2026-08-20 after Agents and Skills were found existing both as a full-screen page and as
settings panes. The rule that resolves it:

> Anything you **configure** lives in Settings. The sidebar is for places you **work**.

- [x] Sidebar destinations are Chat, Projects, Scheduled — surfaces you inhabit and return to.
- [x] Agents, Skills, and Connections are settings panes. Opening one keeps the chat mounted
      behind the modal, so closing it returns you to your place with no state to restore.
- [x] A sidebar row may be a **shortcut into settings** (`data-setpane`) rather than a page.
      Such a row never takes the active nav state — you have not gone anywhere.
- [x] All routes to a surface resolve identically. Every composer `+` menu "manage" action and
      the sidebar shortcut all call `showPane(x); openSettings();`. Previously **Manage
      connectors** opened the modal while **Manage agents** opened a page — three sibling menu
      items, two kinds of destination.
- [x] Agents keeps **Your agents** / **Browse** as tabs in one pane, because configuring and
      installing are two jobs on the same objects. Splitting them into two rail entries would
      re-create the duplication this rule removes. Skills has only the browse job, so no tabs.

Fixed in the same pass: `IC.chart` and `IC.users` were referenced by `INSTALLED_ICONS` but never
defined, so `svg()` interpolated the string `"undefined"` and two tiles in the installed strip
rendered empty. The page-only context had hidden it.
