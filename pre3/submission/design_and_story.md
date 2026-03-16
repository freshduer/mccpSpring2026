# Design and Story — 3MT Slide and Non-Specialist Explanation

This document describes (a) how the one-page slide was designed and (b) how the research story is explained to a non-specialist audience. It is for assessors to understand design and storytelling choices; it is **not** a script to be read aloud.

---

## (a) Slide design

### Format and readability
- **Format:** One-page slide in **HTML** (`3mt_slide.html`) and **SVG** (`3mt_slide.svg`), both text-based and machine-readable as required.
- **Layout:** Single 16:9-style view with a clear flow: title → one central diagram → one short takeaway line.
- **Colour and contrast:** Dark gradient background with high-contrast text and three coloured blocks (red → green → blue) to show “problem → method → outcome” without jargon.

### Content on the slide
- **Title:** “When your history is too long to use … we make it count.” — states the problem and promise in everyday language.
- **Central diagram:** Three boxes with arrows:
  1. **Long past behaviours (thousands of items)** — the challenge (too much history).
  2. **LONGER: compress & focus, without losing what matters** — the idea in plain language.
  3. **Better recommendations in real apps, at scale** — the result and impact.
- **Takeaway line:** One sentence summarising the slide: from “long, noisy history” to “clear signal” for recommendations.

### Design choices
- **Minimal text:** Only a few short phrases so the audience can grasp the idea quickly while listening.
- **No technical terms on the slide:** Terms like “sequence,” “transformer,” “FLOPs,” “KV cache” are avoided; they are explained orally with metaphors if needed.
- **One clear narrative:** The slide supports a single story (problem → solution → impact) that can be told in under three minutes.

---

## (b) Explaining the research story to a non-specialist audience

### Core message in plain language
- **Aim:** Help recommendation systems use your *whole* long history (e.g. thousands of past clicks or views) in a way that is both accurate and efficient enough for real products.
- **Result:** A method called LONGER that does this end-to-end, improves recommendations, and has been used in large-scale apps (e.g. advertising and e-commerce) serving very large numbers of users.

### Strategies used (and suggested for the oral presentation)

1. **Everyday metaphor — “long bookshelf”**
   - Imagine your past behaviour as a very long bookshelf. The system cannot “read” every book every time. LONGER is like creating a smart summary and index: it compresses and focuses on what matters so the system can still use the full history effectively.

2. **Problem–solution–impact structure**
   - **Problem:** Apps want to use your long history to recommend better, but using everything in full is too costly (time, computation). Many existing approaches shorten or summarise in ways that lose important information.
   - **Solution:** LONGER keeps the long history but compresses and focuses it in a structured way (e.g. “compress & focus” on the slide), so we get both efficiency and better use of the full history.
   - **Impact:** Better recommendations in real products (e.g. ads, e-commerce), validated at very large scale.

3. **Avoiding jargon**
   - Replace technical terms with simple equivalents when speaking, for example:
     - “Long behaviour sequence” → “your long history of clicks, views, or actions”
     - “Token merge / hybrid attention” → “compressing and focusing on the most relevant parts”
     - “End-to-end modeling” → “using the full history in one coherent process”
   - The slide already avoids these terms so the audience is not overloaded.

4. **Concrete examples (for the spoken part only)**
   - E.g. “When you open an app, it has thousands of things you’ve seen or clicked. We want it to use all of that to suggest what you’ll like next — without making the system too slow or expensive. LONGER is a way to do exactly that.”

5. **Engagement**
   - Start with a hook (e.g. “Have you ever wondered how an app seems to know what you might like?”) and tie it to “using your long history wisely.”
   - Emphasise real-world impact: “used in real products that serve huge numbers of users” rather than only offline metrics.

### What this document is not
- This is **not** a script to read aloud. The actual presentation should be delivered using note cards with key points only (e.g. “bookshelf metaphor,” “problem → solution → impact,” “real apps, scale”) and spoken from understanding, in line with the assessment rules.

---

## File list in this submission

| Item | File(s) |
|------|--------|
| One-page slide (machine-readable) | `3mt_slide.html`, `3mt_slide.svg` |
| Design & story description | `design_and_story.md` (this file) |
| Audio link (to be added by you) | `audio_link.md` |

After recording your audio (max 3 minutes, no script-reading), add the link in `audio_link.md` and submit all required links in your forum reply.
