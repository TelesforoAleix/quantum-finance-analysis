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
- idea:hybrid-approach
- idea:near-term-feasibility
journal_or_venue: 2024 International Conference on Trends in Quantum Computing and
  Emerging Business Technologies (TQCEBT)
methodology_tags:
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:02:23.950938'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:04:17.689954'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:04:24.601384'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:04:33.308186'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:04:46.040402'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:04:48.794226'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- topic/asset-pricing
- topic/quantum-ML
- method/quantum-ML
- method/variational
- method/classical-simulation
- idea/hybrid-approach
- idea/near-term-feasibility
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Graph Neural Networks for Portfolio Optimization in Complex Financial
  Markets, A Novel Approach
topic_tags:
- portfolio-optimisation
- asset-pricing
- quantum-ML
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a novel hybrid quantum-classical graph neural network (QGNN) designed for financial time series modeling and portfolio optimization. The authors propose a proof-of-concept model that integrates quantum circuits as message-passing layers within a graph neural network framework, implemented using PyTorch Geometric and PennyLane. The study benchmarks the model on the Cora dataset and applies it to predict stock price movements in the NIFTY50 index, exploring the potential of quantum machine learning in financial forecasting under current hardware limitations.
## Methodology
The paper proposes a novel hybrid quantum-classical graph neural network (QGNN) for financial time series forecasting, specifically predicting stock price movements. The methodology involves constructing graph datasets where nodes represent stocks and edges represent correlations between them. The quantum component uses parameterized quantum circuits (PQCs) as message-passing layers within a classical GNN framework. The model is first benchmarked on the Cora citation network dataset, then applied to financial time series data from the NIFTY50 index. The quantum circuits are implemented using Pennylane's noiseless 'Device Qubit' simulator, integrated with PyTorch Geometric for classical GNN operations. Two quantum embedding schemes (amplitude encoding and angle encoding) and two quantum circuit ansätze (strongly entangling layers and basic entangling layers) are explored. The optimization is performed using the Adam optimizer with cross-entropy loss.
**Frameworks:** PyTorch Geometric, PennyLane

**Experimental setup:** All quantum circuits were simulated on the Pennylane 'Device Qubit' simulator, a noiseless simulator. The hybrid model integrates quantum circuits with classical GNN layers using PyTorch Geometric. Experiments were conducted on both the Cora dataset and a custom NIFTY50 financial time series dataset.

**Dataset:** The Cora citation network dataset (2,708 nodes, 10,556 edges, 1,433 features per node, 7 labels) and a financial time series dataset derived from NIFTY50 stocks. The financial dataset consists of 49 nodes (stocks) with edges based on historical correlation data, and node features representing historical price data for n days to predict the n+1th day's stock movement direction.
## Findings
- [supported] The proposed hybrid quantum-classical Graph Neural Network (QGNN) achieves comparable performance to classical Graph Convolutional Networks (GCN) on the Cora dataset, with test accuracies of 59.6% (strongly entangled layers) and 45.5% (simple entangled layers) vs. 65.2% (GCN h=5) and 79.0% (GCN h=6).
- [supported] On the NIFTY50 stock movement prediction task, the QGNN outperforms classical models (XGBoost and GCN) in F1 score for sparse and balanced graph cases (e.g., 0.5879 vs. 0.5787 for GCN in sparse graphs).
- [supported] Quantum embedding strategies (amplitude and angle encoding) were tested, with amplitude encoding requiring fewer qubits but higher circuit depth, while angle encoding used fewer gates but more qubits.
- [speculative] The authors suggest that hybrid QGNNs may avoid overfitting in high-uncertainty problems like stock movement prediction, unlike classical models.
- [speculative] The paper claims that quantum graph neural networks could scale to larger financial datasets, though this is not empirically validated.
- [supported] Optimization challenges (e.g., barren plateaus) were observed when increasing qubit counts, limiting scalability in simulations.
- [supported] All results are derived from noiseless quantum simulations (Pennylane's 'Device Qubit' simulator), not real quantum hardware.

**Results summary:** The paper introduces a hybrid quantum-classical Graph Neural Network (QGNN) for financial time series prediction, benchmarking it against classical models on the Cora dataset and NIFTY50 stock data. While the QGNN performs similarly to classical GCNs on Cora (with slightly lower accuracy), it outperforms classical baselines in F1 score for stock movement prediction in sparse and balanced graph scenarios. The study highlights the viability of hybrid architectures but notes scalability limitations due to optimization challenges (e.g., barren plateaus) and the absence of real-hardware validation. Quantum embedding strategies and ansatz choices are explored, with no clear advantage demonstrated over classical methods in the tested regimes.

**Performance claims:**
- 59.6% test accuracy on Cora dataset (QGNN with strongly entangled layers)
- 45.5% test accuracy on Cora dataset (QGNN with simple entangled layers)
- 0.5879 F1 score on NIFTY50 sparse graph (QGNN vs. 0.5787 for GCN)
- 0.5817 F1 score on NIFTY50 balanced graph (QGNN vs. 0.5630 for GCN)
- 79.0% test accuracy for classical GCN (h=6) on Cora dataset
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential advantages of QGNNs in avoiding overfitting for high-uncertainty financial data, but all results are from noiseless simulations. No empirical quantum advantage is demonstrated, and scalability claims remain unvalidated due to optimization challenges.
## Limitations
- Experiments conducted on a noiseless simulator (Pennylane 'Device Qubit'), which does not account for hardware noise or decoherence effects present in real NISQ devices [inferred]
- Limited to 7 qubits in the quantum circuit ansatz, restricting scalability to larger financial datasets or more complex graph structures
- Benchmarking primarily performed on the Cora dataset, which is not representative of financial time series data, limiting generalizability to real-world financial applications [inferred]
- Financial time series experiments restricted to NIFTY50 stocks, which may not capture the diversity of global financial markets or smaller-cap stocks [inferred]
- No explicit noise mitigation techniques (e.g., error correction or error mitigation) were applied, which could degrade performance on real quantum hardware [inferred]
- Barren plateaus observed during optimization for larger qubit counts, making training difficult and limiting scalability [author-stated]
- Dimensionality reduction techniques (e.g., PCA or classical layers) required for amplitude encoding, which may discard relevant financial features [author-stated]
- Page-limit constraints of the conference paper may have restricted detailed discussion of hyperparameter tuning or ablation studies [inferred]
- No comparison with state-of-the-art classical deep learning models (e.g., Transformers or advanced GNNs) for financial forecasting [inferred]
- Stock movement prediction limited to direction (binary classification), not magnitude, which may limit practical utility for portfolio optimization [author-stated]
- Graph connectivity derived from historical correlations, which may not reflect dynamic or causal relationships in financial markets [inferred]
## Open questions
- How does the proposed Quantum Graph Neural Network (QGNN) perform on real quantum hardware with noise and decoherence?
- What is the impact of different quantum embedding schemes (e.g., amplitude vs. angle encoding) on financial time series forecasting accuracy?
- Can the QGNN architecture scale to larger qubit counts (e.g., 50+ qubits) without encountering barren plateaus?
- How does the QGNN compare to advanced classical models (e.g., Transformers or temporal GNNs) for financial time series prediction?
- What are the trade-offs between quantum circuit depth and model performance in hybrid quantum-classical GNNs?
- How sensitive is the QGNN to the choice of graph connectivity (e.g., sparse vs. dense graphs) in financial datasets?
- Can noise mitigation techniques (e.g., dynamical decoupling or error mitigation) improve QGNN performance on NISQ devices?
- What is the minimum qubit count required for the QGNN to outperform classical GNNs in financial applications?

**Future work:**
- Test the QGNN on real quantum hardware (e.g., IBM Quantum or Rigetti devices) to evaluate noise resilience
- Extend the model to multi-class or regression tasks for stock price prediction (e.g., predicting magnitude of movement)
- Investigate alternative quantum circuit ansatz designs to mitigate barren plateaus and improve trainability
- Apply the QGNN to other financial datasets (e.g., S&P 500, cryptocurrencies) to assess generalizability
- Explore hybrid architectures combining QGNNs with classical attention mechanisms for improved feature extraction
- Develop dynamic graph construction methods for financial time series to capture evolving market relationships
- Integrate the QGNN into a full portfolio optimization pipeline (e.g., combining with QAOA or VQE for asset allocation)
- Benchmark against state-of-the-art classical models (e.g., Temporal Fusion Transformers) for financial forecasting
- Investigate the use of quantum kernels or quantum attention mechanisms in GNNs for financial applications
- Study the impact of different quantum embedding schemes on model interpretability and performance
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum-classical graph neural network (QGNN) integrating parameterized quantum circuits as message-passing layers for financial time series forecasting and portfolio optimization
- #idea:near-term-feasibility — Demonstrates NISQ-era applicability through noiseless simulations, though scalability is limited by qubit count and optimization challenges
- #idea:hybrid-approach — Classical preprocessing (e.g., dimensionality reduction for amplitude encoding) reduces quantum resource requirements but may discard financial features
- #limitation:noise — Relies solely on noiseless simulations, lacking empirical validation on real quantum hardware
- #limitation:qubit-count — Experiments limited to 7 qubits, restricting scalability to larger financial datasets
## Contradictions
- The paper's claim of NISQ-era suitability for quantum machine learning contradicts broader literature on noise-induced limitations (e.g., barren plateaus and optimization challenges in variational quantum algorithms). The speculative advantage in avoiding overfitting is not empirically validated and conflicts with known hardware constraints.
- The paper suggests QGNNs could scale to larger financial datasets, but this is contradicted by observed barren plateaus and optimization challenges during simulations, which limit scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
For the Cora dataset: 2,708 nodes with 1,433 features (bag-of-words representation) and 7 labels. Features were reduced to 256 using PCA for amplitude encoding. For the NIFTY50 dataset: 49 nodes (stocks) with n features (historical prices) and 1 label (direction of stock movement). Three graph variants were created based on node degree (sparse, balanced, dense). No additional preprocessing details were specified beyond dimensionality reduction for the Cora dataset.

### Process
1. Encode classical data into quantum states using amplitude or angle encoding. 2. Apply parameterized quantum circuits (strongly entangling or basic entangling layers) as message-passing layers. 3. Measure Pauli Z expectation values. 4. Aggregate node information classically. 5. Compute cross-entropy loss and backpropagate gradients using Adam optimizer. 6. Repeat for 3 quantum graph convolution layers with 10 repetitions of the circuit ansatz per layer (90 learnable quantum parameters for 7 qubits).

### Output
For the Cora dataset: Cross-entropy loss and accuracy. Embeddings were visualized in 2D space to show class separation. For the NIFTY50 dataset: Cross-entropy loss, F1 score, and ROC AUC score. Results were compared against classical GNNs and XGBoost baselines.

### Parameters
- qubits: 7
- circuit_layers: 3
- ansatz_repetitions_per_layer: 10
- total_quantum_parameters: 90
- optimizer: Adam
- loss_function: Cross-entropy
- quantum_embedding_schemes: ['Amplitude Encoding', 'Angle Encoding']
- ansatz_types: ['Strongly Entangling Layers', 'Basic Entangling Layers']

### Hardware
Pennylane 'Device Qubit' noiseless simulator. No real QPU was used, and no noise model was applied.

### Reproducibility
Code availability is not explicitly mentioned. The Cora dataset is public, and NIFTY50 data is referenced but not explicitly provided. Sufficient methodological detail is provided to replicate the quantum circuit design and hybrid architecture, but exact hyperparameters (e.g., learning rate) are not specified.
