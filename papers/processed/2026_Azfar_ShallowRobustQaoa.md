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
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.21203/rs.3.rs-8297477/v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Research Square
methodology_tags:
- QAOA
- grover
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:13:13.550995'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:13:18.494406'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:14:00.686787'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:14:53.321382'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:15:24.096685'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:15:31.858924'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/QAOA
- method/grover
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Shallow and Robust QAOA: Improving Feasibility and Hardware Performance via
  Linear-Chain and Ramp Schedules'
topic_tags: []
year: 2026
zotero_key: ''
---

## Abstract summary
The paper studies several variants of the Quantum Approximate Optimization Algorithm (QAOA) for solving vehicle routing problems, with a focus on making them more feasible and robust on current superconducting quantum hardware. It introduces a hardware-aware linear-chain ansatz and linear-ramp parameter schedules, and compares these against standard, two-step, and Grover-mixer QAOA across ideal simulation, noisy simulation, and IBM Eagle/Heron devices. The authors show that structured schedules and shallow, connectivity-aligned circuits improve feasibility, noise robustness, and scalability, especially when combined with simple dynamical decoupling and CVaR-based objective functions.
## Methodology
This preprint reports an empirical benchmark study of five QAOA-based variants for solving small vehicle routing problem (VRP) instances under a hardware-aware algorithm-design framework. The authors formulate VRP as a binary optimization problem over directed edges, convert constraints into quadratic penalties to obtain a QUBO, normalize coefficients, and map the QUBO to an Ising Hamiltonian. They compare Standard QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp-Initialized QAOA (LRI-QAOA), and Linear-Chain QAOA (LC-QAOA). Experiments are implemented in Qiskit SDK 2.1.1 using Qiskit Runtime, with DOcplex models converted to QuadraticProgram and then to SparsePauliOp Hamiltonians via Qiskit optimization tools. Parameters are optimized with the derivative-free COBYQA optimizer to minimize the expectation of the VRP cost Hamiltonian using EstimatorV2, and final solution statistics are obtained from SamplerV2 with 10,000 shots. The study evaluates methods across statevector simulation, Aer shot-based simulation, and real IBM superconducting hardware (IBM Eagle/Rensselaer and IBM Heron/Fez), measuring feasibility of sampled routes, rank of the optimal solution among sampled bitstrings, runtime/iterations, and transpiled two-qubit gate depth. Additional methodology includes parameter transfer from simulation to hardware, linear-ramp schedules for initialization, a nearest-neighbor linear-chain filtering of ZZ interactions to reduce routing overhead, Dicke-state preparation for Grover-mixer variants, and tests of error suppression/mitigation including dynamical decoupling (XX, XpXm, XY), Pauli twirling, TREX, ZNE, and CVaR-based optimization for larger instances.

**Algorithms used:** QAOA, Two-Step QAOA, Grover-Mixer QAOA, Linear-Ramp-Initialized QAOA, Linear-Chain QAOA, CVaR
**Frameworks:** Qiskit, Qiskit Runtime, Qiskit Optimization, DOcplex, CPLEX

**Experimental setup:** Experiments were run in three settings: ideal statevector simulation, shot-based Aer simulation, and real IBM quantum hardware. The workflow used DOcplex to define VRP instances, Qiskit Optimization to convert them to QuadraticProgram and Ising form, SparsePauliOp for Hamiltonian representation, EstimatorV2 for expectation estimation during optimization, and SamplerV2 for final sampling. Each optimized parameter set was evaluated with 10,000 shots. Hardware experiments were conducted on IBM Rensselaer (Eagle) and IBM Fez (Heron), with transpilation to heavy-hex topologies and tests of dynamical decoupling and other mitigation methods.

**Dataset:** Synthetic VRP instances generated from randomly distributed customer locations on a 2D Euclidean plane. The main benchmark instance contains 1 depot, 3 customer nodes, and 2 vehicles; a larger scaling instance contains 5 nodes and 2 vehicles requiring 30 qubits (20 decision variables and 10 slack variables). Edge weights are computed as squared Euclidean distances.
## Findings
- [supported] In noiseless statevector simulations on a small VRP instance, linear-ramp initialized QAOA (LRI-QAOA) achieved the highest feasibility among tested variants, reaching 47.6% feasible samples at p=8 versus 2.4% for standard QAOA, 4.43% for Two-Step QAOA, 21.38% for GM-QAOA, and 2.86% for LC-QAOA.
- [supported] In statevector simulation at p=4, LRI-QAOA achieved 25.54% feasibility versus 2.4% for standard QAOA, 5.6% for Two-Step QAOA, 10.72% for GM-QAOA, and 3.94% for LC-QAOA.
- [supported] In Aer shot-based simulation, LRI-QAOA outperformed standard QAOA in feasibility at p=4 (6.47% vs 2.77%) and p=8 (1.68% vs 1.5%), while GM-QAOA was best at p=8 with 6.7% feasibility.
- [supported] Shot noise substantially reduced feasibility relative to statevector simulation; for example, LRI-QAOA dropped from 47.6% feasible in statevector simulation to 1.68% on Aer at p=8.
- [supported] GM-QAOA improved feasibility in simulation but incurred very large circuit depth; the paper reports two-qubit gate depth above 3000 even at p=2 and transpilation failure for p>5.
- [supported] LC-QAOA produced the shallowest transpiled two-qubit circuits among compared methods on IBM hardware, due to restricting ZZ interactions to nearest neighbors and reducing swap overhead.
- [supported] The paper reports that ramp-initialized standard QAOA at p=4 could match or outperform randomly initialized standard QAOA at p=6 on hardware in solution quality, implying lower depth can suffice with structured initialization.
- [supported] On real IBM Eagle and Heron hardware, raw feasibility remained below 1% for shallow-depth implementations across methods, indicating strong degradation from noise and limited connectivity.
- [supported] LC-QAOA combined with XpXm dynamical decoupling achieved hardware feasibility above 2% on IBM Eagle according to the text, outperforming deeper alternatives under noise.
- [supported] Dynamical decoupling improved hardware performance: on IBM Fez at p=4, feasibility increased from 1.14% with XX decoupling to 1.60% with XpXm, and the optimal solution rank improved from 16 to 6.
- [supported] On IBM Rensselaer at p=4, XpXm dynamical decoupling improved the optimal solution rank from 235 with XX decoupling to 15, while feasibility rose from 0.69% to 0.80%.
- [supported] Heavy mitigation stacks did not outperform simple dynamical decoupling on hardware; on IBM Fez at p=4, XpXm alone gave 1.80% feasibility, while XpXm plus Pauli twirling, TREX, and ZNE reduced feasibility to 0.60%.
- [supported] For a larger 30-qubit VRP instance (5 nodes, 2 vehicles), LC-QAOA with linear-ramp initialization remained compilable while other variants were reported as not reliably executable on hardware.
- [supported] On the 30-qubit instance, LC-QAOA recovered the optimal route on hardware at higher depth: the correct solution appeared at p=19 on IBM Rensselaer and p=18 on IBM Fez, though with low absolute feasibility.
- [supported] CVaR improved large-instance hardware performance in several settings; for example, on IBM Rensselaer at p=18 feasibility increased from 0.3% to 4.95%, and on IBM Fez at p=18 from 0.5% to 4.72%.
- [speculative] The authors argue that hardware-aligned ansatz design and structured schedules provide a practical path for near-term quantum optimization in routing problems, but this is based on small-scale experiments with low absolute feasibility.
- [speculative] The paper suggests that expressibility is not the main bottleneck on current hardware and that compiled two-qubit depth, connectivity, and noise resilience dominate performance.
- [speculative] The authors imply that LC-QAOA with linear-ramp initialization and lightweight decoupling offers a scalable and reproducible route toward larger logistics problems, but this has not been demonstrated beyond small and modest benchmark instances.
- [speculative] Claims of improved scaling from LC-QAOA are preliminary because the evidence is limited to selected small VRP instances and one 30-qubit case, without a demonstrated end-to-end quantum advantage over classical solvers.

**Results summary:** This preprint benchmarks five QAOA variants for small vehicle routing problems across statevector simulation, Aer shot-based simulation, and IBM Eagle/Heron hardware. In simulation, linear-ramp initialization substantially improved feasibility over standard QAOA, while GM-QAOA also improved feasibility but at the cost of extremely deep circuits. LC-QAOA did not show major low-depth simulation gains but consistently produced the shallowest transpiled circuits, which translated into better robustness on hardware. On real devices, all methods suffered severe noise, with raw feasibility generally below 1% at shallow depths; however, XpXm dynamical decoupling improved feasibility and optimal-solution rank, and heavy mitigation stacks underperformed simple decoupling. For a larger 30-qubit VRP instance, LC-QAOA with linear-ramp initialization remained compilable and recovered the optimal route at high depth on both IBM backends, with CVaR further improving feasibility in several runs. Because this is a preprint and results are limited to small-scale benchmarks with low absolute success rates, any broader quantum advantage implications remain speculative.

**Performance claims:**
- Statevector, p=8: feasibility = 2.4% (QAOA), 4.43% (Two-Step), 21.38% (GM-QAOA), 47.6% (LRI-QAOA), 2.86% (LC-QAOA)
- Statevector, p=6: feasibility = 15.4% (QAOA), 0.94% (Two-Step), 16.33% (GM-QAOA), 17.11% (LRI-QAOA), 0.67% (LC-QAOA)
- Statevector, p=4: feasibility = 2.4% (QAOA), 5.6% (Two-Step), 10.72% (GM-QAOA), 25.54% (LRI-QAOA), 3.94% (LC-QAOA)
- Aer, p=8: feasibility = 1.5% (QAOA), 0.13% (Two-Step), 6.7% (GM-QAOA), 1.68% (LRI-QAOA), 1.25% (LC-QAOA)
- Aer, p=6: feasibility = 3.76% (QAOA), 0.29% (Two-Step), 1.79% (GM-QAOA), 3.2% (LRI-QAOA), 2.34% (LC-QAOA)
- Aer, p=4: feasibility = 2.77% (QAOA), 0.4% (Two-Step), 3.71% (GM-QAOA), 6.47% (LRI-QAOA), 1.57% (LC-QAOA)
- GM-QAOA two-qubit gate depth exceeds 3000 at p=2; transpilation fails for p>5
- IBM Fez, p=4: XX decoupling gives rank 16 and 1.14% feasibility; XpXm gives rank 6 and 1.60% feasibility; XY4 gives rank 133 and 1.42% feasibility
- IBM Rensselaer, p=4: XX decoupling gives rank 235 and 0.69% feasibility; XpXm gives rank 15 and 0.80% feasibility; XY4 gives rank 1478 and 0.40% feasibility
- IBM Fez, mitigation study at p=4: no mitigation 1.51% feasibility, XpXm 1.80%, XpXm+Pauli twirling 1.24%, XpXm+ZNE 1.34%, XpXm+Pauli twirling+TREX 0.87%, XpXm+Pauli twirling+TREX+ZNE 0.60%
- 30-qubit instance, IBM Rensselaer: without CVaR feasibility = 0.2% (p=17), 0.3% (p=18), 0.2% (p=19), 0.5% (p=20); with CVaR = 3.0%, 4.95%, 0.4%, 2.97%
- 30-qubit instance, IBM Fez: without CVaR feasibility = 0.2% (p=17), 0.5% (p=18), 0.37% (p=19), 0.6% (p=20); with CVaR = 1.98%, 4.72%, 2.94%, 2.88%
- 30-qubit instance: optimal route appears at rank 2759 on IBM Rensselaer at p=19 and rank 1169 on IBM Fez at p=18; with CVaR, rank improves to 191 on IBM Rensselaer at p=19 and 38 on IBM Fez at p=20
## Quantum advantage claim
**Classification:** speculative

The paper reports improved feasibility, circuit depth, and hardware robustness for LC-QAOA, linear-ramp initialization, dynamical decoupling, and CVaR on small VRP instances and one 30-qubit case, including real IBM hardware runs. However, absolute feasibility remains low, no classical runtime or quality advantage is demonstrated against strong classical baselines, and as a preprint any broader advantage claims should be treated as speculative.
## Limitations
- Lack of peer review: this is a preprint and the findings have not yet undergone formal peer review.
- Absolute feasibility on current hardware remains very low; the paper states that raw hardware feasibility is well below 1% for all methods at shallow depths, and even improved runs remain only around a few percent.
- Recovery of the optimal route is probabilistic rather than reliable or deterministic.
- Experiments use purposefully modest VRP instances to permit repeated sampling and controlled comparisons, limiting conclusions about larger real-world problems.
- The main benchmark instance is very small (single depot, three customers, two vehicles), which constrains external validity.
- More realistic VRP variants are excluded; the formulation assumes no time windows and does not include capacities in the main experiments.
- Results depend heavily on backend calibration and qubit mapping; the authors note that device-specific variability can change the optimal depth and the benefit of decoupling.
- Grover-Mixer QAOA and Two-Step QAOA are hampered in practice by very deep circuits, limiting their usability on current hardware.
- GM-QAOA circuits become extremely deep (two-qubit depth over 3000 even at p = 2), and transpilation fails for GM- and SDGM-QAOA for p > 5.
- Linear-Chain QAOA reduces depth by discarding nonadjacent ZZ interactions, but this comes at the cost of reduced expressiveness and ignoring some problem correlations.
- Linear-ramp initialization was less effective directly on hardware than in simulation, likely due to device noise and calibration variability.
- Advanced mitigation stacks such as Pauli twirling, TREX, and ZNE did not improve results in this study and sometimes worsened feasibility, limiting the effectiveness of post-processing mitigation for this setting.
- The larger 30-qubit experiment still exhibits low absolute feasibility despite occasional recovery of the optimal route.
- Constraint handling remains imperfect: Two-Step QAOA did not always remain strictly in the feasible manifold, suggesting leakage or imperfect intermediate state preparation.
- Grover-mixer feasibility guarantees are only partial in this encoding: fixed Hamming weight increases the chance of feasibility, but does not guarantee full VRP feasibility.
- The study focuses on one problem family (VRP), so conclusions may not generalize to other combinatorial optimization problems or financial optimization tasks.
- [inferred] The use of randomly generated small Euclidean instances rather than operational routing datasets limits ecological validity.
- [inferred] No direct comparison is provided against strong classical heuristics or exact/approximate routing baselines beyond using CPLEX only to certify optimality, so practical quantum advantage is not established.
- [inferred] Reported hardware success may be sensitive to the chosen IBM backends and may not transfer to other hardware platforms or architectures.
- [inferred] The optimizer choice (COBYQA) is fixed, and sensitivity to optimizer selection or hyperparameters is not systematically studied.
- [inferred] The penalty parameter is chosen via heuristic scaling, so results may depend on penalty tuning and may not be robust across instances.
- [inferred] Sampling with 10,000 shots may still leave substantial statistical uncertainty for very low-feasibility events.
- [inferred] Although code and data are shared, reproducibility on hardware may be limited because calibrations drift over time and hardware access conditions change.
- [inferred] The claim of scalability is limited because the demonstrated larger case is still only a 5-node, 2-vehicle instance and remains far from industrial-scale routing.
## Open questions
- How well do linear-ramp schedules and LC-QAOA generalize to larger and more realistic VRP instances with capacities, time windows, and multi-objective costs?
- At what problem sizes, if any, does the depth-versus-expressibility trade-off of LC-QAOA become preferable to more expressive ansatzes?
- How much useful problem structure is lost by removing nonadjacent ZZ interactions in LC-QAOA, and when does that loss begin to dominate the hardware benefits?
- Can feasibility be increased substantially on real hardware, or is low feasibility an inherent bottleneck for penalty-based QAOA on current devices?
- Why does linear-ramp initialization transfer well in simulation but less reliably on hardware, and how can this transfer gap be reduced?
- What mechanisms cause Two-Step QAOA to leak outside the feasible manifold in practice?
- Under what conditions can Grover-mixer or Dicke-state-based approaches become practical on hardware despite their circuit depth overhead?
- How should CVaR level alpha be selected systematically as a function of hardware noise and sampling variance?
- How transferable are learned schedules and parameters across instances, depths, devices, and calibration states?
- What is the best way to co-optimize qubit placement, chain orientation, and dynamical decoupling timing for a given backend?
- How robust are the reported gains to different classical optimizers, initialization schemes, and transpilation settings?
- How do these QAOA variants compare against VQE-style ansatzes, annealing approaches, and constrained quadratic model baselines on the same instances?
- [inferred] Would the observed benefits persist on non-IBM hardware or on architectures with different connectivity and native gate sets?
- [inferred] Is the low hardware feasibility primarily due to noise, the penalty encoding, barren/rough optimization landscapes, or all three together?
- [inferred] Can the approach deliver any practical runtime or quality advantage over state-of-the-art classical routing heuristics on realistic workloads?

**Future work:**
- Incorporate more realistic routing constraints, including capacities, time windows, and multi-objective costs such as emissions.
- Benchmark alternative encodings that better balance qubit count against feasibility guarantees.
- Study adaptive schedule families that respond to measured on-device gradients.
- Quantify cross-instance parameter transfer at fixed circuit depth.
- Co-optimize hardware-aware compilation choices, including qubit placement, chain orientation, and dynamical decoupling timing.
- Perform comparative studies against VQE-style problem-inspired ansatzes on the same instances.
- Perform comparative studies against annealing and constrained quadratic model baselines on the same instances.
- Develop hybrid workflows that use classical heuristics for decomposition or warm starts, apply LC-QAOA with linear-ramp initialization to subproblems, and combine solutions classically.
- Extend scaling studies to larger and more constrained logistics tasks as hardware and compilers improve.
- [inferred] Evaluate the methods on real operational datasets rather than only small randomly generated Euclidean instances.
- [inferred] Add stronger classical baseline comparisons to assess whether hardware-aware QAOA offers any practical advantage.
- [inferred] Investigate alternative penalty-setting strategies or constraint-preserving encodings to improve feasibility.
- [inferred] Test robustness across more hardware backends, calibration snapshots, and transpilation pipelines.
- [inferred] Explore optimizer ablations and hyperparameter sensitivity analyses to determine whether performance gains are optimizer-dependent.
## Key ideas
- #idea:near-term-feasibility — Hardware-aware QAOA design, especially linear-chain ansatzes and linear-ramp initialization, reduces transpiled depth and improves robustness on current IBM superconducting devices.
- #idea:hybrid-approach — Practical performance depends on hybrid quantum-classical workflow elements such as COBYQA parameter optimization, parameter transfer from simulation to hardware, and CVaR-based objectives.
- #idea:near-term-feasibility — Simple dynamical decoupling (especially XpXm) improved feasibility and optimal-solution rank more consistently than heavier mitigation stacks on hardware.
- #idea:quantum-advantage — The paper speculates that hardware-aligned ansatz design could support useful quantum optimization, but does not demonstrate end-to-end advantage over classical methods.
- #idea:near-term-feasibility — LC-QAOA remained compilable for a 30-qubit VRP instance when more expressive variants became too deep or failed transpilation, suggesting a hardware-driven path to somewhat larger instances.
## Contradictions
- The paper suggests improved scalability via LC-QAOA, but the evidence is limited to very small VRP benchmarks and one 30-qubit case with low absolute feasibility, supporting #contradiction:scalability.
- Any implied quantum superiority is contradicted by the absence of strong classical baseline comparisons and by the paper's own statement that no practical runtime or quality advantage over classical solvers is established, supporting #contradiction:classical-vs-quantum.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input consists of synthetic vehicle routing problem instances rather than a standard dataset. The representative benchmark instance has a single depot, 3 customer nodes, and 2 vehicles. Customer coordinates are randomly generated in a 2D Euclidean plane, and pairwise edge weights are computed as squared Euclidean distances. The resulting complete graph is encoded as a QUBO with routing cost, flow conservation, depot constraints, and subtour elimination penalties. A larger instance with 5 nodes and 2 vehicles uses 30 qubits total, comprising 20 decision variables and 10 slack variables. QUBO penalty weight is set globally as lambda = 2 * sum_{i!=j} |w_ij|, and coefficients are normalized by the largest-magnitude term.

### Process
1. Formulate VRP as a binary directed-edge optimization model in DOcplex. 2. Convert constraints into quadratic penalties to obtain a QUBO, then map the QUBO to an Ising Hamiltonian. 3. For standard QAOA and LRI-QAOA, build layered cost/mixer circuits from the Ising Hamiltonian. 4. For Two-Step QAOA, separate cost and constraint Hamiltonians; first optimize a QAOA stage on the constraint Hamiltonian to prepare an approximately feasible state, then freeze those parameters and run a second QAOA stage on the cost Hamiltonian with a feasibility-preserving mixer. 5. For Grover-Mixer QAOA, prepare a Dicke state of fixed Hamming weight and use a Grover-like mixer to preserve that subspace. 6. For LC-QAOA, remove nonadjacent ZZ Pauli terms so only nearest-neighbor interactions remain. 7. Optimize variational parameters using COBYQA with EstimatorV2 to minimize expected cost. 8. For linear-ramp initialization, initialize parameters according to beta_i = (1 - i/p) * Delta_beta and gamma_i = ((i + 1)/p) * Delta_gamma; in some hardware runs, transfer optimized parameters from Aer simulation and optionally warm-start further tuning. 9. Sample each optimized circuit with 10,000 shots using SamplerV2. 10. Evaluate feasibility percentage, rank of the optimal bitstring, runtime, iteration count, and transpiled two-qubit depth. 11. On hardware, test dynamical decoupling sequences (XX, XpXm, XY) and combinations with Pauli twirling, TREX, and ZNE. 12. For larger LC-QAOA instances, also optimize using a CVaR objective to bias toward low-cost tails of the sampled distribution.

### Output
Reported outputs include percentage of feasible sampled solutions, rank position of the known optimal route among sampled bitstrings sorted by frequency, wall-clock solution time, optimizer iteration count, and transpiled two-qubit gate depth. Comparisons are made across QAOA variants, simulation backends, and hardware backends. Classical CPLEX is used to certify the optimal solution for each VRP instance, serving as a correctness baseline rather than a runtime baseline. Hardware mitigation experiments compare solution rank and feasibility under different decoupling and mitigation settings. Larger-instance experiments report rank and feasibility with and without CVaR.

### Parameters
- shots: 10000
- optimizer: COBYQA
- framework_version: Qiskit SDK 2.1.1
- benchmark_depths_p: [4, 6, 8]
- larger_instance_depths_p: [17, 18, 19, 20]
- main_instance_qubits: approximately 12-14 qubits mentioned for small hardware circuits
- larger_instance_qubits: 30
- larger_instance_decision_variables: 20
- larger_instance_slack_variables: 10
- penalty_weight: lambda = 2 * sum_{i!=j} |w_ij|
- linear_ramp_schedule: {'beta_i': '(1 - i/p) * Delta_beta', 'gamma_i': '((i + 1)/p) * Delta_gamma'}
- dynamical_decoupling_sequences_tested: ['XX', 'XpXm', 'XY4']
- error_mitigation_tested: ['Pauli twirling', 'TREX', 'ZNE']

### Hardware
Real-device experiments were run on IBM Rensselaer (Eagle processor) and IBM Fez (Heron processor) through Qiskit Runtime. The paper also references ideal simulation and Aer shot-based simulation. Circuits were transpiled to IBM heavy-hex topologies; LC-QAOA was specifically designed to reduce swap insertion by restricting ZZ couplings to nearest neighbors. The authors note Fez benefits from lower two-qubit error rates and native RZZ implementation. Error suppression and mitigation tested on hardware include dynamical decoupling sequences XX, XpXm, and XY4, plus Pauli twirling, TREX, and zero-noise extrapolation.

### Reproducibility
Preprint. Code and generated data are reported as publicly available at the provided GitHub repository (https://github.com/TalhaAzfar/LC_LRI_QAOA). The paper gives substantial implementation detail on formulation, software stack, optimizer, shot count, hardware backends, and evaluation metrics, making replication reasonably feasible, though some low-level settings such as exact transpilation options, optimizer stopping criteria, and full instance-generation seeds are not fully specified.
