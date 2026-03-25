---
aliases:
- Quantum Deep Hedging
- Quantum Deep Hedging
authors:
- El Amine Cherrat
- Snehal Raj
- Iordanis Kerenidis
- Abhishek Shekhar
- Ben Wood
- Jon Dee
- Shouvanik Chakrabarti
- Richard Chen
- Dylan Herman
- Shaohan Hu
- Pierre Minssen
- Ruslan Shaydulin
- Yue Sun
- Romina Yalovetzky
- Marco Pistoia
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Quantum
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:59:58.429372'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:02.745551'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:01:06.931907'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:45.643596'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:19.063602'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:02:31.250690'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- topic/derivatives-pricing
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Deep Hedging
topic_tags:
- risk-modelling
- derivatives-pricing
year: 2023
zotero_key: ''
---

## Abstract summary
The paper introduces Quantum Deep Hedging, which integrates quantum machine learning into reinforcement-learning-based hedging frameworks for realistic financial markets with frictions. The authors design quantum neural network architectures using orthogonal and compound layers, prove trainability properties, and embed them into policy-search and (expected and distributional) actor-critic algorithms in both classical and quantum-accessible Deep Hedging environments. Through simulations and trapped-ion hardware experiments, they show that quantum models can match classical performance with fewer parameters and that quantum distributional actor-critic methods can outperform standard approaches on a GBM-based hedging task.
## Methodology
The paper presents an empirical study of quantum deep hedging using two methodological tracks: (1) quantum-enhanced deep hedging in a classical market environment, where classical policy-search reinforcement learning is combined with quantum orthogonal neural network layers embedded in feed-forward, recurrent, LSTM, and transformer architectures; and (2) a quantum-native deep hedging framework in a quantum environment, where compound-layer quantum neural networks are used for policy and value functions within expected actor-critic and distributional actor-critic reinforcement learning algorithms. The authors formulate hedging as a finite-horizon MDP with exponential utility as the objective, prove trainability properties for their Hamming-weight-preserving quantum neural networks, and then evaluate the methods through exact classical simulation, noisy hardware emulation, and real trapped-ion quantum hardware inference. In the classical-environment experiments, they benchmark classical linear layers against quantum orthogonal layers (Pyramid and Butterfly circuits) under policy-search deep hedging. In the quantum-environment experiments, they compare policy-search, expected actor-critic, and distributional actor-critic using compound neural networks. Performance is assessed primarily via expected utility and terminal profit-and-loss (PnL), with comparisons against classical neural architectures and the Black-Scholes delta hedge baseline. Hardware validation is performed on Quantinuum H1-1 and H1-2 processors using classically pre-trained models, with up to 16 qubits for orthogonal-layer models and up to 12 qubits for compound-layer models.

**Algorithms used:** Policy-search Deep Hedging, Actor-Critic Deep Hedging, Distributional Actor-Critic, Expected Actor-Critic, Quantum Reinforcement Learning, Quantum Neural Networks, Orthogonal Layers, Compound Layers
**Frameworks:** Quantinuum H1-1, Quantinuum H1-2

**Experimental setup:** Experiments were conducted in three modes: exact classical simulation, noisy hardware emulation, and real trapped-ion QPU inference. For classical-market experiments, quantum orthogonal neural networks were evaluated within feed-forward, recurrent, LSTM, and transformer models using 16-qubit orthogonal layers and compared with classical linear-layer counterparts. Exact simulations used batches of 256 paths over 30 trading days; hardware-emulation experiments used Quantinuum H1-1 emulator with 32 paths and 1000 measurement shots per circuit evaluation; hardware runs used Quantinuum H1-1 with 4 paths over 5 trading days for LSTM and transformer models. For quantum-market experiments, compound neural networks were trained in exact classical simulation and evaluated via exact simulation, Quantinuum H1-1 emulator, and Quantinuum H1-1/H1-2 hardware. Compound-layer simulations were limited to up to 12 qubits due to exponential state-space cost. All compound QNN parameters were Gaussian-initialized, and training was performed classically; hardware was used for inference only.

**Dataset:** Synthetic financial data generated from Black-Scholes/Geometric Brownian Motion (GBM) market models. In the classical environment, the underlying asset price followed GBM and the hedging task involved a European short call option with strike K = S0, over a 30-day horizon with daily rebalancing, with and without proportional transaction costs. Training used 9.6×10^4 simulated samples and testing used 2.4×10^4 samples. In the quantum environment, a discretized GBM was constructed via Bernoulli random variables approximating Brownian motion, with 10-day maturity, strike k = 1, and cases with and without transaction costs.
## Experiment details
### Input
Classical-environment input: synthetic GBM stock-price paths with drift mu = 0 and volatility sigma = 0.2, dt = 1/252, 30 trading days, daily rebalancing, one hedging instrument (equity), and a European short call option with strike K = S0. Market state was the sequence of past and current prices. Training set size was 9.6e4 samples and test set size was 2.4e4 samples. Transaction-cost setting used proportional cost coefficient 0.01. Quantum-environment input: discretized GBM using Bernoulli variables to approximate Brownian motion, with n = 1 Bernoulli variable per day, maturity 10 days, drift mu = 0, volatility sigma = 0.2, effective time increment adjusted to 30 trading days because of qubit limits, strike k = 1, and transaction-cost coefficient epsilon = 0.002 in the cost setting. Hardware inference subsets used 32 paths, 16 paths, 8 paths, or 4 paths depending on experiment.

### Process
Classical-environment process: 1) Simulate GBM market paths. 2) Encode the time series of market observations as inputs to feed-forward, recurrent, LSTM, or transformer models. 3) Replace classical linear layers with quantum orthogonal layers (Pyramid or Butterfly) using 16 qubits, while keeping comparable architecture and hyperparameters. 4) Train policies with policy-search deep hedging by minimizing the exponential-utility loss over sampled episodes. 5) Evaluate via exact simulation, then perform inference under noisy emulator and real hardware using tomography over the unary basis. For hardware-emulation runs, downsized single-layer networks were used; Feed-forward/Recurrent required 1 circuit evaluation per time step, LSTM 4, Transformer 3; 1000 shots were used per circuit evaluation. Quantum-environment process: 1) Build a quantum-accessible discretized GBM environment using Bernoulli jump encodings and transition oracles. 2) Construct compound-layer QNNs for policy and value functions using Hamming-weight-preserving circuits. 3) Train policy-search, expected actor-critic, and distributional actor-critic variants in exact classical simulation. 4) Use Huber loss and scale the value function to avoid exploding gradients. 5) Train for 2000 steps with Adam, using batch size 16 and 3 random seeds. 6) Select best parameters and evaluate on exact simulation, emulator, and trapped-ion hardware. Hardware experiments used reduced circuit depth per block relative to the logarithmic-depth simulation design to fit hardware constraints.

### Output
Reported outputs include expected utility under exponential utility, terminal profit-and-loss (PnL) for individual paths, number of trainable parameters, and number of circuit evaluations/circuits. Baseline comparisons include classical neural-network versions of feed-forward, recurrent, LSTM, and transformer architectures; comparison among policy-search, expected actor-critic, and distributional actor-critic training methods; simulator versus emulator versus real hardware performance; and comparison against the standard Black-Scholes delta-hedging model in the quantum-environment experiments. Main findings emphasize comparable utility with fewer parameters for orthogonal-layer models and superior performance of distributional actor-critic over policy-search and expected actor-critic.

### Parameters
- classical_environment: {'gbm_drift_mu': 0, 'gbm_volatility_sigma': 0.2, 'dt': '1/252', 'time_horizon_days': 30, 'rebalancing_frequency': 'daily', 'strike_price': 'K = S0', 'transaction_cost_coefficient': 0.01, 'training_samples': 96000, 'test_samples': 24000, 'feature_size_classical_layers': 16, 'qubits_orthogonal_layers': 16, 'batch_size_exact_simulation': 256, 'batch_size_hardware_emulation': 32, 'hardware_time_horizon_days': 5, 'hardware_paths': 4, 'shots_per_circuit_evaluation': 1000}
- quantum_environment: {'bernoulli_variables_per_day_n': 1, 'gbm_drift_mu': 0, 'gbm_volatility_sigma': 0.2, 'maturity_days': 10, 'effective_time_step': '30 trading days', 'strike_price': 1, 'transaction_cost_coefficient': 0.002, 'training_steps': 2000, 'optimizer': 'Adam', 'random_seeds': 3, 'batch_size': 16, 'max_qubits_compound_simulation': 12, 'max_qubits_hardware_orthogonal': 16, 'max_qubits_hardware_compound': 12}
- architectures: {'orthogonal_layer_circuits': ['Pyramid', 'Butterfly'], 'compound_layer_circuit': 'Brick', 'feedforward_hidden_layer_repetitions': 3, 'recurrent_hidden_layer_repetitions': 3, 'lstm_hidden_cell_layers': 4, 'transformer_hidden_layers': 3, 'transformer_attention_layers': 2}

### Hardware
Real-hardware inference was run on Quantinuum H1-1 and H1-2 trapped-ion quantum processors; noisy emulation used the Quantinuum H1-1 emulator. Orthogonal-layer hardware experiments used 16-qubit Butterfly circuits, leveraging all-to-all connectivity. Compound-layer hardware experiments used up to 12 qubits. For orthogonal-layer emulator experiments, 1000 measurement shots per circuit evaluation were used to perform tomography over the unary basis. Some experiments reduced network depth or used fixed depth per block to fit hardware limitations. Training itself was done in exact classical simulation; hardware was used only for inference.

### Reproducibility
Code is stated to be available upon request rather than openly released. Synthetic data generation is described in substantial detail (GBM/discretized GBM parameters, horizons, costs, sample sizes, architecture choices), and many experimental settings are reported, but some implementation details and hyperparameters are not fully specified. Overall, partial reproducibility is possible, but exact replication may require access to the authors' code and Quantinuum hardware/emulator settings.
## Findings
- [supported] In classical-environment simulations of deep hedging, quantum orthogonal neural networks achieved performance comparable to classical counterparts while using fewer trainable parameters.
- [supported] In the 30-day GBM hedging benchmark without transaction costs, utilities for quantum orthogonal models were close to classical baselines: Feed-forward classical -2.868 vs Pyramid -2.873 vs Butterfly -2.874; Recurrent classical -2.933 vs Pyramid -2.939 vs Butterfly -2.931; LSTM classical -2.853 vs Pyramid -2.856 vs Butterfly -2.879; Transformer classical -2.865 vs Pyramid -2.876 vs Butterfly -2.861.
- [supported] In the same benchmark with transaction costs, quantum orthogonal models remained competitive: Feed-forward classical -5.064 vs Pyramid -5.048 vs Butterfly -5.043; Recurrent classical -5.075 vs Pyramid -5.102 vs Butterfly -4.854; LSTM classical -4.743 vs Pyramid -4.755 vs Butterfly -4.787; Transformer classical -4.713 vs Pyramid -4.806 vs Butterfly -4.822.
- [supported] Quantum orthogonal models reduced parameter counts relative to classical models in all tested architectures; for example Feed-forward used 881 parameters classically vs 521 (Pyramid) and 257 (Butterfly), LSTM used 569 vs 457 and 217, and Transformer used 1905 vs 1305 and 865.
- [supported] On Quantinuum H1-1 emulator, orthogonal-layer models showed moderate noise robustness, with LSTM exhibiting the closest agreement between exact simulation and emulator under transaction costs: utility -4.809 in simulation vs -4.866 on emulator.
- [supported] On real Quantinuum H1-1 hardware, a 16-qubit LSTM with Butterfly orthogonal layers showed close agreement with noiseless simulation over 4 paths and 5 trading days: utility -2.176 in simulation vs -2.194 on hardware.
- [supported] On the same real-hardware test, the Transformer with Butterfly layers degraded more under noise than LSTM: utility -2.195 in simulation vs -2.539 on hardware.
- [supported] In the quantum-environment experiments using compound neural networks, the distributional actor-critic algorithm outperformed both policy-search and expected actor-critic in exact simulation, both without costs (-3.875 vs -4.064 and -4.193) and with costs (-4.424 vs -4.639 and -4.668).
- [supported] In Quantinuum H1-1 emulator tests for the quantum-environment setting, distributional actor-critic again performed best and matched exact simulation closely under transaction costs: policy-search -4.257 simulation vs -4.277 emulator, expected actor-critic -4.528 vs -4.531, distributional actor-critic -4.185 vs -4.180.
- [supported] On real Quantinuum H1-1/H1-2 hardware in the quantum-environment setting, both expected and distributional actor-critic policies outperformed the Black-Scholes delta hedge baseline on 8 paths with transaction costs, with utilities of -3.501 and -3.369 on hardware versus -4.884 for Black-Scholes.
- [supported] The distributional actor-critic policy achieved the best overall hardware performance in the quantum-environment experiment, with utility -3.369 on hardware compared with -3.501 for expected actor-critic and -4.884 for Black-Scholes.
- [supported] The paper's empirical results are primarily from classical simulation plus inference on real trapped-ion hardware; training of all quantum neural networks was performed in exact classical simulation rather than on quantum hardware.
- [supported] The authors successfully implemented inference for proposed models on trapped-ion quantum processors using circuits up to 16 qubits for orthogonal-layer models and up to 12 qubits for compound-layer models, observing close alignment with noiseless simulation in several cases.
- [speculative] The authors argue that their quantum deep hedging framework is more general than the classically simulable instances used in experiments and could become classically hard to simulate with suitable input states.
- [speculative] The paper proves trainability results for the proposed Hamming-weight-preserving quantum neural networks, claiming gradient variance decays only polynomially with qubit number under stated initialization and measurement assumptions, but these are theoretical rather than directly empirically quantified in the finance experiments.
- [speculative] The authors suggest the quantum reinforcement learning techniques may generalize beyond hedging to other finance tasks such as algorithmic trading or option pricing.

**Results summary:** The paper presents quantum deep hedging methods based on quantum orthogonal layers for classical market environments and compound-layer quantum neural networks for quantum-accessible environments. Empirically, in GBM-based hedging simulations, orthogonal-layer quantum models matched classical feed-forward, recurrent, LSTM, and transformer baselines while using substantially fewer parameters. In the quantum-environment setting, a new distributional actor-critic method consistently outperformed both policy-search and expected actor-critic variants in exact simulation and emulator tests. The authors also ran inference on Quantinuum trapped-ion hardware, using up to 16 qubits for orthogonal-layer models and up to 12 qubits for compound-layer models, and found that hardware results generally tracked noiseless simulation well, especially for LSTM and distributional actor-critic models. Training was done in classical simulation, so the empirical evidence is simulation-backed with hardware inference validation rather than end-to-end quantum training.

**Performance claims:**
- Feed-forward utility without costs: classical -2.868, Pyramid -2.873, Butterfly -2.874
- Feed-forward utility with costs: classical -5.064, Pyramid -5.048, Butterfly -5.043
- Recurrent utility without costs: classical -2.933, Pyramid -2.939, Butterfly -2.931
- Recurrent utility with costs: classical -5.075, Pyramid -5.102, Butterfly -4.854
- LSTM utility without costs: classical -2.853, Pyramid -2.856, Butterfly -2.879
- LSTM utility with costs: classical -4.743, Pyramid -4.755, Butterfly -4.787
- Transformer utility without costs: classical -2.865, Pyramid -2.876, Butterfly -2.861
- Transformer utility with costs: classical -4.713, Pyramid -4.806, Butterfly -4.822
- Parameter counts: Feed-forward 881 classical vs 521 Pyramid vs 257 Butterfly
- Parameter counts: Recurrent 881 classical vs 521 Pyramid vs 257 Butterfly
- Parameter counts: LSTM 569 classical vs 457 Pyramid vs 217 Butterfly
- Parameter counts: Transformer 1905 classical vs 1305 Pyramid vs 865 Butterfly
- Orthogonal-layer emulator results with costs: Feed-forward -5.041 simulation vs -5.155 emulator
- Orthogonal-layer emulator results with costs: Recurrent -5.006 simulation vs -5.333 emulator
- Orthogonal-layer emulator results with costs: LSTM -4.809 simulation vs -4.866 emulator
- Orthogonal-layer emulator results with costs: Transformer -4.846 simulation vs -5.176 emulator
- Real hardware orthogonal-layer LSTM utility: -2.176 simulation vs -2.194 hardware over 4 paths and 5 trading days
- Real hardware orthogonal-layer Transformer utility: -2.195 simulation vs -2.539 hardware over 4 paths and 5 trading days
- Quantum-environment exact simulation utilities without costs: policy-search -4.064, expected actor-critic -4.193, distributional actor-critic -3.875
- Quantum-environment exact simulation utilities with costs: policy-search -4.639, expected actor-critic -4.668, distributional actor-critic -4.424
- Quantum-environment emulator utilities with costs: policy-search -4.257 simulation vs -4.277 emulator
- Quantum-environment emulator utilities with costs: expected actor-critic -4.528 simulation vs -4.531 emulator
- Quantum-environment emulator utilities with costs: distributional actor-critic -4.185 simulation vs -4.180 emulator
- Quantum-environment real hardware utilities with costs over 8 paths: Black-Scholes -4.884, expected actor-critic -3.501, distributional actor-critic -3.369
- Hardware sizes: up to 16 qubits for orthogonal-layer inference and up to 12 qubits for compound-layer inference
- Training setup examples: 9.6e4 training samples and 2.4e4 test samples in the classical-environment benchmark; 2000 training steps with batch size 16 and 3 random seeds in the quantum-environment benchmark
## Quantum advantage claim
**Classification:** speculative

The paper shows competitive performance, parameter reduction, and successful hardware inference, but it does not demonstrate a clear quantum speedup or superior end-to-end performance over best classical methods attributable uniquely to quantum computation. Many results are from classical simulation with quantum-inspired architectures, and the authors explicitly note some experimental circuits are classically simulable.
## Limitations
- Hardware experiments were limited to small problem sizes, with circuits using up to 16 qubits for orthogonal-layer models and up to 12 qubits for compound-layer models.
- Hardware experiments used a reduced maturity horizon (10 days in the quantum-environment setting, and 5 days for some orthogonal-layer hardware runs), rather than longer realistic hedging horizons.
- Training of all quantum neural networks was performed in exact classical simulation rather than on quantum hardware.
- The authors state that classical simulation of training 'very soon becomes infeasible,' which constrained the maturity and scale of the hardware experiments.
- The classical-environment experiments used a simplified toy market model based on Geometric Brownian Motion / Black-Scholes rather than richer real-market dynamics.
- The quantum-environment experiments used a discretized approximation to Brownian motion with n = 1 Bernoulli variable per day, a coarse approximation of market dynamics.
- The quantum-environment setup required changing the time increment from 252 trading days to 30 trading days to fit simulation limits, reducing realism.
- The experiments considered a single hedging instrument and a European short call option, limiting generality across multi-asset or more complex derivatives portfolios.
- The paper notes that some circuits used in the numerical experiments may be classically simulatable with only polynomial overhead, weakening claims of practical quantum advantage for the demonstrated setups.
- The distributional actor-critic results are demonstrated on a 'toy example,' so empirical evidence for broader financial applicability remains limited.
- The code is only 'available upon request,' which limits reproducibility compared with fully open public release.
- [inferred] No benchmarking against strong state-of-the-art classical deep hedging baselines beyond matched classical neural architectures is reported, so relative practical advantage versus best classical methods is unclear.
- [inferred] The use of synthetic/generated market paths instead of real historical market data limits external validity for production financial services use cases.
- [inferred] Sample sizes, while nontrivial (e.g., 9.6e4 training samples in one setting), remain modest relative to industrial-scale financial training pipelines.
- [inferred] Scalability to production is unproven because inference/hardware tests were run on very small batches and short horizons, with no end-to-end latency or deployment analysis.
- [inferred] Hardware validation focused on inference of classically pre-trained models, so robustness of full on-hardware training under noise and shot constraints was not empirically established.
- [inferred] Noise robustness claims are based on close agreement with emulator/hardware in small settings, but not stress-tested under larger circuits, longer horizons, or more severe noise regimes.
- [inferred] The action-independence assumption in the Deep Hedging model (no market impact) simplifies the environment and may limit validity for realistic trading settings with feedback effects.
## Open questions
- How can the trainability results for the proposed quantum neural networks be extended to other settings beyond those analyzed in the paper?
- How can the quantum environment built for Geometric Brownian Motion / Black-Scholes be extended to other market models such as the Heston model?
- How can new distributional losses using temporal-difference methods be designed for Deep Hedging?
- Beyond matching expectations, which additional moments of the value distribution should be matched, both overall and per Hamming-weight subspace?
- Can Quantum Deep Hedging be trained directly on quantum hardware at larger maturities and scales than are classically simulable?
- Do the proposed methods retain their performance advantages on more realistic, higher-dimensional, and multi-asset hedging problems?
- Under what conditions do the proposed quantum models provide a genuine computational or financial advantage over advanced classical compression or pruning methods?
- How well do the methods generalize from toy/simulated environments to real financial market data and realistic frictions?

**Future work:**
- Extend the trainability analysis of the proposed quantum neural networks to broader settings.
- Develop quantum environments for richer stochastic market models beyond GBM, such as the Heston model.
- Design new distributional loss functions for Deep Hedging that use temporal-difference learning.
- Explore moment-matching approaches that capture not only expectations but also higher moments of the value distribution, globally and per subspace.
- Train Quantum Deep Hedging models directly on quantum hardware using methods such as the parameter-shift rule.
- Scale hardware-trained models to longer maturities, potentially a month or more, as hardware improves.
- Apply the proposed quantum reinforcement learning methods to other finance problems such as algorithmic trading and option pricing.
- Investigate broader use of quantum distributional reinforcement learning beyond Deep Hedging.
- [inferred] Evaluate the methods on real historical market data and more realistic market frictions.
- [inferred] Benchmark against stronger classical baselines, including compressed/pruned classical models and state-of-the-art deep hedging solvers.
- [inferred] Study scalability to larger qubit counts, longer horizons, and multi-asset portfolios under realistic hardware noise and resource constraints.
- [inferred] Publicly release code, experiment configurations, and data-generation pipelines to improve reproducibility.
## Key ideas
- #idea:hybrid-approach — The paper proposes quantum deep hedging as a hybrid workflow where quantum neural-network layers are classically trained and then executed for inference on trapped-ion hardware.
- #idea:near-term-feasibility — Real QPU inference on Quantinuum H1-1/H1-2 with up to 16 qubits shows that small hedging models can be run on current hardware with results often close to noiseless simulation.
- #idea:quantum-advantage — Quantum orthogonal-layer models match classical deep hedging baselines with substantially fewer trainable parameters, suggesting a possible expressivity or compression benefit.
- #idea:quantum-advantage — In the quantum-environment setting, quantum distributional actor-critic outperforms policy-search, expected actor-critic, and the Black-Scholes delta hedge baseline on the toy GBM hedging task.
- #idea:hybrid-approach — The study combines reinforcement-learning-based deep hedging with quantum neural networks in both classical-market and quantum-accessible market environments.
- #idea:near-term-feasibility — The paper emphasizes NISQ-compatible architectures such as orthogonal and compound Hamming-weight-preserving circuits designed for trainability and hardware execution.
- #idea:quantum-advantage — The authors speculate that the framework could become classically hard to simulate for richer input states, though this is not demonstrated empirically.
## Contradictions
- The paper suggests potential quantum advantage via parameter efficiency and improved toy-task performance, but its own quantum-advantage assessment is explicitly speculative: no clear end-to-end speedup over strong classical methods is shown, and many experiments use classically simulable circuits. This supports contradiction:classical-vs-quantum.
- The paper presents successful hardware inference as evidence of practicality, yet scalability is undermined by the need to restrict experiments to 12–16 qubits, short horizons, tiny path counts, and classically simulated training. This supports contradiction:scalability.
- Although hardware results sometimes outperform the Black-Scholes delta hedge baseline, the stronger matched classical neural baselines are only competitive or essentially tied with the quantum models in the classical-environment experiments, weakening any broad superiority claim.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
