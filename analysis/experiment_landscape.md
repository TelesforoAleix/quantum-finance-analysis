# Experiment Landscape

Summary of experimental approaches across the quantum finance literature.

Generated: 2026-03-25

## Summary

- Papers with experiment details: 105 / 155 total
- Most common experimental setup: Simulator (unspecified)
- Most common hardware: simulator (71 papers), real QPU (7 papers)

## Experiments by Topic

### Asset Pricing (11 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | — | Qiskit simulator | Model-generated inputs rather than a fixed dataset |
| [[2025_Choudhary_HqnnFspHybrid]] | 2025 | QNN | — | Qiskit simulator | Input data consisted of historical stock prices wi |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | QUBO, Variational | — | Qiskit simulator | For qGAN, Binance API data for five cryptocurrenci |
| [[2025_Vellaipandiyan_HybridQlstmFramework]] | 2025 | QNN, Variational | 4 | Simulator (unspecified) | Yahoo Finance AAPL daily stock data, 1,508 observa |
| [[2023_Kobayashi_CrossSectionalStock]] | 2024 | QNN | 10 | Simulator (unspecified) | Input universe: TOPIX500 constituent stocks in Jap |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | Quantum Kernel | — | — | Input data is described as a Kaggle financial stoc |
| [[2024_Kea_HybridQuantumClassical]] | 2024 | Variational | 7 | IBM Quantum (real) | Single-company stock time-series dataset from Appl |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | — | 7 | PennyLane | Cora dataset: undirected citation graph with 2,708 |
| [[2023_S_PotentialQuantumTechniques]] | 2023 | Quantum Annealing, QUBO, Quantum Kernel | — | Qiskit simulator | Input data consisted of daily stock prices for AAP |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | — | 5 | Qiskit simulator | Input consists of normalized covariance/cross-corr |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |

### Credit Scoring (6 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2025_Minati_QuantumPoweredCredit]] | 2025 | — | — | Simulator (unspecified) | Input data consists of >25,000 bank loan samples w |
| [[2025_Mustapha_ComparativeAnalysisLoan]] | 2025 | Quantum SVM, Quantum Kernel | 12 | Qiskit simulator | Kaggle credit risk dataset with about 12,638 rows  |
| [[2026_Barbaresco_IqnnCsInterpretable]] | 2025 | QNN, Variational | 6 | PennyLane | Input data consisted of two Kaggle credit score cl |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | Variational | — | Qiskit simulator | Churn prediction input: proprietary bank dataset w |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | Illustrative datasets mentioned include MNIST (28x |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |

### Derivatives Pricing (16 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Barbaresco_QuantumAmplitudeEstimation]] | 2026 | Grover, Amplitude Estimation | 6 | Qiskit simulator | Input data consisted of historical AAPL data from  |
| [[2026_Dechant_ErrorResourceEstimates]] | 2026 | Variational | — | — | Two problem inputs are used for numerical illustra |
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | — | Qiskit simulator | Model-generated inputs rather than a fixed dataset |
| [[2025_Chaudhary_PracticalQuantumSolver]] | 2025 | VQE | 2 | Qiskit simulator | Problem instances are generated from discretized P |
| [[2025_Cibrario_AutocallableOptionsPricing]] | 2025 | Amplitude Estimation | 33 | Cirq | Synthetic single-asset autocallable option instanc |
| [[2023_Cherrat_QuantumDeepHedging]] | 2023 | QNN | 16 | Simulator (unspecified) | Classical-environment input: synthetic GBM stock-p |
| [[2023_Udvarnoki_QuantumAdvantageMonte]] | 2023 | Grover, Amplitude Estimation | 2 | Qiskit simulator | Synthetic European call option instances under Bla |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | Amplitude Estimation | 6 | Simulator (unspecified) | Two main inputs were used. (1) Vanilla European ca |
| [[2022_Ferro_DEvaluationQuantum]] | 2022 | Amplitude Estimation | 5 | Simulator (unspecified) | Synthetic option pricing instances under a Black–S |
| [[2022_Saha_IntermediateQutritBased]] | 2022 | Amplitude Estimation, Variational | 0 | IBM Quantum (real) | Inputs consist of (1) symbolic/arithmetic circuit  |
| [[2022_Zhao_QuantumInspiredVariational]] | 2022 | Variational | 5 | Simulator (unspecified) | Synthetic numerical inputs rather than observation |
| [[2020_Tang_QuantumComputationPricing]] | 2021 | Amplitude Estimation | 4 | Qiskit simulator | Example CDO input consists of 4 assets with parame |
| [[2021_Martin_TowardPricingFinancial]] | 2021 | — | 5 | Qiskit simulator | Input consists of normalized covariance/cross-corr |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | Grover, Amplitude Estimation | — | Simulator (unspecified) | Synthetic Black-Scholes-Merton option-pricing inpu |
| [[2025_Kao_MixedSignalQuantum]] | — | Amplitude Estimation | 12 | Qiskit simulator | Synthetic experiment inputs rather than historical |

### Fraud Detection (4 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | Variational | — | Qiskit simulator | Churn prediction input: proprietary bank dataset w |
| [[2024_Mitsuda_ApproximateComplexAmplitude]] | 2024 | Variational | 5 | IBM Quantum (real) | Iris experiment: 4 features per sample (sepal leng |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | Illustrative datasets mentioned include MNIST (28x |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |

### High Frequency Trading (3 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_C_AdvancingStockPrice]] | 2026 | Quantum Annealing, QNN | — | Qiskit simulator | Input data consisted of historical daily stock pri |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | Illustrative datasets mentioned include MNIST (28x |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |

### Market Simulation (4 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | Amplitude Estimation, Variational | — | Qiskit simulator | Model-generated inputs rather than a fixed dataset |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | QUBO, Variational | — | Qiskit simulator | For qGAN, Binance API data for five cryptocurrenci |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | — | 7 | PennyLane | Cora dataset: undirected citation graph with 2,708 |
| [[2021_Coyle_QuantumVersusClassical]] | 2021 | — | — | Rigetti | Financial input data consisted of 5070 samples of  |

### Portfolio Optimisation (44 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2025_Autonomous_QAOA]] | 2026 | QAOA | 5 | Qiskit simulator | {'source': 'Yahoo Finance via yfinance Python libr |
| [[2026_Barbaresco_QPortQuantum]] | 2026 | QAOA, VQE, QUBO | 9 | Simulator (unspecified) | Yahoo Finance historical stock prices from 2020-01 |
| [[2026_Dehn_ExtrapolationMethodOptimize]] | 2026 | QAOA, QUBO, Variational | 28 | Qiskit simulator | Portfolio optimization: annualized returns and cov |
| [[2026_Ganguly_AutonomousQuantumAgents]] | 2026 | QAOA, QUBO, Variational | 5 | Qiskit simulator | Yahoo Finance daily closing prices for 5 assets (A |
| [[2026_Khan_QamooQuantumApproximate]] | 2026 | QAOA, QUBO, Variational | 42 | IBM Quantum (real) | Financial input consists of stock data S = {(mu_i, |
| [[2024_Tancara_HighDimensionalCounterdiabatic]] | 2025 | — | — | — | Inputs include: multiway number partitioning insta |
| [[2024_Yoshioka_ElectricPowerDemand]] | 2025 | QAOA, Variational | 20 | Simulator (unspecified) | Input data consisted of residential electricity us |
| [[2025_Aggarwal_BridgingQuantumAlgorithms]] | 2025 | QAOA, QUBO | — | Qiskit simulator | Input data consists of monthly NSE derivatives tur |
| [[2025_Bhattacharyya_SolvingGeneralQubos]] | 2025 | QAOA, QUBO | — | Simulator (unspecified) | Problem inputs were synthetically generated as fol |
| [[2025_Ganguly_HybridClassicalQuantum]] | 2025 | QUBO, Variational | — | Qiskit simulator | For qGAN, Binance API data for five cryptocurrenci |
| [[2025_Huot_CorrectionsEnhancingKnapsack]] | 2025 | QAOA | — | Simulator (unspecified) | N/A |
| [[2025_Innan_QuantumPortfolioOptimization]] | 2025 | QAOA, QUBO, Variational | — | Qiskit simulator | Input data consisted of Yahoo Finance stock prices |
| [[2025_Matsakos_QuantumUnstructuredSearch]] | 2025 | Grover, QUBO | 4 | Qiskit simulator | A manually constructed 4-asset portfolio optimizat |
| [[2025_Soloviev_ScalingPortfolioDiversification]] | 2025 | QAOA, Variational | 71 | Simulator (unspecified) | Main financial experiment: S&P 500 stock-price tim |
| [[2025_Uotila_HigherOrderPortfolio]] | 2025 | QAOA, QUBO | 6 | Simulator (unspecified) | Input data consisted of daily stock prices for DJI |
| [[2025_Wei_SolvingMultipleDiscretization]] | 2025 | Quantum Annealing, QUBO | 50 | D-Wave | Input data consisted of historical daily closing p |
| [[2012_Dickson_AlgorithmicApproachAdiabatic]] | 2024 | — | 64 | D-Wave | Primary input data are 64-node synthetic graph ins |
| [[2022_Dalzell_EndEndResource]] | 2024 | — | — | — | Financial input consists of randomly sampled stock |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | Quantum Kernel | — | — | Input data is described as a Kaggle financial stoc |
| [[2024_Carrascal_BacktestingQuantumComputing]] | 2024 | QAOA, VQE, Grover | 5 | Qiskit simulator | Primary input: IBEX35 adjusted closing prices from |
| [[2024_Chou_QutritBasedQuantum]] | 2024 | — | — | — | DJIA stock market data from the U.S. over 2013-202 |
| [[2024_Leipold_TrainScalingQuantum]] | 2024 | QAOA | — | Simulator (unspecified) | Input data consists of historical S&P 500 daily st |
| [[2024_M_OptimizingMutualFund]] | 2024 | QNN | — | Simulator (unspecified) | Company/investment portfolio data with features in |
| [[2024_Sharma_QuantumRelaxationSolving]] | 2024 | QAOA, VQE, Variational | 63 | Qiskit simulator | For ansatz selection, 20 small MKP instances were  |
| [[2024_Yu_ImprovedQuantumApproximate]] | 2024 | QAOA, QUBO, Variational | — | Simulator (unspecified) | Historical Nasdaq stock data for 16 named stocks s |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | Illustrative datasets mentioned include MNIST (28x |
| [[2023_Dehn_HybridQuantumClassical]] | 2023 | QAOA, QUBO | 10 | Simulator (unspecified) | Primary inputs are randomly generated portfolio in |
| [[2023_Giron_ApproachingCollateralOptimization]] | 2023 | QUBO | 350 | D-Wave | Knapsack input: a literature-based 10-item instanc |
| [[2023_Shan_QuantumComputingSimulated]] | 2023 | Quantum Annealing, QUBO | — | Simulator (unspecified) | Input consists of stock purchase prices, sale pric |
| [[2023_Vishwakarma_QuantumComputingAlgorithms]] | 2023 | QAOA, VQE | — | Simulator (unspecified) | Inputs are described only at a conceptual level: c |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | QAOA, Grover, Quantum Walk | — | Simulator (unspecified) | CVRP: synthetic instance with l=10 locations, solu |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, Variational | 20 | Qiskit simulator | Inputs consisted of three classes of optimization  |
| [[2022_Hegade_PortfolioOptimizationDigitized]] | 2022 | QAOA, QUBO, Variational | 14 | Real QPU (unspecified) | Input data are randomly generated portfolio instan |
| [[2022_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, QUBO | 20 | Qiskit simulator | Inputs consisted of optimization instances encoded |
| [[2022_Sun_PortfolioOptimizationBased]] | 2022 | HHL | 9 | Qiskit simulator | Synthetic portfolio instance with 3 assets. Expect |
| [[2022_Wang_ClassicallyBoostedQuantum]] | 2022 | QAOA, Quantum Walk, Variational | — | Simulator (unspecified) | Two synthetic instance sets were generated. Max 3S |
| [[2021_DezValle_QuantumVariationalOptimization]] | 2021 | VQE, QUBO, Variational | 12 | — | Input consists of randomly generated QUBO problems |
| [[2021_Egger_WarmStartingQuantum]] | 2021 | QAOA, QUBO, Variational | — | Qiskit simulator | Portfolio optimization: synthetic daily price seri |
| [[2021_FernndezLorenzo_HybridQuantumClassical]] | 2021 | QAOA, VQE, QUBO | — | D-Wave | Financial input consists of intraday prices P_j(t) |
| [[2021_Hegade_PortfolioOptimizationDigitized]] | 2021 | QAOA, QUBO, Variational | — | Simulator (unspecified) | Input instances are randomly generated portfolio o |
| [[2021_OwhadiKareshk_PortfolioOptimizationClassical]] | 2021 | Quantum Annealing, QUBO | — | D-Wave | Input data consist of daily historical prices for  |
| [[2021_Slate_QuantumWalkBased]] | 2021 | QAOA, Quantum Walk, Variational | 16 | Simulator (unspecified) | Input consisted of two 8-asset stock-price dataset |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |
| [[2019_Kerenidis_QuantumAlgorithmsPortfolio]] | 2019 | HHL | — | Simulator (unspecified) | Financial input consists of historical daily retur |

### Quantum Cryptography (1 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |

### Regulatory Compliance (3 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]] | 2025 | — | — | — | The implied inputs are enterprise financial-proces |
| [[2026_Barbaresco_IqnnCsInterpretable]] | 2025 | QNN, Variational | 6 | PennyLane | Input data consisted of two Kaggle credit score cl |
| [[2022_Biesner_SolvingSubsetSum]] | 2022 | QUBO | — | Simulator (unspecified) | Artificial data: for each configuration, n integer |

### Risk Modelling (24 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Barbaresco_QPortQuantum]] | 2026 | QAOA, VQE, QUBO | 9 | Simulator (unspecified) | Yahoo Finance historical stock prices from 2020-01 |
| [[2026_C_AdvancingStockPrice]] | 2026 | Quantum Annealing, QNN | — | Qiskit simulator | Input data consisted of historical daily stock pri |
| [[2026_Khan_QamooQuantumApproximate]] | 2026 | QAOA, QUBO, Variational | 42 | IBM Quantum (real) | Financial input consists of stock data S = {(mu_i, |
| [[2024_Yoshioka_ElectricPowerDemand]] | 2025 | QAOA, Variational | 20 | Simulator (unspecified) | Input data consisted of residential electricity us |
| [[2025_GauthamPanneerSelvam_DrivingOperationalEfficiency]] | 2025 | — | — | — | The implied inputs are enterprise financial-proces |
| [[2025_Mustapha_ComparativeAnalysisLoan]] | 2025 | Quantum SVM, Quantum Kernel | 12 | Qiskit simulator | Kaggle credit risk dataset with about 12,638 rows  |
| [[2023_Thakkar_ImprovedFinancialForecasting]] | 2024 | Variational | — | Qiskit simulator | Churn prediction input: proprietary bank dataset w |
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | Quantum Kernel | — | — | Input data is described as a Kaggle financial stoc |
| [[2024_Chou_QutritBasedQuantum]] | 2024 | — | — | — | DJIA stock market data from the U.S. over 2013-202 |
| [[2024_Sharma_QuantumRelaxationSolving]] | 2024 | QAOA, VQE, Variational | 63 | Qiskit simulator | For ansatz selection, 20 small MKP instances were  |
| [[2024_Yu_ImprovedQuantumApproximate]] | 2024 | QAOA, QUBO, Variational | — | Simulator (unspecified) | Historical Nasdaq stock data for 16 named stocks s |
| [[2025_Deshmukh_QuantumMachineLearning]] | 2024 | QAOA, VQE, QNN | — | IBM Quantum (real) | Illustrative datasets mentioned include MNIST (28x |
| [[2023_Cherrat_QuantumDeepHedging]] | 2023 | QNN | 16 | Simulator (unspecified) | Classical-environment input: synthetic GBM stock-p |
| [[2023_Dehn_HybridQuantumClassical]] | 2023 | QAOA, QUBO | 10 | Simulator (unspecified) | Primary inputs are randomly generated portfolio in |
| [[2021_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, Variational | 20 | Qiskit simulator | Inputs consisted of three classes of optimization  |
| [[2021_Stamatopoulos_TowardsQuantumAdvantage]] | 2022 | Amplitude Estimation | 6 | Simulator (unspecified) | Two main inputs were used. (1) Vanilla European ca |
| [[2022_Ferro_DEvaluationQuantum]] | 2022 | Amplitude Estimation | 5 | Simulator (unspecified) | Synthetic option pricing instances under a Black–S |
| [[2022_Kolotouros_EvolvingObjectiveFunction]] | 2022 | QAOA, VQE, QUBO | 20 | Qiskit simulator | Inputs consisted of optimization instances encoded |
| [[2020_Tang_QuantumComputationPricing]] | 2021 | Amplitude Estimation | 4 | Qiskit simulator | Example CDO input consists of 4 assets with parame |
| [[2019_Miyamoto_ReductionQubitsQuantum]] | 2020 | Amplitude Estimation | — | Qiskit simulator | Synthetic integration problem: I = (1/theta^Nvar)  |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | QAOA, HHL, Grover | 2 | Qiskit simulator | Inputs vary by example: (1) synthetic Boolean orac |
| [[2020_Milek_QuantumImplementationRisk]] | 2020 | Amplitude Estimation | 7 | Simulator (unspecified) | Synthetic inputs only. Copula variables are discre |
| [[2020_Miyamoto_ReductionQubitsQuantum]] | 2020 | Grover, Amplitude Estimation | — | Qiskit simulator | Synthetic input only: estimation of the integral I |
| [[2018_Rebentrost_QuantumComputationalFinance]] | 2018 | Grover, Amplitude Estimation | — | Simulator (unspecified) | Synthetic Black-Scholes-Merton option-pricing inpu |

### Untagged (28 experiments)

| Paper | Year | Algorithm | Qubits | Hardware | Dataset |
|-------|------|-----------|--------|----------|---------|
| [[2026_Azfar_ShallowRobustQaoa]] | 2026 | QAOA, Grover, QUBO | 30 | Qiskit simulator | Input consists of synthetic vehicle routing proble |
| [[2026_Li_HarnessingBayesianStatistics]] | 2026 | VQE, Grover, Amplitude Estimation | — | Qiskit simulator | Amplitude-estimation benchmarks use prescribed amp |
| [[2025_Azadi_QuantumMonteCarlo]] | 2025 | Variational | — | Simulator (unspecified) | Input consists of synthetic/physics-simulation con |
| [[2025_Cai_EnhancingQuantumApproximate]] | 2025 | QAOA, Variational | 26 | Qiskit simulator | Input instances consisted of unweighted Max-Cut gr |
| [[2025_Gibadullin_QuantumAlgorithmsSolving]] | 2025 | QAOA, VQE, Grover | — | — | Synthetic inputs only: initial state x0 = 0.0, tim |
| [[2025_Jiang_RasenganTransitionHamiltonian]] | 2025 | QAOA, Variational | 127 | Qiskit simulator | Benchmark instances from literature for five const |
| [[2025_Lai_TowardsArbitraryQubo]] | 2025 | Quantum Annealing, QUBO | 4 | D-Wave | Synthetic generated instances only. For comparativ |
| [[2025_Tang_DeepQuantumMonte]] | 2025 | Variational | — | Simulator (unspecified) | Synthetic ab initio inputs rather than a tabular d |
| [[2025_Zhang_QuantumComputingQuantum]] | 2025 | VQE, Quantum Walk, Variational | 12 | Real QPU (unspecified) | Two benchmark problem instances were used. For N2, |
| [[2025_Zhong_ClassicalOptimizationImaginary]] | 2025 | QAOA, Variational | — | Qiskit simulator | Input instances were synthetic unweighted 3-regula |
| [[2024_CadiTazi_FoldedSpectrumVqe]] | 2024 | VQE, Variational | 4 | Qiskit simulator | Input systems were molecular electronic structure  |
| [[2024_Huang_EvaluatingQuantumClassical]] | 2024 | VQE | 4 | PennyLane | Hydrogen: H2 in STO-3G, mapped to 4 qubits via Jor |
| [[2023_Chowdhury_AcceleratedQuantumMonte]] | 2023 | — | 1440 | D-Wave | Synthetic benchmark problem defined by the stoquas |
| [[2023_Simula_QuantumMonteCarlo]] | 2023 | Variational | — | Simulator (unspecified) | Materials studied were C, Si, and AlN in pristine  |
| [[2023_YonaEkaPratiwi_PengembanganAlgoritmaKuantum]] | 2023 | QAOA, VQE | — | Simulator (unspecified) | Input consists of optimization problem formulation |
| [[2017_Delyon_ConfidenceEfficiencyScaling]] | 2022 | Variational | — | — | Configuration space R ∈ [−L/2, L/2]^ν with ν = 2Ne |
| [[2022_Sen_VariationalQuantumClassifiers]] | 2022 | Variational | 4 | PennyLane | Synthetic task: 4-bit binary input strings encoded |
| [[2021_Schtzle_ConvergenceFixedNode]] | 2021 | Variational | — | — | Molecular electronic-structure test cases rather t |
| [[2015_Cai_EntanglementBasedMachine]] | 2019 | — | — | Simulator (unspecified) | Synthetic low-dimensional vectors encoded as quant |
| [[2019_Nagy_VariationalQuantumMonte]] | 2019 | Variational | — | — | Model-based input rather than a dataset. The main  |
| [[2016_Isakov_UnderstandingQuantumTunneling]] | 2015 | Grover, Quantum Annealing | — | Simulator (unspecified) | Synthetic model instances only. Continuous-space c |
| [[2016_Petrosyan_GroverSearchAlgorithm]] | 2015 | Grover | — | Simulator (unspecified) | Synthetic quantum-search instances defined by mark |
| [[2015_McClean_ClockQuantumMonte]] | 2014 | Variational | 11 | — | Synthetic quantum-circuit test cases rather than e |
| [[2012_Neuscamman_OptimizingLargeParameter]] | 2012 | Variational | — | Simulator (unspecified) | Model-system inputs rather than observational fina |
| [[2010_Trail_OptimumEfficientSampling]] | 2010 | Variational | — | — | Electronic-structure benchmark set of 26 systems:  |
| [[2007_Sandvik_VariationalQuantumMonte]] | 2007 | Variational | — | Simulator (unspecified) | Input consists of the transverse-field Ising chain |
| [[1996_Eckstein_VariationalQuantumMonte]] | 1996 | Variational | — | Simulator (unspecified) | Simulated physical system: bulk GaAs semiconductor |
| [[2024_Alidaee_HybridHeuristicAlgorithms]] | — | Quantum Annealing, QUBO | — | D-Wave | Input consisted of synthetic/benchmark QUBO (UBQP) |

## Hardware Distribution

| Hardware Type | Papers |
|---------------|--------|
| Simulator (unspecified) | 37 |
| Qiskit simulator | 34 |
| D-Wave | 8 |
| IBM Quantum (real) | 5 |
| PennyLane | 4 |
| Real QPU (unspecified) | 2 |
| Rigetti | 1 |
| Cirq | 1 |

## Dataset Catalog

| Dataset | Used By | Papers |
|---------|---------|--------|
| Input data consisted of daily stock pric... | asset-pricing, portfolio-optimisation | 2 |
| Input data consisted of historical daily... | high-frequency-trading, portfolio-optimisation, risk-modelling | 2 |
| Simulated physical system: bulk GaAs sem... |  | 1 |
| Input consists of the transverse-field I... |  | 1 |
| Electronic-structure benchmark set of 26... |  | 1 |
| Primary input data are 64-node synthetic... | portfolio-optimisation | 1 |
| Model-system inputs rather than observat... |  | 1 |
| Synthetic low-dimensional vectors encode... |  | 1 |
| Synthetic quantum-circuit test cases rat... |  | 1 |
| Synthetic model instances only. Continuo... |  | 1 |
| Synthetic quantum-search instances defin... |  | 1 |
| Configuration space R ∈ [−L/2, L/2]^ν wi... |  | 1 |
| Synthetic Black-Scholes-Merton option-pr... | derivatives-pricing, risk-modelling | 1 |
| Financial input consists of historical d... | portfolio-optimisation | 1 |
| Synthetic integration problem: I = (1/th... | risk-modelling | 1 |
| Model-based input rather than a dataset.... |  | 1 |
| Inputs vary by example: (1) synthetic Bo... | asset-pricing, credit-scoring, derivatives-pricing, fraud-detection, high-frequency-trading, portfolio-optimisation, quantum-cryptography, risk-modelling | 1 |
| Synthetic inputs only. Copula variables... | risk-modelling | 1 |
| Synthetic input only: estimation of the... | risk-modelling | 1 |
| Example CDO input consists of 4 assets w... | derivatives-pricing, risk-modelling | 1 |
| CVRP: synthetic instance with l=10 locat... | portfolio-optimisation | 1 |
| Financial input data consisted of 5070 s... | market-simulation | 1 |
| Input consists of randomly generated QUB... | portfolio-optimisation | 1 |
| Portfolio optimization: synthetic daily... | portfolio-optimisation | 1 |
| Financial input consists of intraday pri... | portfolio-optimisation | 1 |
| Input instances are randomly generated p... | portfolio-optimisation | 1 |
| Inputs consisted of three classes of opt... | portfolio-optimisation, risk-modelling | 1 |
| Input consists of normalized covariance/... | asset-pricing, derivatives-pricing | 1 |
| Input data consist of daily historical p... | portfolio-optimisation | 1 |
| Molecular electronic-structure test case... |  | 1 |
| Input consisted of two 8-asset stock-pri... | portfolio-optimisation | 1 |
| Two main inputs were used. (1) Vanilla E... | derivatives-pricing, risk-modelling | 1 |
| Artificial data: for each configuration,... | regulatory-compliance | 1 |
| Financial input consists of randomly sam... | portfolio-optimisation | 1 |
| Synthetic option pricing instances under... | derivatives-pricing, risk-modelling | 1 |
| Input data are randomly generated portfo... | portfolio-optimisation | 1 |
| Inputs consisted of optimization instanc... | portfolio-optimisation, risk-modelling | 1 |
| Inputs consist of (1) symbolic/arithmeti... | derivatives-pricing | 1 |
| Synthetic task: 4-bit binary input strin... |  | 1 |
| Synthetic portfolio instance with 3 asse... | portfolio-optimisation | 1 |
| Two synthetic instance sets were generat... | portfolio-optimisation | 1 |
| Synthetic numerical inputs rather than o... | derivatives-pricing | 1 |
| Classical-environment input: synthetic G... | derivatives-pricing, risk-modelling | 1 |
| Synthetic benchmark problem defined by t... |  | 1 |
| Primary inputs are randomly generated po... | portfolio-optimisation, risk-modelling | 1 |
| Knapsack input: a literature-based 10-it... | portfolio-optimisation | 1 |
| Input universe: TOPIX500 constituent sto... | asset-pricing | 1 |
| Input consists of stock purchase prices,... | portfolio-optimisation | 1 |
| Materials studied were C, Si, and AlN in... |  | 1 |
| Churn prediction input: proprietary bank... | credit-scoring, fraud-detection, risk-modelling | 1 |
| Synthetic European call option instances... | derivatives-pricing | 1 |
| Inputs are described only at a conceptua... | portfolio-optimisation | 1 |
| Input consists of optimization problem f... |  | 1 |
| Input consisted of synthetic/benchmark Q... |  | 1 |
| Input data is described as a Kaggle fina... | asset-pricing, portfolio-optimisation, risk-modelling | 1 |
| Input systems were molecular electronic... |  | 1 |
| Primary input: IBEX35 adjusted closing p... | portfolio-optimisation | 1 |
| DJIA stock market data from the U.S. ove... | portfolio-optimisation, risk-modelling | 1 |
| Hydrogen: H2 in STO-3G, mapped to 4 qubi... |  | 1 |
| Single-company stock time-series dataset... | asset-pricing | 1 |
| Input data consists of historical S&P 50... | portfolio-optimisation | 1 |
| Company/investment portfolio data with f... | portfolio-optimisation | 1 |
| Iris experiment: 4 features per sample (... | fraud-detection | 1 |
| Cora dataset: undirected citation graph... | asset-pricing, market-simulation | 1 |
| For ansatz selection, 20 small MKP insta... | portfolio-optimisation, risk-modelling | 1 |
| Inputs include: multiway number partitio... | portfolio-optimisation | 1 |
| Input data consisted of residential elec... | portfolio-optimisation, risk-modelling | 1 |
| Historical Nasdaq stock data for 16 name... | portfolio-optimisation, risk-modelling | 1 |
| Input data consists of monthly NSE deriv... | portfolio-optimisation | 1 |
| {'source': 'Yahoo Finance via yfinance P... | portfolio-optimisation | 1 |
| Input consists of synthetic/physics-simu... |  | 1 |
| Problem inputs were synthetically genera... | portfolio-optimisation | 1 |
| Input instances consisted of unweighted... |  | 1 |
| Problem instances are generated from dis... | derivatives-pricing | 1 |
| Input data consisted of historical stock... | asset-pricing | 1 |
| Synthetic single-asset autocallable opti... | derivatives-pricing | 1 |
| Illustrative datasets mentioned include... | credit-scoring, fraud-detection, high-frequency-trading, portfolio-optimisation, risk-modelling | 1 |
| For qGAN, Binance API data for five cryp... | asset-pricing, market-simulation, portfolio-optimisation | 1 |
| The implied inputs are enterprise financ... | regulatory-compliance, risk-modelling | 1 |
| Synthetic inputs only: initial state x0... |  | 1 |
| N/A | portfolio-optimisation | 1 |
| Input data consisted of Yahoo Finance st... | portfolio-optimisation | 1 |
| Benchmark instances from literature for... |  | 1 |
| Synthetic experiment inputs rather than... | derivatives-pricing | 1 |
| Synthetic generated instances only. For... |  | 1 |
| A manually constructed 4-asset portfolio... | portfolio-optimisation | 1 |
| Input data consists of >25,000 bank loan... | credit-scoring | 1 |
| Kaggle credit risk dataset with about 12... | credit-scoring, risk-modelling | 1 |
| Main financial experiment: S&P 500 stock... | portfolio-optimisation | 1 |
| Synthetic ab initio inputs rather than a... |  | 1 |
| Yahoo Finance AAPL daily stock data, 1,5... | asset-pricing | 1 |
| Two benchmark problem instances were use... |  | 1 |
| Input instances were synthetic unweighte... |  | 1 |
| Input consists of synthetic vehicle rout... |  | 1 |
| Input data consisted of two Kaggle credi... | credit-scoring, regulatory-compliance | 1 |
| Yahoo Finance historical stock prices fr... | portfolio-optimisation, risk-modelling | 1 |
| Input data consisted of historical AAPL... | derivatives-pricing | 1 |
| Two problem inputs are used for numerica... | derivatives-pricing | 1 |
| Portfolio optimization: annualized retur... | portfolio-optimisation | 1 |
| Yahoo Finance daily closing prices for 5... | portfolio-optimisation | 1 |
| Financial input consists of stock data S... | portfolio-optimisation, risk-modelling | 1 |
| Amplitude-estimation benchmarks use pres... |  | 1 |
| Model-generated inputs rather than a fix... | asset-pricing, derivatives-pricing, market-simulation | 1 |

## Methodology Gaps

- Topics with no experiment details: none
- Methods tested only in simulation: HHL, grover, quantum-annealing, quantum-walk
- Papers with "demonstrated" QA claim but simulation-only: [[2026_C_AdvancingStockPrice]]
- Topics where all QA claims are "speculative": none
