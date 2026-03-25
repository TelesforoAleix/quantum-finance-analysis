---
aliases:
- Variational quantum algorithm based on Lagrange polynomial encoding to solve differential
  equations
- Variational quantum algorithm based
authors:
- Josephine Hunout
- Sylvain Laizet
- Lorenzo Iannucci
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1103/PhysRevA.111.062404
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-25T16:09:48.800287'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:09:53.178341'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:10:08.701698'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:10:55.432289'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:11:23.260261'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:11:31.941643'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Variational quantum algorithm based on Lagrange polynomial encoding to solve
  differential equations
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
The paper proposes a new variational quantum algorithm that uses Lagrange polynomial encoding combined with derivative quantum circuits based on the Hadamard test to approximate solutions of differential equations. Two circuit architectures—one qubit-efficient and one gate-efficient—are introduced and compared against adapted versions of existing VQAs by Kyriienko et al. and Sato et al. on a damped mass-spring system and a 1D Poisson equation with several boundary conditions. The study focuses on solution quality and gate complexity, showing that the new architectures can achieve comparable or better accuracy with significantly reduced gate counts in noiseless simulations.
## Methodology
The paper develops a peer-reviewed theoretical framework for solving differential equations with a novel hybrid variational quantum algorithm based on Lagrange polynomial encoding and Hadamard-test-based differentiation. The authors formalize two circuit architectures—an extended and a simplified Hadamard-Lagrange design—and compare them analytically and through noise-free simulations against two existing VQA formulations: a Kyriienko-inspired polynomial-fitting approach and the Sato et al. variational Poisson solver. The theoretical model defines a variational quantum circuit as the composition of a quantum feature map and a trainable ansatz, with the approximated solution read out through a cost operator based mainly on local Z-magnetization. The loss function is formally constructed as the mean-squared residual of the differential equation, optionally augmented with weighted terms for initial/boundary conditions and regularization points. A key methodological contribution is the derivation showing that the proposed feature map and cost operator implement a Lagrange interpolating polynomial, with interpolation coefficients controlled by variational parameters. Derivatives with respect to the encoded variable are obtained using derivative quantum circuits and Hadamard test differentiation, while gradients with respect to trainable parameters are obtained via the parameter-shift rule. The paper also provides a formal gate-complexity accounting framework, deriving expressions for the number of circuits and basic gates required per iteration for the proposed method and comparator methods. The analysis is conducted under explicit assumptions of noise-free simulation, projective Z-basis measurement, polynomial encodability of the target function, and availability of suitable interpolation/training points. Main propositions supported in the paper are that the Hadamard-Lagrange encoding reproduces Lagrange basis polynomials, that local measurements help mitigate barren plateau effects relative to global measurements, and that the proposed architectures can achieve similar or better solution quality with lower gate complexity than prior VQAs for the studied differential equations.

**Algorithms used:** Variational Quantum Algorithm (VQA), Hadamard test differentiation, parameter-shift rule, Adam optimizer, BFGS optimizer, hardware-efficient ansatz
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes two architectures of a variational quantum algorithm using Lagrange polynomial encoding and Hadamard-test-based differentiation to solve differential equations.
- [speculative] The authors claim the proposed Hadamard-Lagrange VQA has lower gate complexity than prior VQAs for differential equations while maintaining similar or better solution quality under noise-free simulation.
- [supported] In noise-free simulations, the two proposed architectures (extended and simplified) produce the same theoretical output, differing mainly in qubit count versus gate count trade-offs.
- [speculative] The simplified architecture saves qubits at the cost of additional gates, while the extended architecture uses more qubits but fewer gates; the preferable choice depends on hardware constraints and error sources.
- [speculative] The Lagrange encoding with the chosen cost operator yields a Lagrange interpolating polynomial, with the fitted polynomial degree tied to circuit size.
- [speculative] Using local measurements in the proposed architecture is argued to help delay or mitigate barren plateau effects relative to global measurements.
- [supported] For the damped mass-spring system, the Hadamard-Lagrange algorithm produced smoother solutions and better adherence to boundary/initial conditions than the Kyriienko-inspired baseline in noise-free simulation.
- [supported] For the damped mass-spring system, the best Hadamard-Lagrange result on the first training-set type achieved total DE loss 1.51e-3 and BC loss 1.18e-3, compared with the best Kyriienko-inspired results of DE loss 2.50e-3 or 2.77e-3 and BC loss 0.447 or 0.485.
- [supported] For the damped mass-spring system, the Hadamard-Lagrange optimization was much less sensitive to random initialization than the Kyriienko-inspired baseline.
- [supported] For the damped mass-spring system, the first optimization stage of the Hadamard-Lagrange method showed mean total losses of 1.24e-2 and 2.76e-2 with coefficients of variation 1.0% and 1.5% across five trials for the two training-set types.
- [supported] For the damped mass-spring system, the Kyriienko-inspired baseline showed substantial variability across random initializations, with coefficient of variation in total loss of 20% and 50% for the two best-performing circuit configurations.
- [supported] For the Poisson equation, the Hadamard-Lagrange algorithm matched or exceeded the accuracy of the Sato et al. baseline while using a much smaller variational parameter set and lower estimated gate complexity in noise-free simulation.
- [supported] For the Poisson equation, the Hadamard-Lagrange solution reached the same averaged DE loss as the Sato et al. solution after about 300 iterations in the reported Neumann-boundary-condition comparison.
- [supported] For the Poisson equation, the mean absolute error of the Sato et al. solution was reported as 4x, 3x, and 6x larger than the proposed method for periodic, Dirichlet, and Neumann boundary conditions, respectively.
- [supported] For the Poisson equation, although the Sato et al. algorithm required about half as many iterations on average, its circuit structure was estimated to require about 200x more gates per iteration than the Hadamard-Lagrange algorithm.
- [speculative] The authors argue that meshless polynomial-fitting VQAs such as the proposed method may be promising for nonlinear differential equations because they do not require linearization in the same way as discretized linear-solver approaches.
- [speculative] The authors note that scaling to higher-dimensional PDEs, nonlinear DEs, and real-hardware execution remains future work, so current claims are limited to simulated 1D examples.

**Results summary:** This peer-reviewed theoretical paper introduces a new variational quantum algorithm based on Lagrange polynomial encoding and Hadamard-test differentiation for solving differential equations, and compares it in noise-free simulation against a Kyriienko-inspired polynomial-fitting VQA and the Sato et al. Poisson solver. The main theoretical proposition is that the chosen encoding and cost operator make the circuit output a Lagrange interpolating polynomial, while the Hadamard-test differentiation reduces derivative-evaluation overhead relative to parameter-shift-based approaches. In simulated tests on a damped mass-spring ODE and a Poisson equation with periodic, Dirichlet, and Neumann boundary conditions, the proposed method achieved similar or better solution quality with lower estimated gate complexity. For the damped mass-spring problem, it gave lower DE loss and dramatically lower boundary-condition loss than the Kyriienko-inspired baseline, while also being less sensitive to random initialization. For the Poisson problem, it outperformed the Sato et al. baseline in mean absolute error and was estimated to use roughly 200 times fewer gates per iteration, despite requiring more iterations. The paper does not demonstrate quantum advantage over classical solvers; claims are limited to theoretical and simulation-based comparisons among quantum algorithms.

**Performance claims:**
- For the damped mass-spring system, best Hadamard-Lagrange total DE loss: 1.51e-3 (first training-set type) and 2.87e-3 (second training-set type)
- For the damped mass-spring system, best Hadamard-Lagrange BC loss: 1.18e-3 and 1.07e-4
- For the damped mass-spring system, best Kyriienko-inspired total DE loss: 2.50e-3 (N5L2I2) and 2.77e-3 (N4L3I1)
- For the damped mass-spring system, best Kyriienko-inspired BC loss: 0.447 and 0.485
- For the damped mass-spring system, Hadamard-Lagrange first-stage mean total loss across five trials: 1.24e-2 and 2.76e-2
- For the damped mass-spring system, Hadamard-Lagrange first-stage coefficient of variation in total loss: 1.0% and 1.5%
- For the damped mass-spring system, Hadamard-Lagrange first-stage average iterations to convergence: 670 and 620, with 11% coefficient of variation
- For the damped mass-spring system, Kyriienko-inspired coefficient of variation in total loss: 20% for N5L2I2 and 50% for N4L3I1
- For the damped mass-spring system, Kyriienko-inspired coefficient of variation in iterations: 57% for N5L2I2 and 40% for N4L3I1
- For the Poisson equation, the proposed method reached the same averaged DE loss as the Sato et al. solution after about 300 iterations in the Neumann-case comparison
- For the Poisson equation, Sato et al. mean absolute error was 4x larger (periodic), 3x larger (Dirichlet), and 6x larger (Neumann) than the proposed method
- For the Poisson equation, Sato et al. required about half as many iterations on average, but about 200x more gates per iteration than the proposed method
- Sato et al. baseline used 45 variational parameters in the reported Poisson setup, versus 3 variational parameters for the proposed Hadamard-Lagrange setup
## Quantum advantage claim
**Classification:** theoretical

The paper makes no demonstrated quantum advantage claim over classical financial or numerical methods. Its main advantage claims are theoretical and simulation-based: reduced gate complexity relative to prior VQAs for differential equations under specific circuit constructions and noise-free conditions.
## Limitations
- All VQAs are simulated in a noise-free environment, so the results do not validate performance on real quantum hardware.
- The study evaluates the proposed method only on two 1D benchmark differential equations: a damped mass-spring system and the Poisson equation.
- The meshless polynomial-fitting approaches studied require continuity in the problem definition; this is a stated limitation relative to methods like Sato et al.'s discretized approach.
- The Kyriienko-inspired and Hadamard-Lagrange approaches use polynomial fitting whose degree scales with circuit size, which the authors note may limit implementation on NISQ devices.
- The proposed method has only theoretical/noise-free validation; the practical impact of gate errors, decoherence, crosstalk, and qubit errors is not empirically established.
- Choice between the simplified and extended circuit structures depends on hardware characteristics, but this trade-off is not experimentally resolved.
- For discontinuous source terms, the Hadamard-Lagrange method must be applied on subintervals rather than directly over the full domain, indicating limited direct handling of discontinuities.
- The Kyriienko-inspired comparison baseline required additional tuning choices and modifications from the original method, which may affect fairness of comparison.
- The Kyriienko-inspired algorithm showed high sensitivity to random initialization of variational parameters, leading to variability in loss and iterations.
- The authors note that the Kyriienko-inspired algorithm may lack flexibility to satisfy all types of initial or boundary conditions for higher-order DEs.
- The study focuses on gate-count complexity and solution quality, but does not establish end-to-end runtime or practical quantum advantage.
- [inferred] No comparison is provided against strong state-of-the-art classical differential equation solvers, so the practical competitiveness versus classical methods remains unclear.
- [inferred] Claims of reduced gate complexity are theoretical and may not translate directly to lower wall-clock cost once sampling overhead, measurement shots, and hardware calibration constraints are included.
- [inferred] The work does not analyze scalability in qubit count, optimization difficulty, or training stability for larger problem sizes beyond small proof-of-concept instances.
- [inferred] Missing empirical study of barren plateaus for the proposed architecture; mitigation is argued conceptually via local measurements, but not systematically demonstrated.
- [inferred] The method relies on specific encoding choices such as arccos((x-x_i)/2) for numerical stability, suggesting sensitivity to encoding design that may not generalize across problems.
- [inferred] Financial modeling is mentioned only as motivation; no finance-specific differential equations or datasets are tested, limiting direct evidence for financial-services applicability.
## Open questions
- How well does the proposed VQA scale to higher-dimensional differential equations in 2D and 3D?
- Can the Hadamard-Lagrange approach effectively solve a broader class of DEs beyond the two benchmark problems studied?
- How well can the proposed VQA handle genuinely nonlinear differential equations?
- Which of the two circuit structures, simplified or extended, performs better on actual quantum hardware under realistic noise and crosstalk?
- At what circuit sizes does the polynomial-degree growth become a practical bottleneck for NISQ implementation?
- How robust is the proposed algorithm's trainability as system size and problem complexity increase?
- What is the true practical trade-off between qubit count and gate count for the two architectures on different hardware platforms?
- Can the method maintain its apparent advantages once shot noise, readout error, and noise-mitigation overhead are included?
- [inferred] Does the reduced gate complexity lead to any real computational advantage over advanced classical solvers for financially relevant DEs?
- [inferred] How sensitive are results to the choice of interpolation/training points, optimizer settings, and initialization for more complex problems?
- [inferred] Can the approach be adapted to finance-relevant PDEs such as Black-Scholes-type, HJB, or multi-factor pricing equations?

**Future work:**
- Assess the performance of the proposed VQA on higher-dimensional problems in 2D and 3D.
- Test the method on a wider range of differential equations, including advection-diffusion, Burgers', and possibly Euler equations.
- Investigate how the proposed VQA can be extended to nonlinear differential equations.
- Evaluate both the simplified and extended circuit structures on real quantum computers.
- Study intermediate circuit structures whose encoding uses between 1 and n qubits; the authors explicitly leave this for future work.
- [inferred] Benchmark the proposed method against state-of-the-art classical numerical solvers to clarify whether any practical advantage exists.
- [inferred] Perform hardware-aware studies including noise, decoherence, crosstalk, and error-mitigation techniques.
- [inferred] Analyze scalability and trainability systematically for larger qubit counts and more complex domains.
- [inferred] Apply the method to finance-specific differential equations to validate relevance for financial services.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid variational quantum algorithm using Lagrange polynomial encoding and Hadamard-test-based differentiation to solve differential equations via parametrized circuits and classical optimization.
- #idea:near-term-feasibility — Frames the method as more NISQ-suitable than fault-tolerant linear-solver approaches by using local measurements, shallow structured ansätze, and lower gate complexity.
- #idea:quantum-advantage — Claims an intra-quantum advantage over prior VQAs for differential equations, with similar or better accuracy and substantially lower estimated gate complexity in noiseless simulations.
- #idea:near-term-feasibility — Introduces two circuit architectures with a qubit-count versus gate-count trade-off, intended to adapt to hardware constraints.
- #idea:hybrid-approach — Uses parameter-shift gradients and classical optimizers such as Adam and BFGS, reinforcing a practical quantum-classical workflow.
## Contradictions
- The paper suggests the approach could extend to higher-dimensional and finance-relevant PDEs, but simultaneously acknowledges unresolved scalability due to polynomial-degree growth, qubit/gate trade-offs, and lack of evidence beyond small 1D noiseless simulations.
- Although the paper reports lower gate complexity than comparator quantum methods, it does not compare against strong classical differential-equation solvers, which undercuts any broader implication of computational superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
