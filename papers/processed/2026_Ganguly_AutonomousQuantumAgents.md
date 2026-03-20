---
aliases:
- 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
- Autonomous Quantum Agents Portfolio
authors:
- Kaushik Ganguly
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
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
step1_date: '2026-03-20T00:55:01.599760'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:55:31.922511'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:55:43.911473'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:56:41.482707'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:56:52.060774'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:56:56.004039'
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
- contradiction/classical-vs-quantum
title: 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
topic_tags:
- portfolio-optimisation
year: 2026
zotero_key: ''
---

## Abstract summary
This paper introduces an agentic framework that automates the end-to-end process of quantum portfolio optimization, bridging the gap between advanced quantum algorithms and practical deployment in financial services. The system employs eight specialized AI agents to manage tasks such as data ingestion, circuit construction, cloud quantum execution, and result interpretation, ensuring reproducibility and scalability. By integrating live market data with the Quantum Approximate Optimization Algorithm (QAOA) on cloud-based quantum simulators, the framework demonstrates a vendor-agnostic approach to operationalizing quantum computing for financial decision-making.
## Methodology
The paper presents an agentic framework for end-to-end portfolio optimization using the Quantum Approximate Optimization Algorithm (QAOA) executed on cloud quantum simulators. The framework employs eight specialized agents coordinated through a directed acyclic graph (DAG) state machine built on the LangGraph framework. Each agent handles a distinct stage of the quantum optimization pipeline, including policy enforcement, task decomposition, QAOA circuit construction from live market data, local pre-validation, cloud quantum backend submission, quality assurance, and financial interpretation. The QAOA ansatz is parameterized using empirical annualized asset returns and pairwise covariance entries from Yahoo Finance data for a five-asset universe. The pipeline is executed on two cloud quantum backends via the QBraid unified runtime platform: the AWS Tensor Network simulator and the QBraid QIR state-vector simulator. The framework introduces a maturity-gated governance model to manage quantum resource permissions and ensures reproducibility and vendor-agnostic execution.

**Algorithms used:** QAOA
**Frameworks:** LangGraph, Qiskit, QBraid

**Experimental setup:** The experiments were conducted using a five-asset universe (AAPL, XOM, JPM, JNJ, GLD) with one year of daily closing prices from Yahoo Finance. The QAOA circuit was constructed with 5 qubits and 5 layers, parameterized using annualized returns and covariance matrices derived from the market data. The pipeline was executed on two cloud quantum simulators: AWS Tensor Network simulator (1000 shots) and QBraid QIR state-vector simulator (2000 shots). Local pre-validation was performed using Qiskit's BasicSimulator.

**Dataset:** Historical daily closing prices for five assets (AAPL, XOM, JPM, JNJ, GLD) spanning technology, energy, finance, healthcare, and commodities, sourced from Yahoo Finance over a one-year period ending February 2026.
## Findings
- [supported] The agentic framework for quantum portfolio optimization achieved consistent normalized measurement distribution means of 0.6712 and 0.6713 on AWS Tensor Network and QBraid QIR simulators, respectively, demonstrating cross-platform reproducibility
- [supported] The dominant measured bitstring (01011, corresponding to AAPL+XOM+JNJ) appeared in 23.55% of shots—7.6 times the uniform baseline probability of 3.125%—and achieved an annualized return of 31.17%, volatility of 19.29%, and a Sharpe ratio of 1.62
- [supported] The top-5 bitstrings accounted for 67.60% of all measurements, significantly exceeding the uniform baseline expectation of 15.63%, confirming a strongly non-uniform output distribution driven by market data
- [supported] The QAOA circuit's covariance encoding effectively penalized high-covariance asset pairs, as evidenced by the exclusion of GLD from the dominant portfolio due to its high covariance (2.00 × 10⁻²) with existing selections
- [supported] The agentic overhead constituted less than 2% of total pipeline execution time, with the dominant cost (74.07%) being cloud quantum job wait time
- [supported] The maturity-gated governance model successfully enforced quantum resource permissions, preventing inadvertent hardware expenditure during development stages
- [speculative] The framework could scale to larger asset universes (n ≥ 20) with minimal modifications, though this was not empirically validated in the study
- [speculative] Incorporating a variational outer loop for QAOA parameter optimization could improve distribution quality, but this was not implemented in the current work
- [speculative] The agentic architecture could be extended to orchestrate other quantum optimization algorithms (e.g., BF-DCQO, warm-started QAOA) without significant changes

**Results summary:** The paper presents an agentic framework for quantum portfolio optimization that automates the end-to-end pipeline from live market data ingestion to financially interpreted results. Using a 5-asset universe and QAOA on cloud quantum simulators, the study demonstrates consistent cross-platform measurement distributions (normalized means within 0.0001) and a dominant portfolio (AAPL+XOM+JNJ) appearing in 23.55% of shots—7.6 times the uniform baseline. The framework's covariance-driven asset selection aligns with diversification principles, and the maturity-gated governance model effectively manages quantum resource permissions. While the results are promising, they are limited to simulations and a small asset universe (n=5), with no real hardware validation.

**Performance claims:**
- 23.55% probability for the dominant bitstring (01011), 7.6x the uniform baseline of 3.125%
- Normalized measurement distribution means of 0.6712 (AWS TN1) and 0.6713 (QBraid QIR) with cross-platform consistency within 0.0001
- Annualized return of 31.17%, volatility of 19.29%, and Sharpe ratio of 1.62 for the dominant portfolio
- Top-5 bitstrings accounted for 67.60% of measurements vs. 15.63% uniform baseline expectation
- Agentic overhead < 2% of total pipeline execution time (0.40% for state management and routing)
- QAOA's fourth-ranked portfolio (XOM+JPM+JNJ) achieved the highest Sharpe ratio (2.99) among all evaluated strategies
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim or demonstrate quantum advantage. All results are from quantum simulators (AWS Tensor Network and QBraid QIR state-vector), and the problem scale (5 assets) is classically trivial. The focus is on operational orchestration rather than quantum speedup or solution quality improvements over classical methods.
## Limitations
- Problem scale limited to 5 assets (5 qubits), which is classically trivial and does not demonstrate quantum advantage [inferred]
- Experiments conducted only on cloud quantum simulators (AWS Tensor Network and QBraid QIR), not on real quantum hardware, which may introduce noise and decoherence effects not accounted for
- Non-variational QAOA parameters used (analytically determined rotation angles from market data), which may not optimize solution quality as effectively as variational optimization
- Single-run evaluation without bootstrapped confidence intervals on financial metrics, limiting statistical robustness [inferred]
- Equal-weight allocation used for financial evaluation; optimal weights within selected asset subsets not considered [inferred]
- No error mitigation techniques applied, which could be critical for real hardware execution [inferred]
- No comparison with state-of-the-art classical solvers (e.g., branch-and-bound, heuristics) to benchmark quantum advantage [inferred]
- Pipeline execution performance dominated by cloud quantum job wait times (74.07% of total time), which may not scale efficiently for production use [inferred]
- No dynamic backend selection based on real-time availability, queue depth, or calibration data, which could optimize execution [inferred]
- Simulator-only execution may not reflect the impact of hardware noise on measurement distributions [inferred]
## Open questions
- How does the framework perform with larger asset universes (n ≥ 20) where classical methods struggle?
- What is the impact of hardware noise and decoherence on solution quality when executed on real quantum processors?
- Can variational optimization of QAOA parameters improve the measurement distribution quality compared to analytically determined angles?
- How does the agentic framework compare to classical solvers in terms of solution quality and runtime for industrially relevant problem sizes?
- What error mitigation techniques are most effective for this pipeline when executed on noisy quantum hardware?
- How does the pipeline handle dynamic market conditions, such as sudden changes in asset correlations or returns?
- What is the scalability of the agentic overhead as the number of assets or pipeline complexity increases?
- Can the framework be extended to multi-period portfolio optimization or other financial use cases beyond static mean-variance optimization?

**Future work:**
- Extend the framework to larger asset universes (n ≥ 20) using correlation-based decomposition techniques
- Incorporate a variational outer loop to optimize QAOA parameters for improved solution quality
- Execute the pipeline on real quantum hardware (e.g., IBM Quantum, IonQ) to assess noise impact and error mitigation strategies
- Compare performance with state-of-the-art classical solvers to benchmark quantum advantage
- Implement dynamic backend selection based on real-time availability, queue depth, and calibration data
- Add noise-aware quality gating using statistical divergence measures to improve robustness
- Extend the cost Hamiltonian to encode multi-objective optimization (e.g., Sharpe ratio directly)
- Explore multi-period portfolio optimization and other financial use cases
- Integrate classical post-processing techniques (e.g., gradient-based cardinality repair, local search) to refine quantum solutions
- Develop a benchmarking suite to evaluate the framework across different problem sizes, asset classes, and market conditions
## Key ideas
- #idea:near-term-feasibility — Agentic framework automates end-to-end quantum portfolio optimization using QAOA on cloud quantum simulators, demonstrating near-term applicability for small-scale problems
- #idea:hybrid-approach — Hybrid quantum-classical pipeline integrates AI agents for live data ingestion, quantum circuit construction, and financial interpretation, reducing manual overhead
- #idea:hybrid-approach — Maturity-gated governance model proposed to manage quantum resource permissions, enabling scalable and reproducible quantum workflows
- #limitation:simulation-only — All quantum executions performed on simulators (AWS Tensor Network and QBraid QIR), with no validation on real quantum hardware, limiting assessment of noise and decoherence effects
- #limitation:qubit-count — Framework limited to 5 assets (5 qubits), far below real-world portfolio sizes (hundreds/thousands of assets), constraining practical applicability
- #limitation:noise — No noise mitigation techniques applied, raising concerns about performance degradation on NISQ devices
- #limitation:no-empirical-validation — Lack of comparison with state-of-the-art classical portfolio optimization methods (e.g., branch-and-bound, heuristic solvers) to benchmark performance
## Contradictions
- #contradiction:classical-vs-quantum — Paper claims the framework is the first application of agentic AI orchestration to quantum optimization workflows, but this may overlap with emerging work in quantum MLOps (e.g., Qiskit Runtime, PennyLane)
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Yahoo Finance via yfinance Python library', 'size': '5 assets, approximately 252 trading days (one year)', 'features': ['daily closing prices', 'log-returns', 'annualized returns', 'covariance matrix'], 'preprocessing_steps': ['Daily log-returns computed as r_t = log(p_t / p_{t-1})', 'Annualized returns and risks calculated using 252 trading days convention', 'Covariance matrix derived from log-returns'], 'time_period': 'One year ending February 2026'}

### Process
1. Market data acquisition: Fetch one year of daily closing prices for five assets. 2. Data preprocessing: Compute log-returns, annualized returns, and covariance matrix. 3. Circuit construction: Encode annualized returns as single-qubit RZ rotations and pairwise covariance as ZZ interactions via CX-RZ-CX gate sequences. 4. Local pre-validation: Execute circuit on Qiskit BasicSimulator with 1000 shots. 5. Cloud submission: Submit identical Qiskit circuit to AWS Tensor Network simulator (1000 shots) and QBraid QIR state-vector simulator (2000 shots) via QBraid runtime. 6. Result polling: Monitor job status asynchronously at 5-second intervals. 7. Quality control: Compute normalized mean of measurement distribution and accept results with mean > 0. 8. Financial interpretation: Decode bitstrings into portfolio selections and compute metrics (annualized return, volatility, Sharpe ratio).

### Output
{'metrics_reported': ['Normalized measurement distribution mean', 'Portfolio annualized return', 'Portfolio volatility', 'Sharpe ratio', 'Bitstring frequency and probability'], 'comparison_baselines': ['Equal-weight portfolio (all five assets)', 'Best single asset (XOM)', 'Worst single asset (AAPL)', 'Random 3-asset portfolio (average)', 'Minimum variance portfolio (JPM only)'], 'output_format': 'JSON artifact containing job descriptor, market data snapshot, measurement counts, financial metrics, and provenance metadata.'}

### Parameters
- qubits: 5
- circuit_layers: 5
- shots_aws: 1000
- shots_qbraid: 2000
- optimizer: Analytical (data-driven parameterization)
- trade_off_parameter_lambda: 0.5
- return_encoding: RZ rotations scaled by annualized returns (γᵢ = l · μᵢ · π)
- covariance_encoding: ZZ interactions via CX-RZ-CX (γᵢⱼ = l · Cᵢⱼ · π / 2)
- mixer_angles: RX rotations (βᵢ = l · 0.4 · π / p)

### Hardware
{'simulators': [{'name': 'AWS Tensor Network simulator', 'provider': 'AWS', 'backend_id': 'aws:aws:sim:tn1', 'shots': 1000}, {'name': 'QBraid QIR state-vector simulator', 'provider': 'QBraid', 'backend_id': 'qbraid:qbraid:sim:qir-sv', 'shots': 2000}], 'local_simulator': 'Qiskit BasicSimulator', 'transpilation': 'Handled internally by QBraid runtime for cloud submissions'}

### Reproducibility
Code and framework details are described in sufficient detail for replication. Market data is publicly available via Yahoo Finance. The QBraid runtime provides a vendor-agnostic interface for cloud quantum execution. The paper includes circuit parameterization details, gate counts, and financial metrics. However, the exact LangGraph agent implementations and QBraid-specific configurations are not fully open-sourced in the paper.
