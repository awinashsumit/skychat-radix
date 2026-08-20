# skyLearn Certificates: research and information architecture

Module 3. Why `certificate.html` is shaped the way it is. Course flow reasoning is in
[`CREATE-COURSE-IA.md`](CREATE-COURSE-IA.md); the dashboard's in [`DASHBOARD-IA.md`](DASHBOARD-IA.md).

---

## 1. A certificate is evidence, not a souvenir

The reference screens (Eduverse, built on a Teachable-style creator product) treat a certificate as
a decorative artefact: a title, a name, a date, a colour picker. That is right for an online course
marketplace, where the certificate is a keepsake the learner posts to LinkedIn.

In senior living it is the document a **state surveyor asks to see**. It has to answer: who
completed what, when, for how many hours, valid until when, and can this record be verified. A
certificate that omits the hours is not proof of anything, because Ohio, Texas and Florida count
hours, not courses.

So the builder keeps the reference's shape (Content and Design tabs, live preview, activate step)
and changes what is on the certificate.

## 2. Certificates are organisation-level

A course does not design its own certificate. The organisation owns a small set of them and each
course's Settings step picks one. That is why this is a screen under Certifications rather than a
fifth step in the course wizard, and why the Settings field now links here.

Three seeded: Skypoint standard, State of Ohio format, Continuing education.

## 3. The content is a checklist of evidence, not free-form fields

Rather than a blank canvas, the Content tab lists the six things a certificate can carry, each as a
switch with the reason it exists:

| Field | Why | Required |
|---|---|---|
| Completion date | Every state asks when the training happened. | Yes |
| Training hours | Ohio, Texas and Florida count hours, not courses. | Yes |
| Valid until | Shows the renewal deadline without a separate lookup. | No |
| CE credits | Only for accredited continuing education. | No |
| Licence number | The learner's state registry or licence number. | No |
| Serial number | Lets an inspector verify the record is genuine. | No |

Switching off a required one raises a warning on the page and again in the activate dialog, where
the button changes to **Activate anyway**. The product states the risk and still lets the
organisation decide, because only they know what their state asks for.

## 4. A curated palette, not a colour picker

The reference offers a full colour wheel with a hex field and an eyedropper. Our authors are not
designers, and an arbitrary hex produces off-brand certificates that fail to photocopy.

Six swatches instead, **every one verified at 4.5:1 or better against white paper**, in both
directions: the title colour on white, and white logo text on the swatch. The first draft used
`#B8770E` for the brand amber and measured 3.70:1; it now uses `#A05A00`, which is the design
system's own text-safe amber step and measures 5.31:1.

That check is automated, so a future swatch cannot be added without meeting it.

## 5. Other decisions

- **One drawing function.** The same code renders the live preview, the list thumbnails and the
  template picker, so what is chosen is exactly what is issued. No separate mock images to drift.
- **The preview uses real sample data**, including a long course title and a licence number, so
  the author sees how an awkward value actually sits rather than a tidy placeholder.
- **A duplicate starts as a draft attached to no courses.** Copying a live certificate must never
  quietly produce a second live one.
- **Activating says what it commits to**, including that certificates already issued are never
  altered by later edits. That is the question an administrator will actually have.

## 6. Still open

1. **Who signs?** The signature is a name and a job title today. If states require the trainer's
   own credential number, that is a seventh evidence field.
2. **Do certificates need versioning?** If a certificate is edited after 400 have been issued, the
   old ones stand, but there is currently no record of what they said.
3. **Bulk re-issue** after a template correction: is that ever wanted, or is it a compliance hazard?

## 7. Navigation

The certificate module was built and linked only from the course Settings hint, so the
Certifications item in the sidebar stayed inert and the screen was unreachable from the nav. Fixed:
all three built screens now cross-link.

| Nav item | Goes to |
|---|---|
| Dashboard | `index.html` |
| Courses | `course-create.html` |
| Certifications | `certificate.html` |
| Learners, Sessions, Assessments, Automations, Reports, Content library, Help | still inert |

The active item on each page keeps `href="#"`, since navigating to the page you are on is
pointless. The seven unbuilt items remain inert by design, as recorded in `UI-CHECKLIST.md` §10.

**Rule for the next module: wiring the sidebar is part of shipping a screen, not an afterthought.**
A module that cannot be reached from the nav is not finished.
