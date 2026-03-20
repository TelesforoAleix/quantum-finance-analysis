---
aliases:
- 'Quantum-inspired variational algorithms for partial differential equations: Application
  to financial derivative pricing'
- Quantum inspired variational algorithms
authors:
- Tianchen Zhao
- Chuhao Sun
- Asaf Cohen
- James Stokes
- Shravan Veerapaneni
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.2207.10838
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- variational
- quantum-ML
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:26:09.425526'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:26:12.162387'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:26:24.213742'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:28:12.175112'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:28:21.337868'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:28:25.172857'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- topic/asset-pricing
- method/variational
- method/quantum-ML
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: 'Quantum-inspired variational algorithms for partial differential equations:
  Application to financial derivative pricing'
topic_tags:
- derivatives-pricing
- asset-pricing
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces a generalization of McLachlan’s variational principle to address time-dependent partial differential equations (PDEs), with a focus on overcoming the curse of dimensionality. The authors propose a variational quantum Monte Carlo method using autoregressive neural-network quantum states to approximate solutions, particularly targeting high-dimensional PDEs in financial applications. The study demonstrates the approach through numerical experiments on the multi-asset Black-Scholes PDE for pricing European options, highlighting its potential for scalable and efficient computation in financial modeling.
## Methodology
The paper presents a generalization of McLachlan’s variational principle to arbitrary time-dependent partial differential equations (PDEs), with a focus on financial derivative pricing using the multi-asset Black-Scholes PDE. The methodology employs variational quantum Monte Carlo (VMC) combined with neural-network quantum states (NQS) to approximate solutions to high-dimensional PDEs, overcoming the curse-of-dimensionality. The approach involves discretizing the spatial domain into a mesh represented by qubits, using an autoregressive neural-network quantum state for efficient sampling, and applying stochastic estimation techniques to evolve the variational parameters over time. The algorithm is pre-trained to match initial conditions and then evolved using a first-order Euler scheme. Numerical experiments are conducted on diffusion equations and the Black-Scholes model for option pricing, comparing results against finite difference methods and analytical solutions where applicable.

**Algorithms used:** Variational Quantum Monte Carlo (VMC)
**Frameworks:** PyTorch (implied by BackPack for per-sample gradients)

**Experimental setup:** The experiments are conducted using a mesh-based discretization of the spatial domain, represented by qubits. The neural-network quantum state is implemented with autoregressive assumptions for efficient sampling and normalization. Pre-training is performed using the Adam optimizer, followed by time evolution using a first-order Euler scheme with Monte Carlo sampling. The computational environment involves CPU parallelization for matrix element extraction and stochastic gradient descent for parameter updates.

**Dataset:** Synthetic datasets for diffusion equations with Gaussian initializations and multi-asset Black-Scholes model for option pricing. The Black-Scholes experiments include European call and put options, basket options, rainbow max call options, and spread put options.
## Findings
- [supported] The proposed variational quantum Monte Carlo (VMC) method with neural-network quantum states achieves polynomial scaling O(TB poly(n)) in solving high-dimensional partial differential equations (PDEs), compared to the exponential scaling O(T×2^2n) of the finite difference-based forward Euler method for the same problems.
- [supported] The VMC method demonstrates robust performance in pricing European options under the multi-asset Black-Scholes model, with relative errors within a tolerable threshold (e.g., <10% for dimensions up to 4) when compared to analytical solutions (1D) or forward Euler methods (2D).
- [supported] Increasing the batch size in the VMC method improves accuracy, reducing relative error from 15% to ~3% in high-dimensional diffusion problems, as shown in ablation studies.
- [supported] The VMC method successfully handles boundary conditions (e.g., Dirichlet and periodic) in numerical experiments, as visualized in convergence snapshots for 2D diffusion problems.
- [supported] The method achieves faster runtime than the forward Euler method for problem sizes characterized by n=16 qubits, despite higher overhead in lower dimensions.
- [speculative] The authors suggest that the VMC approach could be extended to mesh-free formulations using continuous-variable neural-network quantum states, including normalizing flows, to address non-trivial boundary conditions.
- [speculative] The paper proposes that high-order time-stepping schemes (e.g., Runge-Kutta methods) or direct solutions of the discrete-time dynamical system could further improve the VMC method's performance.
- [speculative] The VMC method may overcome the curse-of-dimensionality in financial applications such as pricing and hedging contingent claims in multi-asset markets, though this claim is not empirically validated in the paper.

**Results summary:** The paper presents a variational quantum Monte Carlo (VMC) method using neural-network quantum states to solve high-dimensional partial differential equations (PDEs), with a focus on financial derivative pricing under the multi-asset Black-Scholes model. The method demonstrates polynomial scaling in computational complexity, outperforming classical finite difference methods (e.g., forward Euler) in high dimensions (n=16 qubits). Numerical experiments show the VMC method achieves relative errors within 10% for diffusion problems and option pricing tasks, with accuracy improving alongside batch size increases. The method successfully handles boundary conditions and provides a framework for extending to mesh-free formulations. While the results are promising, all empirical findings are derived from simulations, not real quantum hardware.

**Performance claims:**
- Polynomial scaling O(TB poly(n)) for VMC vs. exponential scaling O(T×2^2n) for forward Euler
- Relative error <10% for diffusion problems in up to 4 dimensions (Table 1)
- Relative error reduction from 15% to ~3% with 10x batch size increase (Section 4.4)
- Faster runtime than forward Euler for n=16 qubits (Table 2)
- Relative error of 1.178% for 1D Black-Scholes option pricing (Table 4)
- Relative errors of 3-6% for 2D option pricing tasks (Table 4)
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical advantage in overcoming the curse-of-dimensionality for high-dimensional PDEs, particularly in financial applications like multi-asset option pricing. However, all results are derived from classical simulations of quantum-inspired algorithms, not real quantum hardware. The advantage is argued based on polynomial scaling of the VMC method compared to exponential scaling of classical methods, but empirical quantum advantage is not demonstrated.
## Limitations
- Small qubit count constraints due to mesh-based discretization (n ≤ 16 qubits) limit scalability to higher-dimensional problems
- Experiments limited to synthetic or simplified financial models (e.g., multi-asset Black-Scholes PDE) rather than real-world market data
- Reliance on Monte Carlo sampling for stochastic estimation introduces approximation errors, particularly with small batch sizes
- Performance degrades as dimensionality increases, requiring larger batch sizes for accurate results [inferred]
- No comparison with state-of-the-art classical solvers (e.g., finite difference methods) for high-dimensional PDEs beyond n=16 qubits [inferred]
- Mesh-based formulation may not efficiently handle non-trivial boundary conditions in financial applications [inferred]
- First-order Euler approximation of the ODE (4) may introduce numerical instability or inaccuracies over long time evolutions
- Lack of noise mitigation techniques, which could affect performance on real quantum hardware [inferred]
- Artificial truncation of the domain for Black-Scholes PDE (e.g., [Ke^{-3σ_i√T}, Ke^{3σ_i√T}]^d) may introduce boundary effects
- No empirical validation on actual quantum hardware, limiting assessment of practical feasibility [inferred]
- Regularization techniques required to handle degeneracy in the matrix M_ij, but not thoroughly explored in the paper
## Open questions
- How does the algorithm perform for problems requiring more than 16 qubits, particularly in financial applications with >5 assets?
- What is the impact of hardware noise and decoherence on the variational quantum Monte Carlo (VMC) approach when implemented on real quantum devices?
- Can the method be extended to handle free-boundary problems (e.g., American options) without significant modifications?
- How does the performance of the neural-network quantum state approach compare to classical deep learning methods (e.g., PINNs) for high-dimensional PDEs?
- What are the trade-offs between mesh-based and mesh-free formulations in terms of accuracy and computational efficiency?
- How sensitive is the algorithm to the choice of hyperparameters (e.g., batch size, learning rate, regularization threshold)?
- Can higher-order time-stepping schemes (e.g., Runge-Kutta) improve the accuracy of the ODE evolution without sacrificing scalability?
- What are the implications of the autoregressive assumption for financial models with non-Gaussian or heavy-tailed distributions?

**Future work:**
- Extend the method to mesh-free formulations using continuous-variable neural-network quantum states (e.g., normalizing flows)
- Incorporate higher-order time-stepping schemes (e.g., Runge-Kutta) to improve accuracy of the ODE evolution
- Apply the algorithm to free-boundary problems, such as pricing American options
- Test the approach on real quantum hardware to assess practical performance and noise resilience
- Compare the method with classical deep learning solvers (e.g., PINNs, deep BSDE methods) for high-dimensional PDEs
- Explore adaptive batch sizing or importance sampling techniques to improve Monte Carlo estimation efficiency
- Investigate the use of hybrid quantum-classical approaches to mitigate hardware limitations (e.g., qubit count, noise)
- Extend the framework to non-linear PDEs beyond the affine case (e.g., Hamilton-Jacobi-Bellman equations in portfolio optimization)
- Develop techniques to handle more complex boundary conditions in financial PDEs without domain truncation
- Validate the algorithm on real-world financial datasets to assess its practical applicability
## Key ideas
- #idea:quantum-advantage — Variational quantum Monte Carlo (VMC) method achieves polynomial scaling (O(TB poly(n))) for high-dimensional PDEs, outperforming classical finite difference methods with exponential scaling (O(T×2²ⁿ)) in financial derivatives pricing
- #idea:near-term-feasibility — Demonstrates relative errors below 10% for up to 4-dimensional diffusion problems and multi-asset Black-Scholes PDEs, suggesting near-term applicability in financial modeling
- #idea:hybrid-approach — Combines neural-network quantum states with classical Monte Carlo sampling and variational optimization, enabling a hybrid quantum-classical framework for solving financial PDEs
- #limitation:simulation-only — All results are derived from classical simulations of quantum-inspired methods, with no empirical validation on real quantum hardware
- #limitation:data-encoding — Mesh-based discretization and autoregressive neural-network quantum states may limit flexibility for complex financial domains or non-positive state variables
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'diffusion_equation': {'source': 'Synthetic', 'size': 'Discretized grid with 2^n points (n qubits per dimension)', 'features': 'Spatial coordinates on a hypercube domain', 'preprocessing': 'Initial conditions set as discrete isotropic Gaussian distributions; boundary conditions implemented via source functions', 'time_period': 'Evolution time T = 1 with step size δt = 5×10^-5'}, 'black_scholes': {'source': 'Synthetic', 'size': 'Discretized grid with 2^n points (n qubits per dimension)', 'features': 'Asset prices, strike price K, volatility σ, interest rate r, expiry time T', 'preprocessing': 'Domain truncated to [Ke^-3σ√T, Ke^3σ√T]^d; boundary conditions approximated by time-discounted payoff functions', 'time_period': 'Varies by experiment (e.g., T = 1)'}}

### Process
1. Discretize the spatial domain into a mesh represented by qubits. 2. Pre-train the neural-network quantum state using Adam optimizer to match initial conditions (50k iterations, batch size 128). 3. Evolve the state using McLachlan’s variational principle with stochastic estimation of matrix elements M and V (batch size B = 1024, step size δt = 5×10^-5). 4. Update parameters using a stabilized singular value decomposition of M. 5. Repeat for 20k iterations, comparing against finite difference methods or analytical solutions.

### Output
{'metrics': 'Relative error between variational state and baseline (finite difference or analytical solution), running time, convergence visualization, and option prices for Black-Scholes experiments.', 'comparison_baselines': 'Forward Euler method for diffusion equations; analytical Black-Scholes formula for 1D options; finite difference methods for higher dimensions.', 'output_format': 'Relative error values, snapshots of state evolution, option prices as functions of strike price K, volatility σ, interest rate r, and initial asset price S.'}

### Parameters
- qubits: n (e.g., n = 4, 5, 6 per dimension)
- circuit_depth: Not explicitly stated (determined by neural network architecture)
- shots: Batch size B (e.g., 1024 for Monte Carlo sampling)
- optimizer: Adam (pre-training), Euler scheme (time evolution)
- learning_rate: Warm-started, decayed by factor of 10 at 3/7 and 5/7 of training iterations
- convergence_threshold: Not explicitly stated (implicit in step size δt = 5×10^-5)
- batch_size: 128 (pre-training), 1024 (evolution)
- evolution_time: T = 1
- step_size: δt = 5×10^-5
- regularization: Singular value decomposition threshold ϵ = 10^-12 for stabilizing matrix inversion

### Hardware
{'simulator': 'CPU-based (no specific simulator mentioned; parallelization used for matrix element extraction)', 'QPU': 'Not used (theoretical quantum-inspired algorithm)', 'transpilation_settings': 'Not applicable'}

### Reproducibility
Code and data details are not explicitly provided in the paper. The methodology is described in sufficient detail for replication, including pre-training, evolution steps, and parameter choices. However, no GitHub repository or supplementary materials are mentioned.
