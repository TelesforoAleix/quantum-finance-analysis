---
aliases:
- Pengembangan Algoritma Kuantum Terinspirasi untuk Penyelesaian Masalah Optimasi
  Kompleks dalam Ilmu Komputasi
- Pengembangan Algoritma Kuantum Terinspirasi
authors:
- Yona Eka Pratiwi
- Renatalia Fika
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.59031/jnts.v1i2.773
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Journal of New Trends in Sciences
methodology_tags:
- QAOA
- VQE
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:02:34.512161'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:02:38.069920'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:02:52.273910'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:03:02.548530'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:03:25.164935'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:03:34.147733'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/QAOA
- method/VQE
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Pengembangan Algoritma Kuantum Terinspirasi untuk Penyelesaian Masalah Optimasi
  Kompleks dalam Ilmu Komputasi
topic_tags: []
year: 2023
zotero_key: ''
---

## Abstract summary
The paper investigates quantum-inspired algorithms that blend quantum computing principles with classical evolutionary methods to tackle complex optimization problems. Focusing on quantum-inspired genetic and evolutionary algorithms applied to combinatorial tasks like the Traveling Salesman Problem and Minimum Spanning Tree, the authors use computational simulations to compare performance against traditional algorithms. They assess convergence time, solution quality, and avoidance of local minima, and discuss implications and remaining challenges for scaling and hardware integration in real-world applications such as finance, logistics, telecommunications, and energy management.
## Methodology
The paper presents a simulation-based empirical study of quantum-inspired optimization methods for complex combinatorial optimization problems. The stated methodology combines a conceptual description of Quantum-Inspired Algorithms (QIAs), especially Quantum-Inspired Genetic Algorithm (QIGA), with computational simulations on benchmark problems including the Traveling Salesman Problem (TSP) and Minimum Spanning Tree (MST). In the methods section, the authors describe defining an optimization problem, modeling it in a quantum-style representation, applying QAOA with quantum gate rotations and measurement to estimate optimal solutions, and then testing the approach on a quantum simulation platform. The study evaluates performance against classical algorithms, especially conventional genetic algorithms, using convergence time, solution quality relative to the global optimum, and computational efficiency. Reported results claim that QIAs converge faster and achieve higher-quality solutions than classical baselines, but the paper provides only high-level methodological descriptions and lacks detailed implementation specifics such as simulator name, parameter settings, dataset instances, and optimization hyperparameters.

**Algorithms used:** QIGA, QIEA, QAOA, VQE

**Experimental setup:** Computational simulations were conducted on quantum simulation devices/platforms rather than clearly identified real quantum hardware. The experiments were described as applying QIAs/QAOA/VQE to combinatorial optimization problems such as TSP and MST and comparing outcomes with classical algorithms, particularly conventional genetic algorithms.

**Dataset:** Synthetic/benchmark combinatorial optimization problem instances: Traveling Salesman Problem (TSP) and Minimum Spanning Tree (MST). No real financial dataset was used.
## Experiment details
### Input
Input consists of optimization problem formulations for TSP and MST with decision variables x_i. The paper does not specify the source of instances, number of nodes, number of instances, feature representation, preprocessing, or any time period.

### Process
The described pipeline is: (1) define the optimization problem such as TSP or MST; (2) model the problem in a quantum-style system representation |Psi> linked to the objective function f(x); (3) apply QAOA using quantum gate rotations U(gamma,beta) with problem Hamiltonian H_P and control Hamiltonian H_C, followed by measurement to estimate the optimal solution; (4) run computational simulations on a quantum simulator; (5) compare the obtained solutions with those from classical algorithms such as conventional genetic algorithms; and (6) evaluate using convergence time, solution quality, and computational efficiency. The paper also conceptually describes QIGA as representing individuals in quantum form and using quantum-inspired selection and crossover. No iteration counts, shot counts, optimizer loops, stopping criteria, or parameter tuning details are reported.

### Output
Outputs are reported as convergence time, solution quality/accuracy relative to the global optimum, and computational efficiency. The main baseline comparison is against traditional classical algorithms, especially classical genetic algorithms. Reported headline results are that QIAs require only about 25-30% of the convergence time of classical algorithms and achieve approximately 98-99% of the global optimum versus 90-92% for classical methods.

### Parameters

### Hardware
The paper mentions use of a quantum simulation platform/device ('perangkat simulasi kuantum') but does not identify the simulator software, hardware backend, cloud provider, qubit count, noise model, or transpilation settings.

### Reproducibility
Reproducibility is low. No code, simulator configuration, benchmark instance details, parameter settings, or data files are provided. The paper gives only a high-level workflow and summary metrics, which is insufficient for exact replication.
## Findings
- [supported] In computational simulations on Traveling Salesman Problem (TSP) and Minimum Spanning Tree (MST), quantum-inspired algorithms (QIAs) converged faster than classical genetic algorithms, requiring about 25-30% of the classical convergence time.
- [supported] In the same simulations, QIAs achieved solution quality of about 98-99% of the global optimum, compared with 90-92% for the classical baseline.
- [supported] The reported evidence is based on simulation only, not execution on real quantum hardware.
- [supported] The paper claims QIAs reduce computational time significantly for optimization problems with many variables and constraints relative to traditional methods.
- [supported] The authors report that QIAs are better at avoiding local minima than classical algorithms in the tested optimization settings.
- [speculative] The paper suggests QIAs could be valuable for real-world applications including finance, logistics, telecommunications, and energy management, but no finance-specific experiment is presented.
- [speculative] The paper argues that scalability and hardware integration remain open challenges for larger and more complex optimization problems.

**Results summary:** This peer-reviewed empirical paper reports simulation-based comparisons of quantum-inspired algorithms against classical optimization methods on TSP and MST benchmark problems. The main empirical result is that QIAs achieved substantially faster convergence, using only about 25-30% of the time required by classical algorithms, while also producing higher-quality solutions at roughly 98-99% of the global optimum versus 90-92% for the classical baseline. The study attributes these gains to improved exploration of the solution space and better avoidance of local minima. However, the evidence is limited to computational simulation, with no real quantum hardware results, no confidence intervals or statistical significance reporting, and no direct financial-services use case despite mentioning potential finance applications.

**Performance claims:**
- Convergence time for QIAs was about 25-30% of the time required by classical algorithms on TSP and MST simulations
- Solution quality reached about 98-99% of the global optimum for QIAs
- Classical baseline solution quality was about 90-92% under similar conditions
- Significant reduction in computational time relative to traditional methods was reported, but exact absolute runtimes were not provided
## Quantum advantage claim
**Classification:** speculative

The paper reports improved performance for quantum-inspired classical algorithms in simulation, not a demonstrated quantum computing advantage. No real quantum hardware evidence is provided, and the claims concern quantum-inspired methods rather than actual quantum speedup.
## Limitations
- Experiments are limited to computational simulations rather than deployment on real quantum hardware or real industrial systems.
- Evaluation is restricted to benchmark combinatorial problems (TSP and MST), limiting evidence for applicability to financial services or other domain-specific real-world tasks.
- The paper explicitly notes scalability challenges: performance may degrade for very large, high-dimensional problems or problems with many complex constraints.
- The paper states that hardware integration remains a challenge, especially for larger and more intricate optimization problems.
- The paper highlights limitations related to noisy intermediate-scale quantum (NISQ) devices, including the need for better error mitigation.
- Efficiency on highly complex problems is said to depend on external factors such as hardware quality and the specific quantum algorithm used.
- [inferred] The study appears to use small-to-medium problem instances; exact dataset sizes, instance counts, and problem scales are not reported, weakening internal validity.
- [inferred] Reproducibility is limited because the paper does not provide sufficient implementation details, simulation settings, hyperparameters, software stack, or code.
- [inferred] The empirical comparison seems to be against traditional/classical genetic algorithms only, with no comparison to stronger state-of-the-art classical optimization baselines.
- [inferred] Claims about applications in finance, logistics, telecommunications, and energy are not empirically validated within the study.
- [inferred] The paper conflates quantum-inspired classical algorithms with quantum algorithms/hardware in several places, which may blur the validity of conclusions about actual quantum advantage.
- [inferred] No statistical significance analysis, variance across runs, or robustness analysis is reported, so the stability of the reported 98-99% accuracy is unclear.
- [inferred] The source contains signs of literature-synthesis style writing and broad claims, suggesting limited original empirical depth despite being presented as an empirical study.
## Open questions
- How well do quantum-inspired algorithms scale to much larger optimization problems with many variables and complex constraints?
- To what extent can improved hardware integration enhance QIA performance in practical industrial applications?
- How effective are error-mitigation techniques in preserving performance when these methods are implemented on noisy quantum hardware?
- Can the reported convergence and accuracy gains be maintained on real-world optimization tasks rather than benchmark problems like TSP and MST?
- How do QIAs compare against modern state-of-the-art classical solvers on the same optimization tasks?
- What problem sizes or structures mark the point where QIA performance begins to deteriorate?
- Can these methods deliver practical value in financial applications such as portfolio optimization under realistic market constraints and data?
- What is the relative contribution of algorithm design versus hardware quality to the observed performance improvements?

**Future work:**
- Optimize QIAs further to improve scalability and computational efficiency on larger and more complex problems.
- Develop stronger quantum hardware to better support large-scale optimization tasks.
- Integrate more effective error-mitigation techniques to improve performance in real-world applications.
- Investigate tighter hardware-algorithm integration to maximize efficiency.
- Extend empirical testing to practical industrial domains such as finance, logistics, and telecommunications.
- Validate QIAs on larger, more realistic optimization instances with more complex constraints.
- [inferred] Benchmark QIAs against stronger classical baselines and hybrid methods to establish whether gains persist under more rigorous comparison.
- [inferred] Provide reproducible implementations, parameter settings, and standardized evaluation protocols.
- [inferred] Test on real financial datasets and production-like portfolio optimization settings rather than generic benchmark problems.
- [inferred] Study robustness across repeated runs, noise conditions, and varying instance distributions.
## Key ideas
- #idea:quantum-advantage — The paper reports simulation-based performance gains of quantum-inspired methods over classical genetic algorithms on TSP/MST, with faster convergence and higher solution quality.
- #idea:hybrid-approach — It presents a hybrid framing that mixes quantum-inspired evolutionary representations with QAOA/VQE-style simulated optimisation and classical comparison workflows.
- #idea:near-term-feasibility — The work suggests possible practical relevance for optimisation domains including finance, but only as a future application contingent on better scalability and hardware integration.
## Contradictions
- The paper implies quantum-style superiority, but the reported gains come from quantum-inspired classical algorithms and simulator-based experiments rather than demonstrated quantum hardware advantage, creating a #contradiction:classical-vs-quantum.
- The paper suggests applicability to large real-world optimisation problems including finance, yet it only evaluates small benchmark TSP/MST instances in simulation and explicitly acknowledges scaling difficulties for larger, more constrained problems, creating a #contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
