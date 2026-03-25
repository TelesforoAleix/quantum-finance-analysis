---
aliases:
- Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications in
  Finance
- Quantum Algorithm Stochastic Optimal
authors:
- João F. Doriguello
- Alessandro Luongo
- Jinge Bao
- Patrick Rebentrost
- Miklos Santha
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.4230/LIPIcs.TQC.2022.2
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: 17th Conference on the Theory of Quantum Computation, Communication
  and Cryptography (TQC 2022)
methodology_tags:
- amplitude-estimation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2021_Rebentrost_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T15:56:30.597769'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:35.116901'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:50.043421'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:21.880051'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:57:52.317556'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:58:00.301354'
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
- method/amplitude-estimation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
title: Quantum Algorithm for Stochastic Optimal Stopping Problems with Applications
  in Finance
topic_tags:
- derivatives-pricing
year: 2022
zotero_key: ''
---

## Abstract summary
The paper develops a quantum version of the least squares Monte Carlo (LSM) algorithm to solve stochastic optimal stopping problems, with a focus on American option pricing. It combines quantum access to stochastic processes, quantum circuits for computing stopping times, and quantum Monte Carlo techniques to approximate continuation values and Snell envelopes. Under smoothness and structural assumptions, the authors show that their quantum LSM achieves an almost quadratic speedup in runtime over the classical LSM, and they discuss applications to Brownian and geometric Brownian motion models relevant in finance and insurance.
## Methodology
This conference paper is primarily theoretical, proposing and analyzing a quantum least-squares Monte Carlo (quantum LSM) algorithm for stochastic optimal stopping problems, with finance as a main application domain via American option pricing. The authors formalize the optimal stopping problem through the Snell envelope and dynamic programming over stopping times, then adapt the classical Longstaff-Schwartz least-squares Monte Carlo method into a quantum setting. Their framework assumes quantum sampling access to a Markov chain and quantum query access to payoff and basis functions, and combines quantum Monte Carlo mean estimation with quantum circuits that recursively compute approximate stopping times in superposition. The method approximates continuation values by projection onto finite-dimensional linear function classes, computes matrix and vector expectations using Montanaro-style quantum Monte Carlo/amplitude-estimation-based subroutines, and then classically inverts the resulting linear systems to obtain regression coefficients. The paper provides formal lemmas, theorems, error bounds, and runtime complexity analyses, showing a near-quadratic speedup in oracle/runtime complexity relative to classical LSM under smoothness and conditioning assumptions. It also includes theoretical case studies for Brownian motion and geometric Brownian motion, where specific polynomial bases such as Hermite polynomials or monomials simplify the analysis of the regression matrices.

**Algorithms used:** Least Squares Monte Carlo (LSM), Quantum LSM, Quantum Monte Carlo, Amplitude Estimation
## Findings
- [speculative] The paper proposes a quantum least-squares Monte Carlo (LSM) algorithm for stochastic optimal stopping problems that combines quantum access to the stochastic process, quantum circuits for stopping-time computation, and quantum Monte Carlo techniques.
- [speculative] Under mild assumptions, the proposed quantum LSM achieves a nearly quadratic runtime speedup over the classical LSM algorithm.
- [speculative] The algorithm applies to American option pricing and more broadly to finance applications such as insurance and risk management, as well as other optimal stopping problems.
- [supported] The paper derives an error bound showing that both classical and quantum LSM return an estimate of the optimal stopping value with additive error composed of a Monte Carlo estimation term plus a function-approximation error term.
- [speculative] In the general setting, the authors claim classical and quantum runtimes of approximately O~(Tm^6/epsilon^2) and O~(T^2 m^4/epsilon), respectively, up to polylogarithmic factors.
- [speculative] When continuation values are sufficiently smooth and polynomial approximation is used, the authors claim final runtimes of approximately O~((5T/epsilon)^(2+6d/n)) classically and O~((5T/epsilon)^(1+4d/n)) quantumly.
- [speculative] If continuation values have smoothness n = Theta(log(5T/epsilon)/log log(5T/epsilon)), the authors claim the quantum runtime approaches O~(5T/epsilon) versus classical O~((5T/epsilon)^2), i.e. near-quadratic improvement.
- [speculative] For Brownian motion with Hermite polynomial basis, the matrices At become identity matrices, simplifying the algorithm and improving the stated complexities to O~((5T/epsilon)^(2+4d/n)) classically and O~((5T/epsilon)^(1+7d/2n)) quantumly.
- [speculative] For geometric Brownian motion with suitable monomial bases, the matrices At become Vandermonde matrices with bounded minimum singular value, yielding weaker but still improved asymptotic complexities than the generic case.
- [supported] The quantum algorithm computes stopping times recursively in superposition and uses quantum Monte Carlo to estimate the matrix and vector quantities needed for regression, rather than sampling explicit Monte Carlo paths one by one.
- [supported] The authors note that the quantum algorithm requires redoing previous dynamic-programming steps before advancing to the next earlier time step, leading to O(T^2) time-step structure versus O(T) in classical LSM.
- [speculative] The paper argues that the exponential dependence on the number of exercise dates T in the final bounds is likely due to loose error analysis and may be improvable.

**Results summary:** This conference paper presents a theoretical quantum version of the least-squares Monte Carlo method for stochastic optimal stopping, with American option pricing as the main finance application. The authors construct quantum circuits to compute approximate stopping times in superposition and combine them with quantum Monte Carlo subroutines to estimate regression quantities used in backward induction. They provide formal error and complexity analyses rather than hardware experiments. Their main claim is a near-quadratic reduction in oracle/runtime dependence on the target precision relative to classical LSM under smoothness and approximation assumptions. In the generic setting, the quantum method improves the epsilon dependence from roughly 1/epsilon^2 to 1/epsilon, though it incurs an extra T factor from recomputing dynamic-programming steps. They further analyze Brownian motion and geometric Brownian motion cases relevant to finance, showing how basis choices can simplify the regression matrices and sharpen complexity bounds. All results are theoretical and algorithmic, not empirical demonstrations on real quantum hardware.

**Performance claims:**
- General informal complexity: classical O~(T m^6 / epsilon^2) vs quantum O~(T^2 m^4 / epsilon), up to polylog factors
- Informal error guarantee: Pr[|U_tilde0 - U0| >= 5T(epsilon + max_t min_a ||a·e_t(X_t) - E[Z_tau_{t+1}|X_t]||_{L2})|] <= delta
- With polynomial basis of degree q and continuation values in C^n, choosing q = ceil((5T/epsilon)^(1/n)) gives classical O~((5T/epsilon)^(2+6d/n)) and quantum O~((5T/epsilon)^(1+4d/n))
- For smoothness n = Theta(log(5T/epsilon)/log log(5T/epsilon)), claimed scaling approaches classical O~((5T/epsilon)^2) and quantum O~(5T/epsilon)
- Brownian motion case: classical O~((5T/epsilon)^(2+4d/n)) and quantum O~((5T/epsilon)^(1+7d/2n))
- Geometric Brownian motion case: classical eO((5T/epsilon)^(2/n)) (5T/epsilon)^(2+12d/n) and quantum eO((5T/epsilon)^(2/n)) (5T/epsilon)^(1+15d/2n)
- Quantum Monte Carlo subroutine runtime: O((sigma/epsilon) log(1/delta) log^(3/2)(sigma/epsilon) log log(sigma/epsilon)) times oracle costs
## Quantum advantage claim
**Classification:** theoretical

The paper claims a near-quadratic quantum speedup over classical LSM based on complexity analysis and proved bounds, but provides no empirical benchmark or real-hardware demonstration. The advantage depends on assumptions such as quantum access to the stochastic process, efficient function oracles, and sufficient smoothness of continuation values.
## Limitations
- The claimed nearly quadratic speedup holds only under mild assumptions, including smooth continuation values and favorable properties of the approximation architecture and Markov process.
- There is a gap between asymptotic query/runtime complexity and practical implementation because the algorithm assumes quantum sampling access to the stochastic process and quantum query access to payoff and basis functions.
- The arithmetic cost is abstracted away via a quantum arithmetic model that assumes constant-time arithmetic operations and negligible numerical errors, which may underestimate practical resource requirements.
- The model assumes access to constant-time controlled rotations, again hiding implementation overhead that could materially affect end-to-end performance.
- The construction of the state-preparation oracle for the Markov chain is assumed rather than fully costed; the paper notes that constructing such a unitary is an important question on its own.
- The analysis is restricted to finite sample spaces and finite state spaces for the quantum input model, which may limit direct applicability to continuous financial models without discretization.
- The final quantum procedure requires recomputing previous dynamic-programming steps, leading to O(T^2) time-step dependence rather than O(T) as in the classical recursion.
- The final complexities have an exponential dependence on T, the number of time steps; the authors explicitly note this as a downside.
- For geometric Brownian motion, the resulting complexity bounds are weaker than the usual idealized O~(1/epsilon) and O~(1/epsilon^2) forms because the minimum singular value bounds for the Vandermonde-like matrices are sensitive to the polynomial degree.
- The algorithm's performance depends implicitly on quantities such as the minimum singular value of the regression matrices At, which may be hard to characterize or control in general models.
- The practical regime often uses a constant number of basis functions m, whereas the theoretical error analysis requires m = poly(5T/epsilon), creating a mismatch between theory and practice.
- The paper provides no empirical implementation on quantum hardware or even classical simulation benchmarks demonstrating end-to-end performance for realistic financial instances.
- [inferred] No comparison is provided against state-of-the-art classical American option pricing methods beyond asymptotic comparison to standard LSM, so practical competitiveness remains unclear.
- [inferred] No treatment of hardware noise, decoherence, fault-tolerance overhead, or noise mitigation is included, limiting relevance to near-term quantum devices.
- [inferred] No resource estimates in terms of qubit counts, circuit depth, or gate counts are given for realistic finance-sized problems.
- [inferred] Reproducibility is limited because the work is theoretical and does not provide implementation artifacts, benchmark instances, or experimental protocols.
- [inferred] The conference-paper format likely constrains detail, and the paper itself points readers to the arXiv full version for fuller statements and proofs.
## Open questions
- How can the exponential dependence on the number of time steps T be improved, and is it mainly an artifact of loose error analysis?
- How can the assumed quantum sampling oracle for the underlying Markov chain be efficiently constructed in realistic financial models?
- Under what practical conditions do the hidden constants and oracle-construction costs preserve the claimed quantum advantage?
- Can the dependence on the number of basis functions m be reduced without introducing prohibitive precision overhead?
- Would HHL-like quantum linear-system methods for producing |alpha_t> states improve overall complexity in practice?
- Can a single time-independent set of approximation functions be used more broadly to improve complexity, as suggested for transformed American option pricing formulations?
- How robust are the complexity guarantees when the regression matrices At are ill-conditioned or when singular value bounds are weak?
- How and when can the algorithm find practical application given highly specialized classical algorithms and hardware for American option pricing?
- [inferred] What is the discretization error introduced when mapping continuous stochastic processes and payoffs into the finite-state quantum input model?
- [inferred] Does the asymptotic speedup survive once fault-tolerant overhead, state preparation, and arithmetic synthesis costs are fully included?

**Future work:**
- Perform further analysis of precision-parameter effects when using quantum subroutines for inner-product estimation to reduce polynomial dependence on m.
- Investigate replacing classical inversion of the regression systems with HHL-like algorithms that output quantum states |alpha_t>.
- Explore improved choices of approximation functions, including approaches that suppress explicit time dependence and use a single basis set across time steps.
- Extend the template to other quantum Monte Carlo subroutines such as those in Refs. [41, 22, 21].
- Apply the framework to related problems in dynamic programming, stochastic optimal stopping, optimal control, and problems similar in spirit to those solved by regression-based methods.
- Develop a more careful error analysis to improve the dependence on the number of time steps T.
- Study practical applicability in finance, especially identifying when the algorithm can outperform specialized classical methods in real-world settings.
- [inferred] Provide concrete resource estimates, including qubits, logical gates, and fault-tolerant overhead, for realistic American option pricing instances.
- [inferred] Validate the method empirically through simulations and, eventually, experiments on quantum hardware or fault-tolerant resource models.
- [inferred] Benchmark against advanced classical solvers and realistic market datasets to assess practical advantage rather than only asymptotic improvement.
## Key ideas
- #idea:quantum-advantage — Proposes a quantum least-squares Monte Carlo method for stochastic optimal stopping with American option pricing as the main finance application.
- #idea:quantum-advantage — Uses amplitude-estimation-style quantum Monte Carlo subroutines to improve the precision dependence of LSM from roughly 1/epsilon^2 classically to 1/epsilon quantumly under stated assumptions.
- #idea:quantum-advantage — Computes stopping times recursively in superposition and estimates regression quantities quantumly, yielding a theoretically near-quadratic runtime improvement over classical LSM.
- #idea:near-term-feasibility — The paper discusses finance-relevant Brownian and geometric Brownian motion settings, but practical deployment depends on strong oracle-access assumptions and is not demonstrated on hardware.
## Contradictions
- The paper claims near-quadratic quantum speedup for American option pricing, but also acknowledges unfavorable scaling from recomputing dynamic-programming steps and exponential dependence on the number of exercise dates T, which undermines practical scalability (#contradiction:scalability).
- Theoretical quantum advantage is conditioned on efficient quantum sampling/state-preparation oracles and abstract arithmetic assumptions; without costing these components, the superiority claim is weaker and aligns with broader caution in 2021_Rebentrost_QuantumAlgorithmsFinance about practical finance advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
