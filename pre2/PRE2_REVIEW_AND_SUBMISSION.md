# Pre2 review and submission guide

## 1. Pre2 folder structure

### 1.1 pre2/demo — design and guidelines

| Content | Path | Purpose |
|---------|------|---------|
| Poster design inspiration | `demo/posterInspire.md` | Design ideas and references |
| Institutional guidelines | `demo/institutionalGuidelines/math.md` | HKBU Math poster rules (A0, logo, fonts, layman's summary, etc.) |
| GitHub inspiration | `demo/getGitHubinspiration.md` | Ideas from GitHub |
| **posterScripts** | `demo/posterScripts/` | Templates and export tools |

**posterScripts overview:**

- **Root:** `export-poster.html` (browser html2canvas export to PNG), `poster-template.html` (minimal HTML template), `export-node.js` (Puppeteer high-quality export)
- **Subfolders:** INSIGHTS and reusable files from 5 repos (betterposter-latex, betterposter-portrait, html-poster, canvas-poster, tex-scientific)
- **Quick export:** Open `export-poster.html` in a browser and click “Export PNG”, or run `npm install puppeteer` then `node export-node.js`

### 1.2 pre2/sample — full example

| File | Purpose |
|------|---------|
| `samplePoster.html` | Sample poster HTML (A0 portrait, sections, layman's summary, figure placeholders) |
| `sampleProcess.md` | Process and **alignment with course/institutional requirements** (MCCP6020 + HKBU Math) |
| `outlineScript.md` | Outline + script for 2–3 min presentation + possible Q&A answers + timing checklist |

Use these to understand **structure, layout, fonts, section order, and how they map to assessment criteria**.

### 1.3 pre2/materials — course materials

- `Presentation_2_Brief.md`: assignment (poster design, 2–3 min presentation, Q&A, submission)
- `pre2AssessmentRubrics.md`: assessment criteria and rubrics
- Other session handouts

---

## 2. Requirements you must meet (summary)

### MCCP6020 (course)

- Poster: research topic, objectives, methods, hypotheses, key/preliminary/anticipated findings, conclusions; **A1 or A3** (A4 not acceptable); clear headings, bullets, visuals; readable font size.
- Presentation: 2–3 minutes with the poster as visual aid, then Q&A; address both specialist and non-specialist audiences.

### HKBU Department of Mathematics (if applicable)

- Size: A0 portrait 841×1189 mm; PDF 600 dpi, <25 MB.
- Header: HKBU logo (top left), Department of Mathematics (top right); title, presenter, Principal Supervisor centred.
- Sections: Introduction, Methodology, Results, Discussion/Conclusion, References; include **Layman's summary**.
- Fonts: titles/headings sans-serif ≥100 pt (measure in final PDF); body serif ≥24 pt (≥30 pt recommended); sentence case; avoid ALL CAPS.
- Balance: text 50–60%, visuals 40–50%; figures/tables minimum ~216×280 mm.

Use the alignment table in `sampleProcess.md` to check your poster against these requirements.

---

## 3. Recommended workflow

1. **Draft the poster in HTML**  
   Start from `sample/samplePoster.html` or `demo/posterScripts/poster-template.html` / `html-poster/poster-basic.html`, then adapt content and layout to your research.
2. **Write outline and script**  
   In Markdown, write a 2–3 minute outline and script (see `sample/outlineScript.md`).
3. **Iterate with AI**  
   In Cursor or similar tools, revise the HTML and MD based on feedback until they meet course and institutional requirements.
4. **Check alignment**  
   Use the same style of alignment as in `sampleProcess.md` (or your own process doc) to confirm the poster meets MCCP6020 and institutional rules.
5. **Prepare Q&A**  
   List likely questions and short answers in `outlineScript.md` or a separate Q&A.md (see sample “Possible Q&A”).
6. **Submit to the forum**  
   In your Moodle forum reply, provide the links described under “How to submit” below.

---

## 4. How to submit (forum reply)

Include the following in your forum reply:

| Item | Description and example |
|------|-------------------------|
| **Poster link** | e.g. GitHub Pages URL for the poster, or the repo link to the HTML (e.g. `https://github.com/[your-username]/mccpSpring2026/blob/main/pre2/posterSubmission/poster.html`). With GitHub Pages: `https://[your-username].github.io/mccpSpring2026/pre2/posterSubmission/poster.html` |
| **Audio link** | URL of your 2–3 minute recording (e.g. GitHub raw link or other host). You can put the URL in `pre2/posterSubmission/audio_link.md` and submit either that file’s link or the audio URL directly. |
| **Q&A .md link** | GitHub link to your Q&A file (e.g. `Q&A.md`), raw or repo view. |
| **(Optional) Folder path** | e.g. `https://github.com/[your-username]/mccpSpring2026/tree/main/pre2/posterSubmission` so the lecturer can open all submission files at once. Ensure the folder is accessible. |

---

## 5. Submission folder in this repo

Under `pre2/posterSubmission/` you have:

- **poster.html** — Your poster HTML (or use your own filename and give the correct link in the forum).
- **audio_link.md** — Put your **audio file URL** (or where it is hosted) here.
- **Q&A.md** — Your Q&A with possible questions and short answers.

Do the following: place your poster HTML in this folder (or replace the placeholder), record and host your audio and add the link in `audio_link.md`, complete `Q&A.md`, then post the required links in your forum reply.

---

**References:** `sample/sampleProcess.md`, `sample/outlineScript.md`, `demo/institutionalGuidelines/math.md`, `materials/Presentation_2_Brief.md`, `materials/pre2AssessmentRubrics.md`.
