---
aliases:
- Quantum versus classical generative modelling in finance
- Quantum versus classical generative
authors:
- Brian Coyle
- Maxwell Henderson
- Justin Chan Jin Le
- Neeraj Kumar
- Marco Paini
- Elham Kashefi
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1088/2058-9565/abd3db
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Quantum Science and Technology
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:53:02.766152'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:53:06.955040'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:53:36.051320'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:54:06.866242'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:54:37.205359'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:54:46.479810'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/market-simulation
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum versus classical generative modelling in finance
topic_tags:
- market-simulation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper compares a fully quantum generative model (a quantum circuit Born machine) with a classical restricted Boltzmann machine for synthetic data generation on a real financial dataset of FX currency pair returns encoded in binary form. Using matched model capacities and several training objectives, the authors evaluate performance via an adversarial discriminator and show that the simulated quantum model consistently matches or exceeds the classical model, with clearer advantages at higher data precision. They also implement and partially train larger quantum models on Rigetti hardware, and analyze entanglement properties of the trained circuits, observing that instances where the quantum model outperforms the RBM tend to exhibit higher entangling capability.
## Methodology
The study is a peer-reviewed empirical comparison of classical and quantum generative models for synthetic financial data generation. The authors train and evaluate a restricted Boltzmann machine (RBM) and a quantum circuit Born machine (QCBM) on a real-world foreign-exchange dataset of correlated currency-pair log-returns. To ensure a fair comparison, they constrain both models to have matched numbers of trainable parameters, initially training only local parameters: single-qubit rotation angles in the QCBM and node biases in the RBM, while keeping QCBM entangling gates fixed and RBM weights randomly initialized and fixed. The QCBM uses hardware-efficient ansätze tailored to Rigetti Aspen chip connectivity, and is trained primarily with the Sinkhorn divergence using analytic gradients via the parameter-shift rule and the Adam optimizer. The RBM is trained by maximizing log-likelihood with vanilla gradient descent, with model samples generated using QxSQA, a GPGPU-accelerated simulated quantum annealer. Experiments are conducted across multiple problem sizes by varying the number of currency pairs and bit precision after discretizing each pair into binary form. Performance is assessed mainly through an adversarial random-forest discriminator that distinguishes real from generated samples, with higher discriminator error indicating better generative quality; additional qualitative comparison uses QQ plots, and the authors also analyze the Meyer-Wallach entangling capability of trained QCBM states. The work includes both simulator-based and real-hardware experiments on Rigetti QPUs, including partial training of a 28-qubit QCBM.

**Algorithms used:** QCBM, RBM, Sinkhorn divergence training, Adam, parameter-shift rule, log-likelihood maximization, vanilla gradient descent, QxSQA, random forest discriminator, MMD, genetic algorithm
**Frameworks:** Rigetti QCS, PyQuil, scikit-learn

**Experimental setup:** Experiments were run on both simulated and physical Rigetti quantum hardware using hardware-efficient QCBM circuits matched to Aspen-7 and Aspen-8 chip topologies. Simulated QCBM runs used Rigetti noisy-QVM-style noise models including readout error and T1/T2 effects. Physical runs were executed on Rigetti Aspen sublattices including 4-, 6-, 8-, 10-, 12-, and 28-qubit configurations. RBM sampling used QxSQA, a GPGPU-accelerated simulated quantum annealer. The main QCBM training used Sinkhorn divergence with Adam; the RBM used log-likelihood maximization with gradient descent. Multiple problem sizes were tested by mapping binary-encoded financial variables to qubits/visible nodes.

**Dataset:** A real-world financial dataset of 5070 daily log-return samples for four FX currency pairs over 1999-2019. The paper states that spot prices of each currency pair were converted into 16-bit binary values, yielding 64-bit samples, and smaller problem instances were formed by selecting subsets of currency pairs and lower bit precision.
## Experiment details
### Input
Financial input data consisted of 5070 samples of daily log-returns for 4 currency pairs (including EUR/USD and GBP/USD, with the paper referring to four total FX pairs) from 1999-2019. Each currency pair's spot price series was discretized into a 16-bit binary representation, producing 64-bit samples overall. Problem size was controlled by selecting i currency pairs and j bits of precision per pair, denoted (i, j), e.g., 2 pairs at 2, 3, 4, or 6 bits; 3 pairs at 2 or 4 bits; 4 pairs at 2, 3, or 7 bits. A simple one-to-one mapping from variables to qubit indices was used; no alternative embedding strategies were explored in the main experiments.

### Process
1. Prepare binary-encoded FX return data at a chosen problem size (number of currency pairs and bit precision). 2. Construct a hardware-efficient QCBM ansatz aligned with the selected Rigetti chip sublattice, using an initial layer of Ry rotations followed by repeated layers of native CZ entanglers and Ry rotations; an n-qubit, l-layer circuit has n*l trainable parameters. 3. Build a matched RBM with n visible nodes and enough hidden nodes to match the QCBM parameter count; in the main setup only node biases are trained while weights are random and fixed. 4. Train the QCBM by minimizing Sinkhorn divergence between generated and data samples using analytic gradients from the parameter-shift rule and the Adam optimizer. 5. Train the RBM by maximizing log-likelihood using vanilla gradient descent, estimating model expectations from samples generated by QxSQA simulated quantum annealing. 6. In all cases, use 250 samples from the data and 250 model-generated samples per training step. 7. Evaluate generative quality during training using a scikit-learn random forest discriminator with 1000 estimators; higher discriminator error indicates generated samples are harder to distinguish from real data. 8. Repeat selected experiments over 5 independent runs and report mean and standard deviation where feasible. 9. For additional analysis, compute QQ plots of marginal distributions and estimate Meyer-Wallach entangling capability of initial and trained QCBM states. 10. Supplementary experiments compare alternative QCBM training methods including MMD, adversarial training, and a genetic algorithm, and explore varying QCBM layers, RBM hidden nodes, and RBM weight training.

### Output
Primary outputs are discriminator error curves from a random forest classifier distinguishing real versus generated samples, with 50% error representing indistinguishability and thus better generative performance. The paper compares QCBM versus RBM across problem sizes and also compares simulated QCBM versus QPU-executed QCBM. Additional outputs include QQ plots of marginal distributions for generated versus real data, entangling capability values of trained QCBM states, and qualitative conclusions about whether the QCBM matches or outperforms the RBM as precision and scale increase. Baselines/comparisons include RBM as the classical baseline, simulated versus hardware QCBM, and in appendices alternative QCBM training objectives such as MMD, adversarial discriminator training, and genetic algorithms.

### Parameters
- qcbm_qubits_tested: [4, 6, 8, 10, 12, 28]
- qcbm_layers_main_setting: 2
- qcbm_trainable_parameters_formula: n_qubits * n_layers
- single_qubit_gate: Ry
- entangling_gate: CZ
- qcbm_optimizer: Adam
- qcbm_initial_learning_rate: 0.05
- sinkhorn_epsilon: 0.5
- samples_per_step_data: 250
- samples_per_step_model: 250
- rbm_training_objective: log-likelihood maximization
- rbm_optimizer: vanilla gradient descent
- rbm_hidden_nodes_formula_main: n * (l - 1)
- discriminator_model: RandomForestClassifier
- discriminator_estimators: 1000
- independent_runs_reported: 5
- qxsqa_parameters: {'Gamma0': 3, 'Gamma_tau': 1e-20, 'Nsweeps': 1, 'PT': 0.1, 'Nanneals': 250, 'Teff': 1}
- mmd_kernel: Gaussian mixture kernel
- mmd_bandwidths: [0.25, 10, 1000]

### Hardware
Quantum experiments used Rigetti Aspen-7 and Aspen-8 superconducting QPUs via Rigetti Quantum Cloud Services (QCS). Specific sublattices included Aspen-7-4Q-C, Aspen-7-6Q-C, Aspen-7-8Q-C, 10-qubit and 12-qubit Aspen-8 sublattices, and Aspen-7-28Q-A with 28 usable qubits. Circuits were designed to be close to hardware-native, using native CZ connectivity and Ry rotations decomposed into Rigetti-native single-qubit rotations. Further compilation was left to the Rigetti compiler. Simulated experiments used the noisy-QVM noise model from PyQuil, including readout errors and standard T1/T2 noise.

### Reproducibility
The paper provides substantial methodological detail: dataset size and period, encoding scheme, circuit structures, training objectives, optimizer settings, sample counts, discriminator configuration, and QxSQA parameters. It also names the hardware platform and simulator noise model. However, the text does not explicitly state that code was released, and the exact raw data source for the FX series is not clearly specified in the excerpt. Reproducibility is moderate: the study is largely replicable in principle, but full replication would benefit from code, exact data source/access details, and more complete training schedules/iteration counts.
## Findings
- [supported] On a real-world FX dataset of 5070 daily samples from 4 currency pairs (1999–2019), the simulated QCBM always matched or exceeded the RBM under the authors' matched-parameter experimental setup.
- [supported] The simulated QCBM showed superior performance to the RBM as problem precision/model scale increased, with the crossover becoming apparent around 4 bits of precision for 2 currency pairs.
- [supported] For 2 currency pairs at 4 and 6 bits of precision, the QCBM achieved higher random-forest discriminator error than the RBM, indicating generated samples were harder to distinguish from real data.
- [supported] For 3 currency pairs, similar QCBM-over-RBM behavior was observed at 4 bits of precision in simulation.
- [supported] For 4 currency pairs at 2–3 bits of precision, QCBM and RBM performance was similar, with only a possible small QCBM advantage.
- [supported] Experiments were conducted on both simulation and Rigetti Aspen quantum hardware; hardware runs partially reproduced learning behavior on small instances, though below simulated performance.
- [supported] The authors report partial training on a 28-qubit Rigetti Aspen-7 device, which they describe as the largest QCBM instance trained to date in the literature.
- [supported] In the 28-qubit hardware experiment (4 currency pairs at 7 bits precision), the QCBM learned nontrivially, reaching about 20% discriminator error, but remained substantially worse than the RBM.
- [supported] Trained QCBMs that outperformed RBMs tended to exhibit higher Meyer-Wallach entanglement capability after training than instances where no advantage was observed.
- [speculative] The correlation between higher trained-state entanglement and QCBM outperformance suggests entanglement may contribute to the observed advantage.
- [supported] Increasing QCBM layers or RBM hidden nodes beyond the main-text settings did not materially improve final performance on the tested small problem sizes, suggesting parameter saturation in those regimes.
- [supported] Training RBM weights in addition to biases improved convergence speed and helped larger RBMs, but the QCBM still outperformed 8- and 12-visible-node RBMs in the reported comparisons.
- [speculative] The authors suggest hardware underperformance at larger scale is likely due to quantum noise and possibly ansatz limitations rather than absence of QCBM expressive advantage.
- [speculative] The paper argues for an expressive-power advantage of Born machines over classical models in some settings, but does not demonstrate computational speedup or fault-tolerant quantum advantage.

**Results summary:** This peer-reviewed empirical study compares a quantum circuit Born machine (QCBM) with a restricted Boltzmann machine (RBM) for generative modeling of foreign-exchange log-return data encoded into binary strings. Using matched parameter counts and a random-forest discriminator as the main evaluation metric, the authors report that simulated QCBMs consistently matched or outperformed RBMs, with the advantage becoming clearer as precision increased. For 2 currency pairs, the QCBM began to outperform the RBM around 4 bits of precision and remained stronger at 6 bits; similar behavior was observed for 3 currency pairs at 4 bits, while 4-pair tasks at lower precision showed near parity. The study includes both noisy simulation and runs on Rigetti Aspen hardware, including partial training of a 28-qubit QCBM on real hardware. Hardware results showed learning but degraded performance relative to simulation and relative to the RBM at the largest scale. The authors also found that cases where the QCBM outperformed the RBM were associated with higher entanglement capability in the trained circuits, though this mechanistic interpretation remains inferential rather than conclusively established.

**Performance claims:**
- Dataset: 5070 samples of daily log-returns from 4 currency pairs over 1999–2019
- Data encoding: each currency pair converted to 16-bit binary values, yielding 64-bit full samples
- QCBM outperformed RBM for 2 currency pairs at 4-bit and 6-bit precision according to higher random-forest discriminator error
- QCBM showed similar advantage trend for 3 currency pairs at 4-bit precision
- For 4 currency pairs at 2-bit and 3-bit precision, QCBM and RBM performed similarly, with only a possible QCBM edge
- Largest hardware experiment: 28-qubit QCBM on Rigetti Aspen-7 for 4 currency pairs at 7-bit precision
- 28-qubit hardware QCBM reached approximately 20% discriminator error during training
- Random-forest discriminator used 1000 estimators
- Error bars, where shown, are mean and standard deviation over 5 independent training runs
- QCBM and RBM training commonly used 250 samples from data and 250 model samples per iteration
## Quantum advantage claim
**Classification:** speculative

The paper presents empirical evidence that simulated QCBMs can outperform matched RBMs on this finance generative-modeling task, and includes limited real-hardware experiments. However, the advantage is task-specific, based mainly on simulation, not a demonstrated computational speedup, and the largest hardware result underperforms the classical baseline. Thus the paper supports a possible expressive advantage but not a definitive demonstrated quantum advantage.
## Limitations
- Experiments are restricted to small problem sizes and NISQ-era devices; the study explicitly focuses on small, error-prone quantum computers.
- Physical-hardware results are limited by quantum errors; the authors note that diminishing performance on larger hardware runs is most likely caused by hardware noise.
- The largest 28-qubit QCBM could not be classically simulated in a reasonable amount of time, preventing a direct simulated-vs-hardware comparison at that scale.
- The 28-qubit hardware result underperforms the RBM counterpart, and the authors cannot rule out whether this is due to hardware errors, ansatz choice, or other factors.
- The comparison is simplified by training only local parameters in both models: only single-qubit unitaries are trained in the QCBM and only node biases are trained in the RBM in the main experiments.
- RBM weights are randomly chosen and fixed in the main setup, which constrains the classical baseline and may not reflect the strongest possible RBM performance.
- The study uses a specific hardware-efficient ansatz closely matched to Rigetti chip topology; ansatz dependence is acknowledged and not fully explored.
- Potential barren plateau issues are not addressed; the authors state this is primarily because they consider only small problem sizes.
- The dataset is relatively small, consisting of 5070 samples of daily log-returns, which may limit statistical power and generalization.
- The financial data are discretized into binary strings (16 bits per currency pair), so results depend on a particular encoding choice and may lose information from the original continuous data.
- Only one real-world financial dataset/domain is studied (FX currency pairs), limiting external validity across other financial services tasks.
- The classical comparison suite is narrow, focusing mainly on RBMs rather than a broader set of state-of-the-art classical generative models.
- The fairness criterion is based on matching the number of trainable parameters, but the authors note it is difficult to directly compare model connectivity/capacity across QCBMs and RBMs.
- QCBM simulations use a simple noise model ('readout errors and standard T1 and T2 times'), which may not capture all real-device noise sources.
- Approximate RBM sampling via QxSQA introduces a source of model error, even though prior work suggests it is near exact for relevant sizes.
- Only a simple one-to-one mapping from variables to qubits is used; alternative embedding methods that may affect performance are not investigated.
- The necessary sample sizes for successful training are not studied; all experiments use 250 samples from data and model for simplicity.
- Reproducibility on other hardware platforms may be limited because the experiments are tightly coupled to Rigetti Aspen chip topologies and the Rigetti QCS/PyQuil stack.
- [inferred] Several authors are affiliated with Rigetti Computing, and the hardware experiments are conducted exclusively on Rigetti systems, which may introduce platform-specific bias.
- [inferred] No comparison is reported against modern classical deep generative models such as GANs, VAEs, normalizing flows, or diffusion-based approaches, so claims of practical advantage remain limited.
- [inferred] Scalability to production financial synthetic-data generation is unproven, since experiments remain at low qubit counts, low precision settings, and limited asset universes.
- [inferred] The use of discriminator error as the primary benchmark may not fully capture downstream utility, calibration, tail-risk fidelity, or regulatory relevance for financial applications.
- [inferred] The study does not report extensive robustness checks across time periods, market regimes, or out-of-sample stress scenarios.
## Open questions
- How can useful near-term quantum applications in finance be identified concretely?
- Why does the QCBM outperform the RBM on some higher-precision instances, and what role does entanglement play in that advantage?
- Is the observed correlation between higher trained-state entanglement and better QCBM performance causal or merely coincidental?
- How will barren plateau effects impact training as QCBMs scale to larger problem sizes?
- How can problem information be incorporated effectively into data-driven QML ansatz design to avoid barren plateaus?
- What is the best ansatz choice for financial generative modeling on quantum hardware?
- How much of the performance degradation on larger hardware runs is due to noise versus ansatz limitations or optimization issues?
- What sample sizes are necessary for successful and stable training of QCBMs and RBMs in this setting?
- How much does variable-to-qubit embedding affect QCBM performance on structured financial datasets?
- Would mixed-state quantum models or Hamiltonian-based models provide materially greater expressive power than pure-state QCBMs for this task?
- How should classical and quantum resources be optimally divided in hybrid learning procedures?
- Do the reported advantages persist when compared against a broader range of strong classical generative models?
- Can the observed results generalize beyond FX log-return data to other financial services datasets and tasks?

**Future work:**
- Improve Born machine training speed, for example through GPU-accelerated computation of cost functions.
- Incorporate techniques to improve QPU running time and execution efficiency.
- Investigate variable-structure ansatze for the QCBM.
- Explore quantum-specific optimizers for training the model.
- Enlarge the suite of classical comparison models to better validate any perceived quantum advantage.
- Extend the model to mixed states to potentially increase expressive power.
- Investigate methods to divide classical and quantum resources in the learning procedure.
- Study the connection between entanglement and QCBM advantage more thoroughly.
- Address barren plateau issues as models scale to larger problem sizes.
- Improve hardware performance using error mitigation techniques.
- Develop more thorough hardware error modeling.
- Use parametric compilation and active qubit reset to improve execution on hardware.
- Investigate different embedding methods for mapping currency variables to hardware connectivity.
- Study the necessary sample sizes for successful training.
- Further investigate larger-scale QCBMs beyond the 28-qubit instance.
- Explore extensions of the methods to more general Boltzmann machine structures beyond RBMs.
- Further investigate the effect of RBM weight training and model structure at larger scales.
## Key ideas
- #idea:quantum-advantage — Simulated quantum circuit Born machines (QCBMs) match or outperform a matched-capacity RBM on FX return synthetic data generation, with stronger gains at higher bit precision.
- #idea:quantum-advantage — Higher Meyer-Wallach entangling capability in trained QCBMs is associated with cases where the quantum model outperforms the RBM, suggesting a possible expressivity mechanism.
- #idea:near-term-feasibility — The paper demonstrates partial training of QCBMs on Rigetti hardware up to 28 qubits, showing nontrivial learning on real financial data despite NISQ limitations.
- #idea:hybrid-approach — The workflow is explicitly hybrid, combining classical data preprocessing, classical optimization and evaluation, and quantum generative circuits for financial synthetic-data generation.
- #idea:quantum-advantage — The claimed advantage is expressive and task-specific rather than a demonstrated computational speedup or fault-tolerant quantum advantage.
## Contradictions
- The paper suggests simulated quantum superiority over a classical RBM baseline, but its largest real-hardware 28-qubit result underperforms the RBM, creating a #contradiction:classical-vs-quantum between simulation-based advantage claims and hardware evidence.
- The paper points to improving QCBM performance with scale/precision in simulation, yet also reports that practical scaling is blocked by NISQ noise, restricted problem sizes, and underperformance on the largest hardware instance, yielding a #contradiction:scalability.
- Claims of quantum advantage are weakened by the constrained classical baseline: the main RBM comparison trains only biases while fixing weights, so the observed advantage may not hold against stronger classical generative models.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
