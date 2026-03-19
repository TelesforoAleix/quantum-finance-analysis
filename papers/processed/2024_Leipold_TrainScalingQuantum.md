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
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T22:17:21.692856'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:17:24.111101'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:17:31.098656'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:17:59.328056'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:18:08.946103'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:19:05.375133'
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
This paper introduces the Train-and-Scale method, a technique for optimizing quantum circuits to solve the Portfolio Diversification problem using the Quantum Alternating Operator Ansatz (QAOA). The approach addresses challenges in training high-depth quantum circuits by iteratively scaling circuit depth alongside problem instance size, leveraging warm-start parameters from smaller instances. The method is tested on Maximum Independent Set formulations of portfolio diversification for S&P 500 assets, demonstrating its potential to maintain solution quality while managing computational complexity.
## Methodology
The paper presents an empirical study introducing the 'Train-and-Scale' method for optimizing the Quantum Alternating Operator Ansatz (QAOA) to solve the Portfolio Diversification problem, formulated as a Maximum Independent Set (MIS) problem. The methodology involves a hybrid quantum-classical approach where QAOA parameters are initially trained on smaller problem instances (subgraphs of size 6) and progressively scaled up to larger instances (up to size 30) by incrementally increasing the circuit depth (p-depth). The training process uses gradient-based optimization with the parameter shift rule to minimize the energy of the cost Hamiltonian. The approach leverages warm-starting parameters from smaller instances to initialize training for larger instances, thereby mitigating the barren plateau problem in variational quantum algorithms. The study benchmarks the method using historical stock price data from the S&P 500 (2010-2020), generating covariance graphs with varying correlation thresholds to test the algorithm's performance on different problem complexities.

**Algorithms used:** QAOA, Quantum Alternating Operator Ansatz

**Experimental setup:** The experiments were conducted using a quantum simulator (no specific hardware mentioned). The QAOA circuit depth (p) was scaled from p=6 for n=6 to p=54 for n=30. Training involved 130,000 finite difference gradient updates using the parameter shift rule, with learning rates decaying exponentially from 0.02 to 0.002 over 64 epochs. The study utilized classical simulation to evaluate the approximation ratio and sampling complexity of the QAOA solutions.

**Dataset:** Historical daily price data for S&P 500 stocks (2010-2020) obtained from Kaggle. The dataset was cleaned to include 350-500 stocks per month. Covariance matrices were computed from daily returns, and unweighted graphs were generated using correlation thresholds (λ ∈ {0.1, 0.2, 0.3, 0.4, 0.5}). Subgraphs of sizes n=6 to n=30 were generated via breadth-first search for training and evaluation.
## Findings
- [supported] The Train-and-Scale method achieves high average quality solutions for the Portfolio Diversification problem (approximation ratio below 0.4) with modest increases in QAOA p-depth (p=54 for n=30) on SP500-derived instances
- [supported] The method demonstrates linear growth in p-depth (p = O(n)) maintains high-quality approximation ratios and modest sampling complexity increases for problem sizes up to n=30
- [supported] QAOA-54 trained on n=30 instances shows good transferability to larger instances (n=100), with lower empirical scaling exponent (0.044) compared to simulated annealing (0.057)
- [supported] The Train-and-Scale approach successfully mitigates vanishing gradient issues in deeper QAOA circuits by iteratively scaling depth and instance size with warm-starting
- [speculative] The authors suggest polynomial scaling in depth and sampling complexity may continue for problem instances with hundreds of variables, enabling practical Portfolio Diversification on real datasets
- [speculative] The paper claims this is the largest size instance scaling reported for QAOA-p to date (n=30, p=54) on hard optimization problems

**Results summary:** The paper introduces the Train-and-Scale method for QAOA, which iteratively increases circuit depth while scaling up problem instance sizes to solve the Portfolio Diversification problem (mapped to Maximum Independent Set). Using SP500 data, the authors demonstrate that linear growth in p-depth (p=54 for n=30) maintains high solution quality (approximation ratio <0.4) and modest sampling complexity. The method shows better scaling than simulated annealing and good transferability to larger instances (n=100). Results are based on classical simulations, with no real hardware validation.

**Performance claims:**
- Approximation ratio below 0.4 for n=30 instances
- p-depth of 54 for n=30 problem size
- Sampling complexity scaling exponent of 0.044 (vs 0.057 for simulated annealing)
- Median success probability maintained across n=6 to n=30 instances
- Linear growth in p-depth (p = O(n)) for maintained solution quality
## Quantum advantage claim
**Classification:** speculative

While the paper demonstrates promising scaling results on simulated QAOA, no quantum advantage is empirically demonstrated. The claimed potential for solving hundreds-variable problems remains theoretical and unvalidated on real quantum hardware. The advantage is suggested based on classical simulation performance relative to simulated annealing.
## Limitations
- Experiments limited to problem instances of size n ≤ 30 due to classical simulation cost constraints
- Results rely on synthetic subgraphs generated from SP500 data rather than full-scale real-world instances [inferred]
- Dataset exhibits survivorship bias (only stocks that survived between 2010 and 2020 are included)
- Training relies on finite difference gradient updates with a fixed learning rate decay schedule, which may not be optimal for all problem sizes [inferred]
- The randomized algorithm for partitioning mixer terms may not yield optimal groupings, potentially increasing circuit depth [inferred]
- No noise mitigation techniques were applied, limiting applicability to near-term noisy quantum hardware [inferred]
- Sampling complexity analysis assumes ideal quantum hardware without accounting for readout errors or gate infidelities [inferred]
- Conference paper page limits may have constrained detailed discussion of failure cases or edge conditions [inferred]
- The method's performance on non-graph-based financial optimization problems remains untested [inferred]
- No comparison with state-of-the-art classical solvers (e.g., simulated annealing beyond n=100) to benchmark quantum advantage [inferred]
## Open questions
- Can the observed polynomial scaling in depth and sampling complexity persist for problem instances with hundreds or thousands of variables?
- How does the Train-and-Scale method perform under realistic hardware noise conditions?
- What is the impact of different correlation thresholds (λ) on the algorithm's robustness across diverse market regimes?
- Can the method be generalized to other financial optimization problems beyond portfolio diversification?
- How sensitive are the results to the choice of initial learning rate and decay schedule?
- What are the theoretical bounds on the approximation ratio for larger problem sizes?
- How does the performance compare to other warm-starting techniques for QAOA?

**Future work:**
- Extend experiments to larger problem instances (n > 30) using quantum hardware
- Test the method on real quantum devices with noise mitigation techniques
- Apply Train-and-Scale to other combinatorial optimization problems in finance (e.g., option pricing, risk analysis)
- Investigate adaptive learning rate strategies for training QAOA parameters
- Explore hybrid quantum-classical approaches combining Train-and-Scale with classical optimization heuristics
- Develop theoretical guarantees for the approximation ratio scaling with problem size
- Benchmark against state-of-the-art classical solvers on large-scale real-world datasets
- Study the impact of different mixer Hamiltonians on the method's performance
- Implement and test the method on neutral-atom quantum processors for larger instances
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
