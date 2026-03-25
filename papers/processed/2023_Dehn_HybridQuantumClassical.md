---
aliases:
- A hybrid quantum-classical approach to warm-starting optimization
- hybrid quantum classical approach
authors:
- Vanessa Dehn
- Thomas Wellens
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
journal_or_venue: arXiv
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:00:00.360644'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:04.149729'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:00:36.989331'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:06.580777'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:01:33.428549'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:01:48.769962'
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
- topic/risk-modelling
- method/QAOA
- method/QUBO
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A hybrid quantum-classical approach to warm-starting optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2023
zotero_key: ''
---

## Abstract summary
The paper studies how warm-starting the Quantum Approximate Optimization Algorithm (QAOA) affects performance on a portfolio optimization problem formulated as a QUBO. The authors compare standard QAOA with warm-start QAOA across random, “hot”, and “cold” instances, where hot/cold refer to how close the relaxed continuous solution is to the optimal discrete one. They then introduce a purely classical preprocessing scheme based on rounding and variable elimination before running standard QAOA, and show that this hybrid classical–quantum approach can reproduce or even surpass the performance gains usually attributed to warm-start QAOA, suggesting that these gains are not inherently quantum in origin.
## Methodology
This preprint presents an empirical simulation study comparing standard QAOA and warm-start QAOA for binary portfolio optimization, and then introducing a hybrid classical preprocessing method followed by standard QAOA. The portfolio problem is formulated as a QUBO with a covariance matrix for risk, expected returns for reward, a risk-preference parameter q, and a quadratic penalty term enforcing a budget constraint. Standard QAOA uses the usual |+>^N initial state and X-mixer, while warm-start QAOA first solves the continuous relaxation of the QUBO over [0,1]^N, uses that relaxed solution to prepare a parameterized initial state via RY rotations, and replaces the standard mixer with a warm-start mixer dependent on the relaxed solution. The authors evaluate both methods on ensembles of randomly generated portfolio instances with N=10 assets and budget B=5, and further classify 1000 random instances into 'hot' and 'cold' subsets based on how close the relaxed solution is to the optimal binary solution, using both maximum deviation and RMSE criteria. They then test a classical preprocessing scheme that rounds relaxed variables near 0 or 1 using threshold parameters, eliminates fixed variables, and solves the reduced problem with standard QAOA. Performance is assessed across QAOA depths p from 0 to 7 using mean approximation ratio and ground-state probability, averaged over 20-instance subsets with error bars from standard deviation. The study concludes that much of the warm-start advantage can be reproduced or exceeded by classical preprocessing plus standard QAOA, especially in approximation ratio.

**Algorithms used:** QAOA, warm-start QAOA

**Experimental setup:** Simulation-based study on randomly generated portfolio QUBO instances. Quantum circuits correspond to N=10 qubits (one per asset) with budget constraint B=5. Standard QAOA and warm-start QAOA are evaluated for depths p=0 to 7. Warm-start initialization is obtained from the continuous relaxation solved classically with a gradient-based optimizer; the QAOA parameter optimization uses a gradient-free classical optimizer. Circuits are executed on a qasm simulator with 1000 shots. Additional experiments use a classical preprocessing/rounding stage before running reduced standard QAOA.

**Dataset:** Synthetic/randomly generated portfolio optimization instances based on financial return vectors and covariance matrices; one appendix example uses 10 assets from the German DAX 30 with explicit return vector and covariance matrix. Main experiments use ensembles of random instances rather than a fixed historical benchmark dataset.
## Experiment details
### Input
Primary inputs are randomly generated portfolio instances formulated as QUBOs with N=10 assets and budget constraint B=5. The study uses an ensemble of 20 random instances for the main comparison, and 1000 random instances to derive 'hot' and 'cold' subsets based on the distance between relaxed and optimal binary solutions. Two distance measures are used for subset selection: maximum deviation epsilon = max_i |x*_i - xopt_i| and RMSE sigma over all variables. From the 1000-instance pool, subsets of 20 hottest and 20 coldest instances are selected under each measure. Financial inputs are expected returns mu_i and covariance matrix sigma_ij; an appendix provides one example instance from 10 German DAX 30 assets. The paper references prior work for the random instance generation procedure and penalty-term selection.

### Process
1. Formulate portfolio optimization as a QUBO with risk term, return term, and budget-constraint penalty. 2. For standard QAOA, map binary variables to Pauli-Z operators, initialize in |+>^N, apply p alternating layers of cost unitaries and standard X-mixers, measure in the computational basis, and use a classical gradient-free optimizer to update variational parameters. 3. For warm-start QAOA, first solve the continuous relaxation over [0,1]^N using a gradient-based optimizer; convert each relaxed variable x*_i into an angle theta_i = 2 arcsin(sqrt(x*_i)); prepare the initial state with RY(theta_i) rotations; use the warm-start mixer M_ws = -sum_i [sin(theta_i) X_i + cos(theta_i) Z_i]; then optimize QAOA parameters classically as above. 4. Evaluate both methods for depths p from 0 to 7 on 20 random instances. 5. Generate 1000 random instances, compute epsilon and sigma between relaxed and optimal binary solutions, and select 20 hot and 20 cold instances under each measure; rerun standard and warm-start QAOA on these subsets. 6. For the proposed preprocessing method, solve the continuous relaxation, round variables using thresholds: if x*_i <= delta_0 set x_i=0, if x*_i >= 1-delta_1 set x_i=1, leave others unfixed, eliminate fixed variables, and solve the reduced problem with standard QAOA. 7. Test preprocessing with threshold settings (0.5,0.5), (0.01,0.01), (0.25,0.25), and (0.1,0.25), again over depths p=0 to 7. 8. Aggregate results over 20-instance ensembles and report means with standard deviations.

### Output
Outputs are the mean approximation ratio r and the probability P of measuring the optimal solution ('ground state probability') as functions of QAOA depth p. The approximation ratio is computed over measured bitstrings, with infeasible solutions assigned zero and feasible solutions scaled between worst and best feasible portfolio cost values. Results are reported for standard QAOA, warm-start QAOA, and preprocessed standard QAOA, with comparisons across random, hot, and cold instance subsets and across different preprocessing threshold settings. Error bars represent standard deviation across the 20 instances in each subset.

### Parameters
- qubits: 10
- assets: 10
- budget_constraint_B: 5
- qaoa_depth_range: p = 0 to 7
- max_qaoa_depth: 7
- shots: 1000
- instance_counts: {'main_random_ensemble': 20, 'random_pool_for_hot_cold_selection': 1000, 'hot_subset_size': 20, 'cold_subset_size': 20}
- optimizers: {'continuous_relaxation': 'gradient-based optimizer', 'qaoa_parameter_optimization': 'gradient-free optimizer'}
- preprocessing_thresholds_tested: [{'delta_0': 0.5, 'delta_1': 0.5}, {'delta_0': 0.01, 'delta_1': 0.01}, {'delta_0': 0.25, 'delta_1': 0.25}, {'delta_0': 0.1, 'delta_1': 0.25}]
- hot_cold_measures: ['maximum deviation epsilon', 'RMSE sigma']

### Hardware
{'hardware_type': 'simulator', 'simulator': 'qasm simulator', 'shots': 1000, 'qpu_used': False}

### Reproducibility
Preprint empirical study. The paper provides the mathematical formulation, instance sizes, evaluation metrics, depth range, shot count, and preprocessing threshold settings, but does not specify the exact simulator software stack or all optimizer/hyperparameter details in the excerpt. Data are mostly randomly generated, with one example portfolio instance shown in the appendix and generation details delegated to a prior reference. No code link is provided in the excerpt. Replication is partially feasible but not fully turnkey from the provided text alone.
## Findings
- [supported] On simulated portfolio-optimization instances with N=10 assets and budget B=5, warm-start QAOA achieved higher mean approximation ratio and higher ground-state probability than standard QAOA across depths p=0 to 7.
- [supported] The benefit of warm-start QAOA depends on how close the relaxed continuous solution is to the binary optimum: 'hot' instances outperform 'cold' instances under warm-start QAOA, while standard QAOA shows little sensitivity to this hot/cold partition.
- [supported] A purely classical preprocessing scheme that rounds relaxed-solution variables near 0 or 1, eliminates fixed variables, and then runs standard QAOA on the reduced problem can reproduce or exceed warm-start QAOA's approximation-ratio performance on the tested instances.
- [supported] For random instances, preprocessed standard QAOA with symmetric bounds δ0=δ1=0.25 reached about 92% approximation ratio at p=7, matching warm-start QAOA within error bars and outperforming it at smaller p.
- [supported] For random instances, preprocessed standard QAOA improved ground-state probability over standard QAOA but generally remained below warm-start QAOA, suggesting it often finds near-optimal rather than optimal solutions.
- [supported] For cold instances, preprocessed standard QAOA reproduced warm-start QAOA's approximation-ratio performance at p=7 for both ε-based and σ-based instance selections, though ground-state probabilities were usually lower than warm-start.
- [supported] For ε-cold instances, an asymmetric preprocessing bound (δ0=0.1, δ1=0.25) produced the highest reported ground-state probability among the tested preprocessing settings and exceeded warm-start QAOA for that subset.
- [supported] For hot instances, naive classical rounding alone solved most or all cases: ε-hot instances achieved r=P=100%, and σ-hot instances achieved r=P=85%, indicating that some warm-start gains arise from classical information already present in the relaxed solution.
- [supported] For σ-hot instances, preprocessed standard QAOA with δ0=δ1=0.25 achieved about 98% approximation ratio and about 86% ground-state probability, slightly surpassing warm-start QAOA's reported ~96% and ~83% at p=7.
- [supported] The paper argues, based on these simulations, that the improved performance of warm-start QAOA in this setting is not due to quantum effects alone and can be largely explained by classical preprocessing.
- [speculative] The authors suggest that understanding which optimization steps can be handled classically versus quantumly may help design more effective hybrid workflows and potentially contribute to future quantum advantage.
- [speculative] The paper notes QAOA as a promising candidate for combinatorial optimization but explicitly states that an advantage over classical algorithms has not yet been proven.

**Results summary:** This preprint studies standard QAOA versus warm-start QAOA for portfolio optimization using qasm-simulator experiments on 20-instance ensembles of 10-asset problems, with additional hot/cold subsets drawn from 1000 random instances. Warm-start QAOA consistently outperformed standard QAOA in both approximation ratio and probability of measuring the optimum, especially when the relaxed continuous solution was close to the binary optimum ('hot' instances). However, the authors show that much of this gain can be reproduced by a classical preprocessing step that rounds near-binary relaxed variables, removes them, and then applies standard QAOA to the reduced problem. In several tested settings, this preprocessed standard QAOA matched or exceeded warm-start QAOA in approximation ratio, particularly at low depth, though warm-start often retained higher ground-state probability. Because all evidence is from simulator-based experiments on small instances, the paper does not demonstrate quantum advantage; instead, it argues that warm-start improvements in this application are largely attributable to classical information from the relaxation.

**Performance claims:**
- 20 random portfolio instances, each with N=10 assets and budget B=5, evaluated up to QAOA depth p=7 using 1000 simulator shots
- For random instances, classical baseline naive rounding (δ0=δ1=0.5) achieved mean r=P=15% (=3/20 solved exactly)
- For random instances, preprocessed standard QAOA with lower bounds achieved approximation ratio about r≈80% at p=7
- For random instances, preprocessed standard QAOA with δ0=δ1=0.25 achieved approximation ratio about r≈92% at p=7, matching warm-start within error bars
- For ε-cold instances at p=7, preprocessed standard QAOA achieved about rε≈89% versus warm-start rε,WS≈92%
- For σ-cold instances at p=7, preprocessed standard QAOA achieved about rσ≈83% versus warm-start rσ,WS≈86%
- For ε-hot instances, naive rounding baseline achieved r=P=100%
- For σ-hot instances, naive rounding baseline achieved r=P=85% (=17/20 solved exactly)
- For ε-hot instances at p=7 with δ0=δ1=0.25, preprocessed standard QAOA achieved about rε≈96.7% and Pε≈60% versus warm-start rε,WS≈96.9% and Pε,WS≈77%
- For σ-hot instances at p=7 with δ0=δ1=0.25, preprocessed standard QAOA achieved about rσ≈98% and Pσ≈86% versus warm-start rσ,WS≈96% and Pσ,WS≈83%
## Quantum advantage claim
**Classification:** speculative

This is a preprint with results from small-scale qasm-simulator experiments rather than real hardware, and the paper explicitly states that classical preprocessing can reproduce or surpass warm-start gains. It does not demonstrate quantum advantage; any future advantage discussion is speculative.
## Limitations
- As a preprint, the study has not undergone peer review.
- Experiments are limited to simulated quantum circuits (qasm simulator) rather than real quantum hardware, so hardware noise, calibration drift, and decoherence effects are not assessed.
- Problem size is small: the reported portfolio instances use N = 10 assets/qubits with budget B = 5, limiting conclusions about scalability.
- The evaluation uses only 20 instances per reported subset (random, hot, cold), which may limit statistical robustness despite generating 1000 instances for selection.
- QAOA depth is restricted to p <= 7, so conclusions may not hold for deeper circuits.
- The study does not consider the regularization parameter proposed in prior warm-start work to handle relaxed variables exactly equal to 0 or 1.
- The continuous relaxation is easy to solve in their setting because the matrix is positive semidefinite; this assumption may not hold for more general QUBO instances.
- The portfolio formulation is simplified to binary asset selection with a budget constraint, which omits many realistic financial constraints and market frictions.
- Performance is evaluated mainly via approximation ratio and ground-state probability, without reporting end-to-end runtime or total hybrid optimization cost.
- [inferred] No comparison is made against strong state-of-the-art classical portfolio optimization baselines beyond naive rounding and preprocessing, limiting claims about practical advantage.
- [inferred] The use of randomly generated instances and one example based on DAX data may not reflect real-world financial data diversity or nonstationarity.
- [inferred] Results may be sensitive to optimizer choice (gradient-based for relaxation, gradient-free for QAOA), but optimizer dependence is not systematically analyzed here.
- [inferred] Reproducibility may be limited because the paper does not fully specify all experimental settings in the main text (e.g., seeds, exact optimizer hyperparameters), instead referring to another source for details.
- [inferred] The preprocessing thresholds (δ0, δ1) are hand-chosen and tested on a small set of values, so conclusions may depend on heuristic parameter selection.
- [inferred] Since only simulator-based shot noise with a fixed 1000 shots is used, the study does not establish robustness under realistic sampling and hardware error conditions.
## Open questions
- How well do the observed advantages of classical preprocessing versus warm-start QAOA persist for larger portfolio instances with more assets/qubits?
- Would the conclusions change on real NISQ hardware where noise may affect warm-start and standard QAOA differently?
- How should the preprocessing bounds (δ0, δ1) be selected systematically or adaptively for different problem classes and instances?
- Under what conditions does warm-start QAOA provide genuinely quantum benefits beyond what can be achieved by classical preprocessing?
- How do these findings generalize beyond the specific portfolio optimization formulation studied here to other financial optimization problems or general QUBOs?
- What is the trade-off between higher approximation ratio and lower ground-state probability observed for preprocessed standard QAOA?
- How sensitive are the results to the choice of classical optimizer, initialization strategy, and hyperparameters?
- Would including the regularization parameter for warm-start QAOA alter the comparison with classical preprocessing?
- Can a principled decomposition of optimization routines into classical and quantum subroutines lead to measurable quantum advantage over purely classical methods?
- [inferred] How do the methods perform under more realistic financial constraints such as transaction costs, cardinality limits, turnover, and multi-period dynamics?

**Future work:**
- Explore further ways of splitting an optimization routine into classical and quantum processing parts.
- Investigate how targeted allocation of classical versus quantum steps can help realize a quantum advantage over purely classical methods.
- Develop a better understanding of which steps in the optimization routine can be replaced classically to improve overall performance.
- [inferred] Validate the approach on real quantum hardware to assess the impact of noise and device limitations.
- [inferred] Extend experiments to larger problem sizes and deeper QAOA circuits to test scalability.
- [inferred] Study systematic or learned methods for choosing preprocessing/rounding thresholds instead of fixed heuristic bounds.
- [inferred] Benchmark against stronger classical optimization baselines and industry-relevant portfolio solvers.
- [inferred] Apply the framework to more realistic financial portfolio models and other combinatorial finance problems.
## Key ideas
- #idea:hybrid-approach — A classical preprocessing stage based on solving the continuous relaxation, rounding near-binary variables, and eliminating fixed variables can match or exceed warm-start QAOA on small portfolio QUBOs.
- #idea:near-term-feasibility — The study evaluates shallow-depth QAOA (p up to 7) on 10-qubit portfolio instances, framing hybrid workflows as the practical NISQ-era path.
- #idea:hybrid-approach — Warm-start gains depend strongly on how informative the classical relaxation is; 'hot' instances are often largely solvable from classical information alone.
- #idea:near-term-feasibility — The paper treats warm-start QAOA as promising for combinatorial finance but explicitly avoids claiming demonstrated quantum advantage.
## Contradictions
- The paper contradicts implicit or explicit claims that warm-start QAOA's superior performance on portfolio optimisation is inherently quantum: on the tested instances, classical preprocessing plus standard QAOA reproduces or surpasses much of the reported gain.
- The paper undermines strong quantum-superiority narratives by showing that for 'hot' instances, naive classical rounding alone can solve most or all cases, implying the advantage comes from classical relaxation structure rather than quantum processing.
- The paper also contradicts broad scalability optimism for finance QAOA studies by restricting evidence to simulator-based experiments on N=10 assets/qubits and noting that no advantage over strong classical methods is established.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
