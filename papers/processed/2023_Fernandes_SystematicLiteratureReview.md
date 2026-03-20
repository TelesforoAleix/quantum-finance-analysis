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
- quantum-ML
- QUBO
- quantum-walk
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-19T23:29:13.895048'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:29:16.607923'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:29:21.179877'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:30:26.561058'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:30:38.125418'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:30:43.385116'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/QAOA
- method/VQE
- method/quantum-annealing
- method/HHL
- method/quantum-ML
- method/QUBO
- method/quantum-walk
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A Systematic Literature Review of Classical and Quantum Machine Learning Approaches
  for Mutual Fund Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2023
zotero_key: ''
---

## Abstract summary
This review paper systematically examines classical and quantum machine learning approaches for mutual fund portfolio optimization, analyzing 44 papers published between 2003 and 2023. The authors focus on mutual funds within equity markets, comparing traditional and quantum techniques, identifying research gaps, and assessing the potential of quantum computing to address computationally complex optimization problems in financial services.
## Methodology
The paper presents a systematic literature review (SLR) following the PRISMA methodology to examine classical and quantum machine learning approaches for mutual fund portfolio optimization. The review analyzes 44 papers published between 2003 and 2023, sourced from databases such as Scopus, arXiv.org, and academic search engines, including journals like Nature, Quantum Journal, and Physical Review Research. The search strategy focused on papers addressing mutual funds or equities, particularly those leveraging quantum machine learning (QML) and classical machine learning (ML). The review includes a classification of portfolio optimization problems, an analysis of prominent research works, and a synthesis of findings to identify research gaps and trends in the field. The methodology involved defining specific research questions, screening papers based on relevance, and categorizing them by approach, problem type, and geographic distribution of authors.

**Algorithms used:** QAOA, VQE, HHL, Quantum Annealing, QUBO, Quantum Walk Optimization Algorithm, Genetic Algorithm, Simulated Annealing
## Findings
- [supported] The review analyzes 44 papers from 2003 to 2023 on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO), identifying a significant gap in literature focusing on mutual funds rather than stocks
- [supported] Approximately 67.81% of the reviewed papers were published between 2019 and 2023, indicating QML as a rapidly developing field in financial services
- [supported] Quantum algorithms like QAOA and VQE are highlighted as promising tools for solving NP-hard PO problems, though current implementations are limited to NISQ (Noisy Intermediate-Scale Quantum) devices
- [speculative] Quantum computing could provide faster solutions for PO by leveraging superposition and entanglement to process large datasets concurrently, potentially outperforming classical supercomputers
- [speculative] Quantum-assisted ML algorithms may enable real-time dynamic investment decisions for complex market scenarios, particularly in mutual fund PO
- [supported] Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing, reverse quantum annealing on D-Wave) are the most common implementations due to limited qubit counts and noise in NISQ devices
- [supported] Quantum annealers and QUBO models are emerging as de facto standards for solving NP-complete/hard problems in finance, with demonstrated success in small-scale portfolio optimization
- [disputed] The review claims QML overcomes classical ML challenges (e.g., curse of dimensionality, discrete constraints), but notes that no dynamic QML framework has yet outperformed classical covariance models in real-world datasets
- [speculative] Quantum advantage in PO may emerge in specific use cases, offering improvements in solution quality, speed, or both, but this remains unproven at scale
- [supported] Key research gaps include limited qubit stability, coherence time, error correction, and the need for more effective quantum gate accuracy in NISQ devices
- [supported] Most QML implementations for PO rely on hybrid techniques, with classical benchmarks like genetic algorithms, simulated annealing, and Gekko solvers used for evaluation
- [speculative] The HHL algorithm and its NISQ-enhanced versions form the basis for several QML models, but prerequisites and constraints may limit their applicability in finance

**Results summary:** This systematic literature review synthesizes findings from 44 papers on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO). The review highlights the rapid growth of QML research in finance, with nearly 68% of papers published post-2019. While quantum algorithms (e.g., QAOA, VQE) show promise for solving NP-hard PO problems, current implementations are constrained by NISQ device limitations, necessitating hybrid quantum-classical approaches. Quantum annealers and QUBO models are identified as leading methods for tackling combinatorial optimization, with small-scale successes reported. However, the review notes persistent challenges, including qubit instability, decoherence, and the lack of demonstrated quantum advantage over classical methods in real-world datasets. Key gaps include the scarcity of research on mutual funds (vs. stocks) and the need for improved error correction. The consensus is that QML holds theoretical potential for PO, but practical advantages remain speculative until fault-tolerant quantum hardware is available.

**Performance claims:**
- 67.81% of reviewed papers published between 2019 and 2023
- Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing) demonstrated on D-Wave quantum annealers
- Quantum walk optimization algorithm proposed for NISQ devices to find high-quality PO solutions
- QML models (e.g., QCBMs) tested on near-term quantum computers for generative modeling in finance
## Quantum advantage claim
**Classification:** speculative

The review suggests theoretical potential for quantum advantage in portfolio optimization, particularly for solving NP-hard problems faster than classical methods. However, all claims are based on simulations or small-scale NISQ device implementations, with no empirical evidence of advantage on real hardware. Key limitations (e.g., noise, qubit count, error correction) remain unresolved, and hybrid approaches dominate current research.
## Limitations
- Search coverage limited to 44 papers from 2003 to 2023, potentially missing relevant studies outside this range or in non-indexed sources [inferred]
- Scope restricted to mutual funds and equity markets, excluding other financial instruments like bonds, derivatives, or cryptocurrencies [inferred]
- Language bias: Papers primarily sourced from English-language journals and databases (Scopus, arXiv), excluding non-English literature [inferred]
- Grey literature (e.g., industry reports, preprints not on arXiv) excluded from the review [inferred]
- Recency bias: 67.81% of papers published between 2019–2023, potentially underrepresenting earlier foundational work [inferred]
- Focus on quantum machine learning (QML) for mutual fund portfolio optimization (PO) may overlook broader applications of quantum computing in finance
- Limited empirical validation of quantum approaches, as most studies rely on simulations or small-scale quantum hardware (NISQ devices)
- NISQ-era limitations: Current quantum computers are noisy, lack error correction, and have limited qubit counts, restricting practical applicability
- Most reviewed papers use hybrid quantum-classical approaches, which may not fully leverage quantum advantages [inferred]
- Lack of real-world mutual fund datasets in reviewed studies; most use synthetic or equity market data instead
- Benchmarking gaps: Classical benchmarks (e.g., genetic algorithms, simulated annealing) may not be state-of-the-art for all PO problems [inferred]
- Geographical bias: Majority of reviewed papers from the USA, with limited representation from emerging economies
- No discussion of regulatory or ethical constraints in applying quantum computing to financial services [inferred]
## Open questions
- How do quantum algorithms perform for mutual fund PO with more than 50 assets, given current qubit limitations?
- What is the impact of quantum decoherence and noise on the accuracy of QML-based PO solutions?
- Can quantum approaches outperform classical methods for dynamic portfolio rebalancing in real-time market conditions?
- How do hybrid quantum-classical models compare to pure quantum or classical approaches in terms of solution quality and speed?
- What are the computational trade-offs between quantum annealing (e.g., D-Wave) and gate-based quantum computing (e.g., IBM-Q) for PO?
- How can quantum error correction be integrated into QML algorithms to improve reliability for financial applications?
- What are the implications of quantum computing for risk management models (e.g., Value at Risk, stress testing) in mutual funds?
- How do quantum algorithms handle non-convex constraints (e.g., transaction costs, tax efficiency) in PO?
- What are the barriers to adopting quantum computing in financial institutions, beyond hardware limitations (e.g., cost, expertise, regulatory hurdles)?
- Can quantum machine learning identify hidden patterns in mutual fund data that classical ML cannot?

**Future work:**
- Expand the scope of literature reviews to include non-English sources and grey literature for broader coverage
- Develop and test QML algorithms on real-world mutual fund datasets, not just synthetic or equity data
- Compare quantum approaches with state-of-the-art classical methods (e.g., deep reinforcement learning) for PO
- Explore the use of quantum computing for dynamic portfolio optimization and real-time rebalancing
- Investigate the scalability of quantum algorithms for large-scale PO problems (e.g., 100+ assets)
- Develop noise mitigation techniques tailored for QML in financial applications
- Assess the feasibility of quantum error correction for fault-tolerant quantum computing in finance
- Study the integration of quantum computing with other emerging technologies (e.g., blockchain, AI) for financial services
- Conduct empirical studies on the cost-benefit analysis of quantum computing adoption in financial institutions
- Address regulatory and ethical challenges in deploying quantum computing for mutual fund PO
- Explore quantum algorithms for other financial problems (e.g., liquidity management, benchmark tracking) in mutual funds
## Key ideas
- #idea:quantum-advantage — Quantum algorithms (QAOA, VQE) are highlighted as promising for solving NP-hard portfolio optimization problems, though empirical validation on real-world datasets is lacking
- #idea:near-term-feasibility — Hybrid quantum-classical approaches dominate due to NISQ limitations, with experimental success reported on small-scale problems using quantum annealers and QUBO models
- #idea:hybrid-approach — Classical preprocessing and optimization are essential for tuning quantum circuits and reducing qubit requirements in portfolio optimization tasks
- #limitation:noise — NISQ-era hardware limitations (e.g., decoherence, lack of error correction) degrade solution quality, preventing demonstrated quantum advantage
- #limitation:qubit-count — Current qubit counts restrict the scale of portfolio optimization problems, limiting practical applicability to mutual funds
- #limitation:no-empirical-validation — Most quantum claims lack empirical validation on real-world mutual fund datasets, relying instead on simulations or stock-based data
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum algorithms *may* outperform classical methods for portfolio optimization, but this is contradicted by NISQ-era limitations (e.g., noise, decoherence) that prevent such advantages from being realized in practice
- #contradiction:scalability — The paper suggests quantum computing could enable dynamic portfolio optimization, but scalability to real-world problems is unproven due to qubit constraints and computational complexity
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
