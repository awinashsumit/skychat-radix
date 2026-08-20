# skyLearn, sign in: research and the rebuild

The entry point, rebuilt from the supplied screen. The visual contract is in
[`UI-CHECKLIST.md`](UI-CHECKLIST.md).

---

## 1. What the supplied screen said, and why each line had to change

| On the screen | The problem |
|---|---|
| **"Continue wirh Google"**, **"Continue wirh Apple"** | *wirh* for *with*, twice, on the two most prominent buttons |
| "you agree to **Kelaspintar** Terms of Service" | Kelaspintar is a different product. Template copy, never replaced |
| **"Start Creating Today"** / "Set up your account and bring your courses to life" — above a button reading **"Sign In"** | A sign-**up** for course authors with a sign-**in** button. Two screens fused |
| Placeholder **"ex: a personal gmail address"** | All 44 people on the roster are `firstname.lastname@skypoint.ai` |
| **Google and Apple SSO** | Apple ID is a consumer credential |

### The heading was the real defect

The other four are typos and leftovers. The heading is a decision, and it is the wrong one.

*"Start Creating Today — bring your courses to life"* addresses somebody who is about to author a
course. Counted against the roster this product actually serves:

| | |
|---|---|
| People who sign in | **44** |
| Who author courses | **1** (the administrator) |
| Who deliver them | 3 instructors |
| Who only take them | **40** |

**Ninety-one percent of the people reading this screen will never create anything.** A CNA opening
it at the start of a shift is there to find out what she has to do. So the heading is *Sign in* and
the sentence under it is what she gets: *"Your training, your certificates and what is due next."*

### And Apple ID does not belong in a HIPAA setting

The screen offered a personal Apple account and a personal Google account as the way into a system
holding training records for a regulated senior-living operator. Two consequences:

- When somebody leaves, IT cannot revoke a credential it never issued.
- The audit trail names an identity the organisation does not control.

Replaced with one button — the organisation account IT already manages — and the reason is stated
on the screen rather than assumed: *"access ends the day somebody leaves."*

## 2. What the rebuild does

**Signing in picks a role.** The prototype has three, and they are already switchable from the
header once you are inside. Rather than a password box that accepts anything, the three are on the
page with a real person behind each, and choosing one is the sign-in. That closes the loop with the
existing **View as** menu instead of inventing a second mechanism.

**Failure says what to do.** No *invalid credentials*. Empty email reads *"the address your rota
and payslips go to"*; the forgotten-password link says the administrator resets it, **and why** —
the account is the organisation's, not the learner's, so there is no self-service reset.

**The panel is the supplied render**, full bleed, with the copy anchored at the bottom over a
scrim. My first version was an abstract amber wash on the sequential ramp, on the argument that a
picture of somebody at a desk says less than one true sentence about the product. Overruled
2026-08-20, and the render is better on one count I had not weighted: it shows the thing being
used on a wall display in a care setting, which is where a lot of this training actually gets
watched. The sentence stayed; only the background changed.

## 3. Wiring

`Sign out` was added to the bottom of the **View as** menu on all **27** pages that carry the app
shell, under a rule and without a radio dot — it is not a fourth thing you can look as.

`skylearn/index.html` is still the administrator dashboard, so **signin.html is reachable but is not
yet the landing page**. See the open question below.

## 4. Verified

Headless, since the preview renderer has not responded for this project.

- All four copy faults gone from rendered text; heading and button now agree
- Placeholder is `firstname.lastname@skypoint.ai`; 2 inputs, 2 labels
- All three destinations exist; class audit clean both directions, braces 0, tags balanced
- 29 pages execute with a null-returning DOM, none throw; all serve 200
- Sign out sits **inside** the menu panel on all 27, verified by div matching, not by string search

### Contrast over the render

A picture cannot be reasoned about the way a token can, so the scrim was **measured against the
picture** — decoded, sampled pixel by pixel under each block of copy, at four panel shapes, because
`object-fit: cover` moves the crop and you cannot know what lands behind a given word.

The first attempt reasoned about it the easy way instead: the brightest pixel in the render is pure
white (the wall display, the pendant lamp), so a scrim strong enough to hold white text over *white*
must hold everywhere. That gave 82% fading to nothing by 56% up the panel — **9.83:1**, apparently
fine.

It was wrong, and only measuring against the real pixels showed it. The number was right for the
*bottom* of the panel; the heading does not sit at the bottom. By the height it occupies, the
gradient had already thinned to roughly half — and directly behind it is the brightly lit desk:

| scrim ramp | worst point, real pixels, 4 panel shapes |
|---|---|
| `.82 → .66 → 0` at 0/24/56% (first attempt) | **3.64:1** — fails |
| `.84 → .82 → .42 → 0` at 0/32/48/68% (shipped) | **9.82:1** |

The fix is to hold ~82% *flat through the whole copy band* and only then fade, rather than starting
to fade immediately. It still clears by 68%, so the wall display — the reason for using this
picture — is untouched.

**The lesson is that a worst-case bound is not a measurement.** "White is the brightest pixel, so
solve for white" was sound, and it still produced a heading at 3.64:1, because it answered a
question about *colour* when the failure was about *position*.

The copy is plain `#fff`, **not** a ramp token. The render does not flip with the theme — it stays
a light, warm picture in dark mode — so a theme-aware text colour would have been wrong half the
time. That is the opposite of the rule for the tokened version, and the reason is worth keeping:
*match the text colour to what is actually behind it, not to the theme.*

### The bug the earlier version left behind

Worth recording because the rule outlived the panel. The abstract version was first written with a
hardcoded brown heading over a `--seq-2 → --seq-4` wash: **5.48:1**, fine — in light.

The sequential ramp **inverts** between themes. `--seq-4` is `#f5a300` in light and `#c08a10` in
dark, so it is among a panel's lightest colours in one theme and its darkest in the other. The same
wash measured **2.52:1** in dark. Nothing would have caught it, because no skyLearn page persists a
theme today.

That panel is gone, but the rule it produced is in
[`UI-CHECKLIST.md` §27](UI-CHECKLIST.md) and applies to every future use of the ramp.

## 5. Open questions

1. **Should this be the landing page?** `skylearn/index.html` is the administrator dashboard.
   Making sign-in the front door means renaming it and repointing every *Administrator* link —
   roughly 28 files. Cheap to do, but it is your call, not mine.
2. **Is there a real sign-up at all?** Staff are provisioned by an administrator; nobody
   self-registers into a compliance system. If that holds, the screen the original was built from
   should not exist.
3. **`gamification.html` is orphaned** — no app shell, linked from nothing, apparently superseded by
   `recognition.html`. It is the only page with no View As menu.
