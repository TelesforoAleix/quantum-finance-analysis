---
aliases:
- Quantum walk-based portfolio optimisation
- Quantum walk based portfolio
authors:
- N. Slate
- E. Matwiejew
- S. Marsh
- J. B. Wang
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Quantum
methodology_tags:
- QAOA
- variational
- quantum-walk
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:56:02.670279'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:06.163435'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:34.510580'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:09.623862'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:57:41.887281'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:57:56.706159'
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
- method/variational
- method/quantum-walk
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Quantum walk-based portfolio optimisation
topic_tags:
- portfolio-optimisation
year: 2021
zotero_key: ''
---

## Abstract summary
The paper introduces and evaluates a Quantum Walk Optimisation Algorithm (QWOA) for solving the discrete Markowitz portfolio optimisation problem on near-term quantum hardware. It compares QWOA against QAOA and the Quantum Alternating Operator Ansatz using simulated experiments on real financial data sets, analysing search space size, mixer structure, and convergence behaviour. The study shows that by restricting evolution to a carefully indexed subspace of valid, non-degenerate portfolios and using a complete-graph quantum walk mixer, QWOA achieves higher-quality portfolios with fewer iterations and lower variance than the QAOA-based methods.
## Methodology
The study is a peer-reviewed empirical numerical comparison of three quantum approximate optimization methods for discrete Markowitz portfolio optimization with asset-position constraints: standard QAOA, the constrained Quantum Alternating Operator Ansatz variant denoted QAOAz, and a newly proposed Quantum Walk Optimization Algorithm (QWOA). The portfolio problem is formulated using the discrete mean-variance Markowitz objective with ternary asset positions (long, short, no position), a net investment constraint A, and risk-aversion parameter lambda. The authors derive quantum encodings and compare the search-space structure and mixer constructions of the three methods, then evaluate them through classical simulation rather than execution on physical quantum hardware. QAOA uses a soft-constraint penalty added to the objective and a standard X-mixer over the full Hilbert space; QAOAz uses a dual-parity-ring mixer that preserves the constraint but induces disconnected parity bands and degeneracy; QWOA uses an indexing/unindexing scheme to restrict evolution to valid non-degenerate portfolios and applies a continuous-time quantum walk mixer on a complete graph over feasible solutions. Numerical experiments were run with QuOp MPI on two 8-asset Australian stock datasets, using BFGS to optimize the variational parameters over circuit depths p from 1 to 19. For each algorithm and p, results were averaged over 15 repeated runs with the same randomly generated initial parameter seeds drawn uniformly from 0 to 2pi. Performance was assessed primarily by the optimized expected objective value, along with standard deviation across runs, output-state probability concentration on optimal portfolios, and derived expected annual return and annual risk. Baseline comparison included direct comparison among QAOA, QAOAz, and QWOA, with the globally optimal feasible portfolio obtained by classical brute-force enumeration used as a reference minimum objective value.

**Algorithms used:** QAOA, QAOAz, QWOA, BFGS
**Frameworks:** QuOp MPI, Python, Yahoo Finance API

**Experimental setup:** All results were obtained via numerical simulation of the quantum algorithms, not on a real QPU. Simulations were carried out using the QuOp MPI software package in a parallel/distributed-memory environment. The study considered p from 1 to 19 QAOA layers/iterations. Variational parameters gamma and t were classically optimized using the Broyden-Fletcher-Goldfarb-Shanno algorithm; Newton-CG, Nelder-Mead, and Powell were also tested but performed equivalently or worse. For each algorithm and each p, the reported values are the mean and standard deviation over 15 repeats using randomly initialized parameter vectors with entries sampled uniformly from 0 to 2pi. Problem size was n = 8 assets with A = 4 and lambda = 0.5. The corresponding search spaces were 2^16 for QAOA, 1820 for QAOAz, and 266 for QWOA.

**Dataset:** Two empirical financial datasets of daily adjusted closing prices for 8 stocks from the ASX.20 index, downloaded from Yahoo Finance. Data Set A covered 01/01/2017 to 31/12/2018 for AMP, ANZ, AMC, BHP, BXB, CBA, CSL, and IAG. Data Set B covered 24/03/2020 to 06/09/2020 for COVID-19-affected sector stocks FLT, QAN, WEB, REX, AIZ, SYD, SCG, and CTD. Adjusted close prices were used to account for corporate actions such as dividends.
## Experiment details
### Input
Input consisted of two 8-asset stock-price datasets from Yahoo Finance based on daily adjusted close prices. Data Set A: 8 ASX.20 stocks (AMP, ANZ, AMC, BHP, BXB, CBA, CSL, IAG), period 2017-01-01 to 2018-12-31. Data Set B: 8 ASX.20 stocks selected from sectors heavily impacted by COVID-19 (FLT, QAN, WEB, REX, AIZ, SYD, SCG, CTD), period 2020-03-24 to 2020-09-06. Historical prices were used to derive expected returns r_i and covariance matrix sigma_ij for the discrete mean-variance Markowitz objective. Adjusted close prices were chosen to incorporate corporate actions. The optimization setting fixed n = 8 assets, net investment constraint A = 4, and risk-aversion parameter lambda = 0.5. Asset positions were discretized to {long, short, no position} and encoded using two qubits per asset.

### Process
1. Formulate the constrained discrete Markowitz portfolio optimization problem using historical returns and covariances derived from each dataset. 2. Encode each asset with two qubits representing long, short, or no position. 3. Instantiate three quantum optimization methods: (a) QAOA with an X-mixer and soft constraint penalty added to the cost Hamiltonian, initialized in a uniform superposition over the full 2^(2n) space; (b) QAOAz with a dual-parity-ring mixer preserving the investment constraint and an initial state spanning valid parity bands; (c) QWOA with a classical indexing/unindexing procedure over valid non-degenerate portfolios and a continuous-time quantum walk mixer on the complete graph over feasible solutions. 4. For each method and each depth p from 1 to 19, optimize the variational parameters (gamma and t vectors) using BFGS. 5. Repeat each optimization 15 times with randomly initialized parameter values sampled uniformly from 0 to 2pi. 6. Compute the optimized expectation value <psi_f|C|psi_f>, summarize mean and standard deviation across repeats, and inspect output-state probability distributions. 7. Compare against the exact optimum obtained by classical brute-force search over feasible portfolios. 8. Derive expected annual return and expected annual risk from the final state probabilities by weighting each portfolio's return and risk by its measurement probability.

### Output
Reported outputs include the optimized expected objective value <psi_f|C|psi_f> as a function of circuit depth p, mean and standard deviation across 15 runs, probability distributions over output portfolio states, and derived expected annual return and expected annual risk. The main baselines are QAOA and QAOAz, with QWOA as the proposed method. A classical brute-force search over feasible portfolios provides the reference minimum objective value (global optimum). Additional qualitative outputs include search-space sizes, parity-band analyses for QAOAz, and probability mass assigned to optimal or near-optimal portfolios.

### Parameters
- assets: 8
- qubits: 16
- p_range: 1 to 19
- repeats_per_setting: 15
- optimizer: BFGS
- initial_parameter_distribution: uniform on [0, 2pi]
- net_investment_constraint_A: 4
- risk_aversion_lambda: 0.5
- search_space_qaoa: 65536
- search_space_qaoaz: 1820
- search_space_qwoa: 266
- alternative_optimizers_tested: ['Newton-CG', 'Nelder-Mead', 'Powell']

### Hardware
{'execution_type': 'classical numerical simulation', 'simulator_framework': 'QuOp MPI', 'qpu_used': False, 'computing_environment': 'parallel distributed-memory simulation; supported by Pawsey Supercomputing Centre resources'}

### Reproducibility
Moderate reproducibility. The paper provides substantial methodological detail: problem formulation, datasets and tickers, date ranges, parameter settings (n, A, lambda, p range, repeats), optimizer choice, and the simulation package used (QuOp MPI, cited). Data are publicly obtainable from Yahoo Finance. The indexing algorithms and circuit constructions are described in detail. However, no direct code repository for the experiments is explicitly given in the provided text, and some implementation details for preprocessing/return-covariance estimation are not fully specified, so replication appears feasible but not turnkey.
## Findings
- [supported] In numerical simulations of 8-asset portfolio optimization with A=4 and λ=0.5, QWOA consistently achieved better expected solution quality than both QAOA and QAOAz on two real-stock datasets.
- [supported] All reported results are from classical numerical simulation, not execution on real quantum hardware.
- [supported] For n=8 and A=4, the search spaces were 2^16=65,536 for QAOA, 1,820 for QAOAz, and 266 for QWOA.
- [supported] QWOA reduced the search space to 0.406% of QAOA's search space and 14.61% of QAOAz's search space in the tested n=8, A=4 setting.
- [supported] On Data Set A, QAOA showed much larger variability in optimized objective value than the constrained methods, with maximum standard deviation 12.96 versus 0.038 for QAOAz and 0.011 for QWOA.
- [supported] On Data Set B, QAOA again had the largest variability, with maximum standard deviation 12.75 versus 0.61 for QAOAz and 0.115 for QWOA.
- [supported] On Data Set A at p=19, QWOA amplified the optimal portfolio to above 40% measurement probability, while QAOAz left the degenerate optimal solutions below 10^-9 probability in the examined parity band.
- [supported] On Data Set B at p=19, QWOA amplified the optimal portfolio to approximately 20% probability, while QAOAz left the degenerate optimal solutions below 10^-6 probability in the examined parity band.
- [supported] QAOAz exhibited diminishing improvement after about p≈8 on Data Set A and remained about 0.2 above the optimum objective value after 19 iterations.
- [supported] The authors attribute QWOA's better convergence to its smaller non-degenerate feasible search space and fully connected, symmetric mixer over valid solutions.
- [speculative] The paper argues that QWOA's advantages should generalize to other constrained combinatorial optimization problems where the number of valid solutions is not a power of two.
- [speculative] The paper suggests the complete-graph mixer used in QWOA may be close to optimal for combinatorial optimization because of maximal symmetry and graph diameter 1.
- [speculative] The paper frames QWOA as targeted at near-term NISQ computers, but this suitability is not empirically validated on hardware in the study.
- [speculative] Claims of substantial quantum speedups for computationally hard problems are background motivation rather than demonstrated by this paper.

**Results summary:** This peer-reviewed empirical paper compares QAOA, QAOAz, and the Quantum Walk Optimization Algorithm (QWOA) for discrete Markowitz portfolio optimization using classical simulations on two 8-stock datasets derived from ASX market data. With A=4 and λ=0.5, QWOA consistently outperformed QAOA and QAOAz in expected objective value and convergence behavior as the circuit depth parameter p increased. The main empirical explanation is that QWOA searches only the 266 valid non-degenerate portfolios, versus 1,820 valid-but-degenerate states for QAOAz and 65,536 total states for unconstrained QAOA. QWOA also showed much lower run-to-run variability under random parameter initialization. At p=19, QWOA concentrated substantial probability mass on the optimal portfolio (>40% on Data Set A and about 20% on Data Set B), whereas QAOAz failed to amplify the optimal degenerate solutions in the examined parity bands. The study provides evidence of better simulated optimization performance for QWOA, but it does not demonstrate quantum advantage over classical optimization or results on real quantum hardware.

**Performance claims:**
- For n=8, A=4: search space sizes were 65,536 (QAOA), 1,820 (QAOAz), and 266 (QWOA)
- QWOA search space was 0.406% of QAOA's and 14.61% of QAOAz's in the tested setting
- Data Set A maximum standard deviation of optimized objective value: 12.96 (QAOA), 0.038 (QAOAz), 0.011 (QWOA)
- Data Set B maximum standard deviation of optimized objective value: 12.75 (QAOA), 0.61 (QAOAz), 0.115 (QWOA)
- Data Set A at p=19: QWOA amplified the optimal portfolio to >40% probability
- Data Set A at p=19: QAOAz kept the degenerate optimal solutions below 10^-9 probability in the examined parity band
- Data Set B at p=19: QWOA amplified the optimal portfolio to approximately 20% probability
- Data Set B at p=19: QAOAz kept the degenerate optimal solutions below 10^-6 probability in the examined parity band
- Data Set A: QAOAz showed diminishing improvement after about p≈8 and remained approximately 0.2 above the optimum objective value after 19 iterations
- QWOA mixer/indexing complexity claimed as O(n^2) versus O(n) for QAOA and QAOAz mixers
## Quantum advantage claim
**Classification:** speculative

The paper demonstrates improved simulated performance of QWOA relative to QAOA/QAOAz for portfolio optimization, but all results are from classical numerical simulation and there is no demonstrated advantage over classical state-of-the-art solvers or on real quantum hardware.
## Limitations
- Experiments are purely numerical simulations; no execution on real quantum hardware is reported.
- The study is limited to small problem instances with n = 8 assets and fixed constraint settings (A = 4, λ = 0.5).
- Only two datasets are used, both consisting of 8 Australian stocks, limiting external validity and generalizability.
- Results are based on 15 repeats with random initial variational parameters, so outcomes may depend on optimizer initialization.
- The authors note that the classical optimization component suffers from the curse of dimensionality as p increases, causing deterioration in optimization efficiency and increasing the number of circuit shots required.
- QWOA has higher mixing circuit complexity, with overall complexity O(n^2), compared with O(n) for QAOA and QAOAz.
- QAOAz is limited by disconnected parity bands, preventing amplitude transfer between feasible subspaces and constraining reachable performance.
- QAOAz uses an initial state that is efficient to prepare but biased, with probability amplitude binomially distributed across parity bands.
- QAOA includes invalid portfolio states through soft constraints, enlarging the search space and increasing susceptibility to poor local minima.
- QAOA and QAOAz are affected by degeneracy in the portfolio encoding, which biases optimization and can suppress amplification of optimal portfolios.
- [inferred] Despite being motivated for NISQ devices, the paper does not model hardware noise, decoherence, gate errors, readout errors, or noise mitigation.
- [inferred] Resource estimates are asymptotic only; the paper does not provide concrete qubit counts, gate counts, circuit depths, or runtime estimates for practical hardware deployment.
- [inferred] The requirement of two qubits per asset and additional ancilla/register overhead may limit near-term scalability.
- [inferred] The study compares only against QAOA/QAOAz and classical brute-force enumeration for small instances, not against state-of-the-art classical portfolio optimization heuristics or exact solvers on larger instances.
- [inferred] The use of historical Yahoo Finance data and a single Markowitz formulation may not capture realistic market frictions such as transaction costs, liquidity constraints, turnover limits, or multi-period rebalancing.
- [inferred] Reproducibility is only partial: software is named, but full experimental artifacts such as seeds, preprocessing details, and exact optimization settings for all runs are not fully specified in the excerpt.
- [inferred] Claims about applicability to arbitrary black-box optimization problems are broader than the empirical evidence, which is restricted to one portfolio optimization setup.
## Open questions
- How does QWOA perform on larger portfolio instances with substantially more than 8 assets?
- Will the observed simulation advantages of QWOA persist under realistic NISQ noise and limited coherence times?
- What are the practical crossover points where QWOA's reduced search space outweighs its higher O(n^2) mixer complexity on real devices?
- How sensitive are QWOA, QAOA, and QAOAz to the choice of classical optimizer and parameter initialization?
- Can QWOA maintain rapid convergence at low p for more complex financial formulations and constraints?
- How well do these methods perform when realistic portfolio features such as transaction costs, cardinality constraints, and multi-period rebalancing are included?
- To what extent does the complete-graph mixer remain optimal or near-optimal compared with other possible mixer graphs for constrained financial optimization?
- How scalable is the indexing/un-indexing procedure in practice when implemented faultily or noisily on hardware?
- Do the advantages observed on two small ASX datasets generalize to other markets, asset classes, and market regimes?
- How does QWOA compare against strong classical optimization baselines on larger, practically relevant portfolio problems?

**Future work:**
- Test QWOA, QAOA, and QAOAz on real quantum hardware or realistic noisy hardware simulators.
- Scale the experiments to larger numbers of assets and broader ranges of constraint values A and risk-aversion parameters λ.
- Investigate methods to mitigate the curse of dimensionality in the classical variational optimization as p increases.
- Develop lower-overhead or more hardware-efficient implementations of the QWOA indexing and mixing circuits.
- Evaluate QWOA on more realistic portfolio optimization models, including richer constraints and market frictions.
- Benchmark against stronger classical baselines and heuristics for larger portfolio optimization instances.
- Explore alternative mixer graphs and initialization strategies to further improve convergence and reduce bias.
- Study noise robustness and apply error-mitigation techniques for QWOA in NISQ settings.
- Validate the authors' suggestion that QWOA advantages extend to other constrained combinatorial optimization problems beyond portfolio optimization.
- Assess production scalability, including end-to-end runtime, shot requirements, and hardware resource needs for practical financial use cases.
## Key ideas
- #idea:hybrid-approach — The paper compares hybrid variational quantum methods (QAOA, QAOAz, QWOA) for discrete Markowitz portfolio optimisation with long/short/flat positions and a net investment constraint.
- #idea:hybrid-approach — QWOA uses classical indexing/unindexing to restrict evolution to valid, non-degenerate portfolios, sharply reducing the effective search space versus QAOA and QAOAz.
- #idea:quantum-advantage — Within the compared quantum methods, QWOA achieves better simulated objective values, stronger concentration on optimal portfolios, and lower variance across runs than QAOA and QAOAz on 8-asset instances.
- #idea:near-term-feasibility — The paper positions QWOA as promising for NISQ settings because it can reach good solutions at relatively low depth p, despite higher per-layer mixer complexity.
- #idea:quantum-advantage — The claimed performance gains are algorithmic and relative only to other quantum heuristics, not to classical state-of-the-art portfolio solvers.
- #idea:near-term-feasibility — The study uses real stock datasets and derives return/risk statistics from output distributions, but all evidence comes from noiseless classical simulation rather than hardware execution.
## Contradictions
- The paper suggests quantum promise via superior simulated performance of QWOA over QAOA/QAOAz, but this is contradicted by its own evidence that all experiments were classical simulations with no comparison against strong classical portfolio optimisation baselines (#contradiction:classical-vs-quantum).
- The paper frames QWOA as suitable for near-term devices and potentially more scalable due to feasible-subspace restriction, but this is undermined by the tiny tested scale (8 assets), absence of noise/hardware validation, and acknowledged O(n^2) mixer complexity plus classical optimisation bottlenecks (#contradiction:scalability).
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
