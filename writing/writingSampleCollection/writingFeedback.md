# Writing Feedback — YU Wenjun (俞文軍)

## Feedback on YU Wenjun's First Draft: Introduction and Literature Review

**Student:** YU Wenjun (俞文軍)
**Topic:** Near-Real-Time Parameter Synchronization for Deep Learning Recommendation Models (DLRMs)
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** writing/writingSampleCollection/firstDraft.md
**Your reflection:** writing/writingSampleCollection/reflection.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

Your draft demonstrates strong systems research thinking and clear engagement with an industrially relevant problem (DLRM parameter synchronization). You have a well-defined research topic, and your Literature Review shows genuine understanding of the architectural challenges in recommendation systems at scale. The draft has several notable strengths: clear move structure, substantive gap identification (five specific gaps in Move 3), and a strong concluding paragraph that explicitly connects the literature to your proposed approach. The main areas for improvement are: (1) the Introduction needs more citations — several key claims are unsupported; (2) the Literature Review's Move 2 is descriptive rather than critically analytical; and (3) the writing could benefit from tighter synthesis across the different subsections.

**Estimated current level:** Good (7–8 range) — The structure and analytical quality are strong, with clear moves and a genuine research gap. Adding citations, deepening critical analysis, and synthesizing across sources will push this to Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- **Move 1 effectively establishes the territory.** You clearly explain why DLRMs matter (trillion-parameter models, industrial deployment at Meta/Google/ByteDance scale) and why embedding tables are the core challenge
- **Move 2 identifies a genuine, specific gap.** The gap between training-side optimization and inference-side staleness is well-framed and industrially relevant
- **Move 3 clearly states your research direction.** The shift from "inter-cluster synchronization" to "intra-cluster co-location" is a compelling research pivot

### Issue 1: Citations Are Sparse in the Introduction

Your Introduction makes several strong claims about industrial DLRM deployments without citations:

**Your sentence (no citation):** "Modern DLRMs deployed at Meta, Google, and ByteDance have evolved from relatively simple shallow architectures into trillion-parameter systems"

This needs citations. Which Meta/Google/ByteDance papers describe these systems? (e.g., DLRM paper from Naumov et al., Deep & Cross Network from Wang et al., etc.)

**Your sentence (no citation):** "A single recommendation query may require accessing thousands of sparse features across multiple embedding tables"

Which system measurement demonstrates this? Production system papers from industry labs often include these numbers.

**Action:** Add citations to every factual claim in the Introduction. As a guide, each paragraph should have 3–5 citations.

### Issue 2: Move 2 Could Frame the Gap More Sharply

Your Move 2 identifies the synchronization latency problem well but could be more explicit about why existing solutions fail:

**Stronger framing:** "Current approaches to parameter synchronization — including [full sync approach, citation], [delta-based updates, citation], and [periodic batch updates, citation] — all operate within the training-inference decoupled paradigm. As a result, they are fundamentally bounded by inter-cluster network bandwidth, achieving update freshness on the order of minutes rather than seconds. For applications such as real-time bidding and live content ranking, this staleness directly translates to [quantified business impact, if available]."

### Issue 3: Move 3 Preview Could Be More Specific

Your Move 3 mentions "co-locating lightweight training within inference clusters" but could preview specific technical contributions:

**Suggestion:** "Specifically, this work makes three contributions: (1) we propose an in-cluster incremental training architecture that eliminates cross-cluster synchronization; (2) we develop an adaptive low-rank decomposition scheme that exploits the intrinsic structure of embedding updates; and (3) we design a performance isolation mechanism to prevent training workloads from degrading inference latency."

---

## Part 2: Literature Review Feedback

### What Works Well

- **Move 1 (Thematic Overview)** effectively organizes the literature into four themes: DLRM architectures, industrial deployments, parameter management, and real-time update approaches
- **Move 2 covers substantial ground** — from hash-based embedding (Meta's Compositional Embedding) to low-rank factorization to training-inference co-location
- **Move 3 identifies five specific gaps** — this is thorough and well-articulated. The gaps about abstraction interoperability, developer effort, and production workload evidence are particularly insightful
- **Move 4 is strong** — it explicitly connects the literature analysis to your proposed approach, identifying two underexplored opportunities (CPU underutilization and low-rank update structure)

### Issue 4: Move 2 Tends Toward Description

While you cover many approaches, the analysis within each subsection tends to describe what systems do rather than evaluating how well they work and what their limitations are.

**Your sentence (description):** "Recent advances include methods such as Compositional Embedding (CompEmb), which uses hash-based composition to reduce table sizes, and Tensor-Train Decomposition (TTRec), which factorizes embeddings into compact tensor formats."

**With critical analysis:** "Recent compression methods take two distinct approaches: hash-based composition (CompEmb, [citation]) reduces memory by mapping multiple features to shared embedding entries, achieving X% compression but risking hash collisions that degrade recommendation accuracy for tail entities. Tensor-train decomposition (TTRec, [citation]) preserves more structural information through factorization, but introduces computational overhead proportional to the tensor rank, making it less suitable for latency-sensitive serving paths."

### Issue 5: Cross-Subsection Synthesis Is Limited

Your four subsections (architecture, deployment, parameter management, real-time updates) are treated somewhat independently. Adding synthesis paragraphs that connect themes would strengthen the review significantly.

**Suggestion:** After the subsections, add a synthesis paragraph: "Across these four themes, a common pattern emerges: optimizations designed for the training phase (e.g., hash-based compression, low-rank decomposition) do not automatically translate to inference-time benefits because the training-inference boundary introduces a synchronization bottleneck. This observation motivates..."

### Issue 6: Some Technical Claims Need Citations

Several claims in the Literature Review appear to describe specific measurements or results without citing the source:

- "over 80% of parameter update variance can be captured by less than 5% of principal components" — which paper demonstrates this?
- "multi-minute delays" for parameter synchronization — from which production system report?

**Action:** Ensure every specific number or measurement has a citation.

---

## Part 3: Language and Process Feedback

### Issue 7: Writing Quality Is Generally Good

Your writing is clear and well-organized. A few areas for improvement:
- Some sentences are overly long and could be split
- The phrase "near-real-time" appears frequently — define it precisely once and use it consistently

### Issue 8: Reflection Shows Good Self-Awareness

Your reflection identifies that your biggest challenge is "abstracting high-level contributions from detailed system mechanisms." This is visible in the draft — you handle the system details well but sometimes lose the higher-level argument thread. The solution is to start each paragraph with a topic sentence that states the analytical point, then use system details as evidence for that point.

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Add citations throughout the Introduction (every paragraph needs 3–5) | Makes claims evidence-based |
| 🔴 High | Deepen Move 2 critical analysis — add limitations and comparisons | Transforms description into argument |
| 🟡 Medium | Add cross-subsection synthesis paragraph(s) | Shows connections across themes |
| 🟡 Medium | Frame Move 2 gap more sharply with specific failure evidence | Strengthens research motivation |
| 🟡 Medium | Preview specific contributions in Move 3 | Signals clear research value |
| 🟢 Lower | Cite all specific numbers and measurements | Improves academic rigor |
| 🟢 Lower | Define "near-real-time" precisely | Clarifies key concept |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Add citations to every paragraph of the Introduction
3. Revise Move 2 with critical analysis and cross-method comparisons
4. Add synthesis paragraphs connecting the four themes
5. Submit by **15 March 2026** via Moodle forum and Turnitin
