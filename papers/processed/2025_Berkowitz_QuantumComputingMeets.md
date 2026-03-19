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
- quantum-simulation
- QUBO
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: other
source_type_confidence: high
step1_date: '2026-03-18T22:09:44.639036'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:10:16.574787'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:10:19.347449'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:10:24.359262'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:10:29.276583'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:11:20.312665'
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
- topic/risk-modelling
- topic/derivatives-pricing
- method/quantum-annealing
- method/quantum-simulation
- method/QUBO
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Quantum Computing Meets Finance
topic_tags:
- portfolio-optimisation
- asset-pricing
- risk-modelling
- derivatives-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
This interview-based article explores the intersection of quantum computing and financial services, focusing on how quantum algorithms could address computationally intensive problems like asset pricing and portfolio optimization. The discussion highlights challenges in adapting financial models to quantum hardware, the current limitations of quantum algorithms, and the potential long-term impact on the financial industry.
## Methodology
The paper is an interview-based discussion with Eric Ghysels, a financial econometrician, exploring the potential applications of quantum computing in finance. The methodology is conceptual and theoretical, focusing on translating financial models into quantum algorithms. Ghysels discusses the adaptation of financial problems such as asset pricing, portfolio optimization, and stochastic volatility models for quantum computing. The approach involves rewriting financial models (e.g., quadratic unconstrained binary optimization for portfolio allocation and hidden-Markov-chain models for asset-price dynamics) to fit quantum hardware constraints. The discussion highlights the challenges of implementing continuous-time stochastic differential equations on quantum computers and the need for discretization or alternative model families. Theoretical speedups, such as quadratic improvements in credit risk and derivative pricing, are mentioned, but no empirical experiments or formal proofs are detailed.

**Algorithms used:** Quantum Annealing, Hidden-Markov-Chain Models
## Findings
- [speculative] Quantum linear algebra could potentially speed up solving integral or partial differential equations in financial asset pricing
- [speculative] Quantum information theory provides tools for embedding notions of ambiguity in pricing models
- [speculative] Quantum annealing algorithms can solve combinatorial optimization problems like portfolio allocation more efficiently by exploring large solution spaces in parallel
- [speculative] Hidden-Markov-chain models adapted for quantum hardware could enable quadratic speedups in credit risk and derivative-pricing computations
- [speculative] Quantum computing use cases in financial services could generate up to $622 billion in value by 2035, per a McKinsey & Company report
- [speculative] Industrial-scale quantum computers may be achievable before 2030, according to IBM and Google
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining financial data at different frequencies
- [speculative] Current quantum hardware limitations require finance problems to be reformulated (e.g., discretization of stochastic differential equations) to fit quantum algorithms
- [speculative] Physics students with both quantum computing and financial sector knowledge may find career opportunities in financial engineering

**Results summary:** The interview highlights the potential of quantum computing to address computationally intensive financial problems such as asset pricing, portfolio optimization, and risk modeling. While theoretical advantages—such as quadratic speedups in derivative pricing and parallel exploration of solution spaces—are proposed, the discussion emphasizes the current limitations of quantum hardware and the need for algorithmic advancements. The translation of financial models into quantum-compatible frameworks (e.g., quadratic unconstrained binary optimization or hidden-Markov-chain models) is identified as a key challenge. Industry projections suggest significant economic impact by 2035, though these remain speculative without empirical validation.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum speedups (e.g., quadratic speedups in credit risk computations) but does not provide empirical evidence or real-hardware demonstrations. Claims are based on algorithmic adaptations rather than proven performance advantages.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum algorithm development for finance is still in early stages, described as a 'quantum algorithm winter'
- Quantum annealing hardware is limited to problems that fit its specific optimization framework, requiring compromises in problem formulation
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, requiring coarse discretization that may lose model fidelity
- Portfolio allocation problems must be translated into quadratic unconstrained binary optimization, which may not capture all financial constraints
- Quantum solutions produce quantum states, requiring creative approaches to extract salient properties of numerical solutions for asset pricing
- No empirical validation of quantum speedups in real-world financial applications mentioned [inferred]
- Lack of scalable quantum hardware limits commercial viability of quantum computing in finance [inferred]
- Potential vendor bias in industry reports (e.g., McKinsey & Company) regarding quantum computing's financial impact [inferred]
- No discussion of noise mitigation techniques for current quantum hardware [inferred]
## Open questions
- When will quantum computers have commercially viable applications in finance?
- How can financial models be effectively rewritten to be amenable to quantum hardware without losing key properties?
- What is the actual quantum speedup achievable for financial problems like credit risk and derivative pricing?
- How will quantum computing handle the ambiguity in risk factors for asset pricing?
- What are the specific limitations of quantum annealing for financial optimization problems?
- How can continuous-time stochastic models be effectively discretized for quantum implementation without significant loss of accuracy?

**Future work:**
- Develop quantum algorithms specifically tailored for financial applications beyond current optimization frameworks
- Explore hidden-Markov-chain models for quantum implementation in asset pricing and credit risk
- Investigate methods to extract meaningful financial insights from quantum states produced by quantum algorithms
- Expand financial engineering education to include quantum computing fundamentals
- Conduct empirical studies comparing quantum and classical approaches for financial problems
- Develop hybrid quantum-classical approaches to bridge the gap between current capabilities and financial requirements
## Key ideas
- #idea:quantum-advantage — Theoretical quadratic speedups in credit risk and derivative pricing via quantum adaptations of hidden-Markov-chain models
- #idea:near-term-feasibility — Quantum annealing may offer near-term potential for portfolio optimization despite hardware limitations
- #idea:hybrid-approach — Financial models require reformulation (e.g., discretization of stochastic differential equations) to fit quantum hardware constraints, suggesting hybrid quantum-classical approaches
- #limitation:qubit-count — Current quantum hardware lacks the capacity to implement pioneering quantum algorithms from the 1990s for financial applications
- #limitation:noise — No discussion of noise mitigation techniques, implying hardware noise remains a barrier to practical implementation
- #limitation:data-encoding — Challenges in translating continuous-time financial models into quantum-compatible frameworks without losing fidelity
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
