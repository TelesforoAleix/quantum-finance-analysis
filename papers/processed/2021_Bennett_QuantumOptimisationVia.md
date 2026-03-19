---
aliases:
- Quantum optimisation via maximally ampliﬁed states
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
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T23:12:15.210487'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:12:17.847211'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:12:24.992809'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:12:33.726360'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:12:41.710457'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:12:46.204474'
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
- topic/high-frequency-trading
- method/grover
- method/QAOA
- method/quantum-walk
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Quantum optimisation via maximally ampliﬁed states
topic_tags:
- portfolio-optimisation
- high-frequency-trading
year: 2022
zotero_key: ''
---

## Abstract summary
This paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a novel quantum algorithm tailored for combinatorial optimisation under near-term quantum computing constraints. The MAOA aims to maximise the amplification of optimal solutions within limited circuit depths, avoiding the computationally intensive variational procedures of existing methods like QAOA. The authors also propose a restricted circuit depth variant of Grover adaptive search (RGAS) for comparison and demonstrate both algorithms' performance on financial and logistical optimisation problems, highlighting their efficiency gains over classical approaches.
## Methodology
The paper introduces the Maximum Amplification Optimisation Algorithm (MAOA), a novel quantum algorithm for combinatorial optimisation in near-term quantum computing with restricted circuit depth. The MAOA focuses on producing a quantum state where optimal solutions are maximally amplified, avoiding the computationally expensive variational procedure used in algorithms like QAOA. The methodology involves transforming the quality distribution of solutions into a binary marking function applied to a complete graph, enabling maximum amplification of optimal solutions. The paper also introduces a restricted Grover adaptive search (RGAS) as a baseline comparison. The MAOA and RGAS are simulated on three problems: a vehicle routing problem, a portfolio optimisation problem, and an arbitrarily large problem with normally distributed solution qualities. The performance is evaluated by comparing the speedup over classical random sampling and numerical convergence to a theoretically derived upper bound for amplification.

**Algorithms used:** MAOA, RGAS, QAOA, QWOA, Grover's search

**Experimental setup:** Numerical simulations were conducted to evaluate the MAOA and RGAS algorithms. The simulations involved solving combinatorial optimisation problems on a classical computer, modeling the behavior of quantum circuits with restricted depth. The complete graph structure and binary marking function were used to derive optimal parameters for amplitude amplification. The Nelder-Mead optimisation procedure was employed to fine-tune parameters for comparison.

**Dataset:** The paper uses three datasets/problems: (1) a practical vehicle routing problem, (2) a computationally demanding portfolio optimisation problem, and (3) an arbitrarily large problem with normally distributed solution qualities.
## Findings
- [supported] The Maximum Ampliﬁcation Optimisation Algorithm (MAOA) demonstrates substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimisation, and normally distributed solution quality problems, as shown through numerical simulations.
- [supported] MAOA outperforms the Restricted Grover Adaptive Search (RGAS) and Quantum Approximate Optimisation Algorithm (QAOA) in amplifying optimal solutions under restricted circuit depth conditions.
- [supported] MAOA achieves maximum amplification of optimal solutions by using a binary marking function on a complete graph, with derived optimal parameters (γ = π and t = π/N) applied repeatedly, avoiding the computationally expensive variational procedure of QAOA/QWOA.
- [supported] The amplification of optimal solutions in MAOA is quantified by numerical convergence to a theoretically derived upper bound, with a maximum amplification factor of (2r + 1)^2 for r iterations in the low-convergence regime.
- [speculative] MAOA may provide quantum advantage for combinatorial optimisation problems in near-term quantum devices by leveraging restricted circuit depths more effectively than existing algorithms like QAOA.
- [speculative] The binary marking function and complete graph structure in MAOA could enable analytically derived optimal parameters that are insensitive to solution placement or ordering, potentially simplifying implementation on quantum hardware.
- [disputed] The paper claims that optimising for expectation value of quality (as in QAOA) does not maximise amplification of optimal solutions, which contradicts some prior literature on QAOA’s effectiveness for certain problem classes.

**Results summary:** The paper introduces the Maximum Ampliﬁcation Optimisation Algorithm (MAOA), a novel quantum algorithm for combinatorial optimisation under restricted circuit depths. Through simulations, MAOA is shown to outperform classical random sampling, RGAS, and QAOA by maximising the amplification of optimal solutions. The algorithm leverages a binary marking function on a complete graph with derived optimal parameters, avoiding the computationally expensive variational procedure of QAOA. Numerical results demonstrate convergence to a theoretical upper bound, with MAOA achieving a speedup in finding optimal solutions for vehicle routing, portfolio optimisation, and normally distributed solution quality problems. The connection to Grover’s search is established, though the paper notes that MAOA operates in a low-convergence regime to accommodate near-term hardware limitations.

**Performance claims:**
- MAOA provides substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimisation, and normally distributed solution quality problems.
- MAOA consistently outperforms RGAS in all tested cases.
- Maximum amplification of marked solutions in MAOA reaches (2r + 1)^2 for r iterations in the low-convergence regime.
- Optimal parameters for MAOA (γ = π and t = π/N) produce near-maximal amplification up to r = 15 iterations, outperforming optimised parameters in higher-dimensional landscapes.
## Quantum advantage claim
**Classification:** speculative

The claimed quantum advantage of MAOA is based on simulation results and theoretical arguments, but it is not demonstrated on real quantum hardware. The advantage is framed as a potential improvement over classical methods and existing quantum algorithms (e.g., QAOA) for near-term devices, but empirical validation on physical quantum computers is lacking.
## Limitations
- The MAOA and RGAS algorithms are only simulated, not tested on real quantum hardware, limiting empirical validation of performance under noise and decoherence [inferred]
- The paper focuses on near-term quantum computing with restricted circuit depth, which inherently limits the maximum possible amplification of optimal solutions
- The variational procedure in QAOA/QWOA is computationally expensive, but the MAOA avoids this; however, the MAOA's reliance on a binary marking function may not be universally applicable to all combinatorial optimization problems [inferred]
- The study uses synthetic or simplified problem instances (vehicle routing, portfolio optimization, and normally distributed solution qualities), which may not fully represent real-world financial services problems [inferred]
- The derived optimal parameters (γ = π and t = π/N) are shown to work well for small marked-vertex ratios, but their performance may degrade for larger or more complex solution spaces [inferred]
- The paper does not compare MAOA's performance with state-of-the-art classical optimization algorithms, making it difficult to assess practical quantum advantage [inferred]
- The preprint status indicates a lack of peer review, which may affect the robustness of the claims and methodology [inferred]
- The analysis assumes a complete graph structure for quantum walks, which may not be the most efficient or feasible for all problem types [inferred]
- The paper does not address the impact of hardware noise, qubit connectivity constraints, or error mitigation techniques on the MAOA's performance [inferred]
- The numerical simulations are limited to specific problem sizes and do not explore scalability to larger, more realistic problem instances [inferred]
## Open questions
- How does the MAOA perform on real quantum hardware with noise and decoherence?
- What is the impact of qubit connectivity constraints on the implementation of the complete graph structure assumed in the MAOA?
- Can the MAOA be extended or adapted to handle combinatorial optimization problems with non-binary or multi-objective quality distributions?
- How does the MAOA compare to state-of-the-art classical optimization algorithms in terms of solution quality and runtime for large-scale problems?
- What are the trade-offs between circuit depth, solution quality, and computational overhead in the MAOA for practical applications?
- How sensitive is the MAOA to variations in the marked-vertex ratio, and what are the implications for problems with unknown or dynamic solution spaces?
- Can the MAOA be integrated with error mitigation techniques to improve performance on noisy intermediate-scale quantum (NISQ) devices?

**Future work:**
- Test the MAOA on real quantum hardware to validate its performance under noise and decoherence
- Compare the MAOA with state-of-the-art classical optimization algorithms to assess practical quantum advantage
- Extend the MAOA to handle non-binary or multi-objective quality distributions for broader applicability
- Explore the scalability of the MAOA to larger problem instances and its performance on more complex real-world datasets
- Investigate the impact of qubit connectivity constraints and develop strategies to adapt the MAOA to hardware limitations
- Integrate error mitigation techniques into the MAOA to improve its robustness on NISQ devices
- Apply the MAOA to additional combinatorial optimization problems in financial services, such as risk management or fraud detection
- Develop hybrid quantum-classical approaches that combine the MAOA with classical optimization methods for improved performance
## Key ideas
- #idea:quantum-advantage — MAOA demonstrates substantial speedup over classical random sampling and outperforms QAOA/RGAS in amplifying optimal solutions for portfolio optimisation under restricted circuit depth
- #idea:near-term-feasibility — MAOA is designed for near-term quantum devices, avoiding computationally expensive variational procedures and leveraging restricted circuit depths
- #idea:hybrid-approach — MAOA uses a binary marking function on a complete graph with analytically derived optimal parameters, potentially simplifying hybrid quantum-classical implementations
- #limitation:simulation-only — MAOA's performance is only validated via classical simulations, not real quantum hardware
- #limitation:noise — The paper does not address hardware noise, qubit connectivity constraints, or error mitigation, which may impact MAOA's real-world applicability
- #limitation:data-encoding — MAOA's reliance on a binary marking function may limit its applicability to problems with non-binary or multi-objective quality distributions
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims that optimising for expectation value of quality (as in QAOA) does not maximise amplification of optimal solutions, contradicting prior literature on QAOA’s effectiveness for certain problem classes (e.g., portfolio optimisation)
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
