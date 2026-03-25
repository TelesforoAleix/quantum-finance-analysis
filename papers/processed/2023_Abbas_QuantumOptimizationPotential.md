---
aliases:
- 'Quantum Optimization: Potential, Challenges, and the Path Forward'
- Quantum Optimization Potential Challenges
authors:
- Amira Abbas
- Andris Ambainis
- Brandon Augustino
- Andreas Bärtschi
- Harry Buhrman
- Carleton Coffrin
- Giorgio Cortiana
- Vedran Dunjko
- Daniel J. Egger
- Bruce G. Elmegreen
- Nicola Franco
- Filippo Fratini
- Bryce Fuller
- Julien Gacon
- Constantin Gonciulea
- Sander Gribling
- Swati Gupta
- Stuart Hadfield
- Raoul Heese
- Gerhard Kircher
- Thomas Kleinert
- Thorsten Koch
- Georgios Korpas
- Steve Lenk
- Jakub Marecek
- Vanio Markov
- Guglielmo Mazzola
- Stefano Mensa
- Naeimeh Mohseni
- Giacomo Nannicini
- Corey O’Meara
- Elena Peña Tapia
- Sebastian Pokutta
- Manuel Proissl
- Patrick Rebentrost
- Emre Sahin
- Benjamin C. B. Symons
- Sabine Tornow
- Víctor Valls
- Stefan Woerner
- Mira L. Wolf-Bauwens
- Jon Yard
- Sheir Yarkoni
- Dirk Zechiel
- Sergiy Zhuk
- Christa Zoufal
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
journal_or_venue: 'Los Alamos National Laboratory / Intended for: arXiv'
methodology_tags:
- QAOA
- VQE
- amplitude-estimation
- QUBO
- variational
- grover
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: technical-report
source_type_confidence: high
step1_date: '2026-03-25T15:59:05.988570'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:59:15.038212'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:59:29.287980'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:00:09.746618'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:01:07.120696'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:01:19.735825'
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
- topic/risk-modelling
- method/QAOA
- method/VQE
- method/amplitude-estimation
- method/QUBO
- method/variational
- method/grover
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum Optimization: Potential, Challenges, and the Path Forward'
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2023
zotero_key: ''
---

## Abstract summary
This technical report surveys the landscape of quantum optimization, linking complexity-theoretic insights with concrete algorithmic paradigms such as Grover search, adiabatic algorithms, phase estimation, Gibbs sampling, and variational methods. It systematically reviews how these tools apply across major optimization classes (discrete, convex, non-convex, mixed-integer, dynamic, robust, and multi-objective), and analyzes execution issues on noisy gate-based hardware including transpilation, error mitigation, and benchmarking. The authors also propose benchmarking principles and illustrate potential application domains, with detailed discussions of asset allocation in finance and problems arising in sustainable energy systems.
## Methodology
This technical report adopts a broad analytical and specification-oriented methodology rather than an experimental one. It synthesizes perspectives from a large multi-institution working group to structure the field of quantum optimization along four main axes: computational complexity theory, paradigms for quantum optimization algorithm design, optimization problem classes, and execution on noisy hardware at scale. The report first uses complexity-theoretic analysis to distinguish exact, approximate, and heuristic settings and to identify where quantum advantage may or may not be possible. It then organizes the algorithmic landscape around core building blocks such as Grover search, the quantum adiabatic algorithm, quantum phase estimation, Gibbs sampling, approximation algorithms, and variational methods. Next, it classifies optimization problems into discrete, continuous, mixed-integer, dynamic programming, optimal control, robust, and multi-objective optimization, reviewing known quantum approaches and open questions for each. A dedicated section specifies the practical quantum execution stack for noisy devices, including modeling choices, transpilation, error suppression/mitigation, pulse-level compilation, and hardware benchmarking metrics such as layer fidelity, error per layered gate, quantum volume, and CLOPS. The report also proposes a benchmarking methodology for fair comparison with classical optimization, emphasizing benchmark goals, model dependence, preprocessing, platform selection, and evaluation metrics such as resource cost, runtime, solution quality, and problem complexity. Finally, it scopes illustrative application domains, including financial asset allocation and sustainable energy transition, as candidate sources of realistic benchmark problems. Overall, the methodology is a structured technical survey and framework-building exercise that defines standards, scope, terminology, benchmark design principles, and implementation considerations for quantum optimization rather than reporting a single empirical study.

**Algorithms used:** Grover Search, Quantum Adiabatic Algorithm, Quantum Phase Estimation, Gibbs Sampling, QAOA, VQE, QITE, Quantum Alternating Operator Ansatz, Recursive QAOA, Quantum Random Access Optimization, Quantum Hamiltonian Descent, Quantum Central Path Method, Quantum SDP solvers, Quantum branch-and-bound, Quantum dynamic programming, Quantum reinforcement learning, Quantum amplitude estimation, Warm-start QAOA, Variational quantum algorithms
**Frameworks:** Qiskit, OpenQASM, Quil, Blackbird, IBM Quantum
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [supported] The report concludes that complexity theory is useful for identifying where quantum advantage in optimization may be possible, but is neither necessary nor sufficient for practical quantum advantage.
- [speculative] The authors argue that exponential quantum speedups for NP-hard optimization problems are unlikely in general worst-case settings, while practical advantages may still arise on structured or typical instances.
- [speculative] Grover-based optimization offers at most a quadratic speedup over brute-force search for generic discrete optimization, which still leaves exponential runtime for many NP-hard problems.
- [speculative] Quantum adiabatic optimization is limited by spectral-gap scaling, implying at most polynomial speedups in many relevant settings and often exponentially long annealing times in glassy phases.
- [speculative] Variational quantum algorithms such as VQE and QAOA are currently best viewed as heuristics rather than methods with broad provable guarantees for general optimization problems.
- [speculative] Barren plateaus are identified as a major scaling bottleneck for variational quantum optimization, especially as circuit expressivity and system size increase.
- [speculative] Quantum optimization should be benchmarked with clear, fair, and reproducible metrics against classical methods, including time-to-solution, solution quality, resource cost, and problem complexity.
- [supported] The report recommends benchmarking on meaningful real-world-inspired problems rather than relying only on abstract complexity claims or small toy QUBOs.
- [speculative] Finance and sustainability are highlighted as promising domains for future benchmarking and eventual validation of real-world quantum optimization impact.
- [speculative] In finance, practically relevant asset-allocation problems become substantially harder when uncertainty, transaction costs, and multi-period dynamics are included, making them richer targets than simplified binary portfolio QUBOs.
- [speculative] In sustainable energy and e-mobility, optimization problems such as EV scheduling, charging/discharging control, and energy retailing with storage provide realistic testbeds that connect to knapsack, dynamic programming, MIP, and stochastic control formulations.
- [supported] The report recommends developing quantum-native problem formulations, hardware-aware encodings, and benchmarking suites that account for noisy hardware constraints rather than assuming idealized execution.
- [supported] The authors conclude that progress in quantum optimization will require both theoretical analysis and empirical testing on real hardware, especially as devices scale beyond exact classical simulation.

**Results summary:** This technical report provides a broad assessment of quantum optimization, emphasizing recommendations and technical conclusions rather than new empirical performance results. It argues that worst-case complexity theory alone does not determine practical utility, and that while large exponential speedups for generic NP-hard optimization are unlikely, structured instances, approximation settings, and heuristic methods may still offer useful opportunities. The report reviews algorithmic paradigms including Grover search, adiabatic methods, QAOA, VQE, Gibbs sampling, and quantum approaches to convex, discrete, mixed-integer, dynamic, robust, and multi-objective optimization. It stresses that noisy hardware, transpilation, encoding, and error mitigation strongly affect practical performance, and therefore benchmarking must use fair, reproducible metrics and realistic problem families. As policy and technical guidance, it recommends focusing on benchmark design, hardware-aware modeling, and application domains such as finance and sustainability, where increasingly realistic optimization formulations can serve as testbeds for future validation of quantum optimization impact.

**Performance claims:**
- Grover-based optimization can reduce brute-force runtime from O(2^n) to O(sqrt(2^n)) for n-variable problems
- Quantum adiabatic algorithm runtime scales as O(1/Delta^2) with the minimum spectral gap Delta
- Quantum imaginary time evolution is stated to require time O(n/Delta) to exceed a fixed overlap with the ground state under stated assumptions
- For MAXCUT on 3-regular graphs, QAOA worst-case lower bounds are reported as 0.692 for p=1, 0.7559 for p=2, and 0.7924 for p=3 under certain assumptions
- Goemans-Williamson approximation ratio for MAXCUT is cited as approximately 0.87856
- QRAO approximation ratios for MAXCUT are reported as 0.555, 0.625, and 0.722 for variable-to-qubit ratios of 3, 2, and 1.5 respectively
- Quantum SDP approach for MAXCUT is described as achieving runtime O-tilde(n^1.5) plus input-read cost under QRAM assumptions
- Quantum branch-and-bound is reported to solve most Sherrington-Kirkpatrick instances in time O(2^0.226n) with high probability
- Quantum dynamic programming speedups cited include TSP runtime O(1.728...^n) versus classical O*(2^n), generic vertex ordering O(1.817...^n) versus O*(2^n), graph coloring O(1.7956...^n) versus O(2^n), and treewidth O(1.538...^n) versus O(1.755...^n)
- Hardware benchmark examples cite IBM metrics including EPLG of 1.7% and CLOPS of 2700 on ibm_sherbrooke
- Experimental QAOA demonstrations summarized in the report include up to 414 variables on heavy-hex instances with reported mean approximation ratios around 0.56-0.57 and best ratios around 0.68-0.69, though these are literature survey results rather than new experiments in this report
## Quantum advantage claim
**Classification:** theoretical

The report does not demonstrate a new end-to-end quantum advantage. It mainly surveys and analyzes where quantum advantage may be possible in theory, stresses that generic NP-hard advantage is unlikely in worst-case settings, and recommends benchmarking realistic applications to test practical advantage claims.
## Limitations
- The report emphasizes that complexity-theoretic results are neither necessary nor sufficient for establishing practical quantum advantage in optimization.
- Worst-case complexity analysis may poorly reflect practical optimization instances, limiting the direct applicability of many theoretical conclusions.
- Many promising quantum optimization approaches discussed are heuristic and lack provable performance or runtime guarantees.
- Near-term execution is strongly limited by noise; meaningful large-scale optimization likely requires fault-tolerant quantum computing for many exact and approximation algorithms.
- Quantum error correction is acknowledged as introducing significant qubit overhead, limiting near-term scalability.
- Execution on noisy hardware remains constrained by circuit depth, qubit connectivity, transpilation overhead, and hardware-specific noise.
- Benchmarking quantum and classical optimization fairly is difficult because heuristic performance is instance-dependent and often unknown a priori.
- Many proposed quantum speedups for convex optimization and SDP solving rely on QRAM assumptions, whose scalable fault-tolerant implementation remains unresolved.
- For SDP and related methods, input/output bottlenecks can reduce theoretical end-to-end quantum advantages to polynomial or less.
- Several quantum optimization methods, including Grover-based search, QAA, QPE, and many dynamic-programming speedups, are expected to require fault-tolerant quantum computing and are therefore not near-term practical.
- QAOA and related variational methods face barren plateaus and parameter-training difficulties, which hinder scaling to practically relevant problem sizes.
- Constraint handling in quantum optimization often shifts complexity rather than removing it, e.g., from penalty terms to more complex mixers or projections.
- Many real-world optimization problems are simplified to QUBO formulations, but such reductions can destroy useful structure, increase density, require large penalty weights, and may only preserve equivalence for exact solutions.
- The report notes that most existing hardware demonstrations focus on simplified, low-density, or hardware-tailored instances rather than practically realistic optimization models.
- Illustrative finance and sustainability applications are presented as exploratory playgrounds rather than validated demonstrations of practical quantum advantage.
- As a technical report intended for arXiv, the document is not peer reviewed, so claims and synthesis should be interpreted with caution. [inferred]
- The report is broad and synthetic rather than a systematic empirical evaluation, so many conclusions depend on literature interpretation rather than new controlled experiments. [inferred]
- Because this is a technical report from a multi-institution working group, its scope is shaped by consensus-building and broad coverage rather than deep validation of any one application domain. [inferred]
- Currency of hardware and benchmarking claims may age quickly given the rapid pace of quantum hardware development. [inferred]
- For financial-services relevance specifically, the paper discusses finance only as an illustrative application area and does not provide domain-specific empirical validation on production financial workflows. [inferred]
## Open questions
- Can practical quantum advantage be achieved in optimization even when strict complexity-theoretic separations are unavailable?
- Can quantum algorithms saturate known inapproximability bounds that classical methods have not yet reached?
- If approximation ratios cannot be improved, can quantum methods still provide meaningful computational speedups over classical approximation algorithms?
- How can quantum heuristic methods be designed to exploit structure in practically relevant optimization instances?
- How can the relation between factoring-based QUBO instances and practical optimization be harnessed meaningfully?
- Can warm-started QAOA with custom mixers be given provable guarantees at finite circuit depth?
- What ansatz designs are suitable for variational imaginary-time and real-time evolution methods in optimization?
- How can quantum-specific preprocessing simplify optimization problems analogously to classical presolve methods?
- How do a priori and a posteriori performance guarantees carry over when algorithms are executed on noisy quantum hardware?
- How should optimization problems be modeled and mapped to hardware to minimize the impact of noise?
- Can special constraints be incorporated natively into quantum algorithms without incurring prohibitive circuit complexity?
- Can dynamic data-structure ideas used in quantum LP methods be extended to SDPs?
- Can quantum interior-point and SDP methods deliver overall speedups once numerical conditioning and tomography costs are fully accounted for?
- What lower bounds hold for various settings of quantum polynomial and non-convex optimization?
- Which classes of non-convex functions admit efficient amplitude-encoded embeddings, quantum gradient computation, and convergent quantum optimization procedures?
- Can there be a general meta-theorem characterizing provable quantum advantage for mixed-integer programming?
- What is the best possible quantum speedup for branch-and-bound or branch-and-cut methods, and can it be super-quadratic in general settings?
- Which MIP reformulations (e.g., Dantzig-Wolfe, moment/SOS, copositive) are most promising for quantum acceleration?
- Can quantum dynamic programming be generalized beyond hypercube-structured state spaces?
- Can stochasticity be incorporated effectively into quantum dynamic programming and MDP algorithms?
- What MDP classes could benefit from quantum speedups while remaining practically relevant?
- Can near-term quantum methods provide useful advantages for robust optimization under uncertainty?
- What quantum-native algorithms can be developed for multi-objective optimization rather than relying on classical scalarization plus quantum subroutines?
- Which benchmark problems and metrics can fairly compare quantum and classical optimization across platforms?
- Which real-world finance and sustainability optimization instances are genuinely hard classically yet still compatible with near-term or early fault-tolerant quantum hardware?

**Future work:**
- Develop and analyze new quantum optimization heuristics, even before full theoretical guarantees are available.
- Benchmark quantum optimization algorithms systematically on real quantum hardware rather than relying only on simulation or asymptotic theory.
- Establish clear, reproducible, and fair benchmarking standards, metrics, and problem libraries for quantum optimization.
- Investigate optimization problems beyond QUBO and broaden focus to richer problem classes such as constrained, stochastic, robust, mixed-integer, and multi-objective optimization.
- Study quantum-tailored problem formulations, encodings, and preprocessing methods that preserve useful structure and reduce hardware cost.
- Develop better methods for handling constraints natively in quantum algorithms.
- Advance parameter-training strategies, transferability methods, and initialization schemes for QAOA and other VQAs.
- Explore quantum acceleration of classical PTAS, SDP relaxations, branch-and-bound, decomposition, and dynamic-programming methods.
- Design hardware-optimized algorithms, transpilation methods, and pulse-level implementations that reduce circuit depth and duration.
- Develop error-mitigation methods that improve not only expectation values but also the quality of sampled solutions for optimization.
- Test and scale quantum optimization heuristics on devices with more than 100 qubits to build intuition about practical performance under noise.
- Create application-tailored benchmarks for optimization rather than relying only on generic hardware metrics.
- Investigate finance applications at increasing levels of realism, especially asset allocation under uncertainty, transaction costs, and multi-period dynamics.
- Investigate sustainability and energy-transition use cases with increasing realism, including EV scheduling, storage control, and stochastic energy retailing.
- Prioritize use cases with positive societal impact, such as sustainable energy transition, when directing future quantum optimization research.
## Key ideas
- #idea:quantum-advantage — The report argues that practical quantum advantage in optimization is more plausible for structured instances and specific subroutines than for generic NP-hard problems.
- #idea:near-term-feasibility — QAOA, VQE, and related variational methods are framed as the main NISQ-era options, but their performance is heavily constrained by noise, barren plateaus, and training difficulty.
- #idea:hybrid-approach — The paper advocates hybrid quantum-classical workflows, especially for realistic finance problems where quantum routines may accelerate subproblems inside classical optimization frameworks.
- #idea:quantum-advantage — Finance, especially asset allocation and related risk-aware formulations, is presented as a promising benchmark domain where even modest optimization speedups could matter.
- #idea:hybrid-approach — The report recommends moving beyond simplistic QUBO portfolio encodings toward richer formulations with uncertainty, transaction costs, and multi-period dynamics.
- #idea:near-term-feasibility — Fair benchmarking on real hardware with hardware-aware encodings, transpilation, and error mitigation is treated as more important than abstract asymptotic claims.
## Contradictions
- The report explicitly rejects broad claims of exponential quantum advantage for generic NP-hard optimization, contradicting more optimistic finance papers that imply QAOA/QUBO formulations alone yield strong superiority for portfolio optimization.
- The paper argues that most rigorous speedups rely on fault-tolerant hardware, QRAM, and favorable assumptions, contradicting near-term scalability claims made in some application-driven quantum finance studies.
- It states that QAOA and related VQAs remain heuristics without established superiority over strong classical solvers, contradicting interpretations of small-scale portfolio or risk experiments as evidence of general quantum advantage.
- Its emphasis on noise, compilation overhead, and error-mitigation cost contradicts narratives that current NISQ devices can already support realistic large-scale financial optimization workloads.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
