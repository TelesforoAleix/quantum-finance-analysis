---
aliases:
- 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
- Autonomous Quantum Agents Portfolio
authors:
- Kaushik Ganguly
auto_detected: true
classification: ''
contradiction_flags: []
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-20T00:07:28.977065'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:07:32.083450'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:07:47.043456'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:07:57.353892'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:08:37.324240'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:08:40.945756'
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
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
topic_tags:
- portfolio-optimisation
year: 2026
zotero_key: ''
---

## Abstract summary
This paper introduces an agentic framework that automates the end-to-end process of quantum portfolio optimization, integrating live financial data with quantum computing workflows. The system employs specialized AI agents to handle tasks such as circuit construction, cloud quantum execution, and result interpretation, addressing operational challenges in deploying quantum algorithms for financial decision-making. The framework demonstrates reproducibility and vendor-agnostic execution on cloud quantum simulators, offering a scalable approach to bridging quantum optimization algorithms with practical financial applications.
## Methodology
The paper presents an empirical study on an agentic framework for end-to-end portfolio optimization using quantum computing. The framework integrates autonomous AI workflow orchestration with the Quantum Approximate Optimization Algorithm (QAOA) executed on cloud quantum simulators. The system employs eight specialized agents coordinated through a directed acyclic graph (DAG) state machine built on the LangGraph framework. Each agent handles a distinct stage of the quantum optimization pipeline, including policy enforcement, task decomposition, circuit construction from live market data, local pre-validation, cloud QPU submission, quality assurance, and financial interpretation. The QAOA ansatz is parameterized using empirical annualized asset returns and pairwise covariance entries from live Yahoo Finance data for a five-asset universe. The framework is executed on two cloud quantum backends via the QBraid unified runtime platform: the AWS Tensor Network simulator and the QBraid QIR state-vector simulator. The study evaluates the framework's performance, cross-platform consistency, and financial metrics derived from the measurement outcomes.

**Algorithms used:** QAOA
**Frameworks:** LangGraph, Qiskit, QBraid

**Experimental setup:** The experiments were conducted using a five-asset universe (AAPL, XOM, JPM, JNJ, GLD) with live market data from Yahoo Finance. The QAOA circuit was constructed with 5 qubits and 5 layers, executed on two cloud quantum simulators: AWS Tensor Network simulator (1000 shots) and QBraid QIR state-vector simulator (2000 shots). The framework leverages the QBraid runtime for vendor-agnostic quantum execution.

**Dataset:** Historical daily closing prices for five assets (AAPL, XOM, JPM, JNJ, GLD) spanning technology, energy, finance, healthcare, and commodities, fetched from Yahoo Finance over a one-year period ending February 2026.
## Findings
- [supported] The agentic framework for quantum portfolio optimization using QAOA achieved a normalized measurement distribution mean of 0.6712 on AWS Tensor Network simulator and 0.6713 on QBraid QIR state-vector simulator, demonstrating cross-platform consistency [supported]
- [supported] The dominant measured bitstring (01011, corresponding to the portfolio AAPL+XOM+JNJ) appeared in 23.55% of shots—7.6 times the uniform baseline probability of 3.125%—and achieved an annualized return of 31.17%, volatility of 19.29%, and a Sharpe ratio of 1.62 [supported]
- [supported] The top-5 bitstrings accounted for 67.60% of all measurements, compared to a uniform expectation of 15.63%, confirming a strongly non-uniform output distribution [supported]
- [supported] The QAOA’s fourth-ranked bitstring (XOM+JPM+JNJ) achieved the highest Sharpe ratio (2.99) among all evaluated strategies, including equal-weight benchmarks [supported]
- [supported] The agentic overhead constituted less than 2% of total pipeline execution time, with job wait time (74.07%) being the dominant cost [supported]
- [supported] The maturity-gated governance model effectively prevented inadvertent hardware expenditure during development by mapping job lifecycle stages to quantum resource permissions [supported]
- [speculative] The framework could scale to larger asset universes (n ≥ 20) with minimal modifications, though this was not empirically validated [speculative]
- [speculative] Incorporating a variational outer loop for QAOA parameter optimization could improve solution quality, but this was not implemented [speculative]
- [speculative] The agentic architecture could orchestrate other quantum optimization algorithms (e.g., BF-DCQO, warm-started QAOA) without significant changes [speculative]

**Results summary:** The paper presents an agentic framework for automating quantum portfolio optimization using QAOA on cloud quantum simulators. The system demonstrated consistent performance across two cloud backends (AWS Tensor Network and QBraid QIR), with negligible distributional shift in measurement outcomes. The dominant portfolio (AAPL+XOM+JNJ) achieved a Sharpe ratio of 1.62, outperforming several classical benchmarks. The framework's maturity-gated governance model effectively managed quantum resource permissions, and the agentic overhead was minimal (<2% of execution time). While the results are promising, they are limited to simulations and a small asset universe (n=5).

**Performance claims:**
- Normalized measurement distribution mean of 0.6712 (AWS TN1) and 0.6713 (QBraid QIR) with cross-platform consistency within 0.0001
- Dominant bitstring (01011) appeared in 23.55% of shots (7.6x uniform baseline)
- Top-5 bitstrings accounted for 67.60% of measurements (vs. 15.63% uniform expectation)
- QAOA’s fourth-ranked portfolio achieved a Sharpe ratio of 2.99, the highest among all evaluated strategies
- Agentic overhead <2% of total pipeline execution time (0.40% for routing/state management)
- Job wait time dominated execution (74.07% of total wall-clock time)
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim quantum advantage. All results are from simulations (AWS Tensor Network and QBraid QIR state-vector simulators) on a small-scale problem (5 assets) that is classically trivial. The focus is on operational orchestration rather than quantum speedup or solution quality improvements over classical methods.
## Limitations
- Problem scale limited to 5 assets (5 qubits), which is classically trivial and does not demonstrate quantum advantage [inferred]
- Experiments conducted only on quantum simulators (AWS Tensor Network and QBraid QIR state-vector simulators), not on real quantum hardware, which may introduce noise and decoherence effects not accounted for
- Non-variational QAOA parameters used (analytically determined rotation angles from market data), which may limit optimization performance compared to variational approaches
- Single-run evaluation without bootstrapped confidence intervals on financial metrics, limiting statistical robustness [inferred]
- Equal-weight allocation used for financial evaluation, which may not reflect optimal weight distributions within selected asset subsets
- No error mitigation techniques applied, which could be critical for real hardware execution [inferred]
- No comparison with state-of-the-art classical solvers (e.g., branch-and-bound, heuristics) to benchmark quantum advantage [inferred]
- Pipeline execution performance dominated by cloud quantum job wait times (74.07% of total time), which may not scale efficiently for production use [inferred]
- No dynamic backend selection based on real-time availability, queue depth, or calibration data, which could optimize resource usage [inferred]
- Quality control agent uses a simplistic threshold (normalized mean > 0) that may not adequately capture hardware noise or solution quality on real devices [inferred]
## Open questions
- How does the agentic framework perform with larger asset universes (n ≥ 20) where classical methods struggle?
- What is the impact of hardware noise and decoherence on solution quality when executed on real quantum processors?
- Can variational optimization of QAOA parameters improve the measurement distribution and financial metrics compared to the current data-driven approach?
- How does the framework compare to state-of-the-art classical solvers in terms of solution quality and computational efficiency?
- What error mitigation techniques are most effective for this pipeline when executed on noisy intermediate-scale quantum (NISQ) devices?
- How does the pipeline handle dynamic market conditions, such as real-time data updates or regime shifts?
- What is the scalability of the agentic overhead as the number of assets or pipeline complexity increases?
- How can the quality control agent be enhanced to better distinguish between quantum noise and meaningful solution distributions?

**Future work:**
- Extend the framework to incorporate a variational outer loop for optimizing QAOA parameters
- Implement correlation-based decomposition for large asset universes, enabling parallel QPU submissions for subproblems
- Test the pipeline on real quantum hardware (e.g., IBM Quantum, IonQ) to evaluate noise resilience and solution quality
- Develop dynamic backend selection based on real-time availability, queue depth, and calibration data
- Incorporate noise-aware quality gating using statistical divergence measures to improve robustness
- Explore multi-objective cost Hamiltonians that encode the Sharpe ratio directly for better risk-adjusted performance
- Evaluate the framework with bootstrapped confidence intervals to assess statistical significance of results
- Extend the financial interpretation to solve for optimal weights within selected asset subsets, rather than equal-weight allocation
- Integrate error mitigation techniques (e.g., zero-noise extrapolation, probabilistic error cancellation) for real hardware execution
- Benchmark the pipeline against classical solvers to quantify quantum advantage at scale
## Key ideas
- #idea:near-term-feasibility — Agentic framework automates end-to-end quantum portfolio optimization using QAOA on cloud simulators, demonstrating operational feasibility for small-scale problems
- #idea:hybrid-approach — Integration of autonomous AI workflow orchestration with quantum optimization (QAOA) enables vendor-agnostic, reproducible execution on current cloud quantum infrastructure
- #limitation:simulation-only — All results derived from classical simulations (AWS Tensor Network and QBraid QIR), not real quantum hardware, limiting claims about NISQ-era applicability
- #limitation:qubit-count — Framework tested only on a 5-asset universe, with no empirical validation of scalability to larger, industrially relevant portfolios (e.g., 20+ assets)
- #limitation:no-empirical-validation — Speculative claims about scalability and real-world performance lack empirical support, including comparisons with classical solvers
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Yahoo Finance via yfinance Python library', 'size': '5 assets, approximately 252 trading days (one year)', 'features': ['daily closing prices', 'annualized returns', 'pairwise covariance matrix'], 'preprocessing_steps': ['Daily log-returns computed as r_t = log(p_t / p_{t-1})', 'Annualized returns and risks calculated using 252 trading days convention', 'Covariance matrix derived from log-returns'], 'time_period': 'One-year trailing period ending February 2026'}

### Process
1. Market data acquisition: Fetch live Yahoo Finance data for five assets. 2. Circuit construction: AutoCircuitDesigner constructs QAOA ansatz with single-qubit rotations from annualized returns and two-qubit interactions from pairwise covariance. 3. Local pre-validation: SimulationSandbox runs circuit on Qiskit BasicSimulator (1000 shots) to verify non-trivial measurement distribution. 4. Cloud submission: QPUBroker submits circuit to AWS TN1 (1000 shots) and QBraid QIR (2000 shots) via QBraid runtime. 5. Result polling: Asynchronous monitoring of job status at 5-second intervals. 6. Quality control: QCAAgent evaluates measurement distribution mean (> 0 threshold). 7. Financial interpretation: Aggregator decodes bitstrings into portfolio selections and computes metrics (annualized return, volatility, Sharpe ratio).

### Output
{'metrics_reported': ['Normalized measurement distribution mean', 'Portfolio annualized return', 'Portfolio volatility', 'Sharpe ratio', 'Bitstring frequency and probability'], 'comparison_baselines': ['Equal-weight portfolio (all five assets)', 'Best single asset (XOM)', 'Worst single asset (AAPL)', 'Random 3-asset portfolio (average)', 'Minimum variance portfolio (JPM only)'], 'output_format': 'JSON artifact containing job descriptor, market data snapshot, measurement counts, financial metrics, and provenance metadata.'}

### Parameters
- qubits: 5
- circuit_layers: 5
- shots: {'AWS TN1': 1000, 'QBraid QIR': 2000, 'Local simulation': 1000}
- optimizer: Analytical (data-driven parameterization)
- rotation_angles: {'single_qubit': 'Derived from annualized returns (γᵢ = μᵢ · π)', 'two_qubit': 'Derived from pairwise covariance (γᵢⱼ = Cᵢⱼ · π / 2)', 'mixer': 'βᵢ = l · 0.4 · π / p'}
- trade_off_parameter: λ = 0.5 (equal weight to risk and return)

### Hardware
{'simulators': [{'name': 'AWS Tensor Network simulator', 'provider': 'AWS', 'shots': 1000, 'backend_id': 'aws:aws:sim:tn1'}, {'name': 'QBraid QIR state-vector simulator', 'provider': 'QBraid', 'shots': 2000, 'backend_id': 'qbraid:qbraid:sim:qir-sv'}, {'name': 'Qiskit BasicSimulator', 'shots': 1000}], 'transpilation': 'Handled internally by QBraid runtime for cross-platform execution'}

### Reproducibility
Code and framework details are described in sufficient detail for replication, including agent responsibilities, state specifications, and circuit construction. Market data is publicly available via Yahoo Finance. The QBraid runtime and Qiskit are open-source frameworks. The paper provides GitHub references for LangGraph and QBraid, though no direct link to the specific code repository is provided. The methodology is well-documented, enabling replication with access to the described tools and data sources.
