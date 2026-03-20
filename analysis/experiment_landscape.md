# Experiment Landscape

Summary of experimental approaches across the quantum finance literature.

Generated: 2026-03-20

## Summary

- Papers with experiment details: 39 / 69 total
- Most common experimental setup: Qiskit simulator
- Most common hardware: simulator (28 papers), real QPU (2 papers)

## Experiments by Topic

### Asset Pricing (9 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | 10 | Qiskit simulator | Synthetic problem instances were used, including:
 |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | VQE, Variational | 14 | Qiskit simulator | {'Black-Scholes_equation': {'risk_free_rate': 0.04 |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | — | 4 | Qiskit simulator | {'qGAN': {'source': 'Binance API', 'size': 'Over 5 |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | QNN | 4 | Qiskit simulator | {'source': 'Yahoo Finance via yfinance Python libr |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | QNN | — | Simulator (unspecified) | {'source': 'TOPIX500 index constituents, Japanese  |
| [[2024_M_OptimizingMutualFund]] | 2024 | QNN | — | — | Data parameters included growth percentage, total  |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | — | 7 | PennyLane | For the Cora dataset: 2,708 nodes with 1,433 featu |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | QAOA, VQE | — | — | N/A |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | Variational | — | Simulator (unspecified) | {'diffusion_equation': {'source': 'Synthetic', 'si |

### Credit Scoring (4 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | QAOA | 4 | Simulator (unspecified) | {'portfolio_optimization': {'source': 'German DAX  |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | Variational | — | PennyLane | {'4-bit_parity_problem': {'source': 'Synthetic dat |

### Derivatives Pricing (9 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | Grover, Amplitude Estimation | 6 | Qiskit simulator | Historical AAPL data covering 2022-01-02 to 2024-0 |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | 10 | Qiskit simulator | Synthetic problem instances were used, including:
 |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | VQE, Variational | 14 | Qiskit simulator | {'Black-Scholes_equation': {'risk_free_rate': 0.04 |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | Amplitude Estimation | — | Cirq | {'source': 'Synthetic data generated based on mode |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | Amplitude Estimation | 6 | Simulator (unspecified) | {'European_call_option': {'parameters': {'spot_pri |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | Variational | — | Simulator (unspecified) | {'diffusion_equation': {'source': 'Synthetic', 'si |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | Amplitude Estimation | — | Qiskit simulator | For the demonstration, the input is a simple trigo |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | Grover, Amplitude Estimation | — | Qiskit simulator | Input parameters for the simulations included init |

### Fraud Detection (7 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | QAOA | 4 | Simulator (unspecified) | {'portfolio_optimization': {'source': 'German DAX  |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | — | 4 | Qiskit simulator | {'qGAN': {'source': 'Binance API', 'size': 'Over 5 |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | QUBO | — | — | {'artificial_data': {'source': 'Uniformly sampled  |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | Variational | — | PennyLane | {'4-bit_parity_problem': {'source': 'Synthetic dat |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | Grover | — | Simulator (unspecified) | N/A |

### High Frequency Trading (7 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | QAOA, Grover, QUBO | 14 | Qiskit simulator | {'source': 'Synthetic VRP instances generated for  |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | — | 4 | Qiskit simulator | {'qGAN': {'source': 'Binance API', 'size': 'Over 5 |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | QNN | 4 | Qiskit simulator | {'source': 'Yahoo Finance via yfinance Python libr |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | QAOA, VQE | — | — | N/A |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | Grover | — | Simulator (unspecified) | N/A |

### Market Simulation (1 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | 10 | Qiskit simulator | Synthetic problem instances were used, including:
 |

### Portfolio Optimisation (27 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2025_Autonomous_QAOA]] | 2026 | QAOA | 5 | Qiskit simulator | {'source': 'Yahoo Finance via yfinance Python libr |
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | QAOA, Grover, QUBO | 14 | Qiskit simulator | {'source': 'Synthetic VRP instances generated for  |
| [[2026_Barbaresco_QPortQuantum]] | 2026 | QAOA, VQE, QUBO | 12 | Simulator (unspecified) | Historical stock prices for 3, 4, and 12 stocks ov |
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | QAOA | 4 | Simulator (unspecified) | {'portfolio_optimization': {'source': 'German DAX  |
| [[2026_Ganguly_AutonomousQuantumAgents]] | 2026 | QAOA | 5 | Qiskit simulator | {'source': 'Yahoo Finance via yfinance Python libr |
| [[2025_Aggarwal_BridgingQuantumAlgorithms]] | 2025 | QAOA, QUBO | — | Qiskit simulator | The dataset includes monthly turnover figures for  |
| [[2025_Bhattacharyya_SolvingGeneralQubos]] | 2025 | QAOA, QUBO | 17 | Simulator (unspecified) | {'random_qubos': {'source': 'Synthetically generat |
| [[2025_Cai_EnhancingQuantumApproximate]] | 2025 | QAOA, Variational | 6 | Qiskit simulator | {'source': 'Erdos-Renyi random graphs generated us |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | — | 4 | Qiskit simulator | {'qGAN': {'source': 'Binance API', 'size': 'Over 5 |
| [[2025_Innan_QuantumPortfolioOptimization]] | 2025 | QAOA, VQE, QUBO | — | Qiskit simulator | {'source': 'Yahoo Finance', 'size': '10 assets (4  |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2025_Uotila_HigherOrderPortfolio]] | 2025 | QAOA | 6 | Qiskit simulator | {'source': 'Downloaded from Yahoo Finance using th |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | QNN | — | Simulator (unspecified) | {'source': 'TOPIX500 index constituents, Japanese  |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | — | — | — | {'source': 'Kaggle', 'dataset_description': 'Histo |
| [[2024_Chou_QutritBasedQuantum]] | 2024 | — | — | Simulator (unspecified) | {'source': 'DJIA index', 'time_period': '2013-2022 |
| [[2024_Leipold_TrainScalingQuantum]] | 2024 | QAOA | 30 | Simulator (unspecified) | {'source': 'Kaggle (publicly available S&P 500 sto |
| [[2024_M_OptimizingMutualFund]] | 2024 | QNN | — | — | Data parameters included growth percentage, total  |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | — | 7 | PennyLane | For the Cora dataset: 2,708 nodes with 1,433 featu |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |
| [[2025_Huot_CorrectionsEnhancingKnapsack]] | 2024 | QAOA | — | Simulator (unspecified) | Expected returns from Markowitz analysis, mapped t |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | QAOA, Quantum Annealing, QUBO | — | Qiskit simulator | {'knapsack_problem': {'source': 'Synthetic dataset |
| [[2023_Shan_QuantumComputingSimulated]] | 2023 | Quantum Annealing, QUBO | — | Simulator (unspecified) | Stock purchase and sale prices, binary variables f |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | QAOA, VQE | — | — | N/A |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, Variational | — | Qiskit simulator | {'Max-Cut': {'source': 'Random non-regular unweigh |
| [[2022_Sun_PortfolioOptimizationBased]] | 2022 | HHL | 9 | Qiskit simulator | {'source': 'Synthetic data generated for the study |
| [[2019_Kerenidis_QuantumAlgorithmsPortfolio]] | 2019 | — | — | — | Subsampled dataset of 50 companies from the S&P 50 |
| [[2012_Dickson_AlgorithmicApproachAdiabatic]] | 2011 | — | 64 | D-Wave | The input consists of 64-node graphs with a unique |

### Quantum ML (2 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | — | — | — | {'source': 'Kaggle', 'dataset_description': 'Histo |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | — | 7 | PennyLane | For the Cora dataset: 2,708 nodes with 1,433 featu |

### Quantum Cryptography (1 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |

### Regulatory Compliance (1 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | QUBO | — | — | {'artificial_data': {'source': 'Uniformly sampled  |

### Risk Modelling (11 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | QAOA | 4 | Simulator (unspecified) | {'portfolio_optimization': {'source': 'German DAX  |
| [[2025_Cai_EnhancingQuantumApproximate]] | 2025 | QAOA, Variational | 6 | Qiskit simulator | {'source': 'Erdos-Renyi random graphs generated us |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | — | 4 | Qiskit simulator | {'qGAN': {'source': 'Binance API', 'size': 'Over 5 |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, VQE, Variational | 105 | IBM Quantum (real) | {'source': 'Synthetic benchmarks compiled from rel |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | {'MNIST': {'description': 'Handwritten digit image |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | QAOA, Quantum Annealing, QUBO | — | Qiskit simulator | {'knapsack_problem': {'source': 'Synthetic dataset |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | QAOA, VQE | — | — | N/A |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, Variational | — | Qiskit simulator | {'Max-Cut': {'source': 'Random non-regular unweigh |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | Amplitude Estimation | 6 | Simulator (unspecified) | {'European_call_option': {'parameters': {'spot_pri |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | Amplitude Estimation | — | Qiskit simulator | For the demonstration, the input is a simple trigo |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | Grover, Amplitude Estimation | — | Qiskit simulator | Input parameters for the simulations included init |

## Hardware Distribution

| Hardware Type | Papers |
|---------------|--------|
| Qiskit simulator | 17 |
| Simulator (unspecified) | 11 |
| PennyLane | 2 |
| IBM Quantum (real) | 2 |
| D-Wave | 1 |
| Cirq | 1 |

## Dataset Catalog

| Dataset | Used By | Papers |
|---------|---------|--------|
| {'source': 'Yahoo Finance via yfinance P... | asset-pricing, high-frequency-trading, portfolio-optimisation | 3 |
| N/A | asset-pricing, fraud-detection, high-frequency-trading, portfolio-optimisation, risk-modelling | 2 |
| The input consists of 64-node graphs wit... | portfolio-optimisation | 1 |
| Input parameters for the simulations inc... | derivatives-pricing, risk-modelling | 1 |
| Subsampled dataset of 50 companies from... | portfolio-optimisation | 1 |
| For the demonstration, the input is a si... | derivatives-pricing, risk-modelling | 1 |
| {'Max-Cut': {'source': 'Random non-regul... | portfolio-optimisation, risk-modelling | 1 |
| {'European_call_option': {'parameters':... | derivatives-pricing, risk-modelling | 1 |
| {'artificial_data': {'source': 'Uniforml... | fraud-detection, regulatory-compliance | 1 |
| {'4-bit_parity_problem': {'source': 'Syn... | credit-scoring, fraud-detection | 1 |
| {'source': 'Synthetic data generated for... | portfolio-optimisation | 1 |
| {'diffusion_equation': {'source': 'Synth... | asset-pricing, derivatives-pricing | 1 |
| {'knapsack_problem': {'source': 'Synthet... | portfolio-optimisation, risk-modelling | 1 |
| {'source': 'TOPIX500 index constituents,... | asset-pricing, portfolio-optimisation | 1 |
| Stock purchase and sale prices, binary v... | portfolio-optimisation | 1 |
| {'source': 'Kaggle', 'dataset_descriptio... | portfolio-optimisation, quantum-ML | 1 |
| {'source': 'DJIA index', 'time_period':... | portfolio-optimisation | 1 |
| {'source': 'Kaggle (publicly available S... | portfolio-optimisation | 1 |
| Data parameters included growth percenta... | asset-pricing, portfolio-optimisation | 1 |
| For the Cora dataset: 2,708 nodes with 1... | asset-pricing, portfolio-optimisation, quantum-ML | 1 |
| The dataset includes monthly turnover fi... | portfolio-optimisation | 1 |
| {'random_qubos': {'source': 'Synthetical... | portfolio-optimisation | 1 |
| {'source': 'Erdos-Renyi random graphs ge... | portfolio-optimisation, risk-modelling | 1 |
| {'Black-Scholes_equation': {'risk_free_r... | asset-pricing, derivatives-pricing | 1 |
| {'source': 'Synthetic data generated bas... | derivatives-pricing | 1 |
| {'MNIST': {'description': 'Handwritten d... | credit-scoring, fraud-detection, high-frequency-trading, portfolio-optimisation, quantum-cryptography, risk-modelling | 1 |
| {'qGAN': {'source': 'Binance API', 'size... | asset-pricing, fraud-detection, high-frequency-trading, portfolio-optimisation, risk-modelling | 1 |
| Expected returns from Markowitz analysis... | portfolio-optimisation | 1 |
| {'source': 'Yahoo Finance', 'size': '10... | portfolio-optimisation | 1 |
| {'source': 'Synthetic benchmarks compile... | credit-scoring, derivatives-pricing, fraud-detection, high-frequency-trading, portfolio-optimisation, risk-modelling | 1 |
| {'source': 'Downloaded from Yahoo Financ... | portfolio-optimisation | 1 |
| {'source': 'Synthetic VRP instances gene... | high-frequency-trading, portfolio-optimisation | 1 |
| Historical stock prices for 3, 4, and 12... | portfolio-optimisation | 1 |
| Historical AAPL data covering 2022-01-02... | derivatives-pricing | 1 |
| {'portfolio_optimization': {'source': 'G... | credit-scoring, fraud-detection, portfolio-optimisation, risk-modelling | 1 |
| Synthetic problem instances were used, i... | asset-pricing, derivatives-pricing, market-simulation | 1 |

## Methodology Gaps

- Topics with no experiment details: none
- Methods tested only in simulation: HHL, amplitude-estimation, classical-simulation, grover, hybrid-approach, quantum-simulation
- Papers with "demonstrated" QA claim but simulation-only: none
- Topics where all QA claims are "speculative": quantum-ML
