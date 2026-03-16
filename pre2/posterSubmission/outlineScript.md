# Outline and script for LONGER poster presentation (2–3 minutes)

Use this outline and script for the oral presentation that accompanies the poster, then take questions.

---

## Presentation outline

1. **Opening (15–20 s)**  
   Title + one-sentence takeaway: what LONGER is, what problem it addresses, and the main result.

2. **Problem and gap (25–30 s)**  
   Why ultra-long behavior sequences matter; limitations of current practice (two-stage retrieval, pre-trained user embeddings, memory-augmented)—inconsistency or indirect modeling.

3. **What we did (40–50 s)**  
   LONGER in three parts: global tokens; token merge + InnerTrans + hybrid attention (~50% FLOPs reduction); engineering (mixed precision, KV cache, synchronous training/serving). Point to the architecture and training/KV figures on the poster.

4. **Result in one line (15–20 s)**  
   Offline: better AUC/LogLoss than strong baselines; online A/B: gains in ads and e-commerce; deployed at scale.

5. **Closing (10–15 s)**  
   Summary + thank you + invite questions.

---

## Script (approx. 2 min 30 s)

**Opening**  
“Hi. I’m going to walk you through **LONGER**—a method for **ultra-long sequence modeling** in industrial recommenders. In one sentence: we model ultra-long user behavior **end-to-end**, cut computation by about half, and have validated and deployed it across many scenarios at ByteDance for billions of users.”

**Problem and gap**  
“In recommendation, ultra-long behavior sequences capture both long- and short-term preferences. Current industry practice relies on **two-stage retrieval** (e.g. SIM, TWIN), **pre-trained user representations**, or **memory-augmented** models. These either introduce upstream–downstream inconsistency or only use the raw long sequence indirectly, so they don’t do true end-to-end modeling. We want end-to-end ultra-long sequence modeling while staying GPU-efficient.”

**What we did**  
“We propose **LONGER**: Long-sequence Optimized traNsformer for GPU-Efficient Recommenders. First, **global tokens**—e.g. target item, user ID—anchor the sequence and stabilize attention over long contexts. Second, **token merge** groups adjacent tokens and optionally adds lightweight **InnerTrans** inside each group, keeping local interactions while cutting FLOPs by about 50%. Third, **hybrid attention**: the first layer uses cross-causal attention with query = global tokens plus the most recent k behaviors; later layers use self-causal attention. That allows **KV cache** at inference: we compute the user sequence once and reuse it across candidates. We also use mixed precision, activation recomputation, and a fully synchronous GPU training and serving framework. The architecture and training/KV figures on the poster show these components.”

**Result**  
“On Douyin Ads CVR offline, LONGER beats strong baselines on AUC and LogLoss—about +1.57% AUC and −3.39% LogLoss vs base, and better than Transformer with less compute. Online A/B shows steady gains in both ads and e-commerce. LONGER is now deployed in dozens of scenarios at ByteDance, serving billions of users.”

**Closing**  
“So in summary: LONGER achieves end-to-end ultra-long sequence modeling through structure and engineering, validated in production. I’m happy to take questions on the method, experiments, or deployment. Thank you.”

---

## Possible Q&A — short answers

- **How does LONGER differ from two-stage retrieval (e.g. SIM/TWIN)?**  
  Two-stage retrieves then models a short list, with upstream–downstream mismatch; LONGER models the full ultra-long sequence end-to-end (e.g. 10k steps) and compresses/accelerates inside the model with token merge and hybrid attention.

- **Does token merge lose information?**  
  Grouping shortens the sequence, so some fine-grained detail is reduced; we add InnerTrans inside each group to keep local interactions. In experiments, ~50% FLOPs reduction is almost lossless in performance.

- **Why is “recent k” good in hybrid attention?**  
  Recent behavior is more relevant to the current prediction; we found that using recent 100 matches performance of using the full sequence at about half the compute, so we use recent k as the query sampling strategy.

- **How is KV cache used?**  
  When the user sequence is fixed and only the candidate changes, we compute and cache key/value for the sequence once; each candidate only pays for attention between its global token and the cached sequence. That cuts redundant computation and reduces online throughput degradation from about −40% to about −6.8%.

- **One sentence for a non-specialist:**  
  “We help recommenders use long behavior history more efficiently—with less compute and lower latency—and show gains in both ads and e-commerce.”

---

## Timing checklist

- [ ] Rehearse with a timer; stay within 2–3 minutes.
- [ ] Point at the poster: title, Layman’s summary, architecture figure, training/KV figures, results table and curves.
- [ ] Prepare 2–3 backup answers for “if they ask about X” (e.g. token merge, KV cache, online metrics).
- [ ] Practise one sentence each for: problem, gap, contribution, result, impact.
