---
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
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T21:03:27.704734'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T21:03:30.189113'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T21:03:44.649133'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T21:04:00.421041'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T21:04:25.143644'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T21:04:29.211371'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
title: 'Autonomous Quantum Agents for Portfolio Optimization: Orchestrating QAOA Workflows
  on Cloud Quantum Simulators'
topic_tags:
- portfolio-optimisation
year: 2026
zotero_key: ''
---

## Abstract summary
This preprint introduces an agentic framework that automates end-to-end portfolio optimization using quantum computing, bridging the gap between quantum algorithms and practical deployment in financial services. The system employs specialized AI agents to manage tasks such as live market data ingestion, quantum circuit construction, cloud-based quantum hardware execution, and financial interpretation of results. The approach aims to enhance reproducibility, scalability, and governance in quantum optimization workflows for near-term quantum infrastructure.
## Methodology
The paper presents an empirical agentic framework for end-to-end portfolio optimization that integrates autonomous AI workflow orchestration with quantum approximate optimization. The methodology employs a directed acyclic graph (DAG) state machine built on the LangGraph framework, comprising eight specialized agents, each handling distinct stages of the quantum optimization pipeline: policy enforcement, task decomposition, QAOA circuit construction from live market data, local pre-validation, cloud QPU submission, quality assurance, and financial interpretation. The quantum core implements a Quantum Approximate Optimization Algorithm (QAOA) where single-qubit rotation angles are derived from empirical annualized asset returns and two-qubit interaction strengths from pairwise covariance entries. The framework introduces a maturity-gated governance model to manage quantum resource permissions and ensures vendor-agnostic execution via the QBraid runtime platform. Experiments were conducted using live Yahoo Finance data for a five-asset universe, with the QAOA pipeline executed on two cloud quantum simulators: the AWS Tensor Network simulator and the QBraid QIR state-vector simulator.

**Algorithms used:** QAOA
**Frameworks:** LangGraph, Qiskit, QBraid, QBraid runtime, yfinance

**Experimental setup:** The experimental setup involved executing the QAOA pipeline on two cloud quantum simulators through the QBraid unified runtime platform: the AWS Tensor Network simulator (aws:aws:sim:tn1, 1000 shots) and the QBraid QIR state-vector simulator (qbraid:qbraid:sim:qir-sv, 2000 shots). The QAOA circuit was constructed with 5 qubits and 5 layers, using live market data for parameterization. Local pre-validation was performed using Qiskit Aer AerSimulator and BasicSimulator as fallbacks. The agentic overhead constituted less than 2% of total pipeline execution time.

**Dataset:** Live Yahoo Finance data for five assets spanning technology, energy, finance, healthcare, and commodities (AAPL, XOM, JPM, JNJ, GLD). The dataset includes one year of daily closing prices (approximately 252 trading days, ending February 2026), from which annualized returns and covariance matrices were computed using daily log-returns.
## Findings
- [supported] The agentic framework for portfolio optimization using QAOA on cloud quantum simulators achieved consistent normalized measurement distribution means of 0.6712 and 0.6713 on AWS Tensor Network and QBraid QIR state-vector simulators, respectively
- [supported] The dominant measured bitstring (01011) appeared in 23.55% of shots, 7.6 times the uniform baseline probability, corresponding to a portfolio with an annualized return of 31.17%, volatility of 19.29%, and Sharpe ratio of 1.62
- [supported] The agentic overhead constituted less than 2% of total pipeline execution time, demonstrating efficient orchestration
- [supported] The framework executed a 5-asset portfolio optimization using live Yahoo Finance data, with QAOA circuit parameters derived directly from empirical annualized returns and covariance matrices
- [speculative] The agentic framework could scale to larger asset universes (e.g., 20+ assets) by leveraging decomposition techniques similar to those in prior work, though this was not empirically validated in the paper
- [speculative] The maturity-gated governance model could prevent inadvertent hardware expenditure in production environments, but its effectiveness was not tested in real-world financial workflows
- [speculative] The cross-platform consistency observed in simulations suggests vendor-agnostic deployment is feasible, but this claim requires validation on real quantum hardware
- [supported] The QAOA circuit for 5 assets and 5 layers required 210 gates with a compiled depth of 93, as reported by the Qiskit transpiler

**Results summary:** The paper presents an agentic framework for end-to-end portfolio optimization using QAOA on cloud quantum simulators. The system automates the pipeline from live market data ingestion to financially interpreted quantum optimization results, employing eight specialized agents coordinated via a DAG state machine. Experimental results on a 5-asset universe (AAPL, XOM, JPM, JNJ, GLD) demonstrated consistent performance across two cloud simulators, with the dominant portfolio achieving a 31.17% annualized return and a Sharpe ratio of 1.62. The framework introduces a maturity-gated governance model to manage quantum resource permissions and achieves low overhead (<2%). While the results are promising, all quantum executions were performed on simulators, and scalability to larger asset universes remains speculative.

**Performance claims:**
- Normalized measurement distribution means of 0.6712 (AWS Tensor Network simulator) and 0.6713 (QBraid QIR state-vector simulator)
- Dominant bitstring (01011) appeared in 23.55% of shots (7.6x uniform baseline)
- Portfolio annualized return: 31.17%
- Portfolio volatility: 19.29%
- Portfolio Sharpe ratio: 1.62
- Agentic overhead: <2% of total pipeline execution time
- QAOA circuit for 5 assets and 5 layers: 210 gates, depth 93
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage; all results are from simulations. The authors speculate that the framework could enable quantum advantage for larger asset universes (e.g., 20+ assets) by leveraging decomposition techniques, but this is not empirically supported in the work.
## Limitations
- Experiments limited to a small asset universe (5 assets), which does not reflect real-world portfolio optimization scenarios with hundreds or thousands of assets
- Only tested on cloud quantum simulators (AWS Tensor Network and QBraid QIR state-vector), not real quantum hardware; performance on NISQ devices may differ significantly due to noise and decoherence [inferred]
- Lack of peer review as this is a preprint, which may affect the rigor and validity of the findings [inferred]
- No comparison with state-of-the-art classical portfolio optimization methods (e.g., branch-and-bound, heuristic solvers) to benchmark quantum advantage [inferred]
- QAOA circuit depth (93) and gate count (210) may not be feasible on current NISQ devices with limited coherence times [inferred]
- No noise mitigation techniques (e.g., error correction, dynamical decoupling) were applied, which could degrade performance on real hardware [inferred]
- Fixed trade-off parameter (λ = 0.5) may not generalize to all market conditions or investor risk preferences [inferred]
- Agentic framework overhead (2% of pipeline execution time) may increase with larger asset universes or more complex workflows [inferred]
- No evaluation of the framework's scalability to larger qubit counts (e.g., 20+ qubits) or more complex financial models (e.g., multi-period optimization) [inferred]
- Live market data from Yahoo Finance may not be representative of all financial markets or time periods [inferred]
- No analysis of the impact of data staleness or missing data on the QAOA parameterization and results [inferred]
- Maturity-gated governance model assumes a linear progression of job lifecycle stages, which may not reflect real-world deployment complexities [inferred]
## Open questions
- How does the agentic framework perform with larger asset universes (e.g., 20+ assets) and more complex financial models?
- What is the impact of hardware noise and decoherence on the QAOA solution quality when executed on real quantum devices?
- Can the framework be extended to handle cardinality-constrained portfolio optimization (e.g., selecting exactly K assets from n)?
- How does the performance of the QAOA-based approach compare to classical solvers (e.g., heuristic methods) for industrially relevant problem sizes?
- What are the trade-offs between circuit depth, shot count, and solution quality in the context of portfolio optimization?
- How sensitive is the framework to variations in market data (e.g., different time periods, asset classes, or correlation structures)?
- Can the agentic workflow be adapted to other quantum algorithms (e.g., digitized counterdiabatic optimization) for portfolio optimization?
- What are the implications of the maturity-gated governance model for production deployment in financial institutions?

**Future work:**
- Test the framework on real quantum hardware (e.g., IBM Quantum, IonQ, Rigetti) to evaluate performance under noise and decoherence
- Extend the asset universe to larger sizes (e.g., 20+ assets) and evaluate scalability of the agentic workflow
- Incorporate noise mitigation techniques (e.g., error correction, dynamical decoupling) to improve performance on NISQ devices
- Compare the QAOA-based approach with classical portfolio optimization methods (e.g., branch-and-bound, heuristic solvers) to benchmark quantum advantage
- Explore the use of alternative quantum algorithms (e.g., digitized counterdiabatic optimization) within the agentic framework
- Extend the framework to handle cardinality-constrained portfolio optimization and multi-period optimization models
- Evaluate the framework's robustness to variations in market data (e.g., different time periods, asset classes, or correlation structures)
- Investigate the integration of the agentic framework with existing financial decision-making workflows in production environments
- Develop a more dynamic maturity-gated governance model that adapts to real-world deployment complexities
- Assess the economic viability of the framework for large-scale portfolio optimization in terms of quantum resource costs and classical overhead
## Key ideas
- #idea:near-term-feasibility — Agentic framework automates end-to-end portfolio optimization using QAOA on cloud quantum simulators, demonstrating near-term applicability for small-scale problems
- #idea:hybrid-approach — Hybrid quantum-classical pipeline integrates AI agents for live data ingestion, quantum circuit construction, and financial interpretation, reducing manual overhead
- #limitation:simulation-only — All quantum executions performed on simulators (AWS Tensor Network and QBraid QIR), with no validation on real quantum hardware
- #limitation:qubit-count — Framework limited to 5 assets (5 qubits), far below real-world portfolio sizes (hundreds/thousands of assets)
- #limitation:noise — No noise mitigation techniques applied, raising concerns about performance on NISQ devices
- #idea:hybrid-approach — Maturity-gated governance model proposed to manage quantum resource permissions, though untested in production environments
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
