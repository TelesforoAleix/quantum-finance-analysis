---
aliases:
- Backtesting Quantum Computing Algorithms for Portfolio Optimization
- Backtesting Quantum Computing Algorithms
authors:
- Ginés Carrascal
- Paula Hernamperez
- Guillermo Botella
- Alberto del Barrio
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1109/TQE.2023.3337328
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: IEEE Transactions on Quantum Engineering
methodology_tags:
- QAOA
- VQE
- QUBO
- variational
- grover
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:03:13.579779'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:03:18.598918'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:04:07.477977'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:04:37.935352'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:05:14.384837'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:05:29.718011'
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
- method/grover
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Backtesting Quantum Computing Algorithms for Portfolio Optimization
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
The paper proposes and implements a reusable methodology to backtest and compare classical and quantum algorithms for portfolio optimization under equivalent conditions. Using IBEX35 historical data, the authors benchmark four quantum (including VQE, CVaR-VQE, QAOA, and Grover Adaptive Search) and three classical approaches across 10,000 simulated experiments, and also validate selected quantum methods on IBM’s 27- and 127-qubit devices. They focus on scalability and execution-time behavior, showing that quantum algorithms can be competitive with classical ones and may better handle larger asset universes on future, more capable quantum hardware.
## Methodology
This peer-reviewed empirical study proposes and applies a reusable backtesting methodology to compare classical and quantum portfolio-optimization algorithms under equivalent conditions. The authors formulate portfolio selection as both classical mean-variance / Sharpe-ratio optimization and as a QUBO/Ising problem for quantum methods, restricting portfolios to equal-weight selections with a fixed budget of assets. They implement three classical algorithms (simple moving average strategy, mean-variance optimization, and Sharpe ratio optimization) and four quantum algorithms (VQE, CVaR-VQE, QAOA, and Grover Adaptive Search) in Python using Qiskit, with historical adjusted closing prices from IBEX35 constituents downloaded from Yahoo Finance via the bt library. The main empirical design consists of 10,000 backtesting experiments using random subsets of IBEX35 stocks, with monthly portfolio rebalancing over 2017-2020 and 2016 reserved as lookback history. To ensure practical comparability, quantum backtesting is primarily run on simulators, while real IBM quantum hardware is used for validation and illustrative execution-time / feasibility studies, including 5-qubit, 27-qubit, and 127-qubit devices. The study also analyzes hardware-aware ansatz design, qubit-path selection, transpilation, and circuit-depth constraints for real devices. Evaluation includes execution-time scalability, backtested total returns, summary statistics (means, standard deviations), counts of how often each algorithm achieves the best result, and comparisons against classical exact reference solutions such as NumPyMinimumEigensolver and classical optimization solvers.

**Algorithms used:** VQE, CVaR-VQE, QAOA, Grover Adaptive Search, Mean-Variance Optimization, Sharpe Ratio Optimization, Simple Moving Average Strategy, COBYLA, NumPyMinimumEigensolver
**Frameworks:** Qiskit, bt, cvxopt, ffn, Yahoo Finance

**Experimental setup:** Algorithms were implemented in Python with Qiskit. The main backtesting comparison used simulators for quantum algorithms due to queueing and communication overheads on real hardware. Real IBM quantum devices were used for validation and hardware feasibility studies, including ibmq_athens (5 qubits), ibm_cairo (27-qubit Falcon r5.11), ibm_washington (127-qubit Eagle r1), and later 127-qubit backends ibm_brisbane, ibm_cusco, and ibm_nazca for execution-time scaling. The study used hardware-aware ansatz construction with linear or circular entanglement, selected qubit paths to minimize error and SWAP insertion, and measured execution time excluding queue time in most hardware timing analyses.

**Dataset:** Historical adjusted closing prices for IBEX35 stocks, obtained from Yahoo Finance. Main backtesting dataset spans 2016-2020, with 2016 used as historical lookback and 2017-2020 used for simulated investing and monthly rebalancing. Additional illustrative experiments used random subsets of IBEX35 stocks, including a 19-stock sample from 2022-10-01 to 2022-12-01 for 27-qubit hardware tests and random 3-asset examples from October 2020.
## Experiment details
### Input
Primary input: IBEX35 adjusted closing prices from Yahoo Finance via bt. Main backtesting used data from 2016-2020; 2016 served as historical window and 2017-2020 as the investment period. In the 10,000-run benchmark, each run sampled random subsets of IBEX35 stocks; the text reports five random assets per experiment in the backtesting section, while tables mention six random assets, indicating some inconsistency. Portfolios were constrained to equal weights and a fixed budget, described as avoiding/selecting two out of five available stocks in the main comparison. Additional inputs included a 19-stock random subset for ibm_cairo and a 28-asset setup for ibm_washington. Preprocessing involved computing expected returns and covariance matrices from historical prices and transforming the constrained quadratic portfolio problem into QUBO and then Ising form for quantum algorithms.

### Process
1. Download adjusted closing prices for IBEX35 constituents from Yahoo Finance using bt. 2. Compute portfolio statistics such as expected returns and covariance matrix from historical data. 3. For classical methods: run SMA with a 50-day moving-average window, MVO using cvxopt to compute efficient-frontier portfolios, and SRO using ffn's calc_mean_var_weights. 4. For quantum methods: formulate the portfolio problem as a constrained binary optimization problem with risk-aversion parameter q and budget B; convert the budget constraint into a penalty term, transform the QUBO into Ising form, and express it as a Pauli-Z Hamiltonian. 5. Run VQE, CVaR-VQE, QAOA, and GAS using Qiskit. COBYLA is used as the classical optimizer for variational methods. 6. For real-hardware studies, design low-depth ansatz circuits matched to hardware topology (linear entanglement for 19 assets on ibm_cairo; circular entanglement for 28 assets on ibm_washington), choose low-error qubit paths, transpile to native gates, and execute with large shot counts. 7. For the main empirical comparison, perform 10,000 backtesting runs on random IBEX35 subsets, rebalance monthly, and record each algorithm's backtested performance under matched conditions. 8. Aggregate results using means, standard deviations, boxplots, and counts of how often each algorithm achieved the best result; additionally filter runs by intrarecord variance to focus on cases where algorithms differ meaningfully.

### Output
Outputs include backtested portfolio performance comparisons across algorithms, especially total returns over the backtest horizon, plus summary statistics such as mean and standard deviation across 10,000 runs. The study also reports the number of times each algorithm achieved the best result, both before and after filtering by intrarecord variance. Additional outputs include execution-time scaling versus number of assets, convergence plots for CVaR-VQE, probability histograms from quantum measurements, transpiled circuit depths, per-shot and total hardware execution times, and comparisons against classical baselines including SMA, MVO, SRO, and exact classical reference solutions from NumPyMinimumEigensolver.

### Parameters
- backtesting_runs: 10000
- rebalancing_frequency: monthly
- historical_lookback_start: 2016
- investment_period: 2017-2020
- sma_window_days: 50
- optimizer: COBYLA
- vqe_iterations_real_3_asset_example: 20
- vqe_iterations_simulator_example: 100
- shots_ibm_cairo_example: 100000
- shots_ibm_washington_example: 100000
- qubits_ibmq_athens_example: 5
- qubits_ibm_cairo: 27
- qubits_ibm_washington: 127
- selected_qubit_path_ibm_cairo: 19
- selected_qubit_path_ibm_washington: 28
- transpiled_depth_ibm_cairo_19_asset_vqe: 27
- transpiled_depth_ibm_washington_28_asset_vqe: 37
- budget_constraint: fixed number of selected assets; described as selecting/avoiding two out of five in main backtesting
- portfolio_weighting: equal weight
- risk_aversion_factor: same across all seven tested algorithms

### Hardware
Real hardware included ibmq_athens (5-qubit backend used for a 3-asset illustrative VQE run), ibm_cairo (27-qubit Falcon r5.11, QV 64, 2.4K CLOPS, native gates CX/ID/IF_ELSE/RZ/SX/X, median CNOT error 1.049e-2, median readout error 1.180e-2, median T1 106.81 us, median T2 102.88 us), and ibm_washington (127-qubit Eagle r1, QV 64, 850 CLOPS, native gates CX/ID/IF_ELSE/RZ/SX/X, median CNOT error 1.378e-2, median readout error 1.080e-2, median T1 99.55 us, median T2 93.66 us). Execution-time scaling also used ibm_brisbane, ibm_cusco, and ibm_nazca. Simulators included ibmq_qasm_simulator and Qiskit simulators generally. The authors used hardware-aware qubit mapping, selected low-error linear/circular qubit paths, and transpiled ansatz circuits to native gates while avoiding SWAPs where possible. For ibm_cairo, the 19-asset VQE ansatz transpiled to depth 27 and took about 1125 us per shot; 100000 shots took 35.3 s excluding queue time. For ibm_washington, the 28-asset ansatz transpiled to depth 37 and 100000 shots took 48.6 s.

### Reproducibility
Data source is public and clearly identified (Yahoo Finance / IBEX35), and the paper provides substantial methodological detail on formulations, algorithms, hardware choices, and some parameter settings. However, full reproducibility is only partial because no code repository is explicitly provided in the text, some backtesting details are ambiguous (e.g., five vs. six random assets), and not all hyperparameters for QAOA/GAS/VQE ansatz settings are fully specified.
## Findings
- [supported] In 10,000 backtesting experiments on equivalent conditions using IBEX35 historical data, quantum algorithms could match or slightly outperform classical portfolio optimization algorithms on average, though differences were small relative to high variance across runs.
- [supported] After filtering experiments to retain higher intra-record variance cases, quantum algorithms—especially QAOA and CVaR-VQE—more often produced the best-performing strategy than the classical baselines.
- [supported] In the unfiltered 10,000-run comparison with five random assets, each algorithm was the best performer roughly 20%–30% of the time, making it difficult to conclude that any single method consistently dominates.
- [supported] The simple moving average strategy (SMA) underperformed the optimization-based methods and served as a weak baseline in the backtesting study.
- [supported] On a 19-asset instance executed on IBM's 27-qubit ibm_cairo hardware, CVaR-VQE converged in about 10 iterations and selected a portfolio differing by only one stock from the classical NumPyMinimumEigensolver reference solution.
- [supported] For the 19-asset ibm_cairo experiment, the transpiled VQE circuit had depth 27 circuit layers, estimated chip time 1125 microseconds per shot, and 100,000 shots required about 35.3 seconds of quantum-system execution time excluding queue time.
- [supported] On IBM's 127-qubit ibm_washington hardware, a 28-asset VQE circuit transpiled to depth 37 circuit layers with estimated chip time 4352 microseconds and about 48.6 seconds for 100,000 shots excluding queue time.
- [supported] In a 3-asset real-hardware VQE example on ibmq_athens, limiting optimization to 20 iterations did not reach the exact optimum, whereas running the same problem on a simulator with 100 iterations reached the desired optimum.
- [supported] Real-hardware queue delays dominated wall-clock runtime; in one 3-asset example the average elapsed time per VQE iteration was about two hours including queue/communication, while the algorithmic iteration execution itself was about nine seconds.
- [supported] The authors' execution-time experiments indicate that quantum VQE step time on IBM hardware increased much more slowly with asset count than classical MVO/SRO step times, which showed exponential growth trends in their tests.
- [supported] The study used simulators for the large-scale backtesting comparisons and real IBM hardware mainly for validation and illustrative experiments because queueing and communication overheads make iterative VQE impractical for large backtesting campaigns on current devices.
- [speculative] The paper argues that quantum algorithms have a scalability advantage for very large portfolio optimization problems because classical methods become infeasible while future larger quantum computers may handle many assets in reasonable time.
- [speculative] The claim that quantum algorithms can handle a large number of assets in reasonable time depends on future larger and more reliable quantum hardware rather than being demonstrated end-to-end in this study.

**Results summary:** This peer-reviewed empirical study proposes a reusable backtesting methodology to compare classical and quantum portfolio optimization algorithms under equivalent conditions and applies it to 10,000 experiments using IBEX35 historical data. The main empirical result is that quantum methods were broadly competitive with classical methods in backtesting, with quantum approaches sometimes slightly outperforming classical ones, especially after filtering for cases with larger performance dispersion across algorithms. The strongest quantum performers in the study were QAOA and CVaR-VQE, while SMA was clearly weaker. The paper also reports real-hardware demonstrations on IBM devices: a 19-asset CVaR-VQE run on a 27-qubit machine converged quickly and produced a portfolio close to the classical reference, and a 28-asset VQE circuit was executed on a 127-qubit machine. However, the large-scale comparative backtesting results were obtained on simulators, not real hardware, and the paper does not provide confidence intervals. Claims of superior scalability and ability to handle very large portfolios are therefore based on observed execution-time trends plus extrapolation to future hardware, rather than a demonstrated quantum advantage in practical portfolio optimization today.

**Performance claims:**
- 10,000 backtesting experiments were run to compare 4 quantum and 3 classical algorithms under equivalent conditions
- In the 3-asset real-hardware example on ibmq_athens, 20 VQE iterations did not reach the optimal solution
- In the same 3-asset example, simulator execution with 100 VQE iterations reached the desired optimum
- Average elapsed time per VQE iteration in one real-hardware example was about 2 hours including queue and communication time
- Algorithm iteration execution time in that example was roughly 9 seconds excluding queue effects
- Quantum execution-time scaling was tested on datasets with 2 to 100 random assets across IBM real backends ibm_brisbane, ibm_cusco, and ibm_nazca
- For classical algorithms, mean step execution times were measured over 10 executions with random generated assets
- SRO began having feasibility problems above about 90 assets
- On ibm_cairo (27 qubits), the selected usable path supported 19 qubits/assets
- For the 19-asset ibm_cairo VQE circuit, transpiled depth was 27 circuit layer operations
- For the 19-asset ibm_cairo run, estimated chip time was 1125 microseconds per shot
- For the 19-asset ibm_cairo run, 100,000 shots took an average of 35.3 seconds in the quantum system excluding queue time
- CVaR-VQE on ibm_cairo converged after about 10 iterations
- The classical NumPyMinimumEigensolver reference for the 19-asset case took 126.57 seconds
- The 19-asset quantum portfolio differed from the classical reference by 1 selected stock
- On ibm_washington (127 qubits), the selected usable path supported 28 qubits/assets
- For the 28-asset ibm_washington VQE circuit, transpiled depth was 37 circuit layer operations
- For the 28-asset ibm_washington run, estimated chip time was 4352 microseconds
- For the 28-asset ibm_washington run, 100,000 shots took 48.6 seconds in the quantum system excluding queue time
- In the 10,000 unfiltered simulations with five random assets, each algorithm achieved the best result about 20% to 30% of the time
## Quantum advantage claim
**Classification:** speculative

The paper presents empirical competitiveness and favorable execution-time scaling trends, but the main comparative backtesting results are from simulators, not real hardware, and no clear end-to-end quantum advantage over classical methods is demonstrated. Claims about handling very large asset universes rely on extrapolation to future larger quantum computers.
## Limitations
- Backtesting relies on historical data and assumptions, so results may not accurately predict future market conditions; past performance does not guarantee future results.
- Portfolio optimization models used are based on a static view of the market and do not account for changes over time or unexpected events.
- The study focuses only on equal-weight portfolios and only decides which assets to include or exclude, limiting realism relative to practical portfolio construction.
- The formulation assumes all assets have the same cost and uses a fixed budget constraint, which simplifies real investment settings.
- The QUBO transformation relaxes the budget constraint via a penalty term, so the solution may choose a number of assets different from the target budget.
- Quantum hardware is limited by noise, decoherence, and scalability, which the paper explicitly notes as challenges.
- Current qubit stability is short, so circuit execution must remain within coherence time; this constrains circuit depth and algorithm design.
- Real-hardware experiments required low-depth ansatz design and careful qubit-path selection to avoid larger transpiled circuits, indicating strong hardware dependence.
- QAOA circuits are inherently deeper than VQE circuits and are therefore more prone to noise disturbances on real hardware.
- Grover Adaptive Search requires circuits that are too long to be reliable on current non-error-corrected quantum computers.
- Real quantum computers use a queuing system, and iterative algorithms such as VQE are significantly slowed by repeated job submissions.
- Because of queueing and communication overhead, the authors executed quantum backtesting on simulators rather than real hardware, limiting empirical validation on actual devices.
- Queue times were excluded from the reported execution-time results, so measured timings do not reflect full end-to-end production runtime on cloud quantum hardware.
- In the 3-asset real-hardware example, limiting VQE to 20 iterations led to a non-optimal result, showing sensitivity to optimization budget.
- The number of iterations needed for convergence as asset count grows is unknown for both classical and quantum methods.
- The authors state that all tested algorithms are heuristic and include random components, making definitive comparisons difficult.
- Even after 10,000 simulations, the paper concludes it is challenging to determine with complete certainty which algorithm outperforms the others.
- Backtesting is subject to survivorship bias and look-ahead bias, which can affect result accuracy.
- The empirical dataset is limited to IBEX35 historical data from Spain, reducing geographic and market generalizability.
- The main backtesting setup uses small random subsets of assets (e.g., five or six assets), which may not reflect realistic large-scale institutional portfolios.
- Real-hardware demonstrations were limited to selected IBM devices and specific qubit paths, which may reduce reproducibility across hardware generations or vendors.
- [inferred] The paper does not provide a comparison against strong state-of-the-art classical portfolio optimizers or commercial solvers beyond a small set of baseline methods.
- [inferred] Claims about handling a large number of assets in reasonable time on future quantum computers are not empirically validated on fault-tolerant or production-scale hardware.
- [inferred] The study uses Yahoo Finance adjusted closing prices only, which omits richer market features such as intraday data, liquidity, slippage, and execution constraints.
- [inferred] Reproducibility may be limited because real-hardware performance depends on time-varying calibration, queue conditions, and backend availability.
- [inferred] The filtering of backtesting runs based on intrarecord variance may influence comparative conclusions and introduces a methodological choice that could affect internal validity.
- [inferred] No formal statistical significance testing of performance differences between algorithms is reported, despite the large number of experiments.
- [inferred] The use of simulators for most quantum backtesting means reported quantum competitiveness may not fully capture noise effects encountered in real deployment.
## Open questions
- How do quantum portfolio optimization algorithms perform under more realistic market models that include transaction costs and integer trading constraints?
- How robust are the reported advantages of QAOA and CVaR-VQE across larger and more diverse financial datasets?
- How many iterations are required for convergence of classical and quantum algorithms as the number of assets increases?
- To what extent do noise and hardware errors affect solution quality for VQE and related algorithms on larger real quantum devices?
- Can current or near-term real quantum hardware deliver consistent advantages once queue time and full workflow latency are included?
- How sensitive are results to ansatz choice, qubit mapping, transpilation strategy, and backend calibration?
- Will the better scalability trend observed in step execution time translate into end-to-end advantage in practical portfolio optimization tasks?
- How should penalty terms in the QUBO formulation be selected to enforce constraints without degrading optimization performance?
- Can quantum methods maintain competitiveness when portfolios include many more assets and more realistic constraints than the small subsets used in backtesting?
- How generalizable are the findings beyond the IBEX35 and the specific historical period studied?
- [inferred] Would the conclusions hold when compared against stronger classical heuristics, mixed-integer solvers, or modern stochastic optimization methods?
- [inferred] How much of the observed performance difference is due to the problem formulation and filtering methodology rather than the underlying quantum algorithm?

**Future work:**
- Develop more realistic models that better capture the complexity and uncertainty of real stock market conditions.
- Address portfolio selection with transaction costs included in the optimization model.
- Incorporate integer constraints on the quantities of securities into the optimization problem.
- Implement error mitigation techniques to reduce noise and errors affecting the quantum algorithms.
- Test the proposed models on larger datasets.
- Test the proposed models on more diverse datasets to validate scalability and robustness.
- Apply the methodology directly on real quantum computers when dedicated resources and communications are available.
- Further investigate convergence behavior of classical and quantum algorithms as problem size grows.
- [inferred] Evaluate the methods on broader markets and asset universes beyond IBEX35.
- [inferred] Benchmark against stronger classical baselines and production-grade optimization solvers.
- [inferred] Study end-to-end runtime including queueing, communication, and repeated hybrid optimization loops for realistic deployment assessment.
- [inferred] Explore portfolio formulations beyond equal-weight selection, including continuous weights and multi-period rebalancing.
## Key ideas
- #idea:quantum-advantage — Under matched backtesting conditions on IBEX35 data, quantum portfolio methods (especially QAOA and CVaR-VQE) were broadly competitive with classical baselines and sometimes more frequently best in filtered high-variance cases.
- #idea:hybrid-approach — The study frames portfolio selection as a QUBO/Ising problem and solves it with hybrid variational methods using classical optimizers plus hardware-aware circuit design.
- #idea:near-term-feasibility — Real IBM devices with 27 and 127 qubits were able to execute shallow VQE/CVaR-VQE instances for 19–28 asset formulations, producing solutions close to classical references.
- #idea:quantum-advantage — The paper argues that quantum step-time scaling may become favorable for larger asset universes, but this is presented as a future-facing claim rather than demonstrated end-to-end advantage.
- #idea:near-term-feasibility — The paper proposes a reusable empirical backtesting methodology for fair classical-versus-quantum comparison, which is itself a contribution for NISQ-era evaluation.
## Contradictions
- The paper suggests superior scalability and future competitiveness of quantum portfolio optimization, yet most substantive benchmarking is simulator-based and real-hardware studies are limited to small validation cases; this weakens any strong claim of present practical advantage.
- The study reports favorable quantum execution-time trends while also noting that queue delays, noise, shallow-circuit constraints, and limited iterations make current hardware impractical for full backtesting workflows.
- Quantum methods are described as competitive or slightly better on average, but the paper also states that in the unfiltered 10,000-run benchmark each algorithm wins only about 20%–30% of the time and no method clearly dominates.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
