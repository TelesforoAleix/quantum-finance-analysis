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
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T22:41:59.628277'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:42:02.284460'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:42:06.686471'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:42:14.978482'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:42:27.231524'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:42:50.616249'
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
This paper introduces a generalization of McLachlan’s variational principle to solve time-dependent partial differential equations (PDEs) using variational quantum Monte Carlo (VMC) methods with neural-network quantum states. The authors focus on addressing the curse of dimensionality in high-dimensional PDEs, particularly in financial applications such as multi-asset option pricing under the Black-Scholes model. The work bridges quantum-inspired algorithms and classical numerical methods, demonstrating practical relevance for problems requiring fine-grained state variable information.
## Methodology
The paper presents a generalization of McLachlan’s variational principle to solve time-dependent partial differential equations (PDEs), with a focus on financial derivative pricing using the multi-asset Black-Scholes PDE. The methodology combines variational quantum Monte Carlo (VMC) with neural-network quantum states (NQS) to address the curse-of-dimensionality. The approach involves discretizing the spatial domain into a mesh and representing the PDE solution as a rescaled neural-network quantum state. The variational parameters are evolved using a system of ordinary differential equations derived from McLachlan’s principle, with stochastic estimation of matrix elements via Monte Carlo sampling. Pre-training is performed to match the initial condition of the PDE, followed by time evolution using an Euler scheme. The method is benchmarked against finite difference methods for diffusion equations and applied to option pricing in the Black-Scholes framework.

**Algorithms used:** Variational Quantum Monte Carlo (VMC), Neural-Network Quantum States (NQS)
**Frameworks:** BackPack (for per-sample gradient computation), PyTorch (implied for neural network training)

**Experimental setup:** The experiments were conducted using a mesh-based discretization of the spatial domain, represented as an n-qubit system. The neural-network quantum state was implemented with autoregressive assumptions to enable efficient sampling. Pre-training was performed using the Adam optimizer with a batch size of 128, and time evolution was carried out with a step size of δt = 5×10⁻⁵ and a batch size of B = 1024 for Monte Carlo estimation. The hardware environment was not explicitly stated, but the experiments were run on classical simulators due to the focus on quantum-inspired variational algorithms. CPU parallelization was used for matrix element extraction.

**Dataset:** The numerical experiments used synthetic data for diffusion equations with Gaussian initializations and the multi-asset Black-Scholes PDE for option pricing. The initial condition for the diffusion experiments was a discrete isotropic Gaussian, and the Black-Scholes model was applied to European option pricing contingent on multiple correlated underlying assets.
## Findings
- [supported] The proposed variational quantum Monte Carlo (VMC) method with autoregressive neural-network quantum states achieves polynomial scaling (O(TB poly(n))) for solving high-dimensional PDEs, compared to the exponential scaling (O(T×2²ⁿ)) of classical finite difference methods like forward Euler.
- [supported] The VMC method demonstrates relative errors below 10% for diffusion problems with up to 4 dimensions (n=4 qubits per dimension) when compared to forward Euler baselines, with errors improving further (e.g., from 15% to 3%) with larger batch sizes.
- [supported] The method successfully enforces boundary conditions (e.g., Dirichlet and periodic) in numerical experiments, as visualized in convergence snapshots for 2D diffusion problems.
- [speculative] The authors claim the VMC approach could overcome the curse-of-dimensionality in financial applications like multi-asset option pricing, but this is not empirically validated in the paper.
- [speculative] The paper suggests potential extensions to free-boundary problems (e.g., American options) and mesh-free generalizations, but these are not demonstrated.
- [supported] The VMC method shows faster runtime than forward Euler for problem sizes with n=16 qubits, despite higher overhead in lower dimensions.
- [speculative] The authors argue that the VMC framework could achieve quantum advantage for PDEs requiring fine-grained state variable information (e.g., gradients), but this is not empirically tested on real quantum hardware.

**Results summary:** The paper introduces a generalization of McLachlan’s variational principle for solving time-dependent PDEs using variational quantum Monte Carlo (VMC) with autoregressive neural-network quantum states. The method is applied to the multi-asset Black-Scholes PDE for financial derivative pricing. Numerical experiments demonstrate polynomial scaling in runtime (O(TB poly(n))) compared to the exponential scaling of classical finite difference methods, with relative errors below 10% for up to 4-dimensional diffusion problems. The approach successfully enforces boundary conditions and shows faster runtime than classical methods for larger problem sizes (n=16 qubits). However, claims of overcoming the curse-of-dimensionality and potential quantum advantage remain speculative, as the results are based on classical simulations and not real quantum hardware.

**Performance claims:**
- Polynomial scaling: O(TB poly(n)) runtime for VMC vs. O(T×2²ⁿ) for forward Euler
- Relative error <10% for 4-dimensional diffusion problems (n=4 qubits per dimension)
- Error improvement from 15% to 3% with 10x larger batch size
- Faster runtime than forward Euler for n=16 qubits
## Quantum advantage claim
**Classification:** speculative

The paper claims potential quantum advantage for high-dimensional PDEs requiring fine-grained state information, but all results are from classical simulations. No empirical validation on real quantum hardware is provided, and the advantage is argued theoretically based on polynomial scaling and efficient sampling.
## Limitations
- The paper is a preprint and has not undergone peer review, which may affect the validity and reliability of the results [inferred]
- The method is only tested on synthetic data (e.g., Gaussian initializations for diffusion equations) and not on real-world financial data [inferred]
- Experiments are limited to low-dimensional problems (up to 4 dimensions) due to computational constraints, which may not reflect high-dimensional financial applications [inferred]
- The relative error increases with problem dimensionality, reaching up to 15% for 4 dimensions, indicating potential scalability issues [inferred]
- The method relies on Monte Carlo sampling for stochastic estimation, which introduces approximation errors and may require large batch sizes for accurate results
- The mesh-based discretization of the spatial domain may not be optimal for all financial PDEs, particularly those with irregular boundaries or high-dimensional spaces
- The autoregressive neural-network quantum state implementation assumes strictly positive state variables, which may not hold for all financial applications [inferred]
- The evolution equations are derived under the assumption of an affine linear operator, limiting the generality of the approach [inferred]
- The matrix M in the evolution equations is often ill-conditioned, requiring regularization techniques that may introduce additional errors [inferred]
- The comparison with classical methods (e.g., forward Euler) is limited to small problem sizes (n ≤ 16 qubits) due to memory constraints, making it difficult to assess scalability
- The method does not address noise or decoherence effects, which are critical for real quantum hardware implementations [inferred]
- The paper does not provide a direct comparison with state-of-the-art classical solvers for financial PDEs, such as deep learning-based methods or traditional finite element methods [inferred]
## Open questions
- How does the method perform on real-world financial data, such as multi-asset option pricing with real market correlations?
- What is the impact of noise and decoherence on the algorithm's performance when implemented on near-term quantum hardware?
- Can the method be extended to handle non-affine or nonlinear PDEs commonly encountered in financial modeling?
- How does the algorithm scale to higher dimensions (e.g., >10 assets) relevant for practical financial applications?
- What are the trade-offs between batch size, computational cost, and solution accuracy in high-dimensional settings?
- How does the method compare with other quantum-inspired or classical approaches (e.g., PINNs, deep BSDE methods) in terms of accuracy and computational efficiency?
- Can the mesh-free generalization mentioned in the paper address the limitations of the current mesh-based approach for irregular domains?
- What are the implications of the ill-conditioned matrix M for the stability and convergence of the algorithm in long-time simulations?
- How can boundary conditions be more effectively enforced in the neural-network quantum state framework, particularly for complex financial PDEs?

**Future work:**
- Extend the method to mesh-free implementations to handle irregular domains and boundary conditions more effectively
- Apply the algorithm to real-world financial datasets, such as multi-asset option pricing with empirical market data
- Investigate the performance of the method on near-term quantum hardware, including noise mitigation techniques
- Explore the generalization of the approach to nonlinear and non-affine PDEs relevant to financial modeling
- Develop adaptive batch size strategies to balance computational cost and solution accuracy in high-dimensional settings
- Compare the method with state-of-the-art classical solvers (e.g., deep learning-based methods) to assess its practical advantages
- Extend the framework to free-boundary problems, such as American option pricing, which are critical in financial applications
- Improve the conditioning of the matrix M in the evolution equations to enhance numerical stability
- Investigate the use of alternative neural-network architectures (e.g., transformers) to improve the expressivity and efficiency of the quantum state representation
## Key ideas
- #idea:quantum-advantage — Proposes a variational quantum Monte Carlo (VMC) method with polynomial scaling (O(TB poly(n))) for high-dimensional PDEs, contrasting with exponential scaling (O(T×2²ⁿ)) of classical finite difference methods like forward Euler
- #idea:near-term-feasibility — Demonstrates relative errors below 10% for up to 4-dimensional diffusion problems, suggesting potential for near-term applicability in financial PDEs like multi-asset option pricing
- #idea:hybrid-approach — Combines neural-network quantum states (NQS) with classical Monte Carlo sampling and variational optimization, enabling a hybrid quantum-classical framework for PDE solving
- #limitation:simulation-only — All results are derived from classical simulations, with no empirical validation on real quantum hardware, limiting claims of quantum advantage
- #limitation:data-encoding — Relies on mesh-based discretization and autoregressive neural-network quantum states, which may not generalize to irregular financial domains or non-positive state variables
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
