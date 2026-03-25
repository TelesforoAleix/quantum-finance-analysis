---
aliases:
- A Technical Review of Quantum Computing Use-Cases for Finance and Economics
- Technical Review Quantum Computing
authors:
- Manqoba Q. Hlatshwayo
- Manav Babel
- Dalila Islas-Sanchez
- Konstantinos Georgopoulos
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.20944/preprints202511.1802.v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Preprints.org
methodology_tags:
- QAOA
- VQE
- quantum-annealing
- HHL
- quantum-ML
- quantum-SVM
- amplitude-estimation
- QUBO
- variational
- grover
- quantum-walk
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:09:34.746084'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:09:45.110678'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:09:59.810879'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:10:56.020388'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:12:04.371245'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:12:16.757719'
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
- topic/derivatives-pricing
- topic/fraud-detection
- topic/credit-scoring
- topic/asset-pricing
- topic/quantum-cryptography
- topic/market-simulation
- method/QAOA
- method/VQE
- method/quantum-annealing
- method/HHL
- method/quantum-ML
- method/quantum-SVM
- method/amplitude-estimation
- method/QUBO
- method/variational
- method/grover
- method/quantum-walk
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A Technical Review of Quantum Computing Use-Cases for Finance and Economics
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
- fraud-detection
- credit-scoring
- asset-pricing
- quantum-cryptography
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper surveys how quantum computing could be applied to problems in finance and economics, targeting both algorithm developers and domain practitioners. It first reviews core quantum algorithms—covering simulation, optimisation, machine learning, and cryptography—and then maps them to concrete use-cases such as option pricing, portfolio optimisation, risk management, fraud detection, and macroeconomic modelling. The authors also discuss technical bottlenecks on the path to practical quantum advantage and outline how interdisciplinary work and better benchmarking could accelerate real-world adoption in financial services.
## Methodology
This source is a preprint and, based on its content, is a non-empirical technical review article rather than an experimental study. The methodology is a narrative technical review and mapping exercise focused on quantum computing use-cases in finance and economics. The authors explicitly divide the work into two main methodological components: (i) a survey of state-of-the-art quantum algorithms relevant to finance and economics, grouped into simulation, optimisation, quantum machine learning, and cryptography; and (ii) a mapping of financial and economic use-cases to those algorithmic families, with mathematical formulations of the use-cases and discussion of proof-of-concept implementations from the literature. The paper also includes a discussion of technical challenges on the path to practical quantum advantage. The review is structured by problem domain and use-case category rather than by a formal systematic review protocol. It presents selected, not exhaustive, use-cases and algorithms, and explicitly states that it is not a comprehensive review nor a primer. No formal search strategy, inclusion/exclusion criteria, synthesis protocol, or meta-analytic procedure is described in the provided text.
## Findings
- [speculative] The paper presents a broad technical review mapping quantum algorithm classes (simulation, optimization, machine learning, cryptography) to finance and economics use-cases including asset pricing, derivatives pricing, portfolio optimization, risk analysis, fraud detection, credit scoring, settlement optimization, and macroeconomic forecasting.
- [speculative] Quantum Monte Carlo Integration is claimed to offer a quadratic speedup over classical Monte Carlo for expectation estimation tasks relevant to finance, with error scaling O(1/Nq) versus classical O(1/sqrt(Np)).
- [speculative] Quantum linear system solvers are claimed to offer potential exponential speedups in system dimension for sparse, well-conditioned linear systems arising from PDE discretizations in finance, subject to strong assumptions on sparsity, conditioning, data access, and output requirements.
- [speculative] Practical quantum advantage in finance and economics has not yet been demonstrated, and the paper emphasizes major bottlenecks including data loading, readout, fault tolerance, circuit depth, and hardware scale.
- [speculative] For derivative pricing, the review argues that quantum methods based on amplitude estimation, Hamiltonian simulation, and quantum PDE solvers could improve computational efficiency for option pricing and related products.
- [speculative] For risk management, the review claims that quantum amplitude estimation can potentially accelerate Value-at-Risk, Conditional Value-at-Risk, and economic capital requirement calculations compared with classical Monte Carlo methods.
- [speculative] For portfolio optimization and related combinatorial finance problems, the review argues that QAOA, VQE, quantum annealing, quantum walks, and Grover-style search are promising approaches, but no practical advantage has been established.
- [speculative] Quantum machine learning methods such as QSVMs, quantum kernels, QNNs, QGANs, and quantum clustering are presented as potentially useful for fraud detection, credit scoring, time-series forecasting, and synthetic data generation, but current evidence is limited and benchmarking against classical methods remains inconclusive.
- [speculative] The review states that current benchmarking often shows strong classical baselines still outperforming quantum machine learning methods on small datasets, leaving quantum advantage in these applications unresolved.
- [speculative] Quantum cryptography is identified as a major finance-relevant area because Shor’s algorithm threatens RSA and Diffie-Hellman, motivating migration to post-quantum cryptography and interest in quantum key distribution.
- [speculative] The paper argues that financial institutions should proactively prepare for post-quantum cryptography migration because of harvest-now-decrypt-later risks, even though cryptographically relevant quantum attacks are not yet practical.
- [speculative] Quantum money and quantum assets are presented as longer-term, transformative possibilities for finance and economics, but their adoption is highly uncertain and remains largely theoretical or at proof-of-concept stage.
- [speculative] The authors argue that scaling fault-tolerant quantum hardware, maintaining up-to-date application benchmarks, and developing quantum middleware are key ingredients on the path toward practical quantum advantage in finance.
- [speculative] The review suggests that banking and asset management could be among the earliest financial domains to benefit from quantum technologies, but this is framed as an expectation rather than a demonstrated result.
- [speculative] The paper claims that quantum computing may eventually provide both speed and accuracy benefits in finance, especially for simulation-heavy, optimization-heavy, and machine-learning-heavy workflows.

**Results summary:** This preprint is a technical review rather than an empirical study. It surveys quantum algorithms relevant to finance and economics, including amplitude estimation, quantum linear solvers, variational algorithms, quantum annealing, quantum machine learning, and quantum cryptography, and maps them to use-cases such as option pricing, risk analysis, portfolio optimization, fraud detection, credit scoring, settlement optimization, and macroeconomic forecasting. The paper repeatedly emphasizes that most claimed benefits remain theoretical or proof-of-concept, with no demonstrated practical quantum advantage in financial services. It highlights major barriers including state preparation, data loading, readout, hardware noise, fault-tolerance requirements, and the need for better benchmarking. The review also discusses post-quantum cryptography readiness and speculative future concepts such as quantum money and quantum assets.

**Performance claims:**
- Quantum Monte Carlo Integration error scaling O(1/Nq) versus classical Monte Carlo O(1/sqrt(Np))
- Quantum Phase Estimation scales as O(1/delta) for additive error delta
- Standard QPE success probability at least 4/pi^2 ≈ 40% when 2^n theta is not an integer
- Quantum Amplitude Estimation returns an estimate with probability at least 8/pi^2
- Grover search query complexity O(sqrt(N)) versus classical O(N)
- Discrete-time quantum walk standard deviation sigma_q ~ T versus classical sigma_c ~ sqrt(T)
- Conjugate Gradient complexity O(N s sqrt(kappa) log(1/epsilon)) for sparse positive-definite systems
- HHL complexity reported as O(s^2 kappa^2 / epsilon)
- Improved sparse QLSS methods reported with complexities including O(s kappa polylog(s kappa/epsilon)) and O(kappa log(1/epsilon)) variants
- Dense-matrix QSVE-based QLSS complexity reported as O(sqrt(N) kappa^2 / epsilon)
- Tomography cost for recovering a classical solution vector from a quantum state reported as O(N/epsilon^2) samples
- Oxford Economics projection cited: economy-wide productivity boost up to 8.3% by 2055 in the UK
- Oxford Economics projection cited: each UK worker producing an extra one and a half weeks of output annually by 2055
- Oxford Economics projection cited: quantum computing industry contribution between £5.9 billion and £12.9 billion gross value added to UK GDP by 2055
- McKinsey projection cited: global finance applications of quantum technologies worth $622 billion by 2035
- McKinsey projection cited: banking value about $302 billion and asset management about $80 billion by 2035
- Derivative pricing resource estimate cited: 4.7 x 10^3 logical qubits, 4.5 x 10^7 T-depth, and 2.4 x 10^9 T-count
- Derivative pricing clock-speed requirement cited: about 10^7 T-gate layers per second, corresponding to roughly 50 MHz logical clock rate
- Improved derivative pricing clock-speed requirement cited as 4.5 MHz
- Fault-tolerant QMCI implementations cited as needing support for about 10^10 error-free logical operations
- Classical derivative pricing baseline cited: 4 x 10^4 samples and about 10 seconds for comparable accuracy
- QUS minimum-search success probability at least 1/2 for one run and at least 1 - 1/2^t after t repetitions
- Quantum random number generation experiment cited: over 70,000 certified bits using 56 qubits
- Quantum annealing factorization result cited: factorization of an 80-bit number
- Shor resource estimate cited: about 20 million physical qubits and 8 hours for 2048-bit RSA in one estimate
- Improved Shor resource estimate cited: less than 1 million physical qubits and about a week for 2048-bit RSA
- Quantum optimization benchmark claim cited: QAOA can reach the global optimum in the limit p -> infinity absent noise
- Quantum support vector machine complexity claimed logarithmic in data dimension N and number of data points M under strong assumptions
- Quantum decision tree training complexity cited as O(D sqrt(MN)) versus classical O(DMN) in one proposal
- Incremental quantum decision tree retraining complexity cited as O(D k^2 D N polylog M)
- Quantum tensor PCA claim cited: quartic speedup over classical methods in the spiked tensor model
- Quantum money experiment cited as showing a transaction-time advantage over optimal classical cross-checking protocols over long inter-city distances
## Quantum advantage claim
**Classification:** speculative

Because this is a preprint review article, the paper mainly aggregates theoretical speedups and proof-of-concept demonstrations from prior literature rather than presenting strong new empirical evidence of end-to-end advantage in financial services. The authors explicitly state that practical quantum advantage has not yet been demonstrated and discuss substantial hardware and algorithmic bottlenecks.
## Limitations
- Not peer-reviewed; findings and assessments have not yet undergone formal external validation
- The review is explicitly not comprehensive and only covers a selected subset of quantum algorithms and finance/economics use-cases
- Use-cases were selected based on perceived high impact and existing proof-of-concept activity, which may bias coverage toward more visible topics
- The review presents technical details only for simpler formulations of algorithms and mentions more complex approaches only briefly
- The review is not intended as a primer on quantum computing and assumes reader familiarity with quantum mechanics and related terminology, limiting accessibility
- Current bottlenecks to practical quantum advantage include inefficient data loading into and readout from quantum computers
- Standard Quantum Phase Estimation requires deep circuits and many controlled operations, making it infeasible on current NISQ hardware without error correction
- Quantum Amplitude Estimation in its original form is too resource intensive for near-term devices because it relies on QPE, ancilla qubits, controlled operations, and inverse QFT
- Quantum walk implementations on NISQ devices are limited by noise and decoherence, and scalable walks on large graphs or lattices remain challenging
- HHL-type quantum linear system solvers require strong assumptions such as sparse or efficiently decomposable matrices, small condition number, efficient oracle access, and limited output requirements
- Potential exponential speedups of QLSS can be undermined by the cost of loading data, especially if QRAM is required
- For dense or low-rank problems, dequantized classical algorithms reduce or eliminate claimed quantum advantage in some settings
- Variational quantum algorithms are heuristic and currently lack provable quantum advantage in complexity
- Variational methods are sensitive to ansatz choice and optimizer performance, and can suffer from barren plateaus
- Quantum annealing is mainly suitable for problems that can be reformulated as QUBOs/Ising models, and this reformulation can introduce significant overhead or restrictive constraints
- No demonstration of quantum advantage with QMCI has yet been made due to hardware limitations and algorithmic bottlenecks
- QMCI requires demanding fault-tolerant resources, including high logical clock rates, large code distances, and substantial logical qubit and T-gate budgets
- Efficient state preparation for arbitrary probability distributions remains a major challenge for QMCI and can negate expected speedups
- Quantum arithmetic for payoff/function evaluation can have gate complexity comparable to classical arithmetic
- For finite-difference PDE approaches, practical advantage depends on well-conditioned linear systems and suitable preconditioning
- It remains an active research problem to understand how quantum hardware noise affects the stability and convergence of numerical SDE/PDE solvers
- Training variational quantum algorithms for optimization is NP-hard and can be hindered by barren plateaus
- Quantum optimization has not yet demonstrated large-scale real-world advantage on industrial problems
- Quantum machine learning improvements are often theoretical and not yet demonstrated experimentally at useful scale
- QSVM and related QML methods face practical challenges including efficient data loading, QLSS execution, and NISQ hardware limitations
- QKNN and other distance-based QML methods depend on efficient state preparation and often on QRAM-like assumptions
- QDT speedups are limited by the need for repeated data partitioning, measurement, and re-encoding, and the final trained model is classical
- QKRR and other quantum regression methods may lose practical advantage once all kernel estimation, data access, and readout costs are included
- QNNs face major trainability issues such as barren plateaus, noise sensitivity, and costly gradient estimation
- Quantum clustering and spectral methods often rely on strong assumptions such as QRAM or efficient block-encodings, and large-scale practical advantage remains unproven
- Quantum generative models inherit both quantum hardware limitations and classical training instabilities, including barren plateaus and shot noise
- Quantum dimensionality reduction methods such as QPCA often rely on idealized oracle or QRAM assumptions and can be undermined by data-loading overhead
- Quantum reinforcement learning faces unresolved issues in stable training, state/action encoding, and error amplification in the agent-environment feedback loop
- Shor's algorithm and other cryptanalytic quantum attacks remain impractical today because of very large fault-tolerant resource requirements
- Quantum annealing approaches to factorization currently only work on very small instances and have unknown time complexity
- QKD adoption is constrained by the limited availability of quantum-capable communication infrastructure and by implementation assumptions
- Certified quantum randomness protocols currently have expensive verification costs and limited adversarial models, making them not yet ready for industrial deployment
- Many reviewed quantum finance applications are still at proof-of-concept stage and depend on future hardware scaling to become practical
- [inferred] As a review article, the paper does not report a systematic search protocol, inclusion/exclusion criteria, or reproducible screening methodology
- [inferred] The review does not quantify search coverage, so relevant recent or less prominent literature may have been omitted
- [inferred] Many claims of potential advantage rely on asymptotic complexity rather than end-to-end benchmarks against state-of-the-art classical production systems
- [inferred] The paper largely synthesizes published proposals and proof-of-concepts rather than providing new empirical validation on real financial datasets or production workflows
- [inferred] Several discussed use-cases depend on idealized assumptions such as efficient oracle access, QRAM, or fault-tolerant hardware that are not currently available
- [inferred] There is limited discussion of reproducibility details for the surveyed proof-of-concept studies, such as code availability, exact hardware settings, or standardized benchmark datasets
- [inferred] The review may overrepresent optimistic projections of economic value and practical impact because many cited benefits come from forecasts rather than demonstrated deployments
## Open questions
- What is a viable path toward practical quantum advantage in finance and economics?
- What engineering and algorithmic hurdles must be overcome to achieve practical quantum advantage?
- How can interdisciplinary collaboration accelerate the development and demonstration of quantum advantage in these sectors?
- How can quantum data loading and readout bottlenecks be overcome efficiently enough to preserve end-to-end advantage?
- Can QMCI achieve practical quantum advantage over highly optimized classical Monte Carlo methods in real financial applications?
- What quantum hardware specifications are sufficient for practical advantage in derivative pricing, risk analysis, and related finance tasks?
- Can efficient and broadly applicable state-preparation methods for realistic financial probability distributions be developed?
- How much of the theoretical speedup of QLSS survives once QRAM, data access, and output extraction costs are included?
- For which classes of sparse, dense, or high-rank financial linear systems do quantum linear solvers retain a meaningful advantage over classical and dequantized methods?
- How can barren plateaus be consistently identified and mitigated in practical variational quantum algorithms?
- Do mitigation strategies for barren plateaus reduce the possibility of genuine quantum advantage?
- Which quantum optimization paradigm is most suitable for specific financial problems: annealing, QAOA, VQE, quantum walks, or search-based methods?
- Can quantum machine learning outperform strong classical baselines on realistic, large-scale financial datasets rather than small proof-of-concept tasks?
- Which financial NLP, fraud detection, and credit scoring tasks are most likely to benefit from QML in practice?
- Can quantum reinforcement learning provide practical benefit in finance despite encoding, trainability, and noise challenges?
- Will quantum money and quantum assets become practically adopted, and if so, in what market niches or institutional settings?
- Can public-key quantum money schemes be made both secure and practically implementable?
- How quickly will quantum-safe cryptography and quantum communication infrastructure be adopted across financial services?
- What non-computational factors, such as regulation, business integration, and operational latency, will determine adoption of quantum solutions in finance?
- How should practical quantum advantage be defined and evaluated consistently across finance use-cases?
- Can a standardized, up-to-date benchmark framework be created to compare classical, hybrid, and quantum methods on the same financial problems?
- How do quantum hardware noise and finite resources affect the stability, convergence, and reliability of quantum PDE/SDE solvers for finance?
- Can predicting financial crashes become a near-term quantum application with meaningful practical value?
- [inferred] Which of the many surveyed finance use-cases are genuinely closest to production relevance, as opposed to being theoretically attractive but operationally unrealistic?
- [inferred] How robust are claimed quantum advantages when full workflow costs are included, including preprocessing, data movement, postprocessing, and compliance constraints?
- [inferred] What benchmark datasets and evaluation protocols should the field adopt to make results comparable and reproducible?

**Future work:**
- Stimulate interdisciplinary research to accelerate the development and demonstration of quantum computing advantage for finance and economics
- Extend surveys and technical mappings between finance/economics use-cases and quantum algorithms
- Develop and demonstrate practical quantum advantage for industrial applications in finance and economics
- Explore approximate and low-depth variants of QPE and QAE that are more suitable for near-term hardware
- Investigate alternatives to QPE for eigenvalue and phase estimation that are more feasible on NISQ devices
- Develop improved amplitude amplification and estimation methods with lower circuit depth and better near-term feasibility
- Advance noise-mitigation and reduced-depth implementations of Grover search and related primitives
- Scale quantum walk implementations to larger graphs and improve robustness against decoherence
- Improve QLSS methods, including preconditioning, dense-matrix handling, and more practical data-access models
- Develop better ansatz design, optimizer strategies, and mitigation methods for barren plateaus in VQAs
- Investigate whether MegaQuOp-scale QPUs can enable practical variational quantum advantage
- Improve QUBO/HUBO formulations and embedding methods for annealing and gate-based optimization in finance
- Develop more efficient state-preparation, arithmetic-free, and low-depth methods for QMCI
- Create well-defined frameworks for evaluating practical quantum advantage in finance
- Test quantum algorithms on larger, more realistic financial and economic problems as hardware matures
- Explore hybrid quantum-classical workflows for option pricing, risk analysis, and portfolio optimization
- Further investigate quantum methods for predicting financial crises as a promising near-term application
- Continue research into quantum money and quantum assets as potentially transformative long-term use-cases
- Develop public-key quantum money and related protocols with stronger security and practical verification
- Advance quantum-safe cryptography migration planning and deployment in financial organizations
- Build quantum communication infrastructure to support QKD and related secure financial applications
- Develop certified quantum randomness protocols with lower verification cost and stronger security assumptions
- Create up-to-date application benchmarks and repositories comparing classical, hybrid, and quantum methods on common problems
- Develop quantum middleware with error suppression/mitigation, compilation, heterogeneous orchestration, and application libraries
- Investigate quantum-enhanced computation for institutional algorithmic bond trading
- Explore sampling-based variational quantum schemes for portfolio construction
- Study regulatory considerations of quantum computing applications in financial services
- [inferred] Conduct systematic and reproducible literature reviews with explicit search strategies and inclusion criteria for quantum finance
- [inferred] Benchmark surveyed quantum methods against state-of-the-art classical solvers on standardized real-world financial datasets
- [inferred] Move beyond proof-of-concept studies toward end-to-end demonstrations integrated into realistic financial workflows
## Key ideas
- #idea:quantum-advantage — The review maps major quantum algorithm families to finance use-cases and summarizes theoretical quadratic or exponential speedups for derivatives pricing, risk estimation, optimization, and search.
- #idea:quantum-advantage — Amplitude estimation and related Monte Carlo primitives are presented as especially relevant for option pricing, VaR, and CVaR because of asymptotic sampling advantages over classical Monte Carlo.
- #idea:quantum-advantage — HHL-type linear solvers, quantum simulation, Grover-style search, quantum walks, annealing, and variational methods are identified as candidate tools for PDEs, optimization, and machine-learning-heavy finance workflows.
- #idea:near-term-feasibility — The paper explicitly argues that practical quantum advantage in finance has not yet been demonstrated and that most benefits remain theoretical or proof-of-concept.
- #idea:near-term-feasibility — Near-term applicability is constrained by deep circuits, fault-tolerance requirements, state preparation, readout costs, and limited hardware scale, especially for QPE/QAE-based methods.
- #idea:hybrid-approach — Hybrid quantum-classical workflows are suggested as the most plausible practical path for portfolio optimization, option pricing, and risk analysis while hardware remains limited.
- #idea:hybrid-approach — Better benchmarking, middleware, and interdisciplinary collaboration are framed as necessary to translate algorithmic promise into deployable financial applications.
## Contradictions
- The paper summarizes many theoretical quantum speedups, but simultaneously states that practical quantum advantage in financial services has not yet been demonstrated, contradicting stronger superiority claims sometimes made in optimistic quantum finance literature.
- The review notes that strong classical baselines often outperform current quantum machine learning methods on small datasets, contradicting broad claims that QML already offers superior performance for fraud detection or credit scoring.
- Claims of exponential or major speedups from HHL/QLSS are qualified by sparsity, conditioning, oracle-access, QRAM, and output-readout assumptions; this contradicts unqualified claims that linear-system-based quantum finance methods scale straightforwardly to real production problems.
- For optimization, the paper presents QAOA, VQE, annealing, quantum walks, and Grover variants as promising, but also states that no large-scale real-world advantage has been shown, contradicting narratives that current quantum optimization already scales to industrial portfolio problems.
- For Monte Carlo and derivative pricing, the paper highlights asymptotic advantages from amplitude estimation while also emphasizing fault-tolerant resource demands, state-preparation overhead, and competitive classical baselines, contradicting simple claims of near-term quantum superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
