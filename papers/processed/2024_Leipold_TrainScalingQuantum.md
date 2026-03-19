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
step1_date: '2026-03-19T12:58:43.110103'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:58:47.448720'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:58:57.221432'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:00:10.904426'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:00:28.650245'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:00:36.650307'
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
This paper introduces the Train-and-Scale method, a technique for optimizing quantum circuits to solve the portfolio diversification problem using the Quantum Alternating Operator Ansatz (QAOA). The approach addresses challenges in training high-depth quantum circuits by iteratively scaling both circuit depth and problem instance size, starting from smaller subproblems. The method is tested on real-world financial data (S&P 500 stocks), demonstrating its ability to maintain high solution quality while managing computational complexity as problem size increases.
## Methodology
The paper presents an empirical study introducing the 'Train-and-Scale' method for optimizing the Quantum Alternating Operator Ansatz (QAOA) to solve the Portfolio Diversification problem, formulated as a Maximum Independent Set (MIS) problem. The methodology involves a hybrid quantum-classical approach where QAOA parameters are initially trained on smaller problem instances (subgraphs of size 6) and progressively scaled up to larger instances (up to size 30) by incrementally increasing the circuit depth (p-depth). The training process uses gradient-based optimization with the parameter shift rule to minimize the energy of the cost Hamiltonian. The approach leverages warm-starting parameters from smaller instances to efficiently train larger circuits, aiming to mitigate issues like vanishing gradients (Barren Plateaus) in deeper circuits. The study benchmarks the method using historical stock price data from the S&P 500, generating covariance graphs and thresholding them to create unweighted graphs for MIS problem instances.

**Algorithms used:** QAOA, Quantum Alternating Operator Ansatz

**Experimental setup:** The experiments were conducted using a quantum-classical hybrid framework, where the quantum component was simulated classically. The QAOA circuits were trained using finite difference gradient updates based on the parameter shift rule, with learning rates decaying exponentially over 64 epochs. The training involved 130,000 gradient updates per instance size. The study utilized subgraphs generated from S&P 500 covariance data, with instance sizes ranging from 6 to 30 nodes and circuit depths scaling linearly with instance size (e.g., p=54 for n=30).

**Dataset:** Historical daily price data for S&P 500 stocks from 2010 to 2020, obtained from Kaggle. The dataset was cleaned to include 350-500 stocks per month. Daily returns and Pearson correlation coefficients were computed to generate covariance matrices, which were thresholded to create unweighted graphs for the Maximum Independent Set problem. Subgraphs of sizes 6 to 30 were generated via breadth-first search for training and evaluation.
## Findings
- [supported] The Train-and-Scale method achieves high average quality solutions for the Portfolio Diversification problem (approximation ratio below 0.4) with modest increases in QAOA circuit depth (p=54 for n=30) on SP500-derived instances.
- [supported] The method demonstrates linear growth in p-depth maintains high approximation ratios and modest sampling complexity increases for problem sizes up to n=30.
- [supported] QAOA with Train-and-Scale shows lower empirical scaling exponent (0.044) compared to simulated annealing (0.057) for sampling complexity on instances up to n=100.
- [supported] The approach successfully transfers learned parameters from smaller (n=6) to larger (n=30) instances, showing good transferability of QAOA-54 solutions.
- [speculative] The authors suggest that if polynomial scaling in depth and sampling complexity continues, QAOA could be useful for Portfolio Diversification on real datasets with hundreds of variables.
- [speculative] The paper claims Train-and-Scale is a robust method for solving hard graph problems with hundreds of variables on near-term quantum systems.
- [supported] The method avoids vanishing sampling probabilities (e.g., never below 2^-20) for the tested size range (n ≤ 30).

**Results summary:** The paper introduces the Train-and-Scale method for QAOA, which iteratively increases circuit depth while scaling problem size to solve the Portfolio Diversification problem (mapped to Maximum Independent Set). Empirical results on SP500 data show the method achieves high-quality solutions (approximation ratio < 0.4) with modest depth increases (p=54 for n=30). The approach demonstrates polynomial scaling in sampling complexity and outperforms simulated annealing in empirical scaling. Results are based on classical simulations, with no real hardware validation. The method shows promise for scaling to larger instances, though quantum advantage remains unproven.

**Performance claims:**
- Approximation ratio below 0.4 for n=30 instances
- p-depth of 54 for n=30 instances
- Sampling complexity scaling exponent of 0.044 (vs. 0.057 for simulated annealing)
- Median success probability maintained across n=6 to n=100 for λ=0.1
- 217 gradient updates (≈130,000) per training iteration
## Quantum advantage claim
**Classification:** speculative

The paper claims potential usefulness for hundreds of variables based on polynomial scaling trends observed in simulations (n ≤ 100). However, quantum advantage is not demonstrated on real hardware, and all results are from classical simulations of QAOA.
## Limitations
- Experiments limited to problem instances of size n ≤ 30 due to classical simulation cost constraints [inferred]
- Training and testing performed on subgraphs generated from SP500 data, which may not generalize to other financial datasets or asset classes [inferred]
- Dataset exhibits survivorship bias, as noted in the paper (only stocks that existed throughout 2010-2020 are included)
- Results rely on classical simulation of quantum circuits; performance on real quantum hardware may differ due to noise and decoherence [inferred]
- The Train-and-Scale method assumes smooth parameter transferability across instance sizes, which may not hold for all problem types [inferred]
- Sampling complexity analysis limited to λ = 0.1; performance for other λ values (e.g., higher thresholds) may vary [inferred]
- No comparison with state-of-the-art classical optimization methods (e.g., advanced heuristics or exact solvers) for the Portfolio Diversification problem [inferred]
- Page-limit constraints of the conference paper may have limited the depth of methodological or experimental details [inferred]
- The randomized algorithm for partitioning mixer terms may not always find optimal partitions, potentially affecting circuit efficiency [inferred]
- Training relies on finite difference gradient updates with a fixed learning rate schedule, which may not be optimal for all problem instances [inferred]
## Open questions
- How does the Train-and-Scale method perform for problem instances with n > 30, particularly in the range of hundreds of variables?
- What is the impact of hardware noise on the Train-and-Scale method when executed on real quantum devices?
- Can the observed polynomial scaling in depth and sampling complexity be theoretically proven or is it an empirical artifact of the tested instances?
- How does the method compare to classical solvers (e.g., simulated annealing, genetic algorithms) in terms of solution quality and runtime for large-scale problems?
- What is the robustness of the method to different types of financial datasets (e.g., cryptocurrencies, bonds, or international markets)?
- How sensitive is the method to the choice of correlation threshold λ, and can it adapt dynamically to varying λ values?
- What are the limits of parameter transferability across instance sizes, and how can these be improved?

**Future work:**
- Test the Train-and-Scale method on real quantum hardware to validate performance under noise and decoherence
- Extend the method to larger problem instances (n > 100) to assess scalability
- Compare the method with state-of-the-art classical optimization techniques for the Portfolio Diversification problem
- Explore adaptive strategies for dynamically adjusting circuit depth and training parameters based on problem complexity
- Investigate the method's applicability to other financial optimization problems (e.g., risk parity, asset-liability management)
- Develop noise mitigation techniques tailored to the Train-and-Scale approach for real-world deployment
- Study the impact of different initial states (beyond the all-zeros state) on solution quality and training efficiency
- Extend the method to multi-period or dynamic portfolio optimization problems
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
