# Quantum ML

**Papers:** 2

## Papers

| Paper | Year | Source Type | Methods | QA Claim | Relevance |
|-------|------|-------------|---------|----------|-----------|
| [[2024_Bhasin_EnhancingQuantumMachine]] | 2024 | conference-paper | quantum-SVM, quantum-ML, variational, classical-simulation | speculative | high |
| [[2024_Mustafa_QuantumGraphNeural]] | 2024 | conference-paper | quantum-ML, variational, classical-simulation | speculative | high |

## Key Findings

- [supported] The proposed Quantum Support Vector Machine (QSVM) achieves a portfolio performance of 89.65% over time, outperforming existing quantum algorithms (QPCA, QBM, QKC) by a margin of 25.15% — [[2024_Bhasin_EnhancingQuantumMachine]]
- [supported] QSVM demonstrates a 25% risk-return tradeoff and a 32.12% efficiency frontier, indicating superior optimization of risk-adjusted returns compared to other quantum methods — [[2024_Bhasin_EnhancingQuantumMachine]]
- [supported] Quantum circuit optimization techniques (gate fusion, qubit mapping, circuit compilation) and noise mitigation strategies (e.g., Steane code, surface code) are implemented to enhance QSVM performance — [[2024_Bhasin_EnhancingQuantumMachine]]
- [supported] The proposed hybrid quantum-classical Graph Neural Network (QGNN) achieves comparable performance to classical Graph Convolutional Networks (GCN) on the Cora dataset, with test accuracies of 59.6% (strongly entangled layers) and 45.5% (simple entangled layers) vs. 65.2% (GCN h=5) and 79.0% (GCN h=6). — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] On the NIFTY50 stock movement prediction task, the QGNN outperforms classical models (XGBoost and GCN) in F1 score for sparse and balanced graph cases (e.g., 0.5879 vs. 0.5787 for GCN in sparse graphs). — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] Quantum embedding strategies (amplitude and angle encoding) were tested, with amplitude encoding requiring fewer qubits but higher circuit depth, while angle encoding used fewer gates but more qubits. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] Optimization challenges (e.g., barren plateaus) were observed when increasing qubit counts, limiting scalability in simulations. — [[2024_Mustafa_QuantumGraphNeural]]
- [supported] All results are derived from noiseless quantum simulations (Pennylane's 'Device Qubit' simulator), not real quantum hardware. — [[2024_Mustafa_QuantumGraphNeural]]
- [speculative] The QSVM algorithm may offer exponential speedup for financial portfolio optimization due to quantum parallelism, though this is not empirically validated in the paper — [[2024_Bhasin_EnhancingQuantumMachine]]
- [speculative] The integration of QSVM into existing financial frameworks could revolutionize portfolio management strategies, but real-world scalability and market adaptability remain untested — [[2024_Bhasin_EnhancingQuantumMachine]]
- [speculative] The authors suggest that hybrid QGNNs may avoid overfitting in high-uncertainty problems like stock movement prediction, unlike classical models. — [[2024_Mustafa_QuantumGraphNeural]]
- [speculative] The paper claims that quantum graph neural networks could scale to larger financial datasets, though this is not empirically validated. — [[2024_Mustafa_QuantumGraphNeural]]
- [disputed] The paper claims a 'quantum advantage' in financial decision-making, but results are based on simulations and lack validation on real quantum hardware, contradicting empirical standards in quantum computing literature — [[2024_Bhasin_EnhancingQuantumMachine]]

## Methodologies Used

| Method | Papers |
|--------|--------|
| quantum-ML | 2 |
| variational | 2 |
| classical-simulation | 2 |
| quantum-SVM | 1 |

## Open Questions

- How does the proposed QSVM algorithm perform under varying market conditions (e.g., high volatility, black swan events)? — [[2024_Bhasin_EnhancingQuantumMachine]]
- What is the impact of quantum hardware noise on the algorithm's performance, and how effective are the proposed noise mitigation techniques in practice? — [[2024_Bhasin_EnhancingQuantumMachine]]
- Can the algorithm maintain its performance advantage when scaled to larger portfolios (e.g., 100+ assets) or more complex financial instruments? — [[2024_Bhasin_EnhancingQuantumMachine]]
- How does the QSVM compare to hybrid quantum-classical approaches (e.g., VQE, QAOA) for portfolio optimization? — [[2024_Bhasin_EnhancingQuantumMachine]]
- What are the computational resource requirements (e.g., qubit count, circuit depth) for practical deployment of the algorithm? — [[2024_Bhasin_EnhancingQuantumMachine]]
- How sensitive is the algorithm to hyperparameter tuning, and what are the optimal configurations for different financial datasets? — [[2024_Bhasin_EnhancingQuantumMachine]]
- What are the implications of using synthetic or simplified financial data versus real-world, high-frequency market data? — [[2024_Bhasin_EnhancingQuantumMachine]]
- Validate the algorithm on real quantum hardware (e.g., IBM Quantum, Rigetti) to assess practical performance under noise and hardware constraints — [[2024_Bhasin_EnhancingQuantumMachine]]
- Extend the study to include comparisons with state-of-the-art classical portfolio optimization methods (e.g., deep reinforcement learning, convex optimization) — [[2024_Bhasin_EnhancingQuantumMachine]]
- Explore hybrid quantum-classical approaches to leverage the strengths of both paradigms for financial applications — [[2024_Bhasin_EnhancingQuantumMachine]]
