---
aliases:
- 'Quantum machine learning on near-term quantum devices: Current state of supervised
  and unsupervised techniques for real-world applications'
- Quantum machine learning near
authors:
- Yaswitha Gujju
- Atsushi Matsuo
- Rudy Raymond
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PhysRevApplied.21.067001
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Applied
methodology_tags:
- quantum-ML
- quantum-SVM
- VQE
- variational
paper_type: ''
quantum_advantage_claim: disputed
related_papers:
- 2020_Havlicek_SupervisedLearningQuantum
- 2021_Huang_QuantumAdvantageKernel
- 2022_Rebentrost_QuantumMachineLearning
relevance_phase1: high
relevance_phase3: medium
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-25T16:03:40.934567'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:03:46.201528'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:03:57.431040'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:04:38.413552'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:05:29.952929'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:05:48.056342'
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
- topic/derivatives-pricing
- method/quantum-ML
- method/quantum-SVM
- method/VQE
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum machine learning on near-term quantum devices: Current state of supervised
  and unsupervised techniques for real-world applications'
topic_tags:
- fraud-detection
- derivatives-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
The paper surveys quantum machine learning methods that have actually been implemented on near-term gate-based quantum hardware, with an emphasis on supervised and unsupervised techniques applied to real-world domains such as high-energy physics, finance, and healthcare. It reviews encoding strategies, variational and kernel-based models, and other architectures like QGANs, tensor networks, and quantum PCA, comparing their performance to classical baselines and highlighting practical constraints from current devices. The authors also analyze key limitations—noise, data loading, barren plateaus, long runtimes, and lack of benchmarks—and outline open research directions in error mitigation, ansatz design, quantum data, federated/ensemble schemes, security, and explainability for QML.
## Methodology
This paper is a narrative review/survey of quantum machine learning (QML) on near-term gate-based quantum hardware, with emphasis on supervised and unsupervised techniques applied to real-world domains. The authors explicitly scope the review to QML implementations executed on real hardware, focusing on high-energy physics, finance, and healthcare, while excluding reinforcement learning and quantum chemistry from the main survey despite acknowledging their relevance. The review concentrates on two major QML framework families—quantum kernel methods and variational quantum algorithms—and synthesizes prior work by categorizing papers according to application domain, task type, hardware architecture, training environment, qubit count, and method. The paper provides summary tables for included studies in high-energy physics, finance, healthcare, benchmark datasets, quantum datasets, and artificial datasets, listing for each paper the reference, number of qubits, hardware type (e.g., superconducting, ion-trap), whether training was performed on a QPU or simulator, and the QML method used (e.g., VQC, kernel, QGAN, QPCA, Q-K means). The synthesis is thematic rather than meta-analytic: it reviews encoding strategies, ansatz design, optimization methods, error mitigation, hardware limitations, and comparative performance versus classical counterparts, then discusses bottlenecks and future research directions. The paper notes that the list of surveyed papers was compiled to include as many relevant papers as possible but is not claimed to be exhaustive, and it references use of arXiv/open-access sources for gathering much of the literature. No formal systematic search protocol, database query string, PRISMA flow, or explicit inclusion/exclusion criteria beyond topical scope are reported.

**Algorithms used:** Quantum kernel methods, Variational quantum algorithms, Variational quantum circuit, Quantum support vector machine, Quantum kernel estimation, Swap-test classifier, Quantum principal component analysis, Quantum generative adversarial network, Quantum autoencoder, Quantum tensor networks, Quantum orthogonal neural networks, Quantum K-means
**Frameworks:** IBM Quantum, Qiskit, PennyLane

**Dataset:** As a review article, the paper does not use a single experimental dataset. It surveys prior studies across real-world domains including finance, healthcare, and high-energy physics, and also summarizes work using benchmark datasets such as MNIST, Fashion-MNIST, Iris, Titanic Survival, Astronomical, Wine, as well as quantum datasets and synthetic/artificial datasets.
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [supported] The review identifies quantum kernel methods and variational quantum circuits as the two dominant QML frameworks implemented on near-term gate-based hardware for real-world applications, including finance.
- [supported] Across the reviewed literature, current QML performance on real hardware is strongly constrained by noise, limited qubit counts, connectivity, coherence time, state-preparation and measurement errors, and long execution times.
- [supported] The review finds that efficient classical-data encoding is a central bottleneck for practical QML, with the data-loading problem limiting claims of speedup for many amplitude-encoding-based approaches.
- [supported] Across reviewed studies, hardware-aware choices in encoding, ansatz design, error mitigation, and optimizer selection materially affect QML performance on NISQ devices.
- [supported] The review reports broad consensus that empirical evidence for clear quantum advantage in QML remains limited, especially for classical datasets and real-world tasks.
- [supported] The review notes that finite sampling noise, noisy kernel estimation, and hardware noise often erode any apparent advantage of heuristic quantum learning methods.
- [supported] In finance applications reviewed, QML has been explored for data loading, classification, dimensionality reduction, and feature selection rather than demonstrating decisive end-to-end superiority over classical finance ML pipelines.
- [supported] The review highlights a finance use case where variational quantum algorithms for feature selection on 20 qubits achieved hardware results comparable to state-of-the-art classical methods in some aspects and sometimes found better feature subsets without error mitigation.
- [supported] The review identifies quantum principal component analysis as a finance-relevant approach for reducing noisy factors in derivative pricing, but notes difficulty scaling to larger datasets in reviewed experiments.
- [supported] The review cites quantum reservoir computing for foreign-exchange modeling as a promising near-term finance direction, with reported accurate depiction of stochastic exchange-rate evolution relative to classical methods in the cited study.
- [supported] The review finds disagreement or uncertainty in the literature over whether observed QML gains stem from genuine quantum structure or from benchmark choice, hyperparameter tuning, and comparison methodology.
- [supported] The review emphasizes that quantum advantage appears more plausible when learning from inherently quantum data than from classical data encoded into quantum states.
- [supported] The review identifies barren plateaus, optimizer instability, and poor scalability as recurring algorithmic limitations across variational QML studies.
- [supported] The review concludes that standardized benchmarks, better quantum datasets, improved error mitigation, scalable ansatz/optimizer design, and stronger reproducibility practices are needed before robust claims about practical QML advantage can be made.
- [speculative] The review suggests that future progress in error mitigation, data preparation, federated learning, and hardware improvements may enable more practical and scalable QML applications in finance and other industries.
- [speculative] The review suggests that QML may eventually deliver advantage in sample complexity or time complexity, but only under specific conditions that are not yet established empirically.
- [disputed] Claims of polynomial or exponential QML speedups for practical applications are presented as unsettled because the review notes that strong empirical demonstrations and robust theoretical foundations are still lacking.

**Results summary:** This review surveys supervised and unsupervised quantum machine learning implementations on near-term gate-based quantum hardware, with attention to real-world domains including finance. The main synthesis is that quantum kernel methods and variational quantum circuits dominate current practice, but their real-world utility is limited by hardware noise, qubit/connectivity constraints, long runtimes, inefficient classical-data loading, and trainability issues such as barren plateaus. For finance, the reviewed literature covers data loading, classification, dimensionality reduction, and feature selection, with some hardware experiments showing performance comparable to classical baselines in selected settings, but no robust, general quantum advantage. The review’s overall consensus is that practical QML remains exploratory: promising for certain structured or quantum-native data settings, but not yet empirically superior to classical methods for most real-world financial tasks.

**Performance claims:**
- Finance feature selection study reviewed used 20 qubits and reported hardware results comparable to state-of-the-art classical methods in some aspects, with potential to find better feature subsets without error mitigation
- Finance QPCA study reviewed ran on a 5-qubit IBM Quantum device for 2x2 and 3x3 cross-correlation matrices
- QPCA is described in reviewed literature as constructing principal components in time O(log N) for Hilbert-space dimension N, implying exponential speedup under stated assumptions
- Quantum reservoir computing study cited in the review reportedly modeled foreign-exchange stochastic evolution accurately compared with classical methods
- Healthcare quantum adversarial learning study reviewed reached perfect accuracy in about 30 epochs on training and test datasets for quantum data
- HEP VQC study reviewed reported AUC around 0.80 on 3-qubit hardware/simulator
- HEP one-qubit data-reuploading study reviewed reported inference AUC of 0.830
- HEP 15-qubit QSVM study reviewed reported average AUC 0.831 for training sample size 100 and hardware test AUC approximately 0.78
- HEP 10-qubit VQC study reviewed reported AUC greater than 0.80 and approximately 200 hours for 500 training iterations on 100 events
## Quantum advantage claim
**Classification:** disputed

As a review article, the paper synthesizes literature rather than demonstrating new advantage itself. It repeatedly states that empirical evidence for practical quantum advantage in QML is still limited, that many speedup claims depend on restrictive assumptions such as efficient data loading or quantum-native data, and that observed gains may reflect benchmark or hyperparameter choices rather than genuine quantum superiority.
## Limitations
- The review explicitly excludes reinforcement learning, directing readers elsewhere for that literature.
- The review excludes quantum chemistry from its scope despite acknowledging it as a promising application area.
- The review focuses only on gate-based architectures and excludes other hardware paradigms such as quantum annealing.
- The authors acknowledge that the paper coverage may not be exhaustive due to the rapid pace of development in the field.
- Current QML on near-term hardware is limited by noise, limited qubit connectivity, short coherence times, and state-preparation/measurement errors.
- Prolonged running times on current quantum hardware negatively affect execution and outcomes of QML algorithms.
- Efficient encoding of classical data remains a major limitation, including the data-loading problem and difficulty of storing prepared quantum states without decoherence.
- Variational algorithms suffer from training issues such as barren plateaus, and performance is highly sensitive to optimizer and loss-function choices.
- Kernel methods are limited by the need to choose suitable feature maps and by noisy kernel estimation from finite sampling.
- Scalability and generalization of current QML models remain limited for real-world applications.
- Security vulnerabilities, including susceptibility to adversarial attacks, remain a limitation of current QML models.
- Quantum kernels incur additive noise in each kernel entry due to finite sampling.
- Quantum kernel methods scale poorly with dataset size, with quantum cost scaling quadratically with the training dataset size.
- Useful quantum kernels are constrained by limited qubit counts and heuristic feature-map design.
- Error mitigation for kernels can require significant additional quantum resources.
- Classical optimizers for VQCs require repeated measurements and can converge slowly under noise.
- Gradient calculation complexity in classical optimization grows with feature size and can become a scalability bottleneck.
- Practical implementation of quantum gradient methods still faces applicability and complexity challenges.
- Current training frameworks for QNNs require direct gradient computation on quantum devices, which faces scalability challenges and is sensitive to hardware limitations and sampling noise.
- QGAN training is vulnerable to mode collapse, reducing sample diversity.
- Current quantum hardware has low qubit coherence times and insufficient qubit count/gate fidelity for practical quantum error correction.
- Increasing the number of measurements to reduce generalization error can be counterproductive because of readout error and calibration variability.
- Limited qubit connectivity can require SWAP-gate insertion, adding overhead and error.
- Cloud access to QPUs introduces delays and unclear calibration timing, which can create significant statistical errors.
- Lack of information about qubit assignment, transpilation/compiler methods, drift rate, and time since calibration hampers analysis and reproducibility.
- Long running times on current hardware make validation on multiple sets infeasible and limit practical use on large real-world datasets.
- Small sample sizes often lead to significant variance and poor performance.
- Limited access to QPU resources constrains experimentation and validation.
- Data loading can consume a significant portion of coherence time, leaving little time for the actual learning algorithm.
- Some proposed shallow data loaders have connectivity requirements beyond what current hardware supports.
- There is currently no efficient QRAM capable of reliably encoding and storing information as quantum states.
- Barren plateaus remain a major limitation, especially with expressive ansatzes, exhaustive entanglement, unsuitable observables, poor initialization, and hardware noise.
- Empirical evidence for clear quantum advantage over classical algorithms is still limited.
- A robust theoretical foundation for quantum advantage in QML is still lacking.
- It remains unclear whether reported gains stem from genuine structural quantum advantage or from careful hyperparameter tuning and benchmark selection.
- Finite sampling noise prevents heuristic quantum learning algorithms from being proven to solve classically hard learning problems.
- Only a few variational quantum algorithms have shown apparent advantage, and only in constrained settings.
- There is a lack of standardized quantum datasets and benchmarks for evaluating QML models.
- The current state of QML lacks privacy-preserving features.
- Many studies do not discuss hyperparameter choices in depth, reducing transparency and interpretability.
- Many promising studies do not provide open-source reference implementations, hindering reproducibility.
- Reproducibility is further complicated by frequent updates and deprecations in software stacks such as Qiskit.
- [inferred] The review appears to rely heavily on arXiv and sampled recent papers, which may introduce search-source bias and underrepresent non-arXiv or non-open-access literature.
- [inferred] No explicit systematic review protocol, search string, database list, inclusion/exclusion workflow, or quality-assessment procedure is described, limiting methodological reproducibility.
- [inferred] The review does not mention language restrictions, so non-English literature may be underrepresented.
- [inferred] Grey literature coverage appears limited or unsystematic despite the practical/industrial focus, which may omit relevant industry evidence.
- [inferred] Because the review spans a fast-moving field, its conclusions may become outdated quickly and may miss very recent hardware and algorithmic advances.
## Open questions
- Can QML demonstrate a clear quantum advantage over classical methods in practical data science applications, either in sample complexity or time complexity?
- Are observed QML performance improvements due to genuine structural quantum advantage or mainly due to careful hyperparameter selection, benchmarking, and comparisons?
- Does an efficient classical algorithm exist for many learning problems currently targeted by quantum learning algorithms?
- How can standardized and practically meaningful benchmarks and datasets for QML be established, especially quantum datasets?
- What is the most suitable encoding technique for a given dataset, and how can one identify datasets that truly benefit from quantum kernel computation?
- How can efficient QRAM or equivalent mechanisms for encoding and reliably storing quantum data be realized?
- How can error mitigation and quantum error correction be made efficient enough for practical QML without erasing potential speedups?
- How can ansatzes be selected to avoid barren plateaus while remaining expressive and scalable?
- What is the precise role of entanglement in model ansatz design and QML performance?
- How can parameter initialization strategies for large-scale QNNs be designed to improve scalability?
- How should trainability and prediction error be analyzed for large-scale QML problems?
- Can alternative optimization methods outperform backpropagation-like approaches for parameterized quantum circuits?
- What is the true computational complexity of gradient methods for parameterized quantum models, and how can scalability be improved?
- How can privacy-preserving techniques such as differential privacy be effectively incorporated into QML?
- How robust are QML models to adversarial attacks, and when can hybrid quantum-classical defenses improve security?
- How can explainability and interpretability be developed for QML systems in ways that go beyond classical XAI?
- How can quantum feature spaces and QPU-dependent model behavior be explained in human-understandable terms?
- How can federated learning and quantum boosting be used to improve scalability and utilization of limited-capability quantum devices?
- Which practically relevant problems are genuinely hard for classical simulation and therefore suitable targets for demonstrating useful quantum advantage?

**Future work:**
- Develop standardized benchmarks and datasets, including practically meaningful quantum datasets, for fair evaluation of QML against classical methods.
- Investigate quantum-data-based QML further, as it may offer more promise for quantum advantage than classical-data-based QML.
- Design and identify optimal or task-specific data-encoding techniques and feature maps for different datasets.
- Develop efficient QRAM or alternative hardware/software mechanisms for quantum data preparation and storage.
- Advance error-mitigation and quantum error-correction methods suitable for QML on near-term and future fault-tolerant devices.
- Explore quantum autoencoders for error correction, including their fault tolerance and integration into broader error-correction frameworks.
- Study ensemble-learning-based error mitigation for VQCs and extend such methods to classification, kernel learning, regression, and QSVMs.
- Investigate ansatz selection strategies that improve scalability and reduce barren plateaus.
- Study the impact of entanglement in model ansatzes more systematically.
- Develop efficient methods for parameter adjustment and loss minimization in VQCs.
- Explore parameter initialization strategies for large-scale QNNs.
- Analyze trainability and prediction error to better understand scalability on large problems.
- Develop open-source tools for quantum circuit/ansatz selection tailored to specific quantum devices.
- Explore alternative optimization architectures and methods beyond standard backpropagation for parameterized quantum circuits.
- Implement privacy-preserving QML methods, including differential privacy.
- Investigate secure distributed learning approaches such as quantum federated learning for sensitive data settings.
- Develop explainable quantum machine learning (XQML) methods to provide human-understandable interpretations of QML systems.
- Study hyperparameter choices more systematically and improve transparency through better documentation and open-source reference implementations.
- Promote reproducibility through standardized benchmarks, detailed experimental documentation, source-code sharing, and open-science practices.
- Investigate federated learning to distribute computational tasks across limited-capability quantum machines.
- Study quantum boosting and ensemble methods to improve scalability and performance on near-term devices.
- Establish community consensus on practically relevant problems that are genuinely difficult for classical simulation.
- Continue developing both quantum and classical approximation methods as mutual benchmarks for assessing progress.
## Key ideas
- #idea:near-term-feasibility — Survey shows finance-related QML has been implemented on real NISQ hardware, but only for small-scale tasks such as feature selection, dimensionality reduction, and exploratory modeling.
- #idea:hybrid-approach — Practical QML workflows are predominantly hybrid, combining variational circuits or kernel methods with classical optimization and preprocessing.
- #idea:quantum-advantage — The review finds no robust empirical quantum advantage for real-world financial QML tasks; any future advantage is framed as conditional on restrictive assumptions such as quantum-native data or hard-to-simulate feature maps.
- #idea:near-term-feasibility — Finance examples include feature selection, QPCA for factor reduction in derivative pricing, and foreign-exchange modeling, demonstrating technical feasibility rather than production-ready superiority.
- #idea:quantum-advantage — The paper argues that many claimed QML speedups are undermined in practice by noise, finite sampling, and especially classical data-loading costs.
- #idea:hybrid-approach — Ensemble, federated, and boosting-style hybrid QML are proposed as possible routes to improve robustness and make better use of limited-capability devices.
## Contradictions
- The review disputes strong claims of near-term quantum superiority in QML, arguing that observed gains often disappear when compared carefully against classical baselines and realistic hardware constraints; this contrasts with more optimistic readings such as 2022_Rebentrost_QuantumMachineLearning and 2021_Huang_QuantumAdvantageKernel.
- The paper highlights poor practical scaling of quantum kernels and QPCA under noise, finite sampling, and dataset growth, contradicting idealized exponential-speedup narratives such as 2020_Havlicek_SupervisedLearningQuantum.
- It challenges amplitude-encoding and HHL-style speedup claims by emphasizing that data preparation and encoding costs are nontrivial, so theoretical advantages may not transfer to practical financial ML settings.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
