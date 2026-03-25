---
aliases:
- A Systematic Literature Review of Classical and Quantum Machine Learning Approaches
  for Mutual Fund Portfolio Optimization
- Systematic Literature Review Classical
authors:
- Lydia Fernandes
- Mugdha Kulkarni
- Mandaar B. Pande
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/PUNECON58714.2023.10450063
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2023 IEEE Pune Section International Conference (PuneCon)
methodology_tags:
- QAOA
- VQE
- quantum-annealing
- HHL
- QUBO
- variational
- grover
- quantum-walk
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-25T16:00:06.721410'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:10.780817'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:00:20.732717'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:00:46.864935'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:01:19.760889'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:01:42.386156'
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
- method/quantum-annealing
- method/HHL
- method/QUBO
- method/variational
- method/grover
- method/quantum-walk
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A Systematic Literature Review of Classical and Quantum Machine Learning Approaches
  for Mutual Fund Portfolio Optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2023
zotero_key: ''
---

## Abstract summary
The paper presents a systematic literature review of classical and quantum machine learning methods applied to mutual fund portfolio optimization, with a focus on equity-based mutual funds. It surveys 44 papers from 2003 to 2023, characterizing problem types, algorithmic approaches (including quantum annealing and QUBO formulations), benchmarks, and identified research gaps. The authors highlight the limitations of classical ML for NP-hard portfolio problems and discuss how emerging quantum machine learning techniques, particularly on NISQ devices, may address these challenges and open directions for future work.
## Methodology
This paper is a systematic literature review that explicitly states it follows the PRISMA methodology to survey classical and quantum machine learning approaches for mutual fund portfolio optimization. The authors searched literature from approximately the past 20 years using Scopus as a major source, along with arXiv.org, SSRN, and other academic search engines, and drew from journals such as Nature, Quantum Journal, Physical Review Research, and Quantum Information Processing. The review scope was intentionally narrowed to mutual funds and their equity-market drivers because portfolio optimization is a broad topic; however, the authors note that the search often returned stock-based studies rather than mutual-fund-specific studies, which they identify as a literature gap. The paper reports analyzing 44 papers from 2003 to 2023 in the abstract, while the body also mentions a broader survey corpus of 87 papers, suggesting a two-level screening or descriptive inconsistency. Inclusion emphasized works focused on mutual funds or equities, particularly studies involving machine learning or quantum machine learning, and the paper notes that exceptions were made for two milestone papers with more than 400 citations. The synthesis is narrative and classificatory rather than meta-analytic: the authors organize the literature by classical versus quantum machine learning approaches, summarize problem types in mutual fund portfolio optimization, identify commonly used benchmarks and evaluation criteria, chart publication trends, and extract research gaps. They also provide a taxonomy of portfolio optimization problem types and a critical analysis table of selected milestone papers.

**Algorithms used:** QAOA, VQE, Grover's algorithm, HHL, NISQ-HHL, Reverse Quantum Annealing, Quantum Annealing, QUBO, Quantum Walk Optimization Algorithm, Quantum Circuit Born Machine, Restricted Boltzmann Machine, Simulated Annealing, Genetic Algorithm, Multilayer Perceptron, Random Forest, Decision Tree, LSTM, SVM, Gaussian Process Regression, Deep Reinforcement Learning, Fuzzy Goal Programming, Neural Network Predictive Modeling
**Frameworks:** PRISMA, Scopus, arXiv, SSRN, IBM-Q, D-Wave

**Dataset:** No primary dataset was used because this is a review article. The review covers prior studies on mutual funds, equities, stocks, ETFs, fund-of-funds, and related portfolio optimization applications published between 2003 and 2023.
## Findings
- [supported] The review identifies portfolio optimization for mutual funds as a central NP-hard/combinatorial finance problem and synthesizes classical and quantum machine learning approaches applied to it.
- [supported] The authors state that the literature search examined 44 papers from 2003 to 2023 for the review scope, while also reporting a broader survey corpus of 87 papers, indicating some inconsistency in corpus reporting.
- [supported] The review finds that most relevant papers use stocks or equities rather than actual mutual fund datasets, and identifies this as a major gap in the literature on mutual fund portfolio optimization.
- [supported] The review reports that quantum machine learning is a developing field, with approximately 67.81% of the collected papers published between 2019 and 2023.
- [supported] Among machine-learning applications in quantitative finance, the review highlights return forecasting, portfolio design, and risk modeling as the most common use cases in the surveyed literature.
- [supported] For portfolio construction, multilayer perceptrons are identified as the most commonly used classical ML technique in the reviewed papers, followed by random forests/decision trees, LSTM, SVM, and Gaussian process regression.
- [supported] The review concludes that classical ML approaches for portfolio optimization face limitations including long training/simulation times, high computational cost, curse of dimensionality, and difficulty handling discrete constraints.
- [supported] The review identifies hybrid quantum-classical methods as the dominant near-term approach for portfolio optimization because current quantum hardware lacks enough high-quality qubits for fully quantum large-scale optimization.
- [supported] Quantum annealing and QUBO formulations are presented in the reviewed literature as the main practical quantum approaches for NP-hard portfolio optimization problems.
- [supported] The review notes that benchmark classical comparators used in prominent quantum portfolio optimization papers include genetic algorithms, simulated annealing, Gekko, and exhaustive solvers.
- [supported] The review highlights research gaps including limited NISQ performance, difficulty validating noisy quantum outputs, constraints on applying quantum linear algebra methods, and unresolved issues in error correction, coherence time, and qubit stability.
- [supported] The review finds that the specific application of quantum machine learning to mutual fund portfolio optimization remains underexplored despite perceived potential.
- [speculative] The paper argues that quantum computing could enable faster and potentially better portfolio optimization than existing supercomputers for high-return, low-risk investment allocation.
- [speculative] The paper claims that NISQ devices can perform some calculations better than classical supercomputers, though results may be noisy or inexact.
- [speculative] The review suggests that quantum-assisted ML could provide real-time solutions for dynamic investment decisions and complex market scenarios in mutual fund portfolio optimization.
- [speculative] The paper suggests that quantum machine learning will become crucial for optimization problems as quantum technology advances.
- [speculative] The review suggests that real advantages in solution quality, computing speed, or both may emerge for specific financial use cases.
- [disputed] The paper states that no dynamic portfolio optimization framework can outperform the covariance model, but this is presented as a cited literature position rather than a settled consensus across all reviewed work.

**Results summary:** This review surveys classical and quantum machine learning literature relevant to mutual fund portfolio optimization and finds that the area is still emerging, especially on the quantum side. The authors emphasize that portfolio optimization is widely treated as an NP-hard or combinatorial problem, with classical ML methods commonly used for forecasting, portfolio construction, and risk modeling but limited by dimensionality, computational cost, and discrete constraints. Across the reviewed quantum literature, hybrid quantum-classical approaches, especially quantum annealing and QUBO-based formulations, are the most prominent practical methods, typically benchmarked against genetic algorithms, simulated annealing, and other classical optimizers. A major conclusion is that actual mutual fund-focused quantum studies are scarce, with most work relying on stock or equity datasets instead. The review identifies broad optimism about quantum computing's future role in finance, but also notes substantial barriers including NISQ noise, validation difficulty, limited qubit quality, and unresolved hardware constraints, so any strong advantage for mutual fund portfolio optimization remains prospective rather than demonstrated by this review itself.

**Performance claims:**
- Approximately 67.81% of the collected papers were published between 2019 and 2023
- The review states it examined 44 papers from 2003 to 2023
- The paper also reports a broader survey corpus of 87 papers
- NISQ devices are described as being in the 50-1000 qubit range
## Quantum advantage claim
**Classification:** speculative

As a review article, the paper expresses optimism that quantum computing may deliver faster or higher-quality portfolio optimization and real-time financial decision support, but it does not itself demonstrate quantum advantage. The discussion emphasizes early experiments, hybrid methods, and hardware limitations, so advantage claims remain prospective rather than empirically established in this paper.
## Limitations
- The review explicitly limits its scope to mutual funds and their driver, the equity markets, excluding broader portfolio optimization settings and other financial instruments.
- The search yielded mostly papers using stocks/equities rather than mutual fund data, indicating a sparse evidence base specifically for mutual fund portfolio optimization.
- The surveyed quantum literature is concentrated in a recent period (approximately 67.81% from 2019 to 2023), so the field is still immature and conclusions may be preliminary.
- Current NISQ technology has limited performance, making it difficult to validate quantum computer outputs and reducing confidence in near-term practical results.
- Quantum linear-algebra techniques may not be applicable to all financial use cases because of prerequisites and constraint-accommodation issues, which can bottleneck quantum speedups.
- Machine learning and deep learning approaches for dynamic portfolio optimization still suffer from the curse of dimensionality and have not clearly improved sample-based portfolio performance.
- No dynamic portfolio optimization framework was found to outperform the covariance model, limiting claims of superiority for newer ML/DL methods.
- Portfolio optimization remains computationally complex due to frequent rebalancing under market fluctuations.
- Key quantum hardware challenges remain unresolved, including error correction, coherence time, and qubit stability.
- Most current quantum portfolio optimization implementations are hybrid classical-quantum methods because quantum computers do not yet have enough functional qubits for standalone effective portfolio optimization.
- The paper notes that specific applications of QML to mutual fund portfolio optimization have not received enough attention so far, limiting domain-specific evidence.
- [inferred] The review does not clearly report full systematic-review details such as explicit inclusion/exclusion criteria, screening counts consistency, or quality assessment of included studies, which may affect reproducibility.
- [inferred] Search coverage may be incomplete because the databases and search engines are described broadly ('Scopus, arXiv.org, and other academic search engines') without a fully specified search string or protocol.
- [inferred] The inclusion of arXiv and SSRN sources means part of the evidence base may be non-peer-reviewed, which can weaken the reliability of synthesized conclusions.
- [inferred] There may be language and publication bias, as no multilingual search strategy or grey-literature protocol is described.
- [inferred] The review appears to emphasize highly cited and milestone papers in parts of the discussion, which may bias interpretation toward influential rather than methodologically strongest studies.
- [inferred] Because many cited studies use stocks, ETFs, or fund-of-funds rather than actual mutual fund datasets, the transferability of conclusions to mutual fund portfolio optimization is uncertain.
## Open questions
- Can quantum machine learning deliver real advantages in solution quality, computing speed, or both for specific mutual fund portfolio optimization use cases?
- How can quantum computer outputs be reliably validated given the limited performance of NISQ devices?
- Which financial portfolio optimization problems can genuinely benefit from quantum linear-algebra methods, and where do their prerequisites make them unsuitable?
- Will QML methods outperform strong classical baselines such as covariance-based models in dynamic portfolio management?
- How can discrete constraints in mutual fund portfolio optimization be incorporated effectively at scale on quantum hardware?
- What level of gate accuracy, coherence, and qubit stability is required before quantum methods become practically useful in finance?
- To what extent can hybrid classical-quantum methods scale as portfolio size, constraints, and market dynamics increase?
- How well do promising early quantum portfolio optimization results generalize from stocks and ETFs to real mutual fund datasets?
- Which quantum approaches among annealing, QAOA, quantum walks, and other methods are best suited for different portfolio optimization formulations?
- Can quantum methods avoid local optima more effectively than classical algorithms in realistic mutual fund optimization settings?

**Future work:**
- Conduct more research specifically on QML applications for mutual fund portfolio optimization, as this area remains underexplored.
- Develop more effective methods to improve quantum gate accuracy for future implementations.
- Address core hardware barriers such as error correction, coherence time, and qubit stability to maximize quantum computing utility in finance.
- Further investigate hybrid classical-quantum approaches, which appear to be the most fruitful near-term path.
- Explore QAOA and related quantum optimization techniques for portfolio optimization problems with large parameter spaces.
- Perform more real-world comparisons of classical and quantum models on practical financial datasets.
- Study the expressive power and efficacy of classical versus quantum models on real-world data as part of the transition to a quantum-ready future.
- Strengthen collaboration between quantum researchers and financial experts to develop finance-relevant quantum solutions.
- Investigate quantum approaches for dynamic investment decision-making and real-time portfolio optimization under changing market conditions.
- [inferred] Expand future reviews to include clearer systematic-review protocols, broader database coverage, and explicit quality appraisal of included studies.
- [inferred] Build benchmark datasets and evaluation standards using actual mutual fund data rather than relying primarily on stock-based proxies.
- [inferred] Compare quantum methods against state-of-the-art classical optimization and machine learning baselines under consistent experimental settings.
## Key ideas
- #idea:near-term-feasibility — The review identifies hybrid quantum-classical methods as the dominant practical path for portfolio optimization under NISQ constraints.
- #idea:hybrid-approach — Quantum annealing and QUBO formulations are presented as the main near-term quantum approaches for NP-hard portfolio optimization problems.
- #idea:quantum-advantage — The paper argues that quantum methods may eventually provide faster or better portfolio optimization, but treats this as prospective rather than demonstrated.
- #idea:near-term-feasibility — Most surveyed quantum finance work is recent and immature, with practical studies concentrated on small-scale or early-stage implementations.
- #idea:hybrid-approach — Classical optimization and preprocessing remain necessary for tuning quantum methods and handling current hardware limitations.
- #idea:quantum-advantage — The review frames portfolio optimization as a combinatorial problem where quantum approaches are especially promising relative to classical ML limitations.
## Contradictions
- The paper expresses optimism that quantum algorithms may outperform classical methods in portfolio optimization, but simultaneously concludes that current NISQ noise, validation difficulty, and hardware immaturity prevent any demonstrated superiority in practice.
- The paper suggests quantum methods could support dynamic or real-time portfolio optimization, yet also states that current qubit limitations, unresolved error correction, coherence constraints, and scaling issues make real-world deployment unproven.
- The review highlights quantum promise for mutual fund portfolio optimization, but also notes that most evidence comes from stock or equity proxy datasets rather than actual mutual fund data, weakening the basis for domain-specific advantage claims.
- The paper discusses newer ML and quantum approaches as promising, while also citing literature that no dynamic portfolio optimization framework outperforms the covariance model, creating tension with stronger innovation-driven performance narratives.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
