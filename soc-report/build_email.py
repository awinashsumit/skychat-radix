#!/usr/bin/env python3
"""
Builds the SkyPoint Managed SOC weekly summary as an HTML email.

Why a generator and not hand-written HTML: the layout is a table grid whose
column widths must sum exactly to the content width in every row, and the
white gutters between tiles are real spacer cells. Done by hand that drifts
the first time anyone edits a column. Here the widths are asserted.

GRID
    outer 640  side padding 24  content 592  gutter 8
    2-up 292 | 3-up 192 | 4-up 142     (all whole pixels, see assert_row)

EMAIL CONSTRAINTS this file exists to satisfy
    - no external stylesheet, no CSS variables (Gmail strips both)
    - no flexbox/grid: layout is <table role="presentation">
    - styles inline; the <style> block carries only progressive enhancement
    - padding lives on <td>, never on <div> (Word engine ignores it)
    - explicit px line-heights + mso-line-height-rule for Outlook
    - border-radius degrades to square corners in Outlook, which is fine
"""

W_OUTER, PAD, GUT = 640, 24, 8
CELL_PAD_X = 12          # horizontal padding inside a table tile
CONTENT = W_OUTER - 2 * PAD           # 544

SANS  = "'Inter','Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
SERIF = "'Source Serif 4',Georgia,'Times New Roman',serif"

# The amber wash ramp: brand #FFB31C over white at 4/12/32/37/55 percent.
W1, W2, W3, W4, W5 = "#fffaf1", "#fff6e4", "#ffeabf", "#ffe5b2", "#ffd582"
INK, INK_LOW       = "#161616", "#a0a0a0"
AMBER              = "#ffb31c"
FG, FG_LOW, FG_SUB = "#202020", "#646464", "#838383"
WHITE              = "#ffffff"

# The one knob for the contrast call. AMBER is the design as drawn (1.72:1 on
# the card fill); "#a05a00" is the same hue further down the ramp at 5.10:1.
STAT_COLOR = AMBER

# --- Brand mark ------------------------------------------------------------
# assets/skypoint-lockup-disc.png is the full lockup on transparency, 199x55:
# a white disc carrying the black serif "S" and the amber dot, then the white
# "skypoint" wordmark. Verified by compositing it on #161616 before wiring.
#
# The disc is BAKED INTO the artwork, which is the point: Outlook's Word engine
# ignores border-radius, so a CSS disc would render as a white SQUARE behind a
# black mark on the dark band. Never rebuild it in CSS.
#
# The wordmark is part of the image, so no live text sits beside it.
#
# Email cannot carry a logo any way other than a hosted image: inline SVG is
# unsupported in Gmail and Outlook, and both strip base64 data URIs. At send
# time LOGO_URL must be a public HTTPS URL that never redirects.
#
# Display 130x36 holds the source 3.618 aspect to within 0.2%. The source is
# only 1.53x that, so re-export at 260x72 for a true 2x on retina.
LOGO_URL   = ""                                 # <- set before sending
LOGO_LOCAL = "assets/skypoint-lockup-disc.png"  # preview only, never sent
LOGO_W, LOGO_H = 130, 36                        # displayed size in px

# Type scale for a 600px measure. Ratio ~1.2. Every size carries an explicit
# line-height because Outlook ignores unitless ones.
T = {
    "stat":    (30, 32), "wordmark": (22, 26), "title":  (18, 24),
    "heading": (17, 22), "lead":     (15, 22), "body":   (14, 20),
    "cell":    (13, 18), "note":     (12, 17), "fine":   (11, 16),
}


def font(size_key, family=SANS, color=FG, weight=400, extra=""):
    px, lh = T[size_key]
    return (f"margin:0;font-family:{family};font-size:{px}px;line-height:{lh}px;"
            f"mso-line-height-rule:exactly;font-weight:{weight};color:{color};{extra}")


def assert_row(widths):
    """A row is only valid if its cells plus its gutters fill the content width."""
    total = sum(widths) + GUT * (len(widths) - 1)
    assert total == CONTENT, f"row {widths} sums to {total}, expected {CONTENT}"
    return widths


def assert_flush(widths):
    """A data-table row carries no gutters, so its cells alone fill the width."""
    total = sum(widths)
    assert total == CONTENT, f"flush row {widths} sums to {total}, expected {CONTENT}"
    return widths


def gutter_td(cls="gut"):
    """Real spacer cell. class "gut" flips to a full-width 8px band on mobile,
    which is what turns a stacking tile row into stacked tiles with their gaps
    intact. class "dgut" stays a column, because a data table keeps its shape."""
    return (f'<td class="{cls}" width="{GUT}" style="width:{GUT}px;font-size:0;'
            f'line-height:0;">&nbsp;</td>')


def tiles_row(cells, widths, valign="top"):
    """cells: list of inner HTML. widths: matching column widths."""
    assert_row(widths)
    out = []
    for i, (html, w) in enumerate(zip(cells, widths)):
        if i:
            out.append(gutter_td())
        out.append(f'<td class="stack" width="{w}" valign="{valign}" '
                   f'style="width:{w}px;">{html}</td>')
    return "<tr>" + "".join(out) + "</tr>"


def vgap(cols, h=GUT):
    return (f'<tr><td colspan="{cols}" height="{h}" style="height:{h}px;'
            f'font-size:0;line-height:0;">&nbsp;</td></tr>')


def stat_tile(value, label):
    return (
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
        f'width="100%" style="width:100%;table-layout:fixed;border-collapse:separate;">'
        f'<tr><td bgcolor="{W1}" style="background-color:{W1};border:1px solid {W5};'
        f'border-radius:8px;padding:16px 16px 20px;">'
        f'<p style="{font("stat", color=STAT_COLOR, weight=300)}">{value}</p>'
        f'<p style="{font("body", extra="padding-top:12px;")}">{label}</p>'
        f'</td></tr></table>'
    )


def data_table(headers, rows, widths, numeric=(), current=None):
    """Flush cells, no gutters. Rows are told apart by a 1px white rule rather
    than by a gap, and only the four outer corners are rounded, so the table
    reads as one block instead of a field of tiles."""
    assert_flush(widths)
    last = len(widths) - 1
    n_rows = len(rows)
    R = 6   # outer corner radius

    def vrule(col):
        return f"border-right:1px solid {WHITE};" if col < last else ""

    def cell_w(col, w):
        """Declared width is CONTENT width: subtract padding and any divider."""
        return w - 2 * CELL_PAD_X - (1 if col < last else 0)

    def radius(col, row):
        """row: 'head' or an index into rows. Only true outer corners round."""
        tl = R if (row == "head" and col == 0) else 0
        tr = R if (row == "head" and col == last) else 0
        bl = R if (row == n_rows - 1 and col == 0) else 0
        br = R if (row == n_rows - 1 and col == last) else 0
        return f"border-radius:{tl}px {tr}px {br}px {bl}px;" if (tl or tr or bl or br) else ""

    out = [f'<table role="presentation" class="fluid dt" cellpadding="0" cellspacing="0" border="0" '
           f'width="{CONTENT}" style="width:{CONTENT}px;table-layout:fixed;'
           f'border-collapse:separate;border-spacing:0;">']

    head = []
    for i, (h, w) in enumerate(zip(headers, widths)):
        align = "right" if i in numeric else "left"
        head.append(
            f'<th width="{cell_w(i, w)}" align="{align}" bgcolor="{W4}" '
            f'style="width:{cell_w(i, w)}px;background-color:{W4};'
            f'padding:12px {CELL_PAD_X}px;text-align:{align};{vrule(i)}{radius(i, "head")}">'
            f'<span style="{font("cell", weight=600)}">{h}</span></th>')
    out.append("<tr>" + "".join(head) + "</tr>")

    for r_i, row in enumerate(rows):
        is_cur = current is not None and r_i == current
        bg = W3 if is_cur else W2
        # A hairline in the page colour separates rows without reopening a gap.
        rule = (f"border-bottom:1px solid {WHITE};" if r_i < n_rows - 1 else "")
        cells = []
        for i, (cell, w) in enumerate(zip(row, widths)):
            align = "right" if i in numeric else "left"
            lead = (i == 0) or is_cur
            cells.append(
                f'<td width="{cell_w(i, w)}" align="{align}" bgcolor="{bg}" '
                f'style="width:{cell_w(i, w)}px;background-color:{bg};'
                f'padding:13px {CELL_PAD_X}px;text-align:{align};{rule}{vrule(i)}{radius(i, r_i)}">'
                f'<span style="{font("cell", color=FG if lead else FG_LOW, weight=500 if lead else 400)}">'
                f'{cell}</span></td>')
        out.append("<tr>" + "".join(cells) + "</tr>")

    out.append("</table>")
    return "".join(out)


def section(title, body_html, note=None):
    parts = [f'<tr><td style="padding:32px 0 14px;">'
             f'<h2 style="{font("heading", weight=600)}">{title}</h2></td></tr>',
             f'<tr><td>{body_html}</td></tr>']
    if note:
        parts.append(f'<tr><td style="padding-top:12px;">'
                     f'<p style="{font("note", color=FG_LOW)}">{note}</p></td></tr>')
    return "".join(parts)


# ----------------------------------------------------------------- content
stats_a = [stat_tile("30", "Alerts Raised"),
           stat_tile("30", "Closed"),
           stat_tile("0",  "Open at Close")]
stats_b = [stat_tile("0",  "Confirmed Threats"),
           stat_tile("97", "Within SLA %")]

def tile_band(cells, widths):
    """One row of tiles as a self-contained table. Column widths resolve per
    table in HTML, so a 3-up band and a 2-up band must not share one."""
    return (f'<table role="presentation" class="fluid" cellpadding="0" cellspacing="0" border="0" '
            f'width="{CONTENT}" style="width:{CONTENT}px;table-layout:fixed;border-collapse:collapse;">'
            + tiles_row(cells, widths) + '</table>')


glance = (f'<table role="presentation" class="fluid" cellpadding="0" cellspacing="0" border="0" '
          f'width="{CONTENT}" style="width:{CONTENT}px;table-layout:fixed;border-collapse:collapse;">'
          f'<tr><td>{tile_band(stats_a, assert_row([192, 192, 192]))}</td></tr>'
          + vgap(1)
          + f'<tr><td>{tile_band(stats_b, assert_row([292, 292]))}</td></tr>'
          + '</table>')

sla = data_table(
    ["Priority", "Closed", "Resolution target", "Within target"],
    [["High", "17", "2 hours", "94.0%"],
     ["Medium", "13", "4 hours", "100.0%"]],
    assert_flush([146, 116, 184, 146]), numeric=(1, 3))

categories = data_table(
    ["Category", "Raised", "Outcome"],
    [["Privilege / role assignment change", "11", "Authorised or expected activity"],
     ["Network security control change",    "10", "Authorised or expected activity"],
     ["Bulk resource deletion",              "6", "Authorised or expected activity"],
     ["Security policy change",              "2", "Authorised or expected activity"],
     ["Anomalous data egress volume",        "1", "Authorised or expected activity"]],
    assert_flush([268, 78, 246]), numeric=(1,))

trend = data_table(
    ["Week commencing", "Alerts", "High priority", "Confirmed threats"],
    [["27 Jul", "22", "15", "1"],
     ["03 Aug", "44", "15", "0"],
     ["10 Aug", "52", "23", "0"],
     ["17 Aug (this report)", "30", "17", "0"]],
    assert_flush([192, 106, 136, 158]),
    numeric=(1, 2, 3), current=3)

# Absolute URL wins. Failing that, a local file lets the template be previewed
# in a browser; that path is useless in an actual send, so the build says so.
import os

if LOGO_URL:
    _src, _note = LOGO_URL, None
elif os.path.exists(LOGO_LOCAL):
    _src, _note = LOGO_LOCAL, f"preview only: relative src {LOGO_LOCAL!r}, set LOGO_URL before sending"
else:
    _src, _note = None, f"no logo yet: drop {LOGO_LOCAL!r} in place, then set LOGO_URL before sending"

if _src:
    mark_cell = (
        f'<img src="{_src}" width="{LOGO_W}" height="{LOGO_H}" alt="skypoint" '
        f'style="display:block;width:{LOGO_W}px;height:{LOGO_H}px;border:0;outline:none;'
        f'text-decoration:none;-ms-interpolation-mode:bicubic;'
        f'font-family:{SERIF};font-size:22px;line-height:36px;color:{WHITE};" />')
else:
    # Placeholder disc so the layout is never left broken while the asset is
    # outstanding. Square corners in Outlook, which is exactly why it is not shippable.
    mark_cell = (
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
        f'<td width="{LOGO_W}" height="{LOGO_H}" align="center" valign="middle" bgcolor="{WHITE}" '
        f'style="width:{LOGO_W}px;height:{LOGO_H}px;background-color:{WHITE};border-radius:{LOGO_W // 2}px;">'
        f'<span style="{font("wordmark", SERIF, INK)}">s</span></td></tr></table>')

PREHEADER = ("No confirmed security incidents. 30 alerts raised, 30 closed, "
             "97% within SLA for the week commencing 17 August 2026.")

HTML = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="x-apple-disable-message-reformatting" />
<meta name="color-scheme" content="light" />
<meta name="supported-color-schemes" content="light" />
<title>Security Operations Weekly Summary</title>
<!--[if mso]>
<xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml>
<style>table,td,h1,h2,p,span {{ font-family: 'Segoe UI', Arial, sans-serif !important; }}</style>
<![endif]-->
<!-- Webfonts load in Apple Mail and iOS only. Everything falls back to the
     stacks declared inline, which is why no size depends on Inter loading. -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&amp;family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&amp;display=swap" rel="stylesheet" />
<style>
  body {{ margin:0; padding:0; width:100% !important; -webkit-text-size-adjust:100%; }}
  img {{ border:0; outline:none; text-decoration:none; }}
  table {{ border-collapse:collapse; }}
  a {{ color:#a05a00; }}
  @media screen and (max-width:640px) {{
    .shell   {{ width:100% !important; }}
    .pad     {{ padding-left:16px !important; padding-right:16px !important; }}
    /* Tiles become full-width blocks and the spacer cells become the gaps
       between them, so the 8px rhythm survives the stack. */
    .stack   {{ display:block !important; width:100% !important; }}
    .gut     {{ display:block !important; width:100% !important; height:8px !important; }}
    /* Every fixed-width table goes fluid, or the page scrolls sideways. */
    .fluid   {{ width:100% !important; }}
    /* Data tables keep their columns rather than stacking, which would break
       the header-to-cell relationship, but drop to auto layout so the px
       widths can compress instead of overflowing. */
    .dt      {{ table-layout:auto !important; }}
    /* Right-aligned masthead text orphans its last word once stacked. */
    .m-left  {{ text-align:left !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:{WHITE};">

<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{PREHEADER}</div>

<!-- ===================== MASTHEAD, full-bleed dark ===================== -->
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{INK}" style="width:100%;background-color:{INK};">
<tr><td align="center">
  <table role="presentation" class="shell" cellpadding="0" cellspacing="0" border="0" width="{W_OUTER}" style="width:{W_OUTER}px;">
  <tr><td class="pad" style="padding:28px {PAD}px;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;">
    <tr>
      <!-- Full lockup in one image, disc baked in. Alt text carries the brand
           when images are blocked, which is Outlook's default. -->
      <td class="stack" valign="middle" style="width:{LOGO_W}px;">{mark_cell}</td>
      <td class="stack m-left" align="right" valign="middle">
        <h1 style="{font('title', SERIF, AMBER, 600)}">Security Operations &mdash; Weekly Summary</h1>
        <p style="{font('fine', color=INK_LOW, extra='padding-top:8px;')}">Delta Dental of Arizona &middot; week commencing 17 August 2026</p>
        <p style="{font('fine', color=INK_LOW, extra='padding-top:2px;')}">Prepared by SkyPoint Cloud Managed SOC &middot; issued 24 August 2026</p>
      </td>
    </tr>
    </table>
  </td></tr>
  </table>
</td></tr>
</table>

<!-- ===================== BODY ===================== -->
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="{WHITE}" style="width:100%;background-color:{WHITE};">
<tr><td align="center">
  <table role="presentation" class="shell" cellpadding="0" cellspacing="0" border="0" width="{W_OUTER}" style="width:{W_OUTER}px;">
  <tr><td class="pad" style="padding:32px {PAD}px 36px;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;">

    <tr><td bgcolor="{W3}" style="background-color:{W3};border-radius:8px;padding:18px 20px;">
      <p style="{font('lead', weight=600)}">Position this week: no confirmed security incidents.</p>
      <p style="{font('body', extra='padding-top:6px;')}">All alerts raised during the period were investigated and attributed to authorised activity. No malicious or unauthorised access was identified, and no customer data was affected.</p>
    </td></tr>

    {section("At a glance", glance)}

    {section("Service level performance", sla,
             "Resolution time is measured from alert creation to closure. "
             "Acknowledgement-time reporting will be introduced in a future edition "
             "once first-response capture is in place.")}

    {section("Alert categories", categories,
             "Detection rules are intentionally broad so that no genuine signal is "
             "missed. A high proportion of authorised-activity matches is expected by design.")}

    {section("Four-week trend", trend)}

    {section("Monitoring coverage",
             f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;border-collapse:separate;border-spacing:0;">'
             f'<tr><td bgcolor="{W1}" style="background-color:{W1};border:1px solid {W5};border-radius:8px;padding:18px 20px;">'
             f'<p style="{font("cell", color=FG_LOW)}">'
             f'<span style="color:{FG};font-weight:500;">Continuous monitoring remained in effect throughout the period</span> '
             f'with no interruption to alert ingestion or detection coverage. Detections are mapped to '
             f'HITRUST CSF and MITRE ATT&amp;CK, covering data egress, privilege change, bulk deletion, '
             f'network and key-management control changes, and database authentication.'
             f'</p></td></tr></table>')}

    <tr><td style="padding-top:32px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;">
      <tr><td height="1" bgcolor="{W5}" style="height:1px;background-color:{W5};font-size:0;line-height:0;">&nbsp;</td></tr>
      </table>
    </td></tr>
    <tr><td style="padding-top:16px;">
      <p style="{font('fine', color=FG_SUB)}">Figures cover alerts raised during the stated period. Case-level detail, system identifiers and investigation records are retained within the SOC platform and available on request under the terms of the service agreement.</p>
    </td></tr>

    </table>
  </td></tr>
  </table>
</td></tr>
</table>

</body>
</html>
"""

def build(logo_src):
    """Same document, different logo source. Everything else is identical."""
    if logo_src:
        mark = (f'<img src="{logo_src}" width="{LOGO_W}" height="{LOGO_H}" alt="skypoint" '
                f'style="display:block;width:{LOGO_W}px;height:{LOGO_H}px;border:0;outline:none;'
                f'text-decoration:none;-ms-interpolation-mode:bicubic;'
                f'font-family:{SERIF};font-size:22px;line-height:36px;color:{WHITE};" />')
    else:
        mark = mark_cell
    return HTML.replace(mark_cell, mark)


if __name__ == "__main__":
    import base64

    print(f"grid ok: content {CONTENT}px, gutter {GUT}px")

    # 1. Production. The logo must be a hosted absolute URL; a relative path is
    #    meaningless once the message leaves this machine.
    with open("weekly-summary.email.html", "w") as f:
        f.write(build(LOGO_URL) if LOGO_URL else HTML)
    if _note:
        print(f"LOGO:    {_note}")
    print("wrote weekly-summary.email.html   (for sending)")

    # 2. Share copy. The logo is inlined as a data URI so the file stands alone
    #    in a browser, on Slack, over AirDrop, anywhere. This copy must NEVER be
    #    used as the actual send: Gmail and Outlook both strip data: images, so
    #    the logo would silently vanish for most recipients.
    if os.path.exists(LOGO_LOCAL):
        b64 = base64.b64encode(open(LOGO_LOCAL, "rb").read()).decode()
        with open("weekly-summary.preview.html", "w") as f:
            f.write(build(f"data:image/png;base64,{b64}"))
        print("wrote weekly-summary.preview.html (self-contained, for review only)")
    else:
        print(f"skipped preview: {LOGO_LOCAL} missing")
