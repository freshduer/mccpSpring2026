# Writing Feedback — YU Wenjun (俞文軍)

## Feedback on YU Wenjun's First Draft: Introduction and Literature Review

**Student:** YU Wenjun (俞文軍)
**Topic:** Near-Real-Time Parameter Synchronization for Deep Learning Recommendation Models (DLRMs)
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** writing/writingSampleCollection/firstDraft.md (branch: work2)
**Your reflection:** writing/writingSampleCollection/reflection.md (branch: work2)
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

This is a strong draft that demonstrates clear command of academic writing structure and deep understanding of the DLRM systems research landscape. Your Introduction follows the three-move structure effectively: Move 1 establishes the territory with concrete scale figures (50% training cycles, 60% inference at Meta), Move 2 identifies the bandwidth bottleneck with specific numbers (26 minutes for 10% of 200TB), and Move 2's second paragraph pivots elegantly to two overlooked opportunities (CPU underutilization, low-rank structure). The writing is confident, well-paced, and technically precise. The main areas for improvement are: (1) Move 3 is marked as "..." and needs to be completed; (2) the Literature Review section is missing entirely; (3) while the arguments are strong, citations are absent — every quantitative claim needs a reference; and (4) ensure that any AI-assisted passages are substantially revised so the final text reflects your own academic voice.

**Estimated current level:** Good to Excellent (8–9 range) — The structure, argument quality, and technical depth are impressive. Completing the missing sections and adding citations will push this to Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- **Move 1 is excellent.** Three well-structured paragraphs establish the territory progressively: (1) what DLRMs are and their scale, (2) the decoupled architecture and its synchronization challenge, (3) why freshness matters with business impact. Each paragraph has a clear purpose.
- **Concrete quantification throughout.** "50% of training cycles," "60% of inference resources," "26 minutes," "0.1% accuracy drop → millions in lost revenue," "peak utilization only 20%," "80% of variance in 5% of principal components" — these numbers make the argument vivid and credible.
- **Move 2's pivot is well-crafted.** The transition from "these approaches are fundamentally limited by the training-inference decoupled architecture" to "we identify two overlooked opportunities" is a strong rhetorical move. You name the two opportunities (CPU underutilization, low-rank structure) and show exactly how they enable your paradigm shift.
- **The "paradigm shift" framing is effective.** Saying your approach "eliminates inter-cluster synchronization entirely" is a bold and clear contribution statement.

### Issue 1: All Quantitative Claims Need Citations

Despite the strong use of numbers, not a single citation appears in the draft. This is the most critical gap. Every specific number needs a reference:

- "DLRMs consume over 50% of training cycles and 60% of inference resources" — which Meta/industry paper?
- "syncing just 10% of a 200TB EMT over 100GbE networks takes over 26 minutes" — from which systems measurement?
- "even a 0.1% accuracy drop can translate to millions in lost revenue" — which industry report?
- "peak utilization reaching only 20%" — from which production trace analysis?
- "over 80% of parameter update variance can be captured by less than 5% of principal components" — which empirical study?

**Action:** Add LaTeX citations to every factual claim. Each paragraph should have 3–5 citations. Readers need to verify these numbers, and reviewers will specifically challenge uncited claims.

### Issue 2: Move 3 Is Incomplete

Move 3 shows only "..." — this is where you state your specific contribution. Based on your Move 2, a strong Move 3 would be:

**Suggested Move 3:** "In this paper, we propose [algorithm name], a near-real-time parameter synchronization framework that co-locates lightweight incremental training within inference clusters. Our approach makes three contributions: (1) we design an in-cluster training architecture that leverages idle inference CPUs to compute embedding updates locally, eliminating cross-cluster synchronization; (2) we develop an adaptive low-rank decomposition scheme that dynamically adjusts approximation rank based on update complexity, capturing [X]% of update information with [Y]% parameter reduction; and (3) we introduce a performance isolation mechanism that bounds the interference between co-located training and inference workloads to within [Z]% latency overhead. Experiments on production-scale DLRM workloads demonstrate that [algorithm name] achieves [X]-second update freshness — a [Y]× improvement over state-of-the-art delta synchronization — while maintaining recommendation accuracy within [Z]% of full-sync baselines."

### Issue 3: Consider the Reader's Background

Your draft assumes familiarity with DLRM architecture (embedding tables, training-inference decoupling, parameter servers). While this is appropriate for a systems conference audience, adding one sentence explaining what embedding tables store and why they are so large would help readers from neighboring fields.

### Issue 4: Ensure AI-Assisted Text Is Substantially Revised

You are encouraged to use AI tools throughout your writing process. However, AI-generated text cannot be submitted directly — it must be substantially revised and rewritten in your own voice. Some phrases in your draft have a slightly formulaic quality: "Their operational scale is staggering," "This resource footprint stems from," "creating unprecedented systems challenges." When using AI to help draft or polish, make sure you revise the output so it sounds like you, not like a template. Vary your sentence openings and use more direct language where appropriate.

---

## Part 2: Literature Review Feedback

### Status: Not Yet Written

Your draft does not include a Literature Review section. Based on your Introduction, the Literature Review should cover:

1. **DLRM Architecture and Scale** — Survey papers on DLRM architectures (DLRM paper, Deep & Cross, etc.) and industrial deployment reports
2. **Parameter Synchronization Methods** — Delta-based, prioritization-based, and other approaches you critique in Move 2
3. **Low-Rank Approximation for Embeddings** — Methods that exploit low-rank structure in neural network parameters
4. **Training-Inference Co-location** — Any existing work on co-located training, including edge/federated approaches
5. **Performance Isolation** — How existing systems manage resource contention between co-located workloads

**Structure suggestion:** Organize into 3–4 thematic subsections, each with:
- Move 1: What this line of work addresses
- Move 2: Critical analysis of key papers (not just description — evaluate assumptions, limitations, and tradeoffs)
- Connect each subsection to your contribution

---

## Part 3: Reflection Feedback

### What Works Well

Your reflection is thoughtful and shows strong self-awareness:

- **"I follow a problem–limitation–opportunity structure commonly used in systems papers"** — this is exactly what your Introduction does, and it works well
- **Honest about AI usage:** "AI is helpful for language polishing but requires careful checking for technical accuracy" — this shows maturity
- **Clear improvement goals:** gap identification, synthesis, and academic expression are exactly the right areas to focus on

### Issue 5: Your Self-Identified Concern Is Valid

You note: "I sometimes worry that my introduction doesn't sufficiently motivate the problem for readers outside my specific research area." This concern is valid. Your Move 1 effectively motivates the problem for systems researchers, but a reader from ML/NLP might not immediately grasp why parameter freshness matters so much. Consider adding one sentence connecting stale parameters to user-facing impact (e.g., "Users see irrelevant recommendations during the staleness window, directly reducing click-through rates and session duration").

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Add citations to every quantitative claim (every paragraph needs 3–5) | Makes claims verifiable and credible |
| 🔴 High | Complete Move 3 with specific contributions and result preview | Tells readers what the paper delivers |
| 🔴 High | Write the Literature Review section | Completes the required structure |
| 🟡 Medium | Add one sentence of background on EMTs for non-specialist readers | Improves accessibility |
| 🟡 Medium | Substantially revise any AI-assisted passages in your own voice | Meets submission requirements |
| 🟢 Lower | Add user-facing impact connection in Move 1 | Broadens motivation appeal |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Complete Move 3 with numbered contributions
3. Write the Literature Review (recommend 600–800 words covering 3–4 themes)
4. Add citations throughout
5. Submit by **15 March 2026** via Moodle forum and Turnitin
