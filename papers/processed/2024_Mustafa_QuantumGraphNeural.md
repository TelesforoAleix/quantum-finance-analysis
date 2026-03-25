---
aliases:
- Quantum Graph Neural Networks for Portfolio Optimization in Complex Financial Markets,
  A Novel Approach
- Quantum Graph Neural Networks
authors:
- Hasan Mustafa
- Prateek Jain
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/TQCEBT59414.2024.10545170
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2024 International Conference on Trends in Quantum Computing and
  Emerging Business Technologies (TQCEBT)
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: medium
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:04:54.348343'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:04:57.985634'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:05:22.719588'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:05:57.166851'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:06:30.361710'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:06:38.107932'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/asset-pricing
- topic/market-simulation
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Graph Neural Networks for Portfolio Optimization in Complex Financial
  Markets, A Novel Approach
topic_tags:
- asset-pricing
- market-simulation
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes a hybrid quantum-classical graph neural network architecture that uses parameterized quantum circuits as message-passing layers to model graph-structured data. The authors benchmark their quantum GNN on the Cora citation network and then apply it to NIFTY50 financial time series, where the task is to predict the direction of stock price movements using graph structures derived from historical correlations. They compare different encoding schemes and ansatz choices, and evaluate performance against classical GNNs and XGBoost to assess the viability of quantum approaches for financial forecasting problems.
## Methodology
The paper presents an empirical proof-of-concept hybrid quantum-classical graph neural network (QGNN) for node classification and financial stock-movement prediction. The proposed architecture replaces the message-passing transformation in a graph neural network with parameterized quantum circuits (PQCs), while retaining classical aggregation and loss computation. The model is implemented using PyTorch Geometric and PennyLane, and evaluated first on the Cora citation-network benchmark and then on a financial graph derived from NIFTY50 stock time series. Node features are encoded into quantum states using either angle encoding or amplitude encoding, then processed by either strongly entangling layers or basic/simple entangling layers, and measured via Pauli-Z expectation values. For Cora, dimensionality reduction is handled either by a classical input-mapping layer or PCA to 256 features to support quantum encoding under qubit constraints. For the financial task, graphs are constructed from historical stock correlations by connecting highly correlated stocks with unweighted edges, producing sparse, balanced, and dense graph variants. The model is trained with Adam using cross-entropy loss and backpropagation through both classical and quantum parameters. Performance is compared against classical GCN baselines, a random baseline on Cora, and XGBoost on the stock-prediction task, using cross-entropy loss, accuracy, F1 score, and ROC-AUC.

**Algorithms used:** Parameterized Quantum Circuits, Quantum Graph Neural Network, Graph Convolutional Network, PCA, XGBoost, Adam
**Frameworks:** PennyLane, PyTorch Geometric, PyTorch

**Experimental setup:** Experiments were conducted as hybrid quantum-classical simulations. All quantum circuits were run on the PennyLane 'default.qubit' noiseless simulator. The QGNN used 3 quantum graph convolution layers. For the benchmarked Cora experiments, each quantum layer used a parameterized circuit ansatz with 10 repetitions, totaling 90 learnable quantum parameters across 7 qubits. Classical baselines included GCN models with hidden sizes h=5 and h=6, and XGBoost for the financial prediction task.

**Dataset:** Two datasets were used: (1) the Cora citation network benchmark with 2,708 nodes, 10,556 edges, 1,433 node features, and 7 labels; and (2) a financial graph dataset derived from NIFTY50 historical stock time series, where stocks are connected based on historical correlations. The financial dataset was organized into three graph variants with different average node degrees: sparse, balanced, and dense; each graph had 49 nodes, k edges, n node features based on prior days' prices, and 1 label indicating next-day stock movement direction.
## Findings
- [supported] The proposed hybrid quantum-classical graph neural network (QGNN) was implemented and evaluated entirely on a noiseless Pennylane simulator rather than real quantum hardware.
- [supported] On the Cora benchmark, the best QGNN variant (strongly entangled layers) achieved 59.6% test accuracy with training cross-entropy loss 1.4246, underperforming comparable classical GCN baselines that achieved 65.2% and 79.0% accuracy.
- [supported] On PCA-reduced Cora data, QGNN variants performed substantially worse than classical GCNs: amplitude encoding reached 45.4% accuracy, strongly entangled QGNN 45.8%, and simple entangled QGNN 39.1%, versus 79.1% for both classical GCN baselines.
- [supported] For NIFTY50 stock-movement direction prediction, QGNN variants produced F1 scores broadly similar to classical baselines, with the strongly entangled QGNN outperforming the GCN in sparse and balanced graph settings on F1 score.
- [supported] In the sparse stock graph, the strongly entangled QGNN achieved F1 score 0.5879 and ROC-AUC 0.5385 versus GCN F1 score 0.5787 and ROC-AUC 0.4800.
- [supported] In the balanced stock graph, the strongly entangled QGNN achieved F1 score 0.5817 and ROC-AUC 0.4959 versus GCN F1 score 0.5630 and ROC-AUC 0.4900.
- [supported] In the dense stock graph, the classical GCN achieved the highest F1 score at 0.5983, exceeding the strongly entangled QGNN at 0.5887, although the QGNN had higher ROC-AUC (0.5302 vs 0.4811).
- [supported] The authors conclude that the hybrid model is viable for financial time-series forecasting but does not clearly outperform classical methods overall.
- [supported] The study reports optimization difficulty as qubit count increases, with preliminary investigations indicating training becomes increasingly difficult for larger circuits, consistent with barren plateau concerns.
- [speculative] The authors suggest hybrid quantum models may avoid overfitting relative to classical models in high-uncertainty financial problems, but this mechanism is not directly validated in the reported experiments.

**Results summary:** The paper proposes a hybrid quantum-classical graph neural network for graph learning and financial stock-movement prediction, using parameterized quantum circuits as message-passing layers. All experiments were conducted in simulation on a noiseless Pennylane device. On the Cora benchmark, the QGNN did not match classical GCN performance: the best QGNN reached 59.6% test accuracy, while classical GCNs reached 65.2% and 79.0%. On PCA-reduced Cora data, QGNN performance dropped further to 39.1%–45.8% accuracy versus 79.1% for classical GCNs. On the NIFTY50 stock dataset, QGNN and classical methods showed similar performance overall, with the strongly entangled QGNN slightly exceeding the GCN in F1 score for sparse and balanced graph settings, but not in the dense setting. The results support feasibility of the hybrid approach but do not demonstrate a clear quantum advantage.

**Performance claims:**
- Cora: random baseline test accuracy 14%, training cross-entropy loss 1.3
- Cora: GCN h=5 achieved training cross-entropy loss 1.6833 and test accuracy 65.2%
- Cora: GCN h=6 achieved training cross-entropy loss 0.1966 and test accuracy 79.0%
- Cora: QGNN strongly entangled layers achieved training cross-entropy loss 1.4246 and test accuracy 59.6%
- Cora: QGNN simple entangled layers achieved training cross-entropy loss 1.520 and test accuracy 45.5%
- PCA Cora: GCN h=5 achieved training cross-entropy loss 0.611 and test accuracy 79.1%
- PCA Cora: GCN h=6 achieved training cross-entropy loss 0.5809 and test accuracy 79.1%
- PCA Cora: QGNN amplitude encoding achieved training cross-entropy loss 0.8706 and test accuracy 45.4%
- PCA Cora: QGNN strongly entangled layers achieved training cross-entropy loss 1.649 and test accuracy 45.8%
- PCA Cora: QGNN simple entangled layers achieved training cross-entropy loss 1.5727 and test accuracy 39.1%
- Stock sparse graph: XGBoost cross-entropy loss 0.2605, F1 0.4851, ROC-AUC 0.4842
- Stock sparse graph: GCN h=5 cross-entropy loss 1.5817, F1 0.5787, ROC-AUC 0.4800
- Stock sparse graph: QGNN strongly entangled layers cross-entropy loss 0.6649, F1 0.5879, ROC-AUC 0.5385
- Stock sparse graph: QGNN simple entangled layers cross-entropy loss 0.6762, F1 0.5817, ROC-AUC 0.4834
- Stock balanced graph: XGBoost cross-entropy loss 0.2605, F1 0.4851, ROC-AUC 0.4842
- Stock balanced graph: GCN h=5 cross-entropy loss 8.8751, F1 0.5630, ROC-AUC 0.4900
- Stock balanced graph: QGNN strongly entangled layers cross-entropy loss 0.6788, F1 0.5817, ROC-AUC 0.4959
- Stock balanced graph: QGNN simple entangled layers cross-entropy loss 0.6830, F1 0.5783, ROC-AUC 0.4873
- Stock dense graph: XGBoost cross-entropy loss 0.2605, F1 0.4851, ROC-AUC 0.4842
- Stock dense graph: GCN h=5 cross-entropy loss 5.3250, F1 0.5983, ROC-AUC 0.4811
- Stock dense graph: QGNN strongly entangled layers cross-entropy loss 0.6490, F1 0.5887, ROC-AUC 0.5302
- Stock dense graph: QGNN simple entangled layers cross-entropy loss 0.6714, F1 0.5681, ROC-AUC 0.4150
- Model size on Cora: QGNN used 3 quantum graph convolution layers with 10 ansatz repetitions, totaling 90 learnable quantum parameters across 7 qubits; comparable classical GNN had 98 learnable parameters
## Quantum advantage claim
**Classification:** not-applicable

The paper does not demonstrate quantum advantage. Results are obtained only on a noiseless simulator, and the QGNN generally underperforms classical GCNs on Cora while showing only mixed, near-parity results on the financial dataset.
## Limitations
- The study is presented as a proof of concept rather than a production-ready system.
- All quantum circuits were simulated on the Pennylane 'Device Qubit' noiseless simulator, so results do not reflect real hardware noise, decoherence, or gate errors.
- The authors report that optimization becomes increasingly difficult as the number of qubits increases, indicating limited scalability due to barren plateaus.
- Experiments use a relatively modest number of qubits (7 qubits in the Cora benchmark), constraining model capacity.
- High-dimensional input data required dimensionality reduction or classical preprocessing (input mapping and PCA), which limits end-to-end quantum advantage claims.
- On the Cora benchmark, the hybrid QGNN only performs similarly to a small classical GNN and is outperformed by a larger classical GNN, suggesting scalability and competitiveness challenges.
- The financial task is simplified to predicting only stock movement direction rather than solving full portfolio optimization.
- The financial graph dataset is small, consisting of only 3 graphs with 49 nodes each, limiting statistical power and generalizability.
- The stock universe is limited to NIFTY50 equities from a single market, reducing external validity across regions, asset classes, and market regimes.
- Graph construction is based on historical correlations with unweighted edges, which may oversimplify inter-stock relationships.
- The paper does not report experiments on actual portfolio construction, returns, risk-adjusted performance, transaction costs, or other economically meaningful portfolio metrics.
- [inferred] No evaluation on real quantum hardware was performed, so practical feasibility on NISQ devices remains unverified.
- [inferred] The use of a noiseless simulator likely overestimates achievable performance relative to current hardware.
- [inferred] Reproducibility is limited because the paper does not provide enough detail on train/test splits, time periods, hyperparameter search, random seeds, or code availability.
- [inferred] There is no rigorous comparison against stronger state-of-the-art classical financial forecasting baselines beyond GCN and XGBoost.
- [inferred] The paper does not report repeated runs, confidence intervals, or statistical significance tests, so robustness of the reported gains is unclear.
- [inferred] The claim that the hybrid model may avoid overfitting is speculative and not supported by dedicated ablation or generalization analysis.
- [inferred] Using the Cora citation dataset as a benchmark has limited relevance to financial services applications.
## Open questions
- How well would the proposed QGNN perform on real noisy quantum hardware rather than a noiseless simulator?
- Can the architecture be trained effectively at larger qubit counts without suffering from barren plateaus?
- Does the hybrid QGNN retain any advantage as graph size, feature dimension, and model depth increase?
- How sensitive are results to the choice of quantum embedding method, ansatz design, and circuit depth?
- Would weighted, dynamic, or causality-based financial graphs outperform the simple correlation-based unweighted graph used here?
- Do the observed F1-score improvements on some NIFTY50 graph settings persist across different time periods and market regimes?
- Can the method generalize beyond NIFTY50 to other equity universes, asset classes, or international markets?
- Would the model improve actual portfolio optimization outcomes, not just next-day direction prediction?
- What is the trade-off between classical preprocessing/dimensionality reduction and any genuine quantum contribution?
- How reproducible and statistically stable are the reported results across random initializations and repeated trials?

**Future work:**
- Investigate methods to mitigate barren plateaus and improve optimization for larger-qubit quantum graph neural networks.
- Scale the proposed architecture to higher qubit counts and larger models if optimization challenges can be addressed.
- Evaluate the approach on real-world financial applications beyond stock direction prediction, including fuller portfolio optimization settings.
- Explore alternative quantum embeddings and ansatz choices within the QGNN framework.
- Test the model on larger and more diverse financial datasets and graph structures.
- Study richer graph constructions for financial markets, potentially incorporating stronger association information than simple historical correlation.
- Benchmark against stronger classical baselines and larger classical GNNs to better assess any quantum benefit.
- Validate the approach on real NISQ hardware and assess the impact of noise and error mitigation.
- Conduct more systematic generalization and overfitting analyses to verify whether hybrid models are more robust than classical ones.
- Extend evaluation from classification metrics to economically relevant portfolio metrics such as returns, Sharpe ratio, drawdown, and transaction costs.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum-classical graph neural network where parameterized quantum circuits replace message-passing layers in a GNN for stock-movement prediction on correlation-based financial graphs.
- #idea:near-term-feasibility — Frames the approach as a NISQ-era proof of concept using small variational circuits and hybrid training, but only in noiseless simulation.
- #idea:hybrid-approach — Uses classical preprocessing such as PCA or input mapping to reduce feature dimension before quantum encoding, lowering qubit requirements at the cost of end-to-end quantum purity.
- #idea:near-term-feasibility — On NIFTY50 direction prediction, QGNN reaches near-parity with classical baselines and slightly higher F1 in sparse and balanced graph settings, suggesting limited practical viability rather than clear superiority.
## Contradictions
- The paper's practical viability narrative is contradicted by its own results: the QGNN underperforms classical GCNs on Cora and only achieves mixed near-parity on the financial task, so it does not support quantum superiority.
- The suggestion that the method could scale to larger financial problems is contradicted by reported optimization difficulty and barren plateau concerns as qubit count increases.
- Any implication of NISQ applicability is weakened by the fact that all experiments were run on a noiseless simulator rather than real hardware, conflicting with realistic expectations under noise and decoherence.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Cora dataset: undirected citation graph with 2,708 nodes, 10,556 edges, 1,433 bag-of-words features per node, and 7 class labels. For some quantum experiments, features were reduced from 1,433 to 256 using PCA; alternatively, a classical input layer mapped features to a lower-dimensional space for angle encoding. Financial dataset: historical time-series data for NIFTY50 stocks from the National Stock Exchange of India; graph edges were created from historical stock correlations using unweighted links between highly correlated stocks. Three graph versions were created based on average node degree (sparse, balanced, dense). Final financial graphs contained 49 nodes each, with each node having n historical-day features and a binary label for n+1 day movement direction. The paper does not specify the exact time period, train/test split, or preprocessing beyond correlation-based graph construction and optional PCA for Cora.

### Process
1. Construct graph datasets: use Cora directly; for NIFTY50, compute historical correlations and connect highly correlated stocks to form sparse, balanced, and dense graphs. 2. Prepare node features: for Cora, either reduce dimensionality with a classical input layer for angle encoding or apply PCA to 256 features for amplitude encoding; for financial data, use n days of historical data to predict movement on day n+1. 3. Encode node features into quantum states using either angle encoding or amplitude encoding. 4. Apply parameterized quantum circuit message-passing layers within a 3-layer QGNN architecture. Two ansatz families are tested: strongly entangling layers and simple/basic entangling layers. 5. Measure Pauli-Z expectation values in the computational basis to obtain transformed node representations. 6. Aggregate neighboring node messages classically and update node embeddings. 7. Train the hybrid model using Adam optimizer with cross-entropy loss, backpropagating through both classical and quantum parameters. 8. Benchmark on Cora and compare against classical GCN and random baseline; then select the best-performing quantum model and evaluate on the NIFTY50 stock-direction task against GCN and XGBoost baselines. The paper does not report number of epochs, batch size, learning rate, or shot count, consistent with use of a noiseless simulator.

### Output
For Cora, the reported outputs are training cross-entropy loss and test accuracy, with comparisons against a random baseline and classical GCNs of comparable and larger size. Reported examples include QGNN strongly entangled layers achieving 59.6% test accuracy and simple entangled layers 45.5%, versus GCN baselines up to 79.1%. For the stock-market dataset, outputs include cross-entropy loss, F1 score, and ROC-AUC for sparse, balanced, and dense graph settings. Baselines are XGBoost and classical GCN h=5. The quantum model reportedly outperforms classical baselines on F1 score in sparse and balanced graph cases, while ROC-AUC results are mixed.

### Parameters
- qubits: 7
- qgnn_layers: 3
- ansatz_repetitions_per_layer: 10
- total_learnable_quantum_parameters: 90
- classical_gcn_hidden_sizes: [5, 6]
- optimizer: Adam
- loss_function: cross-entropy
- encoding_methods: ['angle encoding', 'amplitude encoding']
- ansatz_types: ['strongly entangling layers', 'basic/simple entangling layers']
- measurement: Pauli-Z expectation value
- pca_output_dimension: 256

### Hardware
Quantum circuits were simulated on the PennyLane 'default.qubit' simulator (described in the paper as 'Device Qubit'), using a noiseless simulation environment. No real QPU, cloud quantum hardware, noise model, transpilation settings, or shot-based execution details are reported.

### Reproducibility
No code repository or public implementation link is provided in the excerpt. Dataset sources are identifiable (Cora and NIFTY50-derived data), and the architecture, encodings, ansatz choices, optimizer, and key qubit/parameter counts are described, but important replication details are missing, including exact NIFTY50 time period, graph-construction thresholds, train/test splits, epoch counts, learning rate, batch size, and other training hyperparameters. Reproducibility is therefore partial but incomplete.
