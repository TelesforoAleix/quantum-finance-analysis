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
journal_or_venue: ICAIS 2022, LNCS 13339
methodology_tags:
- HHL
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2009_Harrow_HHL_LinearSystems
- 2020_Aaronson_HHL_Limits
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:24:42.064521'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:24:57.649895'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:25:08.805630'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:25:14.976161'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:26:01.439483'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:26:04.193806'
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
- contradiction/scalability
title: Portfolio Optimization Based on Quantum HHL Algorithm
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
This paper explores the application of the quantum HHL algorithm to solve combinatorial optimization problems in financial portfolio management. The authors frame portfolio optimization as a quadratic programming problem with equality constraints and implement the HHL algorithm using IBM’s Qiskit platform. The study demonstrates the feasibility of quantum computing for accelerating solutions to such financial problems, comparing approximate quantum solutions with exact classical ones.
## Methodology
The paper presents an empirical study on applying the quantum HHL algorithm to solve portfolio optimization problems in finance. The research formulates the portfolio optimization problem as a quadratic programming problem with equality constraints, which is then transformed into a linear system of equations. The HHL algorithm is employed to solve this linear system on a quantum computer. The study implements the algorithm using the Qiskit framework on IBM's quantum computing platform. The experimental setup involves a simplified model with three assets, predefined average profit rates, asset correlations, expected return, and total investment cost. The HHL algorithm's phases—quantum phase estimation, controlled rotation, uncompute, and measurement—are executed to obtain an approximate solution to the portfolio weights. The results are compared against the exact classical solution to evaluate the algorithm's accuracy and feasibility.

**Algorithms used:** HHL
**Frameworks:** Qiskit

**Experimental setup:** The experiments were conducted using the Qiskit package on IBM's quantum computing platform. The HHL algorithm was implemented with a 9-qubit circuit, including qubits for phase estimation, input state, and ancilla bits.

**Dataset:** A synthetic financial dataset with three assets was used. The dataset includes predefined average profit rates μT = (0.05, 0.1, 0.2), asset correlation matrix, expected return μ0 = 0.15, and total investment cost ξ = 1.
## Findings
- [supported] The HHL algorithm was implemented using Qiskit on IBM’s quantum computing platform to solve a 3-asset portfolio optimization problem, yielding an approximate solution (0.1608, 0.2557, 0.5833) that closely matches the exact solution (0.1622, 0.2568, 0.5811) in ratio (3:5:12).
- [supported] The approximate solution obtained via the HHL algorithm demonstrated small errors in each component compared to the exact solution, validating its feasibility for quadratic programming problems with equality constraints in finance.
- [speculative] The authors claim that the HHL algorithm can achieve exponential acceleration over classical methods for solving linear systems, as originally proposed by Harrow, Hassidim, and Lloyd (2009).
- [speculative] The paper suggests that the HHL algorithm could be applied to larger and more complex financial problem scenarios, though this is noted as future work.
- [supported] Results were obtained via simulation on quantum hardware (IBM’s platform), not real quantum hardware, with a 9-qubit circuit used for the implementation.

**Results summary:** The paper empirically demonstrates the application of the HHL quantum algorithm to a 3-asset portfolio optimization problem, modeled as a quadratic programming problem with equality constraints. Using a 9-qubit circuit simulated on IBM’s quantum platform, the authors obtained an approximate solution that closely matched the exact classical solution in ratio, with minor component-wise errors. The work validates the feasibility of the HHL algorithm for financial combinatorial optimization but relies on simulation rather than real quantum hardware. The claimed exponential quantum advantage remains theoretical and untested at scale.

**Performance claims:**
- Approximate solution ratio (3:5:12) matched exact solution ratio with minor component-wise errors
- 9-qubit circuit implementation on IBM’s quantum platform (simulated)
## Quantum advantage claim
**Classification:** theoretical

The paper cites the theoretical exponential speedup of the HHL algorithm for solving linear systems (Harrow et al., 2009) but does not demonstrate this advantage empirically. Results are from simulation only, and the problem size (3 assets) is too small to validate quantum advantage.
## Limitations
- Experiments conducted on a small-scale problem (3 assets) with synthetic data, limiting generalizability to real-world financial scenarios
- Qubit count constraints (9 qubits used) restrict the problem size and complexity that can be handled
- Hardware noise and decoherence effects were not explicitly addressed or mitigated in the implementation
- The HHL algorithm requires the matrix A to be Hermitian and well-conditioned, which may not hold for all financial problems [inferred]
- The solution only provides the ratio of investment proportions, not absolute values, which may limit practical applicability
- The study used a simplified correlation matrix (σij) that may not reflect real market conditions [inferred]
- No comparison with state-of-the-art classical portfolio optimization methods was performed [inferred]
- The implementation was limited to a specific quantum simulator (Qiskit on IBM's platform) without testing on real quantum hardware
- The phase estimation stage was limited to 2 bits, which may affect the accuracy of eigenvalue estimation [inferred]
- The study did not address the potential impact of quantum gate errors or readout errors on solution quality [inferred]
## Open questions
- How does the HHL algorithm perform with larger asset portfolios (e.g., 20+ assets) that are common in real-world scenarios?
- What is the impact of quantum noise and decoherence on the accuracy of the HHL-based portfolio optimization?
- Can the HHL algorithm handle ill-conditioned matrices that are common in financial applications?
- How does the quantum solution compare to classical methods in terms of both accuracy and computational efficiency?
- What are the minimum qubit requirements for solving practical portfolio optimization problems?
- How can the absolute values of the solution vector be recovered, rather than just the ratios?
- What noise mitigation techniques could be applied to improve the robustness of the HHL algorithm in financial applications?

**Future work:**
- Extend the method to larger and more complex financial problem scenarios
- Test the algorithm on real quantum hardware to evaluate its performance under noise conditions
- Compare the quantum approach with state-of-the-art classical portfolio optimization methods
- Investigate noise mitigation techniques to improve solution accuracy on near-term quantum devices
- Explore methods to recover absolute solution values rather than just ratios
- Apply the HHL algorithm to other financial problems beyond portfolio optimization, such as risk management or option pricing
- Develop hybrid quantum-classical approaches that combine the strengths of both paradigms
## Key ideas
- #idea:quantum-advantage — HHL algorithm demonstrates potential for exponential acceleration in solving linear systems for portfolio optimization, though empirically unvalidated in this study
- #idea:near-term-feasibility — Study shows feasibility of HHL for small-scale portfolio problems (3 assets) using quantum simulators, but scalability to real-world scenarios remains speculative
- #limitation:qubit-count — 9-qubit implementation restricts problem size, highlighting current hardware limitations for practical financial applications
- #limitation:noise — Lack of noise mitigation techniques raises concerns about performance on real quantum hardware
- #limitation:simulation-only — All results derived from classical quantum simulators, not real QPUs, limiting empirical validation of quantum advantage
- #idea:hybrid-approach — Classical preprocessing (e.g., padding input vectors) used to fit qubit constraints, though not explicitly framed as a hybrid approach
## Contradictions
- #contradiction:scalability — Paper speculates about exponential speedup and scalability of HHL, but limitations (e.g., qubit count, noise, synthetic data) contradict these claims for real-world financial problems. Prior work (e.g., 2020_Aaronson_HHL_Limits) has questioned HHL's practicality due to input/output and error-correction overheads.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Synthetic data generated for the study', 'number_of_assets': 3, 'features': ['average profit rates', 'asset correlations', 'expected return', 'total investment cost'], 'preprocessing_steps': 'The input vector |b⟩ was expanded to an 8-dimensional vector to fit the 3-qubit representation requirement. The matrix A was similarly expanded to 8x8 dimensions.', 'time_period': 'Not applicable (synthetic data)'}

### Process
1. Formulate the portfolio optimization problem as a quadratic programming problem with equality constraints. 2. Transform the problem into a linear system A|x⟩ = |b⟩. 3. Encode the linear system into a quantum circuit using Qiskit. 4. Execute the HHL algorithm phases: quantum phase estimation (QPE) with 2 estimation bits, controlled rotation, uncompute, and measurement. 5. Measure the ancilla qubit; if the result is 1, extract the approximate solution |˜x⟩ from the input qubit register. 6. Normalize the solution to obtain portfolio weights.

### Output
The approximate solution for portfolio weights was compared against the exact classical solution. The ratio of the approximate solution components was analyzed and normalized to derive the investment proportions.

### Parameters
- qubits: 9
- phase_estimation_bits: 2
- success_probability_threshold: 0.9
- circuit_depth: Not explicitly stated, but involves multiple stages (QPE, controlled rotation, uncompute)
- shots: Not explicitly stated, but measurement was performed to extract the solution

### Hardware
IBM's quantum computing platform (simulator or real QPU not explicitly stated, but Qiskit was used for implementation).

### Reproducibility
The paper provides sufficient detail on the algorithm implementation and problem setup to replicate the study. However, no explicit mention of code or data availability is made. The synthetic dataset parameters are fully described, enabling recreation.
