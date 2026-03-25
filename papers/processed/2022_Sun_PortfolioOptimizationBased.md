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
journal_or_venue: ICAIS 2022
methodology_tags:
- HHL
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2020_Aaronson_HHL_Limits
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T15:58:29.943897'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:34.221516'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:59:10.107141'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:59:27.485459'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:59:52.025228'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:00:03.536213'
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
- method/HHL
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
The paper applies the HHL quantum algorithm for solving linear systems to a constrained quadratic programming formulation of portfolio optimization. The authors construct a small illustrative financial model, map it to a linear system, and implement the HHL procedure using Qiskit on IBM quantum hardware. They show that the quantum-derived approximate portfolio weights closely match the exact classical solution, suggesting that HHL can be used to accelerate similar combinatorial optimization problems in finance under suitable conditions.
## Methodology
This conference paper presents an empirical proof-of-feasibility study applying the Harrow-Hassidim-Lloyd (HHL) quantum linear systems algorithm to a constrained portfolio optimization problem. The authors start from a mean-variance style portfolio model with equality constraints on expected return and total investment, formulate it as a quadratic programming problem, and then convert it via Lagrange multipliers into a linear system. That linear system is mapped into a quantum linear systems problem and solved approximately using the HHL pipeline consisting of quantum phase estimation, controlled rotation, uncomputation, and measurement. The implementation is carried out using Qiskit on IBM's quantum computing platform. For evaluation, the paper instantiates a small toy financial example with three assets, specified expected returns, a 3x3 asset correlation matrix, target expected return, and unit total budget. The input vector and matrix are padded to dimension 8 to fit qubit encoding requirements, and the resulting HHL circuit uses 9 qubits. The approximate portfolio weights extracted from the measured quantum state are normalized and compared against the exact classical solution of the same linear system, with the main assessment based on closeness of the component ratios and normalized portfolio allocation values. The paper is a conference paper and appears to be a short empirical implementation/demo rather than a large-scale benchmark study.

**Algorithms used:** HHL, Quantum Phase Estimation, Inverse Quantum Fourier Transform
**Frameworks:** Qiskit, IBM Quantum

**Experimental setup:** The authors implemented the HHL-based portfolio optimization circuit using Qiskit on IBM's quantum computing platform. The test case was a small 3-asset portfolio optimization instance transformed into an 8-dimensional linear system to match qubit encoding constraints. The HHL circuit was configured with 9 qubits total, including registers for the input state, phase estimation, and an ancilla qubit. The phase estimation stage used an estimated success probability of 0.9 and 2 bits of precision.

**Dataset:** No external dataset was used. The study uses a synthetic toy portfolio optimization instance with 3 assets, manually specified expected returns and covariance/correlation structure.
## Findings
- [supported] The paper formulates a constrained portfolio optimization problem as a quadratic program with equality constraints and converts it into a linear system suitable for the HHL algorithm.
- [supported] Using a 3-asset toy portfolio instance implemented in Qiskit on IBM's quantum computing platform, the HHL-based method produced an approximate portfolio allocation of (0.1608, 0.2557, 0.5833).
- [supported] The approximate HHL solution was close to the exact classical solution (0.16216216, 0.25675676, 0.58108108) for the tested instance.
- [supported] The normalized ratio of the HHL-derived solution components was 0.2428:0.386:0.8803, approximately 3:5:12, matching the exact solution ratio closely.
- [supported] The constructed example used 9 qubits, including 3 qubits for the input state after padding the problem to dimension 8 and 2 bits for phase estimation.
- [speculative] The authors argue that HHL can accelerate the solution process for this class of financial combinatorial optimization problems compared with classical methods.
- [speculative] The paper suggests that using more qubits would make the approximate solution closer to the exact solution, at the cost of much larger circuit and gate counts.
- [speculative] The authors claim the approach demonstrates the feasibility of applying HHL to portfolio investment problems, but only on a small proof-of-concept instance.

**Results summary:** This conference paper presents a proof-of-concept application of the HHL quantum linear-systems algorithm to a constrained portfolio optimization problem. The authors reformulate a mean-variance-style portfolio problem with expected return and budget constraints as a linear system and implement the resulting HHL circuit in Qiskit for a 3-asset example. For the chosen instance, the HHL-derived approximate allocation (0.1608, 0.2557, 0.5833) is numerically close to the exact classical solution (0.16216216, 0.25675676, 0.58108108), and the component ratios align closely at about 3:5:12. The evidence is limited to a small-scale example and does not empirically demonstrate runtime speedup or practical quantum advantage; acceleration claims are theoretical and inherited from HHL assumptions rather than shown in the experiment.

**Performance claims:**
- Approximate HHL portfolio solution: (0.1608, 0.2557, 0.5833)
- Exact classical solution: (0.16216216, 0.25675676, 0.58108108)
- Approximate normalized component ratio: 0.2428 : 0.386 : 0.8803 ≈ 3 : 5 : 12
- Expected return target set to 0.15 with total cost 1 in a 3-asset example
- Problem padded to 8 dimensions and implemented with 9 qubits
- Phase estimation success probability set to 0.9 with 2 estimation bits
## Quantum advantage claim
**Classification:** theoretical

The paper invokes the known theoretical HHL speedup for linear systems and suggests portfolio optimization could be accelerated under HHL assumptions, but it only validates solution quality on a small example and does not empirically demonstrate speedup or quantum advantage on real financial-scale problems.
## Limitations
- The empirical demonstration is limited to a toy problem with only 3 assets, which does not establish performance on realistic portfolio sizes.
- The model simplifies the budget vector to P = (1,1,1,...)^T, reducing realism relative to actual asset prices and costs.
- The paper assumes known returns and a covariance structure with normally distributed asset returns, which may not hold in real financial markets.
- The implementation requires padding the problem to an 8-dimensional vector and uses only a 9-qubit circuit, indicating a very small-scale proof of concept.
- The phase estimation uses only 2 estimation bits, so solution accuracy is limited and depends on coarse eigenvalue estimation.
- The authors note that obtaining exact coefficients may not be possible for some problems; only ratios between solution components may be recoverable from the quantum state.
- The authors explicitly state that using more qubits would improve approximation quality but would make the required quantum gates and circuits very large.
- [inferred] No results are reported from execution on noisy real quantum hardware; the Qiskit/IBM platform usage appears to be simulation-oriented or at least does not analyze hardware noise effects.
- [inferred] No comparison is provided against strong classical portfolio optimization baselines in runtime, scalability, or solution quality, so practical quantum advantage is unsubstantiated.
- [inferred] The claimed acceleration relies on HHL assumptions, but the paper does not analyze whether the portfolio linear systems satisfy the sparsity, conditioning, state-preparation, and readout requirements needed for end-to-end speedup.
- [inferred] The study evaluates only one manually constructed instance, so robustness across datasets, market regimes, and covariance structures is unknown.
- [inferred] The paper does not discuss condition number sensitivity, which is critical for HHL performance and approximation error.
- [inferred] There is no treatment of realistic portfolio constraints such as no-short-selling, transaction costs, cardinality constraints, turnover limits, or multi-period dynamics.
- [inferred] Reproducibility is limited because the paper does not provide code, full circuit specifications, runtime settings, or enough implementation detail to replicate all results.
- [inferred] As a conference paper, page-limit constraints may have reduced methodological detail, experimental breadth, and discussion of negative results.
## Open questions
- How can the HHL-based method be applied to larger and more complex financial problem scenarios?
- For which classes of portfolio problems can the algorithm recover exact coefficients rather than only ratios between solution components?
- How does solution quality scale as the number of assets and constraints increases?
- How sensitive is the method to the condition number and spectral properties of the portfolio linear system?
- Do the assumptions required for HHL hold for realistic financial covariance matrices and return vectors?
- What is the effect of hardware noise, decoherence, and finite gate fidelity on the recovered portfolio weights?
- Can any practical end-to-end speedup be achieved once state preparation, Hamiltonian simulation, and measurement overhead are included?
- How does the approach compare with classical solvers on realistic portfolio optimization tasks in accuracy, runtime, and resource cost?

**Future work:**
- Apply the method to larger and more complex financial problem scenarios.
- Investigate ways to obtain more accurate coefficients of the solution vector, not just relative ratios.
- Use more qubits and higher-precision phase estimation to improve approximation accuracy.
- Test the approach on more realistic portfolio models with richer constraints and real market data.
- Study scalability and circuit/gate growth as problem size increases.
- Evaluate the algorithm on real quantum hardware and incorporate noise-aware or error-mitigation techniques.
- Benchmark against state-of-the-art classical optimization methods to assess whether any practical advantage exists.
- Extend the formulation beyond the simplified equality-constrained quadratic program to more realistic financial optimization settings.
## Key ideas
- #idea:quantum-advantage — Reformulates a constrained mean-variance portfolio optimisation problem as a linear system and applies HHL, invoking theoretical HHL speedups for this class of finance problems.
- #idea:near-term-feasibility — Demonstrates a 3-asset proof of concept in Qiskit/IBM with a 9-qubit HHL circuit whose recovered portfolio weights closely match the exact classical solution.
- #idea:near-term-feasibility — Shows that useful relative portfolio allocation ratios can be extracted from the HHL output state even when exact coefficients are harder to recover directly.
- #idea:quantum-advantage — Suggests that successful solution-quality matching on a toy instance indicates possible applicability of HHL to broader portfolio optimisation settings under suitable assumptions.
## Contradictions
- The paper suggests HHL-based acceleration for portfolio optimisation, but its evidence is limited to a single 3-asset toy instance with no runtime benchmark, no realistic-scale experiment, and unclear simulator-versus-hardware execution, contradicting any practical superiority claim over classical solvers.
- The paper implicitly leans on HHL scalability, yet its own limitations note that higher accuracy requires more qubits and much larger circuits, undermining claims that the method scales cleanly to realistic portfolio sizes.
- Theoretical speedup claims depend on HHL assumptions such as efficient state preparation, favorable conditioning, sparsity, and low readout overhead, but the paper does not verify these for realistic financial matrices; this aligns with critiques such as 2020_Aaronson_HHL_Limits.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic portfolio instance with 3 assets. Expected return vector mu = (0.05, 0.1, 0.2), asset allocation price vector P = (1, 1, 1), and correlation/covariance-like matrix Sigma = [[1, 0.5, 0], [0.5, 1, 0.1], [0, 0.1, 1]]. Constraints were target expected return mu0 = 0.15 and total cost xi = 1. The resulting linear-system right-hand side was b = (0.15, 1, 0, 0, 0)^T, then padded with zeros to 8 dimensions so it could be encoded using 3 qubits. The system matrix was likewise expanded to 8x8.

### Process
1. Formulate the portfolio optimization problem as minimizing omega^T Sigma omega subject to expected return and budget equality constraints. 2. Apply the Lagrange method to convert the constrained quadratic program into a linear system in variables (lambda, nu, omega). 3. Map the linear system A x = b into a quantum linear systems problem. 4. Pad the input vector and matrix to dimension 8 to satisfy qubit encoding requirements. 5. Build the HHL circuit in Qiskit with quantum phase estimation, controlled rotation, and uncompute stages. 6. Set phase estimation precision to 2 bits and target success probability to 0.9, yielding a 9-qubit circuit. 7. Measure only the relevant qubits: the ancilla must be 1 and the phase-estimation register must be all zeros. 8. Extract the amplitudes associated with basis states |010>, |011>, and |100> corresponding to the portfolio-weight components. 9. Normalize the extracted amplitudes to obtain approximate portfolio weights and compare them with the exact classical solution.

### Output
The output is an approximate quantum solution state from which portfolio weight ratios are extracted. Reported results include the approximate component ratio x1:x2:x3 = 0.2428:0.386:0.8803, approximated as 3:5:12, and the normalized portfolio allocation (0.1608, 0.2557, 0.5833). These are compared against the exact classical solution (0.16216216, 0.25675676, 0.58108108). The evaluation is qualitative/numerical agreement with the exact solution; no broader benchmark metrics, runtime study, or baseline beyond exact classical comparison are reported.

### Parameters
- assets: 3
- input_vector_dimension_after_padding: 8
- system_matrix_dimension_after_padding: 8x8
- qubits_total: 9
- phase_estimation_bits: 2
- phase_estimation_success_probability: 0.9
- target_expected_return: 0.15
- total_budget: 1

### Hardware
Implemented with Qiskit on IBM's quantum computing platform. The paper does not clearly specify whether execution was on a simulator or a real IBM QPU, and no backend name, shot count, noise model, transpilation settings, or cloud configuration are reported.

### Reproducibility
Partial reproducibility only. The mathematical formulation, toy input values, and some circuit design choices are provided, but critical implementation details are missing, including exact backend, simulator vs. hardware status, number of shots, circuit parameters beyond qubit count and phase-estimation bits, and no code repository is mentioned. Replication of the toy example is possible in principle, but not fully specified.
