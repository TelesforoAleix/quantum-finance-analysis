---
aliases:
- Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
- Higher Order Portfolio Optimization
authors:
- Valter Uotila
- Julia Ripatti
- Bo Zhao
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/QCE65121.2025.00244
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:12:13.870147'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:12:18.580287'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:07.051043'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:13:41.865439'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:14:10.820296'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:14:20.954208'
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
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces a quantum formulation of portfolio optimization that incorporates higher-order moments of return distributions, specifically skewness and kurtosis, leading to a higher-order unconstrained binary optimization (HUBO) problem rather than the usual QUBO. The authors encode realistic integer decision variables and a capital-based budget constraint, and solve the resulting HUBO instances using QAOA, comparing performance against a classical continuous-variable portfolio optimizer with integer-programming-based discretization over 100 Dow Jones-based test cases. They find that the HUBO formulation can yield better portfolio allocations than the classical baseline, and use the experiments to study the behavior and challenges of QAOA on practically motivated higher-order optimization problems in finance.
## Methodology
This conference paper presents an empirical and methodological study of higher-order portfolio optimization formulated as a higher-order unconstrained binary optimization (HUBO) problem and solved with the Quantum Approximate Optimization Algorithm (QAOA). The authors extend classical portfolio optimization beyond mean-variance by incorporating skewness and kurtosis, yielding cubic and quartic terms in the objective. They first define a classical continuous-variable higher-moment portfolio optimization baseline, then discretize its solution using integer programming. In parallel, they formulate an integer-variable capital-constrained optimization problem, convert the budget constraint into a penalty term, and encode integer asset quantities into binary variables using logarithmic encoding, producing a HUBO Hamiltonian with interaction order up to 4. This Hamiltonian is mapped to Pauli-Z operators and implemented as a QAOA cost circuit with a standard X-mixer. The empirical evaluation uses 100 randomly generated portfolio optimization instances derived from Dow Jones Industrial Average constituents, with problem sizes selected to fit within a 15-qubit simulation limit. The study compares exact HUBO solutions, QAOA solutions, and two classical continuous-variable baselines (constrained and unconstrained, both followed by discretization). It also benchmarks several classical optimizers for the QAOA parameter optimization loop and reports solution quality in terms of normalized objective value and budget utilization, along with additional analyses of circuit depth/gate counts, spectral properties, and allocation divergence between QUBO and HUBO formulations. The paper notes that implementation code is available on GitHub.

**Algorithms used:** QAOA, SLSQP, COBYLA, CMA-ES, Nelder-Mead, L-BFGS-B, Powell
**Frameworks:** Qiskit, PennyLane, SciPy, CVXPY, yfinance, pytickersymbols

**Experimental setup:** Experiments were conducted on simulated portfolio optimization instances encoded as HUBO/QAOA problems with 6 to 15 qubits. The authors generated 100 random problem instances, ensuring ten instances for each qubit count from 6 to 15. Exact eigenspectrum computation was used for problems with fewer than 14 qubits, while a sparse eigensolver was used for 14- and 15-qubit cases to approximate the smallest eigenvalues. QAOA circuits used standard Hadamard initialization, cost unitaries derived from Pauli-Z products up to 4-local terms, and a standard X-mixer. Classical baselines were solved using continuous optimization and integer-programming-based discretization.

**Dataset:** Historical stock market data for the 30 Dow Jones Industrial Average (DJIA) companies, downloaded from Yahoo Finance via yfinance. Portfolio instances were created by randomly sampling between 2 and 10 companies and assigning a random budget capped at 6000.
## Findings
- [supported] The paper introduces a higher-order portfolio optimization formulation that includes skewness and kurtosis, producing a higher-order unconstrained binary optimization (HUBO) problem rather than a QUBO.
- [supported] In experiments on 100 randomly generated portfolio optimization instances derived from DJIA data, exact solutions to the HUBO formulation often yielded better portfolio allocations than the classical continuous-variable baseline with integer-programming discretization.
- [supported] The exact HUBO solver achieved 100/100 cases with budget utilization between 95% and 105%, compared with 74/100 for the constrained classical baseline and 70/100 for the unconstrained classical baseline.
- [supported] The exact HUBO solver achieved min-max normalized objective values of at least 0.95 in 53/100 cases, versus 70/100 for the constrained classical baseline and 68/100 for the unconstrained classical baseline.
- [supported] When requiring both near-budget feasibility (95% to 105% utilization) and high objective quality (normalized objective at least 0.95), the exact HUBO solver satisfied both in 53/100 cases, compared with 50/100 for the constrained classical baseline and 46/100 for the unconstrained classical baseline.
- [supported] QAOA performed poorly relative to exact HUBO solving and classical baselines on this problem class, satisfying both the budget-utilization and objective-quality criteria in only 3/100 instances.
- [supported] The authors benchmarked six classical optimizers for the QAOA outer loop and report that CMA-ES often achieved the lowest average objective values among optimizers that completed enough instances.
- [supported] Across all tested cases, QAOA increased the probability of measuring the minimizing state by an average factor of 14.43 over uniform random sampling, with observed enhancement factors ranging from 3.79 to 108.94.
- [supported] The authors report that larger penalty weights for the budget term generally performed better, with values greater than 1 often giving the best QAOA results.
- [supported] For small qubit counts, the spectral differences between the higher-order HUBO and corresponding mean-variance QUBO formulations were very small, on the order of 10^-9 to 10^-11, but the differences became more pronounced as qubit count increased.
- [supported] As problem size increased, HUBO and QUBO produced increasingly different allocations, and HUBO solutions stayed closer to uniform allocations, which the authors interpret as producing more diversified portfolios.
- [supported] The study uses simulation and exact/sparse eigensolvers for HUBO instances up to 15 qubits; no real quantum hardware results are reported in this paper.
- [speculative] The authors argue that HUBO problems are a promising class for future quantum hardware because classical solvers do not natively support them well and because higher-moment portfolio optimization is classically complex.
- [speculative] The paper suggests that QAOA may need modifications to its optimization pipeline to effectively solve more complex real-world HUBO portfolio problems.
- [speculative] The authors suggest that quantum methods could potentially address scalability limitations of classical approaches for HUBO problems, but this is not demonstrated here.

**Results summary:** This conference paper formulates portfolio optimization with higher moments (skewness and kurtosis) as a higher-order unconstrained binary optimization problem and evaluates it on 100 portfolio instances built from 10 years of DJIA stock data. The study compares exact/sparse eigensolver solutions of the HUBO formulation, QAOA-based solutions, and classical continuous-variable baselines with discretization. Exact HUBO solutions often produced better overall allocations than the classical baselines when considering both objective quality and budget utilization, achieving both target criteria in 53 of 100 cases versus 50 and 46 for the two classical baselines. However, QAOA struggled on these higher-order instances, meeting both criteria in only 3 of 100 cases, despite improving the probability of sampling the minimizing state by an average factor of 14.43 over random guessing. The experiments were conducted via simulation and classical exact/sparse solvers up to 15 qubits, not on real quantum hardware. The paper concludes that higher-order portfolio optimization is a promising quantum-native formulation, but practical quantum performance remains limited with current QAOA methods.

**Performance claims:**
- 100 portfolio optimization instances evaluated
- Problem sizes ranged from 6 to 15 qubits, with 10 random problems per qubit count
- Exact HUBO: 100/100 cases with 95% <= budget utilization <= 105%
- Constrained classical baseline: 74/100 cases with 95% <= budget utilization <= 105%
- Unconstrained classical baseline: 70/100 cases with 95% <= budget utilization <= 105%
- QAOA: 19/100 cases with 95% <= budget utilization <= 105%
- Constrained classical baseline: 70/100 cases with min-max normalized objective >= 0.95
- Unconstrained classical baseline: 68/100 cases with min-max normalized objective >= 0.95
- QAOA: 23/100 cases with min-max normalized objective >= 0.95
- Exact HUBO: 53/100 cases with min-max normalized objective >= 0.95
- Intersection of both criteria: constrained classical 50/100, unconstrained classical 46/100, QAOA 3/100, exact HUBO 53/100
- Average QAOA enhancement factor over random sampling: 14.43x
- Worst observed QAOA enhancement factor: 3.79x
- Best observed QAOA enhancement factor: 108.94x
- Spectral difference between HUBO and QUBO at small qubit counts reported at approximately 10^-9 to 10^-11
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. Results are from simulation/classical exact or sparse eigensolvers and simulated QAOA up to 15 qubits. While the authors argue that higher-order portfolio optimization may be promising for quantum hardware and that HUBO formulations can encode better allocations than classical baselines, QAOA underperformed in practice and no speedup or hardware-based advantage was shown.
## Limitations
- QAOA struggled to match the quality of exact HUBO solutions or classical algorithms on most tested higher-order portfolio instances; only a small subset of problems achieved comparable quality.
- Experiments were limited to simulated problems up to 15 qubits because larger instances were not simulable with available resources.
- Budgets were capped at 6000 to keep the resulting QAOA circuits simulable, constraining the realism and scale of tested portfolio instances.
- The study used only 100 random portfolio optimization problems constructed from 2 to 10 DJIA companies, limiting coverage of larger and more diverse financial universes.
- For 14- and 15-qubit cases, the authors used a sparse eigensolver that approximates only the smallest eigenvalues rather than the full spectrum.
- The penalty formulation for the budget constraint in Eq. (15) is symmetric and does not distinguish between over-budget and under-budget allocations, even though overspending may be infeasible in practice.
- Although the authors describe an alternative encoding intended to prevent overspending, they did not use it because it increases qubit requirements substantially.
- Selection of the penalty parameter λ materially affects performance, and the paper does not provide a principled or general method for choosing λ across instances.
- The optimizer comparison for QAOA is incomplete; the authors explicitly note it lacks noise analysis and hyperparameter search.
- Resource requirements for solving HUBO problems with QAOA are likely too demanding for current hardware.
- Results are only partially shown in the paper due to space limitations, with complete detailed results deferred to GitHub.
- [inferred] No experiments were run on real quantum hardware, so hardware noise, decoherence, connectivity constraints, and sampling overhead were not empirically assessed.
- [inferred] No direct comparison was made against stronger native classical HUBO solvers (e.g., specialized integer programming, tensor-network, annealing, or learning-based methods) beyond the continuous-variable baseline with discretization.
- [inferred] The claimed advantage is relative to a specific classical baseline, not to state-of-the-art classical optimization for higher-order discrete portfolio problems.
- [inferred] The use of only DJIA constituents and a single 10-year historical window may limit generalizability across markets, regimes, and asset classes.
- [inferred] The choice of risk-aversion scaling and moment weights is fixed rather than stress-tested, so conclusions may depend on parameterization.
- [inferred] Estimation error in higher moments (skewness/cokurtosis), which is typically substantial in finance, is not systematically analyzed.
- [inferred] Transaction costs, market impact, liquidity constraints, short selling, and other production portfolio constraints are omitted, limiting practical applicability.
- [inferred] The study does not establish quantum advantage or favorable asymptotic scaling; practical performance is demonstrated only on small simulated instances.
- [inferred] As a conference paper, page limits likely restricted methodological detail, ablation studies, and reporting of full experimental diagnostics.
## Open questions
- How can QAOA be improved so that it solves higher-order binary portfolio optimization problems more efficiently?
- What optimization strategies or classical subroutines are best suited for HUBO portfolio problems?
- How should the budget-penalty parameter λ be selected systematically across different instances?
- Would the alternative budget encoding that prevents overspending improve practical solution quality enough to justify its added qubit overhead?
- How does QAOA performance scale beyond 15 qubits and for larger portfolios with more assets and larger budgets?
- How robust are the results to different choices of risk-aversion and the scaling coefficients q0, q1, and q2?
- To what extent do higher-order moments materially improve portfolio quality versus mean-variance formulations in realistic out-of-sample settings?
- Why do HUBO formulations often encode better allocations than the chosen classical baseline, and does this persist against stronger classical discrete optimizers?
- How much of QAOA's difficulty is caused by rugged energy landscapes and local minima in higher-order portfolio instances?
- Will the observed diversification effect of HUBO solutions translate into better financial performance or risk control in practice?
- How would the method perform under realistic quantum hardware noise and limited circuit depth?
- Can the approach be extended to more realistic financial settings with transaction costs, liquidity limits, and dynamic or multi-period rebalancing?

**Future work:**
- Improve QAOA for higher-order binary optimization problems.
- Develop better optimization strategies and classical subroutines tailored to HUBO problems.
- Explore tensor-network methods for solving or assisting HUBO portfolio optimization.
- Investigate Bayesian optimizers for the QAOA optimization loop.
- Study methods that allow QAOA to tackle HUBO problems more efficiently as qubit counts increase.
- Further research higher-order binary optimization with quantum methods, motivated by the strong solution quality of exact HUBO formulations.
- [inferred] Evaluate the approach on real quantum hardware with noise-aware compilation and error mitigation.
- [inferred] Benchmark against stronger classical discrete/HUBO baselines to clarify whether benefits persist beyond the chosen continuous-discretized baseline.
- [inferred] Test larger and more realistic financial datasets, including more assets, other indices, and different market regimes.
- [inferred] Analyze alternative budget encodings that explicitly forbid overspending while controlling qubit overhead.
- [inferred] Perform sensitivity analyses over λ, risk-aversion, and higher-moment estimation choices.
- [inferred] Extend the formulation to include practical portfolio constraints such as transaction costs, cardinality, turnover, and liquidity.
## Key ideas
- #idea:hybrid-approach — The paper formulates higher-moment portfolio optimization with skewness and kurtosis as a higher-order binary problem (HUBO) and solves it with QAOA plus classical outer-loop optimization.
- #idea:quantum-advantage — The authors suggest higher-order portfolio optimization may be a promising quantum-native setting because exact HUBO solutions often outperform the chosen classical continuous-plus-discretization baseline on allocation quality and budget utilization.
- #idea:near-term-feasibility — The study explores NISQ-style QAOA on practically motivated finance instances, but only on very small simulated problems up to 15 qubits.
- #idea:hybrid-approach — Classical optimizers such as CMA-ES, COBYLA, and SLSQP are used to tune QAOA parameters, making the workflow explicitly quantum-classical hybrid.
- #idea:quantum-advantage — QAOA increased the probability of sampling the minimizing state relative to uniform random sampling by an average factor of 14.43, though this did not translate into competitive end-to-end solution quality.
- #idea:hybrid-approach — The paper highlights that HUBO and standard mean-variance QUBO formulations can produce increasingly different allocations as problem size grows, with HUBO tending toward more diversified portfolios.
## Contradictions
- The paper motivates quantum promise for higher-order portfolio optimization, but its own simulated QAOA results underperform both exact HUBO solving and the classical baselines on most instances, supporting contradiction:classical-vs-quantum.
- The paper suggests potential scalability benefits for quantum methods on HUBO problems, yet experiments are restricted to 6-15 qubits and QAOA quality deteriorates badly at this scale, supporting contradiction:scalability.
- Claims that HUBO-based formulations outperform classical methods are only shown against a specific continuous-variable baseline with discretization, not against stronger native classical discrete/HUBO solvers, which weakens any implied quantum superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input data consisted of daily stock prices for DJIA constituents from 2015-01-01 to 2025-01-01. Tickers for the 30 DJIA companies were obtained using pytickersymbols, and price data were downloaded with yfinance. For each synthetic portfolio optimization instance, 2 to 10 companies were randomly sampled and assigned a random capital budget up to 6000. Returns were computed from price differences, mean returns were annualized using the geometric mean with frequency 252, covariance was annualized, and coskewness/cokurtosis tensors were computed from return data. Instances requiring more than 15 qubits after integer-to-binary encoding were excluded. The final benchmark set contained 100 instances, with 10 instances for each qubit count from 6 to 15.

### Process
1. Download DJIA ticker symbols and 10 years of historical price data. 2. Randomly sample 2-10 assets and assign a random budget capped at 6000. 3. Compute asset returns, annualized geometric mean returns, covariance matrix, coskewness tensor, and cokurtosis tensor. 4. Build the higher-order continuous portfolio optimization objective and solve the constrained baseline with SciPy SLSQP; discretize the resulting weights using an integer program solved with CVXPY. 5. Build an unconstrained continuous baseline with a quadratic budget penalty and discretize similarly. 6. Formulate the integer higher-order portfolio optimization problem with objective q2*K(z) - q1*S(z) + q0*z^T c z - mu^T z + lambda(z^T p - C)^2, using risk-aversion-derived coefficients q0 = risk_aversion/2, q1 = risk_aversion/6, q2 = risk_aversion/24 and risk_aversion = 3. 7. Encode integer asset quantities into binary variables using logarithmic encoding based on each asset's maximum affordable quantity under the budget. 8. Map binary variables to spin variables and construct the HUBO Hamiltonian with Pauli-Z terms up to degree 4. 9. Build QAOA circuits with standard X-mixer and optimize QAOA parameters using classical optimizers; six optimizers were benchmarked, and CMA-ES was selected for the main experiments. 10. For CMA-ES, use sigma = 0.1, default remaining hyperparameters, and a limited number of iterations. 11. Sweep penalty values lambda in {0.001, 0.01, 0.1, 0.9, 1.0, 10, 100, 1000} and report QAOA performance using the most suitable lambda per problem; values above 1 generally performed best. 12. For <14 qubits, compute exact eigenspectra; for 14-15 qubits, use a sparse eigensolver to approximate the lowest eigenvalues. 13. Evaluate each method's discrete allocation using normalized objective value and budget utilization, and additionally analyze enhancement factor, circuit metrics, spectra, and KL divergence of allocations.

### Output
Primary outputs were discrete portfolio allocations and their evaluation under two criteria: (1) min-max normalized objective value derived from the higher-order portfolio objective without the budget penalty, and (2) budget utilization relative to the target capital. Results were visualized as scatter plots with budget utilization versus normalized objective value. The study compared QAOA, exact HUBO solutions, constrained classical continuous optimization plus discretization, and unconstrained continuous optimization plus discretization. Summary counts were reported for solutions within 95%-105% budget utilization, solutions with normalized objective >= 0.95, and the intersection of both criteria. Additional outputs included optimizer comparison curves with 95% confidence intervals, QAOA enhancement factors over random measurement probability, gate count and circuit depth comparisons between QUBO and HUBO formulations, eigenvalue spectra, and KL-divergence-based comparisons of portfolio allocation diversity.

### Parameters
- qubit_range: 6-15
- num_instances: 100
- instances_per_qubit_count: 10
- assets_per_instance: 2-10
- budget_cap: 6000
- time_period: 2015-01-01 to 2025-01-01
- annualization_frequency: 252
- risk_aversion: 3
- q0: 1.5
- q1: 0.5
- q2: 0.125
- lambda_values_tested: [0.001, 0.01, 0.1, 0.9, 1.0, 10, 100, 1000]
- qaoa_mixer: standard X-mixer
- cma_es_sigma: 0.1
- classical_optimizers_benchmarked: ['Powell', 'SLSQP', 'COBYLA', 'CMA-ES', 'Nelder-Mead', 'L-BFGS-B']
- exact_solver_threshold: <14 qubits exact eigensolver; 14-15 qubits sparse eigensolver

### Hardware
{'hardware_type': 'simulator/classical computation only', 'simulator_constraint': 'instances selected to fit a 15-qubit simulator', 'quantum_hardware_used': 'none reported', 'solver_details': 'exact eigensolver for <14 qubits; sparse eigensolver for 14-15 qubits'}

### Reproducibility
Code is reported as available on GitHub (quantum-portfolio repository). Data sources are public (DJIA constituents via pytickersymbols and price data via yfinance). The paper provides substantial detail on formulation, dataset construction, optimizer choices, lambda sweep, and evaluation, though some QAOA details such as circuit depth/layer count and exact iteration limits are not fully specified, so replication appears feasible but not perfectly complete.
