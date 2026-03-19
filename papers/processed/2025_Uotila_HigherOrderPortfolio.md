---
aliases:
- Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
- Higher Order Portfolio Optimization
authors:
- Valter Uotila
- Julia Ripatti
- Bo Zhao
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/QCE65121.2025.00244
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:49:01.879582'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:49:06.285848'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:49:14.069748'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:50:22.315431'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:50:36.064313'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:50:43.809215'
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
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum formulation for portfolio optimization that incorporates higher-order moments (skewness and kurtosis) to better model return distributions. Unlike classical approaches, which often assume normally distributed returns, this method translates the problem into a higher-order unconstrained binary optimization (HUBO) framework solvable via the Quantum Approximate Optimization Algorithm (QAOA). The study benchmarks the quantum approach against classical continuous-variable solutions with integer programming-based discretization, demonstrating that the HUBO formulation frequently yields superior portfolio allocations.
## Methodology
The paper presents an empirical study on higher-order portfolio optimization using the Quantum Approximate Optimization Algorithm (QAOA). The research develops a quantum formulation for portfolio optimization that incorporates higher-order moments (skewness and kurtosis), leading to a higher-order unconstrained binary optimization (HUBO) problem. The methodology involves encoding realistic integer variables and a capital-based budget constraint into the quantum framework. The study compares the quantum approach with classical continuous variable solutions discretized via integer programming. The experimental evaluation includes 100 randomly generated portfolio optimization problems using stock market data from the Dow Jones Industrial Average (DJIA). The QAOA performance is benchmarked against classical baselines, and the exact spectrum of the HUBO problems is computed for smaller instances (less than 14 qubits). The evaluation metrics focus on the normalized value of the cost function and budget utilization.

**Algorithms used:** QAOA
**Frameworks:** Qiskit, PennyLane, SciPy, CVXPY

**Experimental setup:** Experiments were conducted using quantum simulators, specifically targeting up to 15 qubits. The QAOA circuits were constructed and optimized using classical optimizers such as CMA-ES (Covariance Matrix Adaptation Evolution Strategy). The classical baseline solutions were obtained using Sequential Least Squares Programming (SLSQP) for continuous variable optimization and CVXPY for integer programming-based discretization. The exact solutions for smaller problems (6-13 qubits) were computed using standard eigenvalue solvers, while sparse eigenvalue solvers were used for 14-15 qubit problems.

**Dataset:** Stock market data from the Dow Jones Industrial Average (DJIA) spanning ten years (January 1, 2015, to January 1, 2025) was used. The dataset includes 30 large, publicly traded U.S. companies across various industries. Randomly sampled subsets of 2 to 10 companies were selected to create 100 portfolio optimization problems with budgets limited to $6000.
## Findings
- [supported] The paper develops the first quantum formulation for portfolio optimization with higher-order moments (skewness and kurtosis), enabling more realistic modeling of portfolio return distributions.
- [supported] Experimental evaluation of 100 portfolio optimization problems shows that the higher-order unconstrained binary optimization (HUBO) formulation often produces better portfolio allocations than the classical continuous variable formulation with integer programming-based discretization.
- [supported] The HUBO formulation demonstrates potential for encoding portfolio allocations that outperform classical baselines, as shown in Table II and Figure 6, motivating further research into quantum methods for higher-order optimization.
- [supported] QAOA performance on HUBO problems is benchmarked, with results indicating challenges in matching the solution quality of exact methods or classical algorithms, particularly as qubit counts increase (6-15 qubits tested).
- [supported] The average QAOA enhancement factor is 14.43x, meaning the probability of measuring the optimal state is significantly higher than random sampling, though performance varies widely (3.79x to 108.94x).
- [supported] Higher-order portfolio optimization (HUBO) produces more diverse portfolios compared to mean-variance (QUBO) formulations, as measured by KL divergence from uniform allocations (Figure 5b).
- [speculative] Quantum advantage may emerge for HUBO problems due to classical solvers' limitations in handling higher-order terms, though current hardware constraints limit practical demonstration.
- [speculative] The rugged optimization landscape of HUBO problems, with many local minima (Figure 5c), suggests that modified QAOA strategies (e.g., tensor networks, Bayesian optimizers) could improve performance.
- [supported] The capital-based budget constraint and integer variable encoding in the quantum formulation align more closely with real-world portfolio optimization requirements than prior quantum approaches (Table I).
- [disputed] The paper claims that higher-order moments (skewness/kurtosis) are necessary due to non-normal return distributions (Figure 3), but this is debated in finance literature where mean-variance models remain dominant for practical applications.

**Results summary:** The paper introduces a quantum formulation for portfolio optimization incorporating higher-order moments (skewness and kurtosis) via a higher-order unconstrained binary optimization (HUBO) approach. Experimental results on 100 problem instances demonstrate that the HUBO formulation frequently outperforms classical continuous variable methods in solution quality, though QAOA struggles to match exact or classical baselines as problem size grows. The study highlights the potential of quantum methods for more realistic portfolio modeling but identifies optimization challenges, including rugged landscapes and scalability limitations. Comparative analysis shows HUBO produces more diversified portfolios than QUBO (mean-variance) formulations, and the quantum approach achieves a 14.43x average enhancement in measuring optimal states over random sampling.

**Performance claims:**
- HUBO formulation outperforms classical baselines in 53% of cases (min-max normalized objective ≥ 0.95) for budget utilization between 95-105% (Table II).
- QAOA achieves an average 14.43x enhancement factor in measuring optimal states compared to random sampling.
- HUBO solutions maintain closer proximity to uniform allocations (lower KL divergence) than QUBO, indicating greater portfolio diversification (Figure 5b).
- QAOA performance degrades with increasing qubit counts (6-15 qubits tested), with only 3-23% of cases matching exact solutions (Table II).
- Optimal λ values for budget constraint penalization in QAOA are typically >1, with higher values improving performance.
## Quantum advantage claim
**Classification:** speculative

The paper suggests theoretical potential for quantum advantage in solving HUBO-based portfolio optimization due to classical methods' exponential complexity with higher-order terms. However, all results are from simulations, and the claimed advantage is not demonstrated on real hardware. Performance gaps between QAOA and exact/classical methods further temper the speculation.
## Limitations
- Experiments limited to 15 qubits due to simulator resource constraints [inferred]
- No testing on real quantum hardware, only simulations were performed
- QAOA performance degrades as the number of qubits increases, indicating scalability challenges
- Budget constraint encoding does not strictly prevent over-investment, only penalizes it equally with under-investment
- Higher-order terms (skewness and kurtosis) have small impact on the spectrum for small qubit counts (10^-9 to 10^-11 difference from QUBO)
- Optimal λ parameter for budget constraint penalty varies across problem instances and requires manual tuning
- Classical optimizers used in QAOA subroutine may not be optimal for higher-order optimization landscapes
- No noise mitigation techniques were applied, which may affect results on real hardware [inferred]
- Page-limit constraints likely prevented deeper analysis of optimization landscapes and parameter sensitivity [inferred]
- Dataset limited to Dow Jones Industrial Average stocks, which may not represent broader market diversity [inferred]
- No comparison with state-of-the-art classical HUBO solvers beyond basic integer programming approaches
- QAOA enhancement factor varies significantly (3.79x to 108.94x), indicating inconsistent performance across problem instances
## Open questions
- How does QAOA perform on higher-order portfolio optimization problems with more than 15 qubits?
- What is the impact of quantum hardware noise on the solution quality for this HUBO formulation?
- Can alternative quantum algorithms (e.g., digitized counterdiabatic approaches) better handle the complex optimization landscapes of HUBO problems?
- How sensitive is the solution quality to the choice of risk aversion parameters (q0, q1, q2)?
- What is the minimum qubit count required for quantum advantage in higher-order portfolio optimization?
- How does the performance compare between capital-based and asset-based budget constraints in quantum formulations?
- What is the relationship between the spectral properties of HUBO problems and QAOA trainability?
- Can hybrid quantum-classical approaches (e.g., tensor networks) improve solution quality for larger problem instances?
- How do different classical optimizers affect QAOA's performance on HUBO problems beyond the CMA-ES results shown?
- What is the impact of different variable encoding schemes on solution quality and circuit depth?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., IBM Eagle processor)
- Develop and evaluate noise mitigation techniques for HUBO problems on NISQ devices
- Explore alternative quantum algorithms for higher-order optimization (e.g., bias-field digitized counterdiabatic approaches)
- Investigate tensor network methods for improving QAOA performance on HUBO problems
- Extend the evaluation to larger problem sizes (beyond 15 qubits) using more efficient simulators or quantum hardware
- Develop automated methods for selecting optimal λ parameters for budget constraints
- Compare performance with state-of-the-art classical HUBO solvers
- Explore Bayesian optimization for QAOA parameter tuning in HUBO problems
- Investigate the impact of different risk aversion parameter settings on portfolio diversity and solution quality
- Apply the higher-order formulation to other financial optimization problems beyond portfolio optimization
- Develop methods to strictly enforce budget constraints in quantum formulations without excessive qubit overhead
- Study the relationship between portfolio diversification and higher-order moments in quantum formulations
## Key ideas
- #idea:quantum-advantage — First quantum formulation for portfolio optimization incorporating higher-order moments (skewness/kurtosis) via HUBO, outperforming classical continuous variable approaches in solution quality for 100 instances
- #idea:near-term-feasibility — Demonstrates QAOA's applicability to higher-order portfolio optimization on simulated hardware, though scalability to larger asset universes remains untested
- #idea:hybrid-approach — Implicit hybrid approach through classical preprocessing (integer programming discretization) and quantum HUBO formulation, suggesting a practical path for near-term deployment
- #limitation:simulation-only — All results derived from classical simulation of QAOA, with no empirical validation on real quantum hardware
- #limitation:qubit-count — Integer variable encoding introduces logarithmic qubit overhead, potentially limiting problem size on near-term devices
- #limitation:noise — Potential noise and decoherence effects not accounted for due to simulation-only experiments
- #limitation:data-encoding — Logarithmic overhead in qubit requirements for integer-to-binary variable encoding limits practical applicability
- #contradiction:scalability — QAOA performance degrades with increasing qubit counts (6-15 qubits), with only 3-23% of cases matching exact solutions, contradicting claims of scalability
- #contradiction:classical-vs-quantum — The necessity of higher-order moments (skewness/kurtosis) is disputed in finance literature, where mean-variance models remain dominant for practical applications
## Contradictions
- The paper claims superiority of HUBO-based portfolio optimization over classical methods, but QAOA performance degrades with increasing qubit counts (6-15 qubits), with only 3-23% of cases matching exact solutions, undermining scalability claims.
- The paper argues that higher-order moments (skewness/kurtosis) are necessary due to non-normal return distributions, but this is debated in finance literature where mean-variance (QUBO) models remain widely used for practical applications.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
