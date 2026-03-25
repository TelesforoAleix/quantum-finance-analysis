# Asset Pricing

**Papers:** 18 | **Empirical:** 4

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | HHL, amplitude-estimation, quantum-simulation, variational, quantum-ML, classical-simulation | speculative | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | quantum-annealing, QUBO, quantum-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | quantum-annealing, QUBO, HHL | speculative | high |
| [[2025_Choudhary_HqnnFspHybrid]] | 2025 | preprint | quantum-ML, variational, classical-simulation | speculative | medium |
| [[2025_Frana_QuantumSpeedUps]] | 2025 | preprint | quantum-simulation, variational | speculative | high |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | conference-paper | quantum-ML, QUBO, variational, classical-simulation | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, amplitude-estimation, QUBO, variational, grover, quantum-walk, quantum-simulation | speculative | high |
| [[2025_Springer_QuantumFinance]] | 2025 | conference-paper | VQE, grover, QAOA, variational, quantum-simulation, classical-simulation | speculative | medium |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | peer-reviewed-empirical | quantum-ML, variational | speculative | medium |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | preprint | quantum-ML, variational, classical-simulation | speculative | high |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | conference-paper | quantum-ML, quantum-SVM | speculative | high |
| [[2024_Kea_HybridQuantumClassical]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, classical-simulation | speculative | medium |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | peer-reviewed-empirical | quantum-ML, variational, classical-simulation | not-applicable | medium |
| [[2023_Ferro_DUpdateReview]] | 2023 | technical-report | amplitude-estimation, grover, quantum-ML, quantum-walk, quantum-simulation | theoretical | high |
| [[2023_S_PotentialQuantumTechniques]] | 2023 | preprint | quantum-annealing, QUBO, quantum-ML, quantum-SVM, classical-simulation | speculative | medium |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | peer-reviewed-empirical | classical-simulation | speculative | high |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | HHL, quantum-ML, quantum-SVM, quantum-annealing, QUBO, variational, amplitude-estimation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | QAOA, VQE, quantum-annealing, HHL, quantum-ML, quantum-SVM, variational, grover, quantum-walk, classical-simulation | speculative | medium |

## Key Findings

- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] The proposed hybrid quantum-classical models (HybridQNN1 and HybridQNN2) achieved lower RMSE than the standalone CustomQNN across all tested qubit settings on simulator-based experiments. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] HybridQNN2 achieved the best RMSE among the quantum-enhanced models, with average RMSE values of 0.02312, 0.01959, and 0.01920 for 3, 4, and 5 qubits respectively under TimeSeriesSplit. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] HybridQNN1 achieved average RMSE values of 0.02605, 0.02161, and 0.01740 for 3, 4, and 5 qubits respectively, outperforming CustomQNN but with higher training cost at 5 qubits. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] The standalone CustomQNN performed substantially worse than the hybrid variants, with average RMSE values of 0.07603, 0.05528, and 0.06120 for 3, 4, and 5 qubits respectively. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] Classical benchmark models outperformed all quantum and hybrid models in this study, with RMSE around 0.00649-0.00781 depending on architecture and feature count. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] All three quantum-related models showed reasonable overlap with actual prices during a relatively stable regime (Phase 1) but failed to track a sharp downward regime shift in Phase 2. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] Error distribution analysis indicated that HybridQNN1 and HybridQNN2 had narrower error distributions and lower variance than CustomQNN, suggesting more stable predictions. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] Increasing qubit count generally improved predictive accuracy for the hybrid models, but also increased training time, revealing a clear accuracy-computation trade-off. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] HybridQNN2 was more computationally efficient than HybridQNN1 across the tested settings, with notably lower training times while maintaining the best hybrid RMSE. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] The experiments were conducted on a quantum simulator (QULACS) and HPC infrastructure rather than real quantum hardware. — [[2025_Choudhary_HqnnFspHybrid]]
- [supported] The quantum algorithm based on matrix multiplicative weights achieves a runtime of O(n^k ε^{-4} + n^{k/2} ε^{-5}) for approximating Lasserre’s hierarchy values for polynomial optimization under specific conditions (e.g., optimal value attained within an ℓ1-ball or simplex constraints). — [[2025_Frana_QuantumSpeedUps]]
- [supported] For unconstrained polynomial optimization, the quantum algorithm achieves a runtime of O((n^{2k})^{1/2} + (1/ε) n^{k/2}) ε^{-4}) to approximate the optimal value with accuracy ε^{1-r}, where r is the radius of the ℓ1-ball containing the optimal solution. — [[2025_Frana_QuantumSpeedUps]]
- [supported] For inequality-constrained polynomial optimization, the quantum algorithm achieves a runtime of O(s_g (n^{2k}^{1/2} + (Σ_{i=0}^m n^{k-d_i})^{1/2} (1/ε)) ε^{-4}), where s_g bounds the sparsity of coefficient-matching matrices. — [[2025_Frana_QuantumSpeedUps]]
- [supported] The quantum algorithm for portfolio optimization achieves a runtime of O(n ε^{-4} + √n ε^{-5}), improving over the classical O(n^{ω+1} log(1/ε)) bound with ω ≈ 2.373. — [[2025_Frana_QuantumSpeedUps]]
- [supported] The quantum algorithm demonstrates improved asymptotic performance for large-scale polynomial optimization problems compared to classical and quantum interior-point methods, despite worse dependence on the precision parameter ε. — [[2025_Frana_QuantumSpeedUps]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-ML | 13 |
| variational | 12 |
| classical-simulation | 10 |
| quantum-simulation | 6 |
| quantum-annealing | 6 |
| QUBO | 6 |
| HHL | 5 |
| quantum-SVM | 5 |
| amplitude-estimation | 4 |
| grover | 4 |
| QAOA | 3 |
| VQE | 3 |
| quantum-walk | 3 |

## Open Questions

- How do the proposed quantum algorithms perform on real quantum hardware with current error rates and qubit counts? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- What is the impact of hardware noise (e.g., gate errors, decoherence) on the empirical speedups observed in simulations? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- Can the polynomial-to-super-polynomial speedups be maintained for larger problem instances (e.g., d > 20) on near-term devices? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- How do the variational quantum schemes for nonlinear SDEs compare to classical methods in terms of accuracy, robustness, and scalability? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- What are the trade-offs between circuit depth, qubit count, and accuracy for practical financial applications (e.g., option pricing with d=100)? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- How sensitive are the results to the choice of ansatz and training strategy for variational schemes? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- Can the proposed methods be extended to SDEs with non-Lipschitz coefficients or unbounded domains (e.g., rough volatility models)? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- What are the implications of state space truncation for long-time simulations (e.g., T >> 1) or heavy-tailed distributions? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- How do the quantum algorithms perform in the presence of correlated noise or crosstalk on real hardware? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- What are the minimal hardware requirements (e.g., qubit count, gate fidelity) to achieve a practical quantum advantage for SDE solving? — [[2026_Prasad_QuantumAlgorithmsStochastic]]
