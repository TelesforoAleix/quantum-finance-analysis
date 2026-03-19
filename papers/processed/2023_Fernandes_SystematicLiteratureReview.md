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
- grover
- quantum-walk
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:40:02.270953'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:41:00.807998'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:41:07.482910'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:41:17.827531'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:41:32.462279'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:41:38.205434'
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
- method/quantum-annealing
- method/HHL
- method/QUBO
- method/grover
- method/quantum-walk
- method/quantum-ML
- method/variational
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
This paper conducts a systematic literature review of classical and quantum machine learning approaches applied to mutual fund portfolio optimization. It analyzes 44 papers published between 2003 and 2023, focusing on equity markets and mutual funds to identify key problems, preferred methods, benchmarks, and research gaps. The review aims to provide a comprehensive survey for researchers and practitioners exploring quantum computing's potential in financial optimization.
## Methodology
This paper presents a systematic literature review (SLR) following the PRISMA methodology to analyze classical and quantum machine learning approaches for mutual fund portfolio optimization. The review examines 44 papers published between 2003 and 2023, sourced from databases such as Scopus, arXiv.org, and academic journals like Nature and Quantum Journal. The focus is on mutual funds and equity markets, addressing research questions about prominent works in quantum and classical machine learning for NP-hard portfolio optimization tasks and identifying critical research gaps. The methodology includes a structured search strategy, inclusion of milestone papers, and a synthesis of findings from both classical (e.g., genetic algorithms, neural networks) and quantum (e.g., QAOA, quantum annealing) approaches. The review highlights trends, benchmarks, and comparative evaluations of quantum and classical methods, particularly in the NISQ era.

**Algorithms used:** Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Harrow-Hassidim-Lloyd (HHL), NISQ-HHL, Quantum Walk Optimization Algorithm, Grover’s algorithm, Reverse Quantum Annealing, Quadratic Unconstrained Binary Optimization (QUBO), Genetic Algorithm, Simulated Annealing
**Frameworks:** D-Wave Quantum Annealer, IBM-Q, Ion-trap Quantum Computers

**Experimental setup:** The reviewed studies employ a mix of quantum hardware and simulators, including D-Wave Quantum Annealers, IBM-Q systems, and Ion-trap Quantum Computers. Classical counterparts for benchmarking include genetic algorithms, simulated annealing, and optimization solvers like Gekko. Hybrid approaches combining classical and quantum computing are prevalent, reflecting the limitations of current NISQ devices.

**Dataset:** The datasets used in the reviewed papers include mutual fund data, equity market data, Fund of Funds (1-year span), ETFs and stocks (5-year adjusted closing prices), and indices like the S&P 500. Specific metrics such as variance, Treynor Index, Sharpe Ratio, standard deviation, turnover rate, and covariance were employed for evaluation.
## Findings
- [supported] The systematic literature review analyzed 44 papers from 2003 to 2023 on classical and quantum machine learning approaches for mutual fund portfolio optimization, identifying a significant gap in literature focusing specifically on mutual funds rather than stocks
- [supported] Approximately 67.81% of the reviewed papers were published between 2019 and 2023, indicating that quantum machine learning (QML) for portfolio optimization is a rapidly developing field
- [supported] Classical machine learning techniques such as Multilayer Perceptron, Random Forests, and Decision Trees are popular for portfolio construction, but face challenges like high computational time and the curse of dimensionality
- [supported] Quantum-assisted machine learning algorithms (e.g., QAOA, VQE, Quantum Annealing) show potential for real-time solutions to complex market scenarios in mutual fund portfolio optimization, though most implementations are hybrid (quantum-classical) approaches
- [supported] Quantum annealers and QUBO models are becoming standard for solving NP-complete and NP-hard problems in portfolio optimization, with experimental success reported on D-Wave and IBM-Q hardware
- [speculative] Quantum computing may provide faster solutions for portfolio optimization by efficiently searching combinations and managing risk in a fraction of the time compared to classical methods
- [speculative] Quantum advantage in portfolio optimization is expected to emerge as quantum technology advances, particularly for dynamic investment decisions and real-time macroeconomic condition analysis
- [disputed] The paper claims that quantum algorithms can outperform classical supercomputers for portfolio optimization, but this is contradicted by the NISQ-era limitations (e.g., noise, decoherence, and lack of error correction) noted in the review
- [speculative] The authors suggest that quantum machine learning could overcome classical ML challenges, such as incorporating discrete constraints and avoiding local optima in mutual fund portfolio optimization
- [supported] Research gaps identified include limited validation of quantum outputs due to NISQ limitations, bottlenecks in quantum linear-algebra techniques for financial use cases, and insufficient attention to mutual fund-specific portfolio optimization problems

**Results summary:** This conference paper presents a systematic literature review of classical and quantum machine learning approaches for mutual fund portfolio optimization. The review highlights a growing interest in QML, with a majority of recent papers published post-2019. Classical ML techniques dominate current applications but struggle with computational complexity and dimensionality. Quantum approaches, particularly hybrid models like QAOA and quantum annealing, show promise for solving NP-hard problems, though most results are from simulations or small-scale experiments on NISQ devices. The paper identifies key research gaps, including the lack of mutual fund-specific studies and the limitations of NISQ-era hardware, while speculating on the potential for quantum advantage in dynamic portfolio management.

**Performance claims:**
- 67.81% of reviewed papers published between 2019 and 2023
- Quantum annealers and QUBO models used for portfolio optimization on D-Wave hardware
- Hybrid quantum-classical approaches (e.g., QAOA) demonstrated for portfolio optimization problems
## Quantum advantage claim
**Classification:** speculative

The paper suggests theoretical and experimental potential for quantum advantage in portfolio optimization, particularly for dynamic and real-time solutions. However, all claims are based on simulations or small-scale NISQ-era hardware implementations, with no demonstrated advantage on real-world, large-scale problems. The review also notes significant limitations (e.g., noise, decoherence) that currently prevent quantum advantage from being realized.
## Limitations
- Review limited to mutual funds and equity markets, excluding other financial instruments like bonds, derivatives, or cryptocurrencies [inferred]
- Search yielded primarily papers focusing on stocks rather than mutual funds, indicating a significant gap in mutual fund-specific literature
- Page-limit constraints of the conference paper may have restricted the depth of analysis for some research gaps [inferred]
- NISQ-era quantum computers are noisy, susceptible to quantum decoherence, and lack continuous quantum error correction, limiting their practical applicability
- Most quantum machine learning (QML) implementations for portfolio optimization use hybrid techniques, relying on classical computing for significant portions of the algorithm
- Limited qubit count in current quantum hardware restricts the scale of portfolio optimization problems that can be addressed
- Quantum algorithms like HHL and QAOA have prerequisites and constraints that may not always align with real-world financial use cases, potentially limiting quantum speedups
- Lack of empirical validation for many theoretical quantum approaches in real-world mutual fund portfolio optimization scenarios
- Classical benchmarks (e.g., Genetic Algorithm, Simulated Annealing) used for QML models may not fully capture the advantages of quantum approaches [inferred]
- High computational complexity of dynamic portfolio rebalancing in response to market fluctuations remains unresolved in both classical and quantum approaches
- Curse of dimensionality and inability of deep learning architectures to improve performance of sample-based portfolios in classical ML approaches
- Limited discussion on the impact of quantum noise and error rates on the quality of portfolio optimization solutions [inferred]
- Most reviewed papers focus on developed economies (e.g., USA), with limited representation from emerging markets [inferred]
- No clear consensus on the most effective quantum algorithm for mutual fund portfolio optimization, with multiple approaches (QAOA, VQE, quantum annealing) being explored
## Open questions
- How can quantum computing effectively address the discrete constraints inherent in mutual fund portfolio optimization problems?
- What are the most effective ways to achieve higher quantum gate accuracy for financial applications in the NISQ era?
- How do quantum linear-algebra techniques compare to classical methods for specific financial use cases, and what are their limitations?
- Can dynamic portfolio optimization frameworks using QML outperform classical covariance models in real-world scenarios?
- What is the impact of quantum decoherence and noise on the solution quality of portfolio optimization algorithms?
- How can quantum computing overcome the curse of dimensionality in high-dimensional portfolio optimization problems?
- What are the most suitable quantum benchmarks for evaluating QML models in portfolio optimization?
- How can quantum algorithms be adapted to handle real-time market fluctuations and dynamic portfolio rebalancing?
- What is the scalability potential of quantum approaches for large-scale mutual fund portfolio optimization?
- How do hybrid quantum-classical approaches compare to pure quantum or classical methods in terms of performance and practicality?
- What are the specific advantages of quantum computing for mutual fund portfolio optimization compared to classical methods?

**Future work:**
- Further research on quantum machine learning applications specifically tailored for mutual fund portfolio optimization
- Development of more effective quantum error correction and noise mitigation techniques for financial applications
- Empirical validation of quantum approaches on real-world mutual fund datasets, beyond synthetic or stock-based data
- Exploration of quantum algorithms that can handle dynamic portfolio rebalancing in response to market fluctuations
- Investigation of quantum speedups for specific financial use cases, particularly those involving high-dimensional data
- Comparison of different quantum approaches (QAOA, VQE, quantum annealing) for mutual fund portfolio optimization to identify the most effective methods
- Development of quantum benchmarks that better reflect the complexities of real-world portfolio optimization problems
- Research on hybrid quantum-classical approaches to leverage the strengths of both paradigms for portfolio optimization
- Expansion of research to include emerging markets and diverse financial instruments beyond mutual funds and equities
- Longitudinal studies to assess the long-term performance of quantum-based portfolio optimization strategies
- Collaboration between quantum researchers and financial experts to develop domain-specific quantum solutions for finance
## Key ideas
- #idea:quantum-advantage — Quantum-assisted algorithms (e.g., QAOA, VQE) show potential for real-time solutions to NP-hard portfolio optimization problems, though advantages remain speculative in the NISQ era
- #idea:near-term-feasibility — Hybrid quantum-classical approaches are prevalent due to NISQ limitations, with quantum annealers and QUBO models demonstrating experimental success on small-scale problems
- #idea:hybrid-approach — Classical preprocessing and optimization are critical for tuning quantum circuit parameters, reducing qubit requirements, and mitigating noise in portfolio optimization tasks
- #limitation:noise — NISQ-era hardware limitations (e.g., decoherence, lack of error correction) degrade solution quality, preventing demonstrated quantum advantage for large-scale problems
- #limitation:qubit-count — Current qubit counts restrict the scale of portfolio optimization problems that can be addressed, limiting practical applicability to mutual funds
- #limitation:no-empirical-validation — Most quantum claims lack empirical validation on real-world mutual fund datasets, relying instead on simulations or stock-based data
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum algorithms *may* outperform classical supercomputers for portfolio optimization, but this is contradicted by NISQ-era limitations (e.g., noise, decoherence) noted in the same review, which prevent such advantages from being realized
- #contradiction:scalability — While the paper highlights quantum potential for dynamic portfolio optimization, it acknowledges that scalability to real-world problems is unproven due to qubit constraints and high computational complexity in both classical and quantum approaches
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
