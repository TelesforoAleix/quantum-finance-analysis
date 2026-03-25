---
aliases:
- 'IQNN-CS: Interpretable Quantum Neural Network for Credit Scoring'
- IQNN CS Interpretable Quantum
authors:
- Abdul Samad Khan
- Nouhaila Innan
- Aeysha Khalique
- Muhammad Shafique
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:13:22.161240'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:13:27.239261'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:57.627254'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:14:28.688367'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:15:00.182222'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:15:09.633323'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/credit-scoring
- topic/regulatory-compliance
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'IQNN-CS: Interpretable Quantum Neural Network for Credit Scoring'
topic_tags:
- credit-scoring
- regulatory-compliance
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes IQNN-CS, a hybrid classical–quantum neural network architecture tailored for multiclass credit scoring under regulatory demands for transparency. It combines a variational quantum neural network with several post-hoc interpretability techniques adapted to structured financial data and introduces a new metric, Inter-Class Attribution Alignment (ICAA), to quantify how distinctly the model attributes features across classes. The framework is evaluated on two real-world credit datasets, focusing on predictive performance, training stability, and the quality of explanations to assess suitability for high-stakes financial decision-making.
## Methodology
This preprint presents an empirical study of IQNN-CS, a hybrid classical-quantum interpretable quantum neural network for multiclass credit scoring. The methodology follows a five-stage pipeline: data preparation, hybrid model construction, training, post-hoc interpretability analysis, and evaluation. Two real-world benchmark credit scoring datasets are preprocessed using class balancing (undersampling for one dataset and SMOTE for the other), feature standardization, PCA-based dimensionality reduction to match qubit constraints, and stratified train/validation/test splitting. The model consists of a classical preprocessing network, a variational quantum neural network using angle encoding and a multi-layer entangling circuit, and a classical postprocessing head for multiclass logits. The quantum layer measures Pauli-Z expectation values and is integrated with PyTorch through PennyLane TorchLayer for end-to-end differentiable training. Training uses AdamW, learning-rate scheduling, class-weighted loss, and early stopping. Beyond predictive evaluation, the paper emphasizes interpretability through gradient-based attribution methods, occlusion sensitivity, prototype/example matching in quantum feature space, latent-space visualization with t-SNE/PCA, and a newly proposed Inter-Class Attribution Alignment (ICAA) metric that measures attribution similarity across classes. Experiments are run in simulation and results are reported using classification metrics and interpretability diagnostics across the two datasets.

**Algorithms used:** Variational Quantum Neural Network, AngleEmbedding, StronglyEntanglingLayers, PCA, SMOTE, Integrated Gradients, SmoothGrad, Gradient×Input, Saliency Maps, t-SNE, ICAA
**Frameworks:** PennyLane, PyTorch, TorchLayer

**Experimental setup:** Experiments were implemented in PyTorch and PennyLane, with quantum circuits simulated using PennyLane's default.qubit backend. Training was executed on a CPU-only environment (Apple M3, 16 GB RAM) without GPU acceleration. The hybrid model used 6 qubits and 4 StronglyEntanglingLayers, combined with classical dense layers and dropout. Each dataset was split into 70% training, 15% validation, and 15% test sets using stratified sampling.

**Dataset:** Two benchmark real-world credit scoring datasets referred to as Dataset 1 and Dataset 2, both sourced from Kaggle credit score classification datasets. They contain numerical and categorical financial attributes and are used for multiclass credit risk classification (Low, Average, High).
## Experiment details
### Input
Input data consisted of two Kaggle credit score classification datasets: Dataset 1 (https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset) and Dataset 2 (https://www.kaggle.com/datasets/parisrohan/credit-score-classification). The paper states that both datasets include numerical and categorical financial attributes for multiclass credit scoring. Preprocessing included class balancing (undersampling for Dataset 1; SMOTE for Dataset 2, though Appendix Table 2 also lists SMOTE generally), feature standardization via StandardScaler, one-hot encoding for categorical variables per Appendix settings, and PCA reduction to 6 components to match the 6-qubit model. Data were split stratified into 70% train, 15% validation, and 15% test. Exact sample counts and time periods are not reported.

### Process
The experimental pipeline proceeds as follows: (1) preprocess raw credit datasets using class balancing, standardization, encoding, and PCA; (2) split data into train/validation/test using stratified sampling; (3) pass PCA-compressed features through a classical preprocessing network with linear layers and ReLU; (4) encode the resulting latent vector into a 6-qubit quantum circuit using angle encoding; (5) apply a 4-layer variational circuit based on StronglyEntanglingLayers; (6) measure Pauli-Z expectation values from each qubit to obtain quantum features; (7) feed these features into a classical postprocessing head with dropout and linear layers to produce class logits; (8) train end-to-end for up to 50 epochs using AdamW with learning rate 0.01, class-weighted cross-entropy/NLL-style loss, and a learning-rate scheduler (the main text mentions cosine annealing, while Appendix Table 2 specifies StepLR); (9) compute quantum gradients using the parameter-shift rule with shift s = pi/2; (10) monitor validation loss and apply early stopping, retaining the best checkpoint; (11) evaluate on test data using accuracy, macro F1, confusion matrices, and class-wise precision/recall/F1; (12) perform interpretability analysis using saliency, gradient×input, integrated gradients, SmoothGrad, occlusion sensitivity, cosine-similarity-based prototype matching in quantum activation space, t-SNE/PCA latent visualization, and the proposed ICAA metric; (13) additionally assess attribution stability under 20 Gaussian perturbations for selected samples.

### Output
Outputs include classification accuracy, macro F1-score, class-wise precision/recall/F1, confusion matrices, training/validation/test accuracy and loss curves, saliency/attribution maps, occlusion-based confidence degradation curves, t-SNE visualizations of quantum embeddings, cosine-similarity-based influential training examples, ICAA attribution similarity matrices, softmax entropy distributions, and attribution stability statistics under perturbation. Reported predictive results include 100% accuracy/F1 on Dataset 1 and 77.3% accuracy on Dataset 2. No explicit classical baseline comparison is presented; evaluation is primarily across the two datasets and across interpretability methods.

### Parameters
- qubits: 6
- quantum_layers: 4
- variational_ansatz: StronglyEntanglingLayers
- embedding_strategy: AngleEmbedding
- pca_components: 6
- batch_size: 16
- epochs: 50
- optimizer: AdamW
- learning_rate: 0.01
- scheduler: StepLR (Appendix Table 2); main text also mentions cosine annealing
- loss_function: Class-weighted CrossEntropy / NLL-style loss
- train_validation_test_split: 70/15/15
- random_seed: 42
- gradient_method: parameter-shift
- parameter_shift_s: pi/2
- dropout: used in classical postprocessing head
- perturbation_runs_for_stability: 20

### Hardware
{'hardware_type': 'simulator', 'simulator_name': 'PennyLane default.qubit', 'compute_hardware': 'Apple M3 CPU, 16 GB RAM', 'gpu_used': False, 'cloud_provider': None, 'qpu_model': None, 'transpilation_settings': None}

### Reproducibility
Preprint empirical study. The paper provides substantial methodological detail, including pipeline steps, model structure, optimizer, learning rate, qubit count, layer count, split ratios, random seed, and public dataset links. However, no code repository is mentioned in the provided text, some implementation details are inconsistent (e.g., scheduler type; NLL vs CrossEntropy wording; balancing method description), and exact dataset sample sizes are omitted. Public data availability is good, but reproducibility is moderate rather than complete.
## Findings
- [supported] IQNN-CS is a hybrid classical-quantum multiclass credit scoring framework that combines a variational QNN with post-hoc interpretability methods and a new Inter-Class Attribution Alignment (ICAA) metric.
- [supported] All experiments were conducted on a quantum circuit simulator (PennyLane default.qubit) on CPU, not on real quantum hardware.
- [supported] On Dataset 1, the model achieved 100% accuracy and 1.00 F1-score for all three classes (Low, Average, High).
- [supported] On Dataset 2, the model achieved 77.3% accuracy, with class-wise precision/recall/F1 of 0.64/0.97/0.77 for Low, 0.73/0.84/0.78 for Average, and 0.95/0.67/0.79 for High.
- [supported] Training on Dataset 1 converged rapidly and stably, with accuracy stabilizing above 98% across train/validation/test splits and loss dropping sharply with minimal train-validation gap.
- [supported] Training on Dataset 2 was unstable, with validation and test accuracy remaining below 80% and a persistent train-validation gap indicating weaker generalization and possible overfitting.
- [supported] t-SNE visualizations of quantum embeddings showed clear class separation for Dataset 1 but overlapping clusters, especially between Average and High classes, for Dataset 2.
- [supported] Saliency-based attribution maps were concentrated and more interpretable for Dataset 1, while Dataset 2 produced diffuse and noisy attributions that varied across runs.
- [supported] Occlusion analysis showed sharp confidence drops on Dataset 1 when top-ranked features were removed, suggesting reliance on a few informative features; Dataset 2 showed more gradual and less structured degradation.
- [supported] ICAA indicated lower inter-class attribution similarity for Dataset 1 and greater overlap in attribution logic for Dataset 2, suggesting less disentangled class reasoning on the harder dataset.
- [supported] Attribution stability analysis under 20 Gaussian perturbations identified one indecisive case in Dataset 2 (sample 12, saliency std 0.2797 versus 0.1426 on Dataset 1), indicating unreliable class evidence for that sample.
- [supported] Example-based attribution using cosine similarity showed coherent same-class nearest training examples for Dataset 1, whereas Dataset 2 often matched highly similar examples from different classes, indicating ambiguous internal representations.
- [speculative] The authors argue that interpretability-first QNN frameworks such as IQNN-CS could support transparent and accountable deployment of quantum machine learning in regulated financial settings.
- [speculative] The paper suggests that ICAA can serve as a useful diagnostic for detecting breakdowns in a model's internal class-specific reasoning beyond standard predictive metrics.
- [speculative] The authors claim QNN performance depends strongly on alignment between dataset structure and the model's quantum encoding and inductive bias.

**Results summary:** This preprint presents IQNN-CS, an interpretable hybrid quantum-classical neural network for multiclass credit scoring, evaluated on two real-world datasets using simulated quantum circuits rather than real hardware. Empirically, the model performed extremely well on Dataset 1, reaching 100% accuracy and perfect class-wise F1-scores, with stable convergence, clear latent-space separation, concentrated feature attributions, sharp occlusion sensitivity, and low inter-class attribution overlap under the proposed ICAA metric. On Dataset 2, performance was substantially weaker at 77.3% accuracy, with unstable training, overlapping quantum embeddings, noisier and less consistent attributions, weaker occlusion signals, and higher attribution overlap across classes. The paper's main empirical contribution is not a quantum speedup or superiority claim, but the introduction and demonstration of interpretability tools, especially ICAA, for diagnosing class-specific reasoning in QNN-based credit scoring.

**Performance claims:**
- 100% accuracy on Dataset 1
- 1.00 precision / 1.00 recall / 1.00 F1 for Low class on Dataset 1
- 1.00 precision / 1.00 recall / 1.00 F1 for Average class on Dataset 1
- 1.00 precision / 1.00 recall / 1.00 F1 for High class on Dataset 1
- 77.3% accuracy on Dataset 2
- Dataset 2 Low class: precision 0.64, recall 0.97, F1 0.77
- Dataset 2 Average class: precision 0.73, recall 0.84, F1 0.78
- Dataset 2 High class: precision 0.95, recall 0.67, F1 0.79
- Training/validation/test split of 70% / 15% / 15%
- 6 qubits and 4 StronglyEntanglingLayers used in the simulated QNN
- 50 training epochs with AdamW at learning rate 0.01
- Sample 12 saliency-map standard deviation under 20 Gaussian perturbations: 0.2797 on Dataset 2 versus 0.1426 on Dataset 1
- Example-based attribution cosine similarities for Dataset 1 test sample 7 reached 0.9989, 0.9976, 0.9976, 0.9930, and 0.9416 for same-class training examples
- Example-based attribution cosine similarities for Dataset 2 test sample 7 reached 1.0000 for several different-class training examples
## Quantum advantage claim
**Classification:** not-applicable

The authors explicitly state that the goal is not to demonstrate quantum supremacy or outperform classical machine learning models. Results are from simulator-based experiments focused on interpretability and classification behavior, so no quantum advantage is demonstrated; any broader deployment relevance remains speculative.
## Limitations
- This is a preprint and has not undergone peer review, so claims and methodology have not yet been independently validated
- Experiments were conducted only on two benchmark credit-scoring datasets, limiting external validity across other financial institutions, geographies, and credit products
- The model was evaluated on only two datasets and performance varied sharply between them, indicating sensitivity to dataset structure and limited robustness
- Dataset 2 showed unstable training, lower accuracy, overlapping latent representations, and inconsistent explanations, suggesting the approach may not generalize reliably to more complex real-world data
- To fit quantum constraints, the pipeline applies PCA dimensionality reduction to 6 components, which may discard financially meaningful information and affect both predictive performance and interpretability
- The study uses only 6 qubits and 4 variational layers, constraining representational scale and leaving larger problem sizes untested
- All quantum experiments were run on the PennyLane default.qubit simulator rather than real quantum hardware
- No evaluation of hardware noise, decoherence, readout errors, or noise-mitigation strategies is provided
- The paper does not demonstrate scalability to production-scale credit scoring workloads or larger feature spaces
- Interpretability is largely post-hoc; the explanations do not guarantee faithful causal reasoning by the QNN
- The authors note that gradient-based explanations were inconsistent in noisy predictions and should be used cautiously in quantum settings
- The proposed ICAA metric is introduced and used in this paper, but broader validation against human judgment, regulatory needs, or established explainability benchmarks is not shown
- The work explicitly does not aim to outperform classical machine learning models, so its practical advantage over strong classical baselines remains unclear
- [inferred] No direct comparison with state-of-the-art classical credit-scoring models is reported, making it difficult to assess whether the quantum approach offers any predictive or interpretability benefit
- [inferred] No ablation study is described to isolate the contribution of the quantum layer, the hybrid architecture, PCA preprocessing, or the ICAA metric
- [inferred] The use of class balancing methods such as undersampling and SMOTE may alter the original data distribution and affect real-world validity
- [inferred] The paper does not report repeated runs, confidence intervals, or statistical significance tests, so result stability is hard to assess
- [inferred] Perfect performance on Dataset 1 raises the possibility of dataset simplicity, leakage, or benchmark saturation rather than demonstrating broad model capability
- [inferred] Fairness, bias, and subgroup performance are not empirically evaluated despite the regulatory framing of credit scoring
- [inferred] Regulatory compliance is discussed conceptually, but no formal auditability or compliance assessment is performed
- [inferred] Reproducibility is only partial: some settings are given, but full code, preprocessing details, dataset versions, and experiment artifacts are not included in the text
- [inferred] The approach is tested only for multiclass static classification and does not address temporal credit dynamics, concept drift, or changing macroeconomic conditions
## Open questions
- How well does IQNN-CS generalize to more complex, noisier, and institution-specific credit datasets beyond the two benchmarks used here?
- Will the proposed interpretability framework remain reliable when scaling to more features, more classes, and larger qubit counts?
- How would IQNN-CS perform on real quantum hardware under realistic noise and limited connectivity constraints?
- Does ICAA correlate with explanation faithfulness, human expert judgment, or regulatory usefulness in real credit decision workflows?
- Can the model maintain interpretability without PCA compression, or with alternative feature encoding strategies?
- What specific data characteristics make a credit dataset align well or poorly with the model's quantum inductive bias?
- How does the hybrid QNN compare against strong classical baselines in both predictive performance and explanation quality?
- Are the observed explanation patterns stable across random seeds, train/test splits, and repeated training runs?
- Can post-hoc explanations for QNNs be trusted in high-stakes lending decisions when gradient-based methods become inconsistent on difficult datasets?
- How robust is the method to class imbalance, distribution shift, and out-of-sample changes in borrower behavior?
- Does the model satisfy fairness requirements across protected groups, and how do its explanations interact with fairness constraints?
- What is the computational cost of training and explaining the model relative to classical interpretable credit-scoring systems?

**Future work:**
- Validate IQNN-CS and the ICAA metric on additional real-world credit-scoring datasets with greater diversity and complexity
- Test the framework on real quantum hardware and study the impact of noise, decoherence, and error mitigation on both accuracy and interpretability
- Benchmark against state-of-the-art classical credit-scoring and explainable AI methods to quantify any practical quantum advantage
- Perform ablation studies to isolate the effects of the quantum layer, preprocessing choices, and each interpretability component
- Develop more robust and standardized interpretability tools for structured multiclass QML tasks
- Investigate alternative encoding schemes and dimensionality-reduction methods that preserve more financial information while remaining quantum-compatible
- Study scalability to larger feature spaces, more classes, and production-scale financial datasets
- Evaluate explanation stability and model reliability across multiple seeds, perturbations, and cross-validation settings
- Incorporate fairness, bias auditing, and regulatory compliance evaluation into the assessment of interpretable QML credit models
- Explore methods for detecting and handling indecisive or unreliable predictions in high-stakes financial settings
- Extend the framework to other regulated financial applications and possibly healthcare, as suggested in the conclusion
- Investigate intrinsically interpretable quantum model designs rather than relying primarily on post-hoc explanations
## Key ideas
- #idea:hybrid-approach — Proposes IQNN-CS, a hybrid classical–quantum neural network for multiclass credit scoring with classical preprocessing/postprocessing around a 6-qubit variational quantum layer.
- #idea:near-term-feasibility — Focuses on NISQ-compatible simulated QNNs for regulated credit scoring, emphasizing interpretability and transparency rather than quantum speedup.
- #idea:near-term-feasibility — Introduces Inter-Class Attribution Alignment (ICAA) as a diagnostic for whether class-specific reasoning in multiclass credit scoring is disentangled or overlapping.
- #idea:hybrid-approach — Uses PCA compression to 6 components to fit qubit constraints, then applies angle encoding and StronglyEntanglingLayers as a learned quantum feature map.
- #idea:near-term-feasibility — Shows interpretability tools can reveal coherent model behavior on an easier dataset and unstable, ambiguous reasoning on a harder dataset.
## Contradictions
- The paper explicitly does not claim quantum superiority and provides no classical baseline, which contradicts stronger quantum-performance narratives in finance-oriented QML papers; any implication of practical benefit over classical credit-scoring models remains unsubstantiated.
- The paper discusses regulated financial applicability, but its evidence is limited to 6-qubit simulator experiments with PCA-compressed inputs and no hardware validation, contradicting broader claims that current quantum methods scale to realistic production credit-scoring workloads.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
