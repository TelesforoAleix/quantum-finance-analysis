---
aliases:
- 'Rasengan: A Transition Hamiltonian-based Approximation Algorithm for Solving Constrained
  Binary Optimization Problems'
- Rasengan Transition Hamiltonian based
authors:
- Qifan Jiang
- Liqiang Lu
- Debin Xiang
- Tianyao Chu
- Tianze Zhu
- Jingwen Leng
- Yun Liang
- Xiaoming Sun
- Jianwei Yin
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1145/3725843.3756107
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 58th IEEE/ACM International Symposium on Microarchitecture (MICRO
  ’25)
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:10:01.542254'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:10:06.122301'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:11:05.363121'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:11:37.265806'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:12:00.121141'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:12:10.616168'
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
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Rasengan: A Transition Hamiltonian-based Approximation Algorithm for Solving
  Constrained Binary Optimization Problems'
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces Rasengan, a variational quantum algorithm tailored for constrained binary optimization that uses a specially designed transition Hamiltonian to expand the search space from a single feasible solution while remaining within the feasible region. The authors combine this with three implementation optimizations—Hamiltonian simplification and pruning, segmented execution, and constraint-based purification—to reduce circuit depth and mitigate noise, making the approach deployable on current NISQ hardware. They evaluate Rasengan on multiple benchmark problems and both simulators and IBM quantum devices, showing substantially improved approximation quality and reduced depth compared to HEA- and QAOA-based baselines.
## Methodology
This conference paper presents Rasengan, a variational quantum algorithm for constrained binary optimization based on a newly defined transition Hamiltonian. Methodologically, the work is both theoretical and empirical: it formulates a transition-Hamiltonian framework that expands the feasible solution space starting from one precomputed feasible solution using homogeneous basis vectors of the linear constraint system, proves coverage guarantees for feasible solutions under stated assumptions (including a theorem giving m^2 or m^3 upper bounds on transition simulations), and then implements the approach as a parameterized quantum circuit. The circuit sequentially applies transition-Hamiltonian simulations, with optimization of evolution-time parameters via a classical constrained optimization by linear approximation method. To improve deployability on NISQ hardware, the authors introduce three algorithm-hardware co-design optimizations: Hamiltonian simplification via basis transformation to reduce nonzero entries, Hamiltonian pruning to remove redundant transitions that do not expand the feasible space, and segmented execution with probability-preserving handoff between segments plus purification-based error mitigation that removes infeasible intermediate outputs. Empirically, the method is evaluated against HEA, penalty-term-based QAOA, and commute-Hamiltonian-based QAOA (Choco-Q) on 2000 benchmark instances spanning five constrained optimization domains relevant to practical applications, using both noise-free simulation and real IBM quantum devices. Reported outcomes include approximation ratio gap, circuit depth, parameter count, in-constraints rate, latency, scalability, noise sensitivity, and ablation studies. The paper appears to be a full conference paper rather than a short paper or workshop paper.

**Algorithms used:** Rasengan, QAOA, HEA, P-QAOA, Choco-Q
**Frameworks:** Qiskit, DDSim, CUDA Quantum, qiskit-aer-gpu, Jupyter, Python

**Experimental setup:** Experiments include noise-free simulation, noisy simulation, and execution on real IBM Quantum hardware. The classical part and simulation experiments were run on an AMD EPYC 9554 64-core server with 1 TB RAM; the artifact appendix also mentions dual AMD EPYC 9554 CPUs and optional NVIDIA H100 GPU, while baseline simulations using RX-heavy circuits were accelerated on one NVIDIA A100 GPU via CUDA Quantum. Rasengan circuits were simulated with DDSim; artifact materials also state Qiskit-based circuit simulation and optional qiskit-aer-gpu backend. Real-device evaluations were conducted on IBM Kyiv and IBM Brisbane 127-qubit Eagle r3 systems. For algorithmic evaluation, baselines HEA, P-QAOA, and Choco-Q used 5 repeated layers, and parameter optimization was run for up to 300 iterations; large-scale FLP scalability experiments used up to 1000 iterations; real-device runs used up to 100 iterations due to hardware cost. Segmented execution was used to reduce circuit depth to deployable levels, with 1024 shots per segment in one overhead study and dynamic shot allocation between segments based on measured probabilities.

**Dataset:** Synthetic/benchmark constrained binary optimization instances compiled from prior literature across five application domains: facility location problem (FLP), k-partition problem (KPP), job scheduling problem (JSP), set cover problem (SCP), and graph coloring problem (GCP). The main evaluation uses 400 cases per benchmark family from relevant literature, totaling 2000 cases across five domains and 20 benchmark scales. Additional large-scale FLP instances with 6 to 105 variables are used for scalability analysis.
## Findings
- [supported] Rasengan proposes a transition-Hamiltonian-based variational algorithm that expands the search space from one feasible solution rather than shrinking from a global superposition, aiming to stay within the feasible solution space throughout evolution.
- [speculative] The transition Hamiltonian is claimed to exponentially explore the feasible solution space using combinations of homogeneous basis vectors.
- [speculative] Theorem 1 claims that for totally unimodular constraint matrices, repeating m transition Hamiltonians for m rounds (m^2 total simulations) can cover all feasible solutions, with an upper bound of m^3 for more complex cases.
- [speculative] The transition operator is claimed to have linear decomposition complexity in the number of nonzero elements of the homogeneous basis vector, with 34k CX gates where k is the number of nonzero entries.
- [supported] The authors introduce three implementation optimizations—Hamiltonian simplification and pruning, segmented execution, and purification-based error mitigation—to reduce circuit depth and improve deployability on NISQ hardware.
- [supported] Across 2000 benchmark cases from five domains, Rasengan improves approximation-ratio-gap accuracy by 4.12x versus the strongest baseline Choco-Q and by much larger margins versus HEA and penalty-QAOA.
- [supported] In noise-free evaluation over 20 benchmarks, Rasengan achieves the lowest ARG among compared methods, including values such as 0.01 on F1, 0.07 on K1, and 0.01 on J1.
- [supported] Rasengan reduces circuit depth by 1.96x to 49.0x relative to baselines across the benchmark suite, with examples such as depth 58 on F4 versus 3848 for Choco-Q.
- [supported] Rasengan reduces circuit depth from about 7000 to about 50 after optimization, making the authors' implementation deployable on current quantum platforms.
- [supported] Hamiltonian simplification and pruning plus segmented execution reduce circuit depth by over 94.6% in the reported experiments.
- [supported] On IBM Kyiv and IBM Brisbane hardware, Rasengan is reported as the first tested quantum algorithm in this study to beat the mean quality of the feasible-solution baseline, with a reported 379x improvement in ARG over prior methods.
- [supported] Rasengan achieves a 100% in-constraints rate on real hardware in the reported experiments due to purification-based error mitigation, whereas Choco-Q drops far below its theoretical constraint-preservation guarantee under noise.
- [supported] The purification-based error mitigation improves accuracy by more than 303x on hardware in the ablation study.
- [supported] Segmented execution lowers effective per-segment circuit depth to that of a single transition Hamiltonian simulation, enabling execution on NISQ devices while preserving probability information between segments.
- [supported] In large-scale facility-location simulations, Rasengan attains ARG below 0.5 on a 78-qubit instance, while the paper reports Choco-Q exceeding 0.5 ARG on a 28-qubit instance.
- [supported] Under simulated depolarizing noise, more than 99% of Rasengan runs have ARG below 0.025 at a Pauli error rate of 1e-4, and mean ARG remains below 0.15 at error rate 0.001.
- [supported] Under amplitude damping noise, Rasengan remains effective up to moderate damping levels, but when damping reaches 2%, segmented execution can fail because no feasible intermediate state remains for the next segment.
- [speculative] The paper argues Rasengan has a higher probability of evolving to the optimal basis state than HEA or QAOA because it can tune transition times toward a basis-state optimum rather than ending in a superposition containing poor solutions.
- [speculative] The paper suggests the expansion-based design offers better scalability than prior VQAs for constrained binary optimization.

**Results summary:** This conference paper introduces Rasengan, a transition-Hamiltonian-based variational quantum algorithm for constrained binary optimization. The method starts from one feasible solution and expands within the feasible subspace using transition Hamiltonians derived from homogeneous basis vectors, rather than shrinking from a superposition over all states as in HEA or QAOA-style methods. The paper provides a theoretical coverage claim for feasible solutions under repeated transition simulations and proposes three practical optimizations: Hamiltonian simplification/pruning, segmented execution, and purification-based error mitigation. Empirically, results are reported from both simulation and real IBM hardware. In noise-free experiments over 2000 cases from five application domains, Rasengan achieves the best approximation-ratio-gap and the shallowest circuits among compared methods, with a reported 4.12x ARG improvement over Choco-Q and up to 49.0x lower circuit depth. On IBM Kyiv and Brisbane, Rasengan reportedly outperforms prior methods by 379x in ARG and achieves 100% in-constraints rate via purification. The paper does not demonstrate a general quantum speedup over classical optimization; instead it shows improved performance relative to prior quantum heuristics, with both theoretical and empirical claims depending on simulation and small-scale hardware tests.

**Performance claims:**
- 4.12x ARG improvement over Choco-Q across 2000 cases from five domains
- 1954x ARG improvement over HEA across the benchmark suite
- 1897x ARG improvement over penalty-QAOA across the benchmark suite
- 379x improvement on real-world quantum platforms versus prior methods
- Circuit depth reduced from ~7000 to ~50 after optimization
- Over 94.6% circuit-depth reduction from Hamiltonian simplification/pruning and segmented execution
- 1.96x to 49.0x lower circuit depth than baselines across 20 benchmarks
- Example: F4 circuit depth 58 for Rasengan versus 3848 for Choco-Q
- Example ARGs: F1 0.01, K1 0.07, J1 0.01 for Rasengan
- 100% in-constraints rate on IBM Kyiv and IBM Brisbane for Rasengan
- 12.2x improvement in in-constraints rate over baselines on less noisy hardware
- 303x accuracy improvement from purification-based error mitigation in ablation
- Hamiltonian simplification, pruning, and segmented execution reduce circuit depth by 9.8%, 67%, and 82%, respectively, in ablation
- Opt 2 improves ARG by 1.18x on simulators and 1.37x on hardware in ablation
- Opt 3 improves ARG by 2.43x in ablation
- Purification overhead is 0.05 ms versus ~700 ms classical training time per iteration for a 24-variable graph coloring problem
- For depolarizing noise at Pauli error rate 1e-4, >99% of ARGs are below 0.025
- At Pauli error rate 0.001, average ARG remains below 0.15
- Rasengan achieves ARG < 0.5 on a 78-qubit FLP simulation, while Choco-Q is reported with ARG > 0.5 on a 28-qubit problem
- Compared with Choco-Q, Rasengan reduces total training time by 1.73x
## Quantum advantage claim
**Classification:** theoretical

The paper makes theoretical claims about exponential exploration of the feasible solution space and improved expressivity relative to prior VQAs, but it does not demonstrate a clear quantum advantage over classical algorithms. Empirical results compare against other quantum heuristics using simulation and small-scale IBM hardware rather than establishing end-to-end quantum advantage.
## Limitations
- Performance on noisy hardware degrades as problem size increases; when the problem size exceeds 28 qubits in noisy simulation, some segments fail to produce feasible solutions, causing optimization to terminate early.
- Real-hardware evaluation is limited to small-scale instances (F1, K1, J1) because baseline circuit depths and device decoherence times prevent larger deployments.
- Theoretical coverage guarantees depend on structural assumptions about the constraint matrix; Theorem 1 gives stronger guarantees for totally unimodular matrices and only an upper bound for more complex cases.
- Rasengan requires one feasible solution to be pre-calculated before quantum evolution, so applicability depends on the availability of an efficient feasible-state initialization procedure.
- The method is specialized to constrained binary optimization with linear equality constraints (with inequalities converted using auxiliary binary variables), which may limit direct applicability to broader financial optimization formulations.
- Although circuit depth is reduced substantially, scalability on current hardware remains constrained by noise, and larger instances still rely mainly on simulation rather than end-to-end real-device execution.
- The artifact scales down reproduction from the original evaluation setup (reducing cases per benchmark from 100 to about 10), which may introduce slight statistical bias compared to the reported results.
- [inferred] The paper reports improvements against a limited set of VQA baselines and does not compare against strong classical optimization solvers, limiting assessment of practical quantum advantage.
- [inferred] Most experiments use generic combinatorial benchmarks rather than finance-specific datasets, so direct evidence for financial-services use cases is limited despite finance being cited as a motivation.
- [inferred] The conference-paper format and 14-page limit may constrain discussion of negative results, hyperparameter sensitivity, and broader empirical validation.
## Open questions
- How well does Rasengan perform on larger real quantum hardware as qubit counts increase beyond the small instances tested on IBM devices?
- How robust is the segmented execution strategy under stronger or different hardware noise models, especially when intermediate feasible states become hard to preserve?
- Can the transition-Hamiltonian framework be extended beyond problems with linear constraints and efficiently obtainable feasible initial states?
- How does Rasengan compare with state-of-the-art classical solvers in runtime, solution quality, and total cost for practically relevant constrained optimization tasks?
- What is the best strategy for choosing segment sizes and shot allocation to balance latency, noise resilience, and solution quality?
- How sensitive is the method to the structure of the constraint matrix, especially for non-totally-unimodular or denser real-world instances?
- Can the purification-based error mitigation remain effective at larger scales where noise may eliminate all feasible intermediate states?
- [inferred] For financial applications such as portfolio optimization, how does the method handle realistic constraints, market data uncertainty, and larger asset universes?

**Future work:**
- Deploy and evaluate Rasengan on larger and less noisy quantum hardware as device capabilities improve.
- Further improve error mitigation so that feasible intermediate states can be preserved at larger qubit counts and higher noise levels.
- Optimize segmented execution, including segment partitioning and dynamic shot configuration, to better trade off execution overhead and solution quality.
- Explore broader classes of constrained optimization problems and more complex constraint structures beyond the benchmark suite used here.
- Investigate additional Hamiltonian simplification and pruning opportunities to further reduce circuit depth.
- [inferred] Validate the approach on finance-specific benchmark problems and real market datasets relevant to financial services.
- [inferred] Benchmark against advanced classical optimization methods to clarify where Rasengan may offer practical benefit.
- [inferred] Study automated methods for finding or preparing high-quality feasible initial solutions, since initialization is required by the approach.
## Key ideas
- #idea:near-term-feasibility — Rasengan is a NISQ-oriented variational algorithm for constrained binary optimization that uses Hamiltonian simplification, pruning, segmented execution, and purification to reduce depth enough for IBM hardware runs.
- #idea:hybrid-approach — The workflow is hybrid: a classical feasible solution is precomputed, classical optimization tunes evolution times, and quantum circuits implement transition-Hamiltonian exploration within the feasible region.
- #idea:quantum-advantage — The paper claims improved performance over prior quantum heuristics such as HEA and QAOA variants, including better approximation-ratio-gap and much lower circuit depth on benchmark constrained optimization instances.
- #idea:quantum-advantage — Theoretical claims emphasize exponential exploration of feasible solution spaces and stronger expressivity within constrained subspaces, but these are not validated against classical state-of-the-art solvers.
## Contradictions
- The paper suggests quantum performance gains, but this is contradicted by the absence of benchmarking against strong classical optimization solvers; superiority is only shown relative to other quantum heuristics.
- The paper implies improved scalability and reports simulations up to larger qubit counts, but real-hardware evidence is limited to small instances and noisy runs begin to fail as size grows, contradicting broad scalability claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Benchmark instances from literature for five constrained binary optimization domains: FLP, KPP, JSP, SCP, and GCP. The main benchmark suite contains 20 benchmark scales (F1-F4, K1-K4, J1-J4, S1-S4, G1-G4) with 400 cases per domain, totaling 2000 cases. Problem sizes range from 6 to 28 variables/qubits in the main table, with 3 to 15 constraints depending on benchmark. Example qubit counts include FLP 6/15/21/28, KPP 8/15/18/21, JSP 7/10/14/18, SCP 9/12/16/20, and GCP 12/15/20/24. The paper also reports numbers of feasible solutions and average constraint-graph degree as hardness descriptors. Initialization requires one feasible solution, constructed by simple domain-specific heuristics in linear time (e.g., open one facility for FLP, greedy assignment for KPP/JSP, select all sets for SCP, unique color assignment for GCP). No financial dataset is specifically used despite finance being listed as an application area.

### Process
1. Formulate each constrained binary optimization problem as linear constraints Cx=b over binary variables. 2. Compute one feasible solution and derive homogeneous basis vectors u from the null space Cu=0. 3. Construct transition Hamiltonians H_tau(u) using raising/lowering operators so that each Hamiltonian maps between feasible basis states differing by u. 4. Build the Rasengan circuit by sequentially applying transition-Hamiltonian simulations tau(u,t)=exp(-i H_tau(u) t), repeated according to the theoretical schedule; optimize the evolution-time parameters with a classical constrained optimization by linear approximation method. 5. Apply Hamiltonian simplification by greedily replacing basis vectors with valid linear combinations having fewer nonzero entries, then prune redundant transition Hamiltonians by identifying simulations that do not generate new feasible basis states; use early stopping after m consecutive ineffective transitions. 6. Partition the remaining transition sequence into low-depth segments; execute each segment separately, passing forward measured basis states with dynamic shot allocation proportional to their observed probabilities. 7. After each segment, perform purification by checking constraint satisfaction Cx=b and removing infeasible outputs before allocating shots to the next segment. 8. Compare against HEA, P-QAOA (with FrozenQubits and Red-QAOA optimizations), and Choco-Q under matched optimization settings. 9. Evaluate in noise-free simulation, noisy simulation under Pauli/depolarizing and amplitude/phase damping models, and on IBM Kyiv/Brisbane hardware. 10. Conduct ablation studies for simplification, pruning, and segmented execution plus purification, as well as scalability and latency analyses. Baseline settings include 5 repeated layers and up to 300 optimization iterations; scalability uses up to 1000 iterations; real-device runs use up to 100 iterations.

### Output
Primary outputs are approximation ratio gap (ARG), circuit depth, number of trainable parameters, in-constraints rate, and latency (classical plus quantum). Comparisons are made against HEA, penalty-term-based QAOA (P-QAOA), and Choco-Q, with additional references to FrozenQubits and Red-QAOA enhancements for P-QAOA. Results are reported in tables and figures across benchmark scales, including noise-free simulator performance, noisy simulator performance, real-device average ARG and in-constraints rate on IBM Kyiv and Brisbane, scalability curves, noise sensitivity distributions, segmented-execution overhead, and ablation studies. The paper also reports improvements such as 4.12x better accuracy than Choco-Q in algorithmic evaluation and 379x improvement on real hardware.

### Parameters
- baseline_layers: 5
- max_iterations_main: 300
- max_iterations_scalability: 1000
- max_iterations_real_hardware: 100
- real_hardware_qubits: 127
- main_benchmark_qubit_range: 6-28
- scalability_qubit_range: 6-105
- shots_per_segment_overhead_study: 1024
- single_qubit_gate_error_rate_noise_analysis: 0.035%
- two_qubit_gate_error_rate_noise_analysis: 0.875%
- segment_depth_after_optimizations_example: ~50
- circuit_depth_reduction_example: from ~7000 to ~50

### Hardware
Real hardware: IBM Quantum Kyiv and IBM Quantum Brisbane, both described as 127-qubit Eagle r3 devices; execution time estimates in one table are based on the IBM Quebec model. Simulation/classical environment: AMD EPYC 9554 server with 1 TB RAM; artifact appendix mentions dual AMD EPYC 9554 CPUs (128 cores total), optional NVIDIA H100 GPU, and one NVIDIA A100 GPU used for accelerating HEA/QAOA simulations via CUDA Quantum. Simulators/platforms: DDSim for Rasengan circuits, Qiskit-based circuit simulation, optional qiskit-aer-gpu backend. Noise studies use Pauli/depolarizing noise and amplitude/phase damping models parameterized from IBM calibration data. No detailed transpilation settings are given beyond mention of transpiled circuit depth on Quebec.

### Reproducibility
Strong reproducibility support. The paper states Rasengan is publicly available on GitHub and archived on Zenodo (DOI provided), with MIT license. The artifact appendix includes repository structure, environment files, installation instructions, scripts/notebooks for reproducing Table 2 and Figures 9-17, and estimated runtime. However, the artifact notes that reproduction scripts scale down the original evaluation from 100 cases per benchmark to about 10 for practical runtime, which may introduce slight statistical bias relative to the full reported results. Overall, code availability and methodological detail are sufficient for substantial replication.
