---
aliases:
- Accelerated quantum Monte Carlo with probabilistic computers
- Accelerated quantum Monte Carlo
authors:
- Shuvro Chowdhury
- Kerem Y. Camsari
- Supriyo Datta
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1038/s42005-023-01202-3
evidence_type: ''
idea_tags:
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Communications Physics
methodology_tags:
- classical-simulation
paper_type: ''
quantum_advantage_claim: not-applicable
related_papers:
- 2018_King_ObservationOfTopologicalPhenomena
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:59:59.080938'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:00:02.717117'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:00:37.254506'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:01:12.299618'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:01:50.017173'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:01:59.884679'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/classical-simulation
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Accelerated quantum Monte Carlo with probabilistic computers
topic_tags: []
year: 2023
zotero_key: ''
---

## Abstract summary
The paper presents hardware acceleration of quantum Monte Carlo simulations for transverse field Ising models using probabilistic-bit (p-bit) based architectures. The authors implement a graph-colored, massively parallel discrete-time path integral Monte Carlo scheme on an FPGA and project additional gains from a clockless analog p-computer design. They benchmark these approaches against optimized CPU codes and a D-Wave quantum annealer, outlining a roadmap to achieve 5–6 orders of magnitude speedup in convergence time for stoquastic quantum problems.
## Methodology
The study is an empirical hardware-benchmarking paper that evaluates whether a probabilistic computer based on p-bits can accelerate discrete-time path integral Monte Carlo (DT-PIMC) simulation of a stoquastic transverse-field Ising model (TFIM). The authors map the quantum Hamiltonian on a frustrated square-octagonal lattice to a classical replicated system using the Suzuki-Trotter approximation, using 10 replicas in the main p-computer experiments. They design a graph-colored update scheme to enable massive parallel updates of p-bits while avoiding simultaneous updates of connected nodes; because the replicated lattice is bipartite, only two colors are needed, allowing one sweep every two clock cycles. The methodology combines: (1) CPU simulations of the graph-colored DT-PIMC emulator, (2) an FPGA implementation on an AWS F1 instance for the smallest lattice, and (3) SPICE simulations of a clockless analog p-computer using resistive synapses and low-barrier-magnet-inspired p-bit models. Performance is assessed by tracking the relaxation of an order parameter from specified initial states (mainly counterclockwise wound, with discussion of clockwise and ordered states), fitting the time evolution with a double-exponential-plus-offset model, and defining convergence time as the time to reach a fixed mean squared error threshold of 0.0025 relative to the fitted equilibrium value. The p-computer results are compared against an optimized 4q continuous-time PIMC CPU baseline and published quantum annealer results from King et al. The paper reports both absolute speedup and scaling behavior with lattice size, and also quantifies Trotterization error by comparing 10-replica DT-PIMC equilibrium values against 4q CT-PIMC outputs.

**Algorithms used:** Discrete-time Path Integral Monte Carlo (DT-PIMC), Continuous-time Path Integral Monte Carlo (CT-PIMC), Suzuki-Trotter approximation, Graph coloring update scheme, Metropolis / Gibbs-style p-bit sampling
**Frameworks:** MATLAB, SPICE, Amazon Web Services F1

**Experimental setup:** Experiments combine software simulation and hardware emulation. The main quantum problem is a transverse-field Ising Hamiltonian on a square-octagonal lattice with total qubit count 4L(2L-6), benchmarked for lattice sizes up to L=15 (up to 1,440 qubits in the original lattice). The DT-PIMC mapping uses 10 replicas, producing up to 14,400 p-bits. Actual digital hardware emulation was performed only for the smallest lattice (L=6) on an FPGA running at 125 MHz with an 8 ns clock period and 16 ns per sweep due to two-color updates. Larger digital p-computer results were projected from CPU/MATLAB simulations assuming the same sweep timing. A separate analog clockless architecture was evaluated in SPICE on a 6x6 triangular antiferromagnetic lattice using resistive synapses and p-bit device models. CPU-side graph-colored simulations were run on an Intel Core i7-10750H, 2.60 GHz, 16 GB RAM, Windows 11, single-threaded.

**Dataset:** No financial or external dataset is used. The input consists of synthetic physics benchmark instances: frustrated square-octagonal TFIM lattices and a 6x6 triangular antiferromagnetic lattice for analog SPICE validation. Initial conditions include counterclockwise wound, clockwise wound, and ordered states, with most reported scaling results focused on the counterclockwise wound state.
## Experiment details
### Input
Synthetic benchmark problem defined by the stoquastic transverse-field Ising Hamiltonian H_Q = -sum_{<ij>} J_ij sigma^z_i sigma^z_j + Gamma sum_i sigma^x_i on a square-octagonal lattice. Lattice sizes include 6x6, 12x9, 18x12, and 24x15 square-octagonal instances corresponding to N_Q = 4L(2L-6) qubits, up to 1,440 qubits for L=15. Couplings: ferromagnetic J_FM = -1.8, antiferromagnetic J_AFM = 1.0 in bulk, and boundary AFM couplings reduced to 0.5. Main benchmark parameters: Gamma = 0.736 and beta = 1/0.244. DT-PIMC uses 10 Trotter replicas. For analog validation, a 6x6 triangular AFM lattice with beta = 2 is used. Order parameter is computed by averaging four FM-coupled qubits into a triangular-lattice basis, forming complex pseudospins per plaquette, averaging over plaquettes, then averaging absolute values over configurations/runs. Results are averaged over 1000 runs for most digital experiments and 500 runs for SPICE analog experiments, with different RNG seeds to reduce autocorrelation.

### Process
1. Define the TFIM benchmark instance on the square-octagonal lattice with specified FM/AFM couplings and initial state. 2. Map the quantum partition function to a classical replicated Ising system using the Suzuki-Trotter approximation, with J_k,ij = J_ij/r and inter-replica coupling J_perp = -(0.5/beta) ln[tanh(beta*Gamma/r)], using r = 10 replicas. 3. Replace qubits by p-bits and construct the replicated p-bit network. 4. Apply graph coloring to the replicated network; because the network is bipartite for even replica count, use two colors so half the p-bits are updated in one clock cycle and the other half in the next, yielding one sweep every two cycles. 5. Run the graph-colored DT-PIMC emulator in MATLAB/CPU and on FPGA for the smallest lattice; for larger lattices, project wall-clock time from CPU sweep counts using the measured FPGA sweep time. 6. Compute the average order parameter versus time by averaging across many independent runs with different random seeds at matched time points. 7. Fit each relaxation curve with a*exp(-b x) + c*exp(-d x) + g, where g estimates the equilibrium order parameter. 8. Compute mean squared error versus time from the fitted equilibrium value and define convergence time as the time to reach MSE = 0.0025, equivalent to reaching g - 0.05. 9. Compare equilibrium values from 10-replica DT-PIMC against 4q CT-PIMC to quantify Trotter error. 10. For analog clockless validation, simulate a resistive-synapse p-computer in SPICE without global clocking, allowing asynchronous updates and comparing convergence against a graph-colored digital implementation on a 6x6 triangular AFM lattice. 11. Compare convergence-time scaling against optimized CPU CT-PIMC and published quantum annealer results from King et al.

### Output
Primary outputs are relaxation curves of the average order parameter <m(t)>, fitted equilibrium values g, mean squared error decay over time, and convergence times extracted at an MSE threshold of 0.0025. The paper reports speedup factors and scaling laws versus number of qubits, including approximately N_Q^2 scaling for optimized CPU CT-PIMC, approximately N_Q scaling for the p-computer, and projected clockless analog performance within less than one order of magnitude of the quantum annealer. Baseline comparisons include optimized 4q CT-PIMC on CPU, graph-colored MATLAB simulation on CPU, FPGA-based digital p-computer emulation, projected clockless analog p-computer, and published quantum annealing processor results. Fidelity is also reported via equilibrium-value differences between 10-replica DT-PIMC and 4q CT-PIMC, with absolute errors around 0.01-0.03.

### Parameters
- replicas: 10
- qubit_count_formula: N_Q = 4L(2L-6)
- max_qubits_original_lattice: 1440
- max_pbits_replicated_network: 14400
- graph_coloring_colors_main: 2
- graph_coloring_colors_triangular_example: 3
- clock_frequency_fpga: 125 MHz
- clock_period_fpga: 8 ns
- sweep_time_fpga_main: 16 ns per sweep
- Gamma_main: 0.736
- beta_main: 1/0.244
- beta_triangular_example: 2
- J_FM: -1.8
- J_AFM_bulk: 1.0
- J_AFM_boundary: 0.5
- digital_runs_averaged: 1000
- spice_runs_averaged: 500
- fit_model: a*exp(-b x) + c*exp(-d x) + g
- convergence_mse_threshold: 0.0025
- analog_synapse_resistances: {'R0': '15 MOhm', 'Rr': 'R0/10', 'Rb': 'R0/4', 'R1': 'R0/3.5', 'R1_open_boundary_mag1': 'R0/2', 'R1_open_boundary_mag0.5': 'R0'}

### Hardware
Digital hardware: FPGA emulation on Amazon Web Services F1 instance; actual implementation demonstrated for the smallest lattice only, operating at 125 MHz with 8 ns clock period. CPU environment for graph-colored MATLAB simulations: Intel Core i7-10750H CPU @ 2.60 GHz, 16 GB RAM, Windows 11 Home, single-threaded. Analog hardware evaluation: SPICE simulations of a clockless mixed-signal p-computer using resistive synapses and p-bit models based on experimentally benchmarked low-barrier magnet / stochastic MTJ concepts. Comparisons also include published data from a physical D-Wave quantum annealing processor reported in King et al., but that hardware was not directly used by the authors.

### Reproducibility
Partial reproducibility. The paper provides substantial methodological detail, equations, lattice definitions, coupling values, replica count, convergence criterion, fitting model, hardware timing assumptions, and CPU specifications. However, code and figure data are not publicly linked; both are available only upon request from the authors. FPGA implementation details are partly deferred to supplementary material, and most larger-lattice FPGA results are projections rather than direct hardware runs. Replication appears feasible but not turnkey.
## Findings
- [supported] A graph-colored digital probabilistic computer (p-computer) implemented on FPGA achieved about 2–3 orders of magnitude faster convergence than a single-thread CPU implementation for the benchmark transverse-field Ising model (TFIM) quantum Monte Carlo task, with the largest studied lattice projected to be about 1000× faster than CPU.
- [supported] The digital p-computer result is empirical only for the smallest lattice (L = 6) on real FPGA hardware; larger-lattice performance is projected from CPU simulations using the measured FPGA sweep time of 16 ns per sweep.
- [supported] Using 10 Suzuki–Trotter replicas, the p-computer reproduced 4q continuous-time PIMC equilibrium values with absolute error 0.01–0.03 and relative error about 2–4% across the tested lattice sizes.
- [supported] The average order-parameter curves in Fig. 3 were averaged over 1000 runs and reported with 95% confidence intervals around the mean.
- [supported] The clockless analog p-computer was not built in hardware but evaluated via SPICE simulation using experimentally benchmarked device models; in a 6×6 triangular AFM example it converged in about 5 ns versus about 1.73 μs for a comparable 125 MHz 3-colored digital implementation, implying about 400× speedup.
- [supported] The authors report that convergence time scales approximately as N for the p-computer versus roughly N^2 for CPU implementations on this benchmark, attributing the improvement to hardware parallelism rather than a new algorithmic improvement.
- [supported] The clockless analog hardware is estimated to deliver performance within a factor of less than 10 of the quantum annealer on this benchmark, based on projected rather than direct hardware measurements.
- [speculative] The paper proposes a roadmap to 5–6 orders of magnitude acceleration for TFIM quantum Monte Carlo and possible extension to other QMC models, but the full 5–6 order gain is not directly demonstrated experimentally.
- [speculative] The claim that up to one million p-bits could be integrated on-chip with reasonable power budget is an architectural projection rather than an empirical result in this paper.
- [speculative] The suggestion that mixed-signal ASICs with stochastic MTJ-based p-bits could close the gap to quantum annealers by another 1–3 orders of magnitude is based on projections and SPICE/device-model simulations, not fabricated hardware.
- [supported] The paper explicitly states that its observed scaling improvement over CPU arises from exploiting massive parallelism in custom hardware and not from an algorithmic quantum speedup.
- [supported] This work does not demonstrate quantum advantage; instead it benchmarks classical probabilistic hardware against CPU and compares projected performance to previously published quantum annealer results.

**Results summary:** This peer-reviewed empirical paper studies hardware acceleration of quantum Monte Carlo for a stoquastic transverse-field Ising model using classical probabilistic computers based on p-bits. On real hardware, the authors implemented the smallest instance on a 125 MHz FPGA and used graph coloring to update half the p-bits per clock cycle, yielding a measured 16 ns per sweep and projected roughly 1000× faster convergence than a single-thread CPU for the largest benchmarked lattice. Accuracy relative to a reference 4q continuous-time PIMC method was maintained with 10 replicas, giving absolute equilibrium-value errors of 0.01–0.03 (about 2–4% relative). For larger lattices, however, the FPGA results are projections derived from CPU simulations rather than direct hardware runs. The analog clockless p-computer results are also not from fabricated hardware; they come from SPICE simulations using experimentally benchmarked models and suggest an additional 2–3 orders of magnitude speedup, including a 400× improvement over a comparable digital implementation in a 6×6 triangular-lattice example. The authors report approximate N scaling for p-computer convergence time versus N^2 for CPU on this benchmark, but they attribute this to hardware parallelism rather than any algorithmic or quantum advantage.

**Performance claims:**
- 2–3 orders of magnitude acceleration of a standard QMC algorithm using a specially designed digital processor versus CPU
- A further 2–3 orders of magnitude acceleration projected by mapping to a clockless analog processor
- Roadmap to 5–6 orders of magnitude acceleration for TFIM QMC
- Clockless analog hardware performance within a factor of <10 of the quantum annealer
- Convergence time scaling approximately as N for clockless analog/p-computer hardware versus approximately N^2 for CPU implementations
- For the largest lattice size (L = 15), projected about 1000× improvement over a single-thread CPU implementation
- FPGA implementation used 8 ns clock period and 16 ns per sweep for the 2-color graph-colored design
- With 10 replicas, equilibrium-value absolute error versus 4q CT-PIMC was 0.01–0.03, with relative error about 2–4%
- Fig. 3 results averaged over 1000 runs with 95% confidence intervals
- In SPICE, a 6×6 triangular AFM analog clockless design converged in about 5 ns versus about 1.73 μs for a comparable 125 MHz 3-colored digital design, about 400× faster
- Actual FPGA design achieved about 90 flips/ns for the smallest lattice, compared with cited GPU literature values of about 10–30 flips/ns for bipartite graphs
## Quantum advantage claim
**Classification:** not-applicable

The paper does not claim a demonstrated quantum advantage from its own results. It evaluates classical probabilistic hardware (FPGA and SPICE-simulated analog p-computers) for accelerating QMC and compares them with CPU and previously published quantum annealer data. Any comparison to quantum annealers is indirect and largely projected; the reported gains are classical hardware-parallelism advantages, not quantum advantage.
## Limitations
- Only the smallest lattice size (L = 6) was implemented on actual FPGA hardware; results for larger lattice sizes are projections based on CPU simulations rather than direct hardware measurements.
- Digital p-bit implementations are resource intensive, requiring thousands of transistors per p-bit, which limited the FPGA study to the smallest problem instance.
- The analog clockless p-computer results are based on SPICE simulations using experimentally benchmarked models, not fabricated hardware measurements.
- The clockless analog demonstration was performed on a simplified 6 × 6 classical triangular AFM lattice rather than the full square-octagonal TFIM benchmark used elsewhere in the paper.
- The DT-PIMC approach relies on the Suzuki-Trotter approximation with a finite number of replicas; with 10 replicas there remains a nonzero approximation error relative to CT-PIMC.
- The benchmark is restricted to a specific stoquastic transverse field Ising model and a particular equilibration task, so generality to other QMC models is not established.
- The reported acceleration is for convergence/equilibration time of an order parameter, not for broader end-to-end application metrics such as time-to-solution for optimization workloads.
- The comparison to quantum annealers remains incomplete because the p-computer still appears slower than the QA processor and the QA scaling advantage cannot be confirmed due to limited data points.
- Data and code are only available upon request rather than through a public repository, which limits reproducibility.
- The study averages over many runs with different random seeds, but does not provide a full reproducibility package for hardware configurations, implementation details, and raw benchmarking artifacts.
- [inferred] No experiments are performed on financial datasets or financial problem instances, limiting direct applicability to financial services use cases.
- [inferred] No comparison is provided against state-of-the-art GPU or highly optimized multi-threaded classical implementations on the same benchmark; GPU discussion is literature-based rather than experimental.
- [inferred] Scalability to production hardware is unproven because claims about integrating up to millions of p-bits and maintaining performance are prospective rather than demonstrated.
- [inferred] Internal validity may be affected by mixing actual hardware measurements, CPU-based projections, and SPICE-based projections within the same performance narrative.
- [inferred] The benchmark uses a narrow set of initial conditions and parameters, so robustness across broader operating regimes is unclear.
## Open questions
- Will the projected speedups for larger lattices hold when those larger instances are implemented on real FPGA or ASIC hardware?
- Can a fabricated clockless analog p-computer achieve the projected additional 2 to 3 orders of magnitude speedup seen in SPICE simulations?
- How well does the proposed architecture generalize beyond the stoquastic TFIM benchmark to other QMC models?
- What performance can be achieved on non-bipartite or more irregular interaction graphs that require more complex coloring or synchronization strategies?
- How does the approach compare empirically with optimized GPU, TPU, or multi-core CPU implementations on the same benchmark?
- Can the gap to quantum annealers be closed further, or is there an inherent advantage from non-local quantum processes?
- What is the true asymptotic scaling of the quantum annealer on this task, given that the paper notes there are not enough data points to be certain?
- How sensitive are the results to the number of Trotter replicas and to approximation error from finite-replica DT-PIMC?
- Can the architecture maintain correctness and low error rates when scaled to much larger numbers of p-bits in physical hardware?
- How robust is clockless autonomous operation to simultaneous updates, device variability, and analog nonidealities in fabricated systems?
- [inferred] Would the reported acceleration persist for practical financial Monte Carlo workloads, such as option pricing or risk simulation, rather than physics-based Ising benchmarks?

**Future work:**
- Fabricate customized mixed-signal ASIC designs using stochastic MTJ-based p-bits to improve over the current FPGA implementation.
- Develop fully analog, clockless p-computer hardware to realize the projected additional speedups beyond digital implementations.
- Investigate applicability of probabilistic computers to quantum problems beyond the transverse field Ising Hamiltonian studied here.
- Scale the architecture to much larger p-bit counts, potentially up to millions of p-bits on chip.
- Explore extensions of the roadmap to other QMC models beyond the specific TFIM benchmark.
- Perform larger direct hardware demonstrations rather than relying on projected results for bigger lattices.
- [inferred] Benchmark against modern GPU and multi-threaded classical baselines using identical workloads and measurement protocols.
- [inferred] Release public code, data, and implementation artifacts to improve reproducibility.
- [inferred] Validate the approach on application-domain workloads, including finance-relevant Monte Carlo problems, to assess practical utility outside condensed-matter benchmarks.
## Key ideas
- #idea:near-term-feasibility — Specialized probabilistic classical hardware (FPGA p-computers and projected analog p-computers) can substantially accelerate Monte Carlo-style simulation workloads in the near term without requiring fault-tolerant quantum hardware.
- #idea:hybrid-approach — The paper frames specialized classical probabilistic hardware as a practical complement or competitor to quantum annealers for sampling and equilibration tasks.
- #contradiction:classical-vs-quantum — The study explicitly states that observed gains come from classical hardware parallelism rather than any quantum speedup or demonstrated quantum advantage.
- #contradiction:scalability — Large-instance and analog performance claims are mostly projected from CPU simulations or SPICE models rather than demonstrated on scaled physical hardware.
## Contradictions
- Contradicts broad claims that quantum hardware is necessarily superior for Ising/QMC-style workloads: this paper shows substantial acceleration using classical probabilistic hardware and explicitly denies any demonstrated quantum advantage.
- Contradicts strong scalability narratives in some quantum-advantage discussions by noting that larger-lattice FPGA results are projections only and that analog p-computer gains are based on SPICE rather than fabricated hardware.
- Relative to the cited quantum annealer comparison in 2018_King_ObservationOfTopologicalPhenomena, the paper suggests specialized classical hardware may narrow the performance gap, but also acknowledges that the annealer still appears faster and that QA scaling cannot be firmly established from limited data.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
