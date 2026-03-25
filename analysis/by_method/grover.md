# Grover

**Papers:** 26 | **Empirical:** 2 | **Theoretical:** 6 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | — | speculative | low |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | — | speculative | low |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection | theoretical | medium |
| [[2025_Chawla_QuantumComputingUnderlying]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, market-simulation | theoretical | medium |
| [[2025_Chuvakov_FactoringDecisionSupport]] | 2025 | peer-reviewed-theoretical | risk-modelling | theoretical | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | — | theoretical | low |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_Matsakos_QuantumUnstructuredSearch]] | 2025 | preprint | portfolio-optimisation | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, quantum-cryptography, regulatory-compliance | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | quantum-cryptography, high-frequency-trading | speculative | medium |
| [[2024_Carrascal_BacktestingQuantumComputing]] | 2024 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2024_Pasupuleti_AdvancementsQuantumComputing]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, quantum-cryptography | theoretical | medium |
| [[2024_Unknown_QuantumMachineLearning]] | 2024 | peer-reviewed-theoretical | — | theoretical | medium |
| [[2022_Lim_QuantumOnlinePortfolio]] | 2023 | preprint | portfolio-optimisation | speculative | high |
| [[2023_Abbas_QuantumOptimizationPotential]] | 2023 | technical-report | portfolio-optimisation, risk-modelling | theoretical | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Ferro_DUpdateReview]] | 2023 | technical-report | derivatives-pricing, risk-modelling, asset-pricing | theoretical | high |
| [[2023_Udvarnoki_QuantumAdvantageMonte]] | 2023 | peer-reviewed-empirical | derivatives-pricing | theoretical | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | preprint | portfolio-optimisation | speculative | high |
| [[2022_Ferro_DEvaluationQuantum]] | 2022 | technical-report | derivatives-pricing, risk-modelling | theoretical | high |
| [[2023_Saini_CurrentChallengeLimitations]] | 2022 | peer-reviewed-theoretical | — | speculative | low |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | speculative | medium |
| [[2019_Li_ResearchQuantumComputing]] | 2019 | conference-paper | quantum-cryptography | speculative | medium |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing, risk-modelling | theoretical | high |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | preprint | — | speculative | low |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 13 |
| risk-modelling | 13 |
| derivatives-pricing | 9 |
| quantum-cryptography | 7 |
| fraud-detection | 5 |
| asset-pricing | 4 |
| credit-scoring | 3 |
| market-simulation | 2 |
| high-frequency-trading | 2 |
| regulatory-compliance | 1 |

## Key Findings

- [supported] In noiseless statevector simulations on a small VRP instance, linear-ramp initialized QAOA (LRI-QAOA) achieved the highest feasibility among tested variants, reaching 47.6% feasible samples at p=8 versus 2.4% for standard QAOA, 4.43% for Two-Step QAOA, 21.38% for GM-QAOA, and 2.86% for LC-QAOA. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] In statevector simulation at p=4, LRI-QAOA achieved 25.54% feasibility versus 2.4% for standard QAOA, 5.6% for Two-Step QAOA, 10.72% for GM-QAOA, and 3.94% for LC-QAOA. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] In Aer shot-based simulation, LRI-QAOA outperformed standard QAOA in feasibility at p=4 (6.47% vs 2.77%) and p=8 (1.68% vs 1.5%), while GM-QAOA was best at p=8 with 6.7% feasibility. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Shot noise substantially reduced feasibility relative to statevector simulation; for example, LRI-QAOA dropped from 47.6% feasible in statevector simulation to 1.68% on Aer at p=8. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] GM-QAOA improved feasibility in simulation but incurred very large circuit depth; the paper reports two-qubit gate depth above 3000 even at p=2 and transpilation failure for p>5. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA produced the shallowest transpiled two-qubit circuits among compared methods on IBM hardware, due to restricting ZZ interactions to nearest neighbors and reducing swap overhead. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] The paper reports that ramp-initialized standard QAOA at p=4 could match or outperform randomly initialized standard QAOA at p=6 on hardware in solution quality, implying lower depth can suffice with structured initialization. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real IBM Eagle and Heron hardware, raw feasibility remained below 1% for shallow-depth implementations across methods, indicating strong degradation from noise and limited connectivity. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA combined with XpXm dynamical decoupling achieved hardware feasibility above 2% on IBM Eagle according to the text, outperforming deeper alternatives under noise. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling improved hardware performance: on IBM Fez at p=4, feasibility increased from 1.14% with XX decoupling to 1.60% with XpXm, and the optimal solution rank improved from 16 to 6. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On IBM Rensselaer at p=4, XpXm dynamical decoupling improved the optimal solution rank from 235 with XX decoupling to 15, while feasibility rose from 0.69% to 0.80%. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Heavy mitigation stacks did not outperform simple dynamical decoupling on hardware; on IBM Fez at p=4, XpXm alone gave 1.80% feasibility, while XpXm plus Pauli twirling, TREX, and ZNE reduced feasibility to 0.60%. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] For a larger 30-qubit VRP instance (5 nodes, 2 vehicles), LC-QAOA with linear-ramp initialization remained compilable while other variants were reported as not reliably executable on hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On the 30-qubit instance, LC-QAOA recovered the optimal route on hardware at higher depth: the correct solution appeared at p=19 on IBM Rensselaer and p=18 on IBM Fez, though with low absolute feasibility. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] CVaR improved large-instance hardware performance in several settings; for example, on IBM Rensselaer at p=18 feasibility increased from 0.3% to 4.95%, and on IBM Fez at p=18 from 0.5% to 4.72%. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] The review identifies QAOA, VQE, QNNs, QSVMs, Grover-based methods, QPCA, and quantum k-means as the main QML approaches studied for optimization across finance, logistics, AI, and chemistry. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Across the reviewed literature, the paper finds a broad theme that QML methods show potential for exploring large solution spaces, faster convergence, and improved optimization performance relative to some classical approaches, but this is not established as a general empirical superiority. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review concludes that QAOA and VQE are the most prominent optimization-oriented QML methods, with QAOA emphasized for combinatorial optimization and VQE for energy/molecular optimization. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The review identifies portfolio optimization in finance as a key application area, arguing that QAOA, VQE, and Grover-style search are being explored for asset allocation, risk management, and option-pricing-related tasks. — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] A consensus theme in the reviewed literature is that current practical deployment is constrained by NISQ-era limitations, especially quantum noise, decoherence, limited qubit counts, and shallow-circuit requirements. — [[2026_Nawaz_ExploringQuantumMachine]]
