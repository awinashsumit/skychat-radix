# Charts

Four shapes, one hue. Live examples and copyable code: **[`charts.html`](charts.html)**.

```html
<link rel="stylesheet" href="tokens.css?v=77" />
<link rel="stylesheet" href="dashboard.css?v=77" />
<script src="charts.js?v=77" defer></script>
```

Every function returns an HTML string, so it drops into whatever you are already building:

```js
$('panel').innerHTML = Chart.area({ labels: MONTHS, values: signups });
Chart.bind($('panel'));      // only needed for area; safe to call after every render
```

---

## 1. The one rule

**Magnitude is carried by shade of one hue, never by a set of unrelated colours.**

Two reasons, and the second is the one that keeps mattering:

1. It stays on brand. Every chart is Skypoint amber.
2. It survives colour blindness. Someone who cannot separate red from green can still read
   *darker means more*. A rainbow chart makes them guess.

## 2. The ramp, and why it is not the accent scale

`--seq-1` … `--seq-6`, defined in `tokens.css` for both themes.

The obvious move is to reach for `--accent-3` … `--accent-11`. It does not work. That scale is
tuned for UI states — borders, hovers, solid fills — and it is **not monotonic in contrast**:

| | contrast on white |
|---|---|
| `--accent-7` | 1.71 : 1 |
| `--accent-8` | 2.20 : 1 |
| **`--accent-9`** | **1.79 : 1** ← lighter than accent-8 |
| `--accent-10` | 2.07 : 1 |

Shade would not read as order, which is the entire job. And `--accent-3`/`4`/`5` sit at
1.13–1.27 : 1, effectively invisible on a white card.

The sequential ramp climbs steadily instead — 1.09 → 6.68 on white, 1.36 → 13.42 on the dark
page — while keeping the brand hue. Brand amber itself is untouched at `--accent-9`.

| | light | dark |
|---|---|---|
| `--seq-1` | `#fff4dc` | `#3a2a08` |
| `--seq-2` | `#ffe2a8` | `#5c4109` |
| `--seq-3` | `#ffc65c` | `#8a6208` |
| `--seq-4` | `#f5a300` | `#c08a10` |
| `--seq-5` | `#c47400` | `#ffb31c` |
| `--seq-6` | `#8a4d00` | `#ffd479` |

Text on a filled step: `--seq-on-light` up to step 4, `--seq-on-dark` on 5 and 6.

`--seq-empty` is grey, and it means **no data** — which is not the same fact as zero. A chart
that paints "the system was down" the same colour as "nobody logged in" is lying about one of
them. Pass `null` for a missing cell, `0` for a real zero.

## 3. When *not* to use the ramp

The ramp encodes **ordered** magnitude. For unordered categories — Desktop against Mobile, one
course against another — there is no "more", so shade would imply a ranking that does not exist.

Use the categorical palette `--chart-1` … `--chart-8` there, and keep it to four or fewer.

## 4. The four charts

### `Chart.area({ labels, values, ... })`

One series over time. Gradient fade, dashed grid, and a hover column with a dot and a readout —
a shape tells you the trend, only a number tells you the number.

| option | |
|---|---|
| `labels`, `values` | parallel arrays |
| `height` | default 280 |
| `min`, `max` | pin the axis; see the warning below |
| `target`, `targetLabel` | dashed reference line, drawn *over* the data |
| `valueLabel`, `alt` | for the screen-reader summary |

Call `Chart.bind(container)` after inserting, and set `data-unit` on the container for the
tooltip suffix.

> **A baseline above zero exaggerates change.** A rate wobbling 88–92 looks like a cliff on an
> 85–100 axis. Only pass `min` when the reader already knows the scale — a compliance rate
> against a target — and let the axis say so.

**Axis rules, handled for you.** Ticks land on round numbers, not on `max/4`. Integer data gets
integer gridlines, because a chart of "3 completions" with a line at 0.8 offers a reading that
cannot happen. And a pinned span picks a round *step* over a round *count*: over 85–100 you get
85 / 90 / 95 / 100, not 85 / 88 / 91 / 94 / 97 / 100.

### `Chart.heatmap({ rows, cols, values, max })`

Two categories, one value, `values[r][c]`. Ships with its own scale legend — the ramp shown as
itself, with the thresholds under it.

Best when most cells are full. Below roughly 40% density you are asking people to scan empty
space; a ranked list of exceptions serves them better.

### `Chart.donut({ segments, total, label })`

Parts of one whole. Segments sort largest first and take consecutive steps down the ramp, so the
biggest slice is the darkest. Three or four slices, never nine. Renders its own legend with
percentages.

### `Chart.bars({ items, max })`

Ranked horizontal bars, `items: [{ n, v, label }]`. Sorted descending, shade following rank.
The right shape for *where is it worst* — sorting plus length answers it in a glance.

## 5. Verified

Headless, since the preview renderer has not responded for this project.

- `step()` is monotonic across the full range and every one of the six steps is reachable
- Both ramps are monotonic in contrast: light 1.09 → 6.68, dark 1.36 → 13.42
- No duplicate y-axis tick labels for any max from 1 to 2000
- Integer data produces integer gridlines; fractional data keeps fractional ones
- Every generator's markup is tag-balanced, with no `undefined` / `NaN` / `[object Object]`
- The skyLearn dashboard renders on the shared chart across all three ranges

## 6. Open

1. **Should `area` take more than one series?** It is deliberately single-series: two amber
   bands at different shades overlap into a third shade that means nothing. Multi-series wants
   the categorical palette, or small multiples.
2. **Print.** The ramp is screen-tuned; `--seq-1` will likely vanish on paper.
3. **Live regions.** Each chart carries a screen-reader summary, but a chart that updates on a
   filter change should probably announce the new headline rather than the whole series.
