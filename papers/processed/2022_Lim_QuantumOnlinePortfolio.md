---
aliases:
- A Quantum Online Portfolio Optimization Algorithm
- Quantum Online Portfolio Optimization
authors:
- Debbie Lim
- Patrick Rebentrost
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:hybrid-approach
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- grover
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:58:00.485519'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:07.260676'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:58:18.155719'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:58:47.541994'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:59:11.242747'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:59:24.179412'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/amplitude-estimation
- method/grover
- idea/quantum-advantage
- idea/hybrid-approach
- idea/near-term-feasibility
- contradiction/scalability
title: A Quantum Online Portfolio Optimization Algorithm
topic_tags:
- portfolio-optimisation
year: 2023
zotero_key: ''
---

## Abstract summary
The paper develops a quantum algorithm for online portfolio selection by quantizing the classical multiplicative-weights-based method of Helmbold et al. It introduces a sampling-based classical variant to reduce transaction costs, then extends it to a quantum version using quantum state preparation, inner product estimation, amplitude amplification, and quantum multi-sampling. The resulting quantum algorithm achieves a quadratic speedup in the number of assets while maintaining comparable regret guarantees and transaction costs that do not scale with the asset universe size.
## Methodology
This paper is a preprint and is primarily theoretical with algorithmic analysis rather than empirical experimentation. The authors develop a quantum online portfolio optimization method by starting from the classical online multiplicative-weights portfolio selection algorithm of Helmbold et al. and progressively transforming it through four algorithmic stages: (1) the original exponentiated-gradient online portfolio update with transaction costs, (2) a sampling-based classical variant that reduces transaction costs by investing only in sampled assets, (3) an approximate classical variant that estimates the required inner products with controlled relative error, and (4) a fully quantum version that replaces classical subroutines with quantum state preparation, quantum inner product estimation, quantum norm estimation, quantum maximum finding, amplitude amplification, and quantum multi-sampling. The methodology is based on a formal online optimization framework with no-short-selling, bounded price relatives, and fixed per-asset transaction costs. The main results are derived through theorem-proof analysis of regret bounds, runtime complexity, and transaction-cost complexity under oracle access assumptions. The paper proves that the quantum algorithm achieves a quadratic speedup in the number of assets n relative to the classical online method, while preserving sublinear regret up to constant-factor degradation. No real financial backtest or hardware experiment is reported; the contribution is a formal computational model, algorithm construction, and complexity analysis under quantum query access to price-relative vectors.

**Algorithms used:** Exponentiated Gradient, Multiplicative Weight Update, Quantum Inner Product Estimation, Quantum State Preparation, Quantum Norm Estimation, Quantum Maximum Finding, Amplitude Amplification, Amplitude Estimation, Quantum Multi-Sampling, Grover Search
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes a quantum online portfolio optimization algorithm by quantizing the Helmbold et al. multiplicative-update online portfolio selection method.
- [speculative] The authors claim the quantum algorithm achieves a quadratic speedup in runtime with respect to the number of assets n.
- [speculative] The claimed speedup relies on quantum state preparation, quantum inner product estimation, amplitude amplification, and quantum multi-sampling.
- [speculative] The quantum algorithm is claimed to achieve regret bounded by 12/rmin * sqrt(log n / (2T)) with success probability at least 1 - 3δ.
- [speculative] The classical baseline algorithm achieves regret bounded by 1/rmin * sqrt(log n / (2T)) with total runtime O(Tn) and transaction cost O(TnC).
- [speculative] A sampling-based classical variant reduces transaction cost dependence on n, achieving transaction cost O(T^2 C log(T/δ)) instead of O(TnC), at the expense of worse runtime and a larger constant in the regret bound.
- [speculative] The sampling-based classical algorithm is claimed to satisfy regret bound 2/rmin * sqrt(log n / (2T)) with success probability at least 1 - 2δ.
- [speculative] An approximate classical algorithm using sampled inner-product estimation is claimed to achieve regret bound 8/rmin * sqrt(log n / (2T)) with success probability at least 1 - 3δ.
- [speculative] The quantum algorithm's transaction cost is claimed to be independent of n, specifically O(T^2 C log(T/δ)), which the authors argue is useful for large-asset portfolios.
- [speculative] The paper generalizes the exponentiated-gradient convergence analysis to erroneous updates where inner products and normalization constants are only approximately known.
- [speculative] Under approximate update conditions, the paper claims regret guarantees remain within constant-factor degradation relative to the exact-update algorithm.
- [speculative] The authors claim the quantum method is more space efficient than the classical counterpart because portfolio vectors need not be stored explicitly and can instead be generated by arithmetic unitaries.
- [speculative] The paper notes that practical implementation may be bottlenecked by constructing price-relative oracles/QRAM, estimated as O(Tn log n) time and O(Tn) space.

**Results summary:** This preprint presents a theoretical quantum algorithm for online portfolio optimization based on a quantized version of the Helmbold et al. multiplicative-update method. The paper develops a progression from the original classical online algorithm to a sampling-based classical version, then to an approximate classical version with estimated inner products, and finally to a quantum version using quantum state preparation, inner-product estimation, and multi-sampling. The main claimed result is a quadratic runtime improvement in the number of assets n, from linear dependence in the classical baseline to square-root dependence in the quantum algorithm, while keeping transaction cost independent of n through sampling. However, the work is analytical/theoretical only, with no hardware experiments or simulation benchmarks demonstrating empirical advantage; the paper also acknowledges that oracle/QRAM construction may be a practical bottleneck.

**Performance claims:**
- Classical online algorithm (Algorithm 1): regret <= 1/rmin * sqrt(log n / (2T)); runtime O(Tn); transaction cost O(TnC)
- Sampling-based classical algorithm (Algorithm 2): regret <= 2/rmin * sqrt(log n / (2T)) with success probability at least 1 - 2δ; runtime O(T^2 n log(T/δ)); transaction cost O(T^2 C log(T/δ))
- Approximate sampling-based classical algorithm (Algorithm 3): regret <= 8/rmin * sqrt(log n / (2T)) with success probability at least 1 - 3δ; runtime O(Tn + T^2/rmin * log(1/δ) + T^2 log(T/δ)); transaction cost O(T^2 C log(T/δ))
- Quantum online algorithm (Algorithm 4): regret <= 12/rmin * sqrt(log n / (2T)) with success probability at least 1 - 3δ
- Quantum online algorithm runtime: O(T^3 * sqrt(n) / rmin * log^1.5(1/δ)) up to polylog factors
- Quantum inner product estimation subroutine: O(sqrt(n)/(ε * sqrt(umin)) * log(1/δ)) queries and gates
- Quantum norm estimation subroutine: O(sqrt(n)/ε * log(1/δ)) queries and gates
- QRAM/oracle construction overhead discussed as O(Tn log n) time and O(Tn) space
## Quantum advantage claim
**Classification:** speculative

The paper claims a theoretical quadratic speedup in runtime with respect to the number of assets n, but this is a preprint with no empirical validation on real hardware or simulation benchmarks demonstrating end-to-end advantage. The claimed benefit also depends on oracle/QRAM assumptions that the authors acknowledge may be a practical bottleneck.
## Limitations
- As a preprint, the work has not undergone peer review.
- The practical implementation of the price-relative oracles is identified as a bottleneck; building QRAM for each oracle requires O(T n log n) time and O(T n) space.
- The quantum algorithm achieves a worse regret bound than the baseline classical algorithm by a constant factor.
- The analysis assumes a known lower bound r_min on all price relatives, which may be unrealistic or difficult to guarantee in real markets.
- The model assumes no short-selling throughout the trading period.
- The transaction cost model is highly simplified: a fixed cost per investment independent of trade size is assumed.
- The framework assumes bounded price relatives and is stated to be favorable when asset prices have bounded relative volatility, limiting applicability in highly volatile markets.
- The computational model ignores finite-precision issues by assuming classical and quantum arithmetic operations take constant time and that sufficient precision is always available.
- The quantum input model assumes quantum query access to price-relative vectors/oracles, which may be difficult to realize in practice.
- The algorithm is probabilistic and its guarantees hold only up to a failure probability parameter δ.
- The runtime of the quantum algorithm scales as roughly O~(T^3 sqrt(n)/r_min), which may be large for long horizons T despite the quadratic speedup in n.
- [inferred] No empirical experiments or benchmarking on real or simulated financial data are provided, so practical performance is unvalidated.
- [inferred] No implementation on actual quantum hardware or noisy simulators is reported; hardware noise, decoherence, and gate errors are not assessed.
- [inferred] No comparison is made against strong modern classical online portfolio selection baselines beyond the Helmbold et al. algorithm.
- [inferred] The claimed quantum advantage depends on nontrivial data-loading assumptions (QRAM/oracle access), which may offset end-to-end speedups.
- [inferred] The portfolio objective focuses on regret versus a fixed offline portfolio and does not directly evaluate common financial metrics such as risk-adjusted return, drawdown, or turnover.
- [inferred] The use of normalized price relatives may abstract away market features important for deployment, such as liquidity, slippage, and market impact.
## Open questions
- Can the price-relative oracle/QRAM bottleneck be reduced or avoided while preserving quantum speedup?
- How robust is the algorithm when the assumption of a known lower bound r_min is violated or only approximately satisfied?
- Does the theoretical quadratic speedup in n translate into practical end-to-end advantage once data loading and oracle construction costs are included?
- How does the algorithm perform under more realistic transaction cost models that depend on trade size, turnover, or market impact?
- Can the method be extended to settings with additional portfolio constraints, such as turnover, leverage, cardinality, or short-selling constraints?
- How well does the approach work in robust portfolio optimization settings with uncertainty sets over returns or constraints?
- What is the behavior of the algorithm in highly volatile markets where bounded-relative-volatility assumptions are weak or invalid?
- How would finite-precision arithmetic and approximation errors affect the theoretical guarantees in practice?
- [inferred] How does the method compare empirically with state-of-the-art classical online portfolio selection and bandit-based methods on real financial datasets?
- [inferred] What resource requirements in qubits, circuit depth, and fault tolerance would be needed for a practical implementation?

**Future work:**
- Consider additional constraints in the portfolio optimization problem.
- Incorporate transaction-cost minimization directly into the objective, for example via a term involving ||w^(t) - w^(t-1)||_1.
- Study portfolio optimization in the robust setting where parameters belong to an uncertainty set.
- Investigate different notions of robustness, including constraint, objective, and relative robustness, together with different uncertainty sets.
- [inferred] Develop more practical data-access models or oracle constructions that reduce QRAM overhead.
- [inferred] Validate the algorithm empirically on real or realistic market datasets.
- [inferred] Test the approach on noisy quantum hardware or fault-tolerant resource estimates to assess implementability.
- [inferred] Extend the framework to richer market frictions, including variable transaction costs, slippage, and market impact.
- [inferred] Compare against stronger classical baselines and hybrid quantum-classical alternatives.
## Key ideas
- #idea:quantum-advantage — The paper quantizes an online multiplicative-weights / exponentiated-gradient portfolio selection method and claims a quadratic runtime speedup in the number of assets, reducing dependence from O(n) to Õ(√n) under oracle access assumptions.
- #idea:quantum-advantage — Approximate quantum subroutines for inner-product and norm estimation are incorporated into an erroneous-update framework that preserves sublinear regret up to constant-factor degradation.
- #idea:hybrid-approach — The practical workflow is implicitly hybrid: classical data handling and oracle/QRAM construction support quantum subroutines for estimation, maximum finding, amplitude amplification, and multi-sampling.
- #idea:near-term-feasibility — The work is purely theoretical and not NISQ-ready; it relies on idealized quantum query access, amplitude estimation, and other subroutines without hardware validation.
- #idea:quantum-advantage — Sampling-based portfolio updates are used to keep transaction-cost dependence independent of the asset universe size under the paper’s simplified fixed per-asset transaction-cost model.
## Contradictions
- The paper claims quantum advantage via quadratic speedup in the number of assets, but this is weakened by the acknowledged O(Tn log n) time and O(Tn) space needed for oracle/QRAM construction, plus the heavy Õ(T^3√n/r_min) runtime dependence; this creates a clear #contradiction:scalability between asymptotic query-model gains and end-to-end practicality.
- The paper presents quantum superiority relative to a classical Helmbold-style baseline, yet it provides no empirical benchmarking against stronger modern classical online portfolio methods, limiting the strength of the superiority claim.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
