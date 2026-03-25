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
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
methodology_tags:
- QAOA
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:14:49.739436'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:15:00.370633'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:37.349731'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:16.353968'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:16:49.213072'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:17:00.895014'
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
- method/QAOA
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
topic_tags:
- portfolio-optimisation
year: 2026
zotero_key: ''
---

## Abstract summary
The paper proposes an agent-based workflow for end-to-end quantum portfolio optimization that integrates live market data ingestion, QAOA circuit construction, backend selection, job management, and financial interpretation. Eight specialized agents are coordinated via a LangGraph state machine and execute QAOA-based optimization on cloud quantum simulators accessed through the QBraid runtime. The work focuses on making quantum portfolio optimization operationally reproducible and vendor-agnostic, including governance mechanisms for quantum resource usage and cross-platform validation of measurement distributions.
## Methodology
This preprint presents an empirical systems-and-algorithm demonstration of an agentic workflow for quantum portfolio optimization. The authors build an end-to-end directed acyclic graph (DAG) pipeline using LangGraph with eight specialized agents covering policy enforcement, task planning, QAOA circuit construction, local simulation pre-validation, cloud backend selection and submission, asynchronous polling, statistical quality control, and artifact aggregation. The financial optimization problem is formulated as a 5-asset binary mean-variance portfolio selection problem with trade-off parameter lambda = 0.5, mapped to a QUBO/QAOA representation where single-qubit RZ angles are derived from annualized returns and two-qubit ZZ interactions from empirical covariance entries. Rather than variationally optimizing QAOA parameters, the circuit uses analytically data-driven layer-wise schedules over p = 5 layers. Experiments use one year of Yahoo Finance daily price data for AAPL, XOM, JPM, JNJ, and GLD, transformed into daily log-returns and annualized returns/covariances. The workflow is first pre-validated locally, then executed through the QBraid runtime on two cloud simulators to test cross-platform consistency. Outputs are evaluated using measurement-distribution statistics, dominant bitstring frequency relative to a uniform baseline, and decoded portfolio finance metrics including annualized return, volatility, and Sharpe ratio, with comparisons against equal-weight, single-asset, random 3-asset, and classical minimum-variance benchmarks. The paper is explicitly a preprint and not peer reviewed.

**Algorithms used:** QAOA
**Frameworks:** LangGraph, Qiskit, QBraid SDK, yfinance, Qiskit Aer, Qiskit BasicSimulator

**Experimental setup:** The pipeline was implemented as a LangGraph StateGraph with eight agents and three conditional routers. Quantum circuits were constructed in Qiskit and submitted through the QBraid unified runtime. Local pre-validation used Qiskit BasicSimulator (with fallback options including Qiskit Aer AerSimulator and a weighted random bitstring generator). Cloud execution was performed on two simulators: AWS Tensor Network simulator (aws:aws:sim:tn1) with 1000 shots and QBraid QIR state-vector simulator (qbraid:qbraid:sim:qir-sv) with 2000 shots. The problem instance used 5 qubits and 5 QAOA layers; the compiled circuit had 210 gates, transpiled depth 93, and 214 OpenQASM 2.0 instructions. Polling was performed every 5 seconds for up to 60 attempts.

**Dataset:** Live Yahoo Finance market data for five assets spanning technology, energy, finance, healthcare, and commodities: AAPL, XOM, JPM, JNJ, and GLD. The study used approximately one year of daily closing prices ending February 2026, from which daily log-returns, annualized returns, annualized risks, and the annualized covariance matrix were computed.
## Findings
- [supported] The paper presents an eight-agent, DAG-based orchestration framework for end-to-end quantum portfolio optimization, covering policy enforcement, task planning, QAOA circuit construction, local validation, cloud submission, polling, quality control, and artifact generation.
- [supported] The implemented QAOA workflow used live Yahoo Finance data for a 5-asset universe (AAPL, XOM, JPM, JNJ, GLD), with single-qubit rotation angles derived from annualized returns and two-qubit interaction strengths derived from pairwise covariances.
- [supported] The full pipeline was executed on two cloud simulators via QBraid: AWS Tensor Network simulator (1000 shots) and QBraid QIR state-vector simulator (2000 shots).
- [supported] Cross-platform execution produced nearly identical normalized measurement means of 0.6712 and 0.6713, with local simulation also at 0.6713, indicating negligible distributional shift across the tested simulator backends.
- [supported] The dominant measured bitstring on the QBraid QIR simulator was 01011, corresponding to the portfolio AAPL+XOM+JNJ, appearing in 23.55% of shots versus a uniform baseline of 3.125%.
- [supported] The dominant portfolio AAPL+XOM+JNJ achieved an annualized return of 31.17%, volatility of 19.29%, and Sharpe ratio of 1.62 under the paper's equal-weight evaluation method.
- [supported] The top-5 measured bitstrings accounted for 67.60% of all measurements on the QBraid QIR simulator, compared with a uniform expectation of 15.63%, showing a strongly non-uniform sampled distribution.
- [supported] Among the evaluated sampled portfolios, the fourth-ranked QAOA bitstring (XOM+JPM+JNJ) achieved the highest reported Sharpe ratio of 2.99, exceeding the equal-weight all-asset benchmark Sharpe ratio of 2.41.
- [supported] The agentic orchestration overhead was reported as 0.108 seconds or 0.40% of total AWS TN1 pipeline runtime, with cloud job wait time dominating total execution time.
- [supported] The framework includes a maturity-gated governance model that restricts backend access and shot budgets by lifecycle stage, intended to prevent unnecessary paid hardware usage during development.
- [speculative] The authors claim this is the first application of agentic AI orchestration to quantum optimization workflows, but this novelty claim is not empirically verifiable within the paper itself.
- [speculative] The framework is argued to be reproducible, vendor-agnostic, and suitable as a practical foundation for integrating quantum optimization into financial decision workflows, but this is demonstrated only on small-scale simulator-based experiments.
- [speculative] The authors suggest the architecture could become more valuable at larger problem sizes (e.g., n >= 20 assets) and as quantum hardware scales, but no large-scale or real-hardware evidence is provided.
- [speculative] The paper implies that covariance-aware QAOA encoding can drive financially interpretable inclusion/exclusion decisions, though this is shown only on a 5-asset toy-scale instance without repeated trials or statistical confidence intervals.
- [speculative] Any implication of quantum advantage is unproven because the study uses only simulators on a classically trivial 5-asset problem and does not benchmark against strong classical optimizers on equivalent objectives.

**Results summary:** This preprint proposes an agentic orchestration framework for quantum portfolio optimization and demonstrates it on a 5-asset binary portfolio selection problem using a QAOA circuit parameterized from live Yahoo Finance data. The workflow was executed end-to-end on two QBraid-accessed cloud simulators and one local simulator, with nearly identical normalized measurement means (0.6712-0.6713), suggesting consistent simulator-side transpilation and execution. On the 2000-shot QBraid QIR run, the most frequent bitstring, 01011 (AAPL+XOM+JNJ), occurred with 23.55% probability and yielded a reported annualized return of 31.17%, volatility of 19.29%, and Sharpe ratio of 1.62. The top-5 bitstrings captured 67.60% of shots, and one sampled portfolio (XOM+JPM+JNJ) achieved the highest reported Sharpe ratio of 2.99. The paper's main contribution is architectural rather than algorithmic, emphasizing low orchestration overhead (<0.5% of runtime) and governance controls, but all experiments are simulator-based and conducted on a classically trivial small instance, so broader claims about practical quantum benefit remain speculative.

**Performance claims:**
- Normalized measurement mean 0.6712 on AWS TN1 simulator (1000 shots)
- Normalized measurement mean 0.6713 on QBraid QIR state-vector simulator (2000 shots)
- Normalized measurement mean 0.6713 on local Qiskit BasicSimulator (1000 shots)
- Cross-platform normalized means agree within 0.0001 across three environments
- Dominant bitstring 01011 observed in 23.55% of 2000 shots
- Uniform baseline probability for any 5-bit string is 3.125%, making the dominant bitstring 7.6x above baseline
- Dominant portfolio AAPL+XOM+JNJ: annualized return 31.17%, volatility 19.29%, Sharpe ratio 1.62
- Second-ranked portfolio AAPL+XOM+JPM+JNJ: annualized return 34.52%, volatility 16.43%, Sharpe ratio 2.10
- Fourth-ranked portfolio XOM+JPM+JNJ: annualized return 41.65%, volatility 13.92%, Sharpe ratio 2.99
- Top-5 bitstrings account for 67.60% of measurements versus 15.63% uniform expectation
- AWS TN1 wall-clock runtime 27.0 s; QBraid QIR runtime 14.2 s
- AWS TN1 job wait time 20.0 s; QBraid QIR job wait time 10.0 s
- Agentic overhead 0.108 s or 0.40% of total AWS TN1 pipeline runtime
- Compiled circuit depth 93 with 210 gates and 214 OpenQASM instructions for n=5, p=5
## Quantum advantage claim
**Classification:** speculative

As a preprint, any advantage claim defaults to speculative. The study uses only simulators, not physical quantum hardware, on a 5-asset problem that is classically enumerable. It shows workflow feasibility and cross-simulator consistency, but does not demonstrate computational speedup or superior solution quality over classical state-of-the-art methods.
## Limitations
- Lack of peer review: the paper is a preprint and its claims have not yet undergone formal peer review.
- Problem scale is limited to n = 5 assets (5 qubits), which the authors acknowledge is classically trivial and mainly serves as a controlled testbed.
- The QAOA implementation uses analytically determined rotation angles rather than variationally optimized parameters, which may limit solution quality.
- Cloud execution was performed only on simulators, not on physical QPU hardware, so hardware noise and real-device effects were not evaluated.
- Results are based on single-run evaluations; the authors note that a more thorough assessment would require multiple runs and bootstrapped confidence intervals.
- Financial evaluation assumes equal-weight allocation among selected assets rather than optimizing continuous portfolio weights.
- [inferred] The empirical study uses only five assets from a single one-year historical window, limiting external validity across market regimes, asset universes, and time periods.
- [inferred] No comparison is provided against state-of-the-art classical optimization baselines beyond simple benchmark strategies, so relative computational or financial advantage is unclear.
- [inferred] The study does not demonstrate any quantum advantage; the tested instance is too small and simulator-based to support such claims.
- [inferred] The quality-control threshold (normalized mean > 0) is extremely weak and may fail to detect subtle but practically important errors or degraded solution quality.
- [inferred] The fallback strategy to random bitstring generation and local simulation may preserve pipeline continuity but can mask failures in the actual quantum execution path.
- [inferred] The use of live Yahoo Finance/yfinance data may reduce reproducibility over time unless exact snapshots are archived and made accessible.
- [inferred] Cross-platform validation is limited to two simulator backends with nearly ideal behavior; this does not establish robustness across heterogeneous noisy hardware.
- [inferred] The chosen hyperparameters, including p = 5, lambda = 0.5, and mixer coefficient 0.4, appear fixed and only lightly justified, leaving sensitivity to parameter choices untested.
- [inferred] The unconstrained binary inclusion formulation omits realistic portfolio constraints such as cardinality, budget, turnover, transaction costs, and regulatory constraints.
- [inferred] The architecture relies on several software layers and external services (LangGraph, QBraid, Qiskit, Yahoo Finance), which may introduce dependency and reproducibility risks not systematically assessed.
## Open questions
- How well does the agentic framework scale to larger portfolio instances such as n >= 20 assets and beyond?
- How would the workflow perform on physical quantum hardware with realistic noise, decoherence, queue delays, and calibration drift?
- Would adding a variational outer loop materially improve the quality of the measurement distribution and resulting portfolios?
- How should backend selection be optimized in real time using device availability, queue depth, cost, and calibration data?
- What quality-gating metrics are most appropriate for distinguishing useful quantum outputs from noisy or failed runs?
- How robust are the reported portfolio selections to different market windows, asset universes, and changing covariance structures?
- How sensitive are results to the chosen QAOA depth, mixer schedule, and risk-return trade-off parameter lambda?
- Can the framework support realistic constrained portfolio optimization problems, including fixed cardinality or transaction-cost-aware formulations?
- Does the orchestration framework remain efficient and manageable when multiple subproblems or parallel quantum jobs are introduced?
- How reproducible are the results when rerun at different times with updated live data or under different cloud backend conditions?

**Future work:**
- Incorporate a variational outer loop around the AutoCircuitDesigner to optimize QAOA parameters.
- Extend the Planner with correlation-based decomposition for large asset universes, potentially with parallel QPUBroker instances.
- Implement dynamic backend selection based on real-time availability, queue depth, and calibration data.
- Develop noise-aware quality gating using stronger statistical divergence measures.
- Design multi-objective cost Hamiltonians that encode the Sharpe ratio directly.
- Execute the workflow on physical QPU hardware and evaluate the need for error mitigation techniques.
- Perform repeated-run experiments with bootstrapped confidence intervals for financial and algorithmic metrics.
- Move beyond equal-weight evaluation by solving for optimal weights within the selected asset subset.
- Test the framework on larger and more realistic portfolio universes to assess scalability and practical relevance.
- [inferred] Benchmark the framework against stronger classical solvers and hybrid classical-quantum baselines on identical instances.
- [inferred] Evaluate robustness across multiple historical periods, stress regimes, and broader asset classes.
- [inferred] Study hyperparameter sensitivity for circuit depth, mixer strength, shot count, and risk-aversion settings.
- [inferred] Add realistic financial constraints such as cardinality, budget, turnover, and transaction costs to the optimization formulation.
## Key ideas
- #idea:near-term-feasibility — Demonstrates an end-to-end agent-based QAOA workflow for binary mean-variance portfolio optimisation using live Yahoo Finance data and cloud-accessed simulators.
- #idea:hybrid-approach — Uses a hybrid quantum-classical orchestration stack with LangGraph agents for data ingestion, circuit construction, backend selection, job management, quality control, and financial interpretation.
- #idea:hybrid-approach — Emphasizes operational reproducibility, vendor-agnostic execution, and governance controls such as maturity-gated backend access and shot-budget restrictions.
- #idea:near-term-feasibility — Shows cross-simulator consistency of measurement distributions across local and cloud simulators, suggesting the workflow is operationally stable at toy scale.
- #idea:near-term-feasibility — QAOA-sampled portfolios achieved competitive Sharpe ratios versus simple benchmark portfolios on the small test instance, though not against strong classical optimizers.
## Contradictions
- The paper presents the workflow as a practical foundation for quantum portfolio optimisation, but its evidence is entirely simulator-based on a classically trivial 5-asset instance, contradicting any implicit suggestion of quantum superiority over classical methods.
- The architecture is framed as scalable to larger portfolio sizes, yet no empirical results beyond 5 qubits are provided; this conflicts with broader claims about applicability to realistic portfolio optimisation problems.
- The paper highlights near-term operational feasibility, but absence of physical hardware experiments means the conclusions do not account for noise, calibration drift, or queue variability that could materially change performance on real QPUs.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Yahoo Finance daily closing prices for 5 assets (AAPL, XOM, JPM, JNJ, GLD), approximately 252 trading days over a trailing one-year window ending February 2026. Preprocessing: daily log-returns computed as r_t = log(p_t / p_{t-1}); returns and covariance annualized using a 252-trading-day convention. Features used in the quantum encoding were annualized expected returns per asset and pairwise annualized covariance entries.

### Process
1. Fetch one year of daily closing prices via yfinance for the 5 selected assets. 2. Compute daily log-returns and annualize returns and covariance matrix. 3. Formulate the binary mean-variance portfolio optimization problem with lambda = 0.5. 4. Build a 5-qubit, 5-layer QAOA circuit in Qiskit: initialize with Hadamards; for each layer l, apply single-qubit return-encoding RZ rotations with gamma_i^(l) = l * mu_i * pi; apply pairwise covariance encoding using CX-RZ-CX with gamma_ij^(l) = l * C_ij * pi / 2; apply mixer RX rotations with beta_i^(l) = l * 0.4 * pi / p. 5. Transpile the circuit (reported depth 93). 6. Run local pre-validation in the SimulationSandbox using BasicSimulator with 1000 shots and assess whether the measurement distribution is non-trivial. 7. Submit the same circuit through QBraid to cloud simulators, using 1000 shots on AWS TN1 and 2000 shots on QBraid QIR. 8. Poll job status every 5 seconds up to 60 attempts until completion. 9. Extract measurement counts, compute normalized mean of the measurement distribution, and apply a quality gate accepting results with mean > 0. 10. Decode measured bitstrings into equal-weight portfolios over selected assets and compute annualized return, volatility, and Sharpe ratio. 11. Compare top measured portfolios against benchmark strategies and assess cross-platform consistency of measurement distributions.

### Output
Reported outputs include normalized measurement distribution mean, dominant and top-k bitstring frequencies/probabilities, cross-platform consistency across local and cloud simulators, job timing and pipeline overhead, and decoded financial metrics for selected portfolios. Main metrics include normalized mean (0.6712-0.6713 across environments), dominant bitstring probability (23.55% for 01011), concentration relative to the uniform baseline (3.125%), annualized portfolio return, annualized volatility, and Sharpe ratio. Baseline comparisons include equal-weight all-5 portfolio, best single asset, worst single asset, average random 3-asset portfolio, and a classical minimum-variance strategy.

### Parameters
- qubits: 5
- qaoa_layers: 5
- lambda: 0.5
- mixer_coefficient: 0.4
- shots_local_prevalidation: 1000
- shots_aws_tn1: 1000
- shots_qbraid_qir_sv: 2000
- compiled_circuit_depth: 93
- total_gates: 210
- openqasm_instructions: 214
- poll_interval_seconds: 5
- max_poll_attempts: 60
- quality_gate_threshold: normalized mean > 0
- return_encoding: gamma_i^(l) = l * mu_i * pi
- covariance_encoding: gamma_ij^(l) = l * C_ij * pi / 2
- mixer_schedule: beta_i^(l) = l * 0.4 * pi / p

### Hardware
No physical QPU was used despite the broader framing; experiments were run on simulators. Local pre-validation used Qiskit BasicSimulator, with fallback options including Qiskit Aer AerSimulator. Cloud execution used QBraid runtime on aws:aws:sim:tn1 (AWS Tensor Network simulator) and qbraid:qbraid:sim:qir-sv (QBraid QIR state-vector simulator). The paper states that QBraid handled transpilation internally for cloud submission, while Qiskit transpiler reported compiled circuit depth 93.

### Reproducibility
Preprint. Data source is public and clearly identified (Yahoo Finance via yfinance), and the paper provides substantial methodological detail on circuit construction, agent workflow, and execution settings. However, no public code repository or exact implementation artifacts are mentioned in the provided text, so full replication is plausible but not turnkey.
