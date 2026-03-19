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
doi: 10.1007/978-3-031-06788-4
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ICAIS 2022, LNCS 13339
methodology_tags:
- HHL
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2009_Lloyd_QuantumAlgorithm
- 2020_Aaronson_HHL_Limits
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:27:20.009902'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:27:26.173997'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:29:05.950436'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:29:22.169279'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:29:33.842552'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:29:41.710808'
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
The paper presents an empirical study on applying the quantum HHL algorithm to solve portfolio optimization problems in finance. The research formulates the portfolio optimization problem as a quadratic programming problem with equality constraints, which is then transformed into a linear system of equations. The HHL algorithm is employed to solve this linear system on a quantum computing platform. The methodology involves encoding the financial problem into a quantum state, applying the HHL algorithm (which includes quantum phase estimation, controlled rotation, and uncompute stages), and measuring the final quantum state to obtain an approximate solution. The solution is compared to the exact classical solution to evaluate the algorithm's accuracy and feasibility for financial combinatorial optimization problems.

**Algorithms used:** HHL
**Frameworks:** Qiskit

**Experimental setup:** The experiments were conducted using the Qiskit package on IBM’s quantum computing platform. The HHL algorithm was implemented with a 9-qubit circuit, where 3 qubits were used to represent the input vector. The phase estimation stage was configured to estimate eigenvalues with a success probability of 0.9 using 2 bits. The quantum simulator was used to execute the circuit and measure the output states.

**Dataset:** A synthetic financial dataset was used to model a portfolio optimization problem with 3 assets. The average profit rates for the assets were μT = (0.05, 0.1, 0.2), and the correlation matrix Σ was defined as a 3x3 matrix with diagonal entries of 1 and off-diagonal entries representing asset correlations. The expected return was set to μ0 = 0.15, and the total investment cost was ξ = 1.
## Findings
- [supported] The HHL algorithm was implemented using Qiskit on IBM’s quantum computing platform to solve a 3-asset portfolio optimization problem, yielding an approximate solution close to the exact solution with ratios 0.2428:0.386:0.8803 (≈3:5:12) vs. exact 0.16216216:0.25675676:0.58108108 (≈3:5:12).
- [supported] The approximate solution obtained via the HHL algorithm on a 9-qubit circuit (simulated) matched the exact solution’s component ratios, demonstrating feasibility for portfolio optimization.
- [speculative] The authors suggest that the HHL algorithm could achieve exponential acceleration over classical methods for solving linear systems, as originally proposed by Lloyd et al. (2009).
- [speculative] The paper claims that quantum computing could better address combinatorial optimization problems in finance due to quantum speedup, but this is not empirically validated in the study.
- [supported] The HHL algorithm’s performance was tested on a simplified 3-asset model with a fixed expected return (μ0 = 0.15) and total cost (ξ = 1), showing small errors in the approximate solution compared to the exact solution.
- [disputed] The claim of exponential acceleration via HHL is disputed in literature due to practical limitations (e.g., input state preparation, error correction, and hardware noise), which are not addressed in this paper.

**Results summary:** The paper empirically demonstrates the application of the HHL algorithm to a 3-asset portfolio optimization problem using a 9-qubit quantum circuit simulated on IBM’s Qiskit platform. The approximate solution derived from the quantum algorithm closely matched the exact solution’s component ratios, validating the feasibility of HHL for such problems. However, the results are based on simulations, and the claimed exponential quantum advantage remains theoretical and untested on real hardware. The study focuses on a simplified model, and scalability to larger, real-world financial problems is not addressed.

**Performance claims:**
- Approximate solution ratios: 0.2428:0.386:0.8803 (HHL) vs. exact 0.16216216:0.25675676:0.58108108
- 9-qubit circuit used for simulation with phase estimation success probability set to 0.9
- Error in approximate solution components was small, demonstrating close agreement with exact solution
## Quantum advantage claim
**Classification:** theoretical

The paper cites the theoretical exponential speedup of the HHL algorithm for solving linear systems (Lloyd et al., 2009) but does not demonstrate this advantage empirically. Results are from simulation only, and the study does not address practical challenges (e.g., error rates, qubit coherence) that could undermine the claimed advantage on real hardware.
## Limitations
- Experiments conducted on a small-scale problem (3 assets) limits practical applicability to real-world portfolio optimization [inferred]
- Use of only 9 qubits constrains the problem size and scalability of the HHL algorithm implementation
- Approximate solution ratios were compared rather than exact amplitudes, which may not fully capture solution accuracy
- Implementation was performed on a quantum simulator (Qiskit), not real quantum hardware, limiting assessment of noise and decoherence effects [inferred]
- Dataset size and complexity were artificially constrained to fit qubit limitations (8-dimensional input vector)
- No noise mitigation techniques were applied, which may significantly impact performance on real quantum devices [inferred]
- The study only tested synthetic data with simplified assumptions (e.g., fixed asset correlation matrix), not real market data [inferred]
- The HHL algorithm requires the matrix A to be Hermitian and well-conditioned, which may not hold for all financial problems [inferred]
- The phase estimation stage was limited to 2 bits, reducing eigenvalue approximation accuracy [inferred]
- No comparison with state-of-the-art classical solvers (e.g., quadratic programming solvers) to benchmark quantum advantage [inferred]
## Open questions
- How does the HHL algorithm perform with larger asset portfolios (e.g., >20 assets) given current qubit constraints?
- What is the impact of quantum noise and decoherence on the accuracy of the HHL-based portfolio optimization?
- Can the algorithm maintain its exponential speedup advantage when scaled to real-world financial datasets?
- How does the solution quality degrade as the condition number of the matrix A increases?
- What are the trade-offs between qubit count, circuit depth, and solution accuracy in practical deployments?
- How can the HHL algorithm be adapted to handle non-Hermitian matrices common in financial models?
- What noise mitigation strategies are most effective for HHL-based financial applications?

**Future work:**
- Extend the HHL algorithm to larger and more complex financial problem scenarios (e.g., multi-period portfolio optimization)
- Test the algorithm on real quantum hardware to assess noise resilience and practical performance
- Incorporate noise mitigation techniques (e.g., error correction, dynamical decoupling) to improve solution accuracy
- Compare the HHL algorithm with classical solvers (e.g., interior-point methods) to quantify quantum advantage
- Explore hybrid quantum-classical approaches to overcome current qubit limitations
- Develop methods to extract exact solution coefficients (not just ratios) from the quantum state
- Apply the algorithm to real market data and assess its robustness to financial noise and volatility
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
