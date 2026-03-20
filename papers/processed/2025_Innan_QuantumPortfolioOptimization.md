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
step1_date: '2026-03-20T00:27:22.871033'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:27:25.742118'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:27:38.195228'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:27:47.042342'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:27:56.245952'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:28:13.197294'
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
This paper benchmarks two variational quantum algorithms—Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA)—for portfolio optimization in financial services. The study evaluates their performance across different asset universes, circuit architectures, and depths, revealing that while these methods effectively minimize cost functions, the resulting portfolios often fail to meet practical financial criteria like diversification and risk exposure. To address this, the authors introduce an Expert Analysis Evaluation framework, integrating human financial expertise to assess the economic soundness and market feasibility of quantum-optimized portfolios, highlighting the gap between algorithmic performance and real-world applicability.
## Methodology
The paper presents an empirical study benchmarking two variational quantum algorithms, Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA), for portfolio optimization in financial services. The methodology involves formulating the portfolio selection problem as a Quadratic Unconstrained Binary Optimization (QUBO) instance, which is then mapped to a quantum Hamiltonian. The study evaluates the performance of QAOA and SamplingVQE across different asset universes (4 and 10 assets), ansatz architectures (TwoLocal, EfficientSU2, PauliTwoDesign, RealAmplitudes), and circuit depths (2, 4, 6, 8, 10). The quantum-optimized portfolios are subsequently assessed by financial experts to evaluate their economic soundness and practical viability. The research highlights the integration of quantum optimization with expert-driven validation to bridge the gap between algorithmic performance and financial applicability.

**Algorithms used:** QAOA, VQE, SamplingVQE
**Frameworks:** Qiskit, Qiskit Aer, Qiskit Finance

**Experimental setup:** Experiments are conducted using Qiskit's QASM simulator with 4 and 10 qubits, corresponding to 4-asset and 10-asset portfolio configurations. The study employs historical stock price data from Yahoo Finance covering December 2024 to May 2025. Each quantum algorithm (QAOA and SamplingVQE) is tested across five circuit depths (2, 4, 6, 8, 10) and five random seeds, with 1024 measurement shots per experiment. The QUBO penalty parameter is set to n/2, and the risk-aversion parameter is fixed at q = 0.5.

**Dataset:** Historical stock prices from Yahoo Finance for 10 assets (AAPL, GOOG, MSFT, TSLA, AMZN, NVDA, GS, MS, NKE, KO) over a six-month period (December 2024 to May 2025). The dataset includes daily closing prices used to compute returns and covariance matrices for portfolio optimization.
## Findings
- [supported] VQE and QAOA demonstrate effective cost function minimization in portfolio optimization, but resulting portfolios often violate financial criteria such as diversification and realistic risk exposure
- [supported] RealAmplitudes ansatz achieves the fastest convergence in 4-asset configurations, reaching optimal solutions in fewer than 100 evaluations across all depths
- [supported] Increasing circuit depth improves convergence stability for most ansatz architectures (e.g., PauliTwoDesign improves from -0.85 to -1.0 in 4-asset configuration), but QAOA exhibits increased variance with depth
- [supported] In 4-asset configurations, quantum algorithms frequently produce multiple high-probability portfolios due to strong asset correlations, indicating selection uncertainty
- [supported] Deeper circuits (depth=10) in 10-asset configurations produce more financially viable portfolios (e.g., TwoLocal and EfficientSU2 generate diversified portfolios with Google, Coca Cola, Goldman Sachs, and Amazon/NVIDIA)
- [supported] Expert evaluation reveals that portfolios containing Microsoft, Google, and Goldman Sachs consistently outperform others in forward-looking returns (e.g., [GOOG, MSFT] achieved 0.95% return in June 2025 vs. -3.17% for [AAPL, TSLA])
- [supported] Quantum-generated portfolios benefit from expert interpretation, with 4 out of 5 10-asset configurations producing positive returns after expert filtering
- [speculative] Quantum computing may offer superior scalability for portfolio optimization due to its ability to handle NP-hard combinatorial problems more efficiently than classical methods
- [speculative] The integration of expert analysis with quantum optimization could enable adaptive financial systems responsive to market fluctuations and investor preferences
- [disputed] The paper claims that quantum algorithms do not inherently incorporate real-world financial considerations, but some recent literature suggests hybrid quantum-classical approaches can integrate such factors (e.g., [17], [22])

**Results summary:** The paper presents a systematic benchmarking of VQE and QAOA for portfolio optimization using real-world financial data (Dec 2024-May 2025) across 4- and 10-asset configurations. While both algorithms demonstrate strong convergence properties—particularly at higher circuit depths—they often produce portfolios that violate practical financial criteria. The study introduces an Expert Analysis Evaluation framework that filters quantum-generated portfolios through financial professionals' judgment, revealing a critical gap between algorithmic performance and real-world applicability. Notably, deeper circuits in larger asset configurations (10 assets) tend to yield more diversified and financially sound portfolios, though convergence metrics alone do not guarantee future performance. The hybrid approach combining quantum optimization with expert validation shows promise for bridging computational efficiency and financial interpretability.

**Performance claims:**
- RealAmplitudes ansatz converges in fewer than 100 evaluations for 4-asset configurations across all depths
- PauliTwoDesign improves convergence from -0.85 to -1.0 as depth increases from 2 to 10 in 4-asset configurations
- [GOOG, MSFT] portfolio achieves 0.95% return in June 2025 (forward-looking) vs. -3.17% for [AAPL, TSLA]
- 4 out of 5 10-asset portfolios produce positive returns after expert filtering (highest: 1.99%)
- QAOA exhibits high variance in convergence, particularly at lower depths (e.g., near -2.0 for 10 assets at depth=2)
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential scalability advantages for quantum algorithms in handling NP-hard portfolio optimization problems but does not demonstrate quantum advantage empirically. All results are from simulations (QASM simulator) rather than real quantum hardware, and the claimed advantage remains theoretical for larger problem sizes (beyond 10 assets). The authors acknowledge that real hardware limitations (noise, decoherence) may further impact performance.
## Limitations
- Experiments limited to small problem sizes (4 and 10 assets), corresponding to 4 and 10 qubits, which may not scale to real-world portfolio optimization scenarios [inferred]
- All simulations performed using the QASM simulator, not real quantum hardware, which may not account for noise, decoherence, or other hardware-specific limitations
- Results may not generalize to larger asset universes due to the exponential growth of the solution space in portfolio optimization problems
- Quantum algorithms rely on historical pricing data, which cannot fully capture evolving market dynamics, geopolitical risks, or investor-specific preferences
- Expert Analysis Framework introduces subjectivity and may not be scalable for high-frequency or automated trading systems [inferred]
- Circuit depth and ansatz architecture choices may introduce bias, as deeper circuits do not always yield better financial outcomes despite improved convergence
- Fixed number of measurement shots (1024) may limit the accuracy of probability distributions for portfolio selection [inferred]
- No comparison with state-of-the-art classical solvers to benchmark quantum advantage in terms of solution quality or computational efficiency
- Penalty parameter α and risk-aversion parameter q are fixed, which may not reflect dynamic investor preferences or market conditions [inferred]
- Portfolio evaluation limited to short-term future returns (June 2025), which may not capture long-term performance or risk characteristics [inferred]
- Conference paper page limits may have constrained detailed discussion of methodology, experimental setup, or results [inferred]
- No noise mitigation techniques applied, which could significantly impact performance on real quantum hardware [inferred]
## Open questions
- How do quantum algorithms perform on larger asset universes (e.g., 50+ assets) that are typical in real-world portfolio optimization?
- What is the impact of noise and decoherence on the quality of quantum-generated portfolios when executed on real quantum hardware?
- Can the Expert Analysis Framework be automated or integrated with machine learning models to reduce subjectivity and improve scalability?
- How do quantum algorithms compare to classical solvers (e.g., simulated annealing, genetic algorithms) in terms of solution quality, computational efficiency, and scalability?
- What are the trade-offs between circuit depth, convergence stability, and financial viability of the generated portfolios?
- How can dynamic market conditions (e.g., volatility, geopolitical risks) be incorporated into quantum optimization pipelines?
- What is the minimum qubit count and circuit depth required to achieve a practical advantage over classical methods for portfolio optimization?
- How do different risk models (e.g., CVaR, Black-Litterman) affect the performance of quantum algorithms in portfolio optimization?
- Can hybrid quantum-classical approaches (e.g., quantum-enhanced classical solvers) bridge the gap between algorithmic performance and financial applicability?

**Future work:**
- Test the proposed framework on real quantum hardware to evaluate the impact of noise and decoherence on portfolio quality
- Extend the study to larger asset universes (e.g., 20+ assets) to assess scalability and practical applicability
- Compare quantum algorithms with state-of-the-art classical solvers to benchmark quantum advantage in portfolio optimization
- Incorporate dynamic market conditions and investor preferences into the quantum optimization pipeline
- Develop automated or machine learning-enhanced versions of the Expert Analysis Framework to improve scalability and reduce subjectivity
- Explore hybrid quantum-classical approaches to combine the strengths of quantum optimization with classical financial modeling
- Investigate the use of noise mitigation techniques to improve performance on near-term quantum devices
- Apply the framework to multi-period portfolio optimization to capture long-term investment strategies
- Integrate alternative risk models (e.g., CVaR, Black-Litterman) into the quantum optimization process
- Evaluate the framework on diverse financial datasets (e.g., bonds, commodities, cryptocurrencies) to test generalizability
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

## Experiment details
### Input
{'source': 'Yahoo Finance', 'size': '10 assets (4 assets in a smaller configuration)', 'time_period': 'December 2024 to May 2025 (6 months)', 'preprocessing_steps': ['Computation of expected returns (µ) and covariance matrix (Σ) from historical prices', 'Normalization of returns to zero mean (log-returns)', 'Formulation of QUBO problem with penalty term for budget constraint'], 'features': 'Daily closing prices, returns, covariance matrix, risk-aversion parameter (q = 0.5), penalty parameter (α = n/2)'}

### Process
['1. Formulate portfolio optimization as a QUBO problem with risk-aversion and budget constraints.', '2. Map QUBO to a cost Hamiltonian using Pauli-Z operators.', '3. Implement QAOA with alternating cost and mixer Hamiltonians, and SamplingVQE with parameterized ansatz circuits (TwoLocal, EfficientSU2, PauliTwoDesign, RealAmplitudes).', '4. Optimize variational parameters (γ, β for QAOA; θ for SamplingVQE) using COBYLA optimizer.', '5. Execute quantum circuits on QASM simulator with 1024 shots per evaluation.', '6. Repeat experiments across five circuit depths and five random seeds to assess convergence and stability.', '7. Sample bitstrings representing candidate portfolios and analyze their probabilities.', '8. Evaluate portfolios on future returns (June 2025) and subject them to expert analysis for financial viability.']

### Output
{'metrics_reported': ['Objective function value (QUBO cost)', 'Convergence behavior (ΔC_t = C(θ_t) - C(θ_{t-1}))', 'Portfolio composition (bitstring probabilities)', 'Average portfolio return (%) for June 2025', 'Expert evaluation of diversification, liquidity, and investor suitability'], 'comparison_baselines': 'None explicitly mentioned, but expert analysis implicitly compares quantum-optimized portfolios against financial best practices (e.g., sector diversification, risk exposure).', 'output_format': 'Convergence curves, probability histograms of bitstrings, tables of portfolio returns, expert assessment reports.'}

### Parameters
- qubit_count: [4, 10]
- circuit_depth: [2, 4, 6, 8, 10]
- shots: 1024
- optimizer: COBYLA
- risk_aversion_parameter: 0.5
- penalty_parameter: n/2 (n = number of assets)
- random_seeds: 5
- ansatz_architectures: ['TwoLocal', 'EfficientSU2', 'PauliTwoDesign', 'RealAmplitudes']
- entanglement: Full entanglement

### Hardware
{'simulator': 'Qiskit Aer QASM simulator', 'noise_model': 'None (ideal simulation)', 'transpilation_settings': 'Not specified'}

### Reproducibility
Code availability is not explicitly mentioned, but the paper provides sufficient methodological detail (e.g., QUBO formulation, ansatz architectures, optimizer settings) to replicate the experiments. Data is publicly available via Yahoo Finance. The use of random seeds and detailed parameter settings enhances reproducibility.
