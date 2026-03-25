---
aliases:
- High-dimensional counterdiabatic quantum computing
- High dimensional counterdiabatic quantum
authors:
- Diego Tancara
- Francisco Albarrán-Arriagada
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
journal_or_venue: arXiv
methodology_tags:
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:05:30.891639'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:05:35.377874'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:06:19.089822'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:06:53.079258'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:23.675310'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:07:31.241607'
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
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/classical-vs-quantum
- contradiction/scalability
title: High-dimensional counterdiabatic quantum computing
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper extends digitized counterdiabatic quantum computing from qubits to high-dimensional systems, focusing on qutrit-based implementations for quadratic optimization problems. It develops explicit qutrit Hamiltonian encodings and approximate counterdiabatic drivings, and benchmarks performance on multiway number partitioning, max 3-cut, and portfolio optimization over 1000 random instances each. The authors show that qutrit encodings generally yield higher success probabilities and lower energy errors than qubit encodings—sometimes by up to two orders of magnitude—and argue that current trapped-ion platforms can feasibly implement these high-dimensional counterdiabatic algorithms in a fully digital form.
## Methodology
This preprint presents a primarily theoretical and numerical study of high-dimensional counterdiabatic quantum computing using qutrits, with empirical evaluation on optimization benchmarks. The authors formulate a digitized counterdiabatic adiabatic evolution with Hamiltonian H(t) = (1-λ)HI + λHF + λdot Aλ, where the initial Hamiltonian prepares a uniform qutrit superposition and the final Hamiltonian encodes discrete optimization problems in trinary form. They derive qutrit Hamiltonian encodings for three quadratic optimization problems: multiway number partitioning, max 3-cut, and portfolio optimization. The counterdiabatic term is approximated using the nested-commutator expansion truncated at first order (l=1), yielding an adiabatic gauge potential approximation Aλ ≈ i(Γ1/Γ2)[HI, HF]. Performance is then assessed numerically by simulating the time evolution for qutrit and qubit encodings and comparing final-state quality using an energy error metric R and a success-probability enhancement ratio P3/2(T). The study includes illustrative case studies and aggregate tests over 1000 random instances for each problem class at multiple total evolution times. For portfolio optimization, the paper uses both a real financial example based on yfinance data for six technology stocks from 2020-2023 and random synthetic portfolio instances. The work also discusses a possible fully digital implementation on qutrit-capable platforms, especially trapped ions, but does not report execution on actual quantum hardware.

**Algorithms used:** Digitized Counterdiabatic Quantum Computing, Adiabatic Quantum Computing, Nested-commutator approximation for adiabatic gauge potential
**Frameworks:** yfinance

**Experimental setup:** Numerical simulations of digitized counterdiabatic adiabatic evolution comparing qutrit and qubit encodings. The study evaluates three total evolution-time regimes (short, medium, long), explicitly including T = 0.1ω0^-1, T = ω0^-1, and T = 10ω0^-1 for the 1000-instance experiments. No actual QPU runs are reported; hardware discussion is limited to feasibility of future fully digital qutrit implementations, especially on trapped-ion systems.

**Dataset:** Three types of inputs are used: (1) 1000 random instances of multiway number partitioning with six random numbers in [0,1]; (2) 1000 random max 3-cut instances on six-node graphs with random connectivity; and (3) 1000 random portfolio optimization instances with random expected returns and covariance matrices. In addition, a real financial example uses yfinance data for six assets—Apple, Microsoft, Google, Amazon, Tesla, and Netflix—over 2020-2023, from which expected returns and covariance matrix are computed.
## Experiment details
### Input
Inputs include: multiway number partitioning instances with N=6 numbers, either a fixed illustrative set (e.g., {0.8, 1.1, 1.1, 0.7, 1, 0.3}) or 1000 random sets sampled from [0,1]; max 3-cut instances on six-node graphs, including a wheel graph W6 for illustration and 1000 random six-node graphs for aggregate evaluation; portfolio optimization instances using either real market data for 6 assets (AAPL, MSFT, GOOGL, AMZN, TSLA, NFLX) from 2020-2023 via yfinance or 1000 synthetic random instances with random expected returns and covariance matrices. For portfolio optimization, the cost function uses expected returns, covariance matrix, budget constraint, and trinary discretization with g trinary digits per asset; examples include g=1 with n=6 and g=2 with n=3.

### Process
1. Define the initial qutrit Hamiltonian HI = -ω0 Σj Xj, whose ground state is the uniform qutrit superposition. 2. Map each optimization problem into a qutrit final Hamiltonian HF using trinary variables and qutrit operators Z, G=Z^2, and for portfolio optimization Qu=Zu+I. 3. Construct the adiabatic Hamiltonian Had = (1-λ)HI + λHF with schedule λ(t) = sin^2[(π/2) sin^2(πt/2T)]. 4. Approximate the adiabatic gauge potential using the first-order nested-commutator truncation Aλ ≈ i(Γ1/Γ2)[HI, HF], where Γk are squared Frobenius norms of nested commutators. 5. Numerically simulate the time evolution under H(t) = Had + λdot Aλ for both qutrit and qubit encodings. 6. Evaluate final-state performance using the normalized energy error R = (E(T)-Eg)/ΔE and success probability Pj(T), then compute enhancement ratio P3/2(T)=P3(T)/P2(T). 7. Repeat over 1000 random instances per problem for T = 0.1ω0^-1, ω0^-1, and 10ω0^-1, and summarize mean enhancement and percentage of instances with P3/2(T) > 1. 8. Inspect spectral evolution of the adiabatic Hamiltonian in representative cases to interpret performance differences via level crossings and energy-gap structure.

### Output
Reported outputs include the final energy error metric R, success probability Pj(T), and qutrit-over-qubit enhancement ratio P3/2(T). Results are shown as curves versus total evolution time T for representative instances and as distributions/scatter summaries over 1000 random instances. Aggregate statistics include mean enhancement values and percentages of instances where qutrits outperform qubits. The main baseline comparison is qutrit encoding versus qubit encoding of the same optimization problems; no classical optimization baseline is emphasized for the numerical performance study.

### Parameters
- system_types_compared: ['qubit', 'qutrit']
- random_instances_per_problem: 1000
- evolution_times_tested: ['0.1ω0^-1', 'ω0^-1', '10ω0^-1']
- agp_truncation_order: 1
- schedule_function: λ(t) = sin^2[(π/2) sin^2(πt/2T)]
- portfolio_examples: [{'g': 1, 'n_assets': 6}, {'g': 2, 'n_assets': 3}]
- graph_size_max_3_cut: 6
- number_partitioning_size: 6

### Hardware
{'execution_hardware': 'Numerical simulation only; no real quantum hardware used for reported results', 'proposed_physical_platforms': ['trapped ions', 'superconducting qutrit platforms'], 'implementation_mode_discussed': ['fully digital', 'digital-analog (future possibility)']}

### Reproducibility
Preprint. Data and code are not openly linked in the text but are stated to be available from the corresponding author upon reasonable request. The paper provides detailed Hamiltonian formulations, schedule, metrics, and benchmark descriptions, so the methodology is partially reproducible, though exact simulation settings (e.g., numerical integrator/discretization details) are not fully specified.
## Findings
- [supported] The paper extends digitized counterdiabatic quantum computing from qubits to qutrits for quadratic optimization problems by deriving qutrit Hamiltonian encodings and approximate counterdiabatic drivings based on the first-order nested-commutator adiabatic gauge potential.
- [supported] Across 1000 random instances each of multiway number partitioning, max 3-cut, and portfolio optimization, qutrit encodings generally achieved higher success probability than qubit encodings under the studied simulated dynamics.
- [supported] For max 3-cut on 6-node random graphs, qutrits outperformed qubits in all 1000 tested instances for the reported evolution times.
- [supported] The largest reported improvement was for max 3-cut, where some instances achieved success-probability enhancement P3/2 greater than 90 relative to qubits.
- [supported] Mean success-probability enhancement for max 3-cut was reported as 35.34 at T = 0.1ω0^-1, 30.41 at T = 1ω0^-1, and 6.99 at T = 10ω0^-1.
- [supported] For multiway number partitioning, mean success-probability enhancement was modest but above 1 on average: 1.31 at T = 0.1ω0^-1, 1.23 at T = 1ω0^-1, and 1.07 at T = 10ω0^-1.
- [supported] For multiway number partitioning, the fraction of instances with qutrit improvement over qubits was 84.6% at T = 0.1ω0^-1, 79.8% at T = 1ω0^-1, and 74.8% at T = 10ω0^-1.
- [supported] For portfolio optimization, qutrits improved over qubits in all tested instances at T = 0.1ω0^-1 and T = 1ω0^-1, with mean enhancement 3.56 and 1.54 respectively; at T = 10ω0^-1, more than 80% of instances improved with mean enhancement 1.12.
- [supported] In illustrative portfolio optimization examples using yfinance data for six assets from 2020-2023, qutrit performance was visibly better than qubits over the simulated evolution, although one tested setting still remained far from the adiabatic regime.
- [supported] The authors attribute qutrit performance gains to more efficient problem codings that reduce redundant states and lower the density of near-ground-state level crossings during evolution compared with qubit encodings.
- [speculative] The authors argue that, without prior knowledge, it is generally preferable to use qutrits and possibly higher-dimensional systems rather than qubits for these classes of optimization problems.
- [speculative] The paper claims experimental feasibility of fully digital high-dimensional counterdiabatic algorithms on current qutrit-capable platforms, especially trapped ions, based on known gate constructions rather than a hardware demonstration in this work.
- [speculative] The work suggests that extending counterdiabatic quantum computing beyond qutrits to higher-dimensional qudits could provide further benefits for efficient optimization encodings.

**Results summary:** This preprint proposes a qutrit-based version of digitized counterdiabatic quantum computing for optimization, with explicit Hamiltonian encodings for multiway number partitioning, max 3-cut, and portfolio optimization, and an approximate counterdiabatic term derived from the first nested commutator. The main evidence is numerical simulation rather than hardware execution. Over 1000 random instances per problem, qutrit encodings generally outperformed qubit encodings in success probability, with the strongest gains for max 3-cut and more modest but still positive average gains for number partitioning and portfolio optimization. The authors also analyze energy spectra and argue that qutrit encodings reduce redundant low-lying levels and level crossings, which helps explain the observed improvements. They further discuss how a fully digital implementation could be realized on current qutrit-capable platforms, but this feasibility claim is not experimentally validated in the paper.

**Performance claims:**
- Up to 90x improvement in solution quality/success probability for qutrits versus qubits in some instances
- 1000 random instances tested for each of three problems: multiway number partitioning, max 3-cut, and portfolio optimization
- Max 3-cut mean success-probability enhancement P3/2: 35.34 at T = 0.1ω0^-1, 30.41 at T = 1ω0^-1, 6.99 at T = 10ω0^-1
- Max 3-cut: qutrits outperformed qubits in 100% of the 1000 random instances tested
- Some max 3-cut instances achieved P3/2 > 90
- Multiway number partitioning mean P3/2: 1.31 at T = 0.1ω0^-1, 1.23 at T = 1ω0^-1, 1.07 at T = 10ω0^-1
- Multiway number partitioning percentage of instances with P3/2 > 1: 84.6% at T = 0.1ω0^-1, 79.8% at T = 1ω0^-1, 74.8% at T = 10ω0^-1
- Portfolio optimization mean P3/2: 3.56 at T = 0.1ω0^-1, 1.54 at T = 1ω0^-1, 1.12 at T = 10ω0^-1
- Portfolio optimization: 100% of instances improved at T = 0.1ω0^-1 and T = 1ω0^-1; more than 80% improved at T = 10ω0^-1
- Illustrative portfolio example used six assets (Apple, Microsoft, Google, Amazon, Tesla, Netflix) with historical data from 2020-2023
## Quantum advantage claim
**Classification:** speculative

Although the paper reports simulated performance improvements of qutrit encodings over qubit encodings within the same counterdiabatic framework, it does not demonstrate quantum advantage over classical algorithms or on real hardware. As a preprint with numerical evidence only, any broader advantage claim remains speculative.
## Limitations
- The work provides numerical evidence only; no experimental implementation on actual qutrit hardware is reported.
- The counterdiabatic term uses only a first-order approximation to the adiabatic gauge potential (l = 1), rather than the exact or higher-order form.
- Performance evaluation is limited to three problem classes: multiway number partitioning, max 3-cut, and portfolio optimization.
- Benchmark instances are small, e.g., six-number partitioning sets, six-node graphs, and portfolio examples with six assets or three assets with g = 2.
- For some portfolio optimization settings, the method remains far from the adiabatic regime even at T = 100ω0^-1, as indicated by R > 10.
- The qutrit advantage is not universal: for some instances of multiway number partitioning, qutrits perform worse than qubits (e.g., P3/2 < 1).
- The claimed experimental feasibility is restricted to at least a fully digital implementation; more efficient implementations are suggested but not demonstrated.
- The authors note that in the fully digital implementation, worst-case error scaling is similar to qubit-based quantum computing because it scales with the number of two-body controlled phase gates, so encoding alone does not improve error scaling.
- Code and data are not openly released in the paper and are only available upon reasonable request, limiting reproducibility.
- [inferred] As a preprint, the work has not undergone peer review.
- [inferred] There is no direct comparison against strong state-of-the-art classical optimization baselines, so practical quantum advantage is not established.
- [inferred] The study appears to rely on idealized simulations and does not quantify the impact of realistic hardware noise, decoherence, gate infidelity, or measurement error on the reported gains.
- [inferred] Scalability to larger financial instances is unproven, especially for realistic portfolio optimization problems with many assets, constraints, and higher precision requirements.
- [inferred] The portfolio optimization experiments use a narrow historical dataset (2020-2023, selected tech stocks) and limited synthetic random instances, which may not reflect broader market conditions.
- [inferred] The conclusion that high-dimensional systems are preferable in general is based mainly on qutrit results and may not generalize to higher-dimensional qudits without further evidence.
- [inferred] Resource estimates such as gate counts, circuit depth, runtime, and error accumulation for large-scale implementations are not quantified in detail.
## Open questions
- How does the qutrit-based counterdiabatic approach scale with problem size beyond the small instances studied here?
- Under what structural conditions of an optimization problem does qutrit encoding outperform qubit encoding, and when can it fail?
- How strongly is the observed enhancement determined by the density of level crossings during the evolution?
- Would higher-dimensional qudits beyond qutrits provide further improvements over both qubits and qutrits?
- How robust are the reported gains under realistic noise models on trapped-ion, superconducting, or other qutrit-capable platforms?
- Can higher-order approximations to the adiabatic gauge potential materially improve solution quality or reduce runtime?
- What is the trade-off between encoding efficiency and hardware/control complexity in practical qutrit implementations?
- How does the method compare with leading classical solvers and heuristics on realistic financial optimization tasks?
- Can the approach handle larger and more realistic portfolio optimization formulations, including additional constraints, transaction costs, and multi-period settings?
- Is the observed advantage preserved when using native hardware gates and finite-precision digitalization rather than idealized simulations?

**Future work:**
- Experimentally implement the proposed high-dimensional counterdiabatic algorithms on universal qutrit platforms such as trapped ions.
- Explore extensions from qutrits to higher-dimensional qudit systems for optimization.
- Develop more efficient implementations using digital-analog paradigms rather than fully digital decompositions.
- Investigate single-layer or impulse-regime versions of high-dimensional counterdiabatic algorithms for near-term devices.
- Apply the codification framework to a broader class of optimization problems beyond the three studied here.
- Study the relationship between spectral structure, especially level crossings, and algorithmic performance more systematically.
- Assess performance on larger instances and more realistic industrial/financial datasets.
- Incorporate more accurate or higher-order counterdiabatic drivings beyond the l = 1 nested-commutator approximation.
- Benchmark against classical optimization methods and alternative quantum algorithms to clarify any practical advantage.
- Evaluate hardware-aware implementations with explicit noise, gate-count, and fidelity analyses.
## Key ideas
- #idea:quantum-advantage — Qutrit-based digitized counterdiabatic evolution outperforms qubit encodings on small simulated portfolio-optimization instances, with mean success-probability enhancement above 1 across tested evolution times.
- #idea:quantum-advantage — The paper attributes qutrit gains to more efficient trinary encodings that reduce redundant states and near-ground-state level crossings during adiabatic evolution.
- #idea:near-term-feasibility — The authors argue that fully digital implementations on qutrit-capable trapped-ion or superconducting platforms may be feasible in the near term, although no hardware experiment is reported.
- #idea:quantum-advantage — Performance claims are comparative only within quantum encodings (qutrit vs qubit) and do not establish advantage over classical portfolio solvers.
## Contradictions
- The paper suggests superior quantum performance via qutrit-over-qubit simulation results, but this conflicts with stronger notions of quantum advantage because no comparison against state-of-the-art classical optimization methods is provided.
- The paper discusses near-term feasibility and general preference for qutrit or higher-dimensional encodings, but its evidence is limited to very small instances (e.g., six assets) and simulation-only benchmarks, contradicting any implication of demonstrated scalability to realistic financial portfolio problems.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
