# QUBO

**Papers:** 21 | **Empirical:** 6 | **Theoretical:** 1 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | portfolio-optimisation, high-frequency-trading | speculative | medium |
| [[2026_Barbaresco_QPortQuantum]] | 2026 | conference-paper | portfolio-optimisation | speculative | high |
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring | theoretical | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | portfolio-optimisation, asset-pricing, risk-modelling, derivatives-pricing, credit-scoring | speculative | high |
| [[2025_Aggarwal_BridgingQuantumAlgorithms]] | 2025 | conference-paper | portfolio-optimisation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | portfolio-optimisation, asset-pricing, derivatives-pricing, risk-modelling, credit-scoring | speculative | high |
| [[2025_Bhattacharyya_SolvingGeneralQubos]] | 2025 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling, high-frequency-trading, fraud-detection | speculative | high |
| [[2025_Innan_QuantumPortfolioOptimization]] | 2025 | conference-paper | portfolio-optimisation | speculative | high |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading | theoretical | high |
| [[2025_NeelotpalDey_QuantumComputingFinancial]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Uotila_HigherOrderPortfolio]] | 2025 | conference-paper | portfolio-optimisation | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Huot_CorrectionsEnhancingKnapsack]] | 2024 | peer-reviewed-empirical | portfolio-optimisation | not-applicable | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation | speculative | high |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2023_Shan_QuantumComputingSimulated]] | 2023 | conference-paper | portfolio-optimisation | speculative | high |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | preprint | fraud-detection, regulatory-compliance | speculative | medium |
| [[2022_Kolotouros_EvolvingObjectiveFunction]] | 2022 | peer-reviewed-empirical | portfolio-optimisation, risk-modelling | speculative | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 20 |
| risk-modelling | 11 |
| fraud-detection | 7 |
| credit-scoring | 7 |
| high-frequency-trading | 6 |
| derivatives-pricing | 6 |
| asset-pricing | 5 |
| regulatory-compliance | 4 |
| quantum-cryptography | 3 |
| market-simulation | 3 |

## Key Findings

- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA on small Vehicle Routing Problem (VRP) instances in noiseless simulations. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuit depth on IBM Eagle/Heron hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (<1% to >2%) and recovers the optimum in several trials. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, improving feasibility rates from ~2% (standard QAOA) to ~47.6% in statevector simulations. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Grover-Mixer QAOA yields high feasibility in simulations (21% at p=8) but is hampered by deep circuits on hardware, failing to compile for p > 5. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Two-Step QAOA improves feasibility over standard QAOA in simulations (5.6% vs. 2.4% at p=4) but struggles with constraint leakage and deeper circuits. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling (XpXm) improves hardware performance, boosting feasibility from 1.14% to 1.60% and improving optimal solution rank from 16 to 6 on IBM Fez. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Heavy error mitigation (e.g., Pauli twirling, ZNE) underperforms compared to lightweight dynamical decoupling, reducing feasibility from 1.80% to 0.60%. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA scales to larger VRP instances (30 qubits), reliably recovering the optimal route at p > 16 on IBM Eagle/Heron, with CVaR objective further improving results. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Multi-qubit representations per stock yield negligible precision gains compared to classical Mean-Variance Optimization (MVO), indicating limited practical benefit — [[2026_Barbaresco_QPortQuantum]]
- [supported] Multi-stock encodings per qubit significantly improve efficiency with minimal precision loss, enabling more scalable quantum portfolio optimization under NISQ-era limitations — [[2026_Barbaresco_QPortQuantum]]
- [supported] QAOA consistently ranks the optimal portfolio solution higher than VQE, particularly at lower circuit depths, across both multi-qubit and multi-stock encoding strategies — [[2026_Barbaresco_QPortQuantum]]
- [supported] Increasing circuit repetitions (layers) generally improves alignment between quantum and classical solutions, with QAOA showing better resilience to compressed encodings than VQE — [[2026_Barbaresco_QPortQuantum]]
- [supported] For 3-stock and 4-stock portfolios, QAOA achieves near-optimal rankings (top positions) even at low circuit depths, while VQE requires deeper circuits to converge — [[2026_Barbaresco_QPortQuantum]]
- [supported] Encoding 2-3 stocks per qubit maintains competitive rankings for QAOA, though VQE exhibits increased variance under aggressive compression — [[2026_Barbaresco_QPortQuantum]]
- [supported] The linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323 — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] For portfolio optimization, the quantum runtime (total circuit depth D) scales as 2^0.219N, while the classical runtime scales as 2^0.323N, indicating a potential quantum scaling advantage [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The extrapolation method for LR-QAOA parameters (Δγ, Δβ, p) from smaller subproblems (4-10 qubits) to larger problems (up to 28 qubits) yields results close to direct optimization minima, validating the approach [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] Universal parameter scaling (algebraic fits for Δγ, Δβ, p across instances) reduces outliers and improves runtime scaling for feature selection, clustering, and MaxCut problems, achieving near-parity with classical benchmarks [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
- [supported] The probability of measuring the optimal solution (P_opt) remains above 0.1 on average for all problem classes, with portfolio optimization and MaxCut showing near-constant or slightly increasing P_opt with problem size [supported] — [[2026_Dehn_ExtrapolationMethodOptimize]]
