---
aliases:
- 'A quantum unstructured search algorithm for discrete optimisation: the use case
  of portfolio optimisation'
- quantum unstructured search algorithm
authors:
- Titos Matsakos
- Adrian Lomas
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- grover
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:10:45.153423'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:10:52.860209'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:11:27.996272'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:11:51.331832'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:12:19.083438'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:12:31.132327'
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
- method/grover
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
title: 'A quantum unstructured search algorithm for discrete optimisation: the use
  case of portfolio optimisation'
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces QSERA, a quantum unstructured search algorithm that reformulates finding extrema or roots of discrete objective functions as an unstructured search problem solvable via Grover’s algorithm. It details how to map a general high-order binary objective function into a quantum oracle, construct the corresponding quantum circuits, and discusses accuracy–depth trade-offs. As a concrete demonstration, the authors implement QSERA for a small portfolio optimisation problem, illustrating how the method identifies near-optimal portfolios and how its performance depends on prior knowledge of function bounds and the oracle construction parameter.
## Methodology
This preprint presents a primarily theoretical and proof-of-concept methodology centered on proposing a new quantum optimization approach, the Quantum Search for Extrema and Roots Algorithm (QSERA), and illustrating it with a small portfolio optimization example. The method first reformulates a discrete objective function f(x), including higher-order polynomial terms beyond standard QUBO, into a scaled function g(x) in [0,1], then raises it to a power n to construct an approximate oracle u_n(z)=g(x)^n that flags extrema or roots. This oracle is embedded into a Grover-style unstructured search procedure to amplify the amplitude of the optimal state, yielding a claimed quadratic speedup in search complexity. The paper derives the oracle construction analytically, decomposes the corresponding operators into quantum gates using phase gates, Hadamards, Pauli-Z, X, and Toffoli gates with ancilla qubits, and then demonstrates the full circuit on a toy portfolio selection problem with four assets. The application minimizes a benchmark-tracking objective based on portfolio return, volatility, and a soft cardinality/budget constraint, using analytically specified asset returns, volatilities, and correlations rather than an external dataset. The implementation is executed on a classical zero-noise Qiskit simulator, and results are reported as state measurement probabilities across the 16 candidate portfolios, including sensitivity to the oracle power parameter n and discussion of approximate knowledge of f_min and f_max.

**Algorithms used:** QSERA, Grover's algorithm, Quantum Unstructured Search Algorithm (QUSA)
**Frameworks:** Qiskit

**Experimental setup:** Proof-of-concept simulation of the proposed QSERA circuit on a classical zero-noise simulator in Qiskit v1.0. The portfolio example uses 4 data qubits to encode 16 portfolios, plus 3 ancilla qubits (2 for AND operations and 1 phase ancilla). The Grover search operator is applied with the optimal number of iterations m_opt = 2 for N = 16 states.

**Dataset:** Synthetic toy portfolio data for 4 assets (a, b, c, d), specified directly in the paper via mean returns, volatilities, and a 4x4 correlation matrix; benchmark target return, volatility, and asset count are also manually specified.
## Experiment details
### Input
A manually constructed 4-asset portfolio optimization instance: mean returns mu = [0.05, 0.01, 0.02, 0.04], volatilities sigma = [0.40, 0.10, 0.20, 0.30], and a 4x4 correlation matrix [[1.0, 0.5, -0.4, -0.2], [0.5, 1.0, -0.1, -0.3], [-0.4, -0.1, 1.0, 0.3], [-0.2, -0.3, 0.3, 1.0]]. The benchmark is set to return mu_b = 0.043, volatility sigma_b = 0.195, and cardinality N_b = 2. All 2^4 = 16 binary portfolios are considered. The objective function combines squared benchmark-tracking error in return and variance with a soft budget/cardinality penalty, using lambda_mu = 0.95 and lambda_sigma2 = 0.049. For oracle construction, the minimization scaling uses approximate bounds f_min ≈ 0 and f_max ≈ 0.15.

### Process
1. Define the discrete portfolio objective function over binary asset-selection variables, including return-tracking, variance-tracking, and soft cardinality penalty terms. 2. Expand the objective into a polynomial form with coefficients for zeroth through fourth order terms. 3. Rescale the objective into g(x) using the minimization mapping g(x) = (f_max - f(x)) / (f_max - f_min), with estimated rather than exact extrema bounds. 4. Construct the approximate oracle u_n(z) = g(x)^n and recursively compute the coefficients of g(x)^n from those of g(x). 5. Build the oracle operator Q* = exp(i pi G^n) and decompose it into order-specific phase operators implemented with ancilla-assisted controlled phase logic. 6. Prepare a uniform superposition over the 16 portfolio states using Hadamard gates. 7. Apply Grover amplitude amplification using (Q+Q*)^m with m_opt = 2. 8. Measure the resulting state probabilities and identify the most likely portfolio. 9. Perform a sensitivity analysis over the exponent n, showing how the probability of the optimal portfolio changes as oracle sharpness increases; the illustrative main example reports results for n = 24.

### Output
Outputs are probability distributions over the 16 computational basis states/portfolios after the QSERA circuit, identifying portfolio 1001 as the highest-probability solution and 0101 as the second most likely near-optimal solution. The paper also reports plots of the objective function f(z), scaled function g(z), oracle approximation u_n(z), and the probability of measuring the optimal portfolio as a function of the exponent n. No classical baseline benchmark, runtime benchmark, or financial performance comparison against standard portfolio optimization solvers is reported.

### Parameters
- data_qubits: 4
- ancilla_qubits: 3
- total_qubits: 7
- search_space_size: 16
- grover_iterations: 2
- oracle_power_n: 24
- lambda_mu: 0.95
- lambda_sigma2: 0.049
- soft_constraint_weight: 0.001
- estimated_f_min: 0.0
- estimated_f_max: 0.15
- benchmark_return: 0.043
- benchmark_volatility: 0.195
- benchmark_cardinality: 2

### Hardware
{'hardware_type': 'classical simulation', 'simulator': 'Qiskit zero-noise simulator', 'framework_version': 'Qiskit 1.0', 'qpu_used': False, 'noise_model': 'none / zero-noise'}

### Reproducibility
Preprint with substantial mathematical and circuit-construction detail, including explicit toy input data, objective function, coefficients, qubit layout, and gate decomposition. However, no code repository or executable implementation link is provided in the text. Replication of the toy example appears feasible from the paper alone, but reproducing coefficient recursion and full circuit assembly may require nontrivial effort.
## Findings
- [speculative] The paper proposes QSERA, a quantum unstructured search method that maps discrete optimisation, extremum finding, and root finding problems into a Grover-search oracle construction.
- [speculative] QSERA is claimed to find extrema or roots of discrete functions in O(sqrt(N)) Grover iterations once the oracle is constructed, implying a quadratic query-speedup over classical unstructured search.
- [speculative] The method can represent objective functions with higher-order terms beyond the standard QUBO framework, so it is presented as more general than optimisation approaches restricted to quadratic forms.
- [supported] In the worked portfolio-optimisation example with 4 assets (16 candidate portfolios), the constructed QSERA circuit assigns the highest measurement probability to portfolio 1001, which is the classical optimum under the paper's objective function.
- [supported] In the same example, portfolio 0101 receives the second-highest measurement probability, consistent with it being near-optimal under the benchmark-tracking objective.
- [supported] The paper shows that when f_min and f_max are only approximated rather than known exactly, the optimal state is not obtained with certainty in one shot; instead, near-optimal states also retain nontrivial probability mass.
- [supported] The probability of measuring the optimal portfolio depends non-monotonically on the exponent n used in the oracle construction, with an apparent best range around n≈20–30 in the example before performance degrades for larger n.
- [speculative] The authors claim QSERA can also be applied to continuous functions after discretisation, and may be useful when structured classical search such as gradient descent struggles on noisy or steep objective landscapes.
- [speculative] The paper states that if true f_min and f_max are known and n is sufficiently large, QSERA is guaranteed to identify the optimum in a single quantum execution.
- [speculative] A practical limitation identified by the authors is that computing the coefficients needed for the oracle, especially for g(x)^n at large problem sizes, may be classically difficult and may increase circuit depth.

**Results summary:** This preprint introduces QSERA, a Grover-based quantum search framework for finding extrema or roots of discrete functions by transforming the objective into an oracle-like function and then applying amplitude amplification. The paper is primarily theoretical but includes an end-to-end simulated portfolio-optimisation example on a 4-asset universe (16 portfolios) implemented with Qiskit on a zero-noise classical simulator. In that example, the algorithm's output distribution peaks on the optimal portfolio (1001), with a near-optimal portfolio (0101) also receiving elevated probability. The authors argue that QSERA can handle higher-order objective terms beyond QUBO and inherits Grover's quadratic query advantage in principle, but they also note important limitations: the need for prior knowledge or estimates of objective extrema, sensitivity to the exponent used in oracle construction, and potentially difficult classical preprocessing to derive oracle coefficients. Because the evidence is simulation-based and limited to a toy example, any broader quantum advantage claim remains speculative.

**Performance claims:**
- Claimed query complexity of O(sqrt(N)) Grover iterations versus O(N) classical unstructured search
- Worked example uses N=16 portfolios represented by 4 qubits, with optimal Grover iteration count m_opt = 2
- In the portfolio example, the probability of measuring the optimal portfolio peaks around exponent n in the range of approximately 20-30
- Example circuit uses 4 data qubits plus 3 ancilla qubits (2 for AND operations and 1 phase ancilla)
## Quantum advantage claim
**Classification:** speculative

The paper claims a quadratic Grover-style speedup in query complexity, but this is a preprint with only a small proof-of-concept demonstrated on a zero-noise classical simulator rather than real quantum hardware or large-scale empirical benchmarking.
## Limitations
- As a preprint, the work has not yet undergone peer review.
- QSERA can find the optimum with certainty only if the global minimum and maximum of the objective function (fmin and fmax) are known a priori.
- When fmin and fmax are not known exactly and must be estimated, the probability of measuring the true optimum is less than 1, and multiple shots are needed to distinguish it from near-optimal points.
- If fmin and fmax are misspecified, increasing the power n can cause the oracle to lose its ability to identify the optimum because un(z) can tend to 0 for all z.
- There is a nontrivial tuning trade-off in choosing the power n: too small and the oracle poorly separates the optimum from nearby states; too large and the signal for the optimum can vanish.
- The coefficients cn, cn,i, cn,i1i2, ... required to build the oracle may be difficult to compute in practice, especially for large problem sizes.
- The authors note that recursive classical computation of the oracle coefficients should be feasible in principle, but may not be trivial for large N.
- The portfolio optimisation demonstration is limited to a toy example with only 4 assets and 16 candidate portfolios.
- The implementation is demonstrated on a zero-noise simulator rather than on real quantum hardware.
- [inferred] No empirical evaluation is provided under realistic hardware noise, decoherence, gate errors, or limited connectivity constraints.
- [inferred] The paper does not report resource estimates such as gate counts, circuit depth scaling, ancilla overhead, or fault-tolerance requirements for financially relevant portfolio sizes.
- [inferred] Although Grover search gives quadratic query speedup, the practical advantage may be offset by the cost of constructing the oracle and computing high-order coefficient expansions.
- [inferred] No comparison is made against state-of-the-art classical optimisation methods or against other quantum optimisation approaches on the same benchmark.
- [inferred] The need to encode all higher-order terms may lead to deep circuits and substantial ancilla usage, limiting near-term practicality.
- [inferred] The claim of applicability to continuous functions is not empirically validated and depends on discretisation, which can substantially increase circuit depth and search space size.
- [inferred] The soft budget constraint used in the example does not guarantee exact constraint satisfaction, which may limit applicability in settings requiring hard portfolio constraints.
- [inferred] The study uses synthetic/simplified portfolio inputs rather than large-scale real financial datasets with realistic market frictions, turnover, liquidity, and transaction costs.
- [inferred] Scalability to realistic financial universes (e.g., thousands to 100,000 assets) is not demonstrated.
## Open questions
- How accurately must fmin and fmax be estimated for QSERA to remain effective in practice?
- How should the optimal power n be selected systematically when the true extrema are unknown?
- How does the classical cost of computing the oracle coefficients scale with problem size and objective-function order?
- At what problem sizes, if any, does QSERA provide practical end-to-end advantage once oracle construction costs are included?
- How robust is QSERA to realistic quantum hardware noise and imperfect gate implementations?
- How many shots are required to reliably identify the true optimum when the oracle is only approximate?
- How does QSERA perform on realistic portfolio optimisation instances with many assets and additional constraints?
- Can QSERA be adapted to enforce hard constraints directly rather than relying on soft penalties?
- For continuous functions, when does discretised unstructured search outperform structured classical methods such as gradient-based optimisation?
- How does QSERA compare empirically with Grover Adaptive Search, QAOA, annealing-based methods, and classical combinatorial solvers on the same financial tasks?

**Future work:**
- Develop methods for choosing or learning good estimates of fmin and fmax when they are not known exactly.
- Investigate principled procedures for selecting the power nopt that best balances oracle sharpness against signal collapse.
- Improve or automate the classical recursive computation of the coefficients cn, cn,i, cn,i1i2, ... for larger instances.
- Test QSERA on larger and more realistic portfolio optimisation problems beyond the 4-asset toy example.
- Evaluate the algorithm on real quantum hardware and study the impact of noise, circuit depth, and error mitigation.
- Produce detailed resource and scalability analyses, including qubit, ancilla, gate-count, and depth requirements.
- Compare QSERA empirically against classical optimisation baselines and alternative quantum optimisation algorithms.
- Extend the approach to portfolio models with realistic financial features such as liquidity, transaction costs, rebalancing, and private assets.
- Explore the use of QSERA for continuous or noisy objective functions after discretisation.
- Investigate formulations with hard constraints or more robust constraint-handling mechanisms for financial optimisation.
## Key ideas
- #idea:quantum-advantage — QSERA reformulates discrete optimisation, including higher-order non-QUBO portfolio objectives, as an unstructured search problem addressed with Grover-style amplitude amplification and claimed O(sqrt(N)) query complexity.
- #idea:quantum-advantage — The paper claims that if exact objective bounds f_min and f_max are known and the oracle sharpness parameter n is chosen appropriately, the optimum can be isolated with high probability or certainty in principle.
- #idea:near-term-feasibility — A full proof-of-concept circuit is demonstrated for a 4-asset portfolio optimisation problem, where the optimal portfolio 1001 receives the highest measurement probability.
- #idea:near-term-feasibility — The study explicitly discusses practical NISQ-relevant issues such as approximate extrema bounds, sensitivity to the exponent n, and the trade-off between oracle sharpness and degraded performance.
## Contradictions
- The paper claims Grover-style quadratic speedup for general discrete optimisation, but this is undermined by its own acknowledgement that oracle construction requires potentially expensive classical coefficient computation, higher-order term expansion, ancilla overhead, and deep circuits; this creates a #contradiction:scalability between asymptotic query advantage and practical end-to-end scaling.
- The paper presents a small successful portfolio example, but because results are obtained only on a zero-noise classical simulator with 4 assets and no classical baseline, the implied superiority of the approach over practical classical optimisation is not established, creating an implicit tension with its quantum-advantage framing.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
