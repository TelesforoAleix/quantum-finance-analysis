---
aliases:
- Approximate complex amplitude encoding algorithm and its application to data classification
  problems
- Approximate complex amplitude encoding
authors:
- Naoki Mitsuda
- Tatsuhiro Ichimura
- Kouhei Nakaji
- Yohichi Suzuki
- Tomoki Tanaka
- Rudy Raymond
- Hiroyuki Tezuka
- Tamiya Onodera
- Naoki Yamamoto
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PhysRevA.109.052423
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
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
step1_date: '2026-03-25T16:04:45.742694'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:04:50.227795'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:05:22.038056'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:05:46.693762'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:06:21.543606'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:06:33.556240'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/fraud-detection
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Approximate complex amplitude encoding algorithm and its application to data
  classification problems
topic_tags:
- fraud-detection
year: 2024
zotero_key: ''
---

## Abstract summary
The paper introduces an approximate complex amplitude encoding (ACAE) algorithm that uses variational quantum circuits and a fidelity-based cost function, estimated via classical shadows, to efficiently load complex-valued classical data into quantum states. Building on prior work that handled only real-valued vectors, the authors extend the approach to complex data and then integrate ACAE with the compact Hadamard classifier to construct a quantum kernel-based binary classifier with reduced gate counts. They demonstrate the method numerically on the Iris dataset and on a credit card fraud detection task relevant to financial institutions.
## Methodology
The paper proposes an empirical quantum machine learning methodology centered on approximate complex amplitude encoding (ACAE), an extension of approximate amplitude encoding for loading complex-valued classical vectors into shallow parametrized quantum circuits. The method replaces the original MMD objective with a fidelity-based cost function between a target quantum state and a variationally prepared model state, and uses classical shadows with random Clifford measurements to estimate both fidelity and gradients efficiently. The parametrized circuit uses a hardware-efficient ansatz composed of single-qubit rotations and CNOTs, optimized via gradient descent with the parameter-shift rule; in the demonstrations, Adam is used. The ACAE routine is then integrated with the compact Hadamard classifier (CHC) to perform binary classification by approximately preparing the training and test states required by CHC, avoiding exact state preparation with exponentially many gates. Empirical evaluation is conducted through numerical simulations on two classification tasks: Iris species classification and credit card fraud detection. The study reports fidelity of state preparation and downstream classification outcomes, and also includes a scalability experiment examining how required circuit depth grows with qubit count for different target fidelity thresholds.

**Algorithms used:** ACAE, AAE, CHC, Classical shadow, Adam, Parameter-shift rule, Gradient descent
**Frameworks:** IBM Quantum

**Experimental setup:** Numerical simulation study using parametrized quantum circuits and classical-shadow-based fidelity estimation. The ACAE training circuit consists of a hardware-efficient ansatz followed by random Clifford unitaries and computational-basis measurements. For Iris, a 5-qubit 12-layer PQC was used for training-data encoding and a 2-qubit 2-layer PQC for test-data encoding. For fraud detection, a 5-qubit setup was used with 4 normal and 4 fraudulent training examples encoded into CHC-compatible states. The paper also reports a scalability simulation varying problem size from 64 data points (5 qubits) to 1024 data points (9 qubits) and measuring circuit depth needed to exceed fidelity thresholds of 0.90, 0.95, and 0.99. The work acknowledges use of IBM Quantum services, but the reported demonstrations are numerical rather than clearly executed on a real QPU.

**Dataset:** Two datasets were used: (1) the Iris dataset from Kaggle/UCI, specifically binary classification tasks on Iris setosa vs Iris versicolor and Iris versicolor vs Iris virginica using four flower features; and (2) the Kaggle credit card fraud detection dataset containing European cardholder transactions from September 2013, with 284,807 transactions including 492 fraudulent cases. For the fraud experiment, only a small proof-of-concept subset was used.
## Experiment details
### Input
Iris experiment: 4 features per sample (sepal length, sepal width, petal length, petal width). For setosa vs versicolor, training used IDs 1-4 and 51-54; test used IDs 5-8 and 55-58. For versicolor vs virginica, analogous small subsets were used. Feature dimension N=4 and number of training samples M=8, giving n=2 data qubits and m=2 index qubits. Fraud experiment: Kaggle credit card fraud dataset with 284,807 transactions and 492 frauds from September 2013; proof-of-concept training subset used 4 normal transactions (IDs 1,2,3,4) and 4 fraudulent transactions (IDs 524,624,4921,6109). Test data used the next four normal and four fraudulent IDs excluding training points. Only 4 PCA-derived features (V1-V4) were used out of 28 available transformed features, so N=4 and M=8. Additional simulation used 48 randomly selected instances from the same fraud dataset. Data were normalized to satisfy the amplitude-encoding normalization condition.

### Process
1. Define a target quantum state whose amplitudes encode either complex-valued training/test vectors directly (ACAE) or the CHC state combining class-specific training vectors in real/imaginary amplitudes. 2. Construct a hardware-efficient PQC with layers of parametrized Rx, Ry, Rz gates and CNOTs; for real-valued test encoding, use a reduced ansatz with only Ry and CNOT gates. 3. Append a random Clifford unitary to the PQC output and perform computational-basis measurements to generate classical snapshots. 4. Estimate the fidelity between model and target states using classical shadows and use the parameter-shift rule to estimate gradients. 5. Optimize PQC parameters with Adam. For Iris training-data encoding, use 400 iterations and 1000 classical snapshots per iteration; learning rate schedule: 0.1 for iterations 1-100, 0.01 for 101-200, 0.005 for 201-300, and 0.001 for 301-400. For Iris test-data encoding, use 100 iterations and 1000 snapshots; learning rate 0.1 for first 50 iterations and 0.01 for last 50. 6. After approximate state preparation, apply the CHC Hadamard operation on the ancilla and measure the ancilla Pauli-Z expectation value; classify by the sign of this expectation. 7. Report fidelity and classification correctness. 8. In the scalability study, vary qubit count from 5 to 9 and determine the circuit depth required to achieve fidelity above 0.90, 0.95, or 0.99.

### Output
Outputs include state-preparation fidelity between target and model states, ancilla expectation value <sigma_z> used as the classifier score, and classification correctness for each test instance. For Iris setosa vs versicolor, all 8 test cases were classified correctly; for versicolor vs virginica, 5 of 8 were correct using ACAE-encoded data, while all 8 were correct when exact data encoding was used, indicating encoding error effects. For the fraud detection proof-of-concept, all 8 selected test cases were classified correctly; in an additional random-sample experiment, 42 of 48 test instances were correctly classified. The paper also reports a scalability output in terms of required circuit depth versus qubit count for target fidelity thresholds (0.90, 0.95, 0.99). There is no direct comparison against classical machine learning baselines or other quantum classifiers in matched experiments; the main implicit baseline is exact-data CHC classification and conceptual comparison to original CHC/exact state preparation requiring exponentially many gates.

### Parameters
- iris_training_qubits_total: 5
- iris_training_data_qubits_n: 2
- iris_training_index_qubits_m: 2
- iris_training_pqc_layers: 12
- iris_training_shots_or_snapshots_per_iteration: 1000
- iris_training_iterations: 400
- iris_training_optimizer: Adam
- iris_training_learning_rate_schedule: {'iterations_1_100': 0.1, 'iterations_101_200': 0.01, 'iterations_201_300': 0.005, 'iterations_301_400': 0.001}
- iris_test_encoding_qubits: 2
- iris_test_encoding_layers: 2
- iris_test_encoding_ansatz: Ry and CNOT only
- iris_test_encoding_iterations: 100
- iris_test_encoding_shots_or_snapshots_per_iteration: 1000
- iris_test_learning_rate_schedule: {'iterations_1_50': 0.1, 'iterations_51_100': 0.01}
- fraud_training_qubits_total: 5
- fraud_feature_count_used: 4
- fraud_training_samples: 8
- scalability_qubit_range: 5 to 9 qubits
- scalability_fidelity_thresholds: [0.9, 0.95, 0.99]

### Hardware
{'execution_mode': 'Numerical simulation', 'quantum_service_acknowledged': 'IBM Quantum services', 'measurement_scheme': 'Random Clifford measurements for classical shadows', 'ansatz_type': 'Hardware-efficient ansatz with single-qubit rotations and CNOTs', 'qpu_used_for_results': 'Not clearly specified; demonstrations appear simulated rather than run on a real QPU'}

### Reproducibility
The paper provides substantial methodological detail: datasets are public (Kaggle/UCI), training/test IDs for the main demonstrations are specified, ansatz structures, qubit counts, layer counts, optimizer, iteration counts, and learning-rate schedules are reported. However, no code repository is mentioned in the provided text, and some implementation details for the fraud experiment are less explicit than for Iris. Overall, partial-to-good reproducibility from the paper alone, but full replication would be easier with released code.
## Findings
- [supported] The paper proposes approximate complex amplitude encoding (ACAE), extending prior approximate amplitude encoding to complex-valued vectors by optimizing fidelity rather than MMD and estimating fidelity/gradients with classical shadows.
- [supported] In the Iris setosa vs. Iris versicolor binary classification experiment, the ACAE+compact Hadamard classifier (CHC) achieved 8/8 correct classifications on simulated data.
- [supported] In the harder Iris versicolor vs. Iris virginica experiment, the ACAE+CHC achieved 5/8 correct classifications, while using exact encoded data instead of ACAE yielded 8/8 correct classifications, indicating encoding approximation error contributed to misclassification.
- [supported] For the Iris training-state preparation experiment, the 5-qubit, 12-layer PQC reached fidelity 0.994 after 400 optimization iterations with 1000 classical-shadow snapshots per iteration.
- [supported] For Iris test-data encoding, a 2-qubit, 2-layer PQC achieved fidelity greater than 0.999 for each test datum after 100 iterations with 1000 snapshots.
- [supported] In the credit-card fraud detection proof-of-concept using 4 normal and 4 fraudulent training examples with 4 features, the ACAE+CHC correctly classified 8/8 selected test transactions.
- [supported] In an additional credit-card fraud simulation with 48 randomly selected test instances, 42/48 were correctly classified, corresponding to 87.5% accuracy.
- [supported] A scalability experiment on the fraud dataset showed that the circuit depth required to reach target fidelities above 0.90, 0.95, or 0.99 increases superlinearly with qubit count from 5 to 9 qubits.
- [supported] The authors report that for a 5-qubit case, reducing fidelity from above 0.99 to about 0.7 still preserved classification accuracy above 80% in their simulation.
- [speculative] ACAE may enable practical shallow-circuit implementations of CHC with fewer gates than exact amplitude encoding, but the paper does not demonstrate end-to-end hardware advantage over classical baselines.
- [speculative] The paper argues ACAE avoids the exponential gate cost of exact state preparation by using PQCs with O(poly(n)) depth, but training still involves exponential classical computation in data dimension for general inputs.
- [speculative] The authors note ACAE may face scalability limits due to barren plateaus and the cost of random Clifford measurements, especially for large financial datasets requiring around 23 qubits.

**Results summary:** This peer-reviewed empirical paper introduces ACAE, a variational method for approximately loading complex-valued classical vectors into quantum amplitudes using fidelity-based training with classical-shadow estimation. Results are numerical simulations rather than real-hardware demonstrations. In a 5-qubit Iris classification setup, the method achieved fidelity 0.994 for training-state preparation and greater than 0.999 for test-state encoding; the resulting ACAE+CHC classifier obtained 8/8 correct predictions for Iris setosa vs. Iris versicolor, but only 5/8 for Iris versicolor vs. Iris virginica, whereas exact encoding gave 8/8 on the latter task, suggesting approximation error affected performance. In a proof-of-concept financial application to credit-card fraud detection using a very small subset of the Kaggle dataset, the method classified 8/8 selected test cases correctly and 42/48 randomly selected test cases correctly in an additional simulation. A separate scalability study found superlinear growth in required circuit depth as qubit count increased from 5 to 9 for target fidelities above 0.90, 0.95, and 0.99, indicating limited scalability despite shallow-circuit benefits relative to exact amplitude encoding.

**Performance claims:**
- Iris training-state preparation: fidelity reached 0.994 using a 5-qubit, 12-layer PQC after 400 iterations with 1000 classical-shadow snapshots per iteration
- Iris test-state encoding: fidelity > 0.999 for each test datum using a 2-qubit, 2-layer PQC after 100 iterations with 1000 snapshots
- Iris setosa vs. Iris versicolor classification: 8/8 correct
- Iris versicolor vs. Iris virginica classification with ACAE: 5/8 correct
- Iris versicolor vs. Iris virginica classification with exact encoding: 8/8 correct
- Credit-card fraud proof-of-concept classification on selected test cases: 8/8 correct
- Additional credit-card fraud simulation on random test instances: 42/48 correct (87.5% accuracy)
- For a 5-qubit case, fidelity reduced from >0.99 to about 0.7 still yielded classification accuracy above 80%
- Scalability study: required PQC depth to achieve fidelity >0.90, >0.95, or >0.99 increased superlinearly as problem size grew from 64 data points (5 qubits) to 1024 data points (9 qubits)
## Quantum advantage claim
**Classification:** speculative

The paper argues that ACAE can replace exact exponential-gate state preparation with shallow PQCs of polynomial depth, but all reported results are simulation-based proof-of-concept studies on small instances, with no empirical speedup or advantage over classical methods demonstrated on real hardware.
## Limitations
- The original AAE method cannot load complex-valued data vectors, which restricts its applicability and motivates ACAE.
- The training process for ACAE still requires classical computation that scales exponentially with the data dimension because evaluating the fidelity estimate involves O(N) = O(2^n) terms.
- Random Clifford measurements used for classical-shadow-based fidelity estimation are practically costly, requiring O(n^2 / log^2(n)) entangling gates to sample n-qubit Clifford unitaries.
- Scalability is a major concern: numerical experiments indicate that the circuit depth required to reach target fidelities grows superlinearly with the number of qubits.
- The authors state that ACAE may not be applicable to large-size problems because required circuit depth increases substantially as problem size grows.
- For realistic financial datasets, the qubit requirement becomes large; the paper notes that handling the full credit card fraud dataset with 28 features and about 280,000 samples would require 23 qubits.
- Using fidelity as a global cost function can induce gradient vanishing / barren plateau behavior, making optimization difficult as the number of qubits increases.
- The demonstrations are numerical proof-of-principle studies rather than executions on noisy quantum hardware, so hardware noise, decoherence, and calibration effects are not empirically validated. [inferred]
- Experiments are limited to very small problem instances: Iris uses 8 training samples and 8 test samples, and the main fraud-detection demonstration uses only 8 training samples and 8 test samples from a much larger dataset.
- The fraud-detection study uses only 4 of the 28 available PCA-transformed features, limiting representativeness of the real task.
- Classification performance is sensitive to encoding fidelity; the paper notes that ACAE approximation error affected misclassifications in the Iris versicolor vs. virginica task.
- The CHC implementation uses fixed uniform weights rather than optimized classifier weights, which may limit achievable accuracy.
- The paper does not benchmark against strong classical baselines for fraud detection or Iris classification, so practical advantage over conventional methods is unclear. [inferred]
- No end-to-end resource estimate is provided for production-scale deployment in financial services, including latency, retraining cost, and throughput constraints. [inferred]
- Reproducibility is limited by incomplete reporting of some experimental details such as random seeds, exact ansatz initialization choices per run, and full implementation artifacts/code availability. [inferred]
## Open questions
- How well does ACAE scale to larger datasets and higher-dimensional feature spaces relevant to real financial applications?
- What circuit depth is required to maintain useful fidelity as the number of qubits grows beyond the small instances studied here?
- To what extent can acceptable classification accuracy be maintained when fidelity is substantially below 1 for larger problems?
- How severe is the barren plateau problem for ACAE in practically relevant system sizes, and which mitigation strategies are most effective?
- Can random-Clifford-based fidelity estimation be replaced or improved with more hardware-friendly measurement schemes without sacrificing performance?
- How does ACAE perform on real noisy quantum hardware compared with noiseless simulation?
- What is the trade-off between encoding approximation error and downstream classifier accuracy across different datasets?
- Would optimizing the classifier weights {b'_j} materially improve classification performance relative to the uniform weighting used here?
- How does ACAE-CHC compare with state-of-the-art classical fraud detection models on realistic, imbalanced financial datasets? [inferred]
- Can the method handle the full 28-feature, hundreds-of-thousands-of-transactions fraud dataset within realistic quantum resource limits? [inferred]

**Future work:**
- Investigate optimization of the classifier weights {b'_j}, analogous to support vector machine weight optimization, to improve classification performance.
- Develop algorithmic improvements that address scalability issues in ACAE for larger datasets and larger qubit counts.
- Explore localized fidelity measurements as proposed in prior work to mitigate gradient vanishing and barren plateau problems.
- Study the use of circuit initialization strategies to alleviate optimization difficulties in large systems.
- Investigate specially structured ansatz designs to improve trainability and scalability.
- Examine parameter embedding methods as another approach to address gradient vanishing.
- Improve the implementation of fidelity estimation by leveraging more efficient Clifford circuit constructions and depth optimizations.
- Extend ACAE and CHC toward practical large-scale applications such as full-scale fraud detection with much larger datasets. [implied]
- Validate the method on real quantum hardware and assess robustness to noise and device constraints. [implied]
- Benchmark against stronger classical and quantum baselines on realistic financial tasks. [implied]
## Key ideas
- #idea:hybrid-approach — Proposes Approximate Complex Amplitude Encoding (ACAE), a variational state-preparation method using classical-shadow-based fidelity estimation to load complex classical data into shallow PQCs.
- #idea:hybrid-approach — Integrates ACAE with the compact Hadamard classifier to build a quantum kernel-style binary classifier and demonstrates it on credit card fraud detection.
- #idea:near-term-feasibility — Targets NISQ settings via hardware-efficient ansatz circuits and approximate state preparation rather than exact exponential-gate amplitude encoding.
- #idea:near-term-feasibility — Small simulated fraud experiments suggest useful classification can persist even when encoding fidelity is imperfect.
- #idea:quantum-advantage — Claims potential benefit from replacing exact state preparation with polynomial-depth variational circuits, though only at the level of quantum gate complexity and small simulated instances.
## Contradictions
- The paper suggests a route to quantum advantage through polynomial-depth approximate encoding, but its own limitations state that fidelity evaluation/training still incurs exponential classical cost in data dimension, contradicting any strong end-to-end quantum superiority claim.
- The paper frames ACAE+CHC as promising for fraud detection, yet evidence is limited to tiny simulated subsets with no matched classical baseline, contradicting any implied claim of practical superiority over classical fraud-detection methods.
- The scalability study reports superlinear growth in required circuit depth with qubit count, which conflicts with the paper's practical positioning for larger financial datasets and supports contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
