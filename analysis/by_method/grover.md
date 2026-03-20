# Grover

**Papers:** 13 | **Theoretical:** 3 | **Review:** 2

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | portfolio-optimisation, high-frequency-trading | speculative | medium |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | medium |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | theoretical | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, high-frequency-trading | speculative | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing, risk-modelling | theoretical | high |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | preprint | fraud-detection, high-frequency-trading | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 11 |
| risk-modelling | 10 |
| high-frequency-trading | 8 |
| derivatives-pricing | 8 |
| fraud-detection | 8 |
| credit-scoring | 7 |
| asset-pricing | 7 |
| quantum-cryptography | 7 |
| regulatory-compliance | 6 |
| market-simulation | 6 |

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
- [supported] The study provides a unified comparative framework for QML algorithms, highlighting their optimization capabilities, practical feasibility, and limitations within a single analytical structure — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Key challenges hindering real-world deployment of QML include quantum noise, scalability constraints, hardware limitations, and algorithmic performance trade-offs — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Numerical experiments demonstrated that the proposed dynamic control model using quantum-inspired optimization achieved a minimal objective function value of 0.4047, indicating effective system management — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] Optimal control actions derived from the optimization process showed that the system could utilize both positive and negative influences to minimize energy costs — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] The Variational Quantum Eigensolver (VQE) algorithm is proposed as an effective tool for minimizing the energy function of time-varying dynamic control systems in quantum computing. — [[2025_Springer_QuantumFinance]]
- [supported] Quantum algorithms, including VQE, Grover’s algorithm, and QAOA, can significantly accelerate the process of finding optimal solutions for dynamic control problems compared to traditional methods. — [[2025_Springer_QuantumFinance]]
- [supported] The study demonstrates the application of quantum algorithms to a dynamic system described by differential equations, achieving optimal control actions and minimizing an objective function with a value of 0.4047. — [[2025_Springer_QuantumFinance]]
- [supported] Numerical methods and optimization algorithms (e.g., SLSQP) were used to solve nonlinear dynamic control problems, highlighting the challenges of sensitivity to parameters and local minima. — [[2025_Springer_QuantumFinance]]
- [supported] Quantum computing has demonstrated practical applications across multiple industries, including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology, with quantified performance improvements in specific use cases — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Google's Willow quantum chip achieved real-time error correction on a superconducting system with 105 qubits, completing a computation in under five minutes that would take the world's fastest supercomputer an estimated 10^25 years — [[2026_Mahmod_StateQuantumComputing]]
- [supported] D-Wave’s Advantage2 hybrid solver demonstrated the ability to solve problems with up to 2 million variable constraints, accessible via cloud service from over 40 countries as of 2025 — [[2026_Mahmod_StateQuantumComputing]]
