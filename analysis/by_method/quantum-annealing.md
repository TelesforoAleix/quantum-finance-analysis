# Quantum Annealing

**Papers:** 24 | **Empirical:** 4 | **Theoretical:** 5 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_C_AdvancingStockPrice]] | 2026 | peer-reviewed-empirical | high-frequency-trading, risk-modelling | demonstrated | high |
| [[2026_Gnal_QuantumComputingApproaches]] | 2026 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, market-simulation, regulatory-compliance | theoretical | high |
| [[2026_Gnal_ScenarioBasedMacroeconomic]] | 2026 | peer-reviewed-theoretical | risk-modelling, market-simulation | theoretical | high |
| [[2024_Ghysels_QuantumFinance]] | 2025 | other | portfolio-optimisation, asset-pricing, risk-modelling, derivatives-pricing, credit-scoring | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2025_Lai_TowardsArbitraryQubo]] | 2025 | peer-reviewed-empirical | — | not-applicable | low |
| [[2025_Vangibhuratha_QuantumMachineLearning]] | 2025 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2025_Wei_SolvingMultipleDiscretization]] | 2025 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | quantum-cryptography, high-frequency-trading | speculative | medium |
| [[2012_Dickson_AlgorithmicApproachAdiabatic]] | 2024 | preprint | portfolio-optimisation | speculative | medium |
| [[2024_KrishnaPasupuleti_QuantumAlgorithmsSolving]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation, risk-modelling, derivatives-pricing, high-frequency-trading | theoretical | high |
| [[2024_Unknown_QuantumMachineLearning]] | 2024 | peer-reviewed-theoretical | — | theoretical | medium |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, quantum-cryptography | speculative | medium |
| [[2023_S_PotentialQuantumTechniques]] | 2023 | preprint | asset-pricing | speculative | medium |
| [[2023_Shan_QuantumComputingSimulated]] | 2023 | conference-paper | portfolio-optimisation | speculative | high |
| [[2022_Albareti_StructuredSurveyQuantum]] | 2022 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, market-simulation, quantum-cryptography | speculative | high |
| [[2021_OwhadiKareshk_PortfolioOptimizationClassical]] | 2021 | preprint | portfolio-optimisation | speculative | high |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | asset-pricing, fraud-detection, credit-scoring, high-frequency-trading, derivatives-pricing, risk-modelling | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | speculative | medium |
| [[2019_Li_ResearchQuantumComputing]] | 2019 | conference-paper | quantum-cryptography | speculative | medium |
| [[2016_Isakov_UnderstandingQuantumTunneling]] | 2015 | preprint | — | speculative | low |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 15 |
| risk-modelling | 12 |
| derivatives-pricing | 7 |
| asset-pricing | 6 |
| quantum-cryptography | 6 |
| high-frequency-trading | 5 |
| market-simulation | 4 |
| credit-scoring | 4 |
| fraud-detection | 3 |
| regulatory-compliance | 1 |

## Key Findings

- [supported] The proposed hybrid QML-HFT framework reports 92.5% prediction accuracy, outperforming the baselines listed in the paper: QSVM at 85.4%, QA at 83.5%, and PCA at 82.1%. — [[2026_C_AdvancingStockPrice]]
- [supported] The framework reports 93.57% execution speed/latency improvement, compared with 41.2% for QSVM, 57.8% for QA, and 64.3% for PCA in the paper's comparison table. — [[2026_C_AdvancingStockPrice]]
- [supported] The framework reports 95.15% risk management efficiency, exceeding the paper's reported baseline values of 43.59% (QSVM), 63.79% (QA), and 84.15% (PCA). — [[2026_C_AdvancingStockPrice]]
- [supported] In the ablation study, QNN-only achieved 90.1% accuracy with 5.8 seconds processing time, QSVM-only achieved 85.4% accuracy with 6.2 seconds, and QA-only achieved 83.5% accuracy with 8.1 seconds; the full hybrid model achieved the best reported accuracy at 92.5%. — [[2026_C_AdvancingStockPrice]]
- [supported] The authors report that QSVM achieved 92.5% accuracy versus 87.3% for an LSTM baseline, and state that the difference in accuracy and speed was statistically significant with paired t-test p = 0.01. — [[2026_C_AdvancingStockPrice]]
- [supported] The paper reports a paired t-test p-value of 0.02 for improvement in execution speed and accuracy between quantum and conventional models, and an ANOVA p-value of 0.03 across models, indicating statistical significance at the 95% confidence level. — [[2026_C_AdvancingStockPrice]]
- [supported] Results were obtained using both simulation and real hardware: IBM Qiskit simulator on a classical Intel Core i7/32 GB RAM system, and IBM Falcon 5-qubit and IBM Eagle 16-qubit quantum processors. — [[2026_C_AdvancingStockPrice]]
- [supported] The study used a Kaggle stock market dataset with OHLC, adjusted close, and volume data; preprocessing included forward-filling missing values, Z-score-based outlier removal, technical indicators such as MA and RSI, Min-Max scaling for price features, log scaling for volume, and an 80/20 train-test split. — [[2026_C_AdvancingStockPrice]]
- [supported] The paper claims the hybrid model combines linear separability from QSVM, nonlinear feature extraction from QNN, and optimization from QA, and that this combination produced the strongest reported performance in the study. — [[2026_C_AdvancingStockPrice]]
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance — [[2024_Ghysels_QuantumFinance]]
- [supported] An unsupervised feedforward neural network (FNN) optimizer achieved over 99% average accuracy on dense 80-variable weighted MaxCut and random QUBO problems in less than 1.1 s on an 8-core CPU. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] On 200-variable random QUBO problems with a 100 s computation limit, the FNN outperformed Gurobi by 72% in objective value according to the paper's reported benchmark. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] For 15-variable benchmarks over 100 instances, QCED reached lower mean percentage errors than FNN after 500 training iterations: MaxCut 0.95% vs 1.46%, random QUBO 0.197% vs 0.826%, MWIS 6.7% vs 7.53%, and 4-city TSP 2.99% vs 5.17%. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] Across scaling tests up to 40 variables, both FNN and QCED maintained low errors on MaxCut and random QUBO, while both degraded substantially on MWIS and TSP as problem size increased. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] Layer-activity analysis showed the encoder in the hybrid quantum-classical encoder-decoder (QCED) remained effectively inactive during training, while the decoder was active, indicating the quantum layer was effectively deactivated. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] Because the quantum layer in QCED was inactive, the hybrid architecture provided no tangible optimization benefit over a simpler classical FNN in the authors' experiments. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] In large-instance benchmarks, post-processed FNN achieved the best reported average objective values among compared solvers for MaxCut and random QUBO at 80 and 200 variables. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] For 80-variable MaxCut and random QUBO, FNN runtime was under 1.1 s and used approximately 1/200 and 1/1200 of Gurobi's time, respectively, while achieving about 99.5% accuracy and nearly identical cost values. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] FNN performed poorly relative to Gurobi on MWIS, reaching only 78.14% accuracy on 80-variable MWIS in 2.3 s, whereas Gurobi solved the instance in about 0.2 s. — [[2025_Lai_TowardsArbitraryQubo]]
- [supported] The D-Wave Advantage annealer optimized 80-variable random QUBOs effectively with accuracy close to post-processed FNN, but struggled on other problem classes and could not handle 200-variable instances due to embedding failure. — [[2025_Lai_TowardsArbitraryQubo]]
