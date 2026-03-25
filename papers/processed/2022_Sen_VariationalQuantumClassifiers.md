---
aliases:
- Variational quantum classifiers through the lens of the Hessian
- Variational quantum classifiers through
authors:
- Pinaki Sen
- Amandeep Singh Bhatia
- Kamalpreet Singh Bhangu
- Ahmed Elbeltagi
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1371/journal.pone.0262346
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: PLOS ONE
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:58:04.347122'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:08.325251'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:58:57.420044'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:59:17.090168'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:59:45.101149'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:59:56.133046'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Variational quantum classifiers through the lens of the Hessian
topic_tags: []
year: 2022
zotero_key: ''
---

## Abstract summary
The paper studies the training behavior of variational quantum classifiers by analyzing the Hessian of their loss functions. The authors compute and visualize Hessian eigenvalues and loss landscapes for a 4-bit parity problem and a diabetes classification task, using quantum simulators and gradient-based optimization. They also propose an adaptive Hessian-based learning rate scheme and show that it can help avoid local minima and speed up convergence in variational quantum circuit training.
## Methodology
This peer-reviewed empirical study investigates the trainability of variational quantum classifiers (VQCs) by analyzing the Hessian of the loss landscape during training. The authors derive Hessian matrix elements for parameterized quantum circuits using the parameter-shift rule applied twice, and use Hessian eigenvalues to characterize curvature, local minima, saddle points, and flat directions. Empirically, they implement VQCs in PennyLane with PyTorch support and study two classification settings: a synthetic 4-bit parity problem as a warm-up example and the diabetes classification task using the Pima Indians Diabetes dataset. For the parity task, a 4-qubit circuit with an Rx-based feature map and three variational layers of parameterized single-qubit rotations plus CNOT entanglers is trained with gradient descent, while Hessian eigenvalues are tracked across iterations and 2D/3D loss landscapes are visualized for selected parameter pairs. For the diabetes task, an 8-qubit VQC is built with a feature map using Hadamard, Ry, and controlled-Z gates, followed by parameterized single-qubit rotations; the feature map and variational block are repeated twice. Inputs are normalized to [-pi, pi], training proceeds with gradient descent, and Hessian eigenvalue distributions are recorded at each iteration to study convergence behavior. The paper also proposes and evaluates an adaptive Hessian learning rate (A-HLR) strategy that switches among discrete learning rates based on loss-change thresholds and uses the count of negative Hessian eigenvalues to distinguish local from global minima, comparing its convergence behavior against standard gradient descent with fixed learning rates.

**Algorithms used:** Variational Quantum Classifier, Gradient Descent, Parameter-shift rule
**Frameworks:** PennyLane, PyTorch, Plotly, Python

**Experimental setup:** All experiments were quantum simulations implemented in Python on the PennyLane platform for differentiable quantum programming, with PyTorch used to accelerate simulation and algebraic manipulation. No real quantum processing unit was used; the paper explicitly states Hessians were computed on a quantum simulator. Plotly was used for 2D and 3D visualization of loss landscapes and Hessian eigenvalue evolution.

**Dataset:** Two datasets/tasks were used: (1) a synthetic 4-bit parity/XOR classification problem with 4-bit binary strings as inputs and binary labels based on odd parity; and (2) the Pima Indians Diabetes dataset from the UCI Machine Learning Repository/Kaggle, containing 8 input features (age, glucose, insulin, pregnancies, BMI, skin thickness, diabetes pedigree function, blood pressure) and one binary output indicating diabetes status.
## Findings
- [supported] The study computes Hessians of variational quantum classifiers (VQCs) using the parameter-shift rule and uses Hessian eigenvalues to characterize local curvature of the loss landscape during training.
- [supported] For the 4-bit parity problem, the loss landscape around selected parameters showed local convexity, and gradient descent recovered a minimum within 100 iterations in simulator-based experiments.
- [supported] In the parity experiment, the Hessian eigenvalue spectrum evolved from a mix of negative and non-negative values near zero at early iterations to mostly non-negative values with a single negative eigenvalue by iteration 100, which the authors interpret as indicating convergence to a stable minimum.
- [supported] For the diabetes classification example, an 8-qubit VQC with repeated feature-map and variational layers was trained in simulation, and the authors report convergence of the loss within 30 iterations.
- [supported] In the diabetes experiment, early training iterations showed Hessian spectra with roughly balanced positive and negative eigenvalues and many near-zero eigenvalues; by iteration 30, only one negative eigenvalue remained and the rest were non-negative.
- [supported] The authors report that many zero Hessian eigenvalues correspond to flat directions in parameter space where parameter changes do not significantly alter the loss landscape.
- [supported] An adaptive Hessian learning rate (A-HLR) schedule converged faster than fixed-learning-rate gradient descent in the 4-bit parity simulation, with the paper stating convergence within 25 iterations for A-HLR.
- [supported] The paper claims A-HLR can overshoot local minima and improve convergence behavior relative to constant learning rates in the presented simulator experiments.
- [speculative] The authors suggest that studying Hessian-based local curvature may help identify when quantum speedup is achievable, but no speedup is empirically demonstrated.
- [speculative] The paper states that VQAs are considered a major route toward quantum advantage, but this work does not provide empirical evidence of quantum advantage.

**Results summary:** This peer-reviewed empirical paper studies variational quantum classifiers through Hessian-based analysis of the loss landscape, using simulator-based experiments implemented in PennyLane/PyTorch rather than reported real quantum hardware runs. On a 4-bit parity task, the authors visualize 2D slices of the loss surface and track Hessian eigenvalues over 100 training iterations, observing a transition from mixed-sign spectra with many near-zero values to predominantly non-negative eigenvalues near convergence. On an 8-qubit diabetes classification setup, they similarly visualize local loss landscapes and report convergence within 30 iterations, with Hessian spectra evolving from mixed positive/negative values to mostly non-negative values with many zeros, interpreted as flat directions. They also compare fixed-learning-rate gradient descent with an adaptive Hessian learning rate method and report faster convergence for the adaptive method, including convergence within 25 iterations on the parity task. The paper focuses on optimization behavior and trainability rather than classification accuracy or financial applications, and it does not demonstrate quantum advantage.

**Performance claims:**
- 4-bit parity VQC used 36 parameterized gates and 12 non-parameterized gates
- Parity-task optimization trajectory analyzed over 100 iterations
- For the parity problem, Hessian spectra at early iterations (0-7) contained mixed negative and non-negative eigenvalues near zero; by iteration 100, a single negative eigenvalue remained and the rest were non-negative
- Diabetes experiment used an 8-qubit VQC with feature map and variational circuit repeated 2 times
- Diabetes-task optimization reported convergence by iteration 30
- For the diabetes task, early Hessian spectra at iterations 0, 2, and 4 showed both positive and negative eigenvalues with many zeros; by iteration 30, one negative eigenvalue remained and the rest were non-negative
- Adaptive Hessian learning rate (A-HLR) reportedly converged within 25 iterations on the parity dataset
- A-HLR was compared against fixed-learning-rate gradient descent over both 25-iteration and 100-iteration runs
## Quantum advantage claim
**Classification:** speculative

The paper discusses VQAs as promising for quantum advantage and suggests Hessian analysis may help understand when speedup is achievable, but all reported results are simulator-based optimization studies with no empirical quantum advantage over classical methods demonstrated.
## Limitations
- All experiments were performed on a quantum simulator (PennyLane/PyTorch) rather than on physical quantum hardware, so hardware noise, decoherence, and calibration effects were not empirically validated.
- The study uses only small-scale examples: a 4-bit parity problem and an 8-qubit variational quantum circuit for the diabetes dataset.
- Visualization of the loss landscape is limited to two parameters at a time; the authors state that for more than two parameters they cannot obtain the full loss range in 3D plots.
- The variational circuits were constructed with a fixed number of qubits and fixed depth, limiting conclusions about broader architecture choices.
- The diabetes experiment is based on a single classical dataset, restricting external validity across tasks and domains.
- The paper notes that at the beginning of training, gradient descent struggles due to small gradients, indicating optimization instability even for small circuits.
- The adaptive Hessian learning rate method depends on manually chosen hyperparameters such as the threshold for consecutive loss differences and the threshold on the count of negative Hessian eigenvalues.
- The criterion for distinguishing local from global minima via the number of negative Hessian eigenvalues is acknowledged as imperfect in practice ('Practically it should be zero, but in reality its not always possible to reach that point').
- [inferred] No quantitative comparison is provided against strong classical machine learning baselines on the diabetes task, so any practical advantage over classical methods is unclear.
- [inferred] No evaluation metrics such as test accuracy, precision/recall, or cross-validation results are reported in the provided text, limiting assessment of classifier generalization and reproducibility.
- [inferred] The claim that the circuit is simple enough to run on real quantum systems is not backed by real-device experiments, so scalability to production NISQ settings remains unproven.
- [inferred] The use of Hessian computation via repeated parameter-shift evaluations may become costly as parameter count grows, raising scalability concerns for larger financial or industrial problems.
- [inferred] Reproducibility is only partial: software tools are named and data availability is mentioned, but the text does not specify seeds, train/test splits, hardware configuration, or full experimental settings.
## Open questions
- How well do Hessian-based insights transfer from noiseless simulation to real NISQ hardware with noise and decoherence?
- Does the observed Hessian eigenvalue behavior persist for larger qubit counts, deeper ansatzes, and more realistic datasets?
- Can adaptive Hessian learning rate reliably avoid barren plateaus or poor local minima in larger variational quantum circuits?
- How sensitive is the adaptive Hessian learning rate method to the choice of thresholds and discrete learning-rate schedules?
- To what extent do Hessian-based diagnostics improve classification performance versus only improving optimization behavior?
- Can the proposed approach generalize beyond parity and diabetes classification to other application domains such as finance or combinatorial optimization?
- What is the computational overhead of Hessian estimation as the number of trainable parameters increases?
- How should one robustly distinguish local minima from global minima in practice when Hessian eigenvalues are noisy or near zero?

**Future work:**
- Extend Hessian-based analysis to solving broader classical and quantum optimization problems.
- Use the framework to support future variational quantum algorithm and circuit-design analysis.
- Investigate the integration of gradient-based methods with NISQ devices, which the authors describe as a young area with more to offer.
- [inferred] Validate the Hessian-based training and visualization approach on real quantum hardware rather than only simulators.
- [inferred] Test the method on larger datasets, more qubits, and deeper circuits to assess scalability.
- [inferred] Benchmark against state-of-the-art classical optimizers and classifiers to determine whether Hessian-based VQC training offers practical benefit.
- [inferred] Develop more scalable or approximate Hessian estimation and visualization methods for high-dimensional parameter spaces.
- [inferred] Apply the approach to domain-specific use cases, including financial optimization and classification tasks, to evaluate practical relevance.
## Key ideas
- #idea:near-term-feasibility — Uses variational quantum classifiers as a NISQ-era approach and studies their trainability via Hessian eigenvalue analysis.
- #idea:hybrid-approach — Implements a hybrid quantum-classical workflow in PennyLane/PyTorch where classical gradient descent and Hessian-based learning-rate adaptation optimize simulated quantum circuits.
- #idea:quantum-advantage — Discusses VQAs as a possible route to quantum advantage, but only speculatively and without empirical demonstration.
- #idea:hybrid-approach — Proposes an adaptive Hessian learning rate scheme that reportedly accelerates convergence relative to fixed learning rates in small simulator experiments.
## Contradictions
- The paper gestures toward quantum advantage for VQAs, but all evidence is from small-scale simulator-based training studies with no comparison against strong classical ML baselines, contradicting any practical claim of quantum superiority.
- The paper presents VQCs as promising for near-term use, yet its own limitations note only 4- and 8-qubit simulated experiments, costly Hessian estimation, and no hardware validation, which contradicts implied scalability to realistic applications.
- The paper suggests relevance to broader domains such as finance, but the actual experiments are generic parity and diabetes classification tasks rather than financial datasets or use cases, weakening domain-specific claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic task: 4-bit binary input strings encoded into 4 qubits, with labels defined by parity (output 1 for odd number of ones, else 0). Diabetes task: Pima Indians Diabetes dataset from the UCI Machine Learning Repository (also referenced via Kaggle), with 8 classical input features and 1 binary target; inputs were normalized to lie in [-pi, pi] before quantum encoding. The paper names the features but does not clearly report sample count, train/test split, or preprocessing beyond normalization.

### Process
1. Derive gradients and Hessian entries of the VQC loss using the parameter-shift rule; Hessian computed by applying the shift rule twice. 2. For the 4-bit parity task, encode 4-bit strings with an Rx-based feature map, then apply a 4-qubit variational circuit with three layers; each layer contains rotational gates with three trainable parameters on each qubit followed by CNOT entanglers. Measure the third qubit in the Pauli-Z basis and classify using a threshold on the expectation value. Train with gradient descent for 100 iterations from random initialization, while computing the full Hessian over trainable parameters after each iteration and recording eigenvalues. Visualize local loss landscapes for selected parameter pairs (e.g., theta_3 and theta_7) while fixing remaining parameters at optimal values. 3. For the diabetes task, encode 8 normalized features into an 8-qubit circuit using a feature map with Hadamard, Ry, and CZ gates, followed by a variational block of single-qubit rotations R(phi1, phi2, phi3); the feature map and variational circuit are repeated twice. In each iteration, for each sample, run feature map -> variational circuit -> measurement, compute prediction, calculate loss against the label, average over samples, and update parameters with gradient descent. Compute the Hessian matrix at each iteration for visualization only, and analyze eigenvalue evolution over 30 iterations. 4. Evaluate an adaptive Hessian learning rate (A-HLR) method using a discrete set of learning rates: start from the largest LR, reduce LR when consecutive loss differences fall below a threshold, and when the smallest LR is reached, use the count of negative Hessian eigenvalues versus a threshold to decide whether the solution is near a global minimum or stuck in a local minimum; if stuck, restart with a higher LR to overshoot local minima. Compare convergence curves of A-HLR against fixed-LR gradient descent over 25 and 100 iterations.

### Output
Outputs are primarily qualitative and optimization-oriented rather than standard predictive ML metrics. Reported results include 2D/3D loss landscape visualizations for selected parameter pairs, contour plots showing optimization trajectories, distributions/evolution of Hessian eigenvalues across training iterations, and training cost convergence curves. For A-HLR, the main comparison baseline is gradient descent with constant learning rates (including LR = 0.5 and other fixed values), with faster convergence claimed for A-HLR. The paper discusses classifier behavior on parity and diabetes tasks but does not clearly report standard classification metrics such as accuracy, precision, recall, F1, or AUC.

### Parameters
- parity_task: {'qubits': 4, 'variational_layers': 3, 'trainable_parameters': 36, 'non_parameterized_gates': 12, 'measurement': 'Pauli-Z on third qubit with thresholding', 'optimizer': 'Gradient Descent', 'iterations': 100, 'initialization': 'random'}
- diabetes_task: {'qubits': 8, 'feature_map_components': ['Hadamard', 'Ry', 'CZ'], 'variational_block': 'single-qubit rotations R(phi1, phi2, phi3) on each qubit', 'repetitions_of_feature_map_and_variational_circuit': 2, 'optimizer': 'Gradient Descent', 'iterations': 30, 'input_normalization_range': '[-pi, pi]'}
- loss_function: squared error / mean squared loss
- adaptive_hessian_learning_rate: {'learning_rate_scheme': 'discrete set of decreasing learning rates', 'switch_condition': 'difference between consecutive costs below threshold', 'hessian_based_decision': 'count of negative eigenvalues compared to threshold hyperparameter'}

### Hardware
{'hardware_type': 'simulator', 'platform': 'PennyLane quantum simulation environment', 'qpu_used': False, 'cloud_provider': None, 'simulator_name': 'not explicitly specified', 'noise_model': 'not reported', 'transpilation_settings': 'not reported'}

### Reproducibility
The paper provides substantial methodological detail on circuit structure, datasets, software stack, and optimization logic, and it is open access. It states that data will be available on publication; the diabetes dataset is public. However, no code repository link is given in the provided text, and several implementation details needed for exact replication are missing or underspecified, including train/test split, exact sample usage, batch handling, full learning-rate schedule values, tolerance thresholds, and simulator backend configuration. Partial reproducibility is possible, but exact replication would require additional details.
