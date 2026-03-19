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
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:29:49.265287'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:29:53.827699'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:30:09.899605'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:30:30.148017'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:31:29.290954'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:32:34.367864'
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
This paper introduces a generalization of McLachlan’s variational principle to tackle time-dependent partial differential equations (PDEs) using quantum-inspired methods. The authors propose a variational quantum Monte Carlo approach with autoregressive neural-network quantum states to address the curse of dimensionality in high-dimensional PDEs. The method is empirically validated through applications to financial derivative pricing, specifically the multi-asset Black-Scholes PDE, demonstrating its potential for overcoming computational challenges in high-dimensional settings.
## Methodology
The paper presents a variational quantum Monte Carlo (VMC) approach combined with neural-network quantum states to solve high-dimensional partial differential equations (PDEs), specifically applied to financial derivative pricing using the multi-asset Black-Scholes PDE. The methodology generalizes McLachlan’s variational principle to arbitrary time-dependent PDEs, employing an autoregressive neural-network quantum state to represent the solution. The research design involves discretizing the spatial domain using a mesh, converting the PDE into a system of ordinary differential equations (ODEs) for variational parameters, and solving these ODEs using stochastic estimation techniques. Pre-training of the neural network is performed to match initial conditions, followed by time evolution using Monte Carlo sampling. The approach is validated through numerical experiments on diffusion equations and option pricing problems, comparing results with finite difference methods (forward Euler) and analytical solutions where applicable.

**Algorithms used:** Variational Quantum Monte Carlo (VMC), McLachlan’s variational principle
**Frameworks:** BackPack, Adam optimizer

**Experimental setup:** The experiments were conducted using a classical computational environment with CPU parallelization. The spatial domain was discretized into a mesh represented by qubits, with each computational basis state corresponding to a grid point. The neural-network quantum state was implemented using autoregressive assumptions for efficient sampling. Pre-training was performed using the Adam optimizer for 50,000 iterations with a batch size of 128. Time evolution was executed with a step size of δt = 5×10⁻⁵ and a Monte Carlo batch size of 1024. The study compared the proposed method against forward Euler time-stepping for diffusion equations and analytical solutions for Black-Scholes pricing in 1D.

**Dataset:** Synthetic datasets were generated for numerical experiments, including discrete isotropic Gaussian initializations for diffusion equations and multi-asset Black-Scholes model parameters (volatility σ, interest rate r, strike price K, expiry time T, and initial asset price S) for option pricing. The financial datasets involved European call and put options, basket options, rainbow max call options, and spread put options with predefined payoff functions.
## Findings
- [supported] The proposed variational quantum Monte Carlo (VMC) method with neural-network quantum states achieves polynomial scaling O(T B poly(n)) in solving high-dimensional partial differential equations (PDEs), compared to the exponential scaling O(T × 2^2n) of classical finite difference methods like forward Euler.
- [supported] The VMC method demonstrates a relative error of less than 10% for diffusion problems with up to 4 dimensions (n=16 qubits), with errors improving to ~3% with larger batch sizes (e.g., 10x increase).
- [supported] For the multi-asset Black-Scholes PDE, the VMC method achieves robust performance across varying parameters (volatility, interest rate, strike price, initial price) with relative errors ranging from 1.0% to 8.7% in 1D and up to 5.8% in 2D, compared to analytical or Euler method baselines.
- [supported] The VMC method outperforms the forward Euler method in runtime for problem sizes characterized by n=16 qubits, demonstrating practical feasibility for higher-dimensional problems where classical methods fail due to memory constraints.
- [supported] The method successfully handles boundary conditions (Dirichlet and periodic) in diffusion problems, as visualized in convergence snapshots over 20k iterations.
- [speculative] The authors suggest that the VMC approach could overcome the curse-of-dimensionality in high-dimensional PDEs, particularly for financial applications like pricing and hedging contingent claims in multi-asset markets.
- [speculative] The paper claims that the method could be extended to mesh-free variants and free-boundary problems (e.g., American options), though these extensions are not empirically validated.
- [speculative] The authors propose that higher-order time-stepping schemes (e.g., Runge-Kutta) could improve the accuracy of the ODE approximation, but this is not tested in the paper.

**Results summary:** The paper presents a variational quantum Monte Carlo (VMC) method using neural-network quantum states to solve high-dimensional time-dependent PDEs, with a focus on financial derivative pricing via the multi-asset Black-Scholes equation. The method demonstrates polynomial scaling in computational complexity, achieving runtime advantages over classical finite difference methods for problem sizes exceeding n=16 qubits. Empirical results show relative errors below 10% for diffusion problems and robust performance in option pricing across varying parameters, though accuracy degrades slightly with increasing dimensionality. The approach is validated through simulations, with no claims of quantum advantage on real hardware. The authors highlight potential extensions to mesh-free formulations and higher-order time-stepping schemes, but these remain untested.

**Performance claims:**
- Polynomial scaling O(T B poly(n)) for VMC vs. exponential scaling O(T × 2^2n) for forward Euler
- Relative error <10% for diffusion problems with up to 4 dimensions (n=16 qubits)
- Relative error improves from 15% to ~3% with 10x larger batch size
- Relative errors of 1.0% to 8.7% for 1D Black-Scholes option pricing compared to analytical solutions
- Relative errors of 3.2% to 5.8% for 2D Black-Scholes option pricing compared to Euler method
- VMC runtime faster than forward Euler for n=16 qubits (e.g., 230s vs. 306s for 4 dimensions)
- Pre-training with Adam optimizer for 50k iterations (batch size 128) to match initial conditions
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim quantum advantage. All results are derived from classical simulations of quantum-inspired algorithms (neural-network quantum states). The method is framed as a quantum-inspired classical approach to overcome the curse-of-dimensionality, with no empirical validation on real quantum hardware.
## Limitations
- Experiments limited to small-scale problems (up to 16 qubits) due to hardware constraints and memory limitations of classical simulators
- Mesh-based discretization restricts the approach to predefined grids, limiting flexibility for complex boundary conditions [inferred]
- Monte Carlo sampling introduces statistical noise, which may affect solution accuracy, especially for high-dimensional problems
- Batch size constraints (e.g., B=1024) limit the precision of stochastic estimations of matrix elements M and V
- Ill-conditioned matrix M requires regularization (e.g., singular value decomposition with thresholding), which may introduce approximation errors
- First-order Euler approximation for time evolution may lead to accumulation of errors over long time horizons [inferred]
- No direct comparison with state-of-the-art classical PDE solvers (e.g., finite element methods with adaptive meshing) to benchmark performance gains [inferred]
- Autoregressive sampling scales as O(T B n^3), which may become computationally expensive for very high dimensions despite polynomial scaling
- Boundary conditions are implemented via source functions, which may not capture all real-world financial scenarios (e.g., free-boundary problems for American options) [inferred]
- Lack of empirical validation on real quantum hardware; all experiments conducted via classical simulation of quantum-inspired methods
- Pre-training phase (50k iterations) adds significant computational overhead, which may limit practical applicability [inferred]
- No noise mitigation techniques applied, which would be necessary for deployment on noisy intermediate-scale quantum (NISQ) devices [inferred]
- Artificial truncation of the domain for Black-Scholes PDE (e.g., [Ke^{-3σ_i√T}, Ke^{3σ_i√T}]^d) may introduce boundary effects in high-dimensional settings [inferred]
## Open questions
- How does the algorithm perform for problems requiring more than 20 qubits, where classical simulators become infeasible?
- What is the impact of hardware noise (e.g., decoherence, gate errors) on solution quality when deployed on real quantum devices?
- Can the method be extended to handle non-linear PDEs beyond the affine case (F(t, x, u) = Lu(t, x) + f(t, x))?
- How does the choice of neural-network architecture (e.g., normalizing flows vs. autoregressive models) affect convergence and accuracy?
- What are the trade-offs between mesh-based and mesh-free formulations in terms of computational efficiency and solution quality?
- Can high-order time-stepping schemes (e.g., Runge-Kutta) improve accuracy without significantly increasing computational cost?
- How does the algorithm scale for free-boundary problems (e.g., American option pricing) where boundary conditions are dynamic?
- What is the minimal qubit count required to achieve quantum advantage for realistic financial PDEs?
- How does the method compare to classical deep learning approaches (e.g., physics-informed neural networks) in terms of accuracy and computational cost?

**Future work:**
- Extend the algorithm to mesh-free formulations using continuous-variable neural-network quantum states (e.g., normalizing flows)
- Implement high-order time-stepping schemes (e.g., Runge-Kutta) to improve accuracy of time evolution
- Test the algorithm on real quantum hardware (e.g., IBM Quantum or Rigetti devices) to evaluate noise resilience
- Apply the method to free-boundary problems (e.g., American option pricing) by incorporating dynamic boundary conditions
- Explore hybrid quantum-classical approaches to reduce the computational burden of pre-training and sampling
- Develop noise mitigation techniques tailored to the variational quantum Monte Carlo framework for NISQ devices
- Benchmark against state-of-the-art classical PDE solvers (e.g., finite element methods with adaptive meshing) for high-dimensional problems
- Investigate the use of alternative neural-network architectures (e.g., transformers) for autoregressive sampling to improve efficiency
- Extend the method to non-linear PDEs (e.g., Hamilton-Jacobi-Bellman equations in portfolio optimization)
- Optimize the algorithm for specific financial applications (e.g., multi-period portfolio optimization, exotic derivatives pricing)
## Key ideas
- #idea:quantum-advantage — Variational quantum Monte Carlo (VMC) method achieves polynomial scaling (O(TB poly(n))) for high-dimensional PDEs, outperforming classical finite difference methods with exponential scaling (O(T×2²ⁿ))
- #idea:near-term-feasibility — Demonstrates relative errors below 10% for up to 4-dimensional diffusion problems and multi-asset Black-Scholes PDEs, suggesting near-term applicability in financial derivatives pricing
- #idea:hybrid-approach — Combines neural-network quantum states with classical Monte Carlo sampling and variational optimization, enabling a hybrid quantum-classical framework for solving financial PDEs
- #limitation:simulation-only — All results are derived from classical simulations of quantum-inspired methods, with no empirical validation on real quantum hardware
- #limitation:data-encoding — Mesh-based discretization and autoregressive neural-network quantum states may limit flexibility for complex financial domains or non-positive state variables
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
