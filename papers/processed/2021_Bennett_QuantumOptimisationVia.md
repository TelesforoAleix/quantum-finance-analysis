---
aliases:
- Quantum optimisation via maximally amplified states
- Quantum optimisation via maximally
authors:
- T. Bennett
- J. B. Wang
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
doi: 10.48550/arXiv.2111.00796
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- grover
- QAOA
- quantum-walk
- variational
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- Golden_2021_GroverMixerQAOA
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T11:59:42.503493'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:00:37.615579'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:00:54.392986'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:01:14.728098'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:01:41.308596'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:02:50.886417'
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
- method/grover
- method/QAOA
- method/quantum-walk
- method/variational
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Quantum optimisation via maximally amplified states
topic_tags:
- portfolio-optimisation
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a quantum algorithm designed for combinatorial optimisation problems under near-term quantum computing constraints. The MAOA maximises the amplification of optimal solutions within restricted circuit depths, outperforming existing near-term algorithms like QAOA by avoiding computationally expensive variational procedures. The study also presents a restricted Grover adaptive search (RGAS) for comparison and demonstrates the MAOA's superior performance on practical problems such as vehicle routing and portfolio optimisation.
## Methodology
The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a novel quantum algorithm for combinatorial optimisation problems in near-term quantum computing contexts with restricted circuit depth. The MAOA focuses on maximising the amplification of optimal solutions by leveraging a binary marking function on a complete graph, avoiding the computationally expensive variational procedures of algorithms like QAOA. The methodology involves transforming the quality distribution of solutions into a binary form (marked vs. unmarked) and applying repeated Grover-like rotations to amplify the marked (optimal) solutions. The algorithm is benchmarked against a restricted circuit depth version of the Grover Adaptive Search (RGAS) and classical random sampling. The study employs numerical simulations to evaluate performance on three problems: a vehicle routing problem, a portfolio optimisation problem, and an arbitrarily large problem with normally distributed solution qualities. The MAOA's performance is quantified by comparing its speedup in finding optimal solutions against theoretical upper bounds and baseline methods.

**Algorithms used:** MAOA, QAOA, QWOA, Grover Adaptive Search (GAS), Restricted Grover Adaptive Search (RGAS), Grover's Search

**Experimental setup:** The experiments are conducted via numerical simulations on classical computers, emulating quantum behavior. The simulations assess the MAOA and RGAS on three distinct problems: (1) a vehicle routing problem, (2) a portfolio optimisation problem, and (3) an arbitrarily large problem with normally distributed solution qualities. The simulations focus on restricted circuit depths, reflecting near-term quantum computing constraints. The MAOA's performance is evaluated by measuring the amplification of optimal solutions and comparing it to classical random sampling and RGAS.

**Dataset:** The paper uses three types of datasets/problems: (1) a practical vehicle routing problem, (2) a computationally demanding portfolio optimisation problem, and (3) an arbitrarily large problem with solution qualities following a normal distribution. Specific datasets (e.g., historical financial data) are not explicitly named, but the problems are representative of combinatorial optimisation challenges in financial services and logistics.
## Findings
- [supported] The Maximum Amplification Optimisation Algorithm (MAOA) demonstrates substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimization, and normally distributed solution quality problems, as shown through numerical simulations.
- [supported] MAOA outperforms the Quantum Approximate Optimisation Algorithm (QAOA) and the Restricted Grover Adaptive Search (RGAS) by amplifying optimal solutions more effectively without requiring computationally expensive variational procedures.
- [supported] MAOA achieves maximum amplification of optimal solutions by using a binary marking function on a complete graph and applying derived optimal parameters (γ = π and t = π/N) repeatedly, avoiding the variational procedure of QAOA/QWOA.
- [supported] The amplification of optimal solutions in MAOA is quantified by a theoretically derived upper bound, with numerical convergence demonstrated in simulations.
- [supported] For a given circuit depth (r iterations), MAOA produces a maximally amplified state where optimal solutions are amplified by a factor of (2r + 1)^2, as validated by simulations on a complete graph with 10^8 vertices.
- [supported] The threshold response curve analysis shows that MAOA reliably navigates to a quality threshold within the low-convergence regime, ensuring maximum amplification of optimal solutions for restricted circuit depths.
- [supported] MAOA's performance is independent of the exact shape of the solution quality distribution, making it robust for large-scale combinatorial optimization problems where distribution tails are uncertain.
- [speculative] The authors suggest that MAOA could be more effective than QAOA for near-term quantum devices due to its avoidance of computationally expensive variational procedures and superior amplification of optimal solutions.
- [disputed] The claim that optimizing for expectation value of quality (as in QAOA) does not maximize amplification of optimal solutions contradicts some prior work, such as Golden et al. [35], which proposes a Grover mixer with binary marking but focuses on expectation value.
- [supported] The Grover Adaptive Search (GAS) is used as a benchmark, but its requirement for large rotation counts (O(√N)) makes it impractical for near-term quantum devices, whereas MAOA is designed for restricted circuit depths.

**Results summary:** The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a quantum algorithm for combinatorial optimization in near-term quantum computing. Through simulations, MAOA is shown to outperform classical random sampling and other near-term quantum algorithms like QAOA and RGAS by amplifying optimal solutions more effectively. The algorithm leverages a binary marking function on a complete graph and derived optimal parameters to achieve maximum amplification without variational procedures. Numerical results demonstrate convergence to a theoretical upper bound for amplification, with MAOA providing substantial speedups in vehicle routing, portfolio optimization, and normally distributed solution quality problems. The paper also highlights the limitations of optimizing for expectation value of quality, as done in QAOA, and argues that MAOA's focus on amplifying optimal solutions is more effective for finding near-optimal solutions in large problem spaces.

**Performance claims:**
- MAOA provides substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimization, and normally distributed solution quality problems.
- MAOA amplifies optimal solutions by a factor of (2r + 1)^2 for r iterations, as demonstrated in simulations on a complete graph with 10^8 vertices.
- MAOA consistently outperforms RGAS and QAOA in simulations across multiple problem types.
- The probability of measuring marked (optimal) solutions in MAOA's maximally amplified state is approximately 1/40 or less, depending on the marked-solution ratio.
## Quantum advantage claim
**Classification:** theoretical

The quantum advantage claimed by MAOA is theoretical, based on simulations showing superior amplification of optimal solutions compared to classical random sampling and other near-term quantum algorithms. The advantage is quantified by a speedup factor derived from the amplification of optimal solutions, but results are from simulations only, not real hardware. The paper argues that MAOA avoids the computational expense of variational procedures, making it more suitable for near-term quantum devices, but empirical validation on real hardware is lacking.
## Limitations
- Hardware noise and decoherence limit the effective circuit depth, restricting the number of iterations (r) that can be reliably executed on near-term quantum devices [inferred]
- The algorithm assumes a binary marking function, which may not be optimal for all types of quality distributions in real-world financial problems [inferred]
- Simulations are conducted on classical computers, not real quantum hardware, which may not fully capture hardware-specific noise and errors [inferred]
- The study is limited to synthetic or precomputed quality distributions (e.g., vehicle routing, portfolio optimization), and performance on real-world financial datasets is not validated
- The MAOA relies on the complete graph structure for maximum amplification, which may not be efficiently implementable on all quantum hardware architectures [inferred]
- The computational effort metric (number of calls to the quality function) does not account for the overhead of quantum walk/mixing operations, which could impact scalability [inferred]
- The algorithm's performance is demonstrated only for small to moderately sized problems (e.g., N = 10^8), and scalability to larger problem sizes (e.g., N > 10^12) is not explored
- The threshold-finding process assumes a well-behaved quality distribution (e.g., normal-like), and performance may degrade for irregular or multimodal distributions [inferred]
- The study does not compare MAOA with state-of-the-art classical optimization algorithms (e.g., simulated annealing, genetic algorithms) for the tested problems
- The RGAS and MAOA are restricted to the same circuit depth, but the RGAS's randomized rotation count may not fully utilize the available amplification potential [inferred]
- The paper does not address the impact of qubit count constraints on the practical implementation of the algorithm for large-scale financial problems [inferred]
- The low-convergence regime assumption (P(r, ρ(T)) < 1/40) may not hold for all problem instances, particularly those with highly skewed quality distributions [inferred]
## Open questions
- How does the MAOA perform on real quantum hardware with noise and decoherence, compared to classical simulations?
- What is the impact of irregular or non-normal quality distributions on the threshold-finding process and overall algorithm performance?
- Can the MAOA be adapted to work with non-complete graph structures while maintaining high amplification of optimal solutions?
- How does the computational overhead of quantum walk/mixing operations affect the overall speedup relative to classical methods?
- What is the minimum qubit count required to achieve a practical advantage for real-world financial problems (e.g., portfolio optimization with >100 assets)?
- How does the MAOA compare to hybrid quantum-classical algorithms (e.g., QAOA with classical post-processing) in terms of solution quality and computational effort?
- Can the threshold-finding process be optimized further to reduce the number of state preparations/measurements required?
- What are the implications of using a binary marking function for problems where solution quality is not easily dichotomized (e.g., multi-objective optimization)?
- How does the algorithm perform when the optimal solution is not unique or when there are multiple near-optimal solutions with similar qualities?
- What is the sensitivity of the MAOA to errors in the quality function or the marking process?

**Future work:**
- Test the MAOA on real quantum hardware (e.g., IBM Quantum, Rigetti) to validate performance under noise and decoherence
- Extend the algorithm to handle non-normal or irregular quality distributions, potentially by incorporating adaptive thresholding techniques
- Explore alternative graph structures (e.g., hypercubes, expander graphs) to reduce qubit requirements while maintaining amplification efficiency
- Compare the MAOA with state-of-the-art classical optimization algorithms (e.g., simulated annealing, genetic algorithms) for large-scale financial problems
- Develop hybrid quantum-classical approaches that combine the MAOA with classical post-processing to improve solution quality
- Investigate the use of noise mitigation techniques (e.g., error correction, dynamical decoupling) to extend the effective circuit depth of the MAOA
- Apply the MAOA to real-world financial datasets (e.g., historical market data for portfolio optimization) to assess practical performance
- Explore the use of the MAOA for multi-period or dynamic optimization problems in finance (e.g., dynamic portfolio rebalancing)
- Develop methods to reduce the computational overhead of quantum walk/mixing operations, potentially by leveraging classical pre-processing
- Investigate the scalability of the MAOA to problem sizes beyond N = 10^8, including the impact of qubit count constraints on performance
## Key ideas
- #idea:quantum-advantage — MAOA demonstrates substantial speedup over classical random sampling and outperforms QAOA/RGAS in amplifying optimal solutions for portfolio optimisation under restricted circuit depth
- #idea:near-term-feasibility — MAOA is designed for near-term quantum devices, avoiding computationally expensive variational procedures and leveraging restricted circuit depths
- #idea:hybrid-approach — MAOA uses a binary marking function on a complete graph with analytically derived optimal parameters, potentially simplifying hybrid quantum-classical implementations
- #limitation:simulation-only — MAOA's performance is only validated via classical simulations, not real quantum hardware
- #limitation:noise — The paper does not address hardware noise, qubit connectivity constraints, or error mitigation, which may impact MAOA's real-world applicability
- #limitation:data-encoding — MAOA's reliance on a binary marking function may limit its applicability to problems with non-binary or multi-objective quality distributions
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims that optimising for expectation value of quality (as in QAOA) does not maximise amplification of optimal solutions, contradicting prior work (e.g., Golden et al. [35]) that supports QAOA’s effectiveness for portfolio optimisation
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
