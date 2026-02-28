# Slide Plan for HTML Presentation — LONGER

**Presentation:** Oral Assessment 1 — Research Story-telling (8 minutes)  
**Article:** Chai et al. (2025). LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders. RecSys '25.

**Slides:** 9 | **Images:** Use files from `papers/longer/image/`

---

## Slide-by-slide plan

| # | Title | Key content | Visual (from folder) | Design notes |
|---|--------|-------------|----------------------|--------------|
| 1 | **Title** | Paper title; authors (ByteDance); your name & date | — | Large title; white space |
| 2 | **Opening / Hook** | One hook question; problem in one sentence | — | Plain language; max 3 lines |
| 3 | **What This Study Is About** | Goal: end-to-end 10k sequences; gap: two-stage loses info; three contributions (global tokens, token merge, hybrid attention) | **longer-v5.pdf** (model architecture) | Explain terms; 6 words/line |
| 4 | **Key Findings** | Architecture; offline +1.57% AUC; online A/B gains; scaling laws | **TokenAuc.pdf** or **TokenLoss.pdf** (length scaling); **Table 1** (offline) | One figure per slide; minimal text |
| 5 | **Scaling & Efficiency** | ~50% FLOPs cut; scaling with length/params/FLOPs | **ParamsAuc.pdf**, **FlopsAuc.pdf** | High contrast; short caption |
| 6 | **Significance** | Practical path; scaling laws; deployed at scale | Optional: **longer-v5.pdf** | 2–3 bullets |
| 7 | **Impact on My Research** | Global tokens; token merge; KV cache; mixed precision | — | 2–3 bullets |
| 8 | **Writing Strategies** | Clear problem; results tied to figures; industrial validation | — | 3–4 items |
| 9 | **Summary & Thank you** | One-line takeaway; Thank you; Q&A | — | Large font |

---

## Image files in `papers/longer/image/`

- **longer-v5.pdf** — Model architecture (use on Slide 3 or 6)
- **jaguar.pdf** — Training framework (optional)
- **kvcache.pdf** — KV cache serving (optional)
- **TokenAuc.pdf** — Scaling with sequence length (AUC)
- **TokenLoss.pdf** — Scaling with sequence length (LogLoss)
- **ParamsAuc.pdf** — Scaling with parameters
- **FlopsAuc.pdf** — Scaling with FLOPs

---

## HTML format

- Reveal.js; clean design; 2–3 colours; high contrast
- Use `<object data="papers/longer/image/xxx.pdf" type="application/pdf">` or convert PDF to PNG for `<img>` if needed
- Navigation: keyboard + click; slide number (c/t)
