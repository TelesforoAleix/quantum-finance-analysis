---
aliases:
- SCALING PORTFOLIO DIVERSIFICATION WITH QUANTUM CIRCUIT CUTTING TECHNIQUES
- SCALING PORTFOLIO DIVERSIFICATION QUANTUM
authors:
- Vicente P. Soloviev
- Antonio Márquez Romero
- Josh Kirsopp
- Michal Krompiec
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
journal_or_venue: arXiv
methodology_tags:
- QAOA
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T16:11:37.442694'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:11:41.721045'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:12:18.651054'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:12:41.306858'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:13:09.522731'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:13:18.820771'
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
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: SCALING PORTFOLIO DIVERSIFICATION WITH QUANTUM CIRCUIT CUTTING TECHNIQUES
topic_tags:
- portfolio-optimisation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper introduces QuantCut, an automatic framework for gate-based circuit cutting that enables execution of large QAOA circuits on hardware with limited qubit counts. The authors apply QuantCut to a 71-qubit QAOA ansatz for portfolio diversification on S&P 500 assets, formulating the task as a Max-Cut problem on a correlation graph and reconstructing expectation values from cut subcircuits. They validate the approach on a noisy toy Max-Cut instance and on real financial data, showing that circuit cutting can support large-scale quantum optimization and may offer some noise-mitigation benefits.
## Methodology
This preprint presents an empirical proof-of-concept study centered on QuantCut, an automatic gate-cutting framework for scaling variational quantum optimization. The authors formulate portfolio diversification as a graph-based Max-Cut problem over a stock-market correlation/covariance network derived from 71 selected S&P 500 assets, with one qubit per asset. They build a QAOA ansatz in which the market graph is encoded into the cost Hamiltonian and use CRZ-based edge interactions to reduce circuit-cutting complexity. QuantCut first identifies gate cuts automatically by solving a cut-placement optimization problem that minimizes the number of cuts subject to a maximum subcircuit qubit constraint, using an estimation-of-distribution evolutionary algorithm implemented with EDAspy. For each QAOA parameter setting, the framework decomposes cut two-qubit gates via quasiprobability-based gate cutting into six local subexperiments per cut, executes the resulting subcircuits on a user-specified backend or simulator, and reconstructs the expectation value through post-processing; the cut pattern is found once and reused across subsequent optimization iterations. The study includes two empirical evaluations: (1) a toy 10-node Max-Cut experiment under a simulated readout-noise model comparing QAOA convergence with and without circuit cutting for p = 1, 2, 3 layers, and (2) a real-data 71-qubit portfolio-diversification experiment using S&P 500 data, where QuantCut is applied at every optimization step to estimate the QAOA objective. After optimization, the final solution is extracted by tensor-network simulation and sampling using cuQuantum integrated with pytket, run on a single NVIDIA A100 GPU. Results are reported in terms of expectation-value convergence and portfolio graph metrics, with comparisons against random sampling and a classical evolutionary algorithm baseline. As this is an arXiv preprint, the work should be treated as non-peer-reviewed.

**Algorithms used:** QAOA, Max-Cut, gate cutting, quasiprobability decomposition, estimation of distribution algorithm, tensor-network simulation, matrix product state
**Frameworks:** QuantCut, EDAspy, pytket, cuQuantum

**Experimental setup:** Two experimental settings are reported. First, a toy QAOA Max-Cut experiment on a randomly generated 10-node Erdős-Rényi graph is run in a noisy simulated environment with a readout error model P(0|0)=0.99, P(0|1)=0.01, P(1|0)=0.01, P(1|1)=0.99, comparing runs with and without circuit cutting for 1, 2, and 3 QAOA layers; one gate cut is applied per layer. Second, a real-world 71-qubit portfolio-diversification experiment is performed where each of 71 selected S&P 500 assets is mapped to one qubit, QAOA with p=1 is optimized, and QuantCut performs three gate cuts per layer to reduce circuit width during expectation estimation. Final solution extraction is done by tensor-network sampling using matrix product state methods on a single NVIDIA A100 GPU.

**Dataset:** Real financial data from the S&P 500 stock market obtained from a Kaggle dataset containing stock values from the last five years; 71 assets were selected from the 500 available for the main portfolio-diversification experiment. A synthetic Erdős-Rényi random graph with 10 nodes was used for the toy Max-Cut noise-resilience experiment.
## Experiment details
### Input
Main financial experiment: S&P 500 stock-price time series from a Kaggle dataset (https://www.kaggle.com/datasets/camnugent/sandp500), covering the last five years; 71 assets selected from 500 total. Preprocessing included normalization of each time series to [0,1], standardization to zero mean and unit variance, computation of Pearson correlations and covariance matrix, and thresholding the covariance/correlation structure at alpha = 0.2 to build a 71-node market graph. Each node corresponds to one asset/qubit. Toy experiment: a random Erdős-Rényi graph with n = 10 nodes generated for Max-Cut under simulated readout noise.

### Process
Pipeline: (1) preprocess stock time series by normalization and standardization; (2) compute correlation/covariance structure and encode the market as a graph with 71 nodes and threshold alpha = 0.2; (3) formulate diversification as a Max-Cut problem and construct a QAOA ansatz with one qubit per node, using CRZ-based edge interactions in the cost layer; (4) run QuantCut to identify optimal gate cuts automatically in the first optimization iteration by minimizing the number of cuts subject to subcircuit qubit constraints via an estimation-of-distribution algorithm; (5) for each QAOA parameter configuration, decompose each cut two-qubit gate using the Mitarai-Fujii quasiprobability method into six local subexperiments, execute subcircuits, and reconstruct the full-circuit expectation value through post-processing; (6) iteratively update QAOA parameters with a classical optimizer until the expectation value decreases over iterations; (7) after optimization, extract the highest-amplitude bitstring solution by tensor-network simulation and sampling using matrix product states. Toy experiment process: generate a 10-node Erdős-Rényi graph, run QAOA for p = 1, 2, 3 under a readout-noise model, compare convergence with and without circuit cutting, with one gate cut per layer. Main experiment process: run 71-qubit QAOA with p = 1 and three gate cuts per layer, then compare final graph-partition metrics against random sampling and a classical evolutionary algorithm.

### Output
Outputs include convergence plots of the QAOA expectation value versus optimization iteration/runtime for both toy and 71-qubit experiments; comparative convergence behavior with and without circuit cutting under noise; and final portfolio-diversification quality metrics. For the 71-qubit experiment, reported metrics are Max-Cut(G) and within-subportfolio accumulated edge weights Acum(G0) and Acum(G1). Baselines include random sampling and a classical evolutionary algorithm (EA). Reported values: random sampling Max-Cut 26.1 ± 2.1, Acum(G0) 15.2 ± 5.0, Acum(G1) 7.9 ± 7.1; QAOA (p=1) Max-Cut 43.41, Acum(G0) 2.439, Acum(G1) 4.113; EA Max-Cut 46.51, Acum(G0) 1.190, Acum(G1) 2.110.

### Parameters
- main_qubits: 71
- toy_qubits: 10
- qaoa_layers_toy: [1, 2, 3]
- qaoa_layers_main: 1
- gate_cuts_per_layer_toy: 1
- gate_cuts_per_layer_main: 3
- graph_threshold_alpha: 0.2
- readout_error_matrix: {'P(0|0)': 0.99, 'P(0|1)': 0.01, 'P(1|0)': 0.01, 'P(1|1)': 0.99}
- subexperiments_per_cut: 6
- gpu: NVIDIA A100

### Hardware
The paper states that QuantCut can target either a real quantum device or a simulator, but the reported experiments appear to rely on simulation. Noise-resilience tests use a simulated readout-noise model. Final large-circuit solution extraction uses NVIDIA cuQuantum tensor-network functionality integrated with pytket, executed on a single NVIDIA A100 GPU. No specific QPU model, cloud provider, shot count, or transpilation settings are reported.

### Reproducibility
No public code repository or executable package link for the paper itself is provided in the text, although external libraries used (EDAspy, pytket, cuQuantum) are named. The financial data source is public via Kaggle, and preprocessing plus core methodological steps are described at a moderate level. However, important replication details such as exact optimizer settings for QAOA, backend configuration, shot counts, stopping criteria, and full cut-finder hyperparameters are missing, so replication is only partially supported.
## Findings
- [supported] The paper introduces QuantCut, an automatic gate-cutting framework that selects cut locations to minimize the number of cuts under a qubit-budget constraint and reconstructs expectation values or state vectors from subcircuit executions.
- [speculative] The authors claim this is the first disclosed implementation of an automatic algorithm that finds suitable gate cuts based on qubit connectivity.
- [supported] In a noisy 10-qubit Max-Cut simulation with readout error probabilities P(0|0)=0.99, P(1|1)=0.99, circuit cutting showed improved convergence accuracy relative to uncut execution for deeper QAOA ansätze (2 and 3 layers).
- [supported] In the same toy experiment, circuit cutting performed worse than the uncut circuit for the 1-layer QAOA setting.
- [speculative] The authors suggest circuit cutting may act as an error-mitigation strategy, based on the observed noisy-simulation behavior and prior literature.
- [supported] The framework was applied to a 71-qubit QAOA portfolio-diversification problem built from 71 selected S&P 500 assets, using a graph threshold of alpha=0.2 on the covariance matrix.
- [supported] For the 71-qubit experiment, QuantCut used three gate cuts per QAOA layer and the optimization trace showed a decreasing expectation value over iterations, indicating the classical optimizer reduced the objective.
- [supported] On the 71-asset portfolio problem, QAOA with p=1 achieved Max-Cut(G)=43.41, outperforming random sampling (26.1 ± 2.1) but underperforming a classical evolutionary algorithm (46.51).
- [supported] On the same task, QAOA with p=1 produced lower within-subportfolio edge accumulation than random sampling, with Acum(G0)=2.439 and Acum(G1)=4.113 versus random sampling 15.2 ± 5.0 and 7.9 ± 7.1.
- [supported] The best classical baseline reported was the evolutionary algorithm, with Acum(G0)=1.190 and Acum(G1)=2.110, better than the QAOA result.
- [supported] Solution extraction for the >70-qubit circuits was performed via tensor-network simulation and sampling using cuQuantum on a single NVIDIA A100 GPU rather than direct full state-vector simulation.
- [speculative] The authors argue that increasing QAOA depth p could allow the quantum approach to converge toward solutions similar to the evolutionary algorithm baseline.
- [speculative] The paper suggests QuantCut could facilitate large-scale quantum computations and be useful for distributed quantum computing, but this is not empirically demonstrated on real hardware.

**Results summary:** This preprint presents QuantCut, an automated gate-cutting framework for decomposing large quantum circuits into smaller subcircuits and reconstructing results through post-processing. The method is evaluated first on a 10-qubit noisy Max-Cut simulation, where circuit cutting improves convergence relative to uncut execution for 2- and 3-layer QAOA but not for 1 layer, leading the authors to suggest possible error-mitigation benefits. The main application is a 71-qubit QAOA formulation of portfolio diversification over selected S&P 500 assets, represented as a thresholded correlation/covariance graph and mapped to Max-Cut. In this setting, the optimization converges downward in expectation value, and the resulting QAOA solution outperforms random sampling but remains worse than a classical evolutionary algorithm. All reported large-scale results rely on simulation and tensor-network methods rather than execution on real quantum hardware, so any broader scalability or quantum-advantage implications remain speculative.

**Performance claims:**
- 10-qubit toy Max-Cut simulation used readout noise with P(0|0)=0.99, P(0|1)=0.01, P(1|0)=0.01, P(1|1)=0.99
- Toy noisy QAOA compared p=1, p=2, and p=3 layers, with one gate cut per layer
- 71-qubit portfolio-diversification QAOA used 71 assets and threshold alpha=0.2 for graph construction
- 71-qubit experiment used p=1 QAOA layer and 3 gate cuts per layer
- Random sampling baseline: Max-Cut(G)=26.1 ± 2.1, Acum(G0)=15.2 ± 5.0, Acum(G1)=7.9 ± 7.1
- QAOA (p=1): Max-Cut(G)=43.41, Acum(G0)=2.439, Acum(G1)=4.113
- Evolutionary algorithm baseline: Max-Cut(G)=46.51, Acum(G0)=1.190, Acum(G1)=2.110
- Solution extraction and sampling were run on a single NVIDIA A100 GPU
## Quantum advantage claim
**Classification:** speculative

This is a preprint with results based on noisy simulation and tensor-network simulation, not real quantum hardware. The quantum method beats random sampling on the 71-asset task but does not beat the reported classical evolutionary algorithm, so no demonstrated quantum advantage is shown.
## Limitations
- Lack of peer review: the work is a preprint and its claims have not yet undergone peer-reviewed validation
- Large-scale quantum circuits remain constrained by current hardware limitations; the proposed approach addresses this via circuit cutting rather than direct execution
- Gate cutting incurs overhead that scales exponentially with the number of cuts, making cut minimization critical and potentially limiting scalability
- The framework focuses only on gate cutting and specifically on entangling gates involving two qubits
- Reconstructing the full state vector is limited to a small number of qubits due to exponential memory cost
- The 71-qubit financial study is a proof-of-concept based on simulation rather than execution on real quantum hardware
- Noise analysis is limited to a toy 10-qubit Max-Cut example rather than the full 71-qubit portfolio problem
- The noise model used is narrow, considering only readout noise, so conclusions about robustness under realistic hardware noise are limited
- The 71-qubit optimization uses only a shallow QAOA ansatz with p = 1 layer, which likely limits solution quality
- The QAOA approach underperforms the classical evolutionary algorithm baseline in the reported portfolio experiment
- The graph threshold for correlations (alpha = 0.2) was empirically adjusted, which may make results sensitive to a heuristic design choice
- Only 71 assets out of the S&P 500 were selected, limiting generalizability to the full market universe
- The mapping uses one asset per qubit, which is qubit-inefficient and restricts scalability
- Solution extraction relies on tensor-network simulation and sampling on a single NVIDIA A100 GPU, introducing substantial classical computational support
- [inferred] No experiments are reported on actual QPUs, so hardware-specific issues such as calibration drift, crosstalk, and non-readout noise remain unvalidated
- [inferred] No comparison is provided against stronger classical portfolio optimization baselines beyond random sampling and one evolutionary algorithm
- [inferred] Reproducibility may be limited because the paper does not provide full implementation details such as optimizer settings, random seeds, runtime budgets, or code availability in the excerpt
- [inferred] The financial formulation optimizes diversification via a Max-Cut proxy and does not appear to incorporate practical portfolio constraints such as transaction costs, liquidity, cardinality, or return targets
- [inferred] The use of thresholded correlations/covariances may discard relevant market structure and affect stability of the resulting portfolios
- [inferred] The claim of competitive results is limited because the quantum workflow still depends heavily on classical preprocessing, classical optimization, and classical tensor-network postprocessing
## Open questions
- How does QuantCut perform as the number of cuts increases on larger and denser financial graphs?
- Will increasing the number of QAOA layers allow the quantum approach to match or surpass the classical evolutionary algorithm on the portfolio task?
- How robust is the method under more realistic noise sources beyond readout error, such as gate noise, decoherence, and crosstalk?
- Can the approach be executed effectively on real quantum hardware rather than simulators and tensor-network backends?
- How sensitive are the results to the empirically chosen correlation threshold alpha = 0.2?
- How well does the framework generalize from the selected 71 assets to larger universes such as the full S&P 500?
- What is the trade-off between qubit savings from circuit cutting and the exponential sampling/post-processing overhead in practical settings?
- Can alternative problem encodings that place more than one asset per qubit improve scalability without degrading solution quality?
- How effective is circuit cutting as an error-mitigation strategy across different ansatz depths and problem classes?
- What are the runtime and cost implications of distributed execution of the generated subcircuits across multiple QPUs or CPUs?
- How stable are the extracted portfolio solutions over different time windows, market regimes, and asset selections?
- [inferred] Does the Max-Cut-based diversification objective produce portfolios that are financially useful when evaluated with standard investment metrics out of sample?

**Future work:**
- Apply alternative problem mappings that assign more than one asset per qubit
- Increase the number of layers in the QAOA ansatz
- Analyze the performance of the approach and the resilience of circuit cutting under different types of quantum noise
- Explore broader applications of QuantCut beyond QAOA and finance
- Investigate the use of the automatic circuit-cutting pipeline for distributed quantum computing
- [inferred] Validate the framework on real quantum hardware with hardware-aware noise mitigation
- [inferred] Benchmark against stronger classical optimization methods and industry-standard portfolio construction approaches
- [inferred] Extend the financial model to include realistic constraints and objectives such as returns, risk budgets, transaction costs, and multi-period rebalancing
- [inferred] Study scalability to larger asset universes and denser market graphs
- [inferred] Perform ablation and sensitivity studies on cut placement, threshold selection, optimizer choice, and tensor-network approximation settings
## Key ideas
- #idea:hybrid-approach — QuantCut automatically decomposes large QAOA circuits into smaller subcircuits via gate cutting and reconstructs expectation values with quasiprobability post-processing.
- #idea:near-term-feasibility — The paper frames circuit cutting as a practical NISQ-era route to handle a 71-qubit portfolio-diversification QAOA instance under limited qubit budgets.
- #idea:hybrid-approach — The workflow is strongly hybrid, combining classical financial preprocessing, classical cut-placement optimization, variational QAOA optimization, and tensor-network/MPS-based classical solution extraction.
- #idea:quantum-advantage — The paper suggests potential quantum benefit because QAOA+QuantCut beats random sampling on the 71-asset diversification task, though not stronger classical baselines.
- #idea:near-term-feasibility — In a noisy 10-qubit toy Max-Cut simulation, circuit cutting improved convergence for deeper QAOA settings (p=2,3), suggesting possible error-mitigation-like benefits.
- #idea:hybrid-approach — QuantCut is positioned as a reusable circuit-partitioning layer for larger optimization workflows and potentially distributed quantum execution.
## Contradictions
- contradiction:classical-vs-quantum — Although the paper implies promise for quantum optimization in portfolio diversification, its main 71-asset result underperforms the reported classical evolutionary algorithm baseline (QAOA+QuantCut Max-Cut 43.41 vs EA 46.51), so no empirical quantum superiority is demonstrated.
- contradiction:scalability — The paper presents QuantCut as enabling larger-scale quantum optimization, but the demonstrated workflow relies on simulation, shallow p=1 QAOA, tensor-network postprocessing on a GPU, and incurs exponential overhead in the number of cuts, which weakens claims of practical scaling to real financial instances.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
