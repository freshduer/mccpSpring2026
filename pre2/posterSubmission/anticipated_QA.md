# Anticipated Q&A — LONGER poster

Anticipated questions after the poster presentation, with short replies in bullet points. Aligns with `poster.html`; use with `outlineScript.md` for the oral pitch.

---

## Motivation & positioning

**Q: Why care about ultra-long sequences in recommenders?**

- Ultra-long behavior captures both long-term interests and short-term intent in one signal.
- Industrial traffic has enough data to justify modeling thousands of steps if compute allows.
- Goal: end-to-end use of that history, not a separate retrieval shortcut that misaligns with the ranking model.

**Q: How is LONGER different from SIM / TWIN and similar two-stage designs?**

- Two-stage: retrieve top-k from the long history, then score a short list → upstream retrieval and downstream ranker are not jointly optimized.
- LONGER: one model over the full sequence (e.g. up to 10k steps), with in-model compression (token merge, hybrid attention) instead of a separate retrieval stage.
- Emphasis: consistency and direct modeling of the raw long sequence under GPU constraints.

**Q: What about pre-trained user embeddings or memory-augmented models?**

- Pre-trained or memory-based approaches often use the long history indirectly or through a compressed state.
- LONGER targets explicit end-to-end sequence modeling with transformer-style attention, plus system tricks (KV cache, mixed precision) for production.

---

## Method: global tokens, merge, attention

**Q: What are global tokens for?**

- Typically: target (candidate) item, user ID, CLS-like slots.
- They anchor attention over very long sequences and tie history to the current prediction task.
- They help stabilize attention (reduce pathologies like over-attending to early positions in deep layers).

**Q: Explain token merge and InnerTrans in one minute.**

- Adjacent tokens are merged in groups (factor K) → shorter sequence → fewer FLOPs (~50% reduction in the paper’s setup).
- InnerTrans: a lightweight transformer **within** each merged group to keep local interactions before/after merging.
- Trade-off: coarser timeline vs. huge compute savings; ablations on the poster support the chosen design.

**Q: What is hybrid attention, and why not full self-attention everywhere?**

- First layer: **cross-causal** — queries from global tokens + sampled **recent k** positions; keys/values from the (possibly merged) full sequence.
- Later layers: **self-causal** attention on the compressed tokens for higher-order mixing.
- Benefits: lower cost than dense full attention on 10k tokens; enables serving patterns where the user side is computed once (see KV cache).

**Q: Why “recent k” (e.g. k = 100) in the first layer?**

- Recent actions are usually most predictive for the next click/conversion.
- Poster / paper: using recent k matches full-sequence quality at roughly half the compute — good operational trade-off.

**Q: Does token merge lose information?**

- Some fine-grained ordering within a group is collapsed.
- Mitigation: InnerTrans preserves intra-group structure; offline metrics show strong accuracy despite ~50% FLOPs cut.
- If pushed: report ablation lines (TokenMerge + InnerTrans, “recent k” selection) from your poster.

---

## Engineering, training, and serving

**Q: What does KV cache do here, and what was the measured impact?**

- User sequence is fixed for many candidate items; compute K/V for that sequence once, reuse for each candidate’s global query.
- Poster figure: throughput degradation improves from about **−40%** to **−6.8%** vs. no cache (numbers as on poster).
- Critical for industrial latency when scoring many ads/items per user.

**Q: What is special about the training stack (e.g. synchronous GPU, dense + sparse)?**

- Fully synchronous training/serving story — no separate slow parameter server path for the main loop.
- Dense + sparse parameters on GPU; sparse embeddings tiered (e.g. HBM / CPU / SSD) by access frequency — matches recommender feature skew.

**Q: Mixed precision and activation recomputation?**

- BF16/FP16 mixed precision and activation recomputation to save memory and time.
- Paper-level numbers (if asked): ~+18% throughput, ~−16% training time, ~−18% memory (use exact figures from paper if presenting formally).

---

## Results & experiments

**Q: What is the offline setup and main numbers on the poster?**

- Douyin Ads **CVR**, ~**5.2B** samples; metrics **AUC** and **LogLoss**.
- LONGER: **AUC 0.85290**, **LogLoss 0.47103** vs. base **0.83968 / 0.48758** → about **+1.57%** relative AUC, **−3.39%** relative LogLoss.
- vs. Transformer baseline: **+0.21%** AUC with lower FLOPs (stronger efficiency–accuracy point).

**Q: What does the scaling / power-law discussion mean?**

- AUC and LogLoss improve predictably with sequence length, FLOPs, and model size — under the tested regime.
- Useful message: longer sequences and sufficient depth help until diminishing returns; supports capacity planning.

**Q: Online A/B — what should I say without over-claiming?**

- Ads (ADSS/ADVV): about **+1.06%–2.10%** across Live / Short Video / Mall (metrics as on poster).
- E-commerce (Order/U, GMV/U): Live about **+4.6%–7.9%**; Short Video about **+4.6%–5.3%** — ranges as printed; base systems are already strong, so relative lifts are meaningful.

**Q: Where is it deployed?**

- Dozens of scenarios at **ByteDance**; **billions** of users; ads and e-commerce — as stated on the poster (RecSys 2025 industrial track narrative).

---

## Limitations & future work

**Q: Limitations of LONGER?**

- Token merge trades temporal resolution for cost; may hurt tasks where sub-group order matters sharply.
- Very long sequences still stress memory and serving; engineering stack is part of the contribution, not “model only.”
- Domain: results are from ByteDance-style ads/e-commerce; generalization to other domains needs validation.

**Q: Future work (from poster)?**

- More efficient sequence modeling (push length/cost frontier further).
- Cross-domain behavior modeling (unify signals across surfaces or accounts).

---

## Elevator / non-specialist

**Q: One sentence for someone outside ML?**

- We let recommendation models use very long user histories in one end-to-end model, cut compute by about half versus naive long transformers, and show better offline metrics and positive online A/B in ads and e-commerce at large scale.

**Q: What is the single headline result?**

- End-to-end **10k**-length modeling, **~50%** FLOPs reduction vs. full attention-style baselines, strong offline metrics, positive online lifts, production deployment.

---

## Quick reference (numbers on poster)

| Item | Value |
|------|--------|
| Sequence length (target) | up to **10,000** steps (end-to-end) |
| FLOPs reduction | ~**50%** (token merge + hybrid design) |
| Offline AUC (LONGER) | **0.85290** |
| Offline LogLoss (LONGER) | **0.47103** |
| KV cache throughput | degradation **−40% → −6.8%** (as on figure caption) |
| Citation | Chai et al., **RecSys 2025** |

---

*Tip during Q&A: point to Figure 1 (architecture), training + KV figures, and the results table when answering method and metrics questions.*
