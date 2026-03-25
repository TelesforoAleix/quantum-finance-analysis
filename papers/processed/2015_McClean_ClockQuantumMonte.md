---
aliases:
- 'Clock Quantum Monte Carlo: an imaginary-time method for real-time quantum

  dynamics'
- Clock Quantum Monte Carlo
authors:
- Jarrod R. McClean
- Alán Aspuru-Guzik
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:50:03.225873'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:50:10.068037'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:50:47.323170'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:51:18.601329'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:51:53.184794'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:51:59.048165'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: 'Clock Quantum Monte Carlo: an imaginary-time method for real-time quantum

  dynamics'
topic_tags: []
year: 2014
zotero_key: ''
---

## Abstract summary
The paper introduces a method that combines the Feynman–Kitaev clock construction with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate real-time quantum dynamics via an imaginary-time ground-state algorithm. By mapping unitary time evolution to the ground state of a specially constructed “Clock Hamiltonian,” the authors adapt interacting-walker Monte Carlo techniques to dynamical problems and analyze how the dynamical sign problem manifests in this setting. They also propose time-dependent basis rotations to mitigate the sign problem and demonstrate that the resulting algorithm parallelizes efficiently in time, illustrating performance on quantum circuit examples.
## Methodology
This preprint presents a primarily methodological and computational study introducing 'Clock Quantum Monte Carlo,' which combines the Feynman-Kitaev Clock construction with Full Configuration Interaction Quantum Monte Carlo (FCIQMC) to simulate real-time quantum dynamics via an equivalent imaginary-time ground-state problem. The authors first derive the Clock Hamiltonian from the time-embedded discrete variational principle, showing that unitary evolution can be encoded as the ground-state history state of a Hermitian operator. They then adapt the standard FCIQMC interacting-walker algorithm to this Clock Hamiltonian, representing amplitudes over system-time configurations with signed real and imaginary walkers and iteratively applying a linearized propagator G = (1 - delta_tau H) through spawning, diagonal death/cloning, and annihilation steps. The method is evaluated numerically on synthetic quantum-circuit examples rather than financial data, including local rotation circuits, quasi-classical gate sets, and circuits with varying numbers of CNOT gates, to study the manifestation of the dynamical sign problem and the critical walker population needed for sign-coherent sampling. The paper also proposes time-dependent basis rotations to mitigate the sign problem and benchmarks a parallel-in-time MPI implementation using time-domain decomposition on a Linux cluster.

**Algorithms used:** FCIQMC, Feynman-Kitaev Clock, Clock Quantum Monte Carlo
**Frameworks:** MPI

**Experimental setup:** Numerical experiments were performed on simulated quantum circuits encoded into a Clock Hamiltonian and sampled with an adapted FCIQMC algorithm. The study includes tests on 11-qubit circuits with discrete time points, varying walker populations, and a parallel implementation using MPI on a standard Linux cluster with AMD Opteron 6376 processors. No quantum hardware or quantum software SDK is mentioned; this is a classical Monte Carlo simulation study.

**Dataset:** No external dataset was used. Inputs consist of synthetic quantum-circuit instances, including Toffoli-based reversible circuits, Pauli/CNOT gate constructions, local single-qubit rotation circuits, and mixed rotation-plus-CNOT circuits.
## Findings
- [speculative] The paper proposes Clock Quantum Monte Carlo (CQMC), combining the Feynman-Kitaev Clock mapping with FCIQMC to simulate real-time quantum dynamics via an imaginary-time ground-state search.
- [speculative] Any unitary quantum evolution can be reformulated as the ground-state eigenvalue problem of a Hermitian Clock Hamiltonian whose unique ground state is the history state encoding the full evolution.
- [speculative] The adapted FCIQMC procedure can in principle recover quantum dynamics by repeatedly applying a linearized propagator G = (1 - δτH) to the Clock Hamiltonian.
- [speculative] For generic problems, the critical walker number needed to remove sign-problem bias is expected to scale on the order of the Hilbert-space dimension and linearly with real time, implying potentially exponential cost in system size.
- [supported] The numerical examples show a sharp transition from sign-incoherent sampling, where observables collapse toward 0, to sign-coherent sampling once the walker population exceeds a critical threshold.
- [supported] The severity of the dynamical sign problem depends strongly on the rotation angle in local-rotation circuits; rotations closer to quasi-classical operations exhibit earlier and sharper transitions to sign-coherent sampling.
- [speculative] Stoquasticity of the Clock Hamiltonian is sufficient but not necessary for sign-problem-free sampling; the authors identify a broader 'quasi-classical' class of configuration-number-preserving evolutions that also avoid destructive sign interference.
- [supported] Time-dependent basis rotations can substantially mitigate the sign problem in the tested circuits, reducing the number of walkers required to reach sign-coherent sampling even when the circuit contains entangling CNOT gates.
- [supported] In the example with controlled-NOT-containing circuits, the rotated-basis approach outperformed the non-rotated basis by reaching converged sign-coherent behavior at lower walker counts.
- [supported] The Clock formulation enables a parallel-in-time decomposition because couplings are local in time, so only adjacent time slices need communication in the MPI implementation.
- [supported] Strong-scaling tests on a commodity AMD Opteron cluster achieved over 95% parallel efficiency with 2 processors and about 70% efficiency with 8 processors for the reported benchmark.
- [speculative] The authors argue the method could become a generally useful approach for quantum dynamics beyond the demonstrated quantum-circuit examples.

**Results summary:** This preprint introduces Clock Quantum Monte Carlo, a method that maps unitary real-time dynamics to a Hermitian ground-state problem using the Feynman-Kitaev Clock and then applies an adapted FCIQMC algorithm to sample the resulting history state. The paper provides numerical demonstrations on small quantum-circuit examples, showing that the dynamical sign problem manifests as a critical walker threshold below which observables become sign-incoherent and above which they converge. The authors further show that time-dependent basis rotations can reduce this sampling difficulty in tested circuits, including cases with entangling gates. They also report favorable parallel-in-time behavior due to the locality of the Clock Hamiltonian in the time dimension. However, the work is primarily methodological and simulation-based, with no demonstrated quantum advantage.

**Performance claims:**
- For the strong-scaling benchmark, parallel efficiency was over 95% with 2 processors.
- For the strong-scaling benchmark, parallel efficiency was about 70% with 8 processors.
- The reported scaling test used 11 qubits, 128 time points, and an average of 10^6 walkers per simulation-time step.
- In local-rotation simulations on 11 qubits, observables exhibited a threshold-like transition to correct sign-coherent values only after the walker population reached several times 10^5 walkers, depending on rotation angle.
- In the basis-rotation mitigation test, rotated-basis simulations with 4 and 8 CNOT gates reached sign-coherent sampling at lower walker counts than the corresponding unrotated simulations, with the plotted range extending to about 1.2×10^6 walkers.
## Quantum advantage claim
**Classification:** not-applicable

The paper presents a classical Monte Carlo simulation method for quantum dynamics and does not claim demonstrated quantum computational advantage. Any implications about efficient simulation are theoretical or heuristic rather than evidence of quantum advantage.
## Limitations
- As a preprint, the work has not undergone peer review.
- The dynamical sign problem remains a fundamental limitation; the authors note that the required walker number can in general grow exponentially with system size and linearly with real time.
- The method is only efficient under structural assumptions on the simulated operators; the system operators must be expressible as a polynomial number of terms so that matrix elements can be evaluated efficiently.
- Numerical demonstrations are limited to a few basic quantum circuits rather than broad classes of physical systems.
- Experiments appear to be restricted to small-scale examples (e.g., 11 qubits and 128 time points), limiting evidence for large-scale applicability.
- The proposed basis-rotation mitigation scheme is not generally constructive; the authors state that finding a basis that removes the sign problem is expected to be at least as difficult as solving the original evolution exactly.
- The local basis-rotation heuristic only partially addresses nontrivial entangling circuits and was tested mainly with simple local rotations plus CNOT structures.
- Parallel scaling results are demonstrated only with a basic MPI implementation on a commodity cluster and only up to a modest processor count, so scalability to larger HPC environments is not established.
- The paper notes that simulation-time-averaged observables may be biased due to the sign problem unless enough walkers are used to maintain sign coherence.
- [inferred] No comparison is provided against state-of-the-art classical real-time dynamics solvers, so relative practical advantage is unclear.
- [inferred] No application to financial-services problems or datasets is included, limiting direct relevance to finance use cases.
- [inferred] Reproducibility is limited by the absence of implementation details such as code, parameter sweeps, and full benchmark protocols.
## Open questions
- For which classes of dynamical problems does the critical walker number remain much smaller than the Hilbert-space dimension, as observed in some ground-state problems?
- How does the critical walker number scale with system size, simulation duration, and circuit structure for generic dynamical systems?
- What circuit or Hamiltonian features determine whether the Clock Hamiltonian is effectively sign-problem free, quasi-classical, or severely sign-problematic?
- How effective are different time-dependent basis-rotation schemes at mitigating the sign problem across more complex quantum circuits?
- What are the computational costs versus benefits of different basis-rotation choices?
- Can approximate basis rotations be found systematically without requiring knowledge equivalent to the exact evolution?
- How well does the method generalize beyond quantum circuits to broader quantum dynamics problems, including open-system settings?
- How far can the parallel-in-time approach scale before communication, load balancing, or annihilation overheads dominate?
- [inferred] Under what conditions does this approach outperform established tensor-network, Krylov, path-integral, or other classical simulation methods?

**Future work:**
- Study explicit connections between the fermionic sign problem and the dynamical sign problem to transfer tools between the two domains.
- Conduct further research on the costs and benefits of different basis-rotation strategies for sign-problem mitigation.
- Test the efficiency of rotation schemes on more complex quantum circuits and as a function of circuit structure.
- Extend the method beyond the demonstrated quantum-circuit examples to more general quantum dynamics applications.
- Further investigate scaling properties of the critical walker number for dynamical systems.
- Develop improved state-generation probabilities using more detailed knowledge of the unitary operators rather than the uniform selection used here.
- Explore more advanced parallel implementations to exploit the method's parallel-in-time structure more fully.
- [inferred] Benchmark the method against leading classical dynamics algorithms on standardized problems.
- [inferred] Validate the approach on larger and more realistic application instances, including domain-specific problems such as finance if relevant to the review scope.
## Key ideas
- #idea:near-term-feasibility — Proposes Clock Quantum Monte Carlo, a fully classical method for simulating quantum dynamics by mapping unitary evolution to a Clock Hamiltonian ground-state problem.
- #idea:hybrid-approach — Adapts FCIQMC-style interacting-walker Monte Carlo to the Feynman-Kitaev Clock construction and uses basis-rotation heuristics plus MPI parallel-in-time decomposition as a practical computational strategy.
- #contradiction:scalability — Although the method works on small synthetic circuit examples, the paper states that the critical walker population can scale with Hilbert-space dimension and linearly with real time, implying poor scalability for generic problems.
## Contradictions
- The paper's methodological promise of simulating real-time quantum dynamics is undercut by its own limitation that the required walker number may grow exponentially with system size, contradicting any broad implication of scalable applicability.
- The paper reports good parallel efficiency on small benchmarks, but this does not resolve the underlying dynamical sign problem, so computational scaling in processor count does not translate into evidence of scaling to large problem instances.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Synthetic quantum-circuit test cases rather than empirical datasets. Examples include: (1) 11-qubit circuits initialized in |0>^⊗N with a single local rotation R(theta) applied uniformly, e.g. theta = 5pi/32; (2) angle sweeps over local rotations with theta values including 0, pi/16, pi/8, and 3pi/16; (3) circuits composed of local rotations followed by a variable number of controlled-NOT gates, with theta = 0.49; and (4) a strong-scaling benchmark using 11 qubits, 128 time points, and consecutive local rotations with theta approximately 0.098. No preprocessing pipeline is applicable.

### Process
1. Map discrete unitary dynamics to a Hermitian Clock Hamiltonian H whose ground state is the history state. 2. Initialize a walker population over system-time basis states with integer real and imaginary weights. 3. Iteratively apply the linearized imaginary-time propagator G = (1 - delta_tau H). 4. In each iteration perform: (a) spawning from each parent walker to connected states at adjacent times using probabilities proportional to off-diagonal matrix elements and delta_tau; (b) diagonal death/cloning using pd = delta_tau (H_ii - S), where S is a population-control shift; and (c) annihilation by combining walkers on identical system-time configurations. 5. Continue until equilibration at simulation time tau > tau_eq, then estimate observables from the sampled history state and average over simulation time with autocorrelation correction. 6. Study convergence as a function of mean walker number to identify the transition from sign-incoherent to sign-coherent sampling. 7. Introduce time-dependent basis rotations B_t, replacing U_t with U'_t = B^dagger_{t+1} U_t B_t, and compare rotated versus non-rotated simulations. 8. For parallel tests, decompose the time dimension across MPI processes and measure strong scaling and parallel efficiency.

### Output
Outputs are reported as computed expectation values of observables such as <Sz> for a single qubit at the final simulation time, plotted against the mean number of walkers. The study also reports qualitative and quantitative evidence of the sign problem via the critical walker threshold for sign-coherent sampling, compares rotated-basis versus non-rotated-basis performance, and reports parallel speedup and parallel efficiency as a function of processor count. Comparisons are primarily internal methodological comparisons across gate sets, rotation angles, walker populations, and basis-rotation strategies rather than against standard classical dynamics solvers.

### Parameters
- qubits: 11
- time_points: 128
- walker_count: varied; examples up to about 1.2e6 mean walkers, with 1e6 average walkers used in strong-scaling benchmark
- rotation_angles: ['5pi/32', '0', 'pi/16', 'pi/8', '3pi/16', '0.49', 'approximately 0.098']
- propagator: G = (1 - delta_tau H)
- time_step: delta_tau (not numerically specified in the provided text)
- population_control: shift parameter S
- processors_tested: up to about 70 cores shown in scaling figure
- parallel_efficiency: over 95% with 2 processors and about 70% with 8 processors

### Hardware
{'hardware_type': 'classical HPC cluster', 'cluster_os': 'Linux', 'cpu_model': 'AMD Opteron 6376', 'parallelization': 'MPI with time-domain decomposition', 'quantum_hardware': 'none'}

### Reproducibility
Preprint with substantial algorithmic detail, including derivation, update equations, and benchmark problem descriptions, but no code repository or implementation package is mentioned in the provided text. Inputs are synthetic and reproducible in principle, yet some practical details such as exact delta_tau choices, equilibration criteria, runtime settings, and full implementation specifics are incomplete, so replication is possible but not turnkey.
