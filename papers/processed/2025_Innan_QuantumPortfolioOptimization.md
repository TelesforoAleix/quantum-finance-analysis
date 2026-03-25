---
aliases:
- Quantum Portfolio Optimization with Expert Analysis Evaluation
- Quantum Portfolio Optimization Expert
authors:
- Nouhaila Innan
- Ayesha Saleem
- Alberto Marchisio
- Muhammad Shafique
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/QCE65121.2025.10344
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- QAOA
- VQE
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:09:51.740872'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:09:55.350302'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:10:30.564982'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:11:01.685380'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:11:31.948620'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:11:41.092105'
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
- method/QAOA
- method/VQE
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum Portfolio Optimization with Expert Analysis Evaluation
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper benchmarks two variational quantum algorithms, QAOA and SamplingVQE, for solving QUBO-formulated portfolio optimization problems using real financial market data and different ansatz architectures and circuit depths. The authors show that while these quantum methods can effectively minimize the cost function, the resulting portfolios often lack diversification and realistic risk profiles, especially when judged against forward-looking performance. To address this, they propose an Expert Analysis Evaluation framework in which financial professionals assess the economic soundness and market feasibility of quantum-generated portfolios, highlighting the need to integrate domain expertise into quantum-assisted financial decision-making.
## Methodology
This conference paper presents an empirical benchmarking study of quantum portfolio optimization combined with a post hoc expert-evaluation framework. The authors formulate mean-variance portfolio selection as a QUBO problem with a cardinality constraint enforced through a penalty term, then map the QUBO to an Ising-style cost Hamiltonian using the standard binary-to-Pauli-Z transformation. They compare two variational quantum optimization approaches—QAOA and SamplingVQE—on small portfolio instances with 4 and 10 assets. For SamplingVQE, they test multiple ansatz families (TwoLocal, EfficientSU2, PauliTwoDesign, RealAmplitudes), varying circuit depth and random seed to study convergence, expressibility, and stability. Optimization performance is assessed through objective-function trajectories and cost differences across iterations, while portfolio outputs are analyzed via sampled bitstring probability histograms and selected asset combinations. Beyond algorithmic convergence, the study introduces an Expert Analysis Evaluation framework in which financially knowledgeable reviewers assess the feasibility of the generated portfolios in terms of diversification, liquidity, investor suitability, and practical market relevance. The portfolios are also evaluated on a forward period after the training/evaluation window to compare future average returns of the selected asset sets.

**Algorithms used:** QAOA, SamplingVQE, COBYLA, MinimumEigenOptimizer
**Frameworks:** Qiskit, qiskit-finance, qiskit_aer, qiskit.circuit.library, qiskit_algorithms, qiskit_optimization, yfinance

**Experimental setup:** Experiments were run on simulated gate-based quantum circuits for two problem sizes: 4 assets (4 qubits) and 10 assets (10 qubits). QAOA used the built-in alternating-operator ansatz, while SamplingVQE was tested with TwoLocal, EfficientSU2, PauliTwoDesign, and RealAmplitudes ansatz circuits. All circuits used full entanglement. Circuit depths of 2, 4, 6, 8, and 10 were evaluated, each repeated with five random seeds. The optimizer was COBYLA, the number of measurement shots was fixed at 1024, and all runs were performed on the QASM simulator through Qiskit/Qiskit Aer.

**Dataset:** Historical stock price data from Yahoo Finance covering December 2024 to May 2025 for two asset universes: a 4-asset set (AAPL, GOOG, MSFT, TSLA) and a 10-asset set (AAPL, GOOG, MSFT, TSLA, AMZN, NVDA, GS, MS, NKE, KO). A future evaluation period in June 2025 was used for expert-oriented out-of-sample portfolio return assessment.
## Findings
- [supported] The paper benchmarks QAOA and SamplingVQE for QUBO-based portfolio optimization on 4-asset and 10-asset problems using historical Yahoo Finance data from Dec 2024 to May 2025, with all experiments run on a QASM simulator rather than real quantum hardware.
- [supported] Both QAOA and SamplingVQE variants generally achieved downward objective-function convergence, but convergence quality did not reliably translate into financially viable portfolios.
- [supported] In the 4-asset setting, QAOA showed the highest instability and variance across circuit depths, while RealAmplitudes, TwoLocal, EfficientSU2, and PauliTwoDesign exhibited smoother convergence behavior.
- [supported] For 4 assets, PauliTwoDesign improved its converged objective value from approximately -0.85 at depth 2 to around -1.0 at depth 10.
- [supported] For 4 assets, RealAmplitudes was reported as the most evaluation-efficient ansatz, consistently converging in fewer than 100 evaluations across all tested depths.
- [supported] In the 10-asset setting, QAOA remained high-variance at low depths but improved with depth, moving from values near -2.0 to more stable convergence below -2.0 at depth 10.
- [supported] In the 10-asset setting, PauliTwoDesign converged near -2.0 across depths, while RealAmplitudes, TwoLocal, and EfficientSU2 typically converged between about -0.5 and -1.0.
- [supported] For TwoLocal, PauliTwoDesign, and RealAmplitudes on 10 assets, convergence variance narrowed at greater depths, indicating more stable optimization; QAOA instead showed increasing variance with depth.
- [supported] In the 4-asset case, shallow-depth circuits sometimes produced more financially sensible portfolios than deeper circuits; for example, RealAmplitudes and EfficientSU2 at depth 2 selected [GOOG, MSFT], while RealAmplitudes at depth 10 selected the weaker [AAPL, TSLA] portfolio.
- [supported] In the 10-asset case, deeper circuits tended to produce more diversified and financially plausible portfolios, with Coca Cola frequently appearing in depth-10 solutions across ansatzes.
- [supported] TwoLocal and EfficientSU2 at depth 10 produced the most balanced 10-asset portfolios, typically including GOOG, KO, GS, and either AMZN or NVDA.
- [supported] Expert evaluation on June 2025 forward returns showed that in the 4-asset case only the [GOOG, MSFT] portfolio had a positive subsequent average return (0.95%), while portfolios containing AAPL and/or TSLA underperformed.
- [supported] In the 10-asset case, 4 of 5 evaluated portfolios had positive June 2025 average returns, ranging from 0.34% to 1.62%, while the [AAPL, TSLA, NVDA, MS, KO] portfolio returned -0.39%.
- [supported] The highest-returning June 2025 portfolio identified by expert analysis was [GOOG, MSFT, KO, GS, NVDA] with a 1.99% average return, but this exact portfolio was not generated by any tested circuit.
- [supported] The authors conclude that expert review is necessary because quantum optimization based only on historical data can produce portfolios that satisfy the mathematical objective yet fail practical criteria such as diversification, risk realism, and forward-looking feasibility.
- [speculative] The paper argues that quantum computing may offer scalable help for NP-hard portfolio optimization by efficiently narrowing the candidate solution space, but this advantage is not empirically demonstrated against classical baselines in the study.

**Results summary:** This conference paper evaluates QAOA and SamplingVQE-based portfolio optimization on 4-qubit and 10-qubit QUBO instances derived from real market data, using simulator-based experiments with multiple ansatzes, depths, and random seeds. The main empirical result is that most quantum configurations achieve cost-function minimization, and deeper circuits often improve convergence stability in the larger 10-asset case. However, the study finds a clear mismatch between optimization convergence and financial usefulness: some portfolios with good objective values are poorly diversified or perform badly in a subsequent out-of-sample month. In the 4-asset case, only the [GOOG, MSFT] portfolio produced a positive June 2025 return, while portfolios containing AAPL or TSLA generally underperformed. In the 10-asset case, deeper TwoLocal and EfficientSU2 circuits generated the most plausible diversified portfolios, and 4 of 5 evaluated portfolios had positive forward returns, though the best-performing expert-identified portfolio was not produced by the quantum circuits. Overall, the paper's central claim is that expert analysis is a necessary complement to quantum portfolio optimization outputs.

**Performance claims:**
- 4-asset experiments used 4 qubits; 10-asset experiments used 10 qubits
- Historical training/evaluation window: December 2024 to May 2025; forward test window: June 2025
- All experiments used 1024 measurement shots, COBYLA optimizer, depths 2/4/6/8/10, and 5 random seeds
- For 4 assets, PauliTwoDesign converged from approximately -0.85 at depth 2 to around -1.0 at depth 10
- For 4 assets, RealAmplitudes converged in fewer than 100 evaluations across all depths
- For 10 assets, QAOA improved from values near -2.0 to more stable convergence below -2.0 at depth 10
- For 10 assets, RealAmplitudes, TwoLocal, and EfficientSU2 typically converged between about -0.5 and -1.0
- June 2025 portfolio return for [GOOG, MSFT]: 0.95%
- June 2025 portfolio return for [AAPL, TSLA]: -3.17%
- June 2025 portfolio return for [GOOG, TSLA]: -3.71%
- June 2025 portfolio return for [MSFT, TSLA]: -1.33%
- June 2025 portfolio return for [GOOG, MSFT, KO, GS, AMZN]: 1.34%
- June 2025 portfolio return for [GOOG, MSFT, KO, GS, NVDA]: 1.99%
- June 2025 portfolio return for [GOOG, AMZN, NVDA, GS, KO]: 1.62%
- June 2025 portfolio return for [AAPL, TSLA, NVDA, MS, KO]: -0.39%
- June 2025 portfolio return for [AAPL, MSFT, AMZN, GS, KO]: 0.34%
- 4 of 5 evaluated 10-asset portfolios had positive forward returns
## Quantum advantage claim
**Classification:** speculative

The paper suggests quantum computing could help with NP-hard portfolio optimization and scalable candidate generation, but it provides only simulator-based results, no classical benchmark comparison, and no empirical demonstration of quantum advantage.
## Limitations
- Quantum algorithms achieved cost-function convergence but often produced portfolios that violated practical financial criteria such as diversification and realistic risk exposure.
- The models rely on historical pricing data and do not capture evolving market dynamics, geopolitical risks, or investor-specific preferences.
- Experiments were limited to small problem sizes of 4 and 10 assets (4 and 10 qubits), restricting conclusions about scalability.
- All results were obtained on a QASM simulator rather than real quantum hardware.
- The paper explicitly notes that real hardware noise and decoherence may further degrade output quality compared with simulator-based results.
- The historical dataset covers only a six-month period (December 2024 to May 2025), limiting temporal robustness.
- Future performance validation uses only a short follow-up period in June 2025, which is a narrow test of out-of-sample generalization.
- QAOA showed high variance and sensitivity to circuit depth and parameter initialization, especially in the 10-asset setup.
- Many ansatz configurations produced multiple high-probability bitstrings, indicating selection uncertainty and instability.
- The formulation assumes equal unit asset prices and full budget usage, which simplifies away realistic portfolio construction constraints.
- The risk-aversion parameter is fixed at q = 0.5, so results may not generalize across different investor risk profiles.
- The QUBO penalty parameter is heuristically set to n/2 without sensitivity analysis.
- The expert analysis stage is qualitative and depends on human judgment, which may introduce subjectivity and limit reproducibility.
- [inferred] No direct comparison is reported against strong classical portfolio optimization baselines, making it difficult to assess any practical quantum advantage.
- [inferred] The asset universe is small and concentrated in a few well-known equities, which may bias findings and underrepresent broader financial markets.
- [inferred] The study uses only five random seeds and 1024 shots per experiment, which may be insufficient for robust statistical characterization.
- [inferred] No noise-mitigation, error-mitigation, or hardware-aware transpilation analysis is provided.
- [inferred] No transaction costs, slippage, liquidity constraints, turnover limits, or market impact are modeled despite their importance in production portfolio optimization.
- [inferred] The conference-paper format may impose page-limit constraints that reduce methodological and reproducibility detail.
## Open questions
- How well do the observed results scale beyond 10 assets to financially meaningful portfolio sizes?
- Will the relative behavior of QAOA and SamplingVQE ansatz choices persist on real quantum hardware under noise and decoherence?
- How sensitive are portfolio outcomes to the choice of risk-aversion parameter and QUBO penalty strength?
- Can convergence metrics be augmented so that they better correlate with financially viable portfolio quality rather than only objective minimization?
- How should expert judgment be systematically integrated into the optimization loop rather than only as a post-processing filter?
- What is the best way to incorporate forward-looking information, macroeconomic signals, and geopolitical risk into quantum portfolio optimization?
- How reproducible and consistent are expert evaluations across different financial professionals?
- Why did some deeper circuits still select underperforming assets such as Apple or Tesla despite improved convergence?
- Under what conditions do deeper circuits improve portfolio quality versus merely increasing instability or reducing interpretability?
- [inferred] Is there any measurable advantage over state-of-the-art classical solvers once realistic constraints and larger datasets are included?
- [inferred] How robust are the findings across longer time horizons, different market regimes, and broader asset classes?

**Future work:**
- Develop adaptive, expert-guided quantum financial systems that respond to market fluctuations and investor preferences.
- Incorporate probabilistic forecasting into the portfolio optimization framework.
- Explore alternative risk models beyond the current mean-variance setup.
- Integrate behavioral or ethical investment preferences into the optimization process.
- Further refine portfolio selection using future expectations, real-time dynamics, and investor-specific constraints.
- Extend the framework so that quantum optimization and expert evaluation are more tightly integrated.
- Evaluate the approach on real quantum hardware to assess the impact of noise and decoherence.
- Test larger and more diverse asset universes to study scalability and diversification effects.
- [inferred] Benchmark against strong classical and hybrid classical-quantum baselines.
- [inferred] Add realistic market frictions such as transaction costs, liquidity constraints, and turnover penalties.
- [inferred] Perform longer-horizon and multi-period backtesting across different market regimes.
- [inferred] Study sensitivity to hyperparameters such as circuit depth, shot count, optimizer choice, penalty coefficient, and risk-aversion setting.
## Key ideas
- #idea:hybrid-approach — The paper combines QUBO-based quantum portfolio optimisation with post hoc expert financial evaluation to assess diversification, liquidity, investor suitability, and market realism.
- #idea:near-term-feasibility — QAOA and SamplingVQE can minimise the portfolio QUBO objective on very small simulated instances (4 and 10 assets), showing limited NISQ-era applicability in constrained settings.
- #idea:hybrid-approach — The study argues that optimisation loss alone is insufficient; domain experts are needed to judge whether quantum-generated portfolios are economically sensible.
- #idea:quantum-advantage — The paper speculates that quantum methods may eventually help with NP-hard portfolio optimisation by narrowing candidate solution spaces, but does not demonstrate this empirically.
- #idea:near-term-feasibility — Different ansatz choices and circuit depths materially affect convergence and portfolio quality, with some deeper circuits improving stability in the 10-asset case.
- #idea:hybrid-approach — Forward-period evaluation reveals a mismatch between mathematically good solutions and financially useful portfolios, motivating tighter integration of financial knowledge into the optimisation loop.
## Contradictions
- The paper suggests possible quantum scalability benefits for portfolio optimisation, but all evidence comes from 4- and 10-qubit QASM simulations with no comparison to strong classical baselines, contradicting any substantive superiority claim (#contradiction:classical-vs-quantum).
- Although deeper circuits sometimes improve convergence and diversification in the 10-asset case, this does not consistently hold in the 4-asset case, and the study provides no evidence that the approach scales to realistic portfolio sizes (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input data consisted of Yahoo Finance stock prices for 4-asset and 10-asset universes over a 6-month period from 2 Dec 2024 to 30 May 2025. The 4-asset universe included Apple, Google, Microsoft, and Tesla; the 10-asset universe added Amazon, NVIDIA, Goldman Sachs, Morgan Stanley, Nike, and Coca Cola. From these prices, expected returns and covariance matrices were derived for mean-variance optimization, then converted into a QUBO with a budget/cardinality constraint. The QUBO penalty parameter was set to alpha = n/2, and the risk-aversion parameter was fixed at q = 0.5. For forward evaluation, stock prices from 2 Jun 2025 to 20 Jun 2025 were used to compute future returns of selected portfolios.

### Process
1. Collect historical stock price data from Yahoo Finance for the selected assets. 2. Compute portfolio optimization inputs, including expected returns and covariance matrix. 3. Formulate the constrained mean-variance portfolio selection problem as a QUBO with a penalty enforcing selection of B assets. 4. Map the QUBO to a cost Hamiltonian using xi = (1 - Zi)/2. 5. Solve the problem using QAOA and SamplingVQE. 6. For SamplingVQE, instantiate four ansatz types: TwoLocal (Rx, Ry, Cz), EfficientSU2, PauliTwoDesign, and RealAmplitudes; for QAOA, use the built-in alternating operator ansatz. 7. Run each configuration with full entanglement at depths 2, 4, 6, 8, and 10, repeating each experiment with five random seeds. 8. Optimize variational parameters using COBYLA with 1024 shots per circuit evaluation on the QASM simulator. 9. Track convergence using objective-function values over iterations and the difference between successive costs. 10. Analyze sampled bitstring probability histograms to identify the most likely portfolio allocations. 11. Compare generated portfolios qualitatively for diversification and composition. 12. Evaluate selected portfolios on a future June 2025 period by computing average asset returns. 13. Apply expert analysis to judge feasibility, diversification, liquidity, and investor suitability of the quantum-generated portfolios.

### Output
Reported outputs include convergence curves of the objective function across iterations, stability trends across ansatz architectures and circuit depths, probability histograms of sampled bitstrings representing candidate portfolios, selected portfolio compositions for different methods/depths, and average future portfolio returns in June 2025. Comparisons are made primarily between QAOA and multiple SamplingVQE ansatz variants, as well as across circuit depths and random seeds. The study emphasizes that low optimization loss does not necessarily correspond to financially viable portfolios, and supplements algorithmic results with expert qualitative assessment.

### Parameters
- qubits: [4, 10]
- circuit_depths: [2, 4, 6, 8, 10]
- shots: 1024
- optimizer: COBYLA
- random_seeds: 5
- risk_aversion_q: 0.5
- qubo_penalty_alpha: n/2
- entanglement: full
- samplingvqe_ansatz: ['TwoLocal', 'EfficientSU2', 'PauliTwoDesign', 'RealAmplitudes']
- twolocal_gates: ['Rx', 'Ry', 'Cz']

### Hardware
Qiskit Aer QASM simulator was used for all experiments; no real quantum hardware was used. The software stack shown includes qiskit-finance, qiskit_finance.data_providers, qiskit_aer.primitives, qiskit.circuit.library, qiskit_algorithms.optimizers, qiskit_finance.applications.optimization, qiskit_algorithms, qiskit_optimization.algorithms, qiskit_algorithms.utils, and qiskit.result.

### Reproducibility
The paper provides substantial methodological detail on problem formulation, asset sets, time periods, ansatz choices, depths, optimizer, shots, and simulator, which supports partial replication. Data appears publicly obtainable from Yahoo Finance/yfinance. However, no code repository or exact implementation details such as stopping criteria, full optimizer settings, and all preprocessing steps are provided, so reproducibility is moderate rather than complete.
