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
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-19T13:02:30.992489'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:02:36.899043'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:02:45.178362'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:02:56.655230'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:03:09.819787'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:03:29.033046'
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
- method/quantum-ML
- method/variational
- method/quantum-simulation
- method/classical-simulation
- idea/hybrid-approach
- idea/near-term-feasibility
- contradiction/classical-vs-quantum
title: Quantum Graph Neural Networks for Portfolio Optimization in Complex Financial
  Markets, A Novel Approach
topic_tags:
- portfolio-optimisation
- asset-pricing
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a novel hybrid quantum-classical graph neural network (QGNN) designed for financial time series modeling and portfolio optimization. The authors propose a proof-of-concept model that integrates quantum circuits as message-passing layers within a graph neural network framework, implemented using PyTorch Geometric and PennyLane. The study benchmarks the model on the Cora dataset and applies it to predict stock price movements in the NIFTY50 index, exploring how quantum-enhanced methods compare to classical approaches in handling financial data's stochastic nature.
## Methodology
The paper proposes a novel hybrid quantum-classical graph neural network (QGNN) for financial time series forecasting, specifically predicting stock price movements. The methodology involves constructing a graph dataset from NIFTY50 stock data, where nodes represent stocks and edges are derived from historical correlation data. The hybrid QGNN architecture uses parameterized quantum circuits (PQCs) as message-passing layers within a classical GNN framework. The model is first benchmarked on the Cora citation network dataset to validate its performance before being applied to financial data. Quantum embedding techniques, including amplitude encoding and angle encoding, are employed to map classical data to quantum states. The quantum circuits utilize strongly entangling layers and basic entangling layers as ansatz designs. Optimization is performed using the Adam optimizer with cross-entropy loss, and gradients are backpropagated through both classical and quantum parameters. The experimental setup involves comparing the hybrid QGNN against classical GNNs and XGBoost models on both benchmark and financial datasets.

**Algorithms used:** Quantum Graph Neural Network (QGNN), Parameterized Quantum Circuits (PQC)
**Frameworks:** PennyLane, PyTorch Geometric, PyTorch

**Experimental setup:** All quantum circuits were simulated using the Pennylane 'Device Qubit' simulator, a noiseless simulator. The experiments involved 7 qubits in the circuit ansatz with 10 repetitions of the circuit layers, totaling 90 learnable quantum parameters. The classical GNN baseline had 98 learnable parameters. The setup included dimensionality reduction techniques (classical layer mapping and PCA) for the Cora dataset but not for the financial time series data due to its lower feature count.

**Dataset:** The Cora citation network dataset (2,708 nodes, 10,556 edges, 1,433 features per node, 7 labels) was used for benchmarking. For financial data, historical stock prices from the NIFTY50 index (top 50 companies of the National Stock Exchange, India) were used to construct three graph datasets with varying node degrees (high, low, and balanced). Each node had 'n' features representing historical data to predict the stock movement direction on the (n+1)th day.
## Findings
- [supported] The proposed hybrid quantum-classical graph neural network (QGNN) achieves comparable performance to classical graph convolutional networks (GCN) on the Cora dataset, with test accuracies of 59.6% (strongly entangled layers) and 45.5% (simple entangled layers) versus 65.2% (GCN h=5) and 79.0% (GCN h=6).
- [supported] On the NIFTY50 stock movement prediction task, the QGNN outperforms classical models (XGBoost and GCN) in F1 score for sparse and balanced graph cases (e.g., 0.5879 vs. 0.5787 for sparse graphs).
- [supported] Quantum embedding strategies (amplitude encoding vs. angle encoding) show trade-offs: amplitude encoding uses fewer qubits but requires higher circuit depth, while angle encoding is more straightforward but limited in feature representation.
- [speculative] The authors suggest that hybrid QGNNs may avoid overfitting in high-uncertainty problems like stock movement prediction, unlike classical models.
- [speculative] Quantum advantage for QGNNs is proposed to emerge with larger qubit counts, though scalability is currently limited by barren plateaus and optimization challenges.
- [supported] Visualization of embeddings demonstrates that QGNNs can achieve class separation comparable to classical GNNs, though larger classical models still outperform in accuracy.

**Results summary:** The paper introduces a hybrid quantum-classical graph neural network (QGNN) for financial time series prediction, benchmarking it against classical models on the Cora dataset and NIFTY50 stock data. Results show that QGNNs perform similarly to classical GNNs of comparable size, with slight advantages in F1 score for stock movement prediction in sparse/balanced graphs. However, larger classical GNNs still achieve higher accuracy, highlighting scalability challenges. The study uses noiseless simulations (Pennylane) and explores quantum embedding strategies, noting trade-offs between qubit efficiency and circuit complexity. While the hybrid approach shows promise for avoiding overfitting, quantum advantage remains speculative due to hardware limitations.

**Performance claims:**
- 59.6% test accuracy on Cora dataset (QGNN with strongly entangled layers)
- 45.5% test accuracy on Cora dataset (QGNN with simple entangled layers)
- 0.5879 F1 score on NIFTY50 sparse graph (QGNN vs. 0.5787 for GCN)
- 0.5817 F1 score on NIFTY50 balanced graph (QGNN vs. 0.5630 for GCN)
- 79.0% test accuracy for classical GCN (h=6) on Cora dataset
## Quantum advantage claim
**Classification:** speculative

The paper suggests potential quantum advantage in avoiding overfitting and scalability to larger qubit counts, but all results are from noiseless simulations. No empirical demonstration of quantum advantage on real hardware or beyond classical model performance is provided.
## Limitations
- Experiments conducted on a noiseless simulator (Pennylane 'Device Qubit'), which does not account for hardware noise or decoherence effects [inferred]
- Limited to 7 qubits in the quantum circuit ansatz, restricting scalability to larger datasets or more complex financial models [inferred]
- Benchmarking primarily on the Cora dataset, which may not fully represent the complexity of real-world financial time series data
- Financial time series experiments limited to NIFTY50 stocks, with no validation on other global markets or asset classes [inferred]
- No explicit noise mitigation techniques applied, which could impact performance on real quantum hardware [inferred]
- Dimensionality reduction techniques (e.g., PCA) required for amplitude encoding, potentially losing critical financial data features [inferred]
- Preliminary investigations showed optimization difficulties (barren plateaus) when increasing qubit count, limiting model scalability
- Page-limit constraints of the conference paper may have restricted detailed discussion of hyperparameter tuning or failure cases [inferred]
- No comparison with state-of-the-art classical deep learning models (e.g., Transformers) for financial forecasting [inferred]
- Stock movement prediction limited to direction (binary classification), not magnitude or volatility [inferred]
- Graph connectivity derived from historical correlations, which may not capture dynamic market regime shifts [inferred]
## Open questions
- How does the hybrid QGNN perform on real quantum hardware with noise and decoherence?
- What is the impact of different quantum embedding schemes (amplitude vs. angle encoding) on financial time series prediction accuracy?
- Can the model scale to larger qubit counts (e.g., 50+ qubits) without encountering barren plateaus?
- How does the QGNN compare to classical GNNs when trained on larger financial datasets (e.g., S&P 500 or global indices)?
- What are the implications of using unweighted edges in the financial graph for stock movement prediction?
- How does the model handle non-stationary financial data where correlations evolve over time?
- What noise mitigation strategies could improve performance on NISQ devices?
- Can the hybrid architecture be extended to multi-task learning (e.g., simultaneous price direction and volatility prediction)?

**Future work:**
- Test the model on real quantum hardware (e.g., IBM Quantum or Rigetti processors)
- Investigate advanced noise mitigation techniques (e.g., error mitigation, dynamical decoupling) for NISQ-era deployment
- Extend the model to larger qubit counts while addressing barren plateau challenges
- Apply the QGNN to other financial tasks (e.g., derivative pricing, risk management, or fraud detection)
- Explore alternative graph construction methods for financial data (e.g., dynamic graphs or weighted edges)
- Compare performance with state-of-the-art classical models (e.g., Transformers, Temporal GNNs) on large-scale financial datasets
- Develop hybrid architectures that combine quantum and classical layers more efficiently
- Investigate the use of quantum attention mechanisms in GNNs for financial applications
- Validate the model on global financial markets beyond NIFTY50 (e.g., S&P 500, FTSE 100)
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum-classical graph neural network (QGNN) integrating parameterized quantum circuits as message-passing layers for financial time series forecasting and portfolio optimization
- #idea:near-term-feasibility — Demonstrates NISQ-era applicability through noiseless simulations, though scalability is limited by qubit count and optimization challenges
- #idea:hybrid-approach — Classical preprocessing (e.g., dimensionality reduction for amplitude encoding) reduces quantum resource requirements but may discard financial features
- #limitation:noise — Relies solely on noiseless simulations, lacking empirical validation on real quantum hardware
- #limitation:qubit-count — Experiments limited to 7 qubits, restricting scalability to larger financial datasets
## Contradictions
- The paper's claim of NISQ-era suitability for quantum machine learning contradicts broader literature on noise-induced limitations (e.g., barren plateaus and optimization challenges in variational quantum algorithms). Specifically, the speculative advantage in avoiding overfitting is not empirically validated and conflicts with known hardware constraints.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
