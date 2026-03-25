---
aliases:
- 'Error and Resource Estimates of Variational Quantum Algorithms for Solving

  Differential Equations Based on Runge-Kutta Methods'
- Error Resource Estimates Variational
authors:
- David Dechant
- Liubov Markovich
- Vedran Dunjko
- Jordi Tura
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
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:14:26.188891'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:14:30.804415'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:16.991025'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:03.493239'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:16:34.514707'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:16:44.610392'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Error and Resource Estimates of Variational Quantum Algorithms for Solving

  Differential Equations Based on Runge-Kutta Methods'
topic_tags:
- derivatives-pricing
year: 2026
zotero_key: ''
---

## Abstract summary
The paper analyzes variational quantum algorithms for solving differential equations that use classical Runge–Kutta methods to evolve variational parameters. It derives rigorous upper bounds on errors arising from Runge–Kutta truncation and from shot noise in quantum measurements, and then uses these to obtain resource estimates (numbers of time steps, measurements, and circuit evaluations) needed to reach a target accuracy. The framework is applied to a simple ODE and to a Black–Scholes option pricing PDE, showing how the optimal Runge–Kutta order depends on problem parameters and that, under conservative assumptions, required quantum resources can be very large.
## Methodology
This preprint is primarily a theoretical and analytical study, with limited numerical benchmarking used to illustrate the derived bounds. The authors analyze variational quantum algorithms (VQAs) for solving differential equations by combining classical Runge-Kutta methods (RKMs) with variational imaginary-time evolution. They formalize the parameter dynamics of the variational ansatz via McLachlan's variational principle, yielding an ODE of the form dθ/dτ = A^{-1}(θ)C(θ), where A and C are estimated from quantum circuit expectation values. The core methodology is to derive rigorous upper bounds on total error and resource requirements under two regimes: noiseless function evaluations and noisy evaluations affected by measurement shot noise. The analysis explicitly includes truncation error from RKMs and shot-noise-induced perturbations in estimating A and C, while excluding representation error, hardware noise, gate infidelity, SPAM errors, and regularization error from singular A matrices. The paper proves theorems for error propagation, derives expressions for the minimum number of time steps and measurements needed to meet a target error, and translates these into total circuit-evaluation counts. To illustrate the framework, the authors benchmark the theory on two cases: a simple 1D classical ODE without shot noise and a finance application based on the Black-Scholes PDE for option pricing, mapped to an imaginary-time Schrödinger equation and then solved with the variational framework. They also use a toy Fourier-like random model for entries of A and C to estimate quantities such as condition number, norms, and Lipschitz constants needed for resource calculations.

**Algorithms used:** Variational quantum algorithm for solving differential equations, Variational imaginary time evolution, Runge-Kutta methods, Euler method, McLachlan variational principle

**Experimental setup:** No physical quantum hardware experiments are reported. The work is mainly analytical, supplemented by numerical evaluation of derived error/resource formulas. The variational algorithm is described abstractly in terms of parameterized quantum circuits and ancilla-based measurement circuits for estimating matrix A and vector C. Numerical illustrations include a classical ODE example and a Black-Scholes option-pricing PDE example; hardware noise is explicitly excluded, and shot noise is modeled analytically via Gaussian/Chebyshev bounds rather than simulated on a named backend.

**Dataset:** No empirical dataset is used. Inputs are analytical differential-equation test problems: (1) a simple scalar ODE dθ/dτ = θ/2 with θ(0)=1, and (2) a finance PDE based on the Black-Scholes option-pricing model with typical parameter assumptions such as one-year maturity and volatility 0.2.
## Findings
- [speculative] The paper derives analytical upper bounds for total error and resource requirements of Runge-Kutta-based variational quantum algorithms for differential equations, explicitly combining truncation error and shot-noise error.
- [speculative] For noiseless Runge-Kutta ODE solving, the authors claim the total error scales with the method order p, time-step count N_tau, and Lipschitz/problem constants via their bound in Eq. (35), and derive a corresponding minimum-cost expression in Eq. (39).
- [speculative] Under shot noise, the authors claim the ODE parameter error is bounded by a sum of a truncation term and a measurement-noise term, leading to formulas for the minimum number of time steps and measurements per function evaluation in Eqs. (46) and (47).
- [speculative] The total number of quantum circuit evaluations for the variational algorithm is claimed to scale as N_circ = N_tau s N_r N_V N_d (N_V N_d + N), i.e., quadratically in the number of variational parameters N_V when other factors are fixed.
- [supported] In a numerical example for a simple classical 1D ODE without shot noise, the most resource-efficient Runge-Kutta method among orders 1-10 was order 4.
- [supported] In that noiseless ODE example, all tested Runge-Kutta methods of order 2 through 10 were more cost-efficient than Euler order 1 under the chosen parameter setting.
- [supported] For the noiseless ODE benchmark with target error 0.001, the order-4 Runge-Kutta method reduced estimated cost by about 2.22 x 10^3 relative to Euler.
- [supported] In the option-pricing Black-Scholes PDE case studied with the variational algorithm and the authors' default parameter estimates, the most resource-efficient Runge-Kutta method was order 2.
- [supported] For the option-pricing case with target error 0.001 and default estimates, the order-2 method reduced estimated total circuit evaluations by a factor of 13.18 relative to Euler.
- [supported] For the option-pricing case with target error 0.001 and default estimates, the authors estimate the algorithm would require about 1.62 x 10^28 total quantum circuit evaluations, making it impractical on current hardware.
- [supported] For the same option-pricing setup, the estimated measurements per circuit/function evaluation were about 3.87 x 10^22, corresponding to roughly classical machine precision in matrix/vector entries.
- [supported] The paper argues from its numerical estimates that matrix inversion in the variational update is the main driver of severe shot-noise amplification and resource overhead.
- [speculative] The authors suggest that related variational time-evolution approaches that avoid matrix inversion may require substantially fewer quantum circuit evaluations.
- [supported] In an alternative tuned parameter scenario for the option-pricing-style analysis, the best method became order 4, with an estimated savings factor of about 2.56 x 10^3 over Euler, though still far beyond feasible hardware limits.
- [speculative] The framework is claimed to be applicable beyond ODEs to PDEs and stochastic differential equations that can be mapped into the analyzed form.
- [speculative] The authors state that their bounds are worst-case and likely conservative, so practical resource needs could be lower for well-behaved instances.

**Results summary:** This preprint develops theoretical error and resource estimates for variational quantum algorithms that solve differential equations using Runge-Kutta methods, accounting for both truncation error and measurement shot noise while excluding representation error and hardware noise. The authors derive closed-form upper bounds for ODE solution error, minimum time steps, minimum measurements, and total circuit counts, then instantiate the framework in two numerical studies: a simple noiseless 1D ODE and a Black-Scholes option-pricing PDE solved via a variational quantum algorithm. In the noiseless ODE example, order-4 Runge-Kutta is estimated to be most resource-efficient, with about a 2.22 x 10^3 cost reduction versus Euler under the chosen parameters. In the option-pricing case, order-2 Runge-Kutta is estimated to minimize total circuit evaluations under default assumptions, but the required resources remain enormous: about 3.87 x 10^22 measurements per circuit evaluation and 1.62 x 10^28 total circuit evaluations for target error 0.001, implying the approach is not practical on current hardware. Because this is a preprint and the main contributions are analytical bounds plus numerical estimates rather than hardware demonstrations, any broader efficiency implications remain speculative.

**Performance claims:**
- Noiseless ODE benchmark: Euler/order-1 estimated cost = 2.25 x 10^7
- Noiseless ODE benchmark: order-2 estimated cost = 9.60 x 10^4
- Noiseless ODE benchmark: order-3 estimated cost = 1.99 x 10^4
- Noiseless ODE benchmark: order-4 estimated cost = 1.01 x 10^4
- Noiseless ODE benchmark: order-4 gives about 2.22 x 10^3 lower cost than Euler
- Noiseless ODE benchmark: order-4 requires N_tau about 2.54 x 10^3 time steps
- Option-pricing VQA benchmark (default parameters): Euler/order-1 total circuit evaluations N_circ = 2.13 x 10^29
- Option-pricing VQA benchmark (default parameters): order-2 total circuit evaluations N_circ = 1.62 x 10^28
- Option-pricing VQA benchmark (default parameters): order-2 gives 13.18x fewer total circuit evaluations than Euler
- Option-pricing VQA benchmark (default parameters): order-2 requires N_r about 3.87 x 10^22 measurements per function evaluation
- Option-pricing VQA benchmark (default parameters): order-2 requires N_tau about 2.04 x 10^2 time steps
- Option-pricing VQA benchmark (default parameters): order-2 uses about 4.19 x 10^5 distinct circuits
- Option-pricing VQA benchmark (default parameters): target error epsilon_target = 0.001
- Alternative tuned option-pricing-style scenario: order-4 total circuit evaluations N_circ = 4.39 x 10^33
- Alternative tuned option-pricing-style scenario: order-4 gives about 2.56 x 10^3 fewer total circuit evaluations than Euler
- Alternative tuned option-pricing-style scenario: order-4 requires N_r about 1.98 x 10^26 measurements per function evaluation
- Hardware feasibility comparison cited by authors: about 2 x 10^10 circuit evaluations could be executed in 24 hours on Sycamore-scale assumptions, far below the estimated 1.62 x 10^28 needed
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. It provides theoretical error/resource bounds and numerical estimates, and its main empirical-style conclusion for the finance use case is that the required resources are prohibitively large on current hardware. Any implication that optimized Runge-Kutta choices improve quantum performance is analytical and instance-dependent, not an experimentally validated advantage over classical methods.
## Limitations
- Lack of peer review as this is a preprint
- The analysis does not take into account representation errors of the variational ansatz, even though these affect both parameter evolution and final-state approximation
- Hardware noise is excluded from the analysis; gate infidelity, bias, and SPAM errors are assumed negligible
- The framework assumes the matrix A is invertible; cases requiring matrix regularization and the additional errors it introduces are not incorporated
- The derived error bounds are general upper bounds and may overestimate the true error in practice, making the resource estimates overly conservative
- Possible stability issues of the differential equations and numerical methods are not analyzed, despite being important for a full error/resource picture
- Several key quantities are only estimated via a toy model rather than derived from actual algorithm executions, including the condition number, norms of A and C, and Lipschitz constants
- The authors cannot verify all assumptions required by Theorem 1 for the option-pricing application because the full function f(theta(t)) is not explicitly known
- The option-pricing case study uses the Black-Scholes PDE, which has an analytic classical solution, limiting practical relevance of the benchmark
- For the option-pricing example, the estimated shot requirements are astronomically large (e.g., around 10^22 shots per circuit), making the approach unrealistic on current hardware
- Only a limited set of benchmark problems is studied: one simple ODE without shot noise and one finance PDE with shot noise
- [inferred] No experiments are run on real quantum hardware, so the practical impact of calibration drift, decoherence, connectivity constraints, and compilation overhead remains unvalidated
- [inferred] No direct empirical comparison is provided against state-of-the-art classical PDE/ODE solvers or classical option-pricing methods, so practical quantum advantage is not assessed
- [inferred] The analysis focuses on linear differential equations mapped to the variational framework; applicability to broader nonlinear finance models is not demonstrated
- [inferred] Resource estimates depend heavily on assumed constants (e.g., K, Lipschitz constants, condition number scaling), so conclusions may be sensitive to misspecification
- [inferred] The study is largely theoretical/analytical and lacks empirical validation of whether the proposed bounds are tight for realistic financial instances
## Open questions
- How feasible is the underlying matrix-inversion-based variational algorithm in practice, given the severe error propagation and shot requirements?
- Can related variational approaches that avoid matrix inversion substantially reduce total circuit evaluations?
- How much can the current worst-case resource estimates be tightened for specific, well-behaved problem instances?
- What is the impact of stability properties of the chosen differential equation and numerical method on total error and resources?
- How large are representation errors for realistic ansatz choices in finance applications, and how do they alter the overall conclusions?
- How do hardware noise and device-specific errors change the optimal choice of Runge-Kutta order?
- Can the toy-model-based estimates for condition numbers, norms, and Lipschitz constants be validated on real variational circuits and real problem instances?
- Would linear multistep methods or other general linear methods outperform Runge-Kutta methods under comparable noise and accuracy constraints?
- How much parallelism is realistically achievable for the large number of circuit evaluations assumed in the resource model?
- Can the framework be extended to more practically relevant financial PDEs or stochastic models that do not admit simple analytic solutions?

**Future work:**
- Include stability analysis of the differential equations and numerical methods to obtain a more complete error and resource characterization
- Incorporate representation errors of the ansatz into the overall error analysis
- Account for circuit-level noise sources such as gate infidelity, bias, and SPAM errors, as well as errors from matrix regularization
- Tighten pessimistic bounds in the analysis, especially the local truncation error bounds and shot-noise estimates
- Combine the framework with recent methods that reduce the number of state preparations for estimating the matrix A from O(N_V^2) to O(N_V)
- Adapt the analysis to linear multistep methods, which may reduce resource requirements by reusing previous stage evaluations
- Formulate the noisy differential-equation analysis in a stochastic differential equation framework, since shot noise is modeled as Gaussian noise
- Apply the framework to other quantum algorithms for differential equations with similar error sources
- Apply the framework to classical algorithms that use noisy data
- Explore applications of the framework to neural-network training dynamics
- Investigate use cases beyond the Black-Scholes benchmark where careful parameter analysis may identify more resource-efficient Runge-Kutta orders
- [inferred] Validate the analytical resource estimates with simulations or experiments on real quantum hardware
- [inferred] Benchmark against strong classical baselines to determine whether any practical advantage is possible in financial applications
- [inferred] Study more realistic and complex financial models beyond analytically solvable Black-Scholes dynamics
## Key ideas
- #idea:hybrid-approach — The paper studies a hybrid variational quantum workflow where classical Runge–Kutta integration evolves parameters estimated from quantum circuits.
- #idea:near-term-feasibility — It provides analytical error and resource bounds for applying variational differential-equation solvers to Black–Scholes option pricing in a NISQ-style setting.
- #idea:near-term-feasibility — Higher-order Runge–Kutta choices can reduce estimated circuit counts versus Euler for fixed target accuracy, with order-2 best in the default Black–Scholes case.
- #idea:near-term-feasibility — The main practical conclusion is negative: even optimized settings require astronomically large measurements and circuit evaluations for the option-pricing example.
- #idea:hybrid-approach — The analysis identifies matrix-inversion-based variational updates as the main source of shot-noise amplification, motivating alternative hybrid variational schemes that avoid explicit inversion.
## Contradictions
- The paper undercuts broad #idea:quantum-advantage narratives by concluding that the Black–Scholes variational quantum approach would require about 1.62e28 circuit evaluations and is therefore impractical on current hardware.
- It contradicts optimistic scalability claims for near-term variational finance algorithms: although higher-order Runge–Kutta methods improve relative efficiency, absolute resource requirements still remain far beyond feasible execution.
- The finance benchmark uses Black–Scholes, which has an analytic classical solution, so the study implicitly challenges claims of practical quantum superiority for this use case in the absence of direct classical baseline wins.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Two problem inputs are used for numerical illustration. First, a 1D ODE dθ/dτ = θ/2 with initial condition θ(0)=1 and final time T=5, whose exact solution is exp(τ/2). Second, a European call option pricing problem governed by the Black-Scholes PDE, transformed via τ=(t_final-t)σ^2 and x=log(S) into an imaginary-time Schrödinger-type equation ∂u/∂τ = (1/2)∂^2u/∂x^2. The option payoff is V(t_final,S)=max(S-K,0). For the finance case, the paper assumes a discretized stock-price interval encoded on n qubits, with basis states corresponding to grid points; typical parameters include t_final≈1 year, volatility σ≈0.2, transformed horizon T≈0.04, Hamiltonian term count N=16, variational parameter count N_V=25, and N_d=1. Additional numerical inputs include target error ε_target≈0.001 and toy-model-generated surrogate coefficients for A and C.

### Process
The methodological pipeline is: (1) formulate the target DE, especially linear DEs of the form dy/dτ = -Hy; (2) map the solution vector to a normalized quantum state and approximate it with a parameterized ansatz |φ(θ)>; (3) apply McLachlan's variational principle to derive the parameter ODE A(θ) dθ/dτ = C(θ), equivalently dθ/dτ = A^{-1}(θ)C(θ) when A is invertible; (4) estimate entries of A and C from ancilla-based quantum circuits measuring real parts of overlaps/expectation values; (5) solve the parameter ODE using s-stage RKMs of order p, including Euler and higher-order methods; (6) derive and evaluate analytical upper bounds for total ODE error from truncation and shot noise, with shot noise modeled as bounded perturbation δ = Σ/sqrt(N_r); (7) optimize over the number of time steps N_τ and measurements per function evaluation N_r to satisfy a target error; (8) convert these into total circuit counts N_circ = N_τ s N_r (N_V^2 N_d^2 + N_V N_d N); (9) benchmark the formulas numerically across RKM orders p=1 to 10 for the classical ODE and Black-Scholes use case; and (10) perform sensitivity analyses by varying parameters such as T, L_fy, b_max, K, Σ, and ε_target. The paper also introduces a toy Fourier-like random model for A and C entries to estimate condition numbers, norms, and Lipschitz constants used in the resource formulas.

### Output
Outputs are analytical error bounds and resource estimates rather than predictive finance performance metrics. Reported results include upper bounds on ε_ODE and ε_total, minimum required time steps N_τ, minimum measurements per function evaluation N_r, total cost C, and total circuit evaluations N_circ. Comparisons are made across Runge-Kutta orders, especially against the Euler method baseline (p=1). For the simple ODE, the paper reports that order-4 RKMs are most resource-efficient under chosen parameters. For the Black-Scholes option-pricing example, order-2 RKMs are reported as most resource-efficient under the default parameter setting, with explicit tables of N_circ, N_r, N_τ, and savings ratios relative to Euler. The paper also reports sensitivity plots showing how resource estimates vary with parameters such as target error, Lipschitz constants, total time, and shot-noise constant.

### Parameters
- classical_ode_example: {'equation': 'dθ/dτ = θ/2', 'initial_condition': 'θ(0)=1', 'final_time_T': 5, 'target_error': 0.001, 'estimated_parameters': {'b_max': 1, 'L_fy': 0.5, 'K': 5, 'L_fτ': 3.1, 'M': 13}, 'rkm_orders_evaluated': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
- black_scholes_vqa_example: {'problem': 'European call option pricing via transformed Black-Scholes PDE', 'target_error': 0.001, 'transformed_time_T': 0.04, 'hamiltonian_terms_N': 16, 'variational_parameters_N_V': 25, 'N_d': 1, 'eta': 0.05, 'default_estimated_parameters': {'a_max': 1, 'b_max': 1, 'L_fy': 15, 'K': 5, 'L_fτ': 15, 'M': 60, 'S': 1, 'Sigma': 340000000.0}, 'alternative_tuned_parameters': {'a_max': 1, 'b_max': 0.5, 'L_fy': 0.1, 'T': 4, 'K': 20, 'L_fτ': 15, 'M': 60, 'S': 1, 'Sigma': 340000000.0, 'target_error': 0.001}, 'rkm_orders_evaluated': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

### Hardware
{'quantum_hardware_used': 'None; no actual QPU execution reported', 'simulation_type': 'Analytical shot-noise model and numerical evaluation of formulas', 'circuit_model': 'Ancilla-based circuits for estimating A and C expectation values; parameterized ansatz circuit R(θ)', 'noise_model': 'Shot noise included analytically; hardware noise, gate infidelity, SPAM, and representation error excluded', 'external_hardware_reference': 'Google Sycamore timing/recalibration figures cited only for feasibility discussion, not used experimentally'}

### Reproducibility
Preprint. The paper provides extensive mathematical derivations, theorem statements, parameter tables, and numerical result tables/figures, so the analytical calculations are in principle reproducible. However, no code repository or executable implementation is mentioned in the provided text, and some numerical estimates rely on heuristic/tuned parameter choices and a toy random model for A and C, which may limit exact replication unless further implementation details are supplied.
