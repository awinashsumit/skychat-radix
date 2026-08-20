/* ============================================================
   Charts, shared across the apps.

   Every function returns an HTML string. No dependencies, no
   build step, no framework: drop <script src="../charts.js"></script>
   in and call it. Styling lives in dashboard.css (.chart, .heat,
   .donut, .series, .bars) and the palette in tokens.css
   (--seq-1 .. --seq-6).

   The one rule these share: magnitude is encoded as SHADE OF ONE
   HUE, never as a set of unrelated colours. Somebody who cannot
   tell red from green can still read "darker means more", and it
   keeps every chart on brand without a rainbow.

   Docs and worked examples: CHARTS.md
   ============================================================ */
(function (global) {
  'use strict';

  var STEPS = 6;
  var esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  };
  var uid = (function () { var n = 0; return function (p) { return p + '-' + (++n); }; })();
  var nice = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ','); };

  /* Which of the six steps a value falls in. Empty is its own answer:
     "nobody logged in" and "we have no data" are different facts, and a
     chart that paints them the same colour is lying about one of them. */
  function step(v, max) {
    if (v == null) return null;
    if (max <= 0) return 1;
    return Math.max(1, Math.min(STEPS, Math.ceil(v / max * STEPS)));
  }
  function fill(s) { return s == null ? 'var(--seq-empty)' : 'var(--seq-' + s + ')'; }

  /* A y-axis people can read: ticks land on 1/2/5 x 10^n, not on
     max/4. Nobody wants a gridline at 3,247. */
  var NICE = [1, 1.5, 2, 2.5, 3, 4, 5, 6, 7.5, 8, 10];
  function niceMax(raw) {
    if (raw <= 0) return 1;
    var mag = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10));
    var f = raw / mag;
    for (var i = 0; i < NICE.length; i++) if (f <= NICE[i] + 1e-9) return NICE[i] * mag;
    return 10 * mag;
  }
  function ticks(max, count) {
    var out = [];
    for (var i = 0; i <= count; i++) out.push(max * i / count);
    return out;
  }

  /* Round step sizes beat a round number of lines. Over a span of 15,
     five gaps give 85/88/91/94/97/100 and three give 85/90/95/100 -- the
     second is the one people read without thinking. Score each candidate by
     how round its step is, then lean towards four gridlines. */
  function divisor(span) {
    var best = 4, bestScore = -1;
    for (var q = 5; q >= 2; q--) {
      var s = span / q;
      if (s % 1 !== 0) continue;
      var score = s % 10 === 0 ? 3 : s % 5 === 0 ? 2 : s % 2 === 0 ? 1 : 0;
      if (score > bestScore || (score === bestScore && Math.abs(q - 4) < Math.abs(best - 4))) {
        best = q; bestScore = score;
      }
    }
    return bestScore < 0 ? 4 : best;
  }

  /* Counts are integers, so their gridlines must be too. A chart of
     "3 completions" with a line at 0.8 is offering a reading that cannot
     happen. Pick a divisor that lands every tick on a whole number. */
  function axis(vals) {
    var raw = Math.max.apply(null, vals.concat([1]));
    var allInt = vals.every(function (v) { return v == null || v % 1 === 0; });
    var max = niceMax(raw);
    if (!allInt) return { max: max, n: 4 };
    max = Math.max(1, Math.ceil(max));
    for (var n = 4; n >= 2; n--) if (max % n === 0) return { max: max, n: n };
    return { max: max + (4 - max % 4), n: 4 };
  }
  var fmt = function (n) {
    if (n >= 1000000) return (n / 1000000).toFixed(n % 1000000 ? 1 : 0) + 'M';
    if (n >= 1000) return (n / 1000).toFixed(n % 1000 ? 1 : 0) + 'K';
    return String(Math.round(n * 10) / 10);
  };

  /* ----------------------------------------------------------
     area({ labels, values, valueLabel, height })
     One series. Gradient fade, dashed grid, and a hover column
     with a dot and a tooltip -- the interaction the reference
     dashboard uses, because a shape tells you the trend and only
     a readout tells you the number.
     ---------------------------------------------------------- */
  function area(o) {
    var labels = o.labels || [], vals = o.values || [];
    var w = 760, h = o.height || 280;
    var pad = { l: 44, r: 12, t: 14, b: 30 };
    var ax = axis(vals), max = o.max != null ? o.max : ax.max;
    /* A baseline above zero exaggerates change: a rate wobbling 88-92 looks
       like a cliff on a 85-95 axis. Only pass `min` when the reader already
       knows the scale -- a compliance rate against a target, say -- and say
       so on the axis. */
    var min = o.min || 0;
    /* When the caller fixes the span, the tick count has to divide it or the
       gridlines land on 88.8 and 96.3. Prefer 4 lines, accept fewer. */
    var span = max - min, tn = ax.n;
    if (o.max != null || o.min != null) tn = divisor(span);
    var n = labels.length;
    var gid = uid('seqFade');
    var x = function (i) { return n < 2 ? pad.l : pad.l + i * (w - pad.l - pad.r) / (n - 1); };
    var y = function (v) { return pad.t + (1 - (v - min) / (max - min)) * (h - pad.t - pad.b); };
    var d = vals.map(function (v, i) { return (i ? 'L' : 'M') + x(i).toFixed(1) + ' ' + y(v).toFixed(1); }).join(' ');

    var grid = ticks(span, tn).map(function (g) {
      var v = min + g;
      return '<line class="grid-line" x1="' + pad.l + '" x2="' + (w - pad.r) + '" y1="' + y(v).toFixed(1) + '" y2="' + y(v).toFixed(1) + '"/>' +
        '<text class="axis-text" x="' + (pad.l - 10) + '" y="' + (y(v) + 4).toFixed(1) + '" text-anchor="end">' + fmt(v) + '</text>';
    }).join('');

    /* A target is a promise, so it is drawn on top of the data, not under it. */
    var target = o.target == null ? '' :
      '<line class="target-line" x1="' + pad.l + '" x2="' + (w - pad.r) + '" y1="' + y(o.target).toFixed(1) +
        '" y2="' + y(o.target).toFixed(1) + '"/>' +
      '<text class="target-text" x="' + (w - pad.r) + '" y="' + (y(o.target) - 7).toFixed(1) + '" text-anchor="end">' +
        esc(o.targetLabel || ('Target ' + fmt(o.target))) + '</text>';

    var every = Math.max(1, Math.ceil(n / 8));
    var xs = labels.map(function (l, i) {
      return i % every ? '' :
        '<text class="axis-text" x="' + x(i).toFixed(1) + '" y="' + (h - 8) + '" text-anchor="middle">' + esc(l) + '</text>';
    }).join('');

    var bw = n < 2 ? 24 : (w - pad.l - pad.r) / (n - 1);
    var hot = vals.map(function (v, i) {
      var cx = x(i), top = pad.t, bot = y(min);
      return '<rect class="area-band" x="' + (cx - bw / 2).toFixed(1) + '" y="' + top + '" width="' + bw.toFixed(1) + '" height="' + (bot - top) + '" rx="3"/>' +
        '<circle class="area-dot" cx="' + cx.toFixed(1) + '" cy="' + y(v).toFixed(1) + '" r="5"/>' +
        '<rect class="area-hit" x="' + (cx - bw / 2).toFixed(1) + '" y="' + top + '" width="' + bw.toFixed(1) + '" height="' + (bot - top) + '"' +
        ' data-i="' + i + '" data-x="' + cx.toFixed(1) + '" data-y="' + y(v).toFixed(1) + '"' +
        ' data-label="' + esc(labels[i]) + '" data-value="' + esc(nice(v)) + '"/>';
    }).join('');

    return '<div class="chart chart-frame">' +
      '<svg viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="' + esc(o.alt || 'Trend over time') + '">' +
        '<defs><linearGradient id="' + gid + '" x1="0" y1="0" x2="0" y2="1">' +
          '<stop offset="0%" stop-color="var(--seq-4)" stop-opacity=".38"/>' +
          '<stop offset="100%" stop-color="var(--seq-4)" stop-opacity="0"/>' +
        '</linearGradient></defs>' +
        grid +
        '<path class="area-fill" style="fill:url(#' + gid + ')" d="' + d + ' L ' + x(n - 1).toFixed(1) + ' ' + y(min).toFixed(1) + ' L ' + x(0).toFixed(1) + ' ' + y(min).toFixed(1) + ' Z"/>' +
        '<path class="area-line" d="' + d + '"/>' + target +
        hot + xs +
      '</svg>' +
      '<div class="chart-tip" data-tip><b></b><span></span></div>' +
      '<span class="sr-only">' + esc(o.valueLabel || 'Values') + ': ' +
        labels.map(function (l, i) { return esc(l) + ' ' + nice(vals[i]); }).join(', ') + '</span>' +
    '</div>';
  }

  /* ----------------------------------------------------------
     heatmap({ rows, cols, values, max })
     values[r][c], null for "no data". Rows and columns are
     labelled; the shade is the whole message.
     ---------------------------------------------------------- */
  function heatmap(o) {
    var rows = o.rows || [], cols = o.cols || [], v = o.values || [];
    var flat = [];
    v.forEach(function (r) { r.forEach(function (c) { if (c != null) flat.push(c); }); });
    var max = o.max || niceMax(Math.max.apply(null, flat.concat([1])));
    var every = Math.max(1, Math.ceil(cols.length / 10));

    var body = rows.map(function (rn, r) {
      return '<div class="heat-row-label">' + esc(rn) + '</div>' +
        '<div class="heat" style="grid-template-columns:repeat(' + cols.length + ',1fr);">' +
          cols.map(function (cn, c) {
            var val = (v[r] || [])[c];
            var s = step(val, max);
            return '<div class="heat-cell" style="background:' + fill(s) + ';"' +
              ' title="' + esc(rn) + ', ' + esc(cn) + ': ' + (val == null ? 'no data' : nice(val)) + '"></div>';
          }).join('') +
        '</div>';
    }).join('');

    return '<div class="heat-wrap">' + body +
      '<div></div><div class="heat" style="grid-template-columns:repeat(' + cols.length + ',1fr);">' +
        cols.map(function (cn, c) {
          return '<div class="heat-col-label">' + (c % every ? '' : esc(cn)) + '</div>';
        }).join('') +
      '</div></div>' + scale(max);
  }

  /* The ramp, shown as itself, with the thresholds it encodes. */
  function scale(max) {
    var out = '<div class="seq-scale"><div class="seq-bar" style="grid-template-columns:repeat(' + STEPS + ',1fr);">';
    for (var i = 1; i <= STEPS; i++) out += '<span style="background:var(--seq-' + i + ');"></span>';
    out += '</div><div class="seq-ticks">';
    for (var k = 0; k <= STEPS; k += 2) out += '<span>' + fmt(max * k / STEPS) + '</span>';
    return out + '</div></div>';
  }

  /* ----------------------------------------------------------
     donut({ segments, total, label })
     Segments take consecutive steps of the ramp, largest first,
     so the biggest slice is the darkest.
     ---------------------------------------------------------- */
  function donut(o) {
    var segs = (o.segments || []).slice().sort(function (a, b) { return b.v - a.v; });
    var total = o.total != null ? o.total : segs.reduce(function (s, x) { return s + x.v; }, 0);
    var r = 70, c = 2 * Math.PI * r, gap = 2, off = 0;

    var arcs = segs.map(function (s, i) {
      var frac = total ? s.v / total : 0;
      var len = Math.max(0, frac * c - gap);
      var tone = 'var(--seq-' + Math.max(2, STEPS - i) + ')';
      var a = '<circle cx="90" cy="90" r="' + r + '" stroke="' + tone + '"' +
        ' stroke-dasharray="' + len.toFixed(1) + ' ' + (c - len).toFixed(1) + '"' +
        ' stroke-dashoffset="' + (-off).toFixed(1) + '" transform="rotate(-90 90 90)"/>';
      off += frac * c;
      s._tone = tone;
      return a;
    }).join('');

    return '<div class="donut">' +
      '<svg viewBox="0 0 180 180" role="img" aria-label="' + esc(o.label || 'Breakdown') + ': ' +
        segs.map(function (s) { return esc(s.n) + ' ' + nice(s.v); }).join(', ') + '">' +
        '<circle class="donut-track" cx="90" cy="90" r="' + r + '"/>' + arcs +
      '</svg>' +
      '<div class="donut-centre"><span class="donut-v">' + nice(total) + '</span>' +
        '<span class="donut-l">' + esc(o.label || '') + '</span></div>' +
    '</div>' + series(segs, total);
  }

  function series(segs, total) {
    return '<div class="series">' + segs.map(function (s) {
      var pct = total ? (s.v / total * 100) : 0;
      return '<div class="series-row"><span class="series-sw" style="background:' + s._tone + ';"></span>' +
        '<span class="series-n">' + esc(s.n) + '</span>' +
        '<span class="series-v">' + pct.toFixed(1) + '%</span></div>';
    }).join('') + '</div>';
  }

  /* ----------------------------------------------------------
     bars({ items, max })  -- horizontal, ranked, shade by rank
     ---------------------------------------------------------- */
  function bars(o) {
    var items = (o.items || []).slice().sort(function (a, b) { return b.v - a.v; });
    var max = o.max || Math.max.apply(null, items.map(function (x) { return x.v; }).concat([1]));
    return '<div class="bars">' + items.map(function (it, i) {
      var tone = 'var(--seq-' + Math.max(2, STEPS - Math.floor(i * STEPS / Math.max(1, items.length))) + ')';
      return '<div class="bar-row"><span class="bar-n" title="' + esc(it.n) + '">' + esc(it.n) + '</span>' +
        '<span class="bar-track"><i class="bar-fill" style="width:' + (max ? it.v / max * 100 : 0).toFixed(1) + '%;background:' + tone + ';"></i></span>' +
        '<span class="bar-v">' + esc(it.label != null ? it.label : nice(it.v)) + '</span></div>';
    }).join('') + '</div>';
  }

  /* ----------------------------------------------------------
     bind(root) -- wire hover on any area chart inside root.
     Idempotent: safe to call after every re-render.
     ---------------------------------------------------------- */
  function bind(root) {
    (root || document).querySelectorAll('.chart-frame').forEach(function (frame) {
      var tip = frame.querySelector('[data-tip]');
      if (!tip) return;
      frame.querySelectorAll('.area-hit').forEach(function (hit) {
        hit.addEventListener('mouseenter', function () {
          var svg = frame.querySelector('svg'), box = svg.getBoundingClientRect();
          var vb = svg.viewBox.baseVal, sx = box.width / vb.width, sy = box.height / vb.height;
          frame.querySelectorAll('.area-dot.is-on, .area-band.is-on').forEach(function (n) { n.classList.remove('is-on'); });
          hit.previousElementSibling.classList.add('is-on');                 /* the dot */
          hit.previousElementSibling.previousElementSibling.classList.add('is-on'); /* the band */
          tip.querySelector('b').textContent = hit.dataset.label;
          tip.querySelector('span').innerHTML = '<em>' + esc(hit.dataset.value) + '</em> ' + esc(frame.dataset.unit || '');
          tip.style.left = (+hit.dataset.x * sx) + 'px';
          tip.style.top = (+hit.dataset.y * sy) + 'px';
          tip.classList.add('is-on');
        });
      });
      frame.addEventListener('mouseleave', function () {
        tip.classList.remove('is-on');
        frame.querySelectorAll('.is-on').forEach(function (n) { n.classList.remove('is-on'); });
      });
    });
  }

  global.Chart = { area: area, heatmap: heatmap, donut: donut, bars: bars, scale: scale, bind: bind, step: step, fill: fill };
})(this);
