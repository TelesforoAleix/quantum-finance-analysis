---
aliases:
- Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing
- Approaching Collateral Optimization NISQ
authors:
- Megan C. Giron
- Georgios Korpas
- Waqas Parvaiz
- Prashant Malik
- Johannes Aspman
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/TQE.2023.3314839
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
- idea:quantum-advantage
journal_or_venue: IEEE Transactions on Quantum Engineering
methodology_tags:
- quantum-annealing
- QUBO
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- Pusey-Nazzaro_UnknownTitle
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T16:00:27.524041'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:32.708007'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:01:22.210417'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:39.468984'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:02:12.725401'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:02:27.240443'
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
- method/quantum-annealing
- method/QUBO
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- idea/quantum-advantage
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Approaching Collateral Optimization for NISQ and Quantum-Inspired Computing
topic_tags:
- portfolio-optimisation
year: 2023
zotero_key: ''
---

## Abstract summary
The paper formulates the collateral optimization problem faced by financial institutions as a mixed-integer linear program and then derives several QUBO encodings to make it amenable to NISQ-era quantum and quantum-inspired solvers. Using small synthetic instances, the authors compare slack-based and unbalanced-penalty QUBO formulations, implemented with simulated and digital annealing, against classical MILP baselines. They find that while the QUBO approaches do not reach the global optimum on these small but constrained instances, they produce near-optimal solutions and illustrate how collateral optimization can be structured for future quantum and hybrid hardware, alongside a survey of alternative QUBO-based optimization methods relevant to finance.
## Methodology
The paper presents an empirical case study on collateral optimization in financial services by first formulating the problem as a mixed-integer/linear optimization model and then converting it into QUBO forms suitable for NISQ and quantum-inspired optimization. The authors develop a business-realistic MILP for allocating collateral assets across accounts under exposure, consistency, and allocation-limit constraints, then derive two QUBO variants: a balanced slack-variable formulation and an unbalanced penalization formulation. To inform the formulation choices, they first run small-scale experiments on a toy 10-item knapsack instance with known optimum, comparing classical MILP solvers against several QUBO encodings and annealing-based solvers. They then evaluate a synthetic but realistic small collateral optimization instance with 10 assets and 5 accounts, using simulated annealing and a Fujitsu digital annealer emulator, and compare outputs against the global optimum obtained by a classical LP/MILP solver (HiGHS/simplex). The study is explicitly framed as heuristic and small-scale, focused on formulation behavior rather than demonstrating quantum advantage. Evaluation emphasizes objective-value proximity to the classical optimum and degree of constraint satisfaction, especially exposure fulfillment and consistency constraints.

**Algorithms used:** QUBO, simulated annealing, digital annealing
**Frameworks:** Qiskit, Qiskit Optimization, ToQUBO.jl, QUBODrives.jl, PyQUBO, JuMP, HiGHS, GLPK, neal

**Experimental setup:** Experiments were local, small-scale computational tests. Classical baselines used HiGHS and GLPK for the knapsack problem and HiGHS/simplex for the collateral optimization benchmark. QUBO experiments used D-Wave's neal simulated annealer, Qiskit Optimization's QuadraticProgramToQubo conversion, ToQUBO.jl, PyQUBO, and an emulation of Fujitsu's proprietary digital annealer rather than real quantum hardware. The collateral optimization experiments were run on an Apple MacBook Pro with M2 Max processor and 16 GB memory.

**Dataset:** Two datasets were used: (1) a toy 10-item knapsack instance from the literature with known optimal solution; and (2) a synthetic but business-realistic collateral optimization dataset consisting of a portfolio of 10 assets with total value about $8.86M and 5 accounts with exposure requirements, including asset tiers, quantities, market values, haircuts, and account durations.
## Findings
- [supported] The paper formulates collateral optimization as both an MILP and a QUBO problem suitable for hybrid quantum, quantum-inspired, and annealing-based solvers.
- [supported] In small-scale collateral optimization experiments on synthetic but business-realistic data, neither the balanced slack-based QUBO nor the unbalanced-penalization QUBO reached the global optimum found by the classical HiGHS solver.
- [supported] The unbalanced-penalization QUBO produced objective values closer to the global optimum than the balanced slack-based QUBO in the reported collateral optimization tests.
- [supported] QUBO-based approaches for collateral optimization produced solutions reasonably close to the global optimum in small-scale experiments, despite failing to find the exact optimum.
- [supported] Results in this paper are based on simulation/emulation and classical quantum-inspired solvers, not on real quantum hardware.
- [supported] For the benchmark 10-item knapsack instance, multiple QUBO encodings solved with simulated annealing and Fujitsu digital annealer emulation recovered the known optimum value of 309.
- [supported] In the knapsack benchmark, Qiskit's automatically generated QUBO also reached the optimum, but required a relatively large number of runs compared with other methods.
- [supported] The one-hot slack encoding for the knapsack instance required 165 slack bits, whereas the log encoding required 8 slack bits, illustrating a substantial resource trade-off between encodings.
- [supported] For the collateral optimization instance with 10 assets, 5 accounts, and 7-bit allocation encoding, the nominal binary formulation required 350 bits, reduced to 298 bits for the balanced formulation and 228 bits for the unbalanced formulation under the authors' constraint handling choices.
- [speculative] The authors argue that QUBO formulations for collateral optimization may be promising for larger instances and future real quantum or quantum-inspired hardware, but this is not demonstrated empirically in the paper.
- [speculative] The paper frames its contribution as part of the broader effort toward practical quantum advantage, but does not demonstrate quantum advantage over classical optimization.

**Results summary:** This peer-reviewed empirical paper develops an MILP and two QUBO formulations for collateral optimization in financial services and evaluates them on small-scale tests using simulated annealing, software toolchains, and emulations of quantum-inspired hardware. On a synthetic collateral optimization instance with 10 assets and 5 accounts, the QUBO-based methods did not recover the global optimum obtained by the classical HiGHS solver, although the unbalanced-penalization formulation produced solutions closer to the optimum than the balanced slack-based formulation. The study emphasizes that all reported optimization results are heuristic and based on simulation/emulation rather than real quantum hardware. As a calibration exercise, the authors also tested several QUBO encodings on a 10-item knapsack benchmark, where simulated annealing and Fujitsu digital annealer emulation recovered the known optimum objective value of 309. Overall, the paper supports the feasibility of formulating collateral optimization for NISQ/quantum-inspired workflows, but does not show a quantum performance advantage.

**Performance claims:**
- Knapsack benchmark known optimum objective value: 309, recovered by HiGHS, GLPK, ToQUBO.jl-based QUBOs, simulated annealing, PyQUBO, and Fujitsu digital annealer emulation
- Knapsack log-encoding slack bits: 8
- Knapsack one-hot slack bits: 165
- Knapsack one-hot encoding found optimum with penalty weights lambda0 = 10^-1 and lambda1 = 10^3
- Knapsack log encoding found optimum under both lambda0 = 1 and lambda0 = 1 x 10^4
- Collateral optimization test instance: 10 assets, 5 accounts, approximate total asset value $8.86M
- Collateral optimization exposures: 2 long-term accounts with combined exposure about $1.49M; 3 short-term accounts with total exposure about $1.09M
- Collateral optimization allocation encoding length: 7 bits per allocation, giving granularity 1/127 ≈ 0.0079%
- Collateral optimization nominal bit count without inequality-constraint handling: 350 bits
- Collateral optimization bit count after formulation choices: 298 bits for balanced QUBO, 228 bits for unbalanced QUBO
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. Results are from simulation/emulation and quantum-inspired methods on small instances, and the QUBO approaches failed to reach the classical global optimum for the collateral optimization case. Any claim that the approach could yield future advantage on larger instances or real hardware remains speculative.
## Limitations
- Experiments are limited to small-scale synthetic collateral optimization instances and local computational tests rather than realistic large-scale production workloads.
- The QUBO-based approaches failed to find the global optimum even on a relatively small but nontrivial collateral optimization instance.
- Results are heuristic in nature, and the authors explicitly do not provide an empirical comparison between quantum and classical approaches for solving MILPs.
- The study does not run on specialized quantum hardware or production digital annealers; instead it uses small emulations of hybrid solvers and simulated annealing.
- Limited computational resources constrained the scope of benchmarking and the number of runs performed.
- A modest number of annealing runs was used, which the authors note likely prevented sufficient exploration of the search space.
- There is a tradeoff between allocation precision and runtime/resource usage because continuous allocations must be binarized with finite bit depth.
- Binarization reduces solution accuracy and imposes granularity constraints on allocations.
- The one-to-one constraint handling in the QUBO can be more restrictive than the MILP formulation because bit counts are floored to avoid violations.
- The balanced slack-based formulation requires many slack bits, creating substantial resource overhead.
- The exposure requirement had to be relaxed/modified in the balanced QUBO formulation by converting an inequality into an equality, which changes the original problem structure.
- Annealing methods can get trapped in local minima, causing under- or over-satisfaction of exposure requirements.
- The many-to-one/group constraints were removed in the numerical experiments, so the tested instance is a relaxed version of the full collateral optimization problem.
- The study focuses on cash allocation and avoids integer constraints associated with equities and bonds, limiting representativeness of full collateral management practice.
- Penalty/Lagrange multiplier tuning is difficult because coefficients differ significantly in magnitude across QUBO terms.
- The authors treat exposure requirements as soft constraints in practice, allowing small violations, which may weaken business validity.
- Reproducibility is limited by reliance on emulator settings, heuristic tuning choices, and proprietary Fujitsu digital annealer emulation details.
- [inferred] No evaluation is reported on real bank collateral datasets, so external validity to live financial operations is unclear.
- [inferred] No direct comparison is made against state-of-the-art commercial MILP solvers on realistic large instances, limiting claims about practical advantage.
- [inferred] No hardware noise analysis is performed because experiments are not conducted on actual NISQ devices, so conclusions about real quantum deployment are incomplete.
- [inferred] Scalability to production remains unverified given qubit/bit requirements of 228-350 variables even for a small instance and the omission of some real-world constraints.
- [inferred] Internal validity may be affected by manual normalization and retrospective tuning of penalty weights, which could bias outcomes toward selected formulations.
## Open questions
- Whether collateral optimization MILPs should be reformulated as QUBOs and solved heuristically rather than with strong classical MILP solvers.
- Which problem formulation, hyperparameter setting, and solver choice constitute the best overall strategy for quantum-ready collateral optimization.
- Whether the promising near-optimal behavior of QUBO formulations on small instances will translate to large real-world collateral optimization problems.
- How much performance improvement can be achieved through more runs, better annealing schedules, warm starts, and improved parameter optimization.
- How the proposed formulations will perform on specialized hardware such as real quantum annealers, gate-based quantum devices, or production digital annealers.
- Whether unbalanced penalization consistently outperforms slack-based formulations across broader classes of collateral optimization instances.
- How to enforce hard business constraints reliably in heuristic quantum/hybrid solvers without excessive resource overhead.
- How the methods scale when many-to-one/group constraints and more realistic asset classes are included.
- What level of discretization/bit depth is sufficient to preserve business-relevant solution quality without making the QUBO too large.
- Whether alternative quantum-ready formulations, such as implicit penalization or stochastic quantum Monte Carlo approaches, are better suited for collateral optimization.
- [inferred] Can these approaches deliver measurable business advantage over existing industrial optimization pipelines under realistic latency and compliance requirements?
- [inferred] How robust are the results across different synthetic or real market scenarios, haircut structures, and exposure distributions?

**Future work:**
- Investigate larger instances of the collateral optimization problem using the proposed QUBO formulations.
- Implement and test the formulations on real quantum or quantum-inspired hardware rather than only emulations.
- Increase the number of annealing runs and potentially decrease step size to improve search-space exploration.
- Apply warm-starting techniques to improve solution quality.
- Optimize the annealing schedule.
- Perform QUBO parameter optimization for better penalty-weight selection.
- Utilize GPU and tensor cores to improve computational performance.
- Explore improved methods for simulated annealing.
- Study alternative formulations of collateral optimization, since the presented formulations are not unique and may be improved.
- Investigate implicit-penalization Hamiltonian-restriction approaches such as parallelized QAOA-style formulations for collateral optimization.
- Explore stochastic quantum Monte Carlo methods that mimic quantum annealing for large-scale collateral optimization, especially for fully connected graphs.
- Reintroduce and test richer constraints such as many-to-one/group constraints in future experiments.
- [inferred] Benchmark against strong commercial MILP solvers on realistic large-scale collateral datasets.
- [inferred] Extend beyond cash-only allocation to include equities, bonds, and integer allocation constraints.
- [inferred] Evaluate robustness and reproducibility across multiple datasets, solver seeds, and hardware backends.
## Key ideas
- #idea:hybrid-approach — The paper reformulates collateral optimization from MILP into QUBO and positions hybrid quantum/quantum-inspired workflows as a practical route for financial optimization.
- #idea:near-term-feasibility — The study argues that small collateral optimization problems can already be structured for NISQ-era or annealing-style solvers through careful QUBO encoding.
- #idea:quantum-advantage — The paper speculates that QUBO-based collateral optimization could become advantageous on larger instances or future hardware, though this is not demonstrated.
- #idea:hybrid-approach — Unbalanced-penalty QUBO performed better than balanced slack-based QUBO on the small collateral instance, suggesting formulation choice is critical in hybrid workflows.
- #idea:near-term-feasibility — Resource counts differ sharply across encodings, with unbalanced formulations reducing binary variable requirements relative to slack-based formulations.
## Contradictions
- The paper makes speculative future-advantage claims, but its own experiments show classical HiGHS reaches the global optimum while QUBO-based annealing methods do not on the collateral optimization instance, creating a #contradiction:classical-vs-quantum.
- The paper suggests promise for larger real-world collateral optimization, but scalability is unverified because experiments are limited to a 10-asset, 5-account synthetic instance, omit some real constraints, and already require 228–350 binary variables, creating a #contradiction:scalability.
- The paper references prior work by Pusey-Nazzaro et al. indicating quantum annealing and simulated annealing can underperform classical branch-and-bound on NP-hard problems, which undercuts its speculative narrative of future quantum superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Knapsack input: a literature-based 10-item instance with item weights and values and known optimum. Collateral optimization input: synthetic small-scale financial data with 10 assets and 5 accounts; assets had tier ratings omega in {0.2, 0.5, 0.8} with 4 low-tier, 2 mid-tier, and 4 high-tier assets; combined asset value approximately $8.86M; 2 long-term accounts with combined exposure about $1.49M and 3 short-term accounts with total exposure about $1.09M. Many-to-one group constraints were removed to relax the instance. Fractional allocations were discretized using 7-bit encoding per asset-account allocation, giving granularity 1/127 (~0.0079%).

### Process
1. Formulate collateral optimization as an MILP/LP with objective to minimize collateral posting cost while satisfying exposure, consistency, and allocation-limit constraints. 2. Convert the problem to QUBO using two approaches: (a) balanced slack-variable encoding with log-encoded slack variables; (b) unbalanced penalization using Taylor-approximated exponential penalties to avoid slack variables. 3. Before applying to collateral optimization, test multiple QUBO encodings on a 10-item knapsack benchmark with known optimum using ToQUBO.jl, Qiskit Optimization, PyQUBO, neal, and Fujitsu digital annealer emulation. 4. For the collateral optimization instance, discretize each allocation with 7 bits. 5. Normalize QUBO terms by dividing by their largest coefficient and rescale so the smallest coefficient in each term is order 1. 6. Set the cost-function weight larger than constraint weights, then retrospectively increase exposure and consistency penalties to improve feasibility. 7. Solve the balanced and unbalanced QUBOs using neal simulated annealing and Fujitsu digital annealer emulation. 8. Compare resulting allocations and objective values against the classical HiGHS optimum and inspect exposure satisfaction per account. The paper notes only a modest number of runs were used due to limited computational resources, and no global optimum was reached by the heuristic QUBO solvers.

### Output
Outputs include objective function values for different QUBO formulations and solvers, allocation matrices/plots showing how assets were assigned to short-term versus long-term accounts, and percentage differences between posted collateral values and required exposures for each account. Baseline comparisons were made against classical solvers: HiGHS and GLPK for the knapsack benchmark, and HiGHS/simplex for the collateral optimization global optimum. The main reported finding is that QUBO-based heuristic methods did not reach the global optimum on the small collateral instance, but the unbalanced penalization formulation produced objective values closer to the classical optimum than the balanced slack-based formulation.

### Parameters
- collateral_instance_assets: 10
- collateral_instance_accounts: 5
- bitstring_length_per_allocation: 7
- allocation_granularity: 1/127 (~0.0079%)
- full_qubit_count_without_inequality_reduction: 350
- qubits_unbalanced_formulation: 228
- qubits_balanced_formulation: 298
- hardware_host_machine: Apple MacBook Pro, M2 Max, 16 GB RAM
- knapsack_log_encoding_slack_bits: 8
- knapsack_one_hot_slack_bits: 165
- knapsack_log_encoding_penalties_tested: [{'lambda_0': 1}, {'lambda_0': 10000.0}]
- knapsack_one_hot_penalties: {'lambda_0': 0.1, 'lambda_1': 1000.0}
- constraint_handling: {'balanced': 'log-encoded slack variables', 'unbalanced': 'second-order Taylor approximation of exponential penalties'}

### Hardware
No real QPU was used. The study used classical hardware and emulators: D-Wave's neal simulated annealer, emulation of Fujitsu's digital annealer, and local execution on an Apple MacBook Pro with M2 Max and 16 GB RAM. The paper explicitly states computations were not run on specialized hardware such as a real quantum annealer or digital annealer.

### Reproducibility
Partial reproducibility. The paper provides detailed mathematical formulations, solver names, encoding choices, dataset characteristics, and several key parameter values, which should allow approximate replication. However, full synthetic dataset values, exact annealing schedules/run counts, and complete penalty-weight settings for all experiments are not fully specified in the provided text, and no code repository is mentioned. Replication is feasible in principle but not turnkey.
