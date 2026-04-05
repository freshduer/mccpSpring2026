# Outline and script for LONGER poster presentation

Use the **2-minute** block below for a timed pitch; the longer script is optional if the session allows 2.5–3 minutes.

---

## 2-minute presentation (use this for a strict 2:00 cap)

**Target:** ~260 spoken words + pauses ≈ 2:00. Rehearse with a phone timer; if you run long, drop the sentence marked *(optional)*.

### Timing map

| Time | Block | What to point at on the poster |
|------|--------|--------------------------------|
| 0:00–0:20 | Hook + title | Title, Layman’s summary |
| 0:20–0:45 | Problem / gap | Introduction (two-stage vs end-to-end) |
| 0:45–1:25 | Method (3 beats) | Figure 1: global tokens → merge + InnerTrans → hybrid attention; training + KV figures |
| 1:25–1:50 | Results + impact | Results table; *(optional)* one online range |
| 1:50–2:00 | Close | Discussion one-liner; “Questions?” |

### Script (~2 minutes)

**0:00 — Opening**  
“Hi — I’ll present **LONGER**: scaling **long-sequence modeling** for industrial recommenders. In one line: we model up to **ten thousand** behavior steps **end-to-end**, cut FLOPs by about **half**, and ship it at ByteDance scale.”

**0:20 — Problem**  
“Long histories capture both long- and short-term preferences. Common practice uses **two-stage retrieval** like SIM or TWIN, or indirect signals — that creates **mismatch** or **indirect** use of the raw sequence. We want **end-to-end** long-sequence modeling that stays **GPU-efficient**.”

**0:45 — Method**  
“**LONGER** uses three ideas. **Global tokens** — target item, user ID — **anchor** attention on long contexts. **Token merge** with **InnerTrans** inside groups keeps local interactions while shortening the sequence — about **fifty percent** fewer FLOPs. **Hybrid attention**: the first layer crosses globals and **recent** behavior with the full history; later layers are self-attention on the compressed sequence. That enables **KV cache**: compute the user once, **reuse** across candidates — the poster shows throughput much better than without cache.” *(optional)* “We also use mixed precision and synchronous GPU training and serving.”

**1:25 — Results**  
“Offline on Douyin Ads CVR, LONGER reaches the best **AUC** and **LogLoss** in our table — about **plus one point six percent** AUC versus the base. **Online A/B** shows gains in ads and e-commerce.” *(optional)* “For example, e-commerce live streams see strong lifts on order and GMV per user.”

**1:50 — Close**  
“So: **structure plus systems** make ultra-long sequences practical in production. Happy to take questions — thanks.”

### One-page cheat sheet (read before you go on)

- **One sentence:** End-to-end 10k-length transformer for recommenders; ~50% FLOPs; deployed at scale.
- **Three method keywords:** global tokens; token merge + InnerTrans; hybrid attention + KV cache.
- **Two numbers:** offline +1.57% AUC vs base (poster table); KV figure −40% → −6.8% degradation.

---

## Presentation outline (2.5–3 minutes)

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

- [ ] Rehearse with a timer: **2:00** (use the 2-minute script above) or **2:30–3:00** (longer script).
- [ ] Point at the poster: title, Layman’s summary, architecture figure, training/KV figures, results table and curves.
- [ ] Prepare 2–3 backup answers for “if they ask about X” (e.g. token merge, KV cache, online metrics); see `anticipated_QA.md`.
- [ ] Practise one sentence each for: problem, gap, contribution, result, impact.
