---
aliases:
- 'Q-PORT: Quantum Portfolio Optimization with Resource-Eﬃcient Encoding and Scalability
  Analysis'
- Q PORT Quantum Portfolio
authors:
- Alberto Marchisio
- Muhammad Umair Hafeez
- Nouhaila Innan
- Muhammad Kashif
- Muhammad Shafique
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1007/978-3-032-13852-1_34
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: QUEST-IS 2025, Communications in Computer and Information Science
  (CCIS 2743), Springer Nature Switzerland
methodology_tags:
- QAOA
- VQE
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:13:23.603559'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:13:28.016965'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:13:47.885428'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:14:15.807399'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:14:44.498380'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:14:53.838299'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- topic/risk-modelling
- method/QAOA
- method/VQE
- method/QUBO
- method/variational
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: 'Q-PORT: Quantum Portfolio Optimization with Resource-Eﬃcient Encoding and
  Scalability Analysis'
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2026
zotero_key: ''
---

## Abstract summary
The paper introduces Q-PORT, a methodology to study how different qubit–asset encoding schemes and circuit depths affect the performance and scalability of quantum portfolio optimization using VQE and QAOA. Using historical stock data and a QUBO formulation, the authors compare multi-qubit-per-stock and multi-stock-per-qubit encodings against a classical mean-variance benchmark. They show that adding qubits per stock offers little accuracy benefit but higher resource cost, while encoding multiple stocks per qubit substantially reduces qubit requirements with only minor precision loss, especially for deeper QAOA circuits.
## Methodology
The paper presents Q-PORT, an empirical methodology for studying scalability trade-offs in quantum portfolio optimization under different stock-to-qubit encoding schemes. The authors first collect historical stock price data and compute expected returns and covariance matrices, then use classical Mean-Variance Optimization (MVO) as a benchmark. They reformulate the portfolio optimization problem as a QUBO and solve it with hybrid quantum-classical methods, specifically QAOA and VQE. The core methodological contribution is a systematic comparison of two encoding strategies: (1) multi-qubit representation per stock, where each asset is redundantly mapped to multiple qubits and final stock allocation is determined by majority voting after measurement, and (2) multi-stock encoding per qubit, where several assets are compressed into one qubit and candidate portfolios are evaluated and clustered using k-means. The study varies ansatz type and circuit repetitions/layers from 1 to 5 to analyze the effect of circuit depth on solution quality and scalability. Results are compared against the classical MVO-optimal portfolio using ranking-based evaluation, with experiments conducted entirely in simulation to avoid hardware noise.

**Algorithms used:** QAOA, VQE, COBYLA, k-means, Mean-Variance Optimization (MVO), QUBO
**Frameworks:** Google Colab, Yahoo Finance

**Experimental setup:** Experiments were run using statevector-based quantum simulators rather than real QPUs. The quantum circuits used layered ansatzes with Hadamard initialization, parameterized RZ rotations for the cost Hamiltonian, two-qubit RZZ entangling gates reflecting the QUBO structure, and RX mixer gates. Circuit repetitions (layers) were varied from 1 to 5. The classical optimizer was COBYLA with a maximum of 5000 iterations. Simulations were executed on Google Colab instances with Intel Xeon E5 CPUs.

**Dataset:** Historical stock price data from Yahoo Finance covering January 1, 2020 to January 1, 2024. The paper evaluates portfolios of 3 stocks (Apple, Microsoft, Google), 4 stocks (Apple, Microsoft, Google, Amazon), and 12 stocks (Apple, Microsoft, Google, Amazon, Tesla, Nvidia, Meta, Netflix, JP Morgan, Disney, Visa, Berkshire Hathaway Inc.). Expected returns and covariance matrices were derived from these data.
## Findings
- [supported] All experiments were conducted on statevector-based simulators rather than real quantum hardware, so results reflect noiseless simulation performance only.
- [supported] Increasing circuit repetitions (1 to 5 layers) generally improved alignment between quantum solutions and the classical mean-variance optimization (MVO) benchmark, especially for QAOA.
- [supported] In 3-stock experiments, QAOA consistently ranked the classically optimal portfolio among the top positions even at low circuit depth, while VQE typically required higher depth to achieve competitive rankings.
- [supported] In 4-stock experiments, both QAOA and VQE showed higher variance than in the 3-stock case, but higher circuit repetitions still tended to improve rankings overall.
- [supported] Increasing the number of qubits per stock from 1 to 3 produced negligible improvement in solution quality relative to the classical MVO benchmark and often worsened ranking stability.
- [supported] Multi-qubit-per-stock encodings increased optimization difficulty by enlarging the solution space, leading to greater variability and poorer ranking performance, particularly at lower circuit depths.
- [supported] For a 12-stock portfolio, compressing 2 stocks per qubit reduced qubit requirements from 12 to 6 while QAOA still often preserved the classically optimal solution within the top few ranks.
- [supported] For a 12-stock portfolio, compressing 3 stocks per qubit reduced qubit requirements from 12 to 4 and QAOA still achieved competitive rankings, especially at higher circuit depths, though with some degradation from compression.
- [supported] VQE was generally more sensitive to compressed encodings than QAOA and benefited more from deeper circuits to stabilize performance.
- [supported] The paper concludes that multi-stock encoding per qubit is a more resource-efficient scaling strategy than multi-qubit representation per stock, with only minor precision loss under the tested settings.
- [speculative] The authors suggest these findings provide a pathway toward near-term financial applications and scalable quantum portfolio optimization under NISQ constraints, but this was not validated on real hardware or against strong classical baselines beyond MVO ranking comparison.

**Results summary:** This peer-reviewed empirical study evaluates Q-PORT, a methodology for quantum portfolio optimization using VQE and QAOA under different encoding strategies and circuit depths. Using historical stock data from Yahoo Finance for 3-, 4-, and 12-stock portfolios, the authors benchmarked quantum outputs against classical mean-variance optimization (MVO). All experiments were run on noiseless statevector simulators with COBYLA optimization and 1 to 5 circuit layers. The main empirical result is that assigning multiple qubits per stock does not materially improve solution quality and can degrade ranking performance by enlarging the search space, whereas encoding multiple stocks per qubit substantially reduces qubit requirements with only limited loss in alignment to the classical optimum. Across settings, QAOA generally outperformed or was more robust than VQE, particularly at lower depths and under compressed encodings. No confidence intervals or statistical significance tests are reported, and no real-hardware demonstration or quantum speedup is shown.

**Performance claims:**
- Simulations used 1 to 5 circuit repetitions (layers) for both QAOA and VQE
- Historical data covered 2020-01-01 to 2024-01-01
- Portfolio sizes evaluated: 3 stocks, 4 stocks, and 12 stocks
- Risk tolerance fixed at 0.2
- COBYLA optimizer run with a maximum of 5000 iterations
- Multi-qubit-per-stock tests scaled from 1 to 3 qubits per stock: 3-stock case used 3, 6, and 9 qubits; 4-stock case used 4, 8, and 12 qubits
- Multi-stock-per-qubit tests for the 12-stock case used 1, 2, and 3 stocks per qubit, reducing qubit counts from 12 to 6 and 4
- QAOA often kept the classical optimum within the top few ranks in the 12-stock, 2-stocks-per-qubit setting
- QAOA maintained competitive rankings even in the 12-stock, 3-stocks-per-qubit setting, particularly at higher depths
## Quantum advantage claim
**Classification:** not-applicable

The paper does not demonstrate quantum advantage or speedup over classical methods. It reports simulator-based comparisons of solution ranking relative to a classical MVO benchmark and focuses on resource-efficiency trade-offs in encoding strategies rather than computational advantage.
## Limitations
- Experiments were conducted only on statevector-based simulators, avoiding sampling noise and real-device effects; results therefore do not validate performance on actual NISQ hardware.
- The paper explicitly acknowledges that NISQ noise and hardware limitations remain a challenge for practical scalability.
- Evaluation uses small problem sizes for the multi-qubit-per-stock study (3-stock and 4-stock cases), limiting evidence for scalability.
- Even the larger experiment considers only a 12-stock portfolio, which is still far from realistic institutional-scale portfolio optimization.
- Historical data were drawn from a limited set of mostly large-cap technology and US equities from Yahoo Finance over 2020-01-01 to 2024-01-01, restricting dataset diversity and external validity.
- The risk tolerance parameter was fixed at 0.2 across all experiments, so robustness to different investor preferences was not assessed.
- The investment budget was fixed as total number of stocks minus one, limiting evaluation under alternative budget and allocation constraints.
- Only circuit repetitions from 1 to 5 were explored, so conclusions about deeper ansatz behavior and scaling remain limited.
- The study uses COBYLA with a maximum of 5000 iterations but does not analyze optimizer sensitivity or convergence stability across optimizers.
- Performance is primarily evaluated by the ranking of the classical MVO-optimal portfolio in the quantum output distribution, which provides a narrow metric and may not fully capture portfolio quality or financial utility.
- Multi-qubit representations per stock were found to increase optimization complexity and can degrade solution quality unless deeper, more expressive circuits are used.
- Multi-stock encoding per qubit introduces approximation errors and loss of individual stock granularity, especially under aggressive compression.
- [inferred] No experiments on real quantum hardware were performed, so claims about near-term applicability are not empirically demonstrated.
- [inferred] No explicit noise model or noise-mitigation strategy was evaluated, despite the paper motivating the work around NISQ limitations.
- [inferred] The comparison baseline is classical Mean-Variance Optimization only; there is no comparison against stronger classical combinatorial or heuristic portfolio solvers.
- [inferred] Reproducibility is limited because the paper does not provide implementation details such as random seeds, exact QUBO coefficients, code availability, or full hyperparameter settings for all runs.
- [inferred] The use of majority voting in multi-qubit encoding and k-means clustering in compressed encoding may introduce heuristic biases that are not separately ablated.
- [inferred] The study assumes historical return/covariance estimates are adequate inputs, but estimation error and market nonstationarity are not examined.
- [inferred] The selected ansatz uses a fixed connectivity pattern, which may not reflect hardware-native constraints or alternative ansatz designs that could materially affect results.
- [inferred] The paper does not assess runtime, wall-clock cost, or end-to-end computational advantage versus classical methods, so production scalability remains unclear.
## Open questions
- Can multi-qubit representations per stock improve solution fidelity enough to justify their additional qubit overhead?
- Can multi-stock encodings per qubit reduce resource requirements while preserving acceptable solution quality?
- How well do the reported simulator-based results transfer to noisy real quantum hardware?
- How does performance change for portfolios substantially larger than 12 assets?
- What circuit depth is required for compressed encodings to maintain solution quality as portfolio size grows?
- Why does QAOA appear more resilient than VQE under compressed multi-stock encodings, and does this hold more generally?
- How sensitive are the results to the choice of risk tolerance, budget constraints, and other portfolio formulation parameters?
- What is the impact of approximation errors from compressed encodings on actual financial decision quality, not just ranking against MVO?
- Would alternative ansatz designs, optimizers, or decoding strategies outperform the configurations tested here?
- Can the methodology generalize to more complex and realistic financial datasets and constraints?

**Future work:**
- Extend the experimental evaluation to larger-scale portfolios.
- Test the methodology on more complex financial datasets.
- Further validate the generalizability and robustness of the proposed methodology.
- [inferred] Evaluate Q-PORT on real NISQ hardware rather than only on statevector simulators.
- [inferred] Incorporate explicit noise models and noise-mitigation techniques to assess practical hardware performance.
- [inferred] Benchmark against stronger classical optimization baselines and heuristics beyond classical MVO.
- [inferred] Study sensitivity to different risk tolerances, budgets, and realistic portfolio constraints such as transaction costs and cardinality limits.
- [inferred] Explore deeper circuits, alternative ansatz families, and different classical optimizers to improve convergence and scalability.
- [inferred] Perform ablation studies on majority voting, candidate generation, and k-means clustering used in the encoding/decoding pipeline.
- [inferred] Investigate production-oriented metrics such as runtime, resource cost, and robustness under changing market conditions.
## Key ideas
- #idea:near-term-feasibility — Q-PORT studies NISQ-oriented trade-offs in portfolio optimisation by varying stock-to-qubit encoding schemes and circuit depth.
- #idea:hybrid-approach — The workflow is hybrid quantum-classical: classical return/covariance estimation, QUBO construction, COBYLA optimisation, and k-means-assisted compressed encoding are combined with QAOA/VQE.
- #idea:near-term-feasibility — Multi-stock-per-qubit encoding reduces qubit requirements substantially (e.g., 12 assets mapped to 6 or 4 qubits) with only modest degradation in ranking quality under tested settings.
- #idea:near-term-feasibility — QAOA appears more robust than VQE, especially at low depth and under compressed encodings, suggesting it may be the more practical variational approach for this formulation.
## Contradictions
- The paper suggests a pathway toward near-term scalable portfolio optimisation, but its evidence is limited to noiseless statevector simulation on small instances (3, 4, and 12 assets), which contradicts stronger scalability implications.
- Any implicit claim of practical NISQ readiness is weakened by the absence of real-hardware validation, explicit noise modelling, runtime analysis, or comparison against stronger classical combinatorial baselines beyond mean-variance optimisation ranking.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Yahoo Finance historical stock prices from 2020-01-01 to 2024-01-01 for three portfolio universes: 3 assets (Apple, Microsoft, Google), 4 assets (Apple, Microsoft, Google, Amazon), and 12 assets (Apple, Microsoft, Google, Amazon, Tesla, Nvidia, Meta, Netflix, JP Morgan, Disney, Visa, Berkshire Hathaway Inc.). Inputs were transformed into expected returns and covariance matrices for MVO and QUBO formulation. Risk tolerance was fixed at 0.2, and the budget constraint was set to number of stocks minus one.

### Process
1. Collect historical stock prices from Yahoo Finance. 2. Compute expected returns and covariance matrices. 3. Solve the classical portfolio problem with Mean-Variance Optimization to obtain a benchmark optimal allocation. 4. Reformulate the portfolio optimization problem as a QUBO including return, risk, budget, and allocation constraints. 5. Encode the QUBO using either (a) multi-qubit per stock encoding with majority voting over redundant qubits, or (b) multi-stock per qubit compressed encoding, where candidate portfolios are generated and grouped using k-means based on return-risk characteristics. 6. Solve the encoded problem using QAOA and VQE with layered ansatz circuits composed of H, RZ, RZZ, and RX gates. 7. Vary circuit depth by changing repetitions/layers from 1 to 5. 8. Optimize variational parameters with COBYLA up to 5000 iterations. 9. Compare the ranking position of the classical MVO-optimal portfolio within the quantum-generated output distributions across algorithms, encodings, and depths.

### Output
The main reported output is the ranking of the classically MVO-optimal portfolio within the sorted distribution of portfolios produced by QAOA and VQE; lower rank indicates better agreement with the classical optimum, and rank 1 means the quantum method identifies the classical optimum as top solution. Comparisons are made across encoding strategies, qubit-resource configurations, and circuit depths. The classical baseline is Mean-Variance Optimization. Qualitative comparisons between QAOA and VQE are also reported, with QAOA generally showing stronger robustness under compressed encodings.

### Parameters
- layers_repetitions: {'min': 1, 'max': 5}
- risk_tolerance: 0.2
- budget_rule: number of stocks minus one
- optimizer: COBYLA
- max_optimizer_iterations: 5000
- qubit_configurations: {'multi_qubit_per_stock': ['3 stocks -> 3, 6, 9 qubits for 1, 2, 3 qubits/stock', '4 stocks -> 4, 8, 12 qubits for 1, 2, 3 qubits/stock'], 'multi_stock_per_qubit': ['12 stocks -> 12, 6, 4 qubits for 1, 2, 3 stocks/qubit']}
- ansatz_gates: ['H', 'RZ', 'RZZ', 'RX']

### Hardware
Statevector-based simulator; no real quantum hardware used. Experiments executed on Google Colab with Intel Xeon E5 CPUs. The paper explicitly states simulations were used to avoid sampling noise from real QPUs. No cloud QPU provider, noise model, or transpilation settings are reported.

### Reproducibility
Data source is public (Yahoo Finance), and the paper provides key methodological details such as asset sets, date range, optimizer, layer range, risk tolerance, and encoding strategies. However, no code repository, exact implementation framework, or full hyperparameter/configuration details are provided, so replication is partially feasible but not fully straightforward.
