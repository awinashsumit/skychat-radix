# skyChat, Radix flavour

A working redesign of skyChat in the Radix visual language, tinted with the Skypoint amber
brand and set in Inter. Static HTML and CSS, no build step and no dependencies beyond two
Google Fonts.

**Open `index.html` in a browser.** That is the whole setup.

To serve it locally instead (needed if your browser blocks local font or file access):

```bash
python3 -m http.server 4173
# then open http://localhost:4173
```

## What is in here

| File | What it holds |
|---|---|
| `index.html` | The entire app: chat shell, message thread, and the eight-pane settings modal |
| `tokens.css` | Design tokens. 12-step colour scales, Inter type ramp, Radix space/radius/shadow |
| `dashboard.css` | The Radix design system: layout shell and component classes |
| `skychat.css` | The skyChat layer: chat shell, composer, settings, analytics, and support UI |
| `UI-CHECKLIST.md` | The visual and interaction contract every screen is checked against |
| `SETTINGS-IA.md` | Why the settings information architecture is shaped the way it is |

`tokens.css` and `dashboard.css` come from the shared Radix design system. `skychat.css` is
app-specific. Changing a token changes the whole app, which is the point.

## What works

The prototype is interactive, not a set of mockups. Real behaviour:

- **Chat.** Send a message, get a canned reply, follow-up chips, copy and rate a response,
  rename, pin and delete conversations, light and dark theme.
- **Settings**, grouped by scope. *You*: account, tenant and instance, personal theme and
  language. *This instance*: people and roles, agents, connections, branding, voice,
  analytics. *Support*: docs entry points and a ticket queue.
- **Agents.** Create from a template, per-type capabilities, model ordering by drag or
  keyboard, knowledge sources with sync state, and an ingested-documents table.
- **Connections.** Two-step create, credential forms generated per connector type, test that
  records its result, and a delete that names what depends on it.
- **Analytics.** Derived from one message log, so every figure on the page agrees.
- **Branding.** Real image uploads with live previews via FileReader.

## Two conventions worth knowing before you edit

**Save model.** Exactly two, and every editable surface uses one. *Immediate* for a single
atomic reversible control, always confirmed by a toast. *Staged* for forms, via the shared
`stagedForm()` helper: one save bar that appears only when something differs, with Discard.
Lifecycle state sits in the header and is immediate; settings sit in the body and are staged.

**Colour.** Amber is brand and identity only. Status uses red, green, orange and blue. Text on
solid amber is `--accent-contrast`, never white. `--accent-11` is the dark text step and stays
dark wherever it colours words; icons that sit beside a label use `--accent-9`.

The reasoning behind both, and behind every design decision that looks like a regression, is in
`UI-CHECKLIST.md` and `SETTINGS-IA.md`. Read those before reverting something that looks wrong.

## Caching note

The CSS import chain is versioned (`@import url("./dashboard.css?v=2")`). If you edit
`tokens.css` or `dashboard.css` and the change does not appear, bump that number.
