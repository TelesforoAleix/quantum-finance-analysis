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
- HHL
- quantum-annealing
- grover
- QUBO
- quantum-walk
- quantum-ML
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-19T12:32:40.681979'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:32:44.945774'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T22:01:38.042823'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:33:46.362800'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:34:12.822095'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:34:18.698200'
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
- topic/risk-modelling
- method/QAOA
- method/VQE
- method/HHL
- method/quantum-annealing
- method/grover
- method/QUBO
- method/quantum-walk
- method/quantum-ML
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
- risk-modelling
year: 2023
zotero_key: ''
---

## Abstract summary
This review paper systematically examines classical and quantum machine learning approaches for mutual fund portfolio optimization, analyzing 44 papers published between 2003 and 2023. The authors focus specifically on mutual funds and equity markets, providing an overview of problem types, preferred methodologies, benchmarks, and research gaps to guide future work in quantum computing applications for financial services.
## Methodology
This review article employs a systematic literature review (SLR) approach following the PRISMA methodology to examine classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization. The authors conducted a comprehensive search across academic databases such as Scopus, arXiv.org, and other academic search engines, focusing on papers published between 2003 and 2023. The inclusion criteria prioritized papers addressing mutual funds or equities, particularly those leveraging QML and machine learning (ML) techniques. A total of 44 papers were selected for detailed analysis, with exceptions made for two highly cited milestone papers. The review synthesized findings by categorizing problems in mutual fund portfolio optimization (e.g., asset allocation, diversification, risk management) and comparing classical and quantum approaches. The authors also identified research gaps and trends in the field, such as the dominance of hybrid quantum-classical techniques and the limited application of QML to mutual funds specifically.

**Algorithms used:** Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Harrow-Hassidim-Lloyd (HHL), Quantum Annealing, Quadratic Unconstrained Binary Optimization (QUBO), Quantum Walk Optimization Algorithm, Reverse Quantum Annealing, Genetic Algorithm, Simulated Annealing
## Findings
- [supported] The review analyzes 44 papers from 2003 to 2023 on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO), identifying key trends and gaps in the literature.
- [supported] Approximately 67.81% of the reviewed papers were published between 2019 and 2023, indicating QML as a rapidly developing field in financial services.
- [supported] Quantum algorithms like QAOA and VQE are highlighted as promising tools for solving NP-hard PO problems, though current implementations are limited to NISQ (Noisy Intermediate-Scale Quantum) devices.
- [speculative] Quantum computing could theoretically provide faster solutions for PO by leveraging superposition and entanglement to process large datasets concurrently, but this advantage is not yet empirically validated on real hardware.
- [supported] Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing, reverse quantum annealing) are the most common methods for PO in the reviewed literature, as pure quantum solutions lack sufficient qubits for large-scale problems.
- [supported] Quantum annealers (e.g., D-Wave) and QUBO models are becoming standard for tackling NP-complete/hard problems in PO, with experimental success reported in small-scale implementations.
- [disputed] The review claims that quantum-assisted ML algorithms can provide real-time solutions for dynamic PO, but this is contradicted by limitations in NISQ hardware (e.g., noise, decoherence, and error correction challenges).
- [supported] Classical ML techniques (e.g., multilayer perceptrons, random forests, LSTM) dominate PO construction in the reviewed literature, but face limitations like high computational costs and the curse of dimensionality.
- [speculative] Quantum computing may overcome classical ML constraints in PO by incorporating discrete constraints and macroeconomic factors in real-time, but this remains unproven in practice.
- [supported] Research gaps identified include the lack of studies on mutual funds (vs. stocks), limited validation of quantum outputs due to NISQ limitations, and the need for improved quantum gate accuracy.
- [speculative] The review suggests that QML could eventually outperform classical ML in PO, offering better solution quality and computational speed, but this is contingent on advancements in fault-tolerant quantum computing.

**Results summary:** This systematic literature review synthesizes findings from 44 papers on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO). The review highlights the growing interest in QML, with nearly 68% of papers published since 2019, and identifies quantum algorithms like QAOA and VQE as promising tools for solving NP-hard PO problems. However, current implementations are limited to NISQ devices, which suffer from noise and decoherence, necessitating hybrid quantum-classical approaches. While quantum annealers and QUBO models show experimental success in small-scale PO, the review notes significant research gaps, including the lack of studies on mutual funds (vs. stocks) and the need for improved quantum hardware. Classical ML techniques remain dominant but face challenges like computational inefficiency and dimensionality. The review speculates that QML could eventually surpass classical methods in speed and solution quality, but this remains theoretical until fault-tolerant quantum computing is achieved.

**Performance claims:**
- 67.81% of reviewed papers published between 2019 and 2023
- Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing) used in multiple studies
- Quantum annealers (e.g., D-Wave) applied to PO problems with small-scale success
## Quantum advantage claim
**Classification:** speculative

The review suggests theoretical advantages of quantum computing for PO, such as faster processing of large datasets and real-time solutions, but these claims are not empirically validated. All reported results are from simulations or NISQ devices, which lack fault tolerance and scalability. Quantum advantage remains speculative until demonstrated on real hardware with sufficient qubits and error correction.
## Limitations
- Search coverage limited to 44 papers from 2003 to 2023, which may not capture all relevant literature on quantum machine learning for mutual fund portfolio optimization [inferred]
- Scope restricted to mutual funds and equity markets, excluding other financial instruments like bonds, derivatives, or cryptocurrencies [inferred]
- Significant gap in literature: most papers focus on stocks rather than mutual funds data, limiting the applicability of findings to mutual fund portfolio optimization
- Review relies heavily on sources from Scopus, arXiv, and selected journals, potentially excluding relevant grey literature or industry reports [inferred]
- Language bias: papers primarily in English, excluding non-English research that may offer valuable insights [inferred]
- Recency bias: 67.81% of the papers are from 2019-2023, which may overrepresent recent trends while underrepresenting foundational work [inferred]
- Geographical bias: author affiliations show dominance of USA-based research, potentially overlooking region-specific financial contexts [inferred]
- NISQ-era limitations: current quantum hardware is noisy, lacks error correction, and has limited qubit counts, restricting the practical applicability of quantum algorithms for portfolio optimization
- Hybrid approaches dominate, indicating that purely quantum solutions are not yet feasible for real-world portfolio optimization problems
- Lack of empirical validation for many quantum machine learning approaches, with most studies relying on simulations or small-scale experiments
- Limited benchmarking: classical benchmarks used (e.g., Genetic Algorithm, Simulated Annealing) may not represent state-of-the-art classical methods [inferred]
- Dataset limitations: many studies use synthetic or limited historical data (e.g., 1-year or 5-year spans), which may not capture real-world market dynamics [inferred]
- No discussion on the cost or accessibility of quantum computing resources for financial institutions, which may limit adoption [inferred]
- Potential overreliance on specific quantum hardware (e.g., D-Wave, IBM-Q), which may not generalize to other quantum computing platforms [inferred]
## Open questions
- How can quantum machine learning algorithms be adapted to handle the unique constraints and dynamics of mutual fund portfolio optimization, given the current focus on stock-based data?
- What are the specific prerequisites and constraints that limit the applicability of quantum linear-algebra techniques for financial use cases?
- How can the curse of dimensionality in machine learning approaches for portfolio optimization be mitigated, particularly in dynamic portfolio management?
- What are the most effective ways to achieve higher quantum gate accuracy in NISQ-era devices to improve the reliability of quantum computing outputs?
- How do quantum algorithms perform compared to state-of-the-art classical methods for large-scale mutual fund portfolio optimization problems?
- What is the impact of quantum decoherence and noise on the solution quality of quantum portfolio optimization algorithms?
- How can quantum computing be leveraged to incorporate real-time macroeconomic conditions into portfolio optimization models?
- What are the trade-offs between solution quality, computational speed, and resource requirements when using hybrid quantum-classical approaches for portfolio optimization?
- How can quantum machine learning models be validated and benchmarked against classical models using real-world mutual fund datasets?
- What are the long-term prospects for fault-tolerant quantum computing in financial services, and how will it reshape portfolio optimization practices?

**Future work:**
- Expand research to include other financial instruments beyond mutual funds and equities, such as bonds, derivatives, and cryptocurrencies
- Develop quantum machine learning algorithms specifically tailored for mutual fund portfolio optimization, addressing the current gap in literature
- Conduct empirical studies using real-world mutual fund datasets to validate the performance of quantum algorithms
- Explore the integration of real-time macroeconomic data into quantum portfolio optimization models for dynamic decision-making
- Investigate methods to improve quantum gate accuracy and reduce noise in NISQ-era devices to enhance the reliability of quantum computing outputs
- Benchmark quantum machine learning approaches against state-of-the-art classical methods to identify specific use cases where quantum computing provides a clear advantage
- Develop hybrid quantum-classical frameworks that leverage the strengths of both paradigms for large-scale portfolio optimization
- Address the curse of dimensionality in machine learning approaches for dynamic portfolio management through advanced quantum techniques
- Collaborate with financial experts and quantum researchers to identify and overcome key challenges such as error correction, coherence time, and qubit stability
- Explore the potential of quantum amplitude estimation for speeding up Monte Carlo sampling in financial simulations and risk assessments
- Investigate the scalability of quantum algorithms for portfolio optimization as quantum hardware advances toward fault-tolerant systems
## Key ideas
- #idea:quantum-advantage — Quantum algorithms like QAOA and VQE are highlighted as promising for solving NP-hard portfolio optimization problems, though empirical validation is lacking
- #idea:near-term-feasibility — Hybrid quantum-classical approaches dominate due to NISQ limitations, with experimental success reported on small-scale problems using quantum annealers and QUBO models
- #idea:hybrid-approach — Classical preprocessing and optimization are essential for tuning quantum circuits and reducing qubit requirements in portfolio optimization tasks
- #limitation:noise — NISQ-era hardware limitations (e.g., decoherence, lack of error correction) degrade solution quality, preventing demonstrated quantum advantage
- #limitation:qubit-count — Current qubit counts restrict the scale of portfolio optimization problems, limiting practical applicability to mutual funds
- #limitation:no-empirical-validation — Most quantum claims lack empirical validation on real-world mutual fund datasets, relying instead on simulations or stock-based data
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum algorithms *may* outperform classical methods for portfolio optimization, but this is contradicted by NISQ-era limitations (e.g., noise, decoherence) that prevent such advantages from being realized
- #contradiction:scalability — The paper suggests quantum computing could enable dynamic portfolio optimization, but scalability to real-world problems is unproven due to qubit constraints and computational complexity
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
