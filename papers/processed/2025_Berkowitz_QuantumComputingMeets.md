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
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: other
source_type_confidence: high
step1_date: '2026-03-20T00:09:42.842220'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:09:44.994224'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:09:48.176761'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:09:51.720235'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:09:57.507460'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:09:59.780925'
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
The paper is an interview-based article discussing the potential applications of quantum computing in financial services, particularly in asset pricing, portfolio optimization, and computationally intensive financial problems. The interviewee, Eric Ghysels, outlines theoretical and practical challenges in adapting financial models to quantum algorithms. Key methodological themes include the translation of financial problems (e.g., portfolio allocation) into quantum-compatible frameworks such as quadratic unconstrained binary optimization (QUBO) and the use of quantum annealing for combinatorial optimization. The discussion also covers the discretization of continuous-time stochastic differential equations for quantum implementation, the potential of hidden-Markov-chain models for capturing dynamic patterns, and the theoretical promise of quadratic speedups in credit risk and derivative pricing. The article does not present empirical results or formal methodologies but rather explores conceptual and algorithmic adaptations of financial models to quantum computing.

**Algorithms used:** Quantum Annealing, Quadratic Unconstrained Binary Optimization (QUBO)
## Findings
- [speculative] Quantum linear algebra could potentially speed up solving integral or partial differential equations in financial asset pricing
- [speculative] Quantum information theory provides tools for embedding notions of ambiguity in pricing models
- [speculative] Quantum annealing algorithms can solve combinatorial optimization problems like portfolio allocation more efficiently by exploring large solution spaces in parallel
- [speculative] Hidden-Markov-chain models adapted for quantum hardware could enable quadratic speedups in credit risk and derivative-pricing computations
- [speculative] Quantum computing use cases in financial services could generate up to $622 billion in value by 2035, per a McKinsey & Company report
- [speculative] Industrial-scale quantum computers may be achievable before 2030, according to public statements by IBM and Google
- [supported] MIDAS (mixed-data sampling) methods are regression-based techniques for combining financial data at different frequencies
- [speculative] Current quantum hardware limitations require finance problems to be reformulated (e.g., discretization of continuous-time models) to fit quantum algorithms
- [speculative] Physics students with knowledge of both quantum computing and finance may find career opportunities in financial engineering

**Results summary:** The interview with Eric Ghysels explores the potential of quantum computing in financial services, particularly for asset pricing, portfolio optimization, and risk modeling. While theoretical advantages are proposed—such as quantum linear algebra for solving differential equations and quadratic speedups in derivative pricing—these claims remain speculative due to hardware limitations and the need for algorithmic adaptations. Ghysels highlights the challenges of translating financial problems into quantum-compatible formats (e.g., quadratic unconstrained binary optimization for portfolio allocation) and notes that progress depends on both hardware scalability and algorithmic innovation. Industry projections (e.g., McKinsey’s $622 billion valuation by 2035) are cited but not empirically validated in the paper.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical potential for quantum advantage in financial applications (e.g., quadratic speedups in derivative pricing, parallel exploration of solution spaces in optimization) but does not provide empirical evidence or hardware demonstrations. All claims are based on algorithmic theory or industry projections, with no validation on real quantum hardware.
## Limitations
- Current quantum hardware is not yet capable of implementing pioneering quantum algorithms from the 1990s, limiting practical applications in finance [inferred]
- Quantum annealing hardware is the most reliable scaled hardware available, but financial problems must be adapted to fit its constraints, which may not be ideal for all use cases
- Discretization of continuous-time stochastic differential equations (e.g., for asset-price dynamics) results in coarse approximations, requiring rethinking of asset-pricing dynamics
- Stochastic volatility diffusion models cannot be directly implemented on quantum computers, necessitating alternative model families like hidden-Markov-chain models
- Portfolio allocation problems must be translated into quadratic unconstrained binary optimization, which involves compromises that may limit the fidelity of the original problem
- [inferred] Lack of empirical validation for quantum speedups in financial applications, as most claims are theoretical or based on simplified models
- [inferred] No discussion of noise mitigation or error correction techniques, which are critical for real-world quantum hardware performance
- [inferred] Potential over-reliance on quantum annealing, which may not be the most suitable approach for all financial optimization problems
- [inferred] The interview format limits depth of technical discussion, potentially omitting key challenges in algorithm design or hardware constraints
## Open questions
- When will quantum computers achieve commercially viable applications in finance?
- How can financial models be effectively rewritten to be amenable to quantum hardware without losing critical features (e.g., stochastic volatility)?
- What are the trade-offs between discretization of continuous financial models and the accuracy of quantum implementations?
- How do hidden-Markov-chain models compare to traditional stochastic differential equations in terms of capturing asset-price dynamics?
- What is the impact of quantum hardware limitations (e.g., qubit count, coherence time) on the scalability of financial quantum algorithms?
- Are there alternative quantum algorithms (beyond annealing) that could better address financial optimization and pricing problems?

**Future work:**
- Develop quantum algorithms tailored to financial problems, such as asset pricing and portfolio optimization, that can leverage near-term hardware
- Explore hybrid quantum-classical approaches to bridge the gap between theoretical quantum speedups and practical implementation
- Investigate the use of hidden-Markov-chain models and other quantum-amenable families for more accurate financial modeling
- Expand research into quantum information theory tools for embedding ambiguity and risk factors in financial models
- Test quantum algorithms on real hardware to validate theoretical claims about speedups and solution quality
- Integrate quantum computing education into financial-engineering programs to prepare the next generation of practitioners
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
