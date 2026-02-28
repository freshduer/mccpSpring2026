# Presentation Outline (Revised) — LONGER

**Article:** Chai et al. (2025). *LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders.* RecSys '25.

**Duration:** 8 minutes | **Audience:** Non-specialist | **Slides:** 9

---

## Opening (~1 min)
Hook: How does the app decide what to show next? Can we use very long histories end-to-end without slowing down?  
Context: Recommender systems; LONGER = GPU-efficient Transformer for 10k sequences.  
Transition: I’ll introduce the problem, main ideas, findings, significance, and impact on my research.

---

## Section 1: Introduction (~1.5 min)
**What:** LONGER = end-to-end ultra-long sequence modeling (up to 10k) in industrial recommenders.  
**Gap:** Two-stage retrieval (SIM, TWIN), pre-trained embeddings, memory models—all sacrifice full-sequence info.  
**Contributions:** (1) Global tokens + token merge + InnerTrans (~50% FLOPs cut). (2) Hybrid attention (cross + self). (3) Engineering: mixed precision, KV cache, synchronous training.  
**Visual:** longer-v5.pdf (model architecture).

---

## Section 2: Key Findings (~2 min)
- **Architecture:** Global tokens stabilize attention; token merge + InnerTrans compress sequence; hybrid attention balances efficiency and expressiveness.
- **Offline:** +1.57% AUC, −3.39% LogLoss vs base; +0.21% vs Transformer. 40% sequence sampling keeps >95% gains with ~50% FLOPs.
- **Online A/B:** Douyin Ads +1–2% ADSS/ADVV; E-Commerce +4–8% Order/U, GMV/U. Deployed in dozens of scenarios, billions of users.
- **Scaling:** Power-law with length, FLOPs, params (R² ≈ 0.97–0.99).  
**Visual:** TokenAuc.pdf, TokenLoss.pdf; Table 1; ParamsAuc.pdf, FlopsAuc.pdf.

---

## Section 3: Significance (~1.5 min)
Practical path to end-to-end 10k modeling; scaling laws in recommendation; deployed at ByteDance.  
**Visual:** 2–3 bullets; optional longer-v5.pdf.

---

## Section 4: Impact on My Research (~1.5 min)
Adopt: global tokens; token merge + InnerTrans; hybrid attention; KV cache; mixed precision.  
**Writing strategies:** Clear problem + three contributions; results tied to tables/figures; honest scope; industrial validation.  
**Visual:** 2–3 bullets impact; 3–4 items writing strategies.

---

## Closing (~0.5 min)
Summary: LONGER enables 10k end-to-end with ~50% FLOPs cut; scaling laws; deployed at scale.  
Thank you; Q&A.

---

## Mapping to 9 Slides

| Slide | Section |
|-------|---------|
| 1 | Title |
| 2 | Opening |
| 3 | Introduction + longer-v5.pdf |
| 4 | Key findings + TokenAuc/TokenLoss or Table |
| 5 | Scaling (ParamsAuc, FlopsAuc) |
| 6 | Significance |
| 7 | Impact on my research |
| 8 | Writing strategies |
| 9 | Summary & Thank you |
