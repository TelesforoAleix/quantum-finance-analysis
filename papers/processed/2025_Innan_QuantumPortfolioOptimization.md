---
aliases:
- Quantum Portfolio Optimization with Expert Analysis Evaluation
- Quantum Portfolio Optimization Expert
authors:
- Nouhaila Innan
- Ayesha Saleem
- Alberto Marchisio
- Muhammad Shafique
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/QCE65121.2025.10344
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- VQE
- QAOA
- variational
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T22:47:32.646773'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:47:35.733340'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:47:42.336422'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:47:53.766565'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:48:01.984938'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:48:17.400286'
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
- method/VQE
- method/QAOA
- method/variational
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Portfolio Optimization with Expert Analysis Evaluation
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper benchmarks two variational quantum algorithms—Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA)—for portfolio optimization in finance. The study evaluates their performance across different asset universes, circuit architectures, and depths, while identifying a gap between algorithmic optimization and real-world financial viability. To address this, the authors introduce an Expert Analysis Evaluation framework, integrating human financial expertise to assess the economic soundness and practical feasibility of quantum-generated portfolios.
## Methodology
The paper presents a hybrid quantum-classical methodology for portfolio optimization, combining QUBO-based quantum optimization with expert-driven financial evaluation. The process begins with formulating the portfolio selection problem as a QUBO instance, where the objective is to minimize risk and maximize return under constraints. This QUBO problem is then mapped to a Hamiltonian and solved using two variational quantum algorithms: QAOA and SamplingVQE. The study systematically benchmarks these algorithms across different asset universes (4 and 10 assets), ansatz architectures (TwoLocal, EfficientSU2, PauliTwoDesign, RealAmplitudes), and circuit depths (2, 4, 6, 8, 10). Optimization performance is evaluated based on convergence behavior, cost function minimization, and stability. To address the gap between algorithmic performance and financial practicality, an Expert Analysis Framework is introduced, where financial professionals assess the economic soundness, diversification, and market feasibility of the quantum-optimized portfolios. The methodology integrates historical financial data from Yahoo Finance (December 2024 to May 2025) and tests portfolio performance on future data (June 2025).

**Algorithms used:** QAOA, VQE, SamplingVQE
**Frameworks:** Qiskit, Qiskit Finance, Qiskit Aer

**Experimental setup:** Experiments are conducted using the QASM simulator with 4 and 10 qubits, corresponding to 4-asset and 10-asset portfolio configurations. The QUBO penalty parameter is set to n/2 (where n is the number of assets), and the risk-aversion parameter is fixed at q = 0.5. Each ansatz architecture is tested across five circuit depths (2, 4, 6, 8, 10) with five random seeds per configuration. The number of measurement shots is fixed at 1024. The study employs the COBYLA optimizer for classical parameter optimization. All simulations are performed on a quantum simulator without real quantum hardware.

**Dataset:** Historical stock price data from Yahoo Finance covering the six-month period from December 2024 to May 2025. The 4-asset portfolio includes Apple (AAPL), Google (GOOG), Microsoft (MSFT), and Tesla (TSLA). The 10-asset portfolio adds Amazon (AMZN), NVIDIA (NVDA), Goldman Sachs (GS), Morgan Stanley (MS), Nike (NKE), and Coca Cola (KO). Future performance is evaluated using stock returns from June 2025 (2 June to 20 June).
## Findings
- [supported] VQE and QAOA demonstrate effective cost function minimization in portfolio optimization tasks for 4- and 10-asset configurations, with results obtained via simulation on QASM simulator
- [supported] RealAmplitudes ansatz achieves the fastest convergence (under 100 evaluations) for 4-asset portfolios across all circuit depths, while PauliTwoDesign shows the most stable convergence improvement with increasing depth
- [supported] Deeper circuits (depth=10) in 10-asset configurations produce more financially viable portfolios (e.g., diversified selections including Google, Coca Cola, and Goldman Sachs) compared to shallower circuits
- [supported] Quantum-generated portfolios often violate financial criteria such as diversification and risk exposure, with 4-asset configurations frequently selecting high-volatility assets (e.g., Tesla and Apple) despite poor historical performance
- [supported] Expert evaluation reveals that only 1 out of 4 quantum-generated 4-asset portfolios and 4 out of 5 10-asset portfolios achieved positive returns in the subsequent month (June 2025), demonstrating a disparity between algorithmic optimization and real-world performance
- [supported] The [GOOG, MSFT] portfolio (selected by RealAmplitudes and EfficientSU2 at depth=2) was the only 4-asset configuration to yield positive returns (+0.95%) in the expert evaluation period
- [speculative] Increasing circuit depth may improve portfolio diversification in larger asset universes, but this trend does not hold for smaller, highly correlated asset sets where deeper circuits introduce instability
- [speculative] The authors suggest that expert-guided validation frameworks could bridge the gap between quantum optimization and practical financial decision-making, though empirical validation of this claim is limited to small-scale experiments
- [disputed] The paper claims that quantum algorithms offer 'potentially superior scalability and performance' for portfolio optimization, but results are limited to 10-qubit simulations with no demonstrated advantage over classical methods

**Results summary:** The paper presents a systematic benchmarking of VQE and QAOA for portfolio optimization using real-world financial data (Dec 2024-May 2025) across 4- and 10-asset configurations. While both algorithms demonstrate effective cost function minimization in simulation, the resulting portfolios frequently violate financial best practices (e.g., diversification, risk management). An expert evaluation framework reveals that only a subset of quantum-generated portfolios achieved positive returns in the subsequent month (June 2025), with deeper circuits (depth=10) showing better alignment with financial viability in larger asset universes. The study highlights a critical gap between algorithmic performance and practical applicability, emphasizing the necessity of human expertise in quantum-assisted financial decision-making.

**Performance claims:**
- RealAmplitudes ansatz converges in fewer than 100 evaluations for 4-asset portfolios across all depths (2-10)
- PauliTwoDesign improves convergence from -0.85 (depth=2) to -1.0 (depth=10) for 4-asset portfolios
- [GOOG, MSFT] portfolio achieves +0.95% return in June 2025 (4-asset configuration)
- [GOOG, MSFT, KO, GS, NVDA] portfolio achieves +1.99% return in June 2025 (10-asset configuration)
- 4 out of 5 quantum-generated 10-asset portfolios yield positive returns in expert evaluation period
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential scalability advantages of quantum algorithms for portfolio optimization but provides no empirical evidence of quantum advantage. All results are derived from classical simulations (QASM simulator) with problem sizes (4-10 qubits) that are trivially solvable by classical methods. Claims of superior performance are based on theoretical complexity arguments rather than demonstrated speedups or solution quality improvements over classical baselines.
## Limitations
- Experiments limited to small problem sizes (4 and 10 assets), corresponding to 4 and 10 qubits, which may not scale to real-world portfolio optimization scenarios [inferred]
- All simulations performed using the QASM simulator, not real quantum hardware, which may not account for hardware noise and decoherence effects
- QAOA exhibits high variance and instability in convergence behavior, particularly at lower circuit depths
- Portfolios generated by quantum algorithms often violate essential financial criteria such as diversification and realistic risk exposure
- Quantum models rely on historical pricing data, which may not capture evolving market dynamics or investor-specific preferences
- Increasing circuit depth does not necessarily improve portfolio quality, especially in small, highly correlated asset sets
- Expert analysis framework is subjective and may introduce bias in portfolio selection [inferred]
- Limited to binary optimization (asset selection), which may not fully capture real-world portfolio constraints like continuous asset weights [inferred]
- Fixed risk-aversion parameter (q = 0.5) may not reflect diverse investor profiles [inferred]
- No comparison with state-of-the-art classical solvers to benchmark quantum advantage [inferred]
- Page-limit constraints of conference papers may have restricted detailed discussion of methodology or results [inferred]
## Open questions
- How do quantum algorithms perform with larger asset universes (e.g., 50+ assets) that reflect real-world portfolio optimization?
- What is the impact of hardware noise and decoherence on the quality of quantum-optimized portfolios?
- Can hybrid quantum-classical approaches improve the financial viability of quantum-generated portfolios?
- How can investor-specific preferences and real-time market conditions be incorporated into quantum optimization pipelines?
- What are the trade-offs between circuit depth, convergence stability, and portfolio quality in variational quantum algorithms?
- How does the performance of quantum algorithms compare to classical solvers for portfolio optimization in terms of scalability and solution quality?
- Can quantum algorithms be adapted to handle continuous asset weights, rather than binary selection?
- What is the long-term economic viability of quantum-optimized portfolios under dynamic market conditions?

**Future work:**
- Test quantum algorithms on real quantum hardware to evaluate the impact of noise and decoherence
- Extend the study to larger asset universes (e.g., 20+ assets) to assess scalability
- Incorporate real-time market data and investor-specific constraints into the quantum optimization pipeline
- Develop hybrid quantum-classical methods to improve portfolio diversification and risk management
- Benchmark quantum algorithms against state-of-the-art classical solvers for portfolio optimization
- Explore the use of quantum algorithms for continuous asset weight optimization
- Investigate the integration of machine learning techniques with quantum optimization for dynamic portfolio management
- Assess the long-term performance of quantum-optimized portfolios under varying market conditions
- Refine the expert analysis framework to reduce subjectivity and improve reproducibility
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical methodology integrates QUBO-based optimization with expert-driven financial evaluation to bridge the gap between algorithmic performance and real-world viability
- #idea:near-term-feasibility — VQE and QAOA demonstrate effective cost function minimization for small-scale portfolio optimization (4-10 assets) in simulated environments, suggesting near-term applicability in constrained settings
- #idea:quantum-advantage — Paper speculatively claims potential scalability advantages for quantum algorithms, though no empirical evidence is provided for quantum advantage over classical methods
- #limitation:no-empirical-validation — Quantum-generated portfolios often violate financial criteria (e.g., diversification, risk exposure), highlighting the need for expert validation frameworks
- #limitation:simulation-only — All results are derived from classical simulations (QASM simulator) with no real quantum hardware validation, limiting insights into noise and decoherence effects
- #idea:hybrid-approach — Expert Analysis Framework integrates human financial expertise to assess economic soundness of quantum-optimized portfolios, improving practical feasibility
## Contradictions
- #contradiction:classical-vs-quantum — Paper claims 'potentially superior scalability and performance' for quantum algorithms, but results are limited to 10-qubit simulations with no demonstrated advantage over classical solvers (e.g., no comparison with state-of-the-art classical portfolio optimization methods)
- #contradiction:scalability — While deeper circuits (depth=10) improve portfolio diversification in 10-asset configurations, the trend does not hold for smaller asset sets, and scalability to real-world problem sizes (50+ assets) remains untested
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
