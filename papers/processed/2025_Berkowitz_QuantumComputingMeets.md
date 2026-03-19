---
aliases:
- Q & A Quantum Computing Meets Finance
- Q Quantum Computing Meets
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
step1_date: '2026-03-19T09:05:57.521292'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T09:05:59.533810'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T09:06:02.967829'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T09:07:30.100453'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T09:07:35.713260'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T09:07:39.921175'
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
- method/quantum-annealing
- method/QUBO
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Q & A Quantum Computing Meets Finance
topic_tags:
- portfolio-optimisation
- asset-pricing
- derivatives-pricing
- risk-modelling
year: 2025
zotero_key: ''
---

## Abstract summary
This interview-based article explores the intersection of quantum computing and financial services, focusing on economist Eric Ghysels' work in translating financial models into quantum algorithms. It discusses potential applications in asset pricing, portfolio optimization, and the challenges of adapting classical financial problems to quantum hardware, while highlighting the current limitations and future opportunities in the field.
## Methodology
The paper is an interview-based discussion with economist Eric Ghysels on the intersection of quantum computing and financial services. It explores conceptual and theoretical approaches to adapting financial models for quantum algorithms, particularly focusing on asset pricing, portfolio optimization, and stochastic processes. Ghysels discusses the translation of financial problems into quantum-compatible frameworks, such as quadratic unconstrained binary optimization (QUBO) for portfolio allocation and hidden-Markov-chain models for asset-price dynamics. The discussion highlights challenges in implementing continuous-time stochastic differential equations on quantum hardware and the need to discretize or reformulate models. Theoretical potential for quadratic speedups in credit risk and derivative pricing is mentioned, along with the role of quantum annealing and quantum linear algebra in solving financial problems. The paper does not present empirical results or formal methodologies but rather conceptual insights and future directions.

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

**Results summary:** The interview with Eric Ghysels explores the potential of quantum computing in financial services, particularly for asset pricing, portfolio optimization, and risk modeling. Ghysels highlights theoretical opportunities such as quantum linear algebra for solving differential equations and quantum annealing for optimization, but notes significant challenges in adapting financial models to quantum hardware. While quadratic speedups are speculated for certain applications (e.g., credit risk and derivative pricing), no empirical validation is provided. The discussion also underscores hardware limitations, algorithmic gaps, and the speculative nature of industry projections (e.g., $622 billion value by 2035).
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum speedups (e.g., quadratic speedups in derivative pricing) and efficiency gains in optimization, but all claims are speculative, lacking empirical validation or real-hardware demonstrations. Industry projections and hardware timelines are also cited without peer-reviewed backing.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum annealing algorithms are the most reliable scaled hardware available, but they require finance problems to fit specific formats (e.g., quadratic unconstrained binary optimization), which may not be ideal for all financial applications
- Discretization of continuous-time stochastic differential equations (e.g., for asset-price dynamics) results in coarse approximations, requiring rethinking of asset-pricing dynamics
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, necessitating alternative model families like hidden-Markov-chain models
- [inferred] Lack of empirical validation for quantum speedups in financial applications, as most claims are theoretical or based on simplified models
- [inferred] Potential vendor bias in industry reports (e.g., McKinsey & Company) projecting quantum computing value in financial services by 2035
- [inferred] No peer review for claims or projections mentioned in the interview, as this is a Q&A article rather than a peer-reviewed study
## Open questions
- When will quantum computers achieve commercially viable applications in finance?
- How can financial models be effectively translated into quantum-compatible formats without compromising their realism or accuracy?
- What are the trade-offs between discretizing continuous financial models and maintaining their predictive power?
- How will quantum computing handle ambiguity in risk factors for asset pricing, and what are the limitations of quantum information theory in this context?
- What is the timeline for achieving scalable quantum hardware capable of solving real-world financial problems?

**Future work:**
- Develop quantum algorithms tailored for financial applications, such as portfolio optimization and derivative pricing, that can leverage current and near-term hardware
- Explore hybrid quantum-classical approaches to bridge the gap between theoretical quantum speedups and practical implementation
- Investigate alternative model families (e.g., hidden-Markov-chain models) for asset pricing that are amenable to quantum computation
- Expand financial-engineering education to include quantum computing fundamentals to prepare the next generation of professionals
- Conduct empirical studies to validate theoretical claims of quantum advantage in finance
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
