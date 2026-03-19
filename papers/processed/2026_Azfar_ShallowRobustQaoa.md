---
aliases:
- 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via Linear-Chain
  and Ramp Schedules'
- Shallow Robust QAOA Improving
authors:
- Talha Azfar
- Ruimin Ke
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.21203/rs.3.rs-8297477/v1
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
journal_or_venue: Research Square (preprint)
methodology_tags:
- QAOA
- quantum-annealing
- variational
- QUBO
- grover
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T13:54:38.388549'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:55:53.855435'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:56:22.962054'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:56:51.092631'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:57:13.842547'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:57:25.235309'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- topic/high-frequency-trading
- method/QAOA
- method/quantum-annealing
- method/variational
- method/QUBO
- method/grover
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/scalability
title: 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via
  Linear-Chain and Ramp Schedules'
topic_tags:
- portfolio-optimisation
- high-frequency-trading
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint explores hardware-aware adaptations of the Quantum Approximate Optimization Algorithm (QAOA) to address challenges in near-term quantum computing, such as constraint handling and circuit depth limitations. The authors introduce a linear-ramp parameter schedule and a Linear-Chain (LC) ansatz that restricts interactions to nearest neighbors, reducing swap overhead and improving noise robustness. The study benchmarks these methods against standard QAOA variants on small Vehicle Routing Problem (VRP) instances, demonstrating improved feasibility and solution quality across simulations and real hardware runs.
## Methodology
The paper presents an empirical study comparing five variants of the Quantum Approximate Optimization Algorithm (QAOA) for solving the Vehicle Routing Problem (VRP). The variants include Standard QAOA, Two-Step QAOA, Grover-Mixer QAOA (GM-QAOA), Linear-Ramp Initialized QAOA (LRI-QAOA), and Linear-Chain QAOA (LC-QAOA). The research employs a hardware-aware co-design approach, integrating linear-ramp parameter schedules with a Linear-Chain (LC) ansatz to reduce circuit depth and improve noise robustness. The study benchmarks these variants across ideal simulation, shot-based Aer simulation, and real quantum hardware (IBM Eagle and Heron processors). The methodology involves formulating the VRP as a Quadratic Unconstrained Binary Optimization (QUBO) problem, converting it to an Ising Hamiltonian, and implementing the QAOA circuits using Qiskit. Performance is evaluated based on feasibility of solutions, solution quality (finding the known optimum), circuit depth, gate requirements, and robustness to noise. Error suppression techniques like dynamical decoupling (XpXm) and Conditional Value at Risk (CVaR) are also tested to enhance optimization outcomes on hardware.

**Algorithms used:** QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp Initialized QAOA, Linear-Chain QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were implemented using Qiskit SDK (version 2.1.1) within the Qiskit Runtime environment. The setup included classical simulators (statevector and Aer), as well as real quantum processors (IBM Eagle and Heron). The QAOA circuits were optimized using the COBYQA optimizer, targeting a low expectation value of the VRP cost Hamiltonian. For each set of optimized parameters, 10,000 measurement outcomes (shots) were sampled to estimate solution statistics. Hardware experiments involved parameter transfer from simulation to hardware, with lightweight error suppression techniques like dynamical decoupling (XpXm) applied to improve feasibility and solution quality.

**Dataset:** A representative Vehicle Routing Problem (VRP) instance comprising a single depot, three customer nodes, and two vehicles was used for benchmarking. Customer locations were randomly distributed on a two-dimensional Euclidean plane, with pairwise edge weights computed as squared Euclidean distances. Larger instances (e.g., 5-node, 2-vehicle problem requiring 30 qubits) were also tested to assess scaling performance.
## Findings
- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA in noiseless and shot-based simulations on small VRP instances.
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuits on IBM Eagle/Heron hardware.
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (from <1% to >2%) and recovers the optimal VRP solution in several trials.
- [supported] Grover-Mixer QAOA and Two-Step QAOA show high feasibility in simulation (e.g., 21% for GM-QAOA at p=8) but are hampered by deeper circuits, making them less effective on real hardware.
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, outperforming random initialization in simulations (e.g., 47.6% feasibility vs. 2% for standard QAOA at p=8).
- [supported] Dynamical decoupling (XpXm) improves hardware performance (e.g., optimal solution rank improved from 235 to 15 on IBM Rensselaer), while heavier error mitigation (e.g., ZNE, Pauli twirling) degrades performance due to circuit distortion.
- [supported] LC-QAOA scales efficiently to larger VRP instances (30 qubits), reliably recovering the optimal route at depths p>16 on both IBM Eagle and Heron, with higher success on lower-error devices.
- [supported] CVaR (Conditional Value at Risk) objective improves optimization by biasing search toward high-quality solutions, enabling reliable performance at larger scales.
- [speculative] Hardware-aligned ansätze and structured schedules (e.g., linear-ramp) may provide a scalable path for quantum optimization in logistics, though absolute feasibility remains low on current hardware.
- [speculative] Co-design of algorithm, schedule, and compilation could unlock reliable performance at the edge of today’s hardware capabilities, but extensions to capacitated/time-window VRPs remain untested.
- [disputed] Heavy post-processing error mitigation (e.g., ZNE, Pauli twirling) is less effective than lightweight error suppression (e.g., dynamical decoupling) for QAOA, contradicting some prior literature on mitigation strategies.

**Results summary:** The paper presents a hardware-aware co-design approach for QAOA applied to the Vehicle Routing Problem (VRP), demonstrating that linear-ramp parameter schedules and Linear-Chain (LC) ansätze significantly improve feasibility, solution quality, and noise robustness. In simulations, LC-QAOA and LRI-QAOA outperform standard QAOA and other variants (e.g., Grover-Mixer, Two-Step) by concentrating probability on feasible solutions and reducing two-qubit gate depth. On real hardware (IBM Eagle/Heron), LC-QAOA with dynamical decoupling achieves >2% feasibility and recovers optimal solutions, while deeper variants (e.g., Grover-Mixer) fail due to noise. The study also shows that lightweight error suppression outperforms heavy mitigation techniques, and CVaR improves scalability to 30-qubit instances. However, absolute feasibility remains low (<1%), and results depend on backend calibration.

**Performance claims:**
- Linear-ramp initialization improves feasibility from 2% (standard QAOA) to 47.6% (LRI-QAOA) in noiseless simulations at p=8.
- LC-QAOA achieves the shallowest two-qubit gate depth (e.g., significantly lower than Grover-Mixer QAOA, which exceeds 3000 gates at p=2).
- LC-QAOA with XpXm dynamical decoupling doubles feasibility on hardware (from <1% to >2%) and improves optimal solution rank (e.g., from 235 to 15 on IBM Rensselaer).
- Grover-Mixer QAOA achieves 21% feasibility in simulation at p=8, but feasibility drops to near-zero on hardware due to circuit depth.
- CVaR enables reliable recovery of the optimal route at p>16 for 30-qubit VRP instances on both IBM Eagle and Heron.
- Dynamical decoupling (XpXm) improves feasibility from 1.14% to 1.60% on IBM Fez and optimal solution rank from 16 to 6.
## Quantum advantage claim
**Classification:** speculative

The paper claims that hardware-aligned ansätze (e.g., LC-QAOA) and structured schedules (e.g., linear-ramp) provide a promising path for near-term quantum optimization, but quantum advantage is not demonstrated. Results are from small-scale simulations and real hardware with low feasibility (<2%), and no comparison to state-of-the-art classical solvers (e.g., CPLEX) is provided for larger instances. The advantage is framed as theoretical/scalability potential rather than empirical.
## Limitations
- Absolute feasibility on current hardware remains low (<1% without mitigation), limiting practical applicability [inferred]
- Experiments limited to small VRP instances (e.g., 3 customers, 2 vehicles) due to hardware constraints and simulation limitations
- Results heavily depend on backend calibration and mapping, introducing variability across devices [inferred]
- No comparison with state-of-the-art classical solvers (e.g., CPLEX) in terms of runtime or solution quality for larger instances [inferred]
- Extending to capacitated or time-window VRPs will stress both qubit count and circuit depth, which was not tested
- The study does not explore hybrid quantum-classical workflows for larger instances, which may be necessary for practical deployment [inferred]
- Hardware noise and decoherence dominate performance, even with error suppression techniques
- Lack of peer review (preprint status) may affect methodological rigor and reproducibility [inferred]
- Linear-Chain QAOA trades expressiveness for hardware efficiency, potentially missing optimal solutions due to restricted connectivity [inferred]
- Parameter transfer from simulation to hardware may not generalize across different problem instances or hardware generations [inferred]
- Error mitigation techniques like Pauli twirling and ZNE underperformed compared to simple dynamical decoupling, suggesting limited utility for QAOA [inferred]
- The study focuses on a single problem family (VRP), limiting generalizability to other combinatorial optimization problems [inferred]
- No analysis of how qubit error rates or gate fidelities directly impact solution quality [inferred]
- The paper does not address the scalability of the proposed methods to industry-relevant problem sizes (e.g., 50+ nodes) [inferred]
## Open questions
- How does the algorithm perform with more than 5 nodes or 2 vehicles in hardware experiments?
- What is the impact of decoherence and gate errors on solution quality at higher depths (p > 20)?
- Can the linear-ramp schedule and LC-QAOA maintain performance on larger, more constrained problems (e.g., capacitated VRP)?
- How do the proposed methods compare to quantum annealing or hybrid quantum-classical approaches for the same problem instances?
- What is the minimum hardware fidelity required to achieve >10% feasibility for VRP instances?
- Can adaptive schedules or parameter transfer techniques improve performance across diverse problem instances?
- How does the choice of penalty weight (λ) affect feasibility and solution quality in larger instances?
- What are the trade-offs between qubit count, circuit depth, and solution quality for industry-relevant problem sizes?
- Can hardware-aware compilation (e.g., qubit placement, chain orientation) further reduce circuit depth without sacrificing performance?

**Future work:**
- Expand problem realism by incorporating capacities, time windows, and multi-objective costs (e.g., emissions) into VRP benchmarks
- Study adaptive schedule families that adjust to measured gradients on-device and quantify cross-instance parameter transfer
- Co-optimize qubit placement, chain orientation, and dynamical decoupling timing for hardware-aware compilation
- Benchmark against VQE-style problem-inspired ansätze and annealing/CQM baselines on the same instances
- Test hybrid strategies combining classical heuristics (e.g., decomposition, warm starts) with LC-QAOA for larger problems
- Investigate the scalability of LC-QAOA with CVaR to industry-relevant problem sizes (e.g., 50+ nodes)
- Explore alternative error suppression techniques (e.g., pulse-level optimization) to improve hardware performance
- Develop encodings that balance qubit count against feasibility guarantees for constrained problems
- Validate the proposed methods on diverse combinatorial optimization problems (e.g., portfolio optimization, scheduling)
## Key ideas
- #idea:near-term-feasibility — Hardware-aware QAOA variants (e.g., Linear-Chain QAOA) reduce circuit depth and improve noise robustness, making them viable for near-term quantum devices in logistics and potentially financial optimization problems like portfolio-optimisation or high-frequency-trading
- #idea:hybrid-approach — Co-design strategies combining classical optimization (e.g., COBYQA, CVaR) with quantum algorithms enhance solution quality and feasibility for VRP, suggesting potential for hybrid approaches in financial use cases
- #idea:quantum-advantage — Speculative claim that hardware-aligned ansätze and structured schedules may enable quantum advantage for combinatorial optimization, though not empirically validated for financial applications
- #limitation:noise — Feasibility on real hardware remains below 1% for all QAOA variants, highlighting noise as a critical barrier to practical deployment in finance
- #limitation:qubit-count — Study limited to small VRP instances (3 customer nodes, 2 vehicles) due to hardware constraints, raising scalability concerns for larger financial problems (e.g., portfolio-optimisation with many assets)
- #limitation:data-encoding — Linear-Chain QAOA sacrifices expressiveness by restricting ZZ interactions to nearest neighbors, potentially limiting performance on financial problems requiring long-range interactions (e.g., multi-asset correlations)
## Contradictions
- #contradiction:scalability — Paper claims LC-QAOA scales to larger VRP instances (30 qubits) on IBM hardware, but feasibility remains low (<2%), contradicting implied scalability advantages. No comparison to classical solvers (e.g., CPLEX) is provided, which is critical for validating quantum advantage claims in financial optimization.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
