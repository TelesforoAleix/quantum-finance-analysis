---
aliases:
- Hybrid Heuristic Algorithms for Adiabatic Quantum Machine Learning Models
- Hybrid Heuristic Algorithms Adiabatic
authors:
- Bahram Alidaee
- Haibo Wang
- Lutfu S. Sua
- Wade W. Liu
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
methodology_tags:
- QUBO
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:02:38.495713'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:02:42.940587'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:03:10.446690'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:03:39.505010'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:04:11.400282'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:04:18.430929'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/QUBO
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid Heuristic Algorithms for Adiabatic Quantum Machine Learning Models
topic_tags: []
year: null
zotero_key: ''
---

## Abstract summary
The paper develops hybrid heuristic algorithms for training adiabatic quantum machine learning models formulated as large-scale QUBO problems. It introduces an r-flip local search strategy, derives theoretical conditions to prune the r-flip neighborhood after achieving 1-flip local optimality, and embeds these ideas in tabu-search-based hybrids. Extensive computational experiments on very large QUBO benchmarks compare these hybrids against the MST2 tabu search (used in quantum annealing solvers), showing that the proposed methods can find high-quality solutions more efficiently, making them suitable as warm-start or standalone optimizers in QUBO-based quantum ML applications.
## Methodology
The paper presents a peer-reviewed empirical and algorithmic study of hybrid heuristic methods for solving large-scale QUBO problems motivated by adiabatic quantum machine learning training. The methodology combines theoretical derivation and empirical benchmarking. First, the authors derive closed-form conditions for pruning candidate r-flip moves after reaching 1-flip local optimality, including Theorem 1, Proposition 1, and related lemmas that reduce the search space for improving multi-bit flips. They then implement several local-search heuristics in C++: Algorithm 3 and Algorithm 4 as hybrid r-flip/1-flip strategies, and Algorithm 5 as a hybrid 1-flip/r-flip tabu-search-based improvement method. The empirical evaluation compares these proposed methods, mainly with r=2, against the classical Multiple Start Tabu Search baseline MST2, described as the core of a D-Wave tabu solver. Experiments are conducted on standard benchmark UBQP/QUBO instances from the literature and on additional very-large-scale generated instances, with performance assessed over multiple independent runs under fixed CPU time limits. The study reports objective-function quality, frequency of reaching best-known values, variability across runs, and time-to-solution behavior, and further applies nonparametric statistical tests (Friedman, Nemenyi, and pairwise Wilcoxon with Bonferroni correction) to compare algorithmic performance. Although framed in the context of adiabatic quantum machine learning and quantum annealing solvers, the experiments themselves are classical heuristic optimization experiments rather than executions on a quantum processing unit.

**Algorithms used:** QUBO, 1-flip local search, r-flip local search, Tabu Search, Multiple Start Tabu Search (MST2), Simulated Annealing

**Experimental setup:** All proposed hybrid heuristics and comparisons were run as classical C++ programs on a single core of an Intel Xeon Quad-core E5420 machine with 8 GB RAM and 2.5 GHz CPU, compiled with GNU C++ v4.8.5 and submitted through Open PBS for consistent resource allocation. No real quantum hardware or quantum simulator was used. The study compared Algorithms 3, 4, and 5, primarily with r=2, and then compared the best-performing proposed method (Algorithm 5 with 1-flip and 2-flip variants) against the classical MST2 implementation from Palubeckis rather than the D-Wave Python wrapper, to avoid wrapper size limitations. Experiments used 10 runs per instance and CPU time limits of 60 seconds, 600 seconds, and for some 30,000-variable tests 600 seconds.

**Dataset:** Benchmark unconstrained binary quadratic programming / QUBO instances from the literature, especially larger-scale instances generated using Palubeckis's instance generator. The paper reports using up to 38 large-scale instances with 2,500 to 6,000 variables for candidate-set experiments, benchmark comparisons on large high-density instances with 3,000 to 8,000 variables, and additional generated very-large-scale high-density QUBO instances with 30,000 variables. Instance data is stated to be available online at https://doi.org/10.18738/T8/WDFBR5.
## Experiment details
### Input
Input consisted of synthetic/benchmark QUBO (UBQP) instances from prior literature and generated instances rather than financial datasets. Reported instance ranges include 38 larger-scale problems with 2,500-6,000 variables for analyzing the candidate set D(1), benchmark comparison instances with 3,000-8,000 variables and varying density, and additional high-density 30,000-variable QUBO instances. The paper discusses instance size and density as key factors; no feature engineering or financial preprocessing is described.

### Process
1. Formulate the optimization target as a QUBO/UBQP problem x^TQx. 2. Derive pruning conditions for improving r-flip moves after a 1-flip local optimum is reached, using derivative values E(x_i), bounds based on M = phi * C(r,2), and candidate-set construction strategies D(n) and D(1). 3. Implement Algorithm 3 and Algorithm 4 as dynamic hybrid local-search procedures that increase r incrementally, and Algorithm 5 as a tabu-search-based hybrid that embeds the r-flip strategy. 4. Run preliminary tests showing strong performance on smaller/low-density instances, then focus formal comparisons on larger high-density instances. 5. Compare Algorithms 3, 4, and 5 with r=2 on 30,000-variable instances under a 600-second CPU limit across 10 runs; select Algorithm 5 as best. 6. Compare Algorithm 5 (with 1-flip and 2-flip variants) against MST2 under 60-second and 600-second CPU limits, again using 10 runs per instance. 7. Record objective values, number of runs reaching the reported objective function value, relative standard deviation across runs, and time deviation to reach the objective value. 8. Perform Friedman omnibus testing across 27 complete instances, followed by Nemenyi post-hoc and pairwise Wilcoxon signed-rank tests with Bonferroni correction to assess significance of pairwise differences.

### Output
Outputs are optimization-performance metrics on QUBO benchmarks: objective function value (OFV), number of times the OFV/best-known solution was reached over 10 runs, relative standard deviation (RSD = 100*sigma/mu) of OFV across runs, and time deviation (DT) to reach OFV. Baseline comparisons were made against MST2, the Palubeckis multiple-start tabu search used as a proxy for the D-Wave tabu solver core. Reported summary results include that Algorithm 5 outperformed Algorithms 3 and 4 on 30,000-variable tests, and that Algorithm 5 with 1-flip or 2-flip significantly outperformed MST2 on the 27 benchmark instances according to Friedman, Nemenyi, and Wilcoxon tests, while 1-flip and 2-flip were not significantly different from each other.

### Parameters
- r_values: [1, 2]
- main_comparison_r: 2
- runs_per_instance: 10
- cpu_time_limits_seconds: [60, 600]
- large_instance_time_limit_seconds: 600
- tabu_tenure: 100
- mst2_initial_tabu_iterations: 25000 * problem_size
- mst2_subsequent_tabu_iterations: 10000 * problem_size
- statistical_tests: ['Friedman test', 'Nemenyi post-hoc test', 'Pairwise Wilcoxon signed-rank test with Bonferroni correction']

### Hardware
Classical hardware only: single core of Intel Xeon Quad-core E5420, 2.5 GHz, 8 GB RAM; GNU C++ compiler version 4.8.5; jobs submitted via Open PBS. No QPU, annealer, or quantum simulator execution was reported. The paper explicitly avoided the D-Wave Python wrapper and instead used the original MST2 C++ code for comparison.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail on algorithms, runtime limits, number of runs, baseline settings, and hardware. It also states that instance data are available via DOI and that Palubeckis's MST code and generator were downloaded. However, no source code for the newly proposed Algorithms 3-5 is reported in the text provided, and some algorithm pseudocode/tables are referenced but not fully included here, so full replication appears possible in principle but not turnkey.
## Findings
- [supported] The proposed hybrid heuristic with r-flip pruning (Algorithm 5) outperformed the baseline MST2 tabu-search benchmark on large dense QUBO instances in terms of reaching best-known solutions within fixed CPU budgets.
- [supported] On 27 benchmark instances with a 60-second CPU limit, MST2 matched 5/27 best solutions, while Algorithm 5 with 1-flip matched 26/27 and Algorithm 5 with 2-flip matched 18/27.
- [supported] On the same 27 benchmark instances with a 600-second CPU limit, MST2 matched 10/27 best solutions, while Algorithm 5 with 1-flip matched 25/27 and Algorithm 5 with 2-flip matched 23/27.
- [supported] For 30,000-variable QUBO instances evaluated over 10 runs, Algorithm 5 performed better than Algorithms 3 and 4, motivating its selection for comparison against MST2.
- [supported] Statistical testing found significant overall performance differences among MST2, 1-flip, and 2-flip variants (Friedman chi-squared = 19.9808, p = 4.5839e-05).
- [supported] Post-hoc Nemenyi tests showed significant differences between MST2 and 1-flip (p = 0.000176) and between MST2 and 2-flip (p = 0.001172), but not between 1-flip and 2-flip (p = 0.882488).
- [supported] Pairwise Wilcoxon tests with Bonferroni correction confirmed significant differences between MST2 and 1-flip (p = 0.000050) and between MST2 and 2-flip (p = 0.000011), with no significant difference between 1-flip and 2-flip (p = 1.000000).
- [supported] Preliminary experiments indicated that for instances smaller than 3,000 variables and with low density, Algorithms 3, 4, and 5 found best-known solutions within 10 seconds.
- [supported] The candidate set for r-flip search, |D(1)|, decreased as QUBO density increased and increased with problem size; the paper also reports that |D(1)| was smaller for better local optima, implying reduced r-flip search effort near high-quality solutions.
- [supported] All reported results were obtained from classical C++ implementations on a single-core Intel Xeon CPU; no real quantum hardware experiments were performed.
- [speculative] The authors argue that the r-flip strategy could improve QUBO-based adiabatic quantum machine learning workflows and serve as an effective warm-start local search for quantum annealing solvers.
- [speculative] The paper suggests applicability to AQML use cases such as quantum SVM, quantum k-means, feature selection, and fraud detection, but these application-level gains were not directly empirically validated in this study.

**Results summary:** This peer-reviewed empirical paper evaluates classical hybrid heuristic algorithms for large-scale QUBO optimization motivated by adiabatic quantum machine learning. The main empirical result is that the proposed Algorithm 5, which combines 1-flip/r-flip local search with tabu search, outperformed the MST2 baseline on 27 large benchmark instances under both 60-second and 600-second CPU limits. At 60 seconds, Algorithm 5 with 1-flip matched 26 of 27 best solutions versus 5 of 27 for MST2; at 600 seconds, it matched 25 of 27 versus 10 of 27 for MST2. The 2-flip variant also outperformed MST2 but was not statistically better than the 1-flip variant. Statistical tests supported these differences: Friedman chi-squared was 19.9808 (p = 4.5839e-05), and both Nemenyi and Bonferroni-corrected Wilcoxon post-hoc tests found MST2 significantly worse than both proposed variants. Results were obtained entirely via classical simulation/CPU execution, not on quantum hardware, so any implications for quantum annealing or AQML are indirect.

**Performance claims:**
- 60-second limit on 27 instances: MST2 matched 5/27 best solutions; Algorithm 5 (1-flip) matched 26/27; Algorithm 5 (2-flip) matched 18/27
- 600-second limit on 27 instances: MST2 matched 10/27 best solutions; Algorithm 5 (1-flip) matched 25/27; Algorithm 5 (2-flip) matched 23/27
- Friedman test across 27 instances: chi-squared = 19.9808, p = 4.5839e-05
- Nemenyi post-hoc p-values: MST2 vs 1-flip = 0.000176; MST2 vs 2-flip = 0.001172; 1-flip vs 2-flip = 0.882488
- Pairwise Wilcoxon with Bonferroni correction p-values: MST2 vs 1-flip = 0.000050; MST2 vs 2-flip = 0.000011; 1-flip vs 2-flip = 1.000000
- Preliminary tests: for instances under 3,000 variables and low density, Algorithms 3, 4, and 5 found best-known solutions within 10 seconds
- Very-large-scale experiments included QUBO instances up to 30,000 variables with 10 runs per instance and a 600-second CPU limit
## Quantum advantage claim
**Classification:** speculative

The paper is motivated by adiabatic quantum machine learning and compares classical heuristics against a classical MST2 tabu-search baseline used in quantum annealing workflows, but all experiments were run classically on CPU and no quantum hardware or quantum speedup over classical methods was demonstrated.
## Limitations
- The proposed methods are heuristic and do not guarantee finding the global optimum.
- Algorithms 1, 3, and 4 are susceptible to getting trapped in local optima; Algorithm 5 mitigates but does not eliminate this issue.
- The computational cost of r-flips still grows with r despite pruning, making exhaustive r-flip checks infeasible for larger problems.
- Derivative updates require O(nr) time and can become a computational bottleneck.
- Performance is sensitive to parameter tuning, including r-value, tabu tenure, M-threshold, probabilistic choices, and iteration counts.
- The correctness and efficiency of the method depend on precise implementation of derivative update rules; implementation errors can degrade performance.
- Algorithm efficacy varies with QUBO instance characteristics such as size, density, and coefficient distribution.
- Stopping criteria based on CPU time or lack of improvement may terminate the search prematurely.
- The pruning strategy assumes a good 1-flip local optimum is obtained before applying r-flip reductions.
- Experiments compare mainly against MST2/D-Wave tabu rather than a broader set of state-of-the-art classical QUBO solvers.
- The empirical evaluation is restricted to benchmark and synthetically generated QUBO instances rather than end-to-end real AQML or financial-service datasets.
- The study evaluates only r = 1 and r = 2 in the main large-scale comparisons, so conclusions may not generalize to larger r values.
- Runs were limited to 10 repetitions per instance, which constrains assessment of stochastic variability and robustness.
- Computational experiments were performed on classical CPU implementations rather than actual quantum annealing hardware, so hardware noise, embedding overhead, and device-specific constraints are not assessed.
- [inferred] No experiments on real quantum hardware means the paper does not validate whether the proposed warm-start/local-search benefits translate under qubit connectivity, noise, or annealing constraints.
- [inferred] No direct application to financial services tasks is demonstrated, limiting domain-specific external validity for finance use cases.
- [inferred] Reproducibility is only partial: instance data is shared, but full implementation details/code for all proposed algorithms are not clearly stated as publicly released.
- [inferred] Scalability to production AQML pipelines remains unproven because evaluation focuses on offline benchmark optimization under fixed CPU budgets.
## Open questions
- How well do the proposed r-flip heuristics perform when integrated into actual adiabatic quantum machine learning workflows such as quantum SVM, quantum k-means, and quantum feature selection?
- Do the observed gains over MST2 persist on real quantum annealers once hardware constraints, embedding, and noise are included?
- How does performance change for larger r values beyond 2, and is there a practical trade-off point where added search power no longer justifies computational cost?
- Which parameter settings are most robust across different QUBO sizes, densities, and coefficient distributions?
- How dependent is the success of the pruning strategy on the quality of the initial 1-flip local optimum?
- Can the method maintain its advantage on sparse versus dense QUBOs across a wider range of real-world problem structures?
- How would the algorithms compare against stronger modern classical baselines beyond MST2?
- What is the impact of different stopping criteria on solution quality and runtime stability?
- Can these heuristics scale effectively in production environments with larger, continuously updated optimization instances?
- [inferred] For financial services specifically, would the method improve practical tasks such as fraud detection, portfolio optimization, or credit risk modeling when mapped to QUBO?

**Future work:**
- Incorporate the r-flip technique into other local search strategies and solver frameworks.
- Use the proposed method as a warm-start local search component for quantum annealing solvers.
- Explore applications to very-large-scale problems and sparse-matrix QUBO formulations in AQML models such as quantum SVM, quantum k-means, and quantum feature selection.
- Investigate more effective implementations of strategic r-flip searches that further reduce computation time while preserving solution quality.
- Study broader parameter tuning strategies for r, tabu tenure, thresholds, and iteration schedules across different instance types.
- Evaluate the approach on a wider variety of QUBO instance classes with differing size, density, and coefficient structures.
- [inferred] Benchmark against additional state-of-the-art classical and hybrid solvers to better establish comparative performance.
- [inferred] Validate the approach on real quantum annealing hardware to assess practical benefits under hardware limitations.
- [inferred] Test the method on real application datasets, including financial services problems, rather than only benchmark/generated QUBOs.
- [inferred] Release full source code and experiment pipelines to improve reproducibility and facilitate independent validation.
## Key ideas
- #idea:hybrid-approach — Proposes classical r-flip and tabu-search hybrids as warm-start or companion optimizers for QUBO-based adiabatic quantum machine learning workflows.
- #idea:near-term-feasibility — Shows that large dense QUBO instances up to 30,000 variables can be handled effectively on classical CPU hardware using pruning after 1-flip local optimality.
- #idea:near-term-feasibility — Provides statistically significant evidence that Algorithm 5 outperforms the MST2 tabu-search baseline under fixed CPU budgets on benchmark QUBO instances.
## Contradictions
- The paper implicitly contradicts broad quantum-superiority narratives by showing that improved classical heuristics substantially outperform MST2, a classical tabu-search core associated with quantum annealing workflows, on large QUBO benchmarks.
- The paper challenges scalability claims sometimes made in AQML or annealing-motivated literature by demonstrating efficient classical solution of dense QUBOs up to 30,000 variables on a single CPU core, without quantum hardware.
- Any suggestion that the work evidences quantum advantage is contradicted by the study design itself: all experiments are classical, with no QPU execution or direct quantum-versus-classical comparison.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
