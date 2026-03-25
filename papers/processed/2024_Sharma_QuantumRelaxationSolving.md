---
aliases:
- Quantum Relaxation for Solving Multiple Knapsack Problems
- Quantum Relaxation Solving Multiple
authors:
- Monit SHARMA
- Jin YAN
- Hoong Chuin LAU
- Rudy RAYMOND
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- QAOA
- VQE
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:05:26.976831'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:05:30.421859'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:06:09.483785'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:06:43.194957'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:16.113838'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:07:29.707885'
step6_model: gpt-5.4
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
- method/VQE
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Quantum Relaxation for Solving Multiple Knapsack Problems
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes a hybrid quantum-classical approach based on quantum relaxation (QRAO) to tackle constrained combinatorial optimization problems with knapsack-type constraints, motivated by applications in finance and supply chain management. It extends QRAO, originally used for unconstrained problems, to multiple knapsack problems and a risk-aware procurement optimization model, combining QRAC-based encodings with linear relaxation to reduce problem size. The authors compare QRAO against QAOA on multiple knapsack instances and demonstrate that QRAO, especially when combined with linear relaxation, can handle larger real-world procurement problems with over 100 variables under current hardware limitations.
## Methodology
This preprint presents an empirical hybrid quantum-classical methodology for constrained combinatorial optimization, focused on multiple knapsack problems (MKP) and a larger risk-aware procurement optimization problem relevant to supply chain and finance. The core approach is Quantum Random Access Optimization (QRAO), specifically using a (3,1,p)-QRAC encoding to compress up to three classical binary variables into one qubit via a relaxed local quantum Hamiltonian. Problem instances are first formulated as ILP/MILP models; for QRAO, the instance graph is colored using the Large Degree First (LDF) heuristic, variables are assigned to qubits with Pauli X/Y/Z operators, and a variational quantum routine is used to search for the maximum eigenstate of the relaxed Hamiltonian, followed by classical recovery through Pauli rounding or Magic rounding. The study includes preliminary ansatz selection experiments on small MKP instances to identify suitable circuit architectures, then a head-to-head comparison of QAOA and QRAO on 100 randomly generated MKP instances using optimal CPLEX solutions as reference. For larger procurement instances with at least 100 binary variables, the authors combine linear relaxation with QRAO as a presolve/reduction step: variables with LP-relaxed values close to 0 or 1 are fixed, reducing dimensionality before quantum optimization. All experiments are run in simulation and performance is assessed using feasibility, optimality, and average optimality gap.

**Algorithms used:** QRAO, QAOA, VQE, Linear Relaxation, Pauli rounding, Magic rounding, Large Degree First graph coloring, COBYLA
**Frameworks:** Qiskit, Qiskit AerSimulator, CPLEX

**Experimental setup:** All experiments were conducted on simulators using Qiskit's AerSimulator. Preliminary ansatz-selection experiments used 20 small MKP instances with 3 bins and 3 items. Comparative experiments evaluated QAOA versus (3,1,p)-QRAO on 100 randomly generated MKP instances with 2-5 bins and 2-10 items, up to 20 binary variables. For the larger risk-aware procurement problem, 10 random instances with at least 100 binary variables were tested. The procurement experiments were constrained by simulator/hardware limits; the authors report using IBM's Qiskit simulator with the matrix product state simulator supporting up to 63 qubits. QAOA used the default QAOA ansatz with 5 layers, while QRAO used a BrickWork ansatz with 8 complete layers and both Pauli and Magic rounding, with COBYLA as the classical optimizer.

**Dataset:** Synthetic randomly generated instances were used for both the MKP and the risk-aware procurement optimization problem. MKP instances were generated with random item weights, profits, and knapsack capacities. The procurement problem used multiple random instances based on a supplier-risk formulation, where supplier risk scores are conceptually derived following prior work, but the experiments described here appear to use generated instances rather than a released real-world dataset.
## Experiment details
### Input
For ansatz selection, 20 small MKP instances were generated, each with 3 bins and 3 items, approximately 10 binary variables and 6 constraints; item weights were sampled from [1,3], item values from [1,10], and bin capacities from [1,3]. For the main QAOA vs QRAO comparison, 100 non-trivial random MKP instances were generated with 2-5 bins and 2-10 items, up to 20 binary variables, with weights in [1,3], capacities in [1,3], and profits in [1,10], satisfying non-triviality conditions from Eq. (2). For the risk-aware procurement study, 10 random instances were generated, each containing at least 100 binary variables; the formulation includes supplier-part costs, supplier risk scores, part demands, and risk tolerance thresholds, but exact instance dimensions beyond the variable count are not fully specified. No preprocessing beyond LP relaxation and variable fixing is described for the procurement experiments.

### Process
1. Formulate MKP as an ILP and the procurement problem as a MILP. 2. For QRAO, construct an instance graph and apply Large Degree First graph coloring to partition variables. 3. Encode up to three binary variables per qubit using (3,1,p)-QRAC with Pauli X/Y/Z assignments, producing a relaxed Hamiltonian. 4. Perform preliminary ansatz screening on small MKP instances, comparing BrickWork, EfficientSU2, PauliTwoDesign, and RealAmplitudes across increasing layer counts, using the frequency of solutions with optimality gap < 0.05% as the selection criterion. 5. For the MKP benchmark, run QAOA with the default ansatz and 5 layers, and run QRAO with the BrickWork ansatz and 8 complete layers; optimize variational parameters with COBYLA. 6. Decode QRAO solutions using both Pauli rounding and Magic rounding, and compare their performance. 7. Compute exact/optimal reference solutions using CPLEX and evaluate feasibility, optimality, and average optimality gap. 8. For large procurement instances, first solve a linear relaxation, then fix variables whose LP values are within a threshold delta of 0 or 1 (or alternatively fix a large percentage of variables), thereby reducing problem size before applying QRAO. 9. Compare different variable-fixing strategies by reporting feasibility, optimality, and optimality gap across 10 large instances.

### Output
Reported outputs include the number of solved instances during ansatz selection, qubit counts required by QAOA versus QRAO, and benchmark metrics of feasible-solution rate, optimal-solution rate, and average optimality gap relative to CPLEX optimum. For MKP, QAOA, QRAO with Pauli rounding, and QRAO with Magic rounding are compared directly. For the procurement problem, QRAO with linear relaxation is evaluated under different percentages/strategies of fixed variables. Results are presented in tables summarizing solved-instance counts and optimization performance.

### Parameters
- qrao_encoding: (3,1,p)-QRAC
- ansatz_candidates: ['BrickWork', 'EfficientSU2', 'PauliTwoDesign', 'RealAmplitudes']
- selected_qrao_ansatz: BrickWork
- qrao_layers_main_experiment: 8
- qaoa_layers_main_experiment: 5
- optimizer: COBYLA
- small_mkp_instances_for_ansatz_search: 20
- main_mkp_instances: 100
- procurement_instances: 10
- small_mkp_bins: 3
- small_mkp_items: 3
- small_mkp_binary_variables_approx: 10
- small_mkp_constraints: 6
- main_mkp_bins_range: 2-5
- main_mkp_items_range: 2-10
- main_mkp_max_binary_variables: 20
- weights_range: [1,3]
- profits_range: [1,10]
- capacities_range: [1,3]
- procurement_min_binary_variables: 100
- simulator_qubit_limit_reported: 63
- rounding_methods: ['Pauli rounding', 'Magic rounding']
- ansatz_selection_metric: frequency of solutions with optimality gap < 0.05%
- variable_fixing_threshold: delta proximity to 0 or 1; example given delta = 0.1
- fixed_variable_percentages_tested: ['90%', '85%']

### Hardware
Experiments were run on Qiskit AerSimulator. For larger procurement instances, the authors specifically mention IBM's Qiskit matrix product state simulator with a maximum supported size of 63 qubits for their runs. No real QPU, noise model, cloud backend name, transpilation settings, or shot count is reported.

### Reproducibility
Preprint flagged. The paper provides problem formulations, random instance generation ranges, ansatz choices, optimizer, layer counts, and evaluation metrics, which supports partial replication. However, no code repository, seeds, exact simulator settings, shot counts, full procurement instance generation procedure, or complete hyperparameter details are provided. Reproducibility is moderate but incomplete.
## Findings
- [supported] On 100 simulated multiple knapsack problem (MKP) instances with up to 20 binary variables, QRAO with magic rounding achieved 98% feasible solutions, 70% optimal solutions, and an average optimality gap of 0.065, outperforming the reported QAOA baseline (98% feasible, 63% optimal, 0.092 gap).
- [supported] QRAO with Pauli rounding performed substantially worse on the same MKP benchmark, with 81% feasible solutions, 4% optimal solutions, and an average optimality gap of 0.606.
- [supported] QRAO reduced qubit requirements relative to QAOA on the MKP instances; the paper states QAOA used one qubit per variable while QRAO used an average of 7 qubits for problems with up to 20 binary variables.
- [supported] In preliminary simulator experiments on 20 small MKP instances, BrickWork and EfficientSU2 ansatzes outperformed PauliTwoDesign and RealAmplitudes for (3,1,p)-QRAO, with BrickWork solving 20/20 instances at 3-4 layers under the authors' success criterion.
- [supported] For 10 simulated risk-aware procurement optimization instances with at least 100 binary variables, QRAO combined with linear relaxation and random fixing achieved 100% feasible solutions, 80% optimal solutions, and an average optimality gap of 0.053.
- [supported] For the same large procurement instances, fixing 90% of variables via linear relaxation before QRAO yielded 70% feasible, 50% optimal, and 0.088 average optimality gap; fixing 85% yielded 70% feasible, 50% optimal, and 0.072 average optimality gap.
- [supported] The study's experiments were conducted on Qiskit's AerSimulator rather than real quantum hardware, and the authors note simulator and hardware memory/qubit limits as practical constraints.
- [speculative] The authors argue that QRAO has a constant-factor space complexity advantage over QAOA/VQE because it can encode up to three classical bits per qubit using QRAC-based relaxations.
- [speculative] The paper claims the hybrid combination of QRAO with linear relaxation can scale constrained optimization to business problems with over 100 binary variables where direct QAOA is impractical under current hardware and memory limits.
- [speculative] The authors suggest the approach is promising for constrained optimization in financial and supply-chain applications, but this practical applicability is not validated on real quantum hardware.

**Results summary:** This preprint studies a hybrid quantum-classical approach for constrained optimization based on Quantum Random Access Optimization (QRAO), with linear relaxation used as a presolve and variable-fixing step for larger instances. In simulator-based experiments, the authors compare QRAO against QAOA on 100 randomly generated multiple knapsack problem instances and report that QRAO with magic rounding slightly outperforms the QAOA baseline in optimality rate and average optimality gap while using fewer qubits. They also test the method on 10 larger risk-aware procurement optimization instances with at least 100 binary variables, where direct QAOA is described as impractical under current simulator/hardware limits; QRAO plus linear relaxation produced feasible and often optimal solutions with reported average optimality gaps between 0.053 and 0.088 depending on the fixing strategy. All evidence is from simulation, so any broader quantum advantage implication remains speculative.

**Performance claims:**
- MKP benchmark (100 instances): QAOA achieved 98% feasible, 63% optimal, average optimality gap 0.092
- MKP benchmark (100 instances): QRAO with Pauli rounding achieved 81% feasible, 4% optimal, average optimality gap 0.606
- MKP benchmark (100 instances): QRAO with Magic rounding achieved 98% feasible, 70% optimal, average optimality gap 0.065
- QRAO used an average of 7 qubits for MKP instances where QAOA used up to 20 qubits (one per variable)
- Preliminary ansatz study (20 small MKP instances): BrickWork solved 20/20 instances at 3 and 4 layers under the paper's success criterion
- Preliminary ansatz study (20 small MKP instances): EfficientSU2 (full entanglement) solved 18/20 instances at 3 and 4 layers
- Risk-aware procurement (10 instances, >=100 binary variables): QRAO with random fixing achieved 100% feasible, 80% optimal, average optimality gap 0.053
- Risk-aware procurement (10 instances, >=100 binary variables): QRAO with 90% fixed variables achieved 70% feasible, 50% optimal, average optimality gap 0.088
- Risk-aware procurement (10 instances, >=100 binary variables): QRAO with 85% fixed variables achieved 70% feasible, 50% optimal, average optimality gap 0.072
- Simulator limit noted: matrix product state simulator supported a maximum of 63 qubits for their runs
## Quantum advantage claim
**Classification:** speculative

The paper argues for qubit-efficiency and better scalability of QRAO versus QAOA, especially for constrained problems and 100+ variable instances, but all results are from classical simulation and not real hardware. As a preprint, claimed advantage is therefore classified as speculative rather than demonstrated.
## Limitations
- Lack of peer review: the work is presented as an arXiv preprint and has not yet undergone formal peer review.
- Experiments were conducted on Qiskit's AerSimulator rather than real quantum hardware, so hardware noise, calibration drift, connectivity constraints, and execution overheads are not empirically validated.
- The authors describe their investigations as preliminary, indicating limited experimental maturity.
- QAOA vs QRAO benchmarking on MKP was restricted to small instances with at most 20 binary variables.
- The larger risk-aware procurement experiments relied on fixing a large fraction of variables via linear relaxation, so the quantum method was not applied end-to-end to the full original problem.
- Current simulator and memory limits constrained experiments: the matrix product state simulator supported at most 63 qubits, and circuits with more than 50 qubits at sufficient depth were described as impractical due to memory constraints.
- QAOA was limited in circuit depth for 20-qubit instances, restricting its performance and making the comparison partly dependent on implementation constraints rather than purely algorithmic merit.
- Pauli rounding was found to be weak for entangled relaxed states, since it can ignore inter-qubit correlations and thus compromise decoding quality.
- The procurement model is explicitly simplified, including the assumption that every supplier can produce all parts; unavailable supplier-part combinations are only approximated by assigning large costs.
- The risk-aware procurement formulation does not yet incorporate stochastic uncertainty in demand and supply, despite these being central in real supply-chain settings.
- [inferred] The study reports results on only 10 large procurement instances, which limits statistical strength and generalizability for real-world financial or supply-chain deployment.
- [inferred] The random MKP instances use narrow parameter ranges (weights and capacities in [1,3], values in [1,10]), which may not reflect harder or more realistic industrial distributions.
- [inferred] No direct experiments on financial datasets are presented, even though the paper motivates applications in finance.
- [inferred] Comparisons are mainly against QAOA and CPLEX-optimal values; there is no benchmarking against strong classical heuristics/metaheuristics tailored to MKP or procurement optimization.
- [inferred] The reported scalability claim is partly enabled by classical presolve/variable fixing, making it unclear how much of the gain is attributable to QRAO itself versus the classical relaxation step.
- [inferred] Reproducibility is limited by missing implementation details such as shot counts, initialization strategy, stopping criteria, hyperparameter tuning protocol, and exact instance-generation seeds.
- [inferred] The use of simulator-based results leaves open whether deeper QRAO circuits would remain advantageous under realistic NISQ noise and error-mitigation costs.
- [inferred] The study does not quantify runtime, wall-clock cost, or training stability of the hybrid optimization loop, which is important for production scalability.
## Open questions
- How well does QRAO perform on real quantum hardware compared with simulator results?
- Will QRAO retain its advantage over QAOA when realistic noise, limited connectivity, and measurement error are present?
- How does the method scale as the number of assets/items, constraints, suppliers, and parts grows beyond the tested ranges?
- What fraction of the observed performance gain comes from QRAO's encoding versus the classical linear-relaxation presolve step?
- How sensitive are results to the choice of ansatz, number of layers, optimizer, and rounding method?
- Under what problem structures does Magic rounding consistently outperform Pauli rounding, and when might that gap disappear?
- Can the approach handle richer constrained optimization settings with multiple interacting business constraints beyond knapsack-style formulations?
- How robust is the method when demand and supply are uncertain rather than deterministic?
- Would the method outperform strong classical approximation and heuristic methods on practically relevant instances?
- How transferable are the reported supply-chain results to financial-services optimization problems such as portfolio construction or capital allocation?
- What is the trade-off between qubit compression and the increased circuit depth needed to preserve expressivity in QRAO?
- At what problem size or hardware regime, if any, does QRAO provide a practical quantum advantage?

**Future work:**
- Integrate stochastic elements into the problem formulation, especially uncertainty in demand and supply variables.
- Investigate additional classical methods to streamline the problem-solving process beyond linear relaxation.
- Extend the hybrid methodology to broader problem landscapes and business optimization settings.
- Explore improved ways of reducing qubit requirements while maintaining or improving solution quality.
- [inferred] Validate the approach on real quantum hardware and study noise robustness empirically.
- [inferred] Benchmark against stronger classical baselines and larger, more realistic industrial datasets.
- [inferred] Test the method on genuine financial-services use cases to substantiate the paper's finance motivation.
- [inferred] Develop more effective rounding and decoding strategies for highly entangled relaxed states.
- [inferred] Study end-to-end scalability without aggressive variable fixing, or quantify the impact of presolve decisions on final solution quality.
- [inferred] Perform more systematic ablation studies on ansatz design, optimizer choice, layer depth, and encoding schemes.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid workflow combining linear relaxation, variable fixing, QRAO-style variational optimization, and rounding to tackle constrained optimization problems motivated partly by finance.
- #idea:quantum-advantage — On simulated multiple knapsack instances, the QRAO-based approach with Magic rounding slightly outperforms the reported QAOA baseline in optimality rate and average optimality gap while using fewer qubits.
- #idea:near-term-feasibility — Uses QRAC-based qubit compression and variational circuits to argue constrained optimization may be more tractable on NISQ-limited devices than direct one-variable-per-qubit formulations.
- #idea:hybrid-approach — For 100+ variable procurement instances, most practical scalability comes from classical LP relaxation and aggressive variable fixing before the quantum step.
- #idea:quantum-advantage — Frames qubit-efficiency as the main claimed advantage over direct QAOA/VQE-style formulations for knapsack-type constrained problems.
## Contradictions
- The paper suggests improved scalability and practical promise over QAOA for 100+ variable constrained problems, but this is supported only by classical simulation, a 63-qubit simulator cap, and heavy LP-based variable fixing; this weakens any strong claim of genuine quantum scalability.
- The apparent advantage over QAOA may partly reflect implementation constraints on the QAOA baseline (limited depth on 20-qubit instances) rather than a clean algorithmic superiority comparison.
- Although motivated by finance, the study does not validate on real financial datasets or end-to-end financial optimization tasks, so the finance relevance is more aspirational than empirically established.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
