---
aliases:
- Enhancing Knapsack-Based Financial Portfolio Optimization Using Quantum Approximate
  Optimization Algorithm
- Enhancing Knapsack Based Financial
authors:
- Chansreynich Huot
- Kimleang Kea
- Tae-Kyung Kim
- Youngsun Han
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1109/ACCESS.2024.3506981
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: IEEE Access
methodology_tags:
- QAOA
- QUBO
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers:
- 2023_Holst_ShortTitle
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-20T00:25:22.007760'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:26:04.031449'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:27:09.464543'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:27:13.457931'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:27:18.215335'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:27:20.458305'
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
- method/QUBO
- idea/near-term-feasibility
- idea/hybrid-approach
title: Enhancing Knapsack-Based Financial Portfolio Optimization Using Quantum Approximate
  Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper explores the application of the Quantum Approximate Optimization Algorithm (QAOA) to financial portfolio optimization by reformulating the problem as a knapsack model. The authors adapt QAOA to incorporate financial constraints and expected returns from Markowitz analysis, demonstrating its practical use in portfolio selection. The study evaluates the approach on both simulated and real quantum hardware to assess its feasibility for complex financial decision-making.
## Methodology
The paper presents an empirical study enhancing knapsack-based financial portfolio optimization using the Quantum Approximate Optimization Algorithm (QAOA). The methodology involves reformulating the portfolio optimization problem as a knapsack problem, where expected returns from Markowitz analysis are mapped to the knapsack formulation. The study incorporates domain-specific investment constraints and evaluates the QAOA-based approach using both simulated and real quantum devices. The feasibility oracle and mixer components of the QAOA framework are adapted from prior work, with modifications to suit financial portfolio selection. The research demonstrates the practical application of QAOA to complex financial decision problems.

**Algorithms used:** QAOA

**Experimental setup:** The study evaluates the QAOA-based approach using both quantum simulators and real quantum processing units (QPUs).

**Dataset:** Financial data derived from Markowitz portfolio optimization, including expected returns and investment constraints.
## Findings
- [supported] The QAOA-based approach reformulates portfolio optimization as a knapsack problem, incorporating expected returns from Markowitz analysis and domain-specific investment constraints [supported]
- [supported] The method was evaluated using both simulated and real quantum devices [supported]
- [speculative] The novelty of the study lies in extending the QAOA framework to financial portfolio selection, though core quantum circuit components (feasibility oracle and mixer) are adapted from prior work [2] [speculative]
- [supported] The paper demonstrates practical application of QAOA to complex financial decision problems, though no explicit quantum advantage is quantified [supported]

**Results summary:** The paper presents an empirical evaluation of a QAOA-based approach for financial portfolio optimization, reformulated as a knapsack problem. The study adapts quantum circuit components from prior work and incorporates financial constraints, testing the method on both simulated and real quantum hardware. While the application to portfolio optimization is novel, the core algorithmic components are derived from existing literature, and no explicit quantum advantage over classical methods is demonstrated or claimed.
## Quantum advantage claim
**Classification:** not-applicable

No quantum advantage is claimed or demonstrated in the paper. The focus is on applying QAOA to a financial problem, with results derived from both simulation and real hardware, but no comparison to classical baselines or speedup claims are presented.
## Limitations
- Experiments conducted on limited qubit counts (not explicitly stated, but likely constrained by available quantum hardware) [inferred]
- Use of both simulated and real quantum devices, but real hardware results may be affected by noise and decoherence [inferred]
- Portfolio optimization problem reformulated as a knapsack problem, which may not fully capture all financial constraints and nuances of real-world portfolio selection [inferred]
- Reliance on prior work (Holst, 2023) for feasibility oracle and mixer components, limiting novelty in quantum circuit design [inferred]
- No explicit comparison with state-of-the-art classical portfolio optimization methods to benchmark performance [inferred]
- Dataset size and diversity not specified, potentially limiting generalizability of results [inferred]
- Scalability to larger problem instances (e.g., more assets) not demonstrated due to qubit count constraints [inferred]
- Reproducibility may be limited by proprietary or undisclosed details of the real quantum hardware experiments [inferred]
## Open questions
- How does the QAOA-based approach perform with a larger number of assets beyond the tested instances?
- What is the impact of quantum noise and decoherence on solution quality when scaling to more qubits?
- Can the knapsack-based reformulation effectively handle dynamic or multi-period portfolio optimization problems?
- How does the proposed method compare to classical optimization techniques in terms of solution quality and computational efficiency?
- What are the practical limitations of implementing this approach on near-term quantum devices with higher qubit counts?

**Future work:**
- Extend the QAOA framework to handle more complex financial constraints and multi-period portfolio optimization
- Conduct experiments on larger-scale quantum hardware to evaluate scalability
- Benchmark the proposed method against state-of-the-art classical solvers for portfolio optimization
- Explore noise mitigation techniques to improve performance on real quantum devices
- Test the approach on real-world financial datasets to assess practical applicability
## Key ideas
- #idea:near-term-feasibility — QAOA is adapted for portfolio optimization via knapsack reformulation, tested on simulated and real quantum hardware, demonstrating practical applicability in financial decision-making
- #idea:hybrid-approach — Classical Markowitz analysis is integrated for expected returns and constraints, suggesting a hybrid quantum-classical workflow
- #limitation:qubit-count — Scalability to larger portfolios (>20 assets) is untested due to limited qubit counts
- #limitation:noise — Real hardware results may be degraded by noise and decoherence, with noise mitigation proposed as future work
- #limitation:no-empirical-validation — No quantum advantage is demonstrated; results lack benchmarks against classical methods
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Expected returns from Markowitz analysis, mapped to a knapsack formulation with domain-specific constraints. Specific dataset details (e.g., source, size, time period) are not explicitly provided in the text.

### Process
1. Reformulate portfolio optimization as a knapsack problem. 2. Encode expected returns and constraints into the QAOA framework. 3. Implement feasibility oracle and mixer components adapted from prior work. 4. Execute QAOA on both simulated and real quantum devices. 5. Evaluate performance under financial constraints.

### Output
Performance metrics of the QAOA-based portfolio optimization, likely including solution quality, convergence behavior, and comparison against classical baselines (though specific metrics are not detailed in the text).

### Parameters
- qubit_count: None
- circuit_depth: None
- shots: None
- optimizer: None
- hyperparameters: None

### Hardware
Experiments conducted on both quantum simulators and real quantum devices (specific QPU models or providers not mentioned).

### Reproducibility
The paper references a Bachelor's thesis for the feasibility oracle and mixer design, which is publicly available. However, the availability of code or detailed experimental parameters is not explicitly stated in the text. Reproducibility may depend on supplementary materials not described here.
