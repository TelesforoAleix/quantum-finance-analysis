---
aliases:
- Quantum Computing Meets Finance
- Quantum Computing Meets Finance
authors:
- Rachel Berkowitz
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/Physics.18.154
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physics Magazine
methodology_tags:
- quantum-annealing
- QUBO
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: other
source_type_confidence: high
step1_date: '2026-03-19T13:08:35.463261'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:08:38.113690'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:08:42.375998'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:09:12.572376'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T13:09:22.641723'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:10:17.336030'
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
- topic/asset-pricing
- topic/derivatives-pricing
- topic/risk-modelling
- topic/credit-scoring
- method/quantum-annealing
- method/QUBO
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Computing Meets Finance
topic_tags:
- portfolio-optimisation
- asset-pricing
- derivatives-pricing
- risk-modelling
- credit-scoring
year: 2025
zotero_key: ''
---

## Abstract summary
This interview-based article explores the intersection of quantum computing and financial services, focusing on how quantum algorithms could address computationally intensive problems like asset pricing and portfolio optimization. The discussion highlights challenges in adapting financial models to quantum hardware, the current limitations of quantum algorithms, and the potential long-term impact on the financial industry.
## Methodology
The paper is an interview-based discussion with economist Eric Ghysels on the intersection of quantum computing and financial services. It explores conceptual and theoretical approaches to adapting financial models for quantum algorithms, particularly focusing on asset pricing, portfolio optimization, and stochastic processes. Ghysels discusses the translation of financial problems into quantum-compatible frameworks, such as quadratic unconstrained binary optimization (QUBO) for portfolio allocation and hidden-Markov-chain models for asset-price dynamics. The discussion highlights challenges in discretizing continuous-time stochastic differential equations and leveraging quantum linear algebra for solving integral or partial differential equations in finance. The paper does not present empirical results or formal proofs but rather outlines potential methodologies and theoretical adaptations for quantum computing in finance.

**Algorithms used:** Quantum Annealing, Hidden-Markov-Chain Models
## Findings
- [speculative] Quantum linear algebra could potentially speed up solving integral or partial differential equations in financial asset pricing
- [speculative] Quantum information theory provides tools for embedding notions of ambiguity in pricing models
- [speculative] Quantum annealing algorithms can solve combinatorial optimization problems like portfolio allocation more efficiently by exploring large solution spaces in parallel
- [speculative] Hidden-Markov-chain models adapted for quantum hardware could enable quadratic speedups in credit risk and derivative-pricing computations
- [speculative] Quantum computing use cases in financial services could generate up to $622 billion in value by 2035, per a McKinsey & Company report
- [speculative] Industrial-scale quantum computers may be achievable before 2030, according to public statements by IBM and Google
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining data at different frequencies in econometrics
- [speculative] Discretization of continuous-time stochastic differential equations for asset-price dynamics on quantum computers results in coarse approximations requiring model rethinking
- [speculative] Physics students with knowledge of both quantum computing and finance may find career opportunities in financial engineering, analogous to the 1970s-80s hiring trend for PDE-solving physicists

**Results summary:** The interview with Eric Ghysels explores the potential of quantum computing in financial services, particularly for asset pricing, portfolio optimization, and risk modeling. While theoretical advantages are proposed—such as quantum linear algebra for solving differential equations and quadratic speedups in derivative pricing—these remain speculative due to hardware limitations and algorithmic challenges. Ghysels highlights the need to adapt financial models (e.g., hidden-Markov-chain models) for quantum hardware and notes the current reliance on quantum annealing for optimization tasks. Industry projections (e.g., McKinsey's $622B valuation by 2035) and hardware timelines (e.g., IBM/Google's 2030 targets) are cited but not empirically validated. The discussion also draws parallels to historical trends in financial engineering, suggesting future demand for interdisciplinary expertise.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum speedups (e.g., quadratic speedups in derivative pricing) and efficiency gains in optimization, but no empirical demonstrations or real-hardware results are provided. All claims are based on algorithmic theory or industry projections, not validated performance metrics.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum algorithm development for finance is still in early stages, described as a 'quantum algorithm winter'
- Quantum annealing hardware is limited to problems that fit its specific optimization framework, requiring compromises in problem formulation
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, requiring coarse discretization that may lose model fidelity
- Asset-pricing models require translation into quantum-amenable families (e.g., hidden-Markov-chain models), which may not capture all financial dynamics
- Quantum solutions produce quantum states, requiring creative methods to extract salient numerical properties for financial applications
- Portfolio optimization problems must be reformulated as quadratic unconstrained binary optimization, which may not fully represent real-world constraints
- [inferred] Lack of empirical validation for quantum speedups in financial applications, as most work remains theoretical or simulation-based
- [inferred] No discussion of noise mitigation techniques or error correction, which are critical for real-world quantum hardware deployment
- [inferred] Potential bias in industry projections (e.g., McKinsey & Company's $622 billion valuation by 2035) due to lack of peer review or independent validation
## Open questions
- When will quantum computers achieve commercially viable applications in finance?
- How can financial models be effectively translated into quantum-amenable formulations without losing key properties (e.g., stochastic volatility)?
- What are the trade-offs between problem fidelity and quantum hardware constraints in financial applications?
- How will quantum computing impact the accuracy and efficiency of asset-pricing models compared to classical methods?
- What are the specific financial problems where quantum computing can provide a clear advantage over classical approaches?
- How can quantum states be effectively measured to extract meaningful financial insights?

**Future work:**
- Develop quantum algorithms tailored for financial applications, particularly for asset pricing and portfolio optimization
- Explore hybrid quantum-classical approaches to bridge the gap between current hardware capabilities and financial modeling needs
- Investigate the use of hidden-Markov-chain models and other quantum-amenable frameworks for financial dynamics
- Expand research into quantum linear algebra for solving integral and partial differential equations in finance
- Integrate quantum information theory tools to better handle ambiguity in financial risk modeling
- Establish financial-engineering programs that combine quantum computing and finance education
- Validate quantum speedups in financial applications through empirical testing on real quantum hardware
## Key ideas
- #idea:quantum-advantage — Theoretical quadratic speedups in credit risk and derivative pricing via quantum adaptations of hidden-Markov-chain models
- #idea:near-term-feasibility — Quantum annealing may offer near-term potential for portfolio optimization despite hardware limitations
- #idea:hybrid-approach — Financial models require reformulation (e.g., discretization of stochastic differential equations) to fit quantum hardware constraints, suggesting hybrid quantum-classical approaches
- #limitation:qubit-count — Current quantum hardware lacks the capacity to implement pioneering quantum algorithms from the 1990s for financial applications
- #limitation:data-encoding — Challenges in translating continuous-time financial models into quantum-compatible frameworks without losing fidelity
- #limitation:no-empirical-validation — Speculative claims about quantum advantage in finance lack empirical validation or real-hardware demonstrations
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
