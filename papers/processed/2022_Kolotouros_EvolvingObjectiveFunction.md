---
aliases:
- Evolving objective function for improved variational quantum optimization
- Evolving objective function improved
authors:
- Ioannis Kolotouros
- Petros Wallden
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PhysRevResearch.4.023225
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
methodology_tags:
- VQE
- QAOA
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:57:56.984639'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:02.630725'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:58:31.227812'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:59:15.089071'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:59:46.454129'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:59:56.685188'
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
- method/VQE
- method/QAOA
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Evolving objective function for improved variational quantum optimization
topic_tags:
- portfolio-optimisation
- risk-modelling
year: 2022
zotero_key: ''
---

## Abstract summary
The paper proposes an evolving objective function, termed ascending-CVaR, for variational quantum algorithms applied to combinatorial optimization problems. Instead of optimizing a fixed conditional value at risk (CVaR) tail of the energy distribution, the method gradually increases the fraction of low-energy outcomes used in the cost function during training, interpolating from small-tail CVaR to the full energy expectation. Using simulations of VQE with a hardware-efficient ansatz and QAOA on MaxCut, number partitioning, and portfolio optimization instances, the authors show that ascending-CVaR improves convergence speed and significantly increases the overlap with optimal solutions compared to both standard expectation-value and fixed-α CVaR objectives, especially on harder instances where other methods often fail to find the optimum.
## Methodology
The paper proposes and empirically evaluates an evolving variational objective function called ascending-CVaR for variational quantum optimization. The method starts optimization with a low-tail conditional value at risk (CVaR) objective and gradually increases the tail parameter alpha during training until reaching the full expectation value, with the goal of avoiding suboptimal local minima while preserving the true global minimum. The authors test the approach through classical numerical emulation on three combinatorial optimization problems—MaxCut, number partitioning, and portfolio optimization—each mapped to Ising/QUBO Hamiltonians. They compare ascending-CVaR against fixed-CVaR objectives with alpha = 0.1, 0.2, 0.5 and the standard expectation-value objective (alpha = 1), using both VQE with a hardware-efficient ansatz and QAOA. Experiments span multiple problem instances and sizes up to 20 qubits, and performance is assessed using overlap with the optimal solution, success rate defined as achieving at least 10% overlap, and convergence speed measured by normalized optimizer iterations and sometimes circuit repetitions. The study uses noiseless multishot simulation and a common classical optimizer (COBYLA) across all settings.

**Algorithms used:** VQE, QAOA, CVaR, ascending-CVaR, COBYLA
**Frameworks:** Qiskit Aer, NetworkX

**Experimental setup:** Classical numerical simulations/emulation only; no real quantum hardware. Experiments were run on IBM Qiskit Aer simulator in a noiseless multishot setting. Problem sizes were up to 20 qubits. Both VQE and QAOA were tested: VQE used a depth-1 hardware-efficient ansatz, while QAOA was tested for depths p = 1 to 6. Each instance was allowed up to 66 × (number of ansatz parameters) optimizer iterations. The same gradient-free classical optimizer, COBYLA, was used throughout. Default circuit executions were K = 1000 shots, scaled as K/alpha for CVaR-based objectives to maintain comparable estimation accuracy.

**Dataset:** Synthetic/computational benchmark instances rather than a conventional dataset. MaxCut used 100 random nonregular unweighted graph instances with 15-19 vertices sampled from graph classes via NetworkX, plus regular graph cases. Number partitioning used 300 random instances with 17-20 integers drawn uniformly from sets N1 = {0,...,200}, N2 = {0,...,500}, N3 = {0,...,750}, and for some QAOA tests a smaller set M = {0,...,50}. Portfolio optimization used 100 random portfolios with 16-20 assets, random budgets B drawn uniformly from {0,...,n}, and varying risk factors q; instances were defined by expected returns and covariance matrices.
## Findings
- [supported] The paper introduces an ascending-CVaR objective that dynamically increases the CVaR tail parameter during variational optimization and empirically outperforms fixed-CVaR and standard expectation-value objectives across MaxCut, number partitioning, and portfolio optimization in simulation.
- [supported] All experiments were conducted in a classical emulation/simulation environment using IBM Qiskit Aer with noiseless multishot circuit executions; no real quantum hardware results are reported.
- [supported] Across all tested problems, ascending-CVaR achieved higher overlap with the optimal state than fixed objective functions; the abstract reports up to 10x greater overlap for portfolio optimization and number partitioning and about 80% improvement for MaxCut.
- [supported] For hard number partitioning instances, standard objective functions found the correct solution in almost none of the cases, fixed CVaR found it in 60% of cases, and ascending-CVaR found it in 95% of cases.
- [supported] In MaxCut VQE on 100 random nonregular unweighted graphs with 15-19 vertices, ascending-CVaR succeeded on 96 instances versus 84, 81, 68, and 53 for fixed CVaR with alpha=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] In the same MaxCut VQE benchmark, average overlap was 64.69% for ascending-CVaR versus 12.13%, 21.45%, 39.28%, and 36.24% for fixed CVaR alpha=0.1, 0.2, 0.5, and expectation value respectively.
- [supported] For number partitioning VQE on 300 instances with 17-20 integers, ascending-CVaR consistently outperformed fixed objectives in both success rate and average overlap across all tested integer ranges.
- [supported] For number partitioning instances drawn from N1={0,...,200}, ascending-CVaR succeeded on 87% of cases with 54.17% average overlap, compared with 85%, 66%, 16%, and 2% success for fixed CVaR alpha=0.1, 0.2, 0.5, and expectation value.
- [supported] For harder number partitioning instances drawn from N2={0,...,500}, ascending-CVaR succeeded on 80% of cases with 48.33% average overlap, compared with 69%, 29%, 11%, and 0% success for fixed CVaR alpha=0.1, 0.2, 0.5, and expectation value.
- [supported] For the hardest number partitioning set N3={0,...,750}, using sigmoid ascending-CVaR yielded 95% success and 56.85% average overlap, versus 58%, 24%, 9%, and 0% success for fixed CVaR alpha=0.1, 0.2, 0.5, and expectation value.
- [supported] In portfolio optimization VQE on 100 random portfolios with 16-20 assets, ascending-CVaR succeeded on 100% of instances and achieved 63.25% average overlap, versus 13.35%, 24.74%, 9.42%, and 0.64% average overlap for fixed CVaR alpha=0.1, 0.2, 0.5, and expectation value.
- [supported] In the same portfolio optimization VQE benchmark, ascending-CVaR and fixed CVaR with alpha=0.1 or 0.2 reached at least 10% overlap in all instances, while expectation value succeeded in only 1% of cases and fixed CVaR alpha=0.5 in 16% of cases.
- [supported] Ascending-CVaR generally improved convergence speed as measured by normalized optimizer iterations to reach 10% overlap; for example, in portfolio optimization it required 9.64 iterations on average versus 11.13 and 16.29 for fixed CVaR alpha=0.1 and 0.2.
- [supported] For number partitioning, ascending-CVaR reached 10% overlap faster than fixed CVaR on N1 and N2, requiring 12.1 and 14.73 normalized iterations respectively versus 19.76 and 24.13 for fixed CVaR alpha=0.1.
- [supported] For MaxCut VQE, ascending-CVaR reached 10% overlap in 8.75 normalized iterations on average versus 9.3 and 10.8 for fixed CVaR alpha=0.1 and 0.2.
- [supported] QAOA with shallow depth (p up to 6) underperformed VQE across all three optimization problems, though ascending-CVaR still provided some improvement over fixed objectives in overlap and local-minimum avoidance.
- [supported] The authors report that VQE with hardware-efficient ansatz performed much better than shallow QAOA for these combinatorial optimization tasks under all objective-function choices tested.
- [speculative] The authors argue that ascending-CVaR works by changing the optimization landscape over time, helping the optimizer escape suboptimal local minima because local minima differ across CVaR alpha values.
- [speculative] The paper suggests that dynamic objective functions such as ascending-CVaR may help bring variational algorithms closer to useful quantum advantage, but this is not empirically demonstrated against classical state-of-the-art solvers.

**Results summary:** This peer-reviewed empirical paper evaluates an evolving objective function, ascending-CVaR, for variational quantum optimization on MaxCut, number partitioning, and portfolio optimization. All results are from noiseless classical simulation/emulation using Qiskit Aer, not real hardware. The main empirical result is that ascending-CVaR consistently outperforms both fixed-CVaR and standard expectation-value objectives, especially in VQE with a hardware-efficient ansatz. Reported gains include up to 10x higher overlap with the optimal state for portfolio optimization and number partitioning, around 80% improvement for MaxCut, and substantially higher success rates on hard instances. In hard number partitioning cases, standard objectives almost always failed, fixed CVaR solved 60% of cases, and ascending-CVaR solved 95%. Portfolio optimization showed the strongest VQE performance, with 100% success and 63.25% average overlap for ascending-CVaR on 100 random 16-20 asset instances. Shallow QAOA improved somewhat under ascending-CVaR but remained substantially weaker than VQE.

**Performance claims:**
- Up to 10x greater overlap for portfolio optimization and number partitioning versus standard objectives
- About 80% overlap improvement for MaxCut
- Hard number partitioning: standard objective fails in almost all cases, fixed CVaR solves 60% of cases, ascending-CVaR solves 95% of cases
- MaxCut VQE on 100 random nonregular graphs (15-19 vertices): success counts 96 (ascending-CVaR) vs 84, 81, 68, 53 (fixed CVaR alpha=0.1, 0.2, 0.5, expectation)
- MaxCut VQE average overlap: 64.69% (ascending-CVaR) vs 12.13%, 21.45%, 39.28%, 36.24%
- Number partitioning VQE on N1={0,...,200}: success 87% vs 85%, 66%, 16%, 2%; average overlap 54.17% vs 11.50%, 16.56%, 7.94%, 0.99%
- Number partitioning VQE on N2={0,...,500}: success 80% vs 69%, 29%, 11%, 0%; average overlap 48.33% vs 10.24%, 7.56%, 5.88%, 0.4%
- Number partitioning VQE on N3={0,...,750} with sigmoid ascending: success 95% vs 58%, 24%, 9%, 0%; average overlap 56.85% vs 8.24%, 5.84%, 3.45%, 0.16%
- Portfolio optimization VQE on 100 random portfolios (16-20 assets): success 100% vs 100%, 100%, 16%, 1%
- Portfolio optimization VQE average overlap: 63.25% (ascending-CVaR) vs 13.35%, 24.74%, 9.42%, 0.64%
- Average normalized iterations to reach 10% overlap: portfolio optimization 9.64 (ascending-CVaR) vs 11.13 and 16.29; number partitioning N1 12.1 vs 19.76 and 25.09; N2 14.73 vs 24.13 and 28.86; MaxCut 8.75 vs 9.3 and 10.8
## Quantum advantage claim
**Classification:** speculative

The paper discusses variational optimization as a route toward useful quantum advantage, but it does not demonstrate quantum advantage empirically. Results are from classical noiseless simulation only and compare quantum objective-function variants rather than quantum methods against best classical financial optimization baselines.
## Limitations
- Experiments are conducted only in a classical emulation/simulation environment rather than on real quantum hardware.
- Simulations are limited to relatively small problem sizes, using up to 20 qubits.
- The study focuses on shallow circuits, especially QAOA with depth p <= 6, so conclusions may not extend to deeper ansatz regimes.
- Performance depends sensitively on the hyperparameter λ (ascending factor), requiring careful tuning for each problem class and size.
- The authors note that if instance sizes increase or problems change, λ must be readjusted, limiting out-of-the-box scalability.
- The choice of ascending function (linear vs sigmoid) is empirical and problem dependent, without a principled selection rule.
- Results are based on noiseless multishot simulation, so robustness to hardware noise, decoherence, and gate errors is untested.
- The evaluation budget uses a fixed shot setting (K = 1000, scaled as K/α), which may not reflect realistic hardware resource constraints.
- Only three combinatorial optimization problems are studied: MaxCut, number partitioning, and portfolio optimization.
- Portfolio optimization experiments use randomly generated portfolios rather than clearly real market datasets, limiting direct financial realism.
- The study uses a single classical optimizer (COBYLA), so results may depend on optimizer choice and may not generalize across optimization strategies.
- Success is defined using a 10% overlap threshold, which is a somewhat arbitrary benchmark and may affect comparative conclusions.
- The paper emphasizes overlap and normalized optimizer iterations rather than full end-to-end production metrics relevant to financial deployment.
- [inferred] No experiments are reported on actual financial production-scale portfolio instances with realistic asset universes beyond about 20 assets.
- [inferred] No direct comparison is provided against state-of-the-art classical portfolio optimization solvers or financial heuristics, so practical advantage remains unclear.
- [inferred] Internal validity may be limited because improvements could partly depend on the chosen ansatz, initialization, optimizer, and benchmark design rather than the objective function alone.
- [inferred] Reproducibility is improved by code release, but exact replication may still depend on random seeds, simulator settings, and instance generation details not fully standardized in the text.
- [inferred] The method's scalability to production financial services is unclear because transaction costs, market impact, dynamic constraints, and regulatory requirements are not modeled.
## Open questions
- How should the ascending factor λ be chosen systematically based on the problem class and instance characteristics?
- What is the best ascending function to use for a given optimization problem or instance?
- Can the approach be theoretically connected to adiabatic quantum computing principles?
- How does ascending-CVaR perform on larger instances beyond 20 qubits?
- Will the observed gains persist on real noisy NISQ hardware rather than noiseless simulation?
- How robust is the method to sampling noise, readout error, decoherence, and imperfect gates?
- Can the optimization be truncated at α < 1 without sacrificing solution quality, and what threshold is best?
- Why does the method appear especially beneficial on harder instances, and can this be characterized theoretically?
- Under what conditions does sigmoid ascending outperform linear ascending, especially for larger or harder instances?
- Can ascending-CVaR mitigate barren plateaus or reachability deficits in a principled way for QAOA?
- How does the method compare with stronger classical baselines on portfolio optimization and other finance problems?
- Does the method remain effective for realistic financial portfolio models with more assets, richer constraints, and real market data?

**Future work:**
- Develop a more systematic rule for selecting the hyperparameter λ based on the problem and instance features.
- Investigate principled ways to choose the ascending function governing how α increases during optimization.
- Generalize the approach beyond the specific ascending-CVaR schedules tested in the paper.
- Explore other dynamic objective functions for variational quantum algorithms.
- Study theoretical connections between the proposed method and adiabatic quantum computing.
- Test the method on larger and harder problem instances, potentially around ~50 qubits as suggested in discussion.
- Examine whether optimization can be truncated before α reaches 1 to reduce iterations while retaining sufficient overlap.
- Evaluate the method under more realistic hardware conditions, including noise and decoherence. 
- Assess performance with alternative ansatz choices, optimizers, and initialization strategies.
- Apply the method to broader application domains beyond the three benchmark combinatorial problems.
- [inferred] Validate the approach on real financial datasets and more realistic portfolio optimization formulations relevant to industry use.
- [inferred] Benchmark against state-of-the-art classical financial optimization methods to assess any practical quantum advantage.
## Key ideas
- #idea:hybrid-approach — Proposes ascending-CVaR, a dynamically changing variational objective that interpolates from small-tail CVaR to full expectation value during training to improve optimization.
- #idea:near-term-feasibility — In noiseless simulations up to 20 qubits, ascending-CVaR improves convergence speed and overlap for VQE and to a lesser extent QAOA, positioning it as a potentially useful NISQ-era heuristic.
- #idea:quantum-advantage — The paper suggests dynamic CVaR objectives may move variational algorithms closer to useful quantum advantage, with especially strong simulated gains on portfolio optimization instances.
- #idea:hybrid-approach — Portfolio optimization is formulated as an Ising/QUBO problem and solved with variational quantum circuits plus a classical optimizer (COBYLA), exemplifying a quantum-classical workflow.
- #idea:near-term-feasibility — VQE with a shallow hardware-efficient ansatz outperformed shallow QAOA across tested combinatorial problems, including portfolio optimization.
## Contradictions
- The paper gestures toward quantum advantage, but its evidence is limited to noiseless classical simulation and comparisons among quantum objective variants rather than against strong classical financial solvers; this supports contradiction:classical-vs-quantum.
- Claims of practical relevance for financial portfolio optimization are undermined by the small scale (16-20 assets/qubits), synthetic portfolios, and need to retune the ascending schedule hyperparameter λ across settings; this supports contradiction:scalability.
- The paper frames the method as near-term applicable, yet it provides no hardware validation and explicitly leaves robustness to noise, decoherence, and realistic resource constraints unresolved.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Inputs consisted of optimization instances encoded as Ising/QUBO Hamiltonians. MaxCut: random unweighted graphs with 15-19 vertices, including 100 random nonregular instances sampled using NetworkX. Number partitioning: 300 random instances of 17-20 integers drawn uniformly from N1={0,...,200}, N2={0,...,500}, and N3={0,...,750}; additional QAOA experiments used M={0,...,50}. Portfolio optimization: 100 random portfolio instances with 16-20 assets, expected returns and covariance matrices, budget B sampled uniformly from {0,...,n}, and multiple risk factors q. No real-world financial market dataset or time period is specified; portfolio data appear to be synthetic/randomly generated problem instances.

### Process
For each problem instance, the classical optimization problem was mapped to a qubit Hamiltonian. A variational circuit was initialized with random parameters, using the same initialization across objective-function variants for fair comparison. The authors optimized either VQE with a hardware-efficient ansatz or QAOA. At each iteration, the circuit was executed for K=1000 shots in the expectation-value case and effectively K/alpha shots for CVaR-based objectives so that only the lowest-energy alpha fraction of samples was used while preserving comparable estimation accuracy. Ascending-CVaR updated alpha dynamically during optimization: linear ascending used alpha_{t+1} = alpha_t + lambda with lambda typically in [0.025, 0.045], and sigmoid ascending used alpha_t = 1/(1+e^(5-lambda t)) with lambda typically in [0.3, 0.4]. The initial alpha for ascending-CVaR was often 0.01. Fixed baselines used alpha = 0.1, 0.2, 0.5, and 1.0. VQE experiments mainly used depth p=1 because this already gave strong performance; QAOA was tested for p=1 to 6. Optimization stopped when the iteration budget was exhausted or convergence/stopping conditions were met, and the resulting state overlap with the known optimum was evaluated.

### Output
Reported outputs include overlap with the optimal solution (probability mass on the optimal computational basis state or degenerate ground-state subspace), success rate defined as the percentage of instances achieving at least 10% overlap, average overlap across instances, and convergence speed measured by normalized optimizer iterations to reach 10% overlap; some appendix results also compare total circuit repetitions. Baseline comparisons were made against fixed-CVaR objectives with alpha = 0.1, 0.2, 0.5 and the standard expectation-value objective (alpha = 1). Results are presented separately for MaxCut, number partitioning, and portfolio optimization, and for VQE versus QAOA.

### Parameters
- max_qubits: 20
- shots_base: 1000
- shots_scaling_for_cvar: K/alpha
- optimizer: COBYLA
- max_optimizer_iterations: 66 × number of ansatz parameters
- vqe_ansatz: hardware-efficient ansatz with Ry rotations and CZ entanglers
- vqe_depth: 1
- vqe_parameter_count: n(1+p)
- qaoa_depth_range: p = 1 to 6
- qaoa_parameter_count: 2p
- fixed_cvar_alphas: [0.1, 0.2, 0.5, 1.0]
- ascending_cvar_initial_alpha: 0.01
- linear_ascending_lambda_range: [0.025, 0.045]
- sigmoid_ascending_lambda_range: [0.3, 0.4]
- example_linear_lambda_values_used: [0.03, 0.045]
- success_threshold_overlap: 0.1

### Hardware
IBM Qiskit Aer simulator; noiseless multishot circuit execution; no real QPU used. The paper describes experiments as classical numerical simulations/emulation up to 20 qubits. No noise model, cloud backend, or transpilation settings are specified.

### Reproducibility
Code is available on GitHub (link provided in the paper). Instance-generation procedures and many hyperparameters are described, including optimizer, shot count, alpha schedules, and problem-size ranges. Reproducibility is reasonably good for simulation-based replication, though some portfolio instance-generation details are not fully specified and exact random seeds are not reported.
