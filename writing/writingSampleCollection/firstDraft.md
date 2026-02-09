# My First Draft

## Source Information

**Date written:** [Date]

**Context:** [What is this draft for? Is it for the course assignment?]

**Status:** [Complete draft / Partial draft - which sections are included?]

---

## Introduction

### Move 1: Establishing a Territory

Deep Learning Recommendation Models (DLRMs) are fundamental infrastructure powering personalized user experiences across major online platforms. Their operational scale is staggering: within Meta's infrastructure alone, DLRMs consume over 50% of training cycles and 60% of inference resources. This resource footprint stems from their complex architecture, which combines dense neural networks with massive embedding tables (EMTs) storing high-dimensional representations of users and items. Industrial deployments now reach petabyte scale, creating unprecedented systems challenges.

Production DLRMs deploy a decoupled architecture, where training clusters continuously update parameters using streaming user interactions, and inference clusters serve predictions using the latest parameters synced via centralized parameter servers. This separation optimizes specialized hardware but introduces severe synchronization overhead across clusters. For example, syncing just 10% of a 200TB EMT over 100GbE networks takes over 26 minutes. During this delay, inference nodes operate with stale parameters, directly degrading recommendation quality.

Maintaining model freshness is crucial for revenue-critical services, as model recommendation accuracy decays rapidly without updates. Industry studies confirm that even a 0.1% accuracy drop can translate to millions in lost revenue, while update delays of more than 5 minutes can measurably reduce user engagement. Therefore, production systems require near-real-time parameter updates. However, synchronizing multi-terabyte EMTs across clusters over commodity networks incurs significant latencies, far exceeding acceptable freshness windows.

### Move 2: Identifying a Niche

Existing solutions struggle to resolve this tension. Delta-based updates synchronize only changed parameters since the last update, reducing data volume compared to full sync. However, update volumes remain massive, exceeding 10% of EMTs even in short 10-minute windows, still translating to multi-minute synchronization delays. Prioritization-based updates transfer only small subsets of important changed parameters based on gradient magnitude. However, this strategy still incurs multi-minute delays, and magnitude-based heuristics omit semantically critical but low-gradient updates, directly leading to accuracy degradation. Ultimately, these approaches are fundamentally limited by the training-inference decoupled architecture, which intrinsically creates an inter-cluster bandwidth bottleneck.

By examining production traces, we identify two overlooked opportunities. First, inference nodes exhibit sustained CPU underutilization, with peak utilization reaching only 20%, creating significant headroom for local computation. Second, embedding gradients possess a strong intrinsic low-rank structure, where over 80% of parameter update variance can be captured by less than 5% of principal components. This allows updates to be represented compactly as low-rank matrices. Together, these insights enable a paradigm shift: co-locating lightweight training within inference nodes, leveraging idle CPUs to compute compact, low-rank updates, eliminating inter-cluster synchronization entirely while preserving model accuracy.

### Move 3: Occupying the Niche

Exploiting these opportunities, this paper presents a system that embeds Low-Rank Adaptation (LoRA) trainer directly within inference nodes. Each node performs continuous, local updates to its embeddings using recently cached interaction data. Instead of transmitting raw parameter deltas, it computes and applies updates via compact factors derived from low-rank decomposition, thereby eliminating inter-cluster synchronization and achieving near-real-time freshness.

However, the design faces two critical challenges. First, the intrinsic low-rankness of updates is dynamic. A fixed LoRA rank is either too small, failing to capture complex updates and degrading accuracy, or too large, wasting memory and compute resources. Second, merging training and inference on the same node exacerbates memory bandwidth contention. The irregular access patterns of online training can directly interfere with inference, causing latency spikes that breach stringent tail-latency SLAs.

To address these challenges, the system introduces two core innovations. First, a dynamic rank adaptation mechanism continuously adjusts the LoRA dimension via real-time PCA monitoring and prunes inactive parameters, effectively constraining memory overhead to less than 2% of full EMTs. Second, a performance-isolated training runtime mitigates interference with inference through NUMA-aware resource scheduling and hardware-enforced QoS partitioning, reinforced by data reuse and load-sensitive scheduling. Comprehensive evaluation demonstrates that the system effectively resolves the freshness-accuracy tradeoff, reducing update latency by 2× compared to delta-update approaches while achieving higher accuracy within tight freshness windows.

---

## Literature Review

### Move 1: Thematic Overview

We examine the state-of-the-art in Deep Learning Recommendation Models (DLRMs), focusing on their architectural design, industrial deployment strategies, and parameter synchronization mechanisms. The scope encompasses three primary research themes: the fundamental architecture and training paradigms of DLRMs, production system designs that decouple training and inference clusters, and parameter update strategies that balance model freshness, accuracy, and system overhead. This section synthesizes findings from both academic research and industry-scale deployments. By critically analyzing existing approaches and identifying their limitations, the following analysis establishes the foundation for understanding the tradeoffs inherent in maintaining fresh, accurate recommendation models at petabyte scale.

### Move 2: Critical Analysis

DLRMs process two distinct input types through parallel pathways: dense features are fed into densely connected networks to generate feature representations, while sparse features are encoded as one-hot or multi-hot vectors and mapped to dense embeddings via massive embedding tables (EMTs). The training process leverages historical interaction data to optimize parameters end-to-end using stochastic gradient descent. EMTs undergo dynamic row-wise updates where only embeddings corresponding to IDs in each mini-batch are modified, creating irregular memory access patterns. During inference, the trained DLRM generates real-time predictions through feedforward passes, demanding low-latency execution under strict SLA constraints. The scale of industrial DLRMs has expanded dramatically, with systems reaching petabyte scale, primarily attributed to large EMTs storing the vast majority of model parameters.

Production environments employ a decoupled architecture where training and inference run on separate clusters. Training clusters continuously process streaming user-item interactions to update model parameters, pushing updates to a central parameter server that manages version control. Inference clusters retrieve the latest parameters to serve real-time recommendations. Training workloads face extreme data rates, requiring high batch processing throughput and frequent parameter exchanges over high-bandwidth networks. Inference clusters must maintain strict latency bounds while frequently pulling fresh parameters, employing hybrid CPU-GPU memory hierarchies to provide low latency and massive storage capacity simultaneously.

Existing deployment frameworks face fundamental limitations. Production systems rely on full-parameter synchronization, transferring entire EMTs from training clusters to parameter servers. While ensuring strong consistency, this approach proves prohibitively expensive, requiring over four hours for 200 TB models over commodity networks, introducing unacceptable staleness. Delta-based synchronization selects priority parameters to transfer, but selection heuristics based on update magnitude omit semantically critical but small-value changes, potentially leading to quality degradation. Even with 5% sampling rates, deltas remain massive, consuming over 14 minutes for transfer, causing unacceptable delays. These approaches are fundamentally limited by the training-inference decoupled architecture, which creates an inter-cluster bandwidth bottleneck.

Maintaining model freshness is crucial, as model accuracy decays rapidly without updates. Even a 0.1% accuracy drop can translate to millions in lost revenue, while update delays exceeding 5 minutes measurably reduce user engagement. Production systems require near-real-time parameter updates, but synchronizing multi-terabyte EMTs incurs significant latencies, highlighting the fundamental tension between freshness, accuracy, and overhead.

### Move 3: Research Gaps

Several critical research gaps remain unaddressed. First, existing parameter synchronization approaches are fundamentally limited by the training-inference decoupled architecture, which creates an inter-cluster bandwidth bottleneck. Whether employing full-parameter synchronization or delta-based updates, these approaches require transferring massive parameter volumes over network links, resulting in multi-minute delays. Second, computational resources at inference nodes remain underexploited. The sustained CPU underutilization observed in production deployments represents an untapped opportunity for local computation. Third, the intrinsic low-rank structure of embedding updates has not been systematically exploited for efficient synchronization. The strong low-rank structure of embedding gradients, where over 80% of parameter update variance can be captured by less than 5% of principal components, presents an opportunity for compact update representation. Fourth, the dynamic nature of update complexity has not been addressed. Fixed-rank approximations either fail to capture complex updates or waste resources. Fifth, interference between training and inference workloads when co-located has not been systematically studied or mitigated, with performance isolation mechanisms remaining an open research question.

### Move 4: Conclusion

We examine existing DLRM architectures, industrial deployment strategies, and parameter synchronization mechanisms. While prior work has made significant progress in scaling DLRMs to petabyte scale, we observe that fundamental limitations remain in achieving near-real-time parameter updates without sacrificing accuracy or system stability. In particular, current solutions are inherently constrained by the bandwidth bottlenecks introduced by decoupled training and inference architectures.

Our analysis reveals two underexplored opportunities: the sustained CPU underutilization at inference nodes and the intrinsic low-rank structure of embedding updates. These observations motivate a paradigm shift toward co-locating lightweight training within inference clusters. However, we identify that realizing this shift requires addressing two key challenges—dynamic rank adaptation and performance isolation. The foregoing analysis thus lays the groundwork for our proposed approach, which aims to achieve near-real-time model freshness while preserving accuracy and minimizing system overhead.

---

## Notes

[Any additional notes about your draft, challenges you faced, questions you have, etc.]
See reflection.md