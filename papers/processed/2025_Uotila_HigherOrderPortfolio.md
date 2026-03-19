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
contradiction_flags: []
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
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-18T23:34:43.622169'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:35:18.534682'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:36:31.041712'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:36:39.530889'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:36:51.611387'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:36:55.500219'
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
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper introduces the first quantum formulation for portfolio optimization incorporating higher-order moments (skewness and kurtosis), extending beyond traditional mean-variance approaches. The authors develop a higher-order unconstrained binary optimization (HUBO) problem and benchmark its performance using the Quantum Approximate Optimization Algorithm (QAOA) against a classical continuous variable solution with integer programming-based discretization. The study evaluates the practical relevance of quantum methods for computationally challenging portfolio optimization tasks in finance.
## Methodology
The paper presents an empirical study on higher-order portfolio optimization using the Quantum Approximate Optimization Algorithm (QAOA). The research develops a quantum formulation for portfolio optimization that incorporates higher-order moments (skewness and kurtosis), leading to a higher-order unconstrained binary optimization (HUBO) problem. The methodology involves encoding integer variables into binary variables with logarithmic overhead and formulating the problem as a spin system energy minimization task. The QAOA circuit is constructed to solve the HUBO problem, with the cost Hamiltonian derived from the portfolio optimization objective function, including penalty terms for budget constraints. The classical baseline for comparison is a continuous variable portfolio optimization problem discretized via integer programming. The experimental evaluation involves 100 portfolio optimization instances, comparing the solution quality of the quantum HUBO formulation against the classical baseline. The study also benchmarks QAOA's performance on these higher-order problems, identifying challenges in its application.

**Algorithms used:** QAOA
**Frameworks:** Qiskit

**Experimental setup:** The experiments were conducted using a quantum simulator, as the paper does not specify the use of real quantum processing units (QPUs). The QAOA circuit was constructed for each of the 100 portfolio optimization instances, with higher-order terms encoded into the Hamiltonian. The classical baseline was solved using Sequential Least Squares Programming for continuous variable optimization, followed by integer programming-based discretization. The quantum and classical solutions were compared based on expected returns and leftover budget metrics.

**Dataset:** The paper uses historical stock price data for portfolio optimization instances, though the exact dataset is not explicitly named. Example data includes stock prices for The Walt Disney Company (DIS) and The Travelers Companies, Inc. (TRV) over a 10-year period (2015-2025). The budget for optimization problems was randomly generated, and the dataset was used to compute expected returns, covariance, coskewness, and cokurtosis tensors.
## Findings
- [supported] The paper develops the first quantum portfolio optimization problem that includes higher-order moments (skewness and kurtosis), enabling more realistic modeling of portfolio return distributions.
- [supported] Experimental evaluation on 100 portfolio optimization problems shows that the higher-order binary optimization (HUBO) formulation often yields better portfolio allocations than the classical continuous variable formulation with integer programming-based discretization.
- [supported] The QAOA algorithm is benchmarked on 100 instances of higher-order binary portfolio optimization problems, identifying challenges in its application to real-world higher-order optimization use cases.
- [supported] The quantum formulation uses realistic integer variable encoding and a capital-based budget constraint, addressing practical limitations of prior quantum portfolio optimization approaches.
- [speculative] The authors suggest that quantum-native approaches like QAOA could address scalability limitations of classical methods for higher-order portfolio optimization problems.
- [speculative] The paper implies that higher-order portfolio optimization may offer a pathway to quantum advantage in financial services due to its classical computational complexity.

**Results summary:** The paper introduces a novel quantum formulation for portfolio optimization incorporating higher-order moments (skewness and kurtosis), which are typically omitted in classical and quantum approaches. Through extensive experimentation on 100 problem instances, the authors demonstrate that their higher-order unconstrained binary optimization (HUBO) formulation, solved via QAOA, frequently produces superior portfolio allocations compared to a classical continuous variable baseline with integer programming-based discretization. The study also benchmarks QAOA performance on higher-order problems, highlighting practical challenges in quantum optimization. While the results are promising for quantum methods in finance, all experiments were conducted via simulation, and no claims of quantum advantage on real hardware are made.

**Performance claims:**
- HUBO formulation outperforms classical continuous variable formulation with integer programming-based discretization in solution quality across 100 portfolio optimization instances
- 5-qubit encoding used for a 2-asset portfolio example with higher-order moments
- Logarithmic overhead in qubit requirements for integer-to-binary variable encoding (e.g., 3 qubits for integers in [0,6])
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage empirically but argues theoretically that higher-order portfolio optimization could be a promising candidate for quantum speedup due to its classical computational complexity. All results are derived from simulations, and the authors note that classical methods remain competitive for small- to medium-scale problems.
## Limitations
- Experiments conducted on a limited number of assets (only up to 100 problem instances, with examples shown for 2 assets), which may not generalize to larger, real-world portfolios [inferred]
- Higher-order unconstrained binary optimization (HUBO) problems are computationally intensive, and the paper does not address scalability beyond small problem sizes
- QAOA performance evaluated only on simulated quantum hardware, not on real quantum devices, which may introduce noise and decoherence effects not accounted for in simulations [inferred]
- Budget constraint encoding penalizes both over- and under-investment equally, which may not reflect real-world financial constraints where over-investment is often impossible
- Integer variable encoding introduces logarithmic overhead in qubit count, limiting practical applicability on near-term quantum devices with restricted qubit counts
- No comparison with state-of-the-art classical solvers (e.g., advanced integer programming or heuristic methods) to benchmark quantum advantage [inferred]
- Higher-order moments (skewness and kurtosis) rely on accurate estimation from historical data, which may not capture future market behavior [inferred]
- Parameter selection for risk aversion (q0, q1, q2) is arbitrary and may not be optimal for all problem instances [inferred]
- Conference paper page limits may have constrained detailed discussion of noise mitigation techniques or error analysis [inferred]
- Lack of empirical validation on real market data; experiments rely on synthetic or historical data without live testing [inferred]
- No analysis of QAOA's sensitivity to initial parameters or circuit depth, which could impact solution quality [inferred]
## Open questions
- How does the QAOA-based HUBO formulation perform on real quantum hardware with noise and decoherence?
- What is the scalability of the proposed method for portfolios with hundreds or thousands of assets?
- How does the solution quality degrade as the number of qubits increases, given the logarithmic overhead in encoding?
- Can alternative budget constraint encodings (e.g., asymmetric penalties) improve practical feasibility?
- What is the impact of different risk aversion parameter settings on portfolio performance?
- How does the method compare to classical higher-order optimization techniques (e.g., tensor decomposition or heuristic solvers) in terms of speed and accuracy?
- Can the approach be extended to multi-period portfolio optimization or dynamic rebalancing?
- What are the implications of using geometric vs. arithmetic mean returns for higher-order moments?

**Future work:**
- Test the algorithm on real quantum hardware (e.g., IBM Quantum or Rigetti devices) to evaluate noise resilience
- Extend the evaluation to larger problem sizes (e.g., 50+ assets) to assess scalability
- Compare the QAOA-based HUBO formulation with state-of-the-art classical solvers for higher-order optimization
- Explore alternative budget constraint encodings to avoid penalizing under-investment equally with over-investment
- Investigate hybrid quantum-classical approaches to reduce qubit requirements (e.g., decomposition techniques)
- Develop noise mitigation strategies tailored to higher-order QAOA circuits
- Apply the method to multi-period portfolio optimization or dynamic asset allocation
- Validate the approach on real-time market data to assess practical utility
- Optimize risk aversion parameters using machine learning or adaptive techniques
## Key ideas
- #idea:quantum-advantage — First quantum formulation for portfolio optimization incorporating higher-order moments (skewness/kurtosis) via HUBO, outperforming classical continuous variable approaches in solution quality for 100 instances
- #idea:near-term-feasibility — Demonstrates QAOA's applicability to higher-order portfolio optimization on simulated hardware, though scalability to larger asset universes remains untested
- #idea:hybrid-approach — Implicit hybrid approach through classical preprocessing (integer programming discretization) and quantum HUBO formulation, suggesting a practical path for near-term deployment
- #limitation:simulation-only — All results derived from classical simulation of QAOA, with no empirical validation on real quantum hardware
- #limitation:qubit-count — Integer variable encoding introduces logarithmic qubit overhead, potentially limiting problem size on near-term devices
- #limitation:noise — Potential noise and decoherence effects not accounted for due to simulation-only experiments
- #limitation:data-encoding — Logarithmic overhead in qubit requirements for integer-to-binary variable encoding limits practical applicability
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
