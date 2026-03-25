---
aliases:
- Variational quantum simulations of stochastic differential equations
- Variational quantum simulations stochastic
authors:
- Kenji Kubo
- Yuya O. Nakagawa
- Suguru Endo
- Shota Nagayama
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1103/PhysRevA.103.052425
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- variational
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-25T15:54:19.440181'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:23.894041'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:38.739794'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:21.663642'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:57.091174'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:12.851748'
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
- topic/market-simulation
- method/variational
- method/amplitude-estimation
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Variational quantum simulations of stochastic differential equations
topic_tags:
- derivatives-pricing
- market-simulation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper proposes a variational quantum simulation (VQS) algorithm to solve stochastic differential equations (SDEs) by first approximating them with a trinomial tree and then encoding the resulting probability distributions directly into the amplitudes of a quantum state. The authors construct a nonunitary time-evolution operator for these distributions, show how to decompose it into implementable unitaries for use with VQS, and develop a compatible method to compute expectation values of functions of the SDE solution without prior knowledge of the solution. They validate the approach numerically on geometric Brownian motion and Ornstein–Uhlenbeck processes, and discuss resource requirements and potential quantum speedups for expectation-value estimation compared to classical Monte Carlo and prior quantum methods based on amplitude estimation.
## Methodology
The paper develops a theoretical quantum-classical hybrid framework for solving stochastic differential equations (SDEs) using variational quantum simulation (VQS). The core methodology first approximates a continuous SDE by a trinomial tree model obtained through time and state-space discretization, with transition probabilities chosen to match the first and second conditional moments of the original process under an Euler-Maruyama-style discretization. The resulting discrete probability dynamics are then reformulated as a linear differential equation over a probability vector, which is embedded directly into the amplitudes of an unnormalized quantum state rather than via square-root amplitude encoding. The authors then apply McLachlan’s variational principle to derive evolution equations for the variational parameters of an ansatz state, thereby mapping the nonunitary dynamics of the embedded probability distribution to a parameterized quantum circuit. A major formal contribution is the explicit decomposition of the induced linear operator L(t) into sums of efficiently implementable unitary components using shift-like operators, cyclic increment/decrement constructions, controlled-Z structures, and diagonal polynomial operators, under the assumption that drift and diffusion terms can be expanded as low-order polynomials. The paper also introduces a theoretical scheme for computing expectation values of functions of the SDE solution by approximating payoff/functions with piecewise polynomials, constructing corresponding nonunitary operators as sums of unitaries, and evaluating them via Hadamard-test or phase-estimation-style subroutines. Theoretical analysis includes complexity arguments, error analysis for the piecewise polynomial approximation, and an extension to multivariate SDEs. Numerical illustrations on geometric Brownian motion and Ornstein-Uhlenbeck processes are presented as validation, but the paper’s main methodological contribution is the formal modeling and operator-construction framework rather than an empirical benchmark study.

**Algorithms used:** Variational Quantum Simulation, McLachlan variational principle, Hadamard test, Quantum Phase Estimation, Quantum Amplitude Estimation, Quantum Linear Solver Algorithm, Euler-Maruyama method, Runge-Kutta method
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes a quantum-classical hybrid algorithm for solving stochastic differential equations (SDEs) by approximating the SDE with a trinomial tree and then simulating the resulting linear differential equation via variational quantum simulation (VQS).
- [speculative] A central proposition is that directly embedding the probability distribution itself in quantum-state amplitudes, rather than embedding square roots of probabilities, makes the SDE dynamics linear and enables simpler VQS circuits for general SDEs.
- [speculative] The authors claim their method requires only the SDE specification and does not require prior knowledge of the probability distribution or expectation-value PDE, making it more generally applicable than prior quantum approaches based on Feynman-Kac reformulations or amplitude-estimation-based distribution loading.
- [speculative] The paper derives that the discretized trinomial-tree dynamics converge to a linear ODE dP/dt = L(t)P, and this is mapped to nonunitary quantum-state evolution d|psi>/dt = L(t)|psi>, which can be handled by McLachlan-based VQS.
- [speculative] Under polynomial expansions of drift and diffusion terms, the generator L(t) can be decomposed into a polynomial number of easily implementable unitaries, with decomposition cost scaling as O(n^m) terms for polynomial order m and gate depth built from O(n^2) few-qubit gates.
- [speculative] The expectation value of functions of the SDE solution can be computed by approximating the payoff/function with piecewise polynomials and constructing an operator Sf so that the target expectation is recovered from <psi|Sf|0><0|Sf^†|psi>.
- [speculative] For piecewise polynomial degree L over d intervals, the expectation-value operator decomposes into O(d^2 n^(2L+2)) unitary terms, and each unitary can be evaluated either by Hadamard tests or QPE-style circuits.
- [speculative] The paper claims that when QPE is used for expectation evaluation, the measurement complexity can scale as O(log(1/(gamma*epsilon))) with circuit depth O(1/(gamma*epsilon)), which may yield a quantum advantage over classical Monte Carlo under favorable gamma and approximation conditions.
- [speculative] The authors explicitly state that any quantum speedup claim is not mathematically rigorous because variational-algorithm errors, especially ansatz error, are difficult to bound accurately.
- [supported] Numerical simulations on geometric Brownian motion and Ornstein-Uhlenbeck processes show that the proposed VQS approach reproduces the time evolution of probability distributions, means, and variances reasonably well in noiseless classical simulation.
- [supported] The numerical study indicates that ansatz expressivity matters: a deeper ansatz (k=3) produced results closer to the Runge-Kutta solution of the discretized linear ODE than a shallower ansatz (k=2), because the shallower ansatz had fewer parameters than lattice degrees of freedom.
- [speculative] The framework extends in principle to multivariate SDEs by constructing multidimensional tree transitions and corresponding operator decompositions, though the expectation-value construction can scale exponentially with dimension unless the target function depends on only a small number of variables.
- [speculative] The method is argued to be relevant for financial applications such as derivative pricing, including European call options under Black-Scholes-type dynamics, because such payoffs can be represented with low-degree piecewise polynomials.

**Results summary:** This peer-reviewed theoretical paper develops a variational quantum simulation framework for stochastic differential equations by first discretizing the SDE with a trinomial tree and then mapping the resulting probability-distribution dynamics to a linear nonunitary quantum-state evolution. The main theoretical contribution is the direct embedding of probabilities into amplitudes, which preserves linearity and allows decomposition of the evolution operator into polynomially many implementable unitaries when drift and diffusion admit low-order polynomial expansions. The paper also derives a piecewise-polynomial method for computing expectation values, including financial payoffs such as European call options. Complexity discussions suggest polynomial resource requirements for the VQS stage and possible quantum advantage for expectation estimation when using QPE under favorable conditions, but the authors caution that rigorous speedup guarantees are not available because variational errors are hard to bound. Numerical validation is limited to noiseless classical simulation of the quantum algorithm on geometric Brownian motion and Ornstein-Uhlenbeck processes, where the method qualitatively matches analytical and Runge-Kutta benchmarks and improves with a more expressive ansatz.

**Performance claims:**
- VQS-stage decomposition of L(t) uses O(n^m) unitary terms for polynomial order m, with each built from O(n^2) few-qubit gates
- For typical practical SDEs, the authors state m_max is usually small (approximately 1 or 2), implying O(Poly(n)) cost for the SDE-simulation part
- Expectation-value operator decomposition requires O(d^2 n^(2L+2)) unitary terms for piecewise polynomial degree L over d intervals
- Each expectation-evaluation circuit is stated to contain O(n^4) quantum gates
- Using Hadamard tests, total measurements for expectation estimation scale as O(d^2 n^(2L+2) / (gamma * epsilon^2))
- Using QPE-style estimation, total measurements scale as O(d^2 n^(2L+2) log(1/(gamma*epsilon))) with circuit depth O(1/(gamma*epsilon)) in the unitary U
- To suppress piecewise-polynomial approximation error below epsilon, the number of unitary terms can scale as O(x_max^2 * epsilon^(-2/(L+1)) * n^(2L+2))
- Numerical validation used n = 4 qubits and ansatz depths k = 2 and k = 3 on noiseless classical simulation
- Geometric Brownian motion test parameters: r = 0.1, sigma = 0.2, Delta x = 1, t in [0,4]
- Ornstein-Uhlenbeck test parameters: r = 7, sigma = 0.5, eta = 0.01, Delta x = 1, t in [0,4]
## Quantum advantage claim
**Classification:** theoretical

The paper argues theoretically that expectation-value evaluation may achieve quantum advantage, particularly with QPE-style estimation versus classical Monte Carlo, but this is not empirically demonstrated on hardware and the authors explicitly note that rigorous speedup is not guaranteed due to unbounded variational/ansatz errors.
## Limitations
- The method relies on discretizing the SDE via a trinomial tree approximation, introducing model/discretization error relative to the continuous process.
- The approach assumes the event space can be truncated to a finite interval and discretized, which may be problematic for processes with broad or unbounded support.
- The operator L(t) must be expressible through low-order polynomial expansions of drift and diffusion terms to obtain a feasible decomposition into implementable unitaries.
- Expectation-value evaluation requires approximating the payoff/function by piecewise polynomials, introducing additional approximation error.
- The authors state that it is difficult to accurately estimate the error caused by the variational ansatz, making the overall error hard to quantify.
- The paper explicitly notes that quantum speedup is not mathematically rigorous because, as with other variational quantum algorithms, precision and speedups are not guaranteed in general.
- Numerical validation is performed only through classical noiseless simulation, not on actual quantum hardware.
- The numerical experiments are limited to small systems (4 qubits) and simple prototype processes (geometric Brownian motion and Ornstein-Uhlenbeck), leaving practical scalability untested.
- The quality of results depends on the expressivity of the chosen ansatz; the paper shows that insufficient ansatz depth/parameter count leads to noticeable error.
- The expectation-value subroutine using the Hadamard test has O(1/epsilon^2) measurement scaling, matching classical Monte Carlo rather than guaranteeing an advantage.
- The alternative QPE-based expectation estimation requires deeper circuits of order O(1/(gamma epsilon)), which may be challenging for NISQ hardware.
- In the multivariate extension, the number of terms can grow exponentially with the dimension when the target function depends on many variables.
- [inferred] The paper does not benchmark against state-of-the-art classical SDE solvers in runtime or accuracy, so the practical competitiveness of the method remains unclear.
- [inferred] No analysis is given of hardware noise, sampling noise, optimizer instability, or error-mitigation strategies, despite positioning the method for NISQ devices.
- [inferred] The assumption Nx = 2^n - 1 is a convenience for encoding but may impose awkward discretization choices in practical applications.
- [inferred] Boundary handling for the truncated lattice/event space is not deeply analyzed, which could affect accuracy near domain edges.
- [inferred] Although finance is a motivating application, no realistic financial datasets, calibration tasks, or production-scale derivative pricing cases are studied.
## Open questions
- Under what conditions can the proposed VQS-based SDE solver deliver a genuine quantum advantage over classical numerical methods?
- How small or large is the factor gamma in realistic applications, and when does it permit an advantage in expectation-value estimation?
- How does the method perform on real noisy quantum hardware, especially for the QPE-based expectation-evaluation routine?
- How scalable is the approach with increasing qubit count, finer discretization, longer time horizons, and more complex ansatz circuits?
- What is the best trade-off between polynomial order L and number of intervals d in the piecewise approximation for practical financial payoffs?
- How severe are truncation and boundary effects when simulating SDEs with effectively unbounded state spaces?
- Which classes of SDEs beyond the demonstrated examples admit efficient polynomial decompositions of L(t)?
- How robust is the method to ansatz choice, barren plateaus, and optimization difficulties in larger instances?
- For multivariate financial models, when does the exponential growth in expectation-value construction become prohibitive, and are there structure-exploiting workarounds?
- [inferred] How does the method compare empirically with classical Monte Carlo, finite-difference, tree, and PDE solvers on realistic financial workloads?
- [inferred] Can the direct probability embedding be combined with error mitigation or alternative measurement strategies to reduce sampling overhead on NISQ devices?

**Future work:**
- Apply the method to other stochastic processes beyond geometric Brownian motion and Ornstein-Uhlenbeck processes.
- Use the framework for solving the Fokker-Planck equation, which also governs time evolution of probability distributions of SDE solutions.
- Extend and exploit the multivariable generalization described in Appendix B for higher-dimensional stochastic processes.
- Investigate expectation-value evaluation strategies, including QPE-based methods, to realize possible quantum advantage.
- Study improved piecewise polynomial approximations and parameter choices for reducing expectation-value approximation error.
- Explore applications in broader scientific domains beyond finance where stochastic processes are important.
- [inferred] Validate the algorithm on actual quantum hardware to assess noise robustness and practical feasibility.
- [inferred] Develop tighter end-to-end error bounds that combine discretization, ansatz, measurement, and polynomial-approximation errors.
- [inferred] Design more expressive or problem-tailored ansatz circuits to reduce approximation error while keeping circuits shallow.
- [inferred] Benchmark against strong classical baselines on realistic financial tasks such as derivative pricing and risk estimation.
- [inferred] Investigate methods to mitigate the dimensionality blow-up in multivariate settings, especially for finance applications with many correlated factors.
## Key ideas
- #idea:hybrid-approach — Proposes a quantum-classical variational quantum simulation framework for SDEs by discretizing them with a trinomial tree and evolving the resulting probability dynamics with McLachlan-based parameter updates.
- #idea:near-term-feasibility — Encodes the probability distribution directly in amplitudes rather than square roots, preserving linear dynamics and enabling a variational treatment with relatively shallow circuits in principle.
- #idea:near-term-feasibility — Derives decompositions of the nonunitary SDE generator into polynomially many implementable unitaries when drift and diffusion admit low-order polynomial expansions.
- #idea:quantum-advantage — Claims possible advantage for expectation estimation of SDE functionals, including option payoffs, via phase-estimation-style routines relative to classical Monte Carlo under favorable conditions.
- #idea:quantum-advantage — Suggests derivative-pricing relevance because European-style payoffs can be approximated by piecewise polynomials and evaluated from the prepared terminal distribution.
- #idea:hybrid-approach — Uses classical optimization and numerical discretization together with quantum subroutines for state evolution and expectation estimation.
- #idea:near-term-feasibility — Validates only on 4-qubit noiseless classical simulations for geometric Brownian motion and Ornstein-Uhlenbeck processes, showing ansatz expressivity strongly affects accuracy.
## Contradictions
- The paper argues for polynomial scaling and potential advantage, but its own resource analysis shows expectation-value construction can grow exponentially with dimension for multivariate SDEs, contradicting broad scalability claims for realistic financial models.
- The work presents the approach as NISQ-friendly through shallow VQS circuits, yet the full expectation-estimation pipeline can require many unitary terms and deep QPE-style circuits, undermining practical near-term feasibility.
- Although the paper suggests quantum advantage over classical Monte Carlo, it explicitly states that end-to-end speedup is not rigorous because ansatz errors are hard to bound and the key advantage factor gamma is application-dependent and unclear.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
