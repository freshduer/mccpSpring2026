# Q&A preparation — LONGER poster presentation

Short answers for the Q&A after the poster, based on the paper and poster content.

---

## 1. Method and concepts

### Q: How does LONGER differ from two-stage retrieval (SIM, TWIN)?
**A:** Two-stage first retrieves top-k items from the ultra-long sequence then models that short list, which creates upstream–downstream inconsistency. LONGER models the full ultra-long sequence (e.g. 10k steps) end-to-end and uses token merge and hybrid attention inside the model for compression and speed, without a separate retrieval module.

### Q: What is token merge? Does it lose information?
**A:** Token merge groups K adjacent tokens into one, shortening the sequence and reducing FLOPs. We add **InnerTrans** inside each group—a lightweight transformer—to preserve local interactions. In experiments, ~50% FLOPs reduction comes with almost no loss in AUC/LogLoss.

### Q: What do global tokens do?
**A:** They include target item, user ID, CLS, etc., and act as global anchors: (1) they strengthen interaction between user history, context, and candidate; (2) they stabilize attention over long sequences and mitigate the “attention sink” effect (deeper layers over-attending to early tokens).

### Q: How is hybrid attention designed?
**A:** The first layer uses **cross-causal attention**: query = global tokens + recent k tokens sampled from the full sequence; key/value = full sequence. Later layers use **self-causal attention** on the compressed tokens for higher-order interaction. This design both reduces compute and enables KV cache (user sequence computed once).

---

## 2. Experiments and results

### Q: Offline experimental setup?
**A:** Douyin Ads CVR task, ~5.2B samples over 130 days; first 123 days for training, last 7 for evaluation. Baselines include Base, SumPooling, TWIN, DIN(Recent50), DIN, HSTU, Transformer. LONGER reaches the best AUC (0.85290) and lowest LogLoss (0.47103), about +1.57% AUC and −3.39% LogLoss vs base.

### Q: Online A/B results?
**A:** Ads (ADSS/ADVV): about 1–2% gains in Live, Short Video, Mall. E-commerce (Order/U, GMV/U): Live about +7.9% Order/U, +6.5% GMV/U; Short Video about +4.6%, +5.3%. Baselines were already strong, so these gains are meaningful in practice.

### Q: What do the scaling experiments show?
**A:** Sequence length, FLOPs, and parameters follow power-law relationships with AUC/LogLoss; longer sequences and appropriate depth improve performance, with diminishing returns at greater depth. This shows LONGER’s scaling behavior is clear and predictable under industrial constraints.

---

## 3. Engineering and deployment

### Q: How is KV cache used? What’s the effect?
**A:** When the user sequence is fixed, we compute and cache its key/value once; each candidate only pays for attention between its global token and the cached sequence. That avoids recomputing the full sequence per candidate. Online throughput degradation drops from about −40% to about −6.8%.

### Q: What’s special about the training framework?
**A:** It’s fully synchronous, with both dense and sparse parameters stored and updated on GPU—no separate parameter server. Sparse embeddings are tiered by access frequency (HBM / CPU / SSD), matching recommendation feature patterns and improving throughput and convergence.

### Q: Mixed precision and recompute?
**A:** We use BF16/FP16 mixed precision and activation recomputation to cut memory and compute while keeping accuracy. The paper reports about +18% throughput, −16% training time, −18% memory (up to −28% in some dense layers).

---

## 4. For a non-specialist audience

### Q: One-sentence explanation of LONGER for a non-specialist?
**A:** “We let recommenders use long user behavior history end-to-end—with about half the compute and controlled latency—and show clear gains in both ads and e-commerce, with deployment across dozens of scenarios and billions of users.”

---

(During the Q&A, use eye contact and body language, and keep explanations clear for both specialist and non-specialist listeners.)
