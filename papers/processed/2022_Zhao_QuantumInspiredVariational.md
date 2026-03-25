---
aliases:
- 'Quantum-inspired variational algorithms for partial diﬀerential

  equations: Application to ﬁnancial derivative pricing'
- Quantum inspired variational algorithms
authors:
- Tianchen Zhao
- Chuhao Sun
- Asaf Cohen
- James Stokes
- Shravan Veerapaneni
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:58:56.268930'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:59.865372'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:59:43.329678'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:00:24.052443'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:00:53.433992'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:01:05.383266'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum-inspired variational algorithms for partial diﬀerential

  equations: Application to ﬁnancial derivative pricing'
topic_tags:
- derivatives-pricing
year: 2022
zotero_key: ''
---

## Abstract summary
The paper generalizes McLachlan’s time-dependent variational principle to a broad class of time-dependent partial differential equations and implements it using neural-network quantum states in a variational Monte Carlo framework. The authors develop a mesh-based, autoregressive neural-network representation that enables approximate time evolution in high-dimensional PDEs with polynomial rather than exponential scaling. They demonstrate the approach on diffusion equations and then apply it to multi-asset Black–Scholes PDEs for pricing various European-style options, comparing accuracy and runtime against finite-difference Euler schemes.
## Methodology
This preprint presents a quantum-inspired, primarily empirical methodology for solving high-dimensional time-dependent PDEs and applying the approach to financial derivative pricing. The authors generalize McLachlan’s variational principle to arbitrary time-dependent PDEs, discretize the spatial domain on a regular mesh, and represent the PDE solution as an unnormalized neural-network quantum state of the form u_theta = alpha * psi_beta, where psi_beta is a unit-normalized autoregressive neural-network quantum state. The method uses variational quantum Monte Carlo (VMC) style importance sampling to estimate the overlap matrix M and driving vector V in the induced parameter-space ODE M(theta) * theta' = V(t, theta). The neural ansatz is pretrained to match the PDE initial condition via stochastic gradient descent, then evolved in time using Euler updates obtained by solving a regularized linear system based on Monte Carlo estimates. Numerical experiments are conducted first on high-dimensional diffusion/heat equations to study convergence, runtime scaling, and batch-size effects, and then on multi-asset Black-Scholes option pricing problems by transforming the Black-Scholes PDE into a multidimensional heat equation. Performance is evaluated against forward Euler finite-difference baselines and, in 1D Black-Scholes cases, against the analytical Black-Scholes formula. As a preprint, the work should be treated as not yet peer reviewed.

**Algorithms used:** Variational Quantum Monte Carlo, McLachlan variational principle, Autoregressive neural-network quantum states, Adam, Forward Euler, Finite difference method, Singular value decomposition
**Frameworks:** BackPack

**Experimental setup:** All experiments are classical/quantum-inspired rather than run on quantum hardware. The PDE domain is discretized on a regular grid with 2^n points and encoded as an n-qubit state representation. The neural ansatz uses an autoregressive architecture inspired by MADE for normalized sampling. Pretraining is performed with Adam, followed by time evolution using Monte Carlo estimation of the variational ODE terms and Euler parameter updates. Forward Euler finite-difference solvers are used as baselines for diffusion and Black-Scholes comparisons. Computational resources were provided by Advanced Research Computing (ARC) at the University of Michigan, and CPU parallelization was used for extracting sparse operator row entries.

**Dataset:** No external dataset is used. Inputs are synthetic PDE instances: d-dimensional diffusion/heat equations with discrete isotropic Gaussian initial conditions, and financial derivative pricing problems derived from the multi-asset Black-Scholes PDE, including 1D European call options and 2D basket call, basket put, rainbow max call, and spread put options under specified model parameters.
## Findings
- [speculative] The paper generalizes McLachlan’s variational principle from time-dependent Schrödinger equations to arbitrary time-dependent PDEs, including the multi-asset Black-Scholes PDE.
- [supported] The proposed quantum-inspired variational Monte Carlo method with autoregressive neural-network quantum states approximately solves high-dimensional diffusion PDEs and Black-Scholes-type pricing problems in numerical experiments.
- [speculative] The authors claim the approach can overcome the curse of dimensionality by replacing exponential-state evolution with stochastic estimation and autoregressive neural representations.
- [supported] For diffusion problems with Dirichlet boundary conditions, the method’s average relative error versus forward Euler increases with dimensionality but remains below about 10% in several tested settings and reaches 14.7% in a harder 4D setting with 4 qubits per dimension.
- [supported] Increasing Monte Carlo batch size materially improves accuracy; the paper states relative error can improve from about 15% to around 3% when batch size is increased by roughly 10x.
- [supported] The method empirically obeys periodic boundary conditions in 2D diffusion experiments without explicit regularization, based on qualitative convergence visualizations.
- [supported] The authors derive and report polynomial runtime scaling for their method, O(T B poly(n)), versus O(T × 2^(2n)) for forward Euler on the discretized grid, and provide timing experiments consistent with this trend.
- [supported] In the reported timing experiments, the proposed method becomes faster than forward Euler at problem size n = 16 qubits, while forward Euler becomes infeasible for higher dimensions due to memory limits.
- [supported] For 1D Black-Scholes European call pricing, the method achieves relative errors against the analytic Black-Scholes formula mostly in the 1.0%–3.3% range, with one higher-error case of 8.68% under a low strike setting.
- [supported] For 2D option pricing tasks benchmarked against Euler solutions, relative errors are reported as 5.35% for basket call, 4.39% for basket put, 5.79% for rainbow max call, and 3.16% for spread put.
- [supported] The method appears robust across tested variations in volatility, interest rate, strike price, expiry, and initial stock price in 1D Black-Scholes experiments.
- [speculative] The authors suggest the framework could extend to free-boundary problems such as American option pricing and to mesh-free variants based on continuous-variable neural-network quantum states.

**Results summary:** This preprint proposes a quantum-inspired, not quantum-hardware-based, variational Monte Carlo framework for solving time-dependent PDEs using autoregressive neural-network quantum states, and applies it to high-dimensional diffusion equations and financial derivative pricing via the multi-asset Black-Scholes PDE. The paper provides numerical evidence from classical simulations that the method can approximate forward Euler solutions for diffusion problems and analytic or Euler benchmarks for option pricing with moderate error. It reports polynomial runtime scaling in the number of qubits used to encode the mesh, contrasting this with the exponential scaling of forward Euler on the full grid, and shows empirical timing crossover around n = 16 qubits. In financial experiments, 1D Black-Scholes call pricing errors versus the analytic solution are generally low, while 2D exotic option pricing errors versus Euler remain in the low single-digit to mid-single-digit percentages. Because this is a preprint and all results are from classical numerical experiments rather than quantum hardware, any broader claims about overcoming the curse of dimensionality or achieving quantum-style advantage remain speculative.

**Performance claims:**
- Diffusion relative error vs forward Euler (Dirichlet, n/d=4): 5D 5.13e-3, 2D 7.92e-3, 3D 3.12e-2, 4D 1.47e-1
- Diffusion relative error vs forward Euler (Dirichlet, n/d=5): 2D 2.91e-3, 3D 9.91e-3, 4D 7.24e-2
- Claimed error improvement from about 15% to around 3% with roughly 10x larger batch size
- Runtime complexity claim: forward Euler O(T × 2^(2n)); proposed method O(T B poly(n))
- Reported forward Euler runtimes over 2k iterations, n/d=4: 1D 0.024s, 2D 0.137s, 3D 1.559s, 4D 305.92s
- Reported forward Euler runtimes over 2k iterations, n/d=5: 1D 0.031s, 2D 0.225s, 3D 68.827s
- Reported proposed-method runtimes over 2k iterations, n/d=4: 1D 29.52s, 2D 55.76s, 3D 138.88s, 4D 230.02s, 5D 360.80s, 6D 518.00s, 7D 792.63s, 8D 1214.09s, 9D 1812.94s
- Reported proposed-method runtimes over 2k iterations, n/d=5: 1D 32.53s, 2D 88.75s, 3D 173.43s, 4D 311.82s, 5D 507.93s, 6D 847.85s, 7D 1355.16s, 8D 2379.86s, 9D 4123.61s
- 1D Black-Scholes call relative error vs analytic solution: 0.011781, 0.032792, 0.017272, 0.011560 across volatility settings σ=0.3, 0.1, 0.2, 0.4
- 1D Black-Scholes call relative error vs analytic solution across strike settings K=1.05,1.15,1.35,1.45: 0.086764, 0.013365, 0.012260, 0.012626
- 1D Black-Scholes call relative error vs analytic solution across interest rates r=0.01,0.02,0.04,0.05: 0.010436, 0.010599, 0.014192, 0.017423
- 1D Black-Scholes call relative error vs analytic solution for expiry T=0.5 and 1.5: 0.022481 and 0.012049
- Corresponding forward Euler relative errors in 1D Black-Scholes are mostly lower, e.g. 0.002494, 0.000930, 0.002389, 0.001392
- 2D Black-Scholes relative error vs Euler: basket call 0.053477, basket put 0.043926, rainbow max call 0.057949, spread put 0.031574
## Quantum advantage claim
**Classification:** speculative

The paper is a preprint and studies a quantum-inspired classical algorithm using neural-network quantum states, not a quantum hardware implementation. It argues for polynomial scaling and overcoming the curse of dimensionality relative to grid-based Euler methods, but this is supported only by classical simulations and timing comparisons on limited benchmarks, so any advantage claim is speculative rather than demonstrated.
## Limitations
- The numerical experiments only consider the inhomogeneous linear case, even though the framework is claimed to apply to more general time-dependent PDEs.
- The implementation assumes spatial discretization on a predefined mesh, which introduces approximation error and does not fully realize the claimed generality of the method.
- The method requires regularization because the matrix M may be degenerate or ill-conditioned; in practice, small singular values are truncated, which may affect stability and accuracy.
- The approach uses only a first-order Euler approximation for the ODE evolution, limiting numerical accuracy.
- Benchmarking against forward Euler is only feasible for n <= 16 qubits because the baseline scales exponentially and hits memory constraints.
- The discrepancy between the proposed method and the forward Euler baseline increases as dimensionality increases.
- Good performance in higher dimensions requires larger Monte Carlo batch sizes, increasing runtime and resource usage.
- The proposed method is slower than forward Euler on lower-dimensional problems because of overhead from sampling, forward passes, per-sample gradient computation, and matrix-element extraction.
- The method provides only approximate time evolution and only implicit access to entries of the state vector, unlike grid-based solvers with direct lookup.
- For the autoregressive neural-network quantum state implementation, the paper assumes the state variable is strictly positive, restricting the demonstrated method to a special case.
- The option-pricing experiments are limited to European-style claims in the Black-Scholes framework.
- For multidimensional Black-Scholes problems, the PDE domain must be artificially truncated to a finite hypercube, introducing boundary approximation error.
- Boundary values on the truncated domain are approximated using time-discounted payoff functions, which the authors describe as only reasonably accurate approximations.
- The 2D option-pricing experiments do not have analytical ground truth; evaluation is done only relative to Euler solutions.
- Results are averaged over only 5 random seeds, which limits statistical robustness.
- As a preprint, the work has not undergone peer review.
- [inferred] No experiments are performed on actual quantum hardware; despite the quantum-inspired framing, the study is entirely classical.
- [inferred] No comparison is provided against stronger high-dimensional PDE baselines such as PINNs, deep BSDE methods, Fourier neural operators, or neural Galerkin methods.
- [inferred] The empirical validation is narrow, focusing mainly on diffusion equations and Black-Scholes pricing, so generalization to broader financial PDEs is unverified.
- [inferred] Scalability claims are based on asymptotic runtime arguments and small-to-moderate experiments rather than production-scale financial workloads.
- [inferred] Reproducibility may be limited because full implementation details, code, and hyperparameter sensitivity analyses are not provided in the text.
## Open questions
- How well does the generalized variational principle perform on nonlinear or more general time-dependent PDEs beyond the linear inhomogeneous cases tested?
- How does the method scale in accuracy and runtime for much higher-dimensional financial problems beyond those demonstrated?
- What is the best way to regularize or stabilize the ill-conditioned matrix M without degrading solution quality?
- How large must the Monte Carlo batch size be to maintain accuracy as dimensionality increases?
- Can the method handle non-trivial boundary conditions reliably in a mesh-free setting?
- How accurate is the approach for computing derivatives of the solution, such as Greeks needed for hedging, not just option prices?
- How sensitive are results to architectural choices, pre-training quality, truncation domain selection, and singular-value cutoff thresholds?
- Can the method be extended effectively to free-boundary problems such as American option pricing?
- How does the approach compare empirically with state-of-the-art classical high-dimensional PDE solvers on the same financial tasks?
- Does the polynomial-scaling advantage persist when targeting practically relevant accuracy levels for real financial applications?

**Future work:**
- Develop meshless variants based on continuous-variable neural-network quantum states, including normalizing flows.
- Address non-trivial boundary conditions in more general formulations.
- Extend the approach to free-boundary problems needed for pricing American contingent claims.
- Incorporate higher-order time-stepping schemes such as Runge-Kutta methods instead of first-order Euler updates.
- Pursue direct solution of the discrete-time dynamical system rather than relying on the infinitesimal-step ODE approximation.
- [inferred] Validate the method on broader classes of financial PDEs, including nonlinear and path-dependent pricing problems.
- [inferred] Benchmark against modern classical baselines for high-dimensional PDE solving in finance.
- [inferred] Study more principled variance-reduction and sampling strategies to reduce the need for very large batch sizes.
- [inferred] Evaluate the method on larger-scale and more realistic financial datasets and production-like settings.
- [inferred] Investigate extensions that relax the positivity assumption and support more general complex- or sign-changing state variables.
## Key ideas
- #idea:hybrid-approach — Uses a quantum-inspired variational Monte Carlo workflow with neural-network quantum states, classical sampling, and classical optimization to solve high-dimensional PDEs relevant to option pricing.
- #idea:near-term-feasibility — Demonstrates approximate pricing for 1D and 2D Black–Scholes-style European options with low-to-mid single-digit relative errors in many tested cases.
- #idea:quantum-advantage — Claims polynomial runtime scaling in the qubit-encoded mesh size versus exponential scaling for forward Euler finite differences, suggesting a possible advantage for high-dimensional derivatives pricing.
- #idea:near-term-feasibility — Shows empirical timing crossover against forward Euler around n=16 qubits in the reported classical experiments, though only for the chosen baseline and benchmark setup.
## Contradictions
- The paper suggests quantum-style or dimensionality advantages, but all experiments are entirely classical and quantum-inspired, not executed on quantum hardware, which contradicts any strong interpretation of demonstrated quantum superiority.
- The claimed scaling advantage is weakened by the fact that forward Euler is often more accurate and much faster on low-dimensional problems, while the proposed method needs larger Monte Carlo batch sizes as dimension grows, contradicting a simple superiority narrative.
- The paper argues it may overcome the curse of dimensionality, yet validation is limited to narrow benchmark families and moderate scales, with no comparison against stronger modern classical high-dimensional PDE solvers; this contradicts broad advantage claims.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic numerical inputs rather than observational datasets. For diffusion experiments, the initial condition is a discrete isotropic Gaussian u0(x) = product_i exp(-t) I_{x_i}(t), on a regular d-dimensional grid with total size 2^n, under either Dirichlet or periodic boundary conditions. Domains are hypercubes with equal side lengths and mesh size 2^(n/d) per axis. For option pricing, the Black-Scholes PDE is transformed to a multidimensional heat equation; experiments vary volatility sigma, strike K, interest rate r, expiry T, initial stock price S, and dimension d. For Black-Scholes truncation, the positive orthant is approximated by a hypercube [K exp(-3 sigma_i sqrt(T)), K exp(3 sigma_i sqrt(T))]^d, and the transformed heat-equation domain is approximately [-5, 5]^d.

### Process
1. Discretize the PDE spatial domain on a regular mesh with 2^n points and encode the discretized field as an n-qubit state vector. 2. Parameterize the solution as u_theta(x) = alpha psi_beta(x), where psi_beta is a unit-normalized autoregressive neural-network quantum state with conditional probabilities over bits. 3. Pretrain the parameters (alpha_0, beta_0) to match the initial condition by minimizing ||alpha_0 |psi_beta0> - |u0>||^2 using Adam for 50,000 iterations with batch size 128. The learning rate is warm-started over the first 10% of training and decayed by a factor of 10 at 3/7 and 5/7 of total iterations. 4. During evolution, assume an affine PDE operator F(t,x,u)=Lu+f(t,x). Estimate the overlap matrix M and vector V using VMC importance sampling from rho_beta(x)=|psi_beta(x)|^2. 5. Use Monte Carlo batches of sampled mesh points, storing unique samples and counts, to approximate expectations. 6. Compute per-sample gradients with BackPack and compute local energies using sparse operator row extraction with CPU parallelization. 7. Update parameters with an Euler step by solving M delta_theta = V delta_t. Because M is ill-conditioned, apply SVD regularization and discard singular values below 1e-12 before inversion. 8. For diffusion experiments, evolve to total time T=1 with step size 5e-5 and batch size 1024; compare against a forward Euler finite-difference baseline using the same step size. 9. Average reported numerical results over 5 random seeds, each trained for 20,000 steps. 10. For option pricing, transform Black-Scholes to a heat equation, run the same solver, then map the solution back to option prices and compare with analytical Black-Scholes values in 1D or Euler solutions in 2D.

### Output
Outputs include relative error between the proposed method and forward Euler over the space-time history for diffusion problems, runtime comparisons versus forward Euler, convergence visualizations, and ablation results on batch size. For 1D Black-Scholes option pricing, outputs are option prices compared against both forward Euler and the analytical Black-Scholes formula, with relative errors reported. For 2D option pricing tasks, outputs are relative errors with respect to Euler solutions for basket call, basket put, rainbow max call, and spread put options. Additional outputs include plots of option price sensitivity to volatility, interest rate, strike, initial stock price, and dimensionality.

### Parameters
- qubits: n total qubits, with experiments including n/d = 4 or 5 qubits per dimension and total n up to at least 16 in baseline comparisons
- grid_points: 2^n total mesh points
- pretraining_iterations: 50000
- training_steps_reported: 20000
- pretraining_batch_size: 128
- evolution_batch_size: 1024
- runtime_analysis_batch_size: 500
- optimizer: Adam
- adam_beta1: 0.9
- adam_beta2: 0.999
- adam_epsilon: 1e-08
- time_step: 5e-05
- total_evolution_time: 1.0
- diffusion_constant: 0.1
- svd_singularity_threshold: 1e-12
- num_seeds: 5
- boundary_conditions: ['Dirichlet', 'Periodic']

### Hardware
{'hardware_type': 'Classical HPC environment; no QPU used', 'compute_resources': 'Advanced Research Computing (ARC) at the University of Michigan', 'parallelization': 'CPU parallelization used for extraction of nonzero operator row entries', 'simulator': 'Not a quantum simulator; quantum-inspired neural/VMC implementation'}

### Reproducibility
Preprint status should be noted. The paper provides substantial methodological detail, including equations, update rules, hyperparameters, batch sizes, time step, training schedule, and benchmark setup. It mentions use of BackPack and describes operator discretization and boundary handling. However, no public code or repository is provided in the text, and some implementation specifics (e.g., exact network architecture depth/width and learning-rate values) are not fully specified, so replication appears partially feasible but not fully turnkey.
