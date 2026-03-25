# Quantum Cryptography

**Papers:** 13 | **Theoretical:** 6 | **Review:** 3

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Shaon_ReviewRoutingResource]] | 2026 | review-article | — | not-applicable | low |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, quantum-SVM, amplitude-estimation, grover | theoretical | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-walk, quantum-simulation | speculative | high |
| [[2025_JETIR_QuantumFinance]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational, classical-simulation | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | QAOA, VQE, quantum-ML, amplitude-estimation, variational | theoretical | high |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, classical-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | HHL, QAOA, VQE, quantum-annealing, quantum-ML, quantum-SVM, variational, grover | speculative | medium |
| [[2024_Pasupuleti_AdvancementsQuantumComputing]] | 2024 | peer-reviewed-theoretical | QAOA, VQE, grover, variational | theoretical | medium |
| [[2023_Alsalman_AcceleratingQuantumReadiness]] | 2023 | peer-reviewed-theoretical | — | not-applicable | medium |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | QAOA, quantum-annealing, quantum-ML, HHL | speculative | medium |
| [[2022_Albareti_StructuredSurveyQuantum]] | 2022 | preprint | QAOA, VQE, quantum-annealing, HHL, amplitude-estimation, QUBO, variational, classical-simulation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, variational, grover, quantum-walk, classical-simulation | speculative | medium |
| [[2019_Li_ResearchQuantumComputing]] | 2019 | conference-paper | quantum-annealing, HHL, grover, quantum-simulation | speculative | medium |

## Key Findings

- [supported] The review identifies four dominant themes in recent quantum networking literature: RL/DRL-driven adaptive routing and control, resource-aware multi-objective optimization, fidelity/noise-robust secure communication, and scalability/deployment-oriented strategies. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] Across reviewed studies, RL/DRL methods are presented as increasingly central for handling stochastic entanglement generation, dynamic topology, and changing resource availability in quantum networks. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The surveyed literature consistently shows trade-offs among fidelity, latency, throughput, fairness, and resource utilization, with improvements in one objective often degrading another. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The review finds broad agreement that practical quantum networking is constrained by decoherence, probabilistic link success, limited qubit and memory resources, and imperfect gates/measurements. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The literature surveyed suggests that learning-based routing can improve adaptivity and request success under dynamic conditions, but its effectiveness depends on simulator assumptions, reward/state design, training cost, and generalization across topologies. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] Optimization- and heuristic-based methods are characterized as more interpretable and deployment-oriented than RL methods, but often face higher computational cost or reduced adaptivity as network size grows. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] Fidelity-preserving and QKD-oriented methods improve robustness and security under realistic noise assumptions, but usually introduce additional qubit, control, or operational overhead. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The review highlights a field-wide shift toward cross-layer designs that jointly consider physical-layer fidelity/noise, network-layer routing/scheduling, and infrastructure constraints. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] A major consensus finding is that reproducible benchmarking remains weak across the literature because studies use inconsistent topology models, traffic assumptions, noise models, baselines, and reporting practices. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The review concludes that hybrid quantum-classical integration, hardware-aware design, and fault-tolerant architectures are recurring recommendations for practical deployment. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The surveyed literature indicates that near-term deployment is most plausible in metro-scale trusted-node QKD, satellite-to-ground links, inter-data-center secure networking, and early distributed quantum computing scenarios. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] Areas of disagreement or tension across the reviewed literature include heuristic simplicity versus learning-based adaptivity, throughput maximization versus fairness, and fidelity enhancement versus resource overhead. — [[2026_Shaon_ReviewRoutingResource]]
- [supported] The review identifies finance as one of the major industry domains where quantum computing applications have emerged by 2025, alongside agriculture, defense, energy, healthcare, infrastructure, manufacturing, and technology. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] In financial services, the review highlights two main themes in the cited literature: quantum-secure transaction infrastructure via quantum tokens/QKD and quantum-enhanced trading optimization for bond markets. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that Quantinuum and Mitsui demonstrated transmission of quantum tokens over a 10 km fiber-optic network in Tokyo for ultra-secure transaction verification, positioning no-cloning-based token schemes as a potential anti-forgery and anti-double-spending mechanism. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that HSBC and IBM presented a quantum-enabled algorithm for algorithmic bond trading in European corporate bond markets, using IBM Heron hardware with Qiskit and classical computing on production-scale trading data. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Across reviewed application areas, the paper’s synthesis suggests that near-term quantum use in industry is predominantly hybrid quantum-classical rather than fully quantum. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review suggests that many practical quantum applications across sectors, including finance, currently focus on optimization, machine learning, and secure communications rather than fault-tolerant large-scale quantum computation. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] A recurring theme across the reviewed literature is that current demonstrations are often proof-of-concept, pilot, or early commercial deployments rather than mature large-scale production systems. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review finds broad consensus that quantum computing remains constrained by high development cost, limited accessibility, hardware scaling challenges, and shortage of specialized workforce. — [[2026_Mahmod_StateQuantumComputing]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| QAOA | 9 |
| VQE | 8 |
| quantum-ML | 8 |
| grover | 7 |
| variational | 7 |
| quantum-annealing | 6 |
| HHL | 6 |
| amplitude-estimation | 5 |
| quantum-SVM | 4 |
| classical-simulation | 4 |
| QUBO | 2 |
| quantum-walk | 2 |
| quantum-simulation | 2 |

## Open Questions

- How can quantum networks scale end-to-end under severe loss and decoherence while maintaining acceptable fidelity, latency, throughput, and request success rates? — [[2026_Shaon_ReviewRoutingResource]]
- How should trade-offs between fidelity, throughput, latency, fairness, and resource consumption be jointly optimized rather than treated separately? — [[2026_Shaon_ReviewRoutingResource]]
- What repeater and quantum memory designs can support long-distance communication with realistic resource overheads and failure tolerance? — [[2026_Shaon_ReviewRoutingResource]]
- How can routing and resource-allocation methods remain robust under realistic noise, device imperfections, and dynamic topology changes? — [[2026_Shaon_ReviewRoutingResource]]
- What unified noise models and sensitivity-analysis frameworks are most appropriate for evaluating quantum networking protocols under real hardware conditions? — [[2026_Shaon_ReviewRoutingResource]]
- How can QKD security claims be maintained when moving from idealized assumptions to imperfect devices and finite-key regimes? — [[2026_Shaon_ReviewRoutingResource]]
- What standardized benchmarking framework should be adopted so that routing, QKD, and resource-optimization studies can be compared fairly across papers? — [[2026_Shaon_ReviewRoutingResource]]
- How can hybrid quantum-classical networks manage synchronization, control-plane overhead, and interoperability across heterogeneous hardware? — [[2026_Shaon_ReviewRoutingResource]]
- Which near-term deployment scenarios—metro-scale trusted-node QKD, satellite-to-ground links, inter-data-center networking, or distributed quantum computing—are most practical under current constraints? — [[2026_Shaon_ReviewRoutingResource]]
- How can satellite quantum networks handle link intermittency, atmospheric effects, and fast topology changes while preserving security and performance? — [[2026_Shaon_ReviewRoutingResource]]
