---
aliases:
- 'Classical optimization with imaginary-time block encoding on quantum computers:
  The MaxCut problem'
- Classical optimization imaginary time
authors:
- Dawei Zhong
- Akhil Francis
- Ermal Rrapaj
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/gtq3-j37b
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- QAOA
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:13:05.228422'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:13:09.869032'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:38.939273'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:14:08.571437'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:14:37.543613'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:14:45.870769'
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
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Classical optimization with imaginary-time block encoding on quantum computers:
  The MaxCut problem'
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces an imaginary-time evolution block-encoding (ITE-BE) method to solve classical optimization problems, focusing on MaxCut, by mapping them to diagonal Hamiltonians and implementing nonunitary imaginary-time evolution via block-encoded circuits. The authors also study a hybrid protocol that uses QAOA to prepare an initial state before applying ITE-BE, and numerically evaluate both approaches on random unweighted 3-regular graphs. They compare approximation ratios, optimal-solution probabilities, and postselection rates, showing that ITE-BE can boost shallow QAOA circuits and guarantee convergence to the ground state, albeit with exponentially decaying postselection success as system size and imaginary time increase.
## Methodology
The paper presents and empirically evaluates two quantum optimization protocols for the MaxCut problem based on imaginary-time evolution block encoding (ITE-BE): (1) a pure ITE-BE approach starting from the equal superposition state and (2) a hybrid QAOA + ITE-BE approach in which a p-level QAOA circuit prepares an initial state that is subsequently refined by ITE-BE. MaxCut is formulated as a diagonal Ising-type cost Hamiltonian over graph edges, and the imaginary-time propagator is exactly factorized into commuting two-qubit nonunitary terms because all Z_j Z_k terms commute, eliminating Trotter error for this problem class. Each nonunitary term is implemented via a block-encoding circuit with analytically derived parameters, avoiding variational optimization in the ITE-BE stage. For the pure ITE-BE protocol, the authors partition edges into a maximal matching and remaining edges so that the first layer can use a deterministic/corrected block-encoding circuit when the input is the transverse |+> state, improving postselection success. For the hybrid protocol, near-optimal QAOA parameters from prior work are used directly without retraining, and the resulting state is passed into the ITE-BE layer. The methods are evaluated numerically on randomly generated unweighted 3-regular graph instances with 6 to 12 vertices, primarily nonbipartite graphs, with additional appendix experiments on bipartite 3-regular graphs. Performance is assessed as a function of imaginary time tau using approximation ratio, probability of obtaining an optimal solution, and postselection success rate, with results reported as 99.7% uncertainty intervals over repeated simulations and graph instances. Comparisons are made between pure ITE-BE, QAOA + ITE-BE at multiple QAOA depths, and standalone QAOA behavior at tau = 0; the paper also discusses classical MaxCut solvers only at a contextual level rather than as direct experimental baselines.

**Algorithms used:** ITE-BE, QAOA
**Frameworks:** Qiskit, Qiskit Aer, networkx

**Experimental setup:** All experiments are numerical simulations of quantum circuits rather than executions on real quantum hardware. Quantum circuits were simulated using the AerSimulator backend from Qiskit. Graph instances were generated in Python using networkx. The pure ITE-BE method used N data qubits plus one reusable ancilla qubit, with ancilla reuse enabled through mid-circuit measurement and reset. For a graph G=(V,E), the ITE-BE circuit depth scales as O(|E|), while the hybrid QAOA + ITE-BE protocol has depth O(p|E| + |E|). Imaginary time tau was swept from 0 to 2. For each graph and tau value, circuits were run with 10^5 shots and repeated 10 times; graphs with at least one overall failure event across repetitions were excluded from the reported aggregate statistics.

**Dataset:** Synthetic graph data consisting of randomly generated unweighted 3-regular (u3R) graph instances. The main experiments used 100 random u3R graph instances for each graph size with vertex counts N = 6, 8, 10, and 12, focusing on nonbipartite graphs in the main figures. Additional appendix experiments used 40 randomly generated bipartite 3-regular graph instances for the same range of N.
## Experiment details
### Input
Input instances were synthetic unweighted 3-regular graphs generated with the networkx Python package. Main experiments considered 100 random graph instances per fixed graph size N in the range 6 to 12, with edge weights w_jk = 1 and each node connected to exactly three others. Bipartite graphs were excluded from the main aggregate plots after the authors observed distinct convergence behavior; separate appendix experiments used 40 random bipartite 3-regular graphs. The optimization problem was encoded as the MaxCut Hamiltonian H_C = -sum_{<j,k>} (w_jk/2)(I - Z_j Z_k). No financial dataset was used.

### Process
For pure ITE-BE, the algorithm starts from the equal superposition state |+>^⊗N. The commuting imaginary-time propagator exp(-tau H_C) is factorized exactly into edge-wise terms exp(-tau w_jk Z_j Z_k / 2). Edges are reordered into two groups: a maximal matching V1 and the remaining edges V2. For V1, the authors use a corrected/deterministic block-encoding circuit specialized to the |+>|+> input to improve postselection; for V2, they use the generic postselected block-encoding circuit. A single ancilla qubit is reused across blocks via mid-circuit measurement and reset, and a shot is terminated if any ancilla measurement in the postselected part returns |1>. Data qubits are measured only after all blocks are applied. For QAOA + ITE-BE, a p-level QAOA state preparation circuit is first applied using near-optimal parameters from prior work for MaxCut on large-girth regular graphs, with p values including 4, 6, 8, 10, and 12 in the reported N=12 experiments; no additional parameter training is performed. The QAOA output state is then evolved with the same ITE-BE procedure, using the generic block-encoding circuit for each edge term. Imaginary time tau is varied from 0 to 2. For each graph instance and tau, the circuit is simulated with 10^5 shots and the full procedure is repeated 10 times to reduce statistical fluctuations. Metrics are computed from successful postselected runs, then aggregated across graph instances and reported with 99.7% uncertainty intervals.

### Output
The main reported outputs are (1) approximation ratio r = C(s)/C_max, (2) probability of obtaining an optimal solution p_opt = N_opt / N_tot, and (3) postselection success rate, defined as the probability that all ancilla postselections succeed. Results are plotted as functions of imaginary time tau and reported as averaged 99.7% uncertainty intervals over graph instances and repetitions. Comparisons include pure ITE-BE versus QAOA + ITE-BE at different QAOA depths, and the tau = 0 point is interpreted as standalone QAOA performance. The paper concludes that ITE-BE converges to the ground state for sufficiently large tau and that QAOA initialization improves both convergence speed and postselection rate relative to starting from |+>^⊗N.

### Parameters
- graph_sizes_N: [6, 8, 10, 12]
- graph_type: random unweighted 3-regular graphs
- main_graph_instances_per_N: 100
- bipartite_graph_instances_per_N: 40
- edge_weights: 1
- imaginary_time_tau_range: 0 to 2
- shots_per_graph_per_tau: 100000
- repetitions_per_setting: 10
- qaoa_depths_tested: [4, 6, 8, 10, 12]
- qubits_required: |V| + 1 with ancilla reuse
- circuit_depth_ite_be: O(|E|)
- circuit_depth_qaoa_plus_ite_be: O(p|E| + |E|)
- uncertainty_interval: 99.7%

### Hardware
{'hardware_type': 'simulator', 'simulator': 'Qiskit AerSimulator', 'real_qpu_used': False, 'ancilla_strategy': 'single reusable ancilla with mid-circuit measurement and reset', 'noise_model': 'not specified'}

### Reproducibility
Data availability is explicitly stated, with an open GitHub repository provided (https://github.com/dawei-zh/ite-be). The paper gives substantial methodological detail on graph generation, circuit construction, shot counts, repetitions, and evaluation metrics, and identifies the simulator backend and software stack. QAOA parameters are taken from a cited prior work rather than reproduced in full here, so exact replication of the hybrid setup may require consulting that reference. Overall reproducibility is good to strong.
## Findings
- [supported] The paper introduces imaginary-time evolution block encoding (ITE-BE) for MaxCut, with analytically determined circuit parameters and no variational parameter optimization required.
- [supported] In numerical simulations on 100 randomly generated unweighted 3-regular graphs with 6 <= N <= 12, both approximation ratio and probability of obtaining the optimal solution increased monotonically with imaginary time tau and approached the optimum as tau approached 2.
- [supported] The ITE-BE-only method converged toward the ground state for the tested MaxCut instances, while postselection success rate decreased exponentially with imaginary time tau.
- [supported] The hybrid QAOA + ITE-BE method also converged toward the ground state by tau ~ 2 for tested graph sizes and QAOA depths, using near-optimal QAOA parameters from prior work without additional training.
- [supported] QAOA-prepared initial states improved ITE-BE performance: they produced faster convergence and higher postselection success than starting from the equal superposition state |+>^N.
- [supported] For N = 12 and tau = 2, the postselection success rate with QAOA + ITE-BE was about one order of magnitude higher than with ITE-BE starting from |+>^N.
- [supported] Shallow QAOA circuits boosted with ITE-BE achieved better performance than deeper QAOA circuits alone on the simulated MaxCut instances.
- [supported] The first ITE-BE layer can be made deterministic for transverse initial states via a modified block-encoding construction, eliminating postselection for that layer.
- [supported] Bipartite 3-regular graphs showed faster convergence and higher postselection success than nonbipartite graphs of the same size in simulation, with success rates reaching a plateau after moderate tau.
- [supported] At tau = 0, QAOA alone achieved high approximation ratios but comparatively lower probabilities of sampling exact optimal solutions, indicating good expected cut values without concentrating probability mass entirely on optimal bitstrings.
- [speculative] The authors argue that concatenating quantum algorithms such as QAOA and ITE-BE may be a promising strategy for larger combinatorial optimization problems beyond MaxCut.
- [speculative] The paper suggests that practical quantum advantage would require more than 100 qubits, but no quantum advantage is demonstrated in this work.

**Results summary:** This peer-reviewed empirical study evaluates two quantum MaxCut protocols using simulation: a pure imaginary-time evolution block-encoding method (ITE-BE) and a hybrid QAOA + ITE-BE method. On 100 randomly generated unweighted 3-regular graphs with 6 to 12 vertices, both methods showed monotonic improvement in approximation ratio and optimal-solution sampling probability as imaginary time increased, with convergence near the optimum by tau approximately 2. All results were obtained with Qiskit Aer simulation rather than real quantum hardware. The hybrid method improved over standalone QAOA by increasing overlap with the ground state and improved over pure ITE-BE by raising postselection success, including about a 10x postselection-rate gain for N = 12 at tau = 2. The main practical limitation observed was exponentially decaying postselection success with increasing tau and graph size.

**Performance claims:**
- Simulations performed on 100 randomly generated unweighted 3-regular graph instances for each graph size N = 6, 8, 10, 12
- Imaginary time scanned from tau = 0 to tau = 2
- 10^5 shots per graph per tau value, repeated 10 times
- Reported 99.7% uncertainty intervals (three-standard-deviation intervals) for approximation ratio, optimal-solution probability, and postselection success rate
- For N = 12 and tau = 2, QAOA + ITE-BE increased postselection success rate by about one order of magnitude relative to ITE-BE initialized with |+>^N
- Pure ITE-BE uses N + 1 qubits with ancilla reuse and circuit depth O(|E|)
- QAOA + ITE-BE uses N + 1 qubits with ancilla reuse and circuit depth O(p|E| + |E|)
- For bipartite 3-regular graphs, postselection success rate plateaued after tau ~ 0.6 for ITE-BE
- For bipartite 3-regular graphs, postselection success rate plateaued after tau ~ 0.4 for QAOA + ITE-BE
- At tau = 0 for QAOA + ITE-BE on N = 6, 8, 10 graphs, approximation ratio was already above 0.9 before applying ITE-BE
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. Results are from classical simulation only on small instances (N <= 12), and the authors explicitly note that demonstrating advantage would likely require more than 100 qubits. Any advantage claim is therefore prospective rather than empirically established.
## Limitations
- Experiments are limited to numerical simulations on randomly generated unweighted 3-regular MaxCut instances with only 6 to 12 vertices.
- The study focuses mainly on MaxCut, so empirical evidence for other optimization problems relevant to finance is not provided.
- Practical applicability is limited by the exponential decay in postselection success rates as imaginary time τ and graph size N increase.
- The convergence becomes slower and the postselection success rate decreases as problem size N increases.
- The demonstrated problem sizes are far below those handled by current classical MaxCut solvers, which the authors note can solve graphs with hundreds to more than 10,000 nodes depending on structure.
- The authors state that demonstrating quantum advantage would require access to more than 100 qubits, beyond the scale studied here.
- The QAOA+ITE-BE protocol still has circuit depth O(p|E| + |E|), which may become challenging for large graphs.
- The method relies on postselection and, in some variants, potentially additional ancilla qubits or amplitude amplification, increasing resource overhead.
- Results are reported for ideal simulator runs rather than noisy hardware executions, so robustness to decoherence, gate errors, readout errors, and mid-circuit reset imperfections is unverified.
- [inferred] No experiments on real quantum hardware were performed, so NISQ-era feasibility and hardware-specific bottlenecks remain unclear.
- [inferred] No noise mitigation or error-correction strategy is evaluated, despite the method's dependence on repeated postselection and ancilla operations.
- [inferred] Internal validity is limited by using only synthetic graph instances from a single graph family; performance may differ on weighted, irregular, dense, or finance-derived QUBO instances.
- [inferred] The use of near-optimal QAOA parameters from prior work rather than instance-specific training may confound attribution of gains between the QAOA initialization and the ITE-BE layer.
- [inferred] The exclusion of graph instances with at least one overall failure may bias reported averages upward by removing hardest cases with zero successful shots.
- [inferred] The comparison to classical methods is indirect; there is no head-to-head benchmark against state-of-the-art classical solvers on the same instances and compute budgets.
- [inferred] Reproducibility is helped by open data/code, but exact simulator settings and practical implementation details for hardware deployment may still be insufficient for full end-to-end replication on quantum devices.
## Open questions
- Can postselection success rates be improved enough for the method to become practical at larger graph sizes?
- How can convergence speed be enhanced without sacrificing solution quality?
- Will the observed guaranteed convergence in simulation translate into useful performance on real noisy quantum hardware?
- At what graph sizes, qubit counts, and error rates could ITE-BE or QAOA+ITE-BE outperform classical MaxCut solvers?
- How does the method perform on weighted, dense, irregular, or real-world optimization instances rather than only unweighted 3-regular graphs?
- What is the best tradeoff between QAOA depth p and imaginary time τ for minimizing total quantum resources?
- Can the approach scale beyond the >100 qubit regime that the authors identify as likely necessary for quantum advantage?
- How much of the performance gain in QAOA+ITE-BE comes from better initial-state overlap versus the imaginary-time block-encoding itself?
- How sensitive is the method to hardware noise, mid-circuit measurement/reset errors, and ancilla reuse imperfections?
- Will the approach remain effective for other combinatorial optimization problems such as knapsack or traveling salesman, especially in finance-relevant formulations?

**Future work:**
- Develop methods to improve the postselection success rate.
- Develop methods to enhance convergence speed of the ITE-BE-based algorithms.
- Explore advanced algorithm designs to overcome the practical limitations caused by exponentially decaying postselection rates.
- Extend the ITE-BE and QAOA+ITE-BE principles to other combinatorial optimization problems such as the traveling salesman problem and knapsack problem.
- Investigate larger graph instances and larger qubit counts to assess the possibility of practical quantum advantage.
- Study algorithm concatenation strategies further to boost performance and overcome limitations of individual quantum methods.
- [inferred] Validate the approach on real quantum hardware with realistic noise models and error mitigation.
- [inferred] Benchmark directly against state-of-the-art classical optimization solvers on matched instance sets and resource budgets.
- [inferred] Test on weighted, finance-inspired QUBO instances to evaluate relevance for financial services applications.
- [inferred] Analyze resource-efficient alternatives to postselection, such as improved block-encoding constructions or amplitude-amplification-based variants.
## Key ideas
- #idea:hybrid-approach — Combines QAOA state preparation with imaginary-time evolution block encoding to improve MaxCut performance over standalone QAOA in simulation.
- #idea:near-term-feasibility — Suggests a potentially NISQ-relevant hybrid structure using shallow QAOA plus ITE-BE on small instances, though only in simulator studies.
- #idea:hybrid-approach — QAOA initialization improves convergence speed and postselection success relative to starting from the uniform superposition state.
- #idea:quantum-advantage — Positions the method as a possible route toward future advantage on larger QUBO-like optimization problems once larger hardware is available.
## Contradictions
- The paper gestures toward future quantum advantage, but its own evidence is limited to classical simulation on very small MaxCut instances with no direct classical baseline, contradicting any strong superiority interpretation (#contradiction:classical-vs-quantum).
- The method guarantees convergence in simulation, yet exponentially decaying postselection success and increasing depth/resource demands with problem size undermine claims of practical scaling to real large optimization problems (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
