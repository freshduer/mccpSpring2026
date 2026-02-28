# Presentation Outline — Research Story-telling by Experienced Writers

**Article:** Chai et al. (2025). *LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders.* RecSys '25.

**Duration:** 8 minutes | **Audience:** Non-specialist (classmates and lecturer)

---

## Opening (~1 minute)

### Content
- **Hook:** “When you scroll through Douyin or shop online, how does the system decide what to show you next? It can use your **entire history**—sometimes thousands of past actions. This paper asks: how can we use **very long histories** end-to-end without making the system slow or too expensive?”
- **Brief context:** This paper is from **recommender systems**—the technology behind “what to show next” on apps. It presents **LONGER**, a framework for **ultra-long sequence modeling** (up to 10,000 items) in industrial settings, with GPU-efficient design.
- **Transition:** “I’ll introduce what the study set out to solve, the main ideas and findings, why they matter, and how they impact my own research.”

### Presenter notes (rubric alignment)
- **Content/Structure:** One hook question + one-sentence context; then transition.
- **Delivery:** Eye contact, clear pace; pause before “I’ll introduce…”
- **Visual Aids:** Title slide; optional: paper’s model architecture figure.
- **Language:** “The pressing question we seek to answer is…”

---

## Section 1: Introduction to the Article (~1.5 minutes)

### Content
- **What the study is about (plain language):** LONGER is a **Transformer-based** framework for modeling **ultra-long user behavior sequences** (e.g. 10,000 items) in **end-to-end** fashion. It aims to capture both long- and short-term preferences without the **two-stage retrieval** (select a small subset first, then model) that many systems use—which loses information.
- **Gap/problem:** Existing approaches include two-stage retrieval (SIM, TWIN), pre-trained user embeddings, and memory-augmented models. These improve efficiency but **sacrifice full-sequence information** due to upstream–downstream inconsistency. LONGER targets **true end-to-end** modeling under industrial constraints.
- **Research objectives:** (1) Design a **GPU-efficient** long-sequence Transformer. (2) Reduce complexity via **token merge** and **hybrid attention**. (3) Provide **engineering optimizations** (mixed precision, KV cache, synchronous training) for deployment. (4) Validate **scaling laws** (performance vs. length, FLOPs, parameters).
- **Accessibility:** Say “recommender” = system that suggests next item; “sequence” = list of past actions; “end-to-end” = model sees full history directly; “token merge” = group adjacent items to shorten the sequence and cut cost.

### Presenter notes (rubric alignment)
- **Content/Structure:** One metaphor or example per technical term; keep objectives in plain language.
- **Delivery:** Pause after each sub-point; stress “three main contributions.”
- **Visual Aids:** One slide: “What this study is about” + three contributions; use **longer-v5.pdf** (model architecture).
- **Language:** “The impetus for this study stems from…”; “The pressing question we seek to answer is…”

---

## Section 2: Key Findings (~2 minutes)

### Content
- **Finding 1 — Architecture:** LONGER uses **global tokens** (e.g. target item, user ID) to stabilize attention; **token merge** with **InnerTrans** to compress sequences (~50% FLOPs reduction, nearly lossless); **hybrid attention** (cross-causal + self-causal) to balance efficiency and expressiveness.
- **Finding 2 — Offline results:** LONGER achieves **+1.57% AUC** and **−3.39% LogLoss** vs. base; **+0.21% AUC** vs. strongest baseline (Transformer). Outperforms DIN, HSTU, TWIN, SumPooling. Sampling 40% of sequence retains >95% of gains with ~50% FLOPs cut.
- **Finding 3 — Online A/B:** Douyin Ads: +1.06–2.10% ADSS, +1.17–2.15% ADVV across Live/Short Video/Mall. Douyin E-Commerce: +4.61–7.92% Order/U, +5.28–6.54% GMV/U. Deployed in dozens of ByteDance scenarios, serving billions of users.
- **Finding 4 — Scaling:** Performance scales with sequence length, FLOPs, and parameters following power-law trends (R² ≈ 0.97–0.99).

### Presenter notes (rubric alignment)
- **Content/Structure:** Use signaling: “The findings reveal that…”; “Our data indicates that…”; point to slides (tables, figures).
- **Delivery:** Slow down on numbers; use gestures for “long history” vs “short sequence.”
- **Visual Aids:** Use **TokenAuc.pdf** / **TokenLoss.pdf** (scaling with length); **ParamsAuc.pdf** / **FlopsAuc.pdf** (scaling with params/FLOPs); Table 1 (offline comparison).
- **Language:** “The findings reveal…”; “Our data indicates that…”; “The analysis demonstrates that…”

---

## Section 3: Significance of the Research (~1.5 minutes)

### Content
- **Why it matters:** LONGER shows a **practical path** to **end-to-end ultra-long sequence modeling** under real industrial constraints. You don’t have to rely only on retrieval or pre-trained embeddings; **architecture** (global tokens, token merge, hybrid attention) + **engineering** (mixed precision, KV cache, synchronous framework) together make 10k-sequence modeling **deployable** at billion-user scale.
- **Contribution to the field:** (1) **GPU-efficient** Transformer design for long sequences. (2) **Token merge + InnerTrans** reduces ~50% FLOPs with minimal accuracy loss. (3) **Scaling laws** validated in recommendation (length, FLOPs, params). (4) **Industrial deployment** across advertising and e-commerce.
- **Broader takeaway:** For large-scale recommenders, **how you design the model** (tokens, merge, attention) and **how you deploy it** (training framework, KV cache) are as important as model size. Scaling laws apply in recommendation as in LLMs.
- **Accessibility:** Link to “why your feed gets better when the system uses more of your history” and “why it doesn’t get slower.”

### Presenter notes (rubric alignment)
- **Content/Structure:** Connect to audience concerns; smooth transition from “contribution” to “broader takeaway.”
- **Visual Aids:** One slide: 2–3 bullets; optional **longer-v5.pdf** or scaling figures.
- **Language:** “This research contributes to the field by…”; “The implications of our findings suggest that…”

---

## Section 4: Impact on My Own Research (~1.5 minutes)

### Content
- **Impact on my research design:** If my work touches **recommendation** or **sequence modeling**, I can adopt: (1) **global tokens** for stabilizing attention in long contexts; (2) **token merge** with lightweight inner transformers for efficiency; (3) **hybrid attention** (cross + self) for long sequences; (4) **KV cache** for inference when scoring many candidates; (5) **mixed precision** and **recomputation** for memory efficiency.
- **Writing strategies I learned (with evidence from the article):**
  - **Clear problem and three contributions:** Intro states why ultra-long sequences matter, why two-stage/retrieval is limiting, and three separated contributions (architecture, efficiency, engineering) with their own sections.
  - **Results tied to design:** Offline table (Table 1), ablation (Table 2), scaling figures (TokenAuc, TokenLoss, ParamsAuc, FlopsAuc), online A/B tables. Each claim backed by a table or figure.
  - **Honest scope:** Focus on CVR, Douyin Ads/E-Commerce; baselines and setup clearly described; readers know what is compared.
  - **Industrial validation:** Online A/B across multiple formats; deployment at scale stated explicitly.
- **Accessibility:** Keep “impact on my research” personal; when mentioning technical terms, use one short phrase.

### Presenter notes (rubric alignment)
- **Content/Structure:** Be specific; refer to slide bullets when listing writing strategies.
- **Visual Aids:** One slide “Impact on my research” (2–3 bullets) + one slide “Writing strategies” (3–4 items with brief evidence).
- **Language:** “This study makes several key contributions, including…”; “Our findings provide new insights into…”

---

## Closing (~0.5 minutes)

### Content
- **Summary:** LONGER enables **end-to-end ultra-long sequence modeling** (up to 10k) in industrial recommenders via **global tokens**, **token merge + InnerTrans**, and **hybrid attention**, with **~50% FLOPs reduction** and **scaling-law** behavior. Deployed at ByteDance across advertising and e-commerce, serving billions of users.
- **Thank you & Q&A:** “To sum up… / In conclusion…”; thank the audience; invite questions.

### Presenter notes (rubric alignment)
- **Content/Structure:** Concluding phrases; one-line takeaway.
- **Delivery:** Eye contact; steady pace; short pause after “Thank you” before Q&A.
- **Visual Aids:** One slide: one-line takeaway + “Thank you / Q&A.”
- **Language:** “To sum up…”; “In conclusion…”; “Thank you for your attention. I’d be glad to answer any questions.”
