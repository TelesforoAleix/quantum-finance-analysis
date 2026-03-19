---
aliases:
- Portfolio Optimization Based on Quantum HHL Algorithm
- Portfolio Optimization Based Quantum
authors:
- Qinghai Li
- Hao Wu
- Weizhong Qian
- Xiaoyu Li
- Qinsheng Zhu
- Shan Yang
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1007/978-3-031-06788-4_8
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ICAIS 2022, LNCS 13339
methodology_tags:
- HHL
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T22:21:25.989424'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:21:28.942153'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:21:32.753234'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:21:39.804156'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:21:46.968815'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:22:24.547987'
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
- method/HHL
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Portfolio Optimization Based on Quantum HHL Algorithm
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
This paper explores the application of the quantum HHL algorithm to solve combinatorial optimization problems in financial portfolio management. The authors frame portfolio optimization as a quadratic programming problem with equality constraints and implement the HHL algorithm using IBM’s quantum computing platform. The study demonstrates the feasibility of quantum computing for accelerating such financial problems by comparing approximate quantum solutions with exact classical solutions.
## Methodology
The paper presents an empirical study applying the quantum HHL algorithm to solve portfolio optimization problems in finance. The research formulates the portfolio optimization problem as a quadratic programming problem with equality constraints, which is then transformed into a linear system of equations. The HHL algorithm is employed to solve this linear system on a quantum computing platform. The methodology involves several stages: quantum phase estimation (QPE), controlled rotation, uncompute, and measurement. The study implements the algorithm using the Qiskit package on IBM's quantum computing platform. A specific financial model with three assets is constructed, and the HHL algorithm is applied to find an approximate solution to the portfolio allocation problem. The results are compared with the exact classical solution to evaluate the accuracy and feasibility of the quantum approach.

**Algorithms used:** HHL
**Frameworks:** Qiskit

**Experimental setup:** The experiments were conducted using IBM's quantum computing platform via the Qiskit package. The HHL algorithm circuit was constructed with 9 qubits, including qubits for phase estimation, controlled rotation, and ancilla bits. The phase estimation stage was set to estimate the probability of success at 0.9 with 2 estimation bits. The quantum simulator was used to execute the circuit and measure the output states.

**Dataset:** A synthetic financial dataset was used, assuming three assets with average profit rates μT = (0.05, 0.1, 0.2), asset allocation vector ⃗PT = (1, 1, 1), and a correlation matrix  = [[1, 0.5, 0], [0.5, 1, 0.1], [0, 0.1, 1]]. The expected return was set to μ0 = 0.15, and the total investment cost was ξ = 1. The input vector for the linear system was expanded to 8 dimensions to fit the qubit requirements.
## Findings
- [supported] The HHL algorithm was implemented using Qiskit on IBM’s quantum computing platform to solve a portfolio optimization problem modeled as a quadratic programming problem with equality constraints
- [supported] The approximate solution obtained via the HHL algorithm closely matches the exact solution, with component-wise errors being very small
- [supported] For a 3-asset portfolio problem, the ratio of the approximate solution (0.1608, 0.2557, 0.5833) aligns closely with the exact solution ratio (0.1622, 0.2568, 0.5811), demonstrating feasibility for portfolio optimization
- [speculative] The HHL algorithm may achieve exponential acceleration over classical methods for solving linear systems under certain assumptions, as claimed in prior theoretical work
- [speculative] The authors suggest that increasing the number of qubits could yield approximate solutions closer to the exact solution, but this would require larger quantum circuits and more quantum gates
- [speculative] The approach could potentially be extended to larger and more complex financial problem scenarios, though this remains untested

**Results summary:** The paper demonstrates the application of the HHL algorithm to a portfolio optimization problem, framed as a quadratic programming problem with equality constraints. Using a 9-qubit implementation on IBM’s quantum simulator, the authors show that the approximate solution derived from the HHL algorithm closely matches the exact solution for a 3-asset portfolio. The results validate the feasibility of using the HHL algorithm for such financial problems, though the work is limited to simulation and small-scale problems. The paper also reiterates theoretical claims of exponential speedup for the HHL algorithm but does not empirically demonstrate quantum advantage on real hardware.

**Performance claims:**
- Approximate solution ratio (0.1608, 0.2557, 0.5833) closely matches exact solution ratio (0.1622, 0.2568, 0.5811) for a 3-asset portfolio
- 9-qubit implementation used to represent an 8-dimensional input vector for the linear system
## Quantum advantage claim
**Classification:** speculative

The paper cites theoretical claims of exponential acceleration for the HHL algorithm over classical methods for solving linear systems, but these claims are not empirically validated in this work. All results are derived from simulation on classical quantum simulators, not real quantum hardware.
## Limitations
- Experiments conducted on a small-scale problem (3 assets) with synthetic data, limiting generalizability to real-world financial scenarios
- Qubit count constraints (9 qubits used) restrict the problem size and complexity that can be handled
- Approximate solution ratios were compared rather than exact amplitudes, which may not fully capture solution accuracy [inferred]
- No noise mitigation techniques were applied, which may affect performance on real quantum hardware [inferred]
- The study only tested a simplified quadratic programming model with equality constraints, not addressing more complex financial models
- Page-limit constraints of the conference paper may have prevented detailed discussion of error analysis and scalability [inferred]
- The HHL algorithm requires the matrix A to be Hermitian and well-conditioned, which may not hold for all financial problems [inferred]
- No comparison with state-of-the-art classical solvers (e.g., interior-point methods) to benchmark quantum advantage [inferred]
- The study did not address the impact of decoherence or gate errors on solution quality [inferred]
- The input vector |b⟩ was padded with zeros to fit qubit requirements, which may introduce artifacts in the solution [inferred]
## Open questions
- How does the HHL algorithm perform with larger asset portfolios (e.g., 20+ assets) and real market data?
- What is the impact of quantum noise and decoherence on the accuracy of the approximate solution?
- Can the HHL algorithm handle ill-conditioned matrices common in financial applications?
- How does the quantum solution compare to classical methods in terms of speed and accuracy for practical problem sizes?
- What are the trade-offs between qubit count, circuit depth, and solution accuracy in financial applications?
- How can the HHL algorithm be extended to handle inequality constraints in portfolio optimization?

**Future work:**
- Apply the HHL algorithm to larger and more complex financial problem scenarios
- Test the algorithm on real quantum hardware with noise mitigation techniques
- Compare the performance of the HHL algorithm with classical solvers for portfolio optimization
- Extend the model to include inequality constraints and multi-period optimization
- Investigate methods to reduce the qubit requirements for larger problem instances
- Explore hybrid quantum-classical approaches to improve scalability and practicality
## Key ideas
- #idea:quantum-advantage — HHL algorithm demonstrates potential for exponential acceleration in solving linear systems for portfolio optimization, though empirically unvalidated in this study
- #idea:near-term-feasibility — Study shows feasibility of HHL for small-scale portfolio problems (3 assets) using quantum simulators, but scalability to real-world scenarios remains speculative
- #idea:hybrid-approach — Implicit hybrid approach via classical preprocessing (e.g., padding input vectors) to fit qubit constraints, though not explicitly framed as hybrid
- #limitation:qubit-count — 9-qubit implementation restricts problem size, highlighting current hardware limitations for practical financial applications
- #limitation:noise — Lack of noise mitigation techniques raises concerns about performance on real quantum hardware
- #limitation:simulation-only — All results derived from classical quantum simulators, not real QPUs, limiting empirical validation of quantum advantage
## Contradictions
- #contradiction:scalability — Paper speculates about exponential speedup and scalability of HHL, but limitations (e.g., qubit count, noise, synthetic data) contradict these claims for real-world financial problems. Prior work (e.g., 2020_Aaronson_HHL_Limits) has questioned HHL's practicality due to input/output and error-correction overheads.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
