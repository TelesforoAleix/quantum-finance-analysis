---
aliases:
- 'Extrapolation method to optimize linear-ramp quantum approximate optimization algorithm
  parameters: Evaluation of runtime scaling'
- Extrapolation method optimize linear
authors:
- Vanessa Dehn
- Martin Zaefferer
- Gerhard Hellstern
- Karthik Jayadevan
- Florentin Reiter
- Thomas Wellens
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/l5r4-zcqv
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review A
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-20T00:52:23.235433'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:53:19.099759'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:54:30.392349'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:54:40.316851'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:54:49.684220'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:54:57.623924'
step6_model: Mistral-Large-3
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
- topic/fraud-detection
- topic/credit-scoring
- method/QAOA
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Extrapolation method to optimize linear-ramp quantum approximate optimization
  algorithm parameters: Evaluation of runtime scaling'
topic_tags:
- portfolio-optimisation
- risk-modelling
- fraud-detection
- credit-scoring
year: 2026
zotero_key: ''
---

## Abstract summary
This paper introduces an extrapolation method to optimize parameters for the linear-ramp quantum approximate optimization algorithm (QAOA), aiming to address the bottleneck of parameter optimization in standard QAOA. The authors propose estimating suitable QAOA parameters by extrapolating from smaller to larger problem sizes, focusing on combinatorial optimization problems such as portfolio optimization, feature selection, clustering, and weighted MaxCut. The study evaluates quantum runtime scaling using a noiseless quantum emulator and compares it with classical methods, demonstrating potential quantum scaling advantages in portfolio optimization.
## Methodology
The paper presents an empirical study evaluating the runtime scaling of the linear-ramp Quantum Approximate Optimization Algorithm (QAOA) for solving combinatorial optimization problems in financial services, specifically portfolio optimization, feature selection, clustering, and weighted MaxCut. The research design involves comparing quantum runtime scaling against classical optimization methods (CPLEX, GUROBI, MQLib/Burer2002, Goemans-Williamson). The quantum methodology employs a noiseless quantum emulator to simulate QAOA circuits with parameters optimized via an extrapolation method. This method reduces the original problem to smaller subproblems (4 to 10 qubits), performs grid searches to optimize QAOA parameters (Δγ, Δβ, and depth p), and extrapolates these parameters to larger problem sizes (up to 28 qubits). The quantum runtime is quantified as the total circuit depth (D), defined as the depth of a single QAOA circuit multiplied by the number of shots required to find the optimal solution. Classical runtime scaling is benchmarked using MQLib/Burer2002 due to its consistent scaling behavior and low absolute runtime values.

**Algorithms used:** QAOA

**Experimental setup:** Experiments were conducted using a noiseless quantum emulator to simulate QAOA circuits. The emulator was used to evaluate the probability of measuring the optimal solution (P_opt) for various problem sizes (N = 12 to 28 qubits). The experimental setup involved generating random instances of each combinatorial optimization problem, optimizing QAOA parameters via extrapolation from smaller subproblems, and comparing quantum runtime scaling with classical methods.

**Dataset:** Four combinatorial optimization problems were addressed: (1) Portfolio optimization using annualized returns and covariance matrices for the German DAX 30 (2016-2020), (2) Feature selection using the 'German Credit Data' dataset with 20 features (7 numerical, 13 categorical), (3) Clustering using 'Moons' and 'Blobs' datasets from SCIKIT-LEARN with two features, and (4) Weighted MaxCut problems with edge weights randomly drawn from a uniform discrete distribution between 0 and 1000.
## Findings
- [supported] The linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323
- [supported] For portfolio optimization, the quantum runtime (total circuit depth D) scales as 2^0.219N, while the classical runtime scales as 2^0.323N, indicating a potential quantum scaling advantage [supported]
- [supported] The extrapolation method for LR-QAOA parameters (Δγ, Δβ, p) from smaller subproblems (4-10 qubits) to larger problems (up to 28 qubits) yields results close to direct optimization minima, validating the approach [supported]
- [supported] Universal parameter scaling (algebraic fits for Δγ, Δβ, p across instances) reduces outliers and improves runtime scaling for feature selection, clustering, and MaxCut problems, achieving near-parity with classical benchmarks [supported]
- [supported] The probability of measuring the optimal solution (P_opt) remains above 0.1 on average for all problem classes, with portfolio optimization and MaxCut showing near-constant or slightly increasing P_opt with problem size [supported]
- [speculative] The authors suggest that combining their extrapolation method with other fixed-parameter QAOA schedules (e.g., Fourier heuristic, Trotterized quantum annealing) could further improve runtime scaling [speculative]
- [disputed] The claimed quantum scaling advantage for portfolio optimization contradicts broader literature where quantum advantage for QAOA remains unproven beyond small-scale simulations [disputed]

**Results summary:** The paper presents an extrapolation-based method to optimize linear-ramp QAOA parameters for combinatorial optimization problems in financial services (portfolio optimization, feature selection, clustering, and MaxCut). Using noiseless quantum emulation, the authors demonstrate that LR-QAOA achieves superior runtime scaling (2^0.219N) compared to classical MQLib/Burer2002 (2^0.323N) for portfolio optimization up to 28 qubits. The extrapolation method, which derives parameters for large problems from smaller subproblems, is validated by close agreement with direct optimization results. For other problem classes, universal parameter scaling reduces outliers and improves scaling, though classical methods still outperform quantum approaches. The probability of measuring optimal solutions remains above 0.1 on average, with near-constant behavior for portfolio optimization and MaxCut.

**Performance claims:**
- Quantum runtime scaling exponent α = 0.219 for portfolio optimization (vs. classical α = 0.323)
- Total circuit depth D scales as 2^0.219N for quantum vs. 2^0.323N for classical in portfolio optimization
- Extrapolation method achieves results within 10% of direct optimization minima for portfolio optimization
- Universal parameter scaling reduces quantum runtime scaling exponents to α = 0.16-0.22 across problem classes
- Optimal solution probability P_opt > 0.1 maintained for all problem classes up to 28 qubits
## Quantum advantage claim
**Classification:** theoretical

The paper demonstrates a theoretical scaling advantage for LR-QAOA in portfolio optimization based on noiseless emulation results. The advantage is classified as 'theoretical' because: (1) results are from simulation, not real hardware; (2) the advantage is shown only for specific problem instances and sizes (up to 28 qubits); and (3) the extrapolation method's generalizability to larger scales remains unproven.
## Limitations
- Experiments conducted on a noiseless quantum emulator, not real quantum hardware, which may not account for hardware noise and decoherence [inferred]
- Limited to problem sizes up to 28 qubits, which may not fully demonstrate scalability to larger, real-world financial problems [inferred]
- Extrapolation method relies on algebraic scaling assumptions (linear behavior on a log-log scale) without theoretical justification [inferred]
- Use of synthetic or simplified datasets (e.g., DAX 30 data for portfolio optimization, Moons and Blobs datasets for clustering) may not reflect real-world complexity
- Classical benchmarks (e.g., MQLib/Burer2002) may not fully represent state-of-the-art classical solvers for all problem types [inferred]
- Outliers observed in clustering results suggest instability in the extrapolation method for certain problem instances
- No comparison with other quantum algorithms (e.g., QAOA variants, VQE) to assess relative performance [inferred]
- Reproducibility may be affected by random sampling of subinstances for extrapolation
- Quantum runtime expressed as total depth (D) assumes uniform gate times, which may not hold for all quantum hardware [inferred]
- Lack of noise mitigation techniques in the quantum simulations may overestimate performance on real hardware [inferred]
## Open questions
- Can the observed quantum scaling advantage for portfolio optimization be maintained or improved for larger problem sizes (N > 28)?
- What is the impact of hardware noise and decoherence on the performance of the linear-ramp QAOA for these financial use cases?
- How does the extrapolation method perform for problem instances with different structural properties (e.g., sparsity, constraint density)?
- Are there theoretical justifications for the algebraic scaling assumptions used in the extrapolation method?
- How does the quantum algorithm compare with other classical heuristics or hybrid quantum-classical approaches?
- What is the role of problem-specific characteristics (e.g., covariance matrix structure in portfolio optimization) in determining quantum advantage?
- Can the universal parameter scaling approach be generalized to other combinatorial optimization problems beyond the four use cases studied?
- How does the probability of measuring the optimal solution (P_opt) behave for problem sizes beyond N = 28?
- What are the implications of the observed polynomial scaling of median quantum runtime for the broader landscape of combinatorial optimization?

**Future work:**
- Extend the analysis to larger problem sizes (N > 28) using high-performance quantum simulators or fault-tolerant quantum hardware
- Test the linear-ramp QAOA on real quantum hardware to assess the impact of noise and decoherence
- Develop theoretical foundations for the algebraic scaling assumptions used in the extrapolation method
- Compare the performance of the linear-ramp QAOA with other quantum algorithms (e.g., standard QAOA, VQE) for financial use cases
- Investigate the use of noise mitigation techniques to improve performance on near-term quantum devices
- Explore hybrid quantum-classical approaches to leverage the strengths of both paradigms for financial optimization
- Conduct a more detailed statistical analysis of runtime scaling, including different percentiles beyond the median
- Apply the extrapolation method to a broader range of combinatorial optimization problems, including those with real-world financial datasets
- Study the impact of problem-specific characteristics (e.g., constraint types, data distributions) on quantum algorithm performance
- Develop methods to identify problem instances that are particularly amenable to quantum advantage
## Key ideas
- #idea:quantum-advantage — LR-QAOA with extrapolated parameters demonstrates superior runtime scaling (α = 0.219) compared to classical MQLib/Burer2002 (α = 0.323) for portfolio optimization up to 28 qubits in noiseless emulation
- #idea:near-term-feasibility — Extrapolation method reduces QAOA parameter optimization overhead by deriving parameters for larger problems from smaller subproblems (4-10 qubits), improving near-term applicability
- #idea:hybrid-approach — Linear-ramp QAOA schedule simplifies parameter optimization by reducing free parameters to two, enabling more efficient quantum-classical hybrid workflows
- #limitation:simulation-only — Quantum advantage claims are based on noiseless emulation, not real quantum hardware, limiting empirical validation
- #limitation:qubit-count — Problem sizes limited to 28 qubits, insufficient for real-world financial applications requiring larger asset universes
- #limitation:noise — No noise mitigation techniques applied, which could degrade performance on real quantum devices and invalidate scaling advantages
- #limitation:data-encoding — Extrapolation method relies on small subproblems (4-10 qubits) to predict parameters for larger problems, with untested generalization to real-world datasets
## Contradictions
- #contradiction:classical-vs-quantum — The claimed quantum scaling advantage for portfolio optimization contradicts broader literature where quantum advantage for QAOA remains unproven beyond small-scale simulations (e.g., disputed by [2022_Herman_QuantumAdvantageLimits])
- #contradiction:scalability — The extrapolation method's generalizability to larger problem sizes (N > 28) is unproven, and outliers in clustering results suggest instability for certain problem instances
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'portfolio_optimization': {'source': 'German DAX 30 (as of 1/2/2021)', 'time_period': '01/01/2016 to 31/12/2020', 'features': 'Annualized returns and covariance matrices for 30 assets', 'preprocessing': 'Random selection of N out of 30 assets, risk preference factor q set to 1, budget constraint B = N/2 (even N) or (N-1)/2 (odd N)', 'size': 'Problem sizes N = 12 to 28 qubits'}, 'feature_selection': {'source': "'German Credit Data' dataset", 'features': '20 features (7 numerical, 13 categorical), expanded to 48 binary features after one-hot encoding', 'preprocessing': 'One-hot encoding of categorical features, linear correlation (ρ_Correl) used as dependence measure, weighting parameter φ set to 0.9', 'size': 'Problem sizes N = 12 to 28 qubits'}, 'clustering': {'source': "'Moons' and 'Blobs' datasets from SCIKIT-LEARN", 'features': 'Two features per data point (x ∈ R²)', 'preprocessing': 'Euclidean distances computed for all data pairs, converted to QUBO formulation', 'size': 'Problem sizes N = 12 to 28 qubits'}, 'weighted_maxcut': {'source': 'Synthetic data', 'features': 'Edge weights randomly drawn from uniform discrete distribution (0 to 1000)', 'preprocessing': 'None specified beyond random weight generation', 'size': 'Problem sizes N = 12 to 28 qubits'}}

### Process
1. Problem instances of size N (12 to 28 qubits) were generated for each optimization problem. 2. For each instance, 10 random subinstances of sizes 4, 6, 8, and 10 qubits were created. 3. Grid searches were performed on subinstances to optimize QAOA parameters (Δγ, Δβ, and p) using a multivariate skew Gaussian fit. 4. Optimized parameters were extrapolated to the original problem size N. 5. The QAOA depth p was optimized by minimizing the total depth D (circuit depth × number of shots). 6. Quantum runtime (total depth D) was computed using a noiseless emulator and compared against classical runtime scaling.

### Output
{'metrics_reported': ['Total depth D (quantum runtime)', 'Probability of measuring optimal solution (P_opt)', 'Scaling exponent α for runtime (D ∝ 2^αN)'], 'baseline_comparisons': ['Classical optimization methods: CPLEX, GUROBI, MQLib/Burer2002, Goemans-Williamson'], 'output_format': 'Exponential fits of runtime scaling (quantum vs. classical), visualizations of parameter optimization (Δγ, Δβ, p), and probability distributions of optimal solutions.'}

### Parameters
- qubit_count: 4 to 28 qubits (subproblems: 4, 6, 8, 10 qubits; full problems: 12 to 28 qubits)
- circuit_depth: Proportional to QAOA depth p, optimized per instance (range: 1 to ~600)
- shots: Median number of shots derived from P_opt (log(1/2)/log(1-P_opt))
- optimizer: Grid search with multivariate skew Gaussian fit for parameter optimization
- hyperparameters: {'Δγ': 'Linear-ramp parameter for cost unitary, optimized via extrapolation', 'Δβ': 'Linear-ramp parameter for mixer unitary, optimized via extrapolation', 'p': 'QAOA depth, optimized to minimize total depth D', 'risk_preference_factor_q': 'Set to 1 for portfolio optimization (focus on risk minimization)', 'weighting_parameter_φ': 'Set to 0.9 for feature selection'}

### Hardware
{'simulator': 'Noiseless quantum emulator (specific emulator name not provided)', 'transpilation_settings': 'Not explicitly mentioned, assumed idealized conditions'}

### Reproducibility
Data for portfolio optimization (DAX 30) and feature selection ('German Credit Data') are publicly available. Code and datasets for reproducibility are referenced as openly available (see Data Availability statement). The methodology provides sufficient detail for replication, including parameter optimization and extrapolation procedures.
