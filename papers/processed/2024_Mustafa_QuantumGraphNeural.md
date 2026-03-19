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
- idea:near-term-feasibility
- idea:hybrid-approach
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
step1_date: '2026-03-18T23:31:45.035382'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:32:01.406711'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:32:09.291080'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:32:19.943383'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:33:09.301219'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:33:13.292915'
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
- idea/near-term-feasibility
- idea/hybrid-approach
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
This paper introduces a novel hybrid quantum-classical graph neural network (GNN) designed for financial time series modeling and portfolio optimization. The authors propose a quantum-enhanced GNN architecture that integrates parameterized quantum circuits as message-passing layers, aiming to capture complex dependencies in financial data. The approach is demonstrated through a proof-of-concept implementation on benchmark datasets and applied to predict stock price movements in the NIFTY50 index, addressing challenges in traditional financial forecasting methods.
## Methodology
The paper proposes a novel hybrid quantum-classical graph neural network (QGNN) for financial time series forecasting, specifically predicting stock price movements. The methodology involves constructing a graph dataset from financial time series data (NIFTY50 stocks) where nodes represent stocks and edges are derived from historical correlation data. The hybrid QGNN architecture integrates parameterized quantum circuits (PQCs) as message-passing layers within a classical GNN framework. Classical computation is limited to aggregating node information and computing the loss function. The model is first benchmarked on the Cora citation network dataset to validate its structure and performance. Quantum embedding techniques, including amplitude encoding and angle encoding, are employed to map classical data to the quantum Hilbert space. The quantum circuit ansatz uses strongly entangling layers and basic entangling layers from the Pennylane library. Optimization is performed using the Adam optimizer with cross-entropy loss, and gradients are backpropagated through both classical and quantum parameters. The experimental setup evaluates the model's performance on financial datasets with varying node degrees to study the impact of graph connectivity on prediction accuracy.

**Algorithms used:** Quantum Graph Neural Network (QGNN), Parameterized Quantum Circuits (PQC)
**Frameworks:** PennyLane, PyTorch Geometric, PyTorch

**Experimental setup:** All quantum circuits were simulated on the Pennylane 'Device Qubit' simulator, a noiseless simulator. The experiments utilized 7 qubits for the quantum circuit ansatz with 10 repetitions of the circuit layers, totaling 90 learnable quantum parameters. The hybrid model was benchmarked against classical GNNs and XGBoost models on both the Cora dataset and NIFTY50 financial time series data.

**Dataset:** The Cora citation network dataset (2,708 nodes, 10,556 edges, 1,433 features per node, 7 labels) was used for benchmarking. Financial time series data from NIFTY50 stocks (top 50 companies on the National Stock Exchange, India) was used to create graph datasets with varying node degrees (high, low, balanced) based on historical price correlations. Each node had 'n' features representing historical stock data, and the task was to predict the direction of stock movement on the (n+1)th day.
## Findings
- [supported] The proposed hybrid Quantum Graph Neural Network (QGNN) achieves comparable performance to classical Graph Convolutional Networks (GCN) on the Cora dataset, with test accuracies of 59.6% (strongly entangled layers) and 45.5% (simple entangled layers) versus 65.2% (GCN h=5) and 79.0% (GCN h=6).
- [supported] On the NIFTY50 stock movement prediction task, the QGNN outperforms classical models (XGBoost, GCN) in F1 score for sparse and balanced graph cases (e.g., 0.5879 vs. 0.5787 for sparse graphs).
- [supported] The QGNN model demonstrates robustness against overfitting in high-uncertainty financial datasets, performing similarly to classical models without overfitting.
- [speculative] The authors suggest that hybrid quantum-classical GNNs may offer advantages in scalability for larger datasets, though this is not empirically validated in the paper.
- [speculative] Quantum advantage may emerge for financial time series forecasting with higher qubit counts, but current results are limited by barren plateaus and optimization challenges beyond modest qubit numbers.
- [supported] Amplitude encoding and angle encoding schemes show trade-offs: angle encoding uses fewer gates but requires dimensionality reduction, while amplitude encoding can encode exponentially more features but with higher circuit depth.
- [disputed] The claim that quantum machine learning algorithms are inherently suitable for NISQ-era devices due to error mitigation from feedback-based methods contradicts broader literature on noise-induced limitations in quantum machine learning.

**Results summary:** The paper introduces a hybrid quantum-classical Graph Neural Network (QGNN) for financial time series forecasting, benchmarking it against classical models on the Cora dataset and NIFTY50 stock data. Results show that QGNNs perform comparably to classical GCNs on Cora (e.g., 59.6% vs. 65.2% accuracy) and outperform classical models in F1 score for sparse/balanced financial graphs (e.g., 0.5879 vs. 0.5787). However, classical models with larger parameter counts still achieve higher accuracy on Cora. The study highlights challenges in scaling QGNNs due to barren plateaus and optimization difficulties at higher qubit counts, with all quantum experiments conducted on noiseless simulators.

**Performance claims:**
- 59.6% test accuracy on Cora dataset (QGNN with strongly entangled layers)
- 45.5% test accuracy on Cora dataset (QGNN with simple entangled layers)
- 0.5879 F1 score on sparse NIFTY50 graphs (QGNN vs. 0.5787 for GCN)
- 0.5817 F1 score on balanced NIFTY50 graphs (QGNN vs. 0.5630 for GCN)
- 90 learnable quantum parameters (7 qubits, 10 repetitions) vs. 98 classical parameters in comparable GCN
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage empirically. Claims of potential advantage are based on theoretical scalability arguments and simulated performance on small-scale problems (7 qubits). All results are from noiseless simulations, and the authors acknowledge challenges in scaling to larger qubit counts due to barren plateaus.
## Limitations
- Experiments conducted on a noiseless simulator (Pennylane 'Device Qubit'), which does not account for hardware noise or decoherence effects [inferred]
- Limited to 7 qubits in the quantum circuit ansatz, restricting scalability to larger financial datasets
- Benchmarking primarily on the Cora dataset, which may not fully represent the complexity of real-world financial time series data [inferred]
- Financial time series experiments limited to NIFTY50 stocks, lacking diversity in market conditions or global financial instruments [inferred]
- No comparison with state-of-the-art classical deep learning models (e.g., Transformers, Temporal Graph Networks) for financial forecasting [inferred]
- Dimensionality reduction techniques (e.g., PCA) required for amplitude encoding, which may discard relevant financial features [inferred]
- Optimization challenges due to barren plateaus when scaling to higher qubit counts, as noted in preliminary investigations
- Page-limit constraints of conference papers may have restricted detailed discussion of hyperparameter tuning or failure cases [inferred]
- Stock movement prediction limited to direction (up/down) rather than magnitude, which may not fully address practical trading needs [inferred]
- Lack of empirical validation on real quantum hardware, limiting assessment of practical feasibility under NISQ constraints
## Open questions
- How does the hybrid QGNN perform under realistic hardware noise and decoherence effects?
- What is the impact of increasing qubit counts on optimization stability and solution quality?
- Can the model generalize to other financial datasets (e.g., S&P 500, cryptocurrencies) or different market regimes (e.g., high volatility)?
- How does the quantum model compare to classical state-of-the-art methods (e.g., temporal graph networks) in terms of accuracy and computational efficiency?
- What noise mitigation techniques could be integrated to improve performance on NISQ devices?
- How does the choice of quantum embedding (amplitude vs. angle encoding) affect financial forecasting accuracy?
- Can the model be extended to multi-step forecasting or portfolio optimization beyond binary movement prediction?

**Future work:**
- Test the hybrid QGNN on real quantum hardware (e.g., IBM Quantum, Rigetti) to evaluate performance under noise
- Explore noise mitigation techniques (e.g., error mitigation, dynamical decoupling) to improve robustness
- Extend the model to larger qubit counts and evaluate scalability for high-dimensional financial datasets
- Benchmark against advanced classical models (e.g., Transformers, Temporal Graph Networks) for financial time series
- Investigate alternative quantum circuit ansätze to mitigate barren plateaus and improve trainability
- Apply the model to multi-step forecasting and portfolio optimization tasks
- Evaluate performance on diverse financial datasets (e.g., global indices, cryptocurrencies) to assess generalizability
- Integrate hybrid quantum-classical architectures with classical deep learning pipelines for enhanced performance
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum-classical graph neural network (QGNN) integrating parameterized quantum circuits as message-passing layers for financial time series forecasting and portfolio optimization
- #idea:near-term-feasibility — Demonstrates NISQ-era applicability through noiseless simulations, though scalability is limited by qubit count and optimization challenges
- #limitation:noise — Acknowledges lack of empirical validation on real quantum hardware, relying solely on noiseless simulations
- #limitation:qubit-count — Experiments limited to 7 qubits, restricting scalability to larger financial datasets
- #idea:hybrid-approach — Classical preprocessing (e.g., dimensionality reduction for amplitude encoding) reduces quantum resource requirements but may discard financial features
- #contradiction:classical-vs-quantum — Claims of NISQ-era suitability contradict broader literature on noise-induced limitations in quantum machine learning
## Contradictions
- The paper's claim that quantum machine learning algorithms are inherently suitable for NISQ-era devices due to error mitigation from feedback-based methods contradicts findings in other works (e.g., noise-induced barren plateaus and optimization challenges in variational quantum algorithms).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
