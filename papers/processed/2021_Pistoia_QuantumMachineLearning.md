---
aliases:
- Quantum Machine Learning for Finance
- Quantum Machine Learning Finance
authors:
- Marco Pistoia
- Syed Farhan Ahmad
- Akshay Ajagekar
- Alexander Buts
- Shouvanik Chakrabarti
- Dylan Herman
- Shaohan Hu
- Andrew Jena
- Pierre Minssen
- Pradeep Niroula
- Arthur Rattew
- Yue Sun
- Romina Yalovetzky
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
journal_or_venue: arXiv
methodology_tags:
- HHL
- quantum-ML
- quantum-SVM
- quantum-annealing
- QUBO
- variational
- amplitude-estimation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:55:42.617820'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:55:48.114140'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:01.379341'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:56:40.144125'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:57:20.566231'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:57:40.725247'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/asset-pricing
- topic/fraud-detection
- topic/credit-scoring
- topic/high-frequency-trading
- topic/derivatives-pricing
- topic/risk-modelling
- method/HHL
- method/quantum-ML
- method/quantum-SVM
- method/quantum-annealing
- method/QUBO
- method/variational
- method/amplitude-estimation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Machine Learning for Finance
topic_tags:
- asset-pricing
- fraud-detection
- credit-scoring
- high-frequency-trading
- derivatives-pricing
- risk-modelling
year: 2021
zotero_key: ''
---

## Abstract summary
This review surveys the state of quantum machine learning algorithms and analyzes how they can be applied to financial use cases. It organizes the discussion around core ML tasks—regression, classification, clustering, generative modeling, feature extraction, reinforcement learning, and NLP—and maps each to concrete financial problems such as asset pricing, fraud detection, credit scoring, and algorithmic trading. The paper also discusses expected quantum speedups, practical constraints of NISQ hardware, and where current methods remain theoretical versus ready for near-term experimentation in financial services.
## Methodology
This paper is a preprint review article rather than an original empirical or theoretical study. Its methodology is a narrative state-of-the-art survey of quantum machine learning methods relevant to finance, organized by machine-learning task categories: regression, classification, clustering, generative modeling, quantum-assisted feature extraction, reinforcement learning, and natural language processing. Within each category, the authors summarize representative quantum algorithms from prior literature, discuss their computational assumptions and claimed speedups, and map them to financial-service use cases such as asset pricing, implied-volatility estimation, fraud detection, credit scoring, stock selection, algorithmic trading, market making, and risk assessment. The paper does not report a formal search protocol, inclusion/exclusion criteria, database query strategy, or quantitative synthesis; instead, it provides a conceptual taxonomy and literature-based discussion of algorithmic approaches, including HHL-based linear regression, QSVM/VQC, quantum clustering, qGANs, quantum Boltzmann machines, quantum PCA, quantum annealing for QUBO feature selection, quantum reinforcement learning, and quantum NLP.

**Algorithms used:** HHL, L2 quantum linear regression, Quantum recurrent neural networks, Quantum LSTM, Deep quantum neural networks, Quantum perceptron, Quantum nearest centroid classifier, Quantum k-nearest neighbors, QSVM, Variational Quantum Classifier, destructive SWAP test, controlled-SWAP test, IQP feature map, Dynamic Quantum Clustering, q-means, Quantum spectral clustering, Quantum Boltzmann Machine, Quantum Annealing, Imaginary Time Evolution, Variational Imaginary Time Evolution, qGAN, Quantum Born Machine, Quantum PCA, Gaussian Boson Sampling, QUBO feature selection, Quantum reinforcement learning, Variational quantum circuits for deep reinforcement learning, Quantum NLP CSC model
**Frameworks:** D-Wave, IBM Quantum, IonQ
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] This paper is a review that maps quantum machine learning in finance into seven task areas: regression, classification, clustering, generative modeling, feature extraction, reinforcement learning, and natural language processing.
- [speculative] The authors argue finance may be among the earliest industries to benefit from quantum computing because many financial use cases tolerate approximation and may fit NISQ-era methods.
- [speculative] The paper states that no end-to-end quantum machine learning application with exponential speedup over a classical counterpart has yet been discovered.
- [speculative] The authors claim that several quantum machine learning subroutines offer promising polynomial speedups, especially in linear algebra, classification, clustering, and optimization components, but these gains are conditional on data access and output-readout assumptions.
- [speculative] A central caveat emphasized throughout the review is that many claimed speedups rely on efficient data loading, often via QRAM, and that data input/output bottlenecks can negate overall advantage.
- [speculative] For regression, the review claims quantum linear-systems-based methods can in principle accelerate least-squares regression, but practical usefulness is limited by QRAM construction costs and the need to extract classical model parameters.
- [speculative] For asset pricing and time-series forecasting, the paper suggests parameterized quantum circuits, quantum RNNs, and quantum LSTMs may improve convergence, expressivity, or prediction quality, but applicability to real financial asset-pricing tasks remains largely untested.
- [supported] The review cites classical empirical evidence that machine-learning asset-pricing models on the S&P 500 achieved an out-of-sample annualized Sharpe ratio of 0.77 versus 0.51 for buy-and-hold, and a long-short decile spread Sharpe ratio of 1.35.
- [speculative] For classification, the review claims quantum perceptron, kernel, and SVM-style methods can provide quadratic or better complexity improvements under specific assumptions, especially when quantum feature maps are classically hard to simulate.
- [speculative] The paper presents QSVMs and VQCs as promising hybrid approaches for financial classification tasks such as binary option prediction, credit scoring, and forecasting, but does not provide finance-specific empirical validation in this paper.
- [supported] The review notes an experimental nearest-centroid classifier was run on an IonQ trapped-ion quantum computer with accuracy matching the classical nearest-centroid baseline, while explicitly not claiming time-complexity speedup.
- [speculative] For clustering, the paper argues quantum clustering, q-means, and coreset-based methods may help with fraud detection, stock selection, exchange-rate regime identification, and hedge-fund clustering, but these are presented mainly as candidate applications.
- [speculative] For generative modeling, the review claims quantum Boltzmann machines, qGANs, and quantum Born machines could support fraud detection and probability-distribution loading for downstream finance tasks.
- [speculative] The paper argues that efficient probability distribution preparation is a key enabler for quantum finance workflows and that learned quantum generators could feed amplitude-estimation-based derivative pricing methods.
- [speculative] The review states that amplitude estimation offers a theoretical quadratic speedup over classical Monte Carlo for derivative pricing once suitable probability distributions are prepared.
- [speculative] For feature extraction, the paper claims quantum PCA can theoretically provide exponential speedup under HHL-like assumptions and may help reduce model dimensionality in finance, such as volatility-factor reduction.
- [speculative] The review suggests quantum annealing can be used for combinatorial feature selection in credit scoring by formulating the task as a QUBO over feature relevance and redundancy.
- [speculative] For reinforcement learning, the paper claims quantum RL may provide quadratic improvements for policy evaluation and could eventually benefit algorithmic trading and market making, though direct financial applications are not yet demonstrated.
- [speculative] For NLP, the review claims quantum compositional language models may accelerate sentence classification and could be relevant to risk assessment, financial forecasting, and accounting/auditing tasks involving unstructured text.
- [speculative] Overall, the paper positions itself as a roadmap rather than an empirical demonstration, emphasizing both the promise of quantum ML in finance and the current limitations imposed by hardware, trainability, and data-loading constraints.

**Results summary:** This preprint is a review article rather than a new empirical study. It surveys quantum machine learning methods relevant to financial services across regression, classification, clustering, generative modeling, feature extraction, reinforcement learning, and NLP. The main message is that quantum methods may offer theoretical speedups in important subroutines, but practical end-to-end quantum advantage in finance has not yet been demonstrated. The paper repeatedly highlights caveats around QRAM, data loading, output extraction, and NISQ hardware limitations. It includes a small number of cited empirical examples from prior literature, such as a nearest-centroid classifier on IonQ hardware matching classical accuracy and classical deep-learning asset-pricing results with Sharpe ratios of 0.77 and 1.35, but the finance-specific quantum claims in the paper are mostly forward-looking and speculative.

**Performance claims:**
- Quantum least-squares regression runtime claimed as O~(log(N) s^3 kappa^6 / epsilon) for the Wiebe et al. approach
- Quantum L2 regression with classical output claimed as poly(log(N), d, kappa, 1/epsilon)
- Prediction-by-linear-regression approach claimed as O(log(N) kappa^2 / epsilon^3)
- Amortized L2-regression complexity with specialized data structures claimed as O~(kappa mu / epsilon * poly(log(Nd)))
- Quantum-inspired classical regression cost claimed as O~(||X||_F^6 ||X||^2 / epsilon^4)
- Classical ML asset-pricing forecast on S&P 500 cited with out-of-sample annualized Sharpe ratio 0.77 versus 0.51 for buy-and-hold
- Classical value-weighted long-short decile spread strategy cited with annualized Sharpe ratio 1.35
- Quantum perceptron-style classification runtime claimed as O(sqrt(nd)/gamma^2) or O(sqrt(nd)/gamma)
- Optimal quantum classifier training runtime claimed as O~(sqrt(n) + sqrt(d)) versus classical O~(n + d)
- Quantum k-NN worst-case time complexity claimed as O(sqrt(M) log(M)) for low-dimensional feature vectors
- Alternative quantum k-NN query complexity claimed as O(sqrt(kM))
- Quantum interior-point/SVM method on random instances claimed to achieve O(n^2.59) versus classical O(n^3.11)
- QSVM runtime claimed as O(log(NM))
- Quantum NLP sentence classification runtime claimed as O(sqrt(MN) log(M)) versus classical O(NM)
- q-means clustering claimed to have polylogarithmic time complexity in dataset size
- Amplitude estimation for derivative pricing claimed to provide a theoretical quadratic speedup over classical Monte Carlo
- Quantum PCA claimed to run in time polynomial in log of the dimension under certain assumptions
- Top three principal components are stated to often explain over 95% of output variation in a model-reduction finance example
- Nearest-centroid classification on IonQ hardware reported to match classical nearest-centroid accuracy, with no speedup claim
## Quantum advantage claim
**Classification:** speculative

Because this is a preprint review, most advantage claims are theoretical or literature-based rather than demonstrated in this paper. The authors explicitly note that no end-to-end quantum ML application with exponential speedup has yet been found, and many claimed gains depend on strong assumptions such as QRAM and efficient data loading.
## Limitations
- As a preprint, the paper has not undergone peer review.
- The paper explicitly notes that today's NISQ devices have low qubit counts, short coherence times, and high operation noise, limiting near-term practical deployment.
- The review states that efficiently loading classical data into quantum computers and extracting classical outputs remains an open challenge; many algorithms rely on QRAM, whose concrete hardware implementations are still unavailable.
- The paper explicitly notes that quantum linear-algebra algorithms cannot always be applied out of the box to financial use cases; several conditions and customizations are required.
- The authors state that end-to-end financial workflows involve multiple classical and quantum components, any of which can become a bottleneck and negate overall quantum advantage.
- The paper explicitly states that no end-to-end quantum ML application with exponential speedup over a classical counterpart has yet been discovered.
- For quantum regression based on linear systems, the paper notes major caveats: QRAM/data-structure construction may require O(N log N) time and obtaining a full classical description of the output may require approximately O(d) copies of the output state.
- For asset pricing, the paper states that the applicability of PQC-based RNN/LSTM approaches to asset pricing has yet to be investigated.
- For nearest-centroid classification on trapped-ion hardware, the paper notes that the reported approach matches classical accuracy but does not claim any quantum speedup in time complexity.
- For QSVM kernel evaluation, the controlled-SWAP test has better asymptotic complexity but is not as feasible on NISQ devices, while the destructive SWAP test is more feasible but has prohibitive asymptotic scaling.
- For some quantum SVM methods, the paper notes that runtime depends on terms that are difficult to bound directly, limiting clarity about practical advantage.
- The paper explicitly states that variational quantum classifiers suffer from barren plateaus, making optimization difficult.
- The authors note that VQC architecture design remains poorly understood, including the choice of cost functions and parameter initialization.
- The paper states that fixed-form variational circuits may be insufficiently expressive to capture all necessary states in Hilbert space.
- For clustering, the paper notes that loading large datasets onto quantum devices may incur huge time/space overhead, motivating the use of coresets.
- For NLP based on CSC/DisCo models, the paper notes that large tensor-product spaces create computational challenges, while classical dimensionality-reduction workarounds rely on assumptions that may not hold.
- The paper states that quantum NLP speedups hold only if certain conditions are met.
- For algorithmic trading, the paper explicitly states that due to current hardware limitations, quantum RL approaches have not yet been directly applied.
- [inferred] As a review-style preprint, the paper does not provide a systematic review protocol, search strategy, inclusion/exclusion criteria, or quality assessment methodology, limiting reproducibility of the literature synthesis.
- [inferred] Many cited advantages are theoretical or based on complexity analysis rather than robust empirical demonstrations on realistic financial datasets.
- [inferred] The paper provides limited head-to-head benchmarking against state-of-the-art classical financial ML baselines across the surveyed use cases.
- [inferred] Practical issues central to financial deployment—such as latency, regulatory compliance, interpretability, transaction costs, and model risk governance—are only lightly addressed.
- [inferred] Several discussed financial applications are speculative mappings from generic quantum ML methods rather than validated finance-specific implementations.
- [inferred] The review does not quantify how hardware noise affects solution quality across the surveyed algorithms.
- [inferred] The paper is authored by an industry institution (JPMorgan), so there may be institutional framing bias despite the disclaimer.
## Open questions
- When, if ever, will end-to-end quantum ML applications for finance demonstrate exponential speedup over classical counterparts?
- Can practical QRAM or alternative data-loading schemes be realized efficiently enough to preserve claimed quantum advantages?
- How should quantum speedup be evaluated for full financial workflows when data loading, preprocessing, optimization, and readout costs are included?
- Do PQC-based recurrent models or quantum LSTMs provide meaningful advantages for real asset-pricing tasks?
- Which financial use cases can achieve genuine near-term benefit on NISQ hardware despite noise and limited qubit counts?
- How can barren plateaus and trainability issues in variational quantum classifiers be mitigated in realistic finance applications?
- What circuit architectures, cost functions, and parameter-initialization strategies are best for finance-oriented VQCs?
- Under what data conditions are quantum kernels and QSVMs classically hard enough to yield practical advantage?
- Can coresets or other compression methods preserve enough financial information to make quantum clustering useful on small devices?
- How well do quantum generative models learn realistic financial probability distributions compared with advanced classical generative models?
- Can quantum RL be made practical for algorithmic trading and market making under realistic market frictions and partial observability?
- What are the empirical effects of hardware noise, decoherence, and finite sampling on financial ML performance metrics such as Sharpe ratio, classification accuracy, or risk estimates?
- How scalable are the surveyed methods with respect to number of assets, features, time steps, and market scenarios?
- Can quantum NLP methods deliver measurable gains on real financial text tasks such as risk assessment, forecasting, and auditing?

**Future work:**
- Investigate the applicability of PQC-based RNNs and quantum LSTM models to asset pricing.
- Develop practical alternatives to QRAM and more efficient classical-to-quantum data-loading methods.
- Design customized end-to-end hybrid quantum-classical pipelines for specific financial use cases rather than relying on generic linear-algebra subroutines.
- Study and mitigate bottlenecks in full financial workflows so that subroutine-level speedups translate into end-to-end advantage.
- Explore adaptive variational quantum algorithms, such as EVQE-like approaches, to improve VQC expressivity and trainability.
- Further research into VQC architecture design, including cost-function selection, parameter initialization, and data encoding strategies.
- Investigate repeated data encoding, categorical-feature encoding, and PQC expressiveness for improved classification performance.
- Use coresets and related summarization methods to enable clustering and other ML tasks on NISQ hardware.
- Advance quantum generative models for efficient probability distribution loading to support downstream finance tasks such as derivative pricing.
- Explore additional techniques for preparing continuous distributions and specific families such as normal distributions on quantum hardware.
- Apply quantum RL components, such as quantum LSTMs and variational quantum circuits, to decision-making modules in algorithmic trading.
- Develop direct quantum RL applications for automated trading as hardware improves.
- Investigate quantum RL formulations for market making under partial information and non-Markovian environments.
- Pursue finance-specific implementations where the literature is currently sparse, as suggested in the conclusion.
- [inferred] Validate surveyed methods on real-world financial datasets with rigorous benchmarking against strong classical baselines.
- [inferred] Perform more experiments on real quantum hardware with explicit noise analysis and error-mitigation strategies.
- [inferred] Establish standardized evaluation protocols for quantum ML in finance, including reproducibility, economic metrics, and deployment-relevant constraints.
- [inferred] Assess production feasibility by incorporating transaction costs, latency, interpretability, and regulatory requirements into future studies.
## Key ideas
- #idea:quantum-advantage — Review surveys theoretical speedups from quantum ML subroutines in finance, including HHL-style regression, QSVMs, quantum PCA, clustering, and amplitude-estimation-based Monte Carlo.
- #idea:near-term-feasibility — Argues finance may be an early NISQ beneficiary because many use cases tolerate approximation and can use small-scale prototype components.
- #idea:hybrid-approach — Positions hybrid quantum-classical pipelines as the most realistic route for near-term financial applications, with quantum modules embedded inside broader classical workflows.
- #idea:quantum-advantage — Highlights amplitude estimation as a theoretical quadratic speedup for derivative pricing and potentially risk estimation when probability distributions can be prepared efficiently.
- #idea:hybrid-approach — Discusses quantum annealing and QUBO-based feature selection as plug-in methods for tasks such as credit scoring and related financial ML pipelines.
- #idea:near-term-feasibility — Uses small hardware demonstrations such as nearest-centroid classification on IonQ and other toy-scale experiments as evidence of implementability, while not claiming end-to-end advantage.
- #idea:quantum-advantage — Emphasizes that most claimed gains are conditional on strong assumptions such as QRAM, efficient state preparation, sparse/well-conditioned inputs, and manageable readout costs.
## Contradictions
- The paper surveys strong theoretical quantum speedup claims for regression and linear-algebra-based finance tasks, but simultaneously notes that quantum-inspired classical methods can match some of these gains under similar data-access assumptions, weakening claims of unique quantum superiority.
- The review presents QSVMs and quantum kernels as promising for financial classification, yet also states that practical advantage depends on feature maps being classically hard to simulate and on feasible kernel evaluation, which remains unproven or NISQ-unfriendly.
- The paper highlights asymptotic improvements for quantum PCA, clustering, and related methods, but also stresses that data loading, QRAM assumptions, output extraction, low qubit counts, and noise likely erase these gains in realistic financial settings.
- The review suggests quantum RL and quantum NLP could help algorithmic trading, market making, and financial text analysis, while also acknowledging that current hardware and problem assumptions are too restrictive for realistic deployment, contradicting scalability optimism.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
