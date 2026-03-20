---
aliases:
- Train-and-Scaling the Quantum Alternating Operator Ansatz to Solve Portfolio Diversification
- Train Scaling Quantum Alternating
authors:
- Hannes Leipold
- Sarvagya Upadhyay
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1109/QCE60285.2024.10266
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2024 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_Marshall_QuantumAnnealingPortfolio
- 2022_Herman_QAOALimits
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T23:58:56.578497'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:59:58.385432'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:00:08.885223'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:00:15.539646'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:00:20.942045'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:01:02.704950'
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
- method/QAOA
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Train-and-Scaling the Quantum Alternating Operator Ansatz to Solve Portfolio
  Diversification
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces the Train-and-Scale method, a technique for optimizing quantum circuits to solve the portfolio diversification problem using the Quantum Alternating Operator Ansatz (QAOA). The approach addresses challenges in training high-depth quantum circuits by iteratively scaling both circuit depth and problem instance size, leveraging warm-start parameters from smaller instances. The method is tested on real-world financial data (S&P 500 stocks), demonstrating its ability to maintain high solution quality with modest increases in circuit depth and sampling complexity.
## Methodology
The paper presents an empirical study introducing the 'Train-and-Scale' method for optimizing the Quantum Alternating Operator Ansatz (QAOA) to solve the Portfolio Diversification problem, framed as a Maximum Independent Set (MIS) problem. The methodology involves iteratively training QAOA on progressively larger problem instances while scaling the circuit depth. The process begins with small instances (n=6) and low-depth circuits (p=6), then incrementally increases the instance size and circuit depth, using parameters from smaller instances as warm starts for larger ones. The QAOA circuit is trained using a hybrid quantum-classical approach with gradient-based optimization via the parameter shift rule. The study benchmarks the approach on historical S&P 500 stock price data, generating covariance graphs and solving the MIS problem for subgraphs of sizes ranging from 6 to 30 assets. The evaluation focuses on approximation ratio, sampling complexity, and scalability of the QAOA circuit depth.

**Algorithms used:** QAOA, Quantum Alternating Operator Ansatz

**Experimental setup:** The experiments were conducted using classical simulation of quantum circuits. The QAOA circuits were trained on subgraph instances derived from S&P 500 historical data, with problem sizes ranging from 6 to 30 assets. The training utilized finite difference gradient updates based on the parameter shift rule, with learning rate decay over 64 epochs.

**Dataset:** Historical daily price data for S&P 500 stocks from 2010 to 2020, obtained from Kaggle. The dataset includes 350 to 500 stocks per month after cleaning, with survivorship bias present.
## Findings
- [supported] The Train-and-Scale method achieves high average quality solutions for the Portfolio Diversification problem (approximation ratio below 0.4) with modest increases in QAOA p-depth (p=54 for n=30) on SP500-derived instances
- [supported] The method demonstrates linear growth in p-depth (p = O(n)) maintains high-quality approximation ratios and modest sampling complexity increases for problem sizes up to n=30
- [supported] QAOA-54 trained on n=30 instances shows good transferability to larger instances (n=100), with a lower empirical scaling exponent (0.044) compared to simulated annealing (0.057)
- [supported] The Train-and-Scale approach reduces sampling complexity for finding optimal solutions, with success probabilities not falling below 2^-20 for n ≤ 30
- [speculative] The authors suggest that if polynomial scaling in depth and sampling complexity continues, QAOA could be useful for Portfolio Diversification on real datasets with hundreds of variables
- [speculative] The paper claims Train-and-Scale is a robust method for solving hard graph problems with hundreds of variables on intermediate-scale quantum systems in the near future
- [supported] The method outperforms simulated annealing in sampling complexity for λ=0.1 correlation graphs, as shown in Fig. 3(C)

**Results summary:** The paper introduces the Train-and-Scale method for QAOA, which iteratively increases circuit depth while scaling problem instance sizes. The approach was tested on the Portfolio Diversification problem (mapped to Maximum Independent Set) using SP500 data. Results demonstrate that linear growth in p-depth (p=54 for n=30) maintains high solution quality (approximation ratio <0.4) and modest sampling complexity. The method shows good transferability to larger instances (n=100) and outperforms simulated annealing in sampling efficiency. All results are from classical simulations, not real quantum hardware.

**Performance claims:**
- Approximation ratio below 0.4 for n=30 instances
- p-depth of 54 for n=30 problem size
- Sampling complexity scaling exponent of 0.044 (vs 0.057 for simulated annealing)
- Success probability not falling below 2^-20 for n ≤ 30
- Linear scaling of p-depth with problem size (p = O(n))
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage for larger problem sizes (hundreds of variables) based on polynomial scaling trends observed in simulations up to n=30. However, no empirical demonstration of quantum advantage is provided, and all results are from classical simulations rather than real quantum hardware.
## Limitations
- Experiments limited to problem instances of size n ≤ 30 due to classical simulation cost constraints [inferred]
- Results rely on synthetic subgraphs generated from SP500 data rather than full real-world graphs, limiting generalizability to actual market conditions
- Dataset exhibits survivorship bias (only stocks that existed between 2010-2020 are included), which may skew results
- Training uses finite difference gradient updates with parameter shift rule, which may not scale efficiently for larger problem sizes [inferred]
- The randomized algorithm for partitioning mixer terms (to reduce circuit depth) may not yield optimal groupings, potentially affecting performance
- Approximation gap results are reported only for λ ∈ {0.1, 0.2, 0.3, 0.4, 0.5}, leaving performance at other thresholds unexplored [inferred]
- No comparison with state-of-the-art classical optimization methods (e.g., advanced MIS solvers) to benchmark quantum advantage [inferred]
- Page-limit constraints of the conference paper may have restricted detailed discussion of noise resilience or hardware-specific challenges [inferred]
- Sampling complexity analysis assumes noiseless simulations; real quantum hardware noise could degrade performance [inferred]
- The Train-and-Scale method's scalability beyond n=100 is extrapolated from trends, not empirically validated
## Open questions
- Can the Train-and-Scale method maintain high approximation ratios for problem sizes beyond n=100, or will exponential sampling complexity emerge?
- How does the algorithm perform under realistic quantum hardware noise, and what noise mitigation techniques are most effective?
- What is the minimal p-depth required to achieve a target approximation ratio for larger instances (e.g., n=1000)?
- How does the choice of correlation threshold λ affect the trade-off between solution quality and computational cost?
- Can the method be adapted to other financial optimization problems (e.g., risk parity, option pricing) without significant modifications?
- What are the theoretical bounds on the scaling of p-depth with problem size for this approach?
- How does the performance of Train-and-Scale compare to other warm-starting techniques for QAOA?

**Future work:**
- Extend the Train-and-Scale method to larger problem instances (n > 100) and validate scalability trends empirically
- Test the approach on real quantum hardware to assess noise resilience and practical applicability
- Compare performance with state-of-the-art classical solvers (e.g., integer programming, simulated annealing) to quantify quantum advantage
- Explore adaptive strategies for dynamically adjusting p-depth and λ during training
- Investigate the impact of different initial states (beyond the all-zeros state) on solution quality and convergence
- Apply the method to other combinatorial optimization problems in finance (e.g., index tracking, arbitrage detection)
- Develop hybrid quantum-classical pipelines that integrate Train-and-Scale with classical post-processing techniques
- Study the effect of noise mitigation techniques (e.g., error mitigation, dynamical decoupling) on real hardware implementations
## Key ideas
- #idea:quantum-advantage — Train-and-Scale method achieves linear scaling in QAOA depth (p=O(n)) while maintaining high solution quality (approximation ratio <0.4) for portfolio diversification up to n=30
- #idea:near-term-feasibility — Demonstrates potential for NISQ-era applicability through warm-starting and iterative scaling, though limited to classical simulations
- #idea:hybrid-approach — Hybrid quantum-classical framework combines gradient-based optimization with classical preprocessing to mitigate barren plateaus and reduce qubit requirements
- #limitation:simulation-only — Results are based on classical simulations, with no empirical validation on real quantum hardware
- #limitation:qubit-count — Problem size limited to n=30 due to classical simulation constraints, insufficient for full-scale financial applications
- #limitation:noise — No noise mitigation techniques applied, limiting direct applicability to near-term quantum devices
## Contradictions
- #contradiction:scalability — Claims polynomial scaling potential for hundreds of variables, but results are limited to n=30 and lack empirical validation on real hardware. Contradicts papers like 2021_Marshall_QuantumAnnealingPortfolio (which shows annealing struggles beyond n=50) and 2022_Herman_QAOALimits (which questions QAOA scalability beyond n=20 without error correction).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Kaggle (publicly available S&P 500 stock market data)', 'size': '350-500 stocks per month, 2010-2020 time period', 'features': 'Daily returns computed as percentage price changes, covariance and correlation matrices derived from daily returns', 'preprocessing_steps': ['Daily returns calculated as rt_k = (price(at_k) - price(at-1_k)) / price(at-1_k)', 'Monthly average returns and covariance matrices computed', 'Pearson correlation coefficients calculated for asset pairs', 'Threshold λ applied to correlation matrix to generate unweighted graphs (λ ∈ {0.1, 0.2, 0.3, 0.4, 0.5})', 'Subgraphs of sizes n=6 to n=30 generated via breadth-first search from larger graphs'], 'number_of_instances': '500 subgraphs per size n for each λ threshold'}

### Process
['1. Start with QAOA-pmin (pmin=6) on smallest instance size (nmin=6).', '2. Train QAOA-p on dataset Dn_k (k=500 instances) using parameter shift rule for gradient estimation.', '3. Perform 130,000 finite difference gradient updates with learning rate decay from 0.02 to 0.002 over 64 epochs.', '4. For each new instance size n, generate dataset Dn_k via breadth-first search.', '5. Determine target depth ptarget (e.g., p + 2) and insert new layers in the middle of the circuit.', '6. Train the new layer while keeping other parameters fixed, then retrain the entire circuit.', '7. Repeat until p reaches ptarget, then increment n and repeat the process.', '8. Evaluate approximation gap and sampling complexity for each instance size and circuit depth.']

### Output
{'metrics_reported': ['Approximation ratio (gap between QAOA solution and optimal solution)', 'Sampling complexity (inverse of success probability to find the best solution)', 'Scaling of circuit depth (p) with problem size (n)'], 'comparison_baselines': ['Simulated annealing (constant temperature T=1) for sampling solutions', 'Classical simulation cost for different λ thresholds'], 'output_format': 'Approximation gap and sampling complexity plots for varying problem sizes and circuit depths, comparison of QAOA scaling with simulated annealing'}

### Parameters
- qubit_count: Equal to problem size n (6 to 30 qubits)
- circuit_depth: p-depth ranging from 6 to 54 (p=2n for n=30)
- shots: Not explicitly stated, but sampling complexity reported as inverse success probability
- optimizer: Finite difference gradient descent with parameter shift rule
- learning_rate: {'initial': 0.02, 'final': 0.002, 'decay': 'Exponential over 64 epochs'}
- shift_size: 0.01
- gradient_updates: 130000
- epochs: 64
- temperature_parameter: 1
- correlation_thresholds: [0.1, 0.2, 0.3, 0.4, 0.5]

### Hardware
Classical simulation of QAOA circuits (no real QPU used). Simulation details (e.g., simulator name, noise model) not specified.

### Reproducibility
Code availability not explicitly mentioned. Dataset is publicly available from Kaggle. Methodology details are sufficiently described for replication, including algorithm pseudocode, parameter choices, and training protocol. However, lack of explicit code or simulation environment details may hinder full reproducibility.
