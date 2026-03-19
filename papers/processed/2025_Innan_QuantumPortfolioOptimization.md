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
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- VQE
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:37:40.531772'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:37:57.402567'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:38:32.064026'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:39:01.608370'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:39:37.145026'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:39:45.668595'
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
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Portfolio Optimization with Expert Analysis Evaluation
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper benchmarks two variational quantum algorithms—Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA)—for portfolio optimization in financial services. The study evaluates their performance across different asset universes, circuit architectures, and depths, revealing that while these methods effectively minimize cost functions, the resulting portfolios often fail to meet practical financial criteria like diversification and risk exposure. To address this, the authors introduce an Expert Analysis Evaluation framework, where financial professionals assess the economic viability of quantum-optimized portfolios, highlighting the gap between algorithmic performance and real-world applicability.
## Methodology
The paper presents a hybrid methodology combining quantum optimization algorithms with expert financial analysis for portfolio optimization. The process begins with formulating the portfolio selection problem as a Quadratic Unconstrained Binary Optimization (QUBO) instance, incorporating risk-aversion and budget constraints. Two variational quantum algorithms, Quantum Approximate Optimization Algorithm (QAOA) and Sampling Variational Quantum Eigensolver (SamplingVQE), are implemented to solve the QUBO problem. The study evaluates these algorithms under diverse experimental settings, including different asset universes (4 and 10 assets), ansatz architectures (TwoLocal, EfficientSU2, PauliTwoDesign, RealAmplitudes), and circuit depths (2, 4, 6, 8, 10 layers). Optimization performance is assessed through convergence analysis, focusing on cost function minimization and stability across multiple random seeds. Following quantum optimization, an Expert Analysis Evaluation framework is introduced, where financial professionals assess the economic soundness, diversification, and market feasibility of the quantum-generated portfolios. This framework integrates human judgment to refine portfolio selections, ensuring alignment with real-world financial criteria and investor preferences.

**Algorithms used:** QAOA, SamplingVQE
**Frameworks:** Qiskit, Qiskit Finance, Qiskit Aer

**Experimental setup:** Experiments are conducted using the QASM simulator within the Qiskit framework. The study evaluates two problem sizes: 4 assets (4 qubits) and 10 assets (10 qubits). Each configuration is tested across five circuit depths (2, 4, 6, 8, 10 layers) with five different random seeds. The number of measurement shots is fixed at 1024. The QUBO penalty parameter is set to n/2, where n is the number of assets, and the risk-aversion parameter is fixed at q = 0.5. Historical financial data from Yahoo Finance covering December 2024 to May 2025 is used for optimization, with an additional evaluation period in June 2025 for expert analysis.

**Dataset:** Historical stock price data from Yahoo Finance for the period December 2024 to May 2025, including assets such as Apple (AAPL), Google (GOOG), Microsoft (MSFT), Tesla (TSLA), Amazon (AMZN), NVIDIA (NVDA), Goldman Sachs (GS), Morgan Stanley (MS), Nike (NKE), and Coca Cola (KO). The dataset is used for both optimization and subsequent expert evaluation in June 2025.
## Findings
- [supported] VQE and QAOA demonstrate effective cost function minimization in portfolio optimization, but resulting portfolios often violate financial criteria like diversification and risk exposure
- [supported] RealAmplitudes ansatz achieves the fastest convergence (under 100 evaluations) in 4-asset configurations across all depths
- [supported] Increasing circuit depth improves convergence stability for most ansatz architectures, but QAOA exhibits high variance even at depth=10
- [supported] In 4-asset configurations, quantum algorithms frequently produce multiple high-probability portfolios due to strong asset correlations, reducing selection certainty
- [supported] In 10-asset configurations, deeper circuits (depth=10) generate more financially viable portfolios with better sector diversification than shallow circuits
- [supported] Expert evaluation reveals that only 1 of 4 quantum-generated 4-asset portfolios produced positive returns in the subsequent month (June 2025)
- [supported] 4 out of 5 quantum-generated 10-asset portfolios produced positive returns in June 2025, with the best performing at 1.99% return
- [supported] Portfolios containing Microsoft, Google, and Goldman Sachs consistently outperformed others in expert evaluation, while Tesla and Apple underperformed
- [speculative] Quantum computing may offer superior scalability for portfolio optimization due to its ability to handle NP-hard problems more efficiently than classical methods
- [speculative] The authors suggest that expert-guided validation could bridge the gap between quantum algorithmic performance and real-world financial applicability
- [disputed] The paper claims quantum advantage in portfolio optimization, but all results are from simulation only and no comparison with state-of-the-art classical methods is provided

**Results summary:** The paper presents a systematic benchmarking of VQE and QAOA for portfolio optimization using real financial data from December 2024 to May 2025. While both algorithms demonstrate strong convergence properties - particularly at higher circuit depths - the resulting portfolios often fail to meet practical financial criteria. The study introduces an Expert Analysis Framework that evaluates quantum-generated portfolios for real-world viability. Results show that quantum algorithms can efficiently generate candidate portfolios, but expert evaluation reveals significant gaps between algorithmic performance and financial practicality. Notably, only 25% of 4-asset quantum portfolios and 80% of 10-asset portfolios produced positive returns in the subsequent month, with deeper circuits performing better in larger asset universes.

**Performance claims:**
- RealAmplitudes ansatz converges in fewer than 100 evaluations across all depths in 4-asset configuration
- PauliTwoDesign improves convergence from -0.85 to -1.0 when increasing depth from 2 to 10 in 4-asset configuration
- QAOA shows high variance with objective values ranging from -2.0 to near 0 at lower depths in 10-asset configuration
- Best performing 10-asset portfolio achieved 1.99% return in June 2025 (though not generated by any quantum circuit)
- EfficientSU2 generated a 10-asset portfolio with 1.62% return in June 2025
- Only 1 of 4 quantum-generated 4-asset portfolios produced positive returns (0.95%) in June 2025
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage in handling the NP-hard nature of portfolio optimization, but all results are from simulation only. No direct comparison with classical methods is provided, and the authors acknowledge that real quantum hardware would introduce additional challenges like noise and decoherence. The claimed advantage remains theoretical and unvalidated on real hardware.
## Limitations
- Experiments limited to small problem sizes (4 and 10 assets), corresponding to 4 and 10 qubits, which may not scale to real-world portfolio optimization scenarios [inferred]
- All simulations performed using the QASM simulator, not real quantum hardware, which may not account for noise, decoherence, and other hardware-specific limitations
- Results may not generalize to larger asset universes due to the exponential growth of the solution space in portfolio optimization
- Quantum algorithms rely on historical pricing data, which cannot fully capture evolving market dynamics, geopolitical risks, or investor-specific preferences
- Expert analysis framework introduces subjectivity and may not be scalable for high-frequency or automated trading systems [inferred]
- Fixed risk-aversion parameter (q = 0.5) and penalty parameter (α = n/2) may not reflect diverse investor profiles or dynamic market conditions
- No comparison with state-of-the-art classical solvers to benchmark quantum advantage [inferred]
- Page-limit constraints of the conference paper may have limited the depth of analysis on certain aspects, such as noise mitigation techniques or alternative optimization methods [inferred]
- Portfolio evaluation limited to a short future time period (June 2025), which may not reflect long-term performance or robustness [inferred]
- High variance in QAOA performance, particularly at lower circuit depths, suggests sensitivity to parameter initialization and circuit design
## Open questions
- How do quantum algorithms perform on larger asset universes (e.g., 50+ assets) that are more representative of real-world portfolio optimization?
- What is the impact of noise and decoherence on the quality of quantum-generated portfolios when executed on real quantum hardware?
- Can the Expert Analysis framework be automated or integrated with machine learning models to reduce subjectivity and improve scalability?
- How do quantum algorithms compare to classical solvers in terms of solution quality, computational efficiency, and scalability for portfolio optimization?
- What are the implications of dynamic risk-aversion parameters and penalty terms on the performance of quantum algorithms?
- How can quantum algorithms incorporate forward-looking market data or probabilistic forecasting to improve portfolio viability?
- What are the trade-offs between circuit depth, expressibility, and financial interpretability in quantum portfolio optimization?
- How can quantum algorithms be adapted to handle additional real-world constraints, such as transaction costs, liquidity requirements, or ethical investment criteria?

**Future work:**
- Test the proposed framework on real quantum hardware to evaluate the impact of noise and decoherence on portfolio quality
- Extend the study to larger asset universes (e.g., 20+ assets) to assess scalability and practical applicability
- Compare quantum algorithms with state-of-the-art classical solvers to benchmark quantum advantage in portfolio optimization
- Incorporate dynamic risk-aversion parameters and penalty terms to reflect diverse investor profiles and market conditions
- Develop hybrid quantum-classical frameworks that integrate probabilistic forecasting or alternative risk models
- Explore adaptive ansatz architectures or optimization techniques to improve convergence stability and financial interpretability
- Investigate the integration of machine learning models with the Expert Analysis framework to automate or enhance portfolio evaluation
- Extend the evaluation period to assess the long-term performance and robustness of quantum-generated portfolios
- Apply the framework to other financial optimization problems, such as asset-liability management or risk parity portfolios
## Key ideas
- #idea:hybrid-approach — Hybrid quantum-classical methodology integrates QUBO-based optimization with expert-driven financial evaluation to bridge the gap between algorithmic performance and real-world viability
- #idea:near-term-feasibility — VQE and QAOA demonstrate effective cost function minimization for small-scale portfolio optimization (4-10 assets) in simulated environments, suggesting near-term applicability in constrained settings
- #idea:quantum-advantage — Paper speculatively claims potential scalability advantages for quantum algorithms in handling NP-hard portfolio optimization problems, though no empirical evidence is provided
- #limitation:no-empirical-validation — Quantum-generated portfolios often violate financial criteria (e.g., diversification, risk exposure), necessitating expert validation frameworks for practical use
- #limitation:simulation-only — All results are derived from classical simulations (QASM simulator) with no real quantum hardware validation, limiting insights into noise and decoherence effects
- #idea:hybrid-approach — Expert Analysis Framework integrates human financial expertise to assess economic soundness of quantum-optimized portfolios, improving practical feasibility
## Contradictions
- #contradiction:classical-vs-quantum — Paper claims 'potentially superior scalability and performance' for quantum algorithms, but results are limited to 10-qubit simulations with no demonstrated advantage over classical solvers (e.g., no comparison with state-of-the-art classical portfolio optimization methods)
- #contradiction:scalability — While deeper circuits (depth=10) improve portfolio diversification in 10-asset configurations, the trend does not hold for smaller asset sets, and scalability to real-world problem sizes (50+ assets) remains untested
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
