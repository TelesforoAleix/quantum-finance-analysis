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
journal_or_venue: Research Square (Preprint)
methodology_tags:
- QAOA
- quantum-annealing
- variational
- grover
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:49:18.631275'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:49:20.564401'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:49:27.414718'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:49:38.210618'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:49:46.776189'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:50:22.881772'
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
- topic/risk-modelling
- method/QAOA
- method/quantum-annealing
- method/variational
- method/grover
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/scalability
title: 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via
  Linear-Chain and Ramp Schedules'
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint explores hardware-aware adaptations of the Quantum Approximate Optimization Algorithm (QAOA) to improve its practical performance on near-term quantum devices for combinatorial optimization problems, specifically the Vehicle Routing Problem (VRP). The authors propose a linear-ramp parameter schedule and a Linear-Chain ansatz to reduce circuit depth and noise sensitivity, benchmarking these against other QAOA variants across simulations and real quantum hardware. The study emphasizes co-design strategies that balance algorithmic feasibility, classical optimization overhead, and hardware constraints to enhance solution quality and robustness.
## Methodology
The paper presents an empirical study focused on improving the Quantum Approximate Optimization Algorithm (QAOA) for the Vehicle Routing Problem (VRP) by addressing hardware constraints and optimization challenges. The authors propose a hardware-aware co-design approach combining a linear-ramp parameter schedule with a Linear-Chain (LC) ansatz to reduce circuit depth and swap overhead. Five QAOA variants (Standard QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp Initialized QAOA, and LC-QAOA) are benchmarked across ideal simulation, shot-based Aer simulation, and real quantum hardware (IBM Eagle/Heron processors). The evaluation metrics include feasibility of solutions, solution quality (finding the known optimum), quantum circuit depth, gate requirements, and robustness to noise. The study uses a small VRP instance (single depot, three customer nodes, two vehicles) with edge weights based on squared Euclidean distances. Experiments are implemented using Qiskit SDK, with parameter optimization via COBYQA and sampling of 10,000 shots per run. Error suppression techniques like dynamical decoupling (XpXm) and post-processing mitigation (Pauli twirling, TREX, ZNE) are tested, alongside Conditional Value at Risk (CVaR) for optimization enhancement. The results emphasize the importance of hardware-aligned ansätze and structured schedules for near-term quantum optimization.

**Algorithms used:** QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp Initialized QAOA, Linear-Chain QAOA
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using the Qiskit SDK (version 2.1.1) within the Qiskit Runtime environment. The setup included classical simulators (statevector and Aer QASM simulator) and real quantum processors (IBM Eagle and Heron). The QAOA variants were transpiled for IBM's heavy-hex topology, with parameter optimization performed using the COBYQA optimizer. Each experiment involved 10,000 measurement shots (samples) per run. Hardware runs incorporated error suppression techniques like dynamical decoupling (XpXm) and tested post-processing error mitigation methods such as Pauli twirling, readout error mitigation (TREX), and zero-noise extrapolation (ZNE).

**Dataset:** A representative Vehicle Routing Problem (VRP) instance comprising a single depot, three customer nodes, and two vehicles. Customer locations were randomly distributed on a two-dimensional Euclidean plane, with pairwise edge weights computed as squared Euclidean distances between nodes. The problem was encoded as a Quadratic Unconstrained Binary Optimization (QUBO) formulation derived from the classical DOcplex model.
## Findings
- [supported] Linear-Ramp LC-QAOA reduces two-qubit gate depth and improves noise robustness compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA on Vehicle Routing Problem (VRP) instances
- [supported] Linear-ramp initialization improves convergence and feasibility of QAOA, concentrating more weight on feasible solutions in noiseless simulations (e.g., 47.6% feasibility for LRI-QAOA vs. ~2% for standard QAOA at p=8)
- [supported] Grover-Mixer QAOA achieves higher feasibility in simulations (21% at p=8) due to constraint-preserving mixers but suffers from deep circuits (two-qubit gate depth >3000 at p=2), making it impractical for hardware execution
- [supported] Two-Step QAOA improves feasibility over standard QAOA (5.6% vs. 2.4% at p=4) but does not eliminate constraint violations due to imperfect state preparation
- [supported] On real hardware (IBM Eagle/Heron), raw feasibility for all QAOA variants is <1%, but LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (e.g., >2% on Eagle) and recovers the optimal solution in several trials
- [supported] Linear-Chain (LC) QAOA achieves the shallowest transpiled circuits (lowest two-qubit gate depth) on heavy-hex topologies, enabling execution at scales where deeper ansätze (e.g., Grover-Mixer) fail to compile or decohere
- [supported] Dynamical decoupling (XpXm) improves hardware performance (e.g., optimal solution rank improved from 235 to 15 on IBM Rensselaer), while heavier error mitigation techniques (e.g., Pauli twirling, ZNE) degrade performance due to increased circuit complexity and sampling noise
- [supported] LC-QAOA with linear-ramp initialization and CVaR objective scales to larger VRP instances (30 qubits, 20 decision variables), reliably recovering the optimal route at depths p>16 on both IBM Eagle and Heron
- [speculative] Hardware-aligned ansätze and structured parameter schedules (e.g., linear-ramp) may enable quantum advantage for combinatorial optimization on near-term devices by prioritizing circuit depth and noise resilience over expressibility
- [speculative] The co-design approach (algorithm, schedule, and compilation) could unlock reliable performance at the edge of current hardware capabilities for practical logistics problems

**Results summary:** The paper presents a hardware-aware co-design of the Quantum Approximate Optimization Algorithm (QAOA) for the Vehicle Routing Problem (VRP), demonstrating that linear-ramp parameter schedules and Linear-Chain (LC) ansätze significantly improve feasibility, solution quality, and noise robustness. In simulations, linear-ramp initialization and constraint-preserving mixers (e.g., Grover-Mixer) outperform standard QAOA in feasibility, but Grover-Mixer and Two-Step QAOA suffer from impractical circuit depths. On real hardware (IBM Eagle/Heron), LC-QAOA achieves the shallowest circuits and highest feasibility (>2%) when combined with dynamical decoupling (XpXm), while heavier error mitigation techniques degrade performance. The approach scales to larger instances (30 qubits), reliably recovering optimal routes at higher depths (p>16) with CVaR optimization. The results emphasize that near-term quantum optimization success hinges on circuit depth, connectivity, and noise resilience rather than formal expressibility.

**Performance claims:**
- 47.6% feasibility for LRI-QAOA vs. ~2% for standard QAOA in noiseless simulations at p=8
- 21% feasibility for Grover-Mixer QAOA at p=8 in simulations
- 5.6% feasibility for Two-Step QAOA vs. 2.4% for standard QAOA at p=4 in simulations
- >2% feasibility for LC-QAOA with XpXm on IBM Eagle hardware (vs. <1% raw feasibility)
- Optimal solution rank improved from 235 to 15 on IBM Rensselaer with XpXm dynamical decoupling
- Two-qubit gate depth >3000 for Grover-Mixer QAOA at p=2 (vs. shallower circuits for LC-QAOA)
- LC-QAOA recovers optimal route at p>16 for 30-qubit VRP instances on IBM Eagle/Heron
## Quantum advantage claim
**Classification:** speculative

The paper demonstrates improved performance of LC-QAOA on near-term hardware for VRP instances, but quantum advantage is not empirically validated. Claims of potential advantage are based on hardware-aligned co-design and scaling to larger instances (30 qubits), but results are from real hardware with limited feasibility (<2%) and no comparison to state-of-the-art classical solvers. The advantage remains speculative until further empirical validation.
## Limitations
- Experiments limited to small VRP instances (single depot, three customer nodes, and two vehicles) due to hardware constraints and simulation feasibility
- Feasibility of solutions on real hardware remains below 1% for all methods at shallow depths, indicating significant noise and error challenges
- Grover-Mixer QAOA and Two-Step QAOA produce deep circuits that exceed error tolerance of current quantum hardware, limiting their practical utility
- Linear-Chain QAOA sacrifices expressiveness by restricting ZZ interactions to nearest neighbors, which may limit performance on problems requiring long-range interactions
- Parameter transfer from simulation to hardware may not fully account for device-specific noise characteristics, potentially affecting performance
- Advanced error mitigation techniques (e.g., Pauli twirling, ZNE, TREX) did not improve results and sometimes degraded performance, suggesting incompatibility with variational optimization
- Study focuses on a specific problem (VRP) and may not generalize to other combinatorial optimization problems with different constraint structures
- [inferred] Lack of comparison with state-of-the-art classical solvers or hybrid quantum-classical approaches for VRP
- [inferred] No exploration of alternative quantum hardware platforms (e.g., trapped ions, photonics) that may offer different noise profiles or connectivity advantages
- [inferred] Limited discussion on the economic or computational trade-offs between quantum and classical approaches for VRP
- [inferred] Preprint status implies lack of peer review, which may affect the robustness of conclusions
## Open questions
- How does the performance of LC-QAOA scale with larger and more complex VRP instances (e.g., more vehicles, time windows, or dynamic routing)?
- What is the impact of different noise profiles (e.g., crosstalk, gate errors) on the feasibility and solution quality of QAOA variants?
- Can hybrid quantum-classical approaches (e.g., combining QAOA with classical repair heuristics) improve feasibility and solution quality for VRP?
- How do alternative quantum hardware platforms (e.g., trapped ions, neutral atoms) compare to superconducting qubits for implementing QAOA variants?
- What are the limits of parameter transferability from simulation to hardware, and how can this process be optimized for different devices?
- How does the choice of CVaR parameter (α) affect the trade-off between solution quality and optimization stability across different problem sizes?
- Can adaptive ansätze (e.g., ADAPT-QAOA) be combined with hardware-aware designs like LC-QAOA to improve performance without increasing circuit depth?
- What are the long-term prospects for QAOA in financial services, given the current limitations in hardware and algorithmic performance?

**Future work:**
- Test LC-QAOA and linear-ramp schedules on larger VRP instances (e.g., 10+ nodes) to assess scalability
- Explore hybrid quantum-classical approaches that combine QAOA with classical post-processing or pre-processing techniques
- Investigate the performance of QAOA variants on alternative quantum hardware platforms with different noise characteristics and connectivity
- Develop noise-aware parameter optimization techniques that account for device-specific error profiles during simulation
- Extend the study to other combinatorial optimization problems in financial services (e.g., portfolio optimization, risk analysis) to assess generalizability
- Combine LC-QAOA with adaptive ansätze or multi-level QAOA to balance expressiveness and hardware efficiency
- Optimize the CVaR parameter (α) for different problem sizes and noise levels to improve solution quality and optimization stability
- Benchmark QAOA variants against state-of-the-art classical solvers to quantify quantum advantage in practical scenarios
- Investigate the use of machine learning techniques to automate the selection of QAOA variants and parameter schedules for specific problem instances
- Explore the integration of error mitigation techniques that are compatible with variational optimization, such as noise-adaptive training
## Key ideas
- #idea:near-term-feasibility — Hardware-aware QAOA variants (e.g., Linear-Chain QAOA) reduce circuit depth and improve noise robustness, making them viable for near-term quantum devices
- #idea:hybrid-approach — Co-design strategies combining classical optimization (e.g., COBYQA, CVaR) with quantum algorithms enhance solution quality and feasibility for VRP
- #idea:quantum-advantage — Speculative claim that hardware-aligned ansätze and structured schedules may enable quantum advantage for combinatorial optimization, though not empirically validated
- #limitation:noise — Feasibility on real hardware remains below 1% for all QAOA variants, highlighting noise as a critical barrier
- #limitation:qubit-count — Study limited to small VRP instances (3 customer nodes, 2 vehicles) due to hardware constraints, raising scalability concerns
- #limitation:data-encoding — Linear-Chain QAOA sacrifices expressiveness by restricting ZZ interactions to nearest neighbors, potentially limiting performance on problems requiring long-range interactions
## Contradictions
- #contradiction:scalability — Paper claims LC-QAOA scales to larger VRP instances (30 qubits) on IBM hardware, but feasibility remains low (<2%), contradicting implied scalability advantages. No comparison to classical solvers is provided to validate claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
