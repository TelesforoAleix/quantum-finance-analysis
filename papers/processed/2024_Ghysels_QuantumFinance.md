---
authors:
- Rachel Berkowitz
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1103/Physics.18.154
evidence_type: ''
idea_tags: []
journal_or_venue: Physics Magazine
methodology_tags: []
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: ''
relevance_phase3: not-yet-assessed
source_type: other
source_type_confidence: high
step1_date: '2026-03-18T20:37:29.694038'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T20:37:45.691810'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T20:46:24.658853'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T20:46:29.497652'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T20:46:34.983145'
step5_model: Mistral-Large-3
step6_date: ''
step6_model: ''
steps_completed:
- 1
- 2
- 3
- 4
- 5
title: Q&A Quantum Computing Meets Finance
topic_tags: []
year: 2025
zotero_key: ''
---

## Abstract summary
This interview-based article explores the intersection of quantum computing and financial services, focusing on how quantum algorithms could address computationally intensive problems like asset pricing and portfolio optimization. The discussion highlights challenges in adapting financial models to quantum hardware and the potential long-term impact of quantum computing on the financial industry, while emphasizing the need for early investment and interdisciplinary expertise.
## Methodology
The paper is an interview-based discussion with Eric Ghysels, a financial econometrician, exploring the potential applications of quantum computing in finance. The methodology is conceptual and theoretical, focusing on translating financial models into quantum algorithms. Ghysels discusses the adaptation of financial problems such as asset pricing, portfolio optimization, and stochastic volatility modeling for quantum computing. The approach involves reformulating financial models (e.g., quadratic unconstrained binary optimization for portfolio allocation, hidden-Markov-chain models for asset-price dynamics) to fit quantum hardware constraints. The discussion highlights the challenges of implementing continuous-time stochastic differential equations on quantum computers and the need for discretization or alternative model families. Theoretical speedups, such as quadratic improvements in credit risk and derivative pricing, are mentioned, but no empirical experimentation or formal proofs are presented.

**Algorithms used:** quantum annealing, quantum linear algebra
## Findings
- [speculative] Quantum linear algebra could potentially speed up solving integral or partial differential equations in financial asset pricing
- [speculative] Quantum information theory provides tools for embedding notions of ambiguity in pricing models
- [speculative] Quantum annealing algorithms can solve combinatorial optimization problems like portfolio allocation more efficiently by exploring large solution spaces in parallel
- [speculative] Hidden-Markov-chain models adapted for quantum hardware could enable quadratic speedups in credit risk and derivative-pricing computations
- [speculative] Quantum computing use cases in financial services could generate up to $622 billion in value by 2035, per a McKinsey & Company report
- [speculative] Industrial-scale quantum computers may be achievable before 2030, according to IBM and Google
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining data at different frequencies in econometrics
- [speculative] Discretization of continuous-time stochastic differential equations for asset-price dynamics is necessary for quantum implementation but results in coarse approximations
- [speculative] Current quantum hardware limitations and a 'quantum algorithm winter' hinder progress in implementing finance-specific quantum algorithms

**Results summary:** The interview with Eric Ghysels explores the potential of quantum computing in financial services, particularly for asset pricing, portfolio optimization, and risk modeling. While theoretical advantages are proposed—such as quantum linear algebra for solving differential equations and quantum annealing for optimization—no empirical results or hardware demonstrations are presented. Challenges include hardware limitations, algorithmic gaps, and the need to adapt financial models to quantum frameworks. The discussion also highlights speculative projections, such as a $622 billion market impact by 2035, and the historical parallel of physics graduates transitioning into finance.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum speedups (e.g., quadratic speedups in credit risk computations) but provides no empirical validation or hardware demonstrations. All claims are based on algorithmic theory or industry projections, not experimental results.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum algorithm development for finance is still in early stages, described as a 'quantum algorithm winter'
- Quantum annealing hardware is limited to problems that fit its specific optimization framework, requiring compromises in problem formulation
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, requiring coarse discretization that may lose model fidelity
- Portfolio allocation problems must be translated into quadratic unconstrained binary optimization, which may not capture all financial constraints
- Quantum solutions produce quantum states that require creative approaches to extract salient properties for asset pricing [inferred]
- Lack of scalable quantum hardware is a major barrier to commercial viability [inferred]
- No empirical validation of quantum speedups in real-world financial applications mentioned [inferred]
- Source is an interview/Q&A format, which may lack technical depth and peer-reviewed rigor [inferred]
- Potential bias toward optimistic industry projections (e.g., McKinsey report) without critical assessment [inferred]
## Open questions
- When will quantum computers achieve commercially viable applications in finance?
- How can financial models be effectively rewritten to be amenable to quantum hardware without losing key properties?
- What are the trade-offs between model fidelity and quantum computability in asset pricing?
- How will quantum computing handle the ambiguity in risk factors for asset pricing?
- What is the realistic timeline for industrial-scale quantum computers in financial services?
- How can quantum algorithms be adapted to handle high-frequency financial data effectively?

**Future work:**
- Develop quantum algorithms specifically tailored for financial applications beyond existing optimization frameworks
- Explore hidden-Markov-chain models for quantum implementations in credit risk and derivative pricing
- Investigate methods to extract meaningful financial insights from quantum states in asset pricing
- Expand financial engineering education to include quantum computing fundamentals
- Conduct empirical studies comparing quantum and classical approaches for financial problems
- Develop hybrid quantum-classical approaches to bridge current hardware limitations
## Key ideas
<!-- Step 6 output — bullet list with idea tags -->

## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
