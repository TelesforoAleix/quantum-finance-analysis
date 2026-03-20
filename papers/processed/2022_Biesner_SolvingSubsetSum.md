---
aliases:
- Solving Subset Sum Problems using Binary Optimization with Applications in Auditing
  and Financial Data Analysis
- Solving Subset Sum Problems
authors:
- David Biesner
- Rafet Sifa
- Christian Bauckhage
- Bernd Kliem
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.36227/techrxiv.18994160.v1
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: TechRxiv
methodology_tags:
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: not-yet-assessed
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T23:14:32.176251'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:14:35.061940'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:14:50.610633'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:15:34.374103'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:15:41.762803'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:15:45.712420'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/fraud-detection
- topic/regulatory-compliance
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
title: Solving Subset Sum Problems using Binary Optimization with Applications in
  Auditing and Financial Data Analysis
topic_tags:
- fraud-detection
- regulatory-compliance
year: 2022
zotero_key: ''
---

## Abstract summary
This preprint explores the application of quantum-inspired optimization techniques to solve the subset sum problem, a key challenge in automating financial auditing and data consistency checks. The authors reformulate the problem as a quadratic unconstrained binary optimization (QUBO) task and demonstrate how gradient descent on Hopfield networks can reliably find solutions for both synthetic and real-world financial datasets. The work also discusses potential extensions to specialized hardware and quantum algorithms for improved performance.
## Methodology
The paper addresses the subset sum problem in the context of automated auditing and financial data analysis by reformulating it as a Quadratic Unconstrained Binary Optimization (QUBO) problem. The authors employ gradient descent on Hopfield Networks to solve the QUBO problem, which is equivalent to the subset sum problem. The methodology involves converting the subset sum problem into a QUBO formulation, then using a Hopfield Network to perform gradient descent to find optimal binary vectors that minimize the QUBO energy function. The approach is evaluated on both artificial and real financial datasets, with experiments conducted using GPU-accelerated parallel optimization of multiple independent Hopfield networks.

**Algorithms used:** Hopfield Networks, QUBO

**Experimental setup:** Experiments were conducted using an NVIDIA A100 GPU to parallelize the optimization of multiple independent Hopfield networks. The algorithm was run for up to 1e+8 initializations in batches of 1e+4, with a maximum computation time of approximately 8 minutes per configuration.

**Dataset:** The study used both artificial and real financial data. Artificial data were uniformly sampled integers between specified bounds, while real data were parsed from a Deutsche Bank financial report containing 190 independent columns of financial performance indicators across multiple quarters and years.
## Findings
- [supported] Gradient descent on Hopfield Networks reliably finds solutions to the subset sum problem for both artificial and real financial data, including tables with up to 256 numbers and magnitudes up to 1e+6.
- [supported] The Hopfield algorithm successfully solved all subset sum problems in parsed financial documents (190 columns) with 100% accuracy under the given constraints.
- [supported] Computation time for the Hopfield algorithm scales more significantly with the magnitude of numbers (Xmax) than with the number of values (n) in the subset sum problem.
- [speculative] Specialized hardware (e.g., FPGAs) or quantum algorithms could further improve the efficiency of QUBO-solving for subset sum problems in auditing.
- [speculative] The algorithm is ready for deployment in smart auditing software to benefit auditors in daily work.

**Results summary:** The paper demonstrates that gradient descent on Hopfield Networks can effectively solve the subset sum problem, a critical task in automated auditing and financial data analysis. The algorithm was validated on both artificial datasets (with varying sizes and magnitudes) and real financial documents, achieving reliable solutions in all tested cases. While the approach shows promise for practical deployment, the authors suggest future work on specialized hardware and quantum computing to enhance performance. Results are based on simulations, with no empirical validation on quantum hardware.

**Performance claims:**
- 100% solution accuracy on 190 real financial document columns
- Mean computation time of 0.4s for n=16, Xmax=10k and 77.2s for n=32, Xmax=1M on artificial data
- Mean runs until solution: 1.0e+04 (assets table) to 8.0e+05 (consincome table) for real data
- 2 of 5 samples unsolved for n=256, Xmax=1e+6 within the maximum iteration limit
## Quantum advantage claim
**Classification:** speculative

The paper mentions quantum algorithms as a future outlook for QUBO-solving but provides no empirical or theoretical validation of quantum advantage. All results are from classical simulations of Hopfield Networks.
## Limitations
- Preprint lacks peer review, which may affect the validity and robustness of the findings [inferred]
- Experiments conducted using Hopfield networks on GPUs, not quantum hardware, limiting insights into quantum-specific performance [inferred]
- Algorithm tested only on synthetic and real financial data with specific configurations (e.g., up to 256 numbers), limiting generalizability to larger or more complex datasets [inferred]
- Real data experiments limited to a single financial report (Deutsche Bank Q4 2020), reducing external validity [inferred]
- No comparison with state-of-the-art classical solvers (e.g., dynamic programming or heuristic methods) to benchmark performance [inferred]
- Algorithm may not scale efficiently for problems with very large magnitudes (e.g., Xmax = 1e+6) or high-dimensional data (e.g., n = 256), as seen in incomplete solutions for some configurations
- Hopfield network convergence to global optima is not guaranteed; reliance on multiple random initializations may not be practical for real-time applications [inferred]
- No noise mitigation techniques discussed, which could be critical for quantum hardware implementations [inferred]
- Lack of discussion on the impact of decoherence or quantum error correction for quantum computing applications [inferred]
- Assumes subset sum problems in financial auditing can be fully reduced to QUBO formulations, ignoring potential structural complexities in real-world tables [inferred]
## Open questions
- How does the Hopfield network algorithm perform on larger datasets (e.g., n > 256) or with higher magnitudes (e.g., Xmax > 1e+6)?
- What is the trade-off between solution accuracy and computational time for real-world financial datasets with sparse or noisy data?
- Can the algorithm be adapted to handle multi-target subset sum problems (e.g., multiple sums in a single table column)?
- How would the algorithm perform on quantum hardware compared to classical GPU implementations?
- What are the implications of hardware noise (e.g., in quantum annealers) on the reliability of solutions?
- How does the algorithm compare to rule-based or hybrid approaches for financial table auditing?
- What are the limitations of QUBO formulations for subset sum problems in terms of problem size and solution uniqueness?

**Future work:**
- Investigate the application of specialized hardware (e.g., FPGAs) for QUBO-solving to improve efficiency
- Explore quantum computing applications, including testing on quantum annealers or gate-based quantum computers
- Extend the algorithm to multi-period or multi-table financial auditing scenarios
- Benchmark against classical solvers (e.g., dynamic programming, heuristic methods) to evaluate relative performance
- Deploy the algorithm in existing smart auditing software to assess real-world usability and impact
- Study the scalability of the algorithm for larger datasets and more complex financial documents
- Incorporate noise mitigation techniques for quantum hardware implementations
## Key ideas
- #idea:near-term-feasibility — Hopfield Networks with gradient descent reliably solve subset sum problems in financial auditing for small-to-medium datasets (n ≤ 128, Xmax ≤ 1M) with 100% accuracy on real financial data (Deutsche Bank reports).
- #idea:hybrid-approach — Future work suggests combining classical QUBO-solving with specialized hardware (FPGAs) or quantum algorithms for scalability, though no empirical validation is provided.
- #limitation:no-empirical-validation — Quantum advantage claims are speculative; all results are derived from classical GPU simulations with no quantum hardware testing.
- #limitation:data-encoding — Performance scales poorly with number magnitude (Xmax), limiting applicability to financial datasets with very large or precise values (e.g., billions of euros).
- #limitation:simulation-only — No comparison with state-of-the-art classical solvers (e.g., dynamic programming) to benchmark performance, raising questions about relative advantage.
- #limitation:qubit-count — While not explicitly tested, the paper implies that quantum implementations would require sufficient qubits to handle large-scale subset sum problems, which are not currently available.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'artificial_data': {'source': 'Uniformly sampled integers', 'size': 'Configurations with n (number of integers) ranging from 16 to 256, and Xmax (magnitude of integers) ranging from 10,000 to 1,000,000', 'number_of_features': 'Single column of integers per problem', 'preprocessing_steps': 'Target sum T calculated as the sum of a randomly selected subset of k integers from the sampled set', 'configurations': [{'n': 16, 'k': 4, 'Xmax': [10000, 100000, 1000000]}, {'n': 32, 'k': 8, 'Xmax': [10000, 100000, 1000000]}, {'n': 64, 'k': 8, 'Xmax': [10000, 100000, 1000000]}, {'n': 128, 'k': 8, 'Xmax': [10000, 100000, 1000000]}, {'n': 256, 'k': 8, 'Xmax': [10000, 100000, 1000000]}]}, 'real_data': {'source': 'Deutsche Bank Financial Data Supplement Q4 2020', 'size': '190 independent columns across multiple tables (e.g., assets, consolidated income, liabilities, net revenues)', 'number_of_features': 'Columns with lengths ranging from 17 to 31 entries', 'preprocessing_steps': 'Columns parsed directly from financial reports; values ranged up to billions of euros with 14 significant figures', 'time_period': 'Q1 2019 to Q4 2020'}}

### Process
1. Convert the subset sum problem into a QUBO formulation using the derived weights and biases for the Hopfield Network. 2. Initialize the Hopfield Network state randomly (s ∈ {-1, 1}^n). 3. Perform gradient descent by updating single neurons based on the energy gradient until convergence. 4. Repeat the initialization and optimization process for up to 1e+8 runs or until a solution is found (energy E(s) = 0). 5. For GPU acceleration, multiple independent networks were optimized in parallel.

### Output
The algorithm outputs the subset of numbers that sum to the target value T, if found. Performance metrics include the mean time to solution (in seconds) and the mean number of runs until a solution is found. Results were compared across different configurations of artificial and real data.

### Parameters
- max_initializations: 100000000.0
- batch_size: 10000.0
- max_steps_per_run: Not explicitly stated, but convergence determined by energy stabilization
- energy_convergence_threshold: 0
- gpu_acceleration: NVIDIA A100

### Hardware
{'gpu': 'NVIDIA A100', 'parallelization': 'Multiple independent Hopfield networks optimized in parallel'}

### Reproducibility
The paper provides detailed algorithmic steps (Algorithm 1) and dataset configurations (Tables I and II). The real dataset is publicly available via a provided link. However, no explicit mention of code availability is made. The methodology is described in sufficient detail to replicate the experiments, assuming access to similar GPU hardware.
