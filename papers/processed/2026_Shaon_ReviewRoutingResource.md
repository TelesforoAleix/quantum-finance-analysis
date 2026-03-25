---
aliases:
- A Review of Routing and Resource Optimization in Quantum Networks
- Review Routing Resource Optimization
authors:
- Md. Shazzad Hossain Shaon
- Mst Shapna Akter
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.3390/electronics15030557
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Electronics
methodology_tags: []
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-25T16:15:59.003497'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:16:02.707477'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:16:10.473851'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:43.458138'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:17:07.573959'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:17:14.572419'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/quantum-cryptography
- idea/near-term-feasibility
- idea/hybrid-approach
title: A Review of Routing and Resource Optimization in Quantum Networks
topic_tags:
- quantum-cryptography
year: 2026
zotero_key: ''
---

## Abstract summary
The paper surveys recent work on routing and resource optimization in quantum networks, with a focus on entanglement routing, QKD, and qubit management over short- and long-distance links. It organizes prior studies by methodological families such as RL/DRL-based control, heuristic and optimization-based routing, and fidelity/QKD-oriented designs, comparing them on objectives, assumptions, and scalability. The review highlights open challenges in dynamic adaptation, resource constraints, noise robustness, and reproducible evaluation, and argues for hybrid quantum–classical, cross-layer approaches to enable practical large-scale quantum networking.
## Methodology
This paper is a scoping review/survey of quantum networking research, with emphasis on routing, resource optimization, entanglement distribution, QKD, fidelity robustness, and scalability. The review explicitly states that it follows the PRISMA-ScR reporting guidelines and summarizes the literature identification, duplicate removal, screening, and inclusion workflow in a PRISMA-style flow diagram. The authors report a final inclusion of 64 studies. Rather than conducting new experiments, the paper synthesizes prior work through a thematic classification taxonomy organized by primary methodological focus: (1) RL/DRL-driven adaptive routing and control, (2) resource-aware and multi-objective optimization, (3) fidelity/noise robustness and secure communication, and (4) scalability and deployment-oriented strategies. The comparative synthesis evaluates studies using common criteria such as target objectives (e.g., fidelity, throughput, request success rate, latency), network assumptions (e.g., topology scale, noise/decoherence model, memory and EPR constraints), and methodological mechanisms (e.g., RL/DRL, heuristic optimization, QKD-oriented designs). The review also includes a comparative table positioning this survey against prior surveys and overview papers, and it highlights cross-study trends, recurring trade-offs, deployment challenges, and future research directions. No formal database search string, named databases, or detailed inclusion/exclusion criteria beyond the PRISMA-ScR-based screening summary are provided in the excerpt.

**Algorithms used:** Q-learning, Deep Q-Learning, DQN, DRN, PPO, Dijkstra, Yen's algorithm, Monte Carlo Tree Search, Integer Linear Programming, Branch-and-Bound
**Frameworks:** PRISMA-ScR, NetSquid, Qiskit
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [supported] The review identifies four dominant themes in recent quantum networking literature: RL/DRL-driven adaptive routing and control, resource-aware multi-objective optimization, fidelity/noise-robust secure communication, and scalability/deployment-oriented strategies.
- [supported] Across reviewed studies, RL/DRL methods are presented as increasingly central for handling stochastic entanglement generation, dynamic topology, and changing resource availability in quantum networks.
- [supported] The surveyed literature consistently shows trade-offs among fidelity, latency, throughput, fairness, and resource utilization, with improvements in one objective often degrading another.
- [supported] The review finds broad agreement that practical quantum networking is constrained by decoherence, probabilistic link success, limited qubit and memory resources, and imperfect gates/measurements.
- [supported] The literature surveyed suggests that learning-based routing can improve adaptivity and request success under dynamic conditions, but its effectiveness depends on simulator assumptions, reward/state design, training cost, and generalization across topologies.
- [supported] Optimization- and heuristic-based methods are characterized as more interpretable and deployment-oriented than RL methods, but often face higher computational cost or reduced adaptivity as network size grows.
- [supported] Fidelity-preserving and QKD-oriented methods improve robustness and security under realistic noise assumptions, but usually introduce additional qubit, control, or operational overhead.
- [supported] The review highlights a field-wide shift toward cross-layer designs that jointly consider physical-layer fidelity/noise, network-layer routing/scheduling, and infrastructure constraints.
- [supported] A major consensus finding is that reproducible benchmarking remains weak across the literature because studies use inconsistent topology models, traffic assumptions, noise models, baselines, and reporting practices.
- [supported] The review concludes that hybrid quantum-classical integration, hardware-aware design, and fault-tolerant architectures are recurring recommendations for practical deployment.
- [supported] The surveyed literature indicates that near-term deployment is most plausible in metro-scale trusted-node QKD, satellite-to-ground links, inter-data-center secure networking, and early distributed quantum computing scenarios.
- [speculative] The paper reiterates that quantum communication can provide unconditionally secure key exchange under standard QKD assumptions, but this review does not itself empirically validate that claim.
- [speculative] The abstract claims quantum entanglement and interference provide exponential improvements for optimization, cryptography, and simulation, but this review does not present original evidence establishing such speedups in financial or networking applications.
- [supported] Areas of disagreement or tension across the reviewed literature include heuristic simplicity versus learning-based adaptivity, throughput maximization versus fairness, and fidelity enhancement versus resource overhead.

**Results summary:** This review synthesizes 64 studies on routing and resource optimization in quantum networks and organizes the literature into four main themes: adaptive RL/DRL routing, resource-aware multi-objective optimization, fidelity/noise-robust secure communication, and scalability/deployment strategies. The main consensus is that quantum networking performance is fundamentally limited by stochastic entanglement generation, decoherence, scarce qubits and memories, and imperfect hardware. The reviewed studies collectively suggest that RL/DRL approaches often improve adaptivity and request success in dynamic simulated environments, while heuristic and optimization methods offer more structured and interpretable control but may scale poorly or adapt less well. The review also emphasizes that fidelity-preserving and QKD-oriented methods improve robustness and security at the cost of extra overhead. A central cross-study conclusion is that the field is moving toward deployment-aware, cross-layer, hybrid quantum-classical designs, but comparison across papers remains difficult because evaluation assumptions and metrics are inconsistent.

**Performance claims:**
- qRL reported around 20% greater fidelity than baselines in a high-resource configuration
- qRL maintained fidelity greater than 0.6 in a low-resource configuration, while qDijkstra fell below 0.4
- qRL maintained request success rates above 80% under 3000-request demand in a resource-constrained setting, while traditional methods fell below 50%
- DQRL improved SEER request success rate from 50% to 74% (48% increase)
- DQRL improved REPS request success rate from 45% to 73% (61% increase)
- Entanglement caching improved request success rates by 12% to 19% when entangled links lasted 6 or more time slots
- Increasing swap probability to 0.9 yielded a 55% improvement over baseline in the proactive swapping study
- DQRA/DQN/DRN achieved 80% to 90% success rates in qubit-rich settings
- DQRA retained 60% to 75% success rates under severe settings with c_i = 2, exceeding baselines by 20% to 40%
- Routing time in DQRA remained linear with network size, including networks up to 25 x 25 nodes
- PPO outperformed Monte Carlo by up to 13,000x in 16-node noisy networks
- PPO required 60,000 actions versus 546 million for Monte Carlo under amplitude damping
- PPO required 39,000 steps versus 60 million for Monte Carlo under phase-noise settings
- PPO retained 93.4% functionality in dynamic error scenarios versus 33.1% for Monte Carlo
- COSP showed a 50% increase in average predicted throughput over earlier methods
- COSP improved service rates by 55%
- Heuristic repeater placement produced feasible solutions within seconds, whereas ILP could take days for a 54-node network
- MULTI-R served all 20 quantum-user pairs in the reported comparison
- MR-REC improved predicted throughput by up to 55% over FER
- A 12-bit key was transmitted using a 13-qubit GHZ state in simulation
## Quantum advantage claim
**Classification:** not-applicable

This is a review article on quantum networking rather than a paper demonstrating a direct quantum computational advantage in financial services. It summarizes prior networking, routing, and QKD studies, but does not itself establish a new quantum advantage result.
## Limitations
- The review notes that practical quantum communication still faces major barriers including end-to-end scalability under loss and decoherence, which degrade entanglement quality, fidelity, and secret-key rates over long distances.
- Quantum repeater deployment remains limited by short memory lifetimes, imperfect gates and measurements, and coordination overhead across nodes.
- Many reviewed methods face trade-offs between fidelity improvement and resource/processing overhead, meaning gains in one metric can reduce throughput or efficiency.
- The paper highlights a lack of standardized and reproducible evaluation across studies, with inconsistent topology generation, traffic models, noise models, baselines, metrics, and reporting granularity.
- The review emphasizes that many protocols rely on idealized assumptions and do not fully bridge the gap to realistic hardware behavior, including device imperfections and finite-key effects in QKD.
- Integration with classical networks is still underdeveloped, with unresolved issues around synchronization, classical control messaging, interoperability, maintenance, monitoring, and fault management.
- The survey is centered on quantum networking, routing, QKD, and resource optimization rather than financial-services-specific quantum computing applications, limiting direct applicability to a finance-focused review.
- [inferred] As a review article, the paper does not report a full reproducible search protocol in the provided text beyond a PRISMA-ScR summary, so database coverage, search strings, and screening criteria may be insufficiently detailed for replication.
- [inferred] The review includes 64 studies but does not clearly state whether non-English studies were included, creating possible language bias.
- [inferred] Grey literature handling appears selective and not systematically justified; although some reports and RFCs are cited, the inclusion/exclusion policy for non-peer-reviewed sources is unclear.
- [inferred] Because the paper was published in early 2026, coverage may quickly become outdated in a fast-moving field, especially for hardware and deployment developments.
- [inferred] The review appears narrative/thematic rather than quantitatively synthesized, so there is no meta-analytic estimate of comparative performance across methods.
- [inferred] No formal quality appraisal or risk-of-bias assessment of included studies is evident in the provided text, limiting confidence in cross-study conclusions.
## Open questions
- How can quantum networks scale end-to-end under severe loss and decoherence while maintaining acceptable fidelity, latency, throughput, and request success rates?
- How should trade-offs between fidelity, throughput, latency, fairness, and resource consumption be jointly optimized rather than treated separately?
- What repeater and quantum memory designs can support long-distance communication with realistic resource overheads and failure tolerance?
- How can routing and resource-allocation methods remain robust under realistic noise, device imperfections, and dynamic topology changes?
- What unified noise models and sensitivity-analysis frameworks are most appropriate for evaluating quantum networking protocols under real hardware conditions?
- How can QKD security claims be maintained when moving from idealized assumptions to imperfect devices and finite-key regimes?
- What standardized benchmarking framework should be adopted so that routing, QKD, and resource-optimization studies can be compared fairly across papers?
- How can hybrid quantum-classical networks manage synchronization, control-plane overhead, and interoperability across heterogeneous hardware?
- Which near-term deployment scenarios—metro-scale trusted-node QKD, satellite-to-ground links, inter-data-center networking, or distributed quantum computing—are most practical under current constraints?
- How can satellite quantum networks handle link intermittency, atmospheric effects, and fast topology changes while preserving security and performance?

**Future work:**
- Develop hybrid quantum-classical algorithms for efficient resource allocation in quantum networks.
- Design hardware-aware methods to improve real-world deployment of routing and resource-optimization techniques.
- Advance fault-tolerant architectures and stronger error-correction mechanisms for dependable quantum communication.
- Integrate quantum networks with existing classical infrastructure to improve security, dependability, and broader adoption.
- Pursue integrated cross-layer optimization linking physical-layer fidelity management with network-layer routing and scheduling.
- Create repeater and memory designs that minimize resource overhead while remaining compatible with telecom infrastructure and realistic device performance.
- Study learning-based routing and control under reproducible benchmarks, realistic noise conditions, and explicit reporting of training cost and generalization behavior.
- Establish standardized evaluation templates covering topology models, traffic distributions, noise/channel models, resource budgets, training budgets, outcome metrics, and experimental environment details.
- Investigate intermittency-aware routing, fast reconfiguration, and cross-layer control for self-organizing satellite quantum networks.
- Prioritize end-to-end system engineering for satellite-based quantum communication, including atmospheric effects, terrestrial backbone integration, and consistent security/performance evaluation.
- Explore deployment-aware hybrid classical-quantum architectures for 6G and next-generation communication systems.
- Improve quantum memory, photonic interfaces, and hybrid quantum-classical integration to enable robust and scalable quantum networks.
## Key ideas
- #idea:hybrid-approach — The review argues that hybrid quantum–classical, cross-layer control and routing are necessary for practical large-scale quantum networks and QKD deployment.
- #idea:near-term-feasibility — Near-term deployment is framed as most plausible for metro-scale trusted-node QKD, satellite-to-ground links, inter-data-center secure networking, and early distributed quantum computing scenarios.
- #idea:near-term-feasibility — Learning-based routing and resource management appear promising in simulation, but practical deployment remains constrained by decoherence, limited memories/qubits, and inconsistent benchmarking.
- #idea:hybrid-approach — Hardware-aware design, standardized evaluation, and integration with classical infrastructure are presented as prerequisites for real-world deployment.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
