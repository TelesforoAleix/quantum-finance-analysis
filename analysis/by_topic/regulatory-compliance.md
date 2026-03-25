# Regulatory Compliance

**Papers:** 6 | **Empirical:** 1 | **Theoretical:** 3

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2026_Gnal_QuantumComputingApproaches]] | 2026 | peer-reviewed-theoretical | quantum-annealing, VQE, QUBO, variational | theoretical | high |
| [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]] | 2025 | peer-reviewed-empirical | — | speculative | low |
| [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] | 2025 | peer-reviewed-theoretical | grover, quantum-ML, classical-simulation | theoretical | high |
| [[2026_Barbaresco_IqnnCsInterpretable]] | 2025 | preprint | quantum-ML, variational, classical-simulation | not-applicable | high |
| [[2023_Alsalman_AcceleratingQuantumReadiness]] | 2023 | peer-reviewed-theoretical | — | not-applicable | medium |
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | preprint | QUBO | speculative | medium |

## Key Findings

- [supported] The paper does not report any original empirical quantum computing results in financial services; quantum computing is mentioned only as a future opportunity for risk modeling, optimization, and strategic planning. — [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]]
- [supported] The article’s reported findings focus on strategic automation in finance operations (e.g., RPA, AI, dashboards, cloud systems), claiming reduced processing times, fewer errors, and faster decision-making, but these claims are presented without paper-specific quantitative estimates or confidence intervals. — [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]]
- [supported] The implementation examples described in compensation administration, performance dashboards, incentive compensation, and executive reporting appear to be illustrative or synthesized case narratives rather than controlled empirical evaluations with reproducible quantitative benchmarks. — [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]]
- [supported] IQNN-CS is a hybrid classical-quantum multiclass credit scoring framework that combines a variational QNN with post-hoc interpretability methods and a new Inter-Class Attribution Alignment (ICAA) metric. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] All experiments were conducted on a quantum circuit simulator (PennyLane default.qubit) on CPU, not on real quantum hardware. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] On Dataset 1, the model achieved 100% accuracy and 1.00 F1-score for all three classes (Low, Average, High). — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] On Dataset 2, the model achieved 77.3% accuracy, with class-wise precision/recall/F1 of 0.64/0.97/0.77 for Low, 0.73/0.84/0.78 for Average, and 0.95/0.67/0.79 for High. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Training on Dataset 1 converged rapidly and stably, with accuracy stabilizing above 98% across train/validation/test splits and loss dropping sharply with minimal train-validation gap. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Training on Dataset 2 was unstable, with validation and test accuracy remaining below 80% and a persistent train-validation gap indicating weaker generalization and possible overfitting. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] t-SNE visualizations of quantum embeddings showed clear class separation for Dataset 1 but overlapping clusters, especially between Average and High classes, for Dataset 2. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Saliency-based attribution maps were concentrated and more interpretable for Dataset 1, while Dataset 2 produced diffuse and noisy attributions that varied across runs. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Occlusion analysis showed sharp confidence drops on Dataset 1 when top-ranked features were removed, suggesting reliance on a few informative features; Dataset 2 showed more gradual and less structured degradation. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] ICAA indicated lower inter-class attribution similarity for Dataset 1 and greater overlap in attribution logic for Dataset 2, suggesting less disentangled class reasoning on the harder dataset. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Attribution stability analysis under 20 Gaussian perturbations identified one indecisive case in Dataset 2 (sample 12, saliency std 0.2797 versus 0.1426 on Dataset 1), indicating unreliable class evidence for that sample. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] Example-based attribution using cosine similarity showed coherent same-class nearest training examples for Dataset 1, whereas Dataset 2 often matched highly similar examples from different classes, indicating ambiguous internal representations. — [[2026_Barbaresco_IqnnCsInterpretable]]
- [supported] The paper reformulates the subset sum problem as a QUBO and equivalent Ising optimization problem, enabling solution via Hopfield-network energy minimization. — [[2022_Biesner_SolvingSubsetSum]]
- [supported] A stochastic Hopfield-network gradient-descent algorithm reliably found correct subset-sum solutions on both artificial and real financial-table data within the tested setup. — [[2022_Biesner_SolvingSubsetSum]]
- [supported] On artificial datasets, the algorithm solved all tested samples for configurations up to n=128 across Xmax values of 1e4, 1e5, and 1e6, and also solved all tested samples for n=16, 32, and 64 in the reported configurations. — [[2022_Biesner_SolvingSubsetSum]]
- [supported] For the hardest reported artificial configuration (n=256, Xmax=1e6), the algorithm did not solve all samples within the run budget, finding solutions for 2 of 5 samples. — [[2022_Biesner_SolvingSubsetSum]]
- [supported] On real financial data parsed from a Deutsche Bank report, the algorithm found correct solutions for all 190 subset-sum instances across four table groups under the maximum iteration budget. — [[2022_Biesner_SolvingSubsetSum]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| QUBO | 2 |
| variational | 2 |
| quantum-ML | 2 |
| classical-simulation | 2 |
| quantum-annealing | 1 |
| VQE | 1 |
| grover | 1 |

## Open Questions

- Under what conditions can hybrid quantum-classical methods outperform advanced classical portfolio optimization techniques in practice? — [[2026_Gnal_QuantumComputingApproaches]]
- How much of the theoretical quantum advantage survives when realistic hardware noise and limited qubit resources are taken into account? — [[2026_Gnal_QuantumComputingApproaches]]
- Can quantum-enhanced sampling materially improve estimation of tail-risk measures such as VaR and CVaR for realistic portfolios? — [[2026_Gnal_QuantumComputingApproaches]]
- How scalable are QUBO-based and variational formulations when the asset universe grows to hundreds or thousands of securities? — [[2026_Gnal_QuantumComputingApproaches]]
- What are the most effective ways to encode portfolio constraints and uncertainty scenarios into quantum optimization frameworks? — [[2026_Gnal_QuantumComputingApproaches]]
- How should interpretability and transparency be ensured so that quantum-generated portfolio decisions satisfy regulatory and governance requirements? — [[2026_Gnal_QuantumComputingApproaches]]
- Which classes of market uncertainty or dependency structures are most likely to benefit from quantum methods? — [[2026_Gnal_QuantumComputingApproaches]]
- What validation standards and benchmarking protocols are needed for financial institutions to trust quantum-assisted optimization outputs? — [[2026_Gnal_QuantumComputingApproaches]]
- Develop and test practical hybrid quantum-classical portfolio optimization architectures. — [[2026_Gnal_QuantumComputingApproaches]]
- Address NISQ-era limitations such as hardware noise and limited scalability to improve feasibility. — [[2026_Gnal_QuantumComputingApproaches]]
