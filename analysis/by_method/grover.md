# Grover

**Papers:** 16 | **Empirical:** 3 | **Theoretical:** 3 | **Review:** 2

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | preprint | portfolio-optimisation, high-frequency-trading | speculative | medium |
| [[2026_DECCANINTERNATIONALACADEMICPUBLISHERS_QuantumComputingAlgorithms]] | 2026 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | medium |
| [[2026_Nawaz_ExploringQuantumMachine]] | 2026 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | conference-paper | portfolio-optimisation, risk-modelling, high-frequency-trading | speculative | medium |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_Malhotra_ComparativeStudyQuantum]] | 2025 | conference-paper | portfolio-optimisation, derivatives-pricing, quantum-cryptography, high-frequency-trading, asset-pricing | speculative | medium |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | asset-pricing, portfolio-optimisation, risk-modelling | speculative | medium |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, quantum-cryptography, regulatory-compliance, market-simulation | theoretical | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | peer-reviewed-empirical | portfolio-optimisation | theoretical | high |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | peer-reviewed-empirical | risk-modelling, derivatives-pricing | theoretical | high |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | peer-reviewed-empirical | derivatives-pricing | theoretical | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, high-frequency-trading, regulatory-compliance | speculative | medium |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | preprint | derivatives-pricing | theoretical | high |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | peer-reviewed-theoretical | fraud-detection, high-frequency-trading | theoretical | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 12 |
| risk-modelling | 10 |
| high-frequency-trading | 9 |
| derivatives-pricing | 9 |
| fraud-detection | 7 |
| quantum-cryptography | 7 |
| credit-scoring | 6 |
| asset-pricing | 6 |
| regulatory-compliance | 5 |
| market-simulation | 5 |

## Key Findings

- [supported] Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, Two-Step QAOA, and Grover-Mixer QAOA in noiseless and shot-based simulations on small VRP instances. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-Chain (LC) QAOA reduces two-qubit gate depth and boosts noise robustness, achieving the shallowest circuits on IBM Eagle/Heron hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] On real hardware (IBM Eagle/Heron), LC-QAOA with XpXm dynamical decoupling more than doubles feasibility (from <1% to >2%) and recovers the optimal VRP solution in several trials. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Grover-Mixer QAOA and Two-Step QAOA show high feasibility in simulation (e.g., 21% for GM-QAOA at p=8) but are hampered by deeper circuits, making them less effective on real hardware. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Linear-ramp initialization (LRI-QAOA) concentrates probability on feasible solutions, outperforming random initialization in simulations (e.g., 47.6% feasibility vs. 2% for standard QAOA at p=8). — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] Dynamical decoupling (XpXm) improves hardware performance (e.g., optimal solution rank improved from 235 to 15 on IBM Rensselaer), while heavier error mitigation (e.g., ZNE, Pauli twirling) degrades performance due to circuit distortion. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] LC-QAOA scales efficiently to larger VRP instances (30 qubits), reliably recovering the optimal route at depths p>16 on both IBM Eagle and Heron, with higher success on lower-error devices. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] CVaR (Conditional Value at Risk) objective improves optimization by biasing search toward high-quality solutions, enabling reliable performance at larger scales. — [[2026_Azfar_ShallowRobustQaoa]]
- [supported] The study provides a unified comparative framework for QML optimization algorithms, highlighting their practical feasibility and identifying key research gaps hindering real-world deployment — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms — [[2026_Nawaz_ExploringQuantumMachine]]
- [supported] The Variational Quantum Eigensolver (VQE) algorithm is proposed as an effective tool for minimizing the energy function of time-varying dynamic control systems, demonstrating potential for quantum acceleration in optimization tasks. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] Quantum algorithms, including VQE, Grover’s algorithm, and QAOA, are applied to dynamic control problems, showing numerical optimization results for differential equation-based systems. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] The paper presents pseudocode and numerical results for optimizing control actions in a dynamic system described by nonlinear differential equations, achieving a minimal objective function value of 0.4047 for a linear system and 2.619e-08 for a nonlinear system. — [[2025_Gibadullin_QuantumAlgorithmsSolving]]
- [supported] The paper demonstrates basic quantum circuits (e.g., Quantum Random Bit Generator) using frameworks like Qiskit, Cirq, QDK, Forest, PennyLane, and ProjectQ on both simulators and real quantum hardware — [[2025_Malhotra_ComparativeStudyQuantum]]
- [supported] IBM's 127-qubit quantum system and Google's 53-qubit Sycamore processor are cited as milestones in quantum hardware development — [[2025_Malhotra_ComparativeStudyQuantum]]
- [supported] Quantum volume is identified as a key metric for measuring quantum computer effectiveness, considering factors like qubit count, gate errors, and compiler efficiency — [[2025_Malhotra_ComparativeStudyQuantum]]
- [supported] The paper compares quantum frameworks (e.g., Qiskit, Cirq, QDK) in terms of language support, hardware compatibility, and open-source availability — [[2025_Malhotra_ComparativeStudyQuantum]]
- [supported] Quantum computing has demonstrated experimental and commercial applications across diverse industries including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology as of 2025 — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Google’s Sycamore and Willow quantum processors have shown quantum advantage in specific tasks, with Willow completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years — [[2026_Mahmod_StateQuantumComputing]]
- [supported] D-Wave’s Advantage2 quantum computer can solve problems with up to 2 million variable constraints via hybrid solver, accessible online from over 40 countries — [[2026_Mahmod_StateQuantumComputing]]
