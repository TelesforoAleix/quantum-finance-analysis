---
aliases:
- 'Towards arbitrary QUBO optimization: analysis of classical and quantum-activated
  feedforward neural networks'
- Towards arbitrary QUBO optimization
authors:
- Chia-Tso Lai
- Carsten Blank
- Peter Schmelcher
- Rick Mukherjee
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1088/2632-2153/addb97
evidence_type: ''
idea_tags:
- idea:hybrid-approach
- idea:near-term-feasibility
journal_or_venue: 'Machine Learning: Science and Technology'
methodology_tags:
- quantum-annealing
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:10:26.855920'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:10:31.597759'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:11:10.821545'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:11:52.159822'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:12:22.409912'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:12:34.031800'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/quantum-annealing
- method/QUBO
- method/classical-simulation
- idea/hybrid-approach
- idea/near-term-feasibility
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Towards arbitrary QUBO optimization: analysis of classical and quantum-activated
  feedforward neural networks'
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes an unsupervised feedforward neural network (FNN) architecture for solving arbitrary QUBO problems, including weighted MaxCut, MWIS, TSP, and dense random QUBOs, without relying on training data. It systematically studies hyperparameter choices and shows that this relatively small FNN can produce high-quality approximate solutions for large instances, often rivaling or surpassing Gurobi and selected quantum and digital annealers in accuracy–runtime trade-offs. The authors also explore a hybrid quantum–classical encoder–decoder variant using a Rydberg-annealer-based quantum activation, finding that in practice the quantum layer becomes inactive, so the performance gains are effectively due to the classical network alone.
## Methodology
The paper presents an empirical benchmarking study of two unsupervised neural-network-based optimizers for arbitrary QUBO problems: a classical feedforward neural network (FNN) and an exploratory hybrid quantum-classical encoder-decoder (QCED) that inserts a simulated Rydberg-atom quantum annealer as a quantum activation layer. The core methodological choice is unsupervised learning, where the QUBO objective itself is used as the loss function rather than labeled training data. Binary decision variables are relaxed to continuous values in [0,1] during training, and the authors empirically select a linearized diagonal term in the QUBO loss to improve gradient behavior. The FNN is trained with gradient descent and backpropagation, using a pre-sampling strategy over multiple random initializations to reduce poor local minima. QCED uses an encoder to map QUBO matrix entries to laser parameters of a 4-qubit Rydberg annealer, simulates the quantum dynamics, measures expectation values, and decodes them into candidate solutions; gradients through the quantum layer are computed by finite differences and validated against an approximate parameter-shift rule. Experiments evaluate optimization quality and runtime across 100 generated instances per problem size for weighted MaxCut, random dense QUBO, MWIS, and TSP, with 500 training iterations in most comparative tests and larger-scale benchmarks up to 200 variables. Performance is compared against Gurobi, D-Wave Advantage, and the Fujitsu digital annealer emulator using average QUBO cost values, percentage error relative to optimum, convergence curves, standard deviations, and runtime. The study concludes that the classical FNN is the practically effective method, while the quantum layer in QCED becomes largely inactive during training.

**Algorithms used:** Feedforward Neural Network (FNN), Quantum-classical encoder-decoder (QCED), Quantum annealing, Gradient descent, Backpropagation, Finite-difference gradient estimation, Approximate parameter-shift rule, Post-processing inspired by simulated annealing, Branch-and-bound, Mixed Integer Programming (MIP), Simulated annealing, Digital annealing
**Frameworks:** QuTiP, Gurobi, D-Wave Advantage, Fujitsu Digital Annealer Emulator

**Experimental setup:** Experiments were conducted primarily as simulations on a local machine using 8 CPU threads. The FNN and QCED were trained for up to 500 iterations in most optimization tests; for runtime benchmarking, MaxCut and random QUBO used 100 iterations while MWIS and TSP used 500. QCED used a simulated 4-qubit Rydberg atom array arranged in a square, with 12 trainable laser parameters in the quantum layer, and quantum evolution was simulated in QuTiP. For FNN, a 7-layer architecture was used for problems up to 40 variables (or 64 variables for TSP), and a 10-layer architecture for larger 80/200-variable benchmarks. Pre-sampling over 20 random initializations was used in FNN vs QCED comparisons. External baselines included Gurobi with 100 s and 1200 s time limits depending on the benchmark, D-Wave Advantage with 20 microsecond annealing time and 100 anneals, and Fujitsu digital annealer emulator with N^2 iterations per run and 4 runs per instance.

**Dataset:** Synthetic QUBO benchmark datasets generated by the authors for weighted MaxCut, random dense QUBO, maximum weighted independent set (MWIS), and traveling salesperson problem (TSP). For each problem size, 100 instances were generated. MaxCut and MWIS graphs were random graphs without degree restrictions; edge weights (MaxCut) and node weights (MWIS) were sampled uniformly from 0 to 10. Random QUBO matrices were dense symmetric matrices with entries sampled uniformly from -10 to 10. TSP instances were generated from random distance matrices normalized to (0,1], with penalty constant set to 10% above the maximum normalized distance.
## Experiment details
### Input
Synthetic generated instances only. For comparative learning-curve and scalability tests, 100 samples were generated for each problem size. Problem sizes included 5, 10, 15, 20, and 40 variables for MaxCut, random QUBO, and MWIS; and 4, 5, 6, 8, and 10 cities for TSP, corresponding to 16, 25, 36, 64, and 100 binary variables. Large-scale benchmarks used 80- and 200-variable MaxCut, random QUBO, and MWIS instances, and 100- and 196-variable TSP instances. MWIS graphs were formed by randomly selecting up to n(n-1)/2 edges and assigning node weights from Uniform(0,10), with penalty P=10. MaxCut graphs had random connectivity and edge weights from Uniform(0,10). Random QUBO matrices were dense symmetric matrices with entries from Uniform(-10,10). TSP used random distance matrices normalized to (0,1], with penalty A set to 1.1 times the maximum normalized distance. No external financial dataset was used, though finance is mentioned as an application area of QUBO.

### Process
1. Formulate each optimization problem as a QUBO objective. 2. Use unsupervised learning by taking the QUBO cost x^TQx as the loss, with binary outputs relaxed to continuous values in [0,1] during training. 3. For FNN, initialize a small trainable input vector of 4 random values, pass it through a multilayer feedforward network with ReLU hidden activations and tanh-based output mapping to [0,1]^n, and optimize parameters via standard gradient descent and backpropagation. 4. Apply pre-sampling: train multiple candidate initializations for a small number of epochs, select the best-performing initialization, then continue full training; 20 pre-sampling rounds were used in FNN vs QCED tests. 5. For QCED, encode the upper-triangular QUBO entries into 12 laser parameters for a 4-qubit Rydberg annealer, simulate time evolution under a parametrized Hamiltonian with piecewise-constant global Rabi schedule and linear local detuning schedules, measure qubit expectation values, decode them with an FNN, and optimize the full hybrid model. 6. Compute quantum-layer gradients by finite differences, requiring 6q simulations per iteration for q atoms; credibility was checked against an approximate parameter-shift rule. 7. Run optimization for 500 iterations in most comparative experiments; for runtime tests, use 100 iterations for MaxCut/random QUBO and 500 for MWIS/TSP. 8. For large FNN benchmarks, increase network depth from 7 to 10 layers. 9. Optionally apply a 10-round post-processing heuristic inspired by simulated annealing: sequentially flip bits in the FNN output, accept improvements deterministically and some worse moves with Boltzmann probability exp(-ΔE/T(r)), where T(r)=|C_FNN|/(nr). 10. Compare final solutions against exact or approximate baselines from Gurobi, D-Wave Advantage, and Fujitsu digital annealer emulator.

### Output
Reported outputs include percentage error relative to optimal QUBO cost, average QUBO cost values over 100 instances, learning curves over training iterations, one-standard-deviation error bands, layer activeness measured by average percentage parameter change, and wall-clock runtime. Baseline comparisons were made against Gurobi optimizer, D-Wave Advantage quantum annealer, and Fujitsu digital annealer emulator. For some benchmarks, exact solutions from Gurobi were used when convergence occurred within the time limit; otherwise best-found approximate solutions were used. Results were also presented before and after FNN post-processing.

### Parameters
- FNN_input_dimension: 4
- FNN_layers_small_problems: 7
- FNN_layers_large_problems: 10
- FNN_hidden_width_small: n+4 neurons per hidden layer
- FNN_output_dimension: n
- FNN_hidden_activation: ReLU
- FNN_output_activation: tanh followed by linear rescaling to [0,1]
- QCED_qubits: 4
- QCED_quantum_layer_trainable_parameters: 12
- QCED_encoder_layers: 3
- QCED_decoder_layers: 3
- QCED_encoder_structure: [n(n+1)/2 + 12, n(n+1)/2 + 12, 12]
- QCED_decoder_structure: [n+4, n+4, n]
- QCED_hidden_activation: ReLU
- QCED_encoder_final_activation: Sigmoid
- training_iterations_main: 500
- training_iterations_runtime_MaxCut_randomQUBO: 100
- training_iterations_runtime_MWIS_TSP: 500
- presampling_rounds: 20
- gradient_method_FNN: standard backpropagation
- gradient_method_QCED: finite difference
- Rydberg_Rabi_max: 10 MHz
- Rydberg_detuning_max: 1 GHz
- Rydberg_boundary_conditions: Omega_0 = Omega_N-1 = 0
- MWIS_penalty: 10
- TSP_penalty: 10% greater than maximal normalized distance
- DWave_annealing_time: 20 microseconds
- DWave_num_anneals: 100
- Gurobi_time_limit_large_benchmark: 100 s
- Gurobi_time_limit_runtime_benchmark: 1200 s
- Fujitsu_iterations_per_run: N^2
- Fujitsu_runs_per_instance: 4
- postprocessing_rounds: 10
- postprocessing_temperature: T(r)=|C_FNN|/(n r)

### Hardware
Primary experiments were run on a local classical machine using 8 CPU threads. The quantum component was not executed on real quantum hardware; the Rydberg annealer in QCED was simulated with QuTiP. Baseline hardware/platforms included D-Wave Advantage quantum annealer (real QPU; Pegasus topology, over 5000 qubits, 15 couplers per qubit) and Fujitsu digital annealer emulator. No transpilation settings were reported because the main quantum method used analog simulation rather than gate-based compilation.

### Reproducibility
Strong reproducibility overall. The paper states that both data and code are openly available on GitHub, and the synthetic datasets are generated from procedures described in the appendices. Architectures, loss design, problem generation, benchmark settings, and many hyperparameters are reported in detail. Replication appears feasible, especially for the FNN and simulated QCED experiments, though some implementation details for external proprietary baselines (Gurobi, D-Wave, Fujitsu) necessarily depend on vendor tools.
## Findings
- [supported] An unsupervised feedforward neural network (FNN) optimizer achieved over 99% average accuracy on dense 80-variable weighted MaxCut and random QUBO problems in less than 1.1 s on an 8-core CPU.
- [supported] On 200-variable random QUBO problems with a 100 s computation limit, the FNN outperformed Gurobi by 72% in objective value according to the paper's reported benchmark.
- [supported] For 15-variable benchmarks over 100 instances, QCED reached lower mean percentage errors than FNN after 500 training iterations: MaxCut 0.95% vs 1.46%, random QUBO 0.197% vs 0.826%, MWIS 6.7% vs 7.53%, and 4-city TSP 2.99% vs 5.17%.
- [supported] Across scaling tests up to 40 variables, both FNN and QCED maintained low errors on MaxCut and random QUBO, while both degraded substantially on MWIS and TSP as problem size increased.
- [supported] Layer-activity analysis showed the encoder in the hybrid quantum-classical encoder-decoder (QCED) remained effectively inactive during training, while the decoder was active, indicating the quantum layer was effectively deactivated.
- [supported] Because the quantum layer in QCED was inactive, the hybrid architecture provided no tangible optimization benefit over a simpler classical FNN in the authors' experiments.
- [supported] In large-instance benchmarks, post-processed FNN achieved the best reported average objective values among compared solvers for MaxCut and random QUBO at 80 and 200 variables.
- [supported] For 80-variable MaxCut and random QUBO, FNN runtime was under 1.1 s and used approximately 1/200 and 1/1200 of Gurobi's time, respectively, while achieving about 99.5% accuracy and nearly identical cost values.
- [supported] FNN performed poorly relative to Gurobi on MWIS, reaching only 78.14% accuracy on 80-variable MWIS in 2.3 s, whereas Gurobi solved the instance in about 0.2 s.
- [supported] The D-Wave Advantage annealer optimized 80-variable random QUBOs effectively with accuracy close to post-processed FNN, but struggled on other problem classes and could not handle 200-variable instances due to embedding failure.
- [speculative] The authors suggest the FNN's runtime and accuracy profile could make it useful for real-time financial optimization tasks such as portfolio optimization in high-frequency trading.
- [speculative] The authors propose that quantum circuits with unbounded parameters may keep a quantum layer active in future hybrid models, but this was not shown to improve optimization here.

**Results summary:** This peer-reviewed empirical paper evaluates a classical unsupervised feedforward neural network (FNN) and a hybrid quantum-classical encoder-decoder (QCED) for arbitrary QUBO optimization using simulated experiments and classical benchmarking. Results are primarily from classical simulation, with external comparisons to commercial solvers and a D-Wave quantum annealer. The FNN achieved over 99% average accuracy on 80-variable weighted MaxCut and random QUBO instances in under 1.1 s on an 8-core CPU, and after post-processing produced the best average objective values among compared solvers for MaxCut and random QUBO at 80 and 200 variables. In 15-variable tests, QCED initially appeared better than FNN, but parameter-update analysis showed the encoder and quantum layer were effectively inactive, meaning the hybrid quantum component did not contribute meaningfully. FNN showed strong runtime advantages over Gurobi on large MaxCut and random QUBO instances, but underperformed badly on MWIS and showed worsening performance on larger TSP instances. The paper therefore supports strong classical heuristic performance for arbitrary QUBO, but does not demonstrate a practical benefit from the proposed quantum-enhanced architecture.

**Performance claims:**
- Over 99% average accuracy on dense 80-variable weighted MaxCut and random QUBO in less than 1.1 s on an 8-core CPU
- 72% better than Gurobi on 200-variable random QUBO within a 100 s computation limit
- 15-variable MaxCut mean error: QCED 0.95% vs FNN 1.46%
- 15-variable random QUBO mean error: QCED 0.197% vs FNN 0.826%
- 15-variable MWIS mean error: QCED 6.7% vs FNN 7.53%
- 4-city TSP mean error: QCED 2.99% vs FNN 5.17%
- For MaxCut up to 40 variables: FNN errors below 2%, QCED below 1.3%
- For 40-variable MWIS: QCED error rose to nearly 50%
- Unprocessed FNN accuracy: 99.32% for 80-variable MaxCut and 99.20% for 80-variable random QUBO
- Post-processed FNN accuracy: 99.78% for 80-variable MaxCut and 99.66% for 80-variable random QUBO
- 80-variable MaxCut average objective: Gurobi -4918.04, FNN -4906.38, post-processed FNN -4929.13, Fujitsu emulator -4906.4, D-Wave -4496.41
- 200-variable MaxCut average objective: Gurobi -27308.26, FNN -27530.78, post-processed FNN -28056.96, Fujitsu emulator -28032.9
- 80-variable random QUBO average objective: Gurobi -1682.73, FNN -1684.35, post-processed FNN -1692.32, Fujitsu emulator -468.61, D-Wave -1691.74
- 200-variable random QUBO average objective: Gurobi -3934.86, FNN -6631.17, post-processed FNN -6768.17, Fujitsu emulator -456.79
- 80-variable MWIS average objective: Gurobi -68.51, FNN -47.07, post-processed FNN -59.16, Fujitsu emulator 7451.40, D-Wave 173.30
- 200-variable MWIS average objective: Gurobi -98.50, FNN -42.82, post-processed FNN -66.86, Fujitsu emulator 12603.4
- 100-variable TSP average objective: Gurobi -19.14, FNN -17.06, post-processed FNN -17.58, Fujitsu emulator 280.51, D-Wave -7.73
- 196-variable TSP average objective: Gurobi -26.98, FNN -22.31, post-processed FNN -25.12, Fujitsu emulator 303.02
- FNN runtime under 4.1 s for MWIS and TSP, and under 1.1 s for MaxCut and random QUBO across tested sizes
- For 80-variable MaxCut and random QUBO, FNN used approximately 1/200 and 1/1200 of Gurobi's runtime, respectively
- 80-variable MWIS: FNN achieved 78.14% accuracy in 2.3 s, while Gurobi solved it in about 0.2 s
## Quantum advantage claim
**Classification:** not-applicable

The paper does not demonstrate quantum advantage. The proposed hybrid QCED uses a simulated Rydberg-annealer-based activation, but empirical analysis shows the quantum layer was effectively inactive during training, so no quantum performance benefit was established. External D-Wave comparisons also do not show a clear quantum advantage over classical methods.
## Limitations
- The quantum–classical encoder–decoder (QCED) did not provide tangible benefit because the quantum layer was effectively deactivated during training.
- The pre-sampling technique for initialization does not guarantee finding the global optimum; it only increases the chance of reaching a good approximate solution.
- The chosen FNN architecture was selected empirically through trial and error, and the authors explicitly note that better configurations may still exist.
- QCED used only 4 qubits arranged in a square, a highly minimalist setup that limits conclusions about larger or more expressive quantum layers.
- Gradient evaluation for the quantum layer used finite differences, requiring 6q simulations per training iteration, which creates a training bottleneck as quantum system size grows.
- The gradients of the quantum layer are inherently susceptible to noise sources such as laser fluctuations and measurement infidelity, which can compromise gradient reliability on real hardware.
- The Rydberg annealer was simulated rather than executed on actual quantum hardware, so hardware-level effects were not empirically validated.
- Encoding arbitrary QUBO instances onto Rydberg atom arrays remains resource-demanding and challenging in practice despite recent advances.
- The D-Wave benchmark could not handle 200-variable instances because embedding onto the hardware topology was unsuccessful.
- FNN performance was uneven across problem classes: it was strong on MaxCut and random QUBO, but comparatively weak on MWIS and less convincing on larger TSP instances.
- For TSP, optimization errors increased steadily with problem size and exceeded 10% for 10-city problems, indicating limited scalability for this structured problem class.
- For MWIS, both FNN and QCED performed poorly as problem size increased, with QCED reaching nearly 50% error on 40-node instances.
- Benchmarking against Gurobi used fixed runtime limits (100 s and 1200 s in different experiments), so comparisons partly reflect time-budgeted heuristic performance rather than unrestricted optimality.
- The Fujitsu digital annealer benchmark is only described at a high level because implementation details are proprietary, limiting interpretability and reproducibility of cross-solver comparisons.
- [inferred] The study uses synthetic/generated QUBO instances (random graphs, random matrices, synthetic TSP distances) rather than real financial datasets, limiting direct evidence for financial-services applicability.
- [inferred] Claims about suitability for real-time applications such as portfolio optimization in high-frequency trading are not validated on production financial workflows or live market constraints.
- [inferred] Internal validity may be affected by extensive empirical hyperparameter tuning and architecture search on the tested problem families, which could bias results toward those benchmarks.
- [inferred] Reproducibility is only partial: although code/data are shared, some benchmark baselines depend on proprietary solvers and hardware settings that other researchers may not be able to replicate exactly.
- [inferred] No direct comparison is reported against some strong modern learning-based combinatorial optimizers beyond the selected baselines, so relative state-of-the-art standing may be incomplete.
- [inferred] The unsupervised objective optimizes QUBO cost directly, but there is limited analysis of robustness across distribution shifts to qualitatively different QUBO structures.
## Open questions
- Under what conditions can a quantum layer in a hybrid quantum–classical neural network remain active during training?
- Why do bounded quantum parameters in QCED lead to deactivation of the encoder and quantum layer?
- Can quantum circuits with unbounded parameters provide a practically useful active quantum layer and outperform purely classical FNNs?
- How should quantum and classical components interact in hybrid networks to yield genuine optimization gains?
- Why do high-randomness QUBO matrices such as dense random QUBO and high-degree weighted MaxCut appear easier for FNN than more structured problems like MWIS?
- What aspects of QUBO structure most strongly determine hardness for neural-network-based optimizers?
- How well would the proposed methods scale beyond the tested sizes, especially for larger TSP, MWIS, and arbitrary industrial QUBOs?
- How robust would the quantum-layer training be under real hardware noise, including laser fluctuations and measurement errors?
- Would larger or differently connected quantum annealer layers change the conclusion that the quantum component is unjustified?
- Can the runtime and accuracy advantages observed on synthetic benchmarks transfer to real-world optimization tasks in finance and other industries?

**Future work:**
- Explore other uses of QCED where the quantum activation function plays a more significant role.
- Investigate quantum circuits with unbounded parameters as alternative quantum activation functions to keep the quantum layer active.
- Study QCED from the perspective of an RNN embedded within FNNs, motivated by the connection between Rydberg atom arrays and recurrent neural networks in a certain limit.
- Develop a better understanding of the interaction between quantum and classical components in hybrid networks.
- Identify conditions under which quantum layers remain active during training.
- Improve the FNN solver by introducing Bayesian-based approaches into the optimization routine.
- Further study the inherent complexity of different QUBO problem classes and the relationship between matrix structure and solver performance.
- [inferred] Validate the approach on real quantum hardware to test whether simulation-based findings hold under realistic noise and control constraints.
- [inferred] Evaluate the method on real financial optimization datasets and domain-specific formulations such as portfolio optimization, trading, or risk management QUBOs.
- [inferred] Test scalability on larger production-scale QUBOs and compare against additional state-of-the-art classical heuristics and learning-based optimizers.
- [inferred] Investigate noise-mitigation or robust gradient-estimation methods for training hybrid quantum–classical models on hardware.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum–classical encoder–decoder with a simulated Rydberg-annealer activation layer for generic QUBO optimisation.
- #idea:hybrid-approach — Empirical analysis shows the quantum layer becomes effectively inactive during training, so observed performance is driven by the classical network rather than the quantum component.
- #idea:near-term-feasibility — A small unsupervised classical FNN trained directly on the QUBO objective achieves strong runtime–accuracy trade-offs on synthetic MaxCut and random QUBO benchmarks.
- #contradiction:classical-vs-quantum — Results undermine the expectation that adding a quantum layer to a neural optimiser improves performance, since the classical FNN matches or exceeds the hybrid model in practical terms.
- #contradiction:scalability — Performance degrades substantially on structured problems such as MWIS and TSP, and the 4-qubit simulated quantum layer is too limited to support claims about scaling hybrid quantum optimisation.
## Contradictions
- The paper contradicts implicit hybrid-quantum-superiority claims by showing that its quantum layer is effectively inactive and provides no measurable benefit over a purely classical FNN.
- The paper also contradicts broad scalability narratives for near-term quantum optimisation: the quantum component is tested only as a 4-qubit simulation, D-Wave fails to embed some 200-variable instances, and both FNN/QCED degrade on harder structured QUBOs.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
