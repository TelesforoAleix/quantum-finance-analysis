---
aliases:
- Quantum Computing Meets Finance
- Quantum Computing Meets Finance
authors:
- Rachel Berkowitz
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
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
step1_date: '2026-03-19T23:54:43.683284'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:54:44.982190'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:54:46.737703'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:54:51.403271'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:55:39.746252'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:55:43.878963'
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
- topic/credit-scoring
- method/quantum-annealing
- method/QUBO
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
title: Quantum Computing Meets Finance
topic_tags:
- portfolio-optimisation
- asset-pricing
- risk-modelling
- derivatives-pricing
- credit-scoring
year: 2025
zotero_key: ''
---

## Abstract summary
This interview-based article explores the intersection of quantum computing and financial services, focusing on how quantum algorithms could address computationally intensive problems like asset pricing and portfolio optimization. The discussion highlights challenges in adapting financial models to quantum hardware and the potential long-term impact of quantum computing on the financial industry, while emphasizing the need for early investment and interdisciplinary expertise.
## Methodology
The paper is an interview-based Q&A with economist Eric Ghysels discussing the potential applications of quantum computing in financial services, particularly in asset pricing, portfolio optimization, and computationally intensive financial problems. The discussion highlights theoretical and conceptual approaches to adapting financial models for quantum algorithms, including the translation of portfolio allocation problems into quadratic unconstrained binary optimization (QUBO) and the use of quantum annealing for combinatorial optimization. The interview also explores the challenges of implementing stochastic volatility models on quantum hardware and proposes alternative approaches such as hidden-Markov-chain models for capturing dynamic patterns in asset pricing. The focus is on theoretical adaptations rather than empirical experimentation or algorithmic implementation details.

**Algorithms used:** Quantum Annealing
## Findings
- [speculative] Quantum linear algebra could potentially speed up solving integral or partial differential equations in financial asset pricing
- [speculative] Quantum information theory provides tools for embedding notions of ambiguity in pricing models
- [speculative] Quantum annealing algorithms can solve combinatorial optimization problems like portfolio allocation more efficiently by exploring large solution spaces in parallel
- [speculative] Hidden-Markov-chain models adapted for quantum hardware could enable quadratic speedups in credit risk and derivative-pricing computations
- [speculative] Quantum computing use cases in financial services could generate up to $622 billion in value by 2035, per a McKinsey & Company report
- [speculative] IBM and Google are aiming for industrial-scale quantum computers before 2030
- [supported] Quantum annealing hardware is currently the most reliable scaled hardware for optimization tasks in finance
- [disputed] The paper notes a 'quantum algorithm winter,' suggesting progress on quantum algorithms has stalled, which may contradict optimistic industry projections

**Results summary:** The interview with Eric Ghysels explores the potential of quantum computing in financial services, particularly for asset pricing, portfolio optimization, and risk modeling. While quantum linear algebra and quantum annealing are identified as promising approaches, the discussion highlights significant challenges, including hardware limitations, algorithmic gaps, and the need to adapt financial models for quantum computation. Ghysels suggests that quadratic speedups may be achievable in specific applications like credit risk and derivative pricing but emphasizes that current implementations require compromises. The paper also cites industry projections for quantum computing's financial impact, though these remain speculative.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum speedups (e.g., quadratic speedups in credit risk and derivative pricing) and efficiency gains in optimization, but no empirical demonstration or real-hardware validation is provided. Claims are based on algorithmic theory and industry projections rather than concrete results.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum annealing hardware is limited to problems that fit quadratic unconstrained binary optimization (QUBO), requiring compromises in problem formulation
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, necessitating coarse discretizations that may not capture realistic asset-price dynamics
- Translation of financial problems into quantum-compatible models (e.g., hidden-Markov-chain models) may oversimplify or distort the original problem [inferred]
- Quantum linear algebra solutions are quantum states, requiring creative methods to extract salient properties of numerical solutions for asset-pricing models
- Lack of scalable quantum hardware is a major barrier to commercial viability in financial services [inferred]
- The field is experiencing a 'quantum algorithm winter,' indicating slow progress in developing new algorithms for finance [inferred]
- No empirical validation or real-world testing of quantum algorithms in financial services is mentioned, limiting confidence in practical performance [inferred]
- Potential vendor bias in industry reports (e.g., McKinsey & Company) regarding quantum computing's financial impact [inferred]
- The interview format limits depth of technical discussion, potentially omitting key constraints or challenges [inferred]
## Open questions
- When will quantum computers achieve commercially viable applications in finance?
- How can quantum algorithms be adapted to handle time-varying volatility in asset-pricing models without significant loss of accuracy?
- What are the trade-offs between problem fidelity and quantum hardware constraints in portfolio optimization?
- How will quantum computing impact the accuracy and speed of credit risk and derivative-pricing computations in real-world scenarios?
- What are the long-term implications of discretizing continuous-time financial models for quantum implementation?
- How can quantum information theory better address ambiguity in risk factors for asset pricing?

**Future work:**
- Develop quantum algorithms that can handle stochastic volatility models without excessive discretization
- Explore hybrid quantum-classical approaches to bridge the gap between theoretical quantum speedups and practical financial applications
- Investigate the use of hidden-Markov-chain models for quantum implementation in derivative pricing and credit risk
- Expand financial-engineering programs to include quantum computing fundamentals alongside traditional finance education
- Conduct empirical studies to validate quantum algorithms on real financial datasets and hardware
- Collaborate with industry to identify finance problems that naturally fit quantum annealing or other quantum optimization frameworks
## Key ideas
- #idea:quantum-advantage — Quantum linear algebra and quantum annealing could theoretically speed up asset pricing and portfolio optimization by exploring large solution spaces in parallel
- #idea:near-term-feasibility — Speculative projections suggest quantum computing could generate significant value in financial services by 2035, but current hardware limitations hinder practical implementation
- #idea:hybrid-approach — Discretization and reformulation of financial models (e.g., stochastic differential equations) are necessary to adapt them to quantum hardware, potentially requiring hybrid quantum-classical approaches
- #limitation:noise — Current quantum hardware is not yet capable of implementing pioneering quantum algorithms, limiting practical applications in finance
- #limitation:data-encoding — Financial models must be translated into quantum-compatible frameworks (e.g., QUBO for portfolio optimization), which may not capture all constraints or fidelity
- #limitation:no-empirical-validation — All claims about quantum speedups are speculative and lack empirical validation or hardware demonstrations
## Contradictions
- #contradiction:classical-vs-quantum — The paper notes a 'quantum algorithm winter,' suggesting progress on quantum algorithms has stalled, which contradicts optimistic industry projections (e.g., McKinsey & Company's $622 billion value claim by 2035)
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
