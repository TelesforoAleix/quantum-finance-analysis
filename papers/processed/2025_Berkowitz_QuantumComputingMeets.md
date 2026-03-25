---
aliases:
- Q & A Quantum Computing Meets Finance
- Q Quantum Computing Meets
authors:
- Rachel Berkowitz
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
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
- HHL
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: other
source_type_confidence: high
step1_date: '2026-03-25T16:06:41.196626'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:06:43.853583'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:06:49.982700'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:07:05.783598'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:07:21.967390'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:07:31.881340'
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
- topic/risk-modelling
- topic/derivatives-pricing
- topic/asset-pricing
- method/quantum-annealing
- method/QUBO
- method/HHL
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Q & A Quantum Computing Meets Finance
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
- asset-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
This Q&A article presents an interview with economist Eric Ghysels about how quantum computing could be applied to financial econometrics and asset pricing. It discusses potential quantum advantages for solving integral and differential equations in finance, portfolio optimization, and modeling asset-price dynamics, as well as current hardware and algorithmic limitations and likely timelines for practical impact in financial services.
## Methodology
This source is a Q&A/interview article rather than a formal research paper, so it does not present a structured methods section or a reproducible empirical design. Methodologically, it describes a conceptual approach to applying quantum computing in finance by translating financial models into quantum-compatible formulations. The interview highlights several problem classes: asset pricing framed through integral or partial differential equations that may benefit from quantum linear algebra; portfolio allocation reformulated as quadratic unconstrained binary optimization (QUBO) for solution via quantum annealing; and asset-price dynamics originally modeled with continuous-time stochastic differential equations but approximated through discretization or rewritten using hidden Markov chain models to make them amenable to quantum hardware. The discussion is primarily high-level and exploratory, emphasizing model reformulation, approximation, and hardware compatibility rather than reporting experiments, datasets, benchmarks, or implementation details.

**Algorithms used:** quantum annealing, QUBO, quantum linear algebra
## Findings
- [speculative] Quantum computing could help with computationally intensive finance problems such as asset pricing and portfolio optimization.
- [speculative] Many financial asset-pricing problems reduce to solving integrals or partial differential equations, and quantum linear algebra could potentially speed up those computations.
- [speculative] In finance applications, quantum linear algebra outputs a quantum state, so practical usefulness depends on extracting salient properties of the numerical solution rather than the full solution itself.
- [speculative] Quantum information theory may provide tools for representing ambiguity in financial pricing models, particularly ambiguity about sources of risk.
- [speculative] Progress in finance-relevant quantum computing is currently limited not only by hardware but also by insufficient algorithmic maturity, described here as a 'quantum algorithm winter.'
- [speculative] Quantum annealing is presented as the most reliable scaled quantum hardware currently available for optimization-style finance problems, but only when the finance problem maps naturally to the hardware-compatible formulation.
- [speculative] Portfolio allocation can be translated into quadratic unconstrained binary optimization (QUBO), though doing so requires compromises that may alter the original financial problem.
- [speculative] Quantum annealing algorithms are claimed to solve combinatorial optimization problems such as portfolio allocation more efficiently by exploring large solution spaces in parallel.
- [speculative] Continuous-time stochastic volatility diffusion models used in finance are not directly implementable on current quantum computers and instead require coarse discretization or reformulation.
- [speculative] Rewriting finance models into hardware-amenable families such as hidden Markov chain models may enable quantum implementations for pricing-related tasks.
- [speculative] The interviewee states that his research has shown the potential for quadratic speedups in credit-risk and derivative-pricing computations using such reformulated models.
- [speculative] Commercially viable quantum computing applications in finance remain uncertain in timing, but the interview argues that investment should begin now.
- [speculative] A cited McKinsey report projects that quantum computing use cases in financial services could generate up to $622 billion in value by 2035.
- [speculative] The interview suggests that if industrial-scale quantum computers arrive before 2030, demand may grow for professionals trained in both quantum methods and finance.

**Results summary:** This Q&A article presents Eric Ghysels' views on how quantum computing might affect financial services, especially asset pricing, portfolio optimization, credit risk, and derivative pricing. The piece does not report original empirical experiments or benchmark results. Instead, it argues that quantum linear algebra and quantum annealing may eventually help with computationally intensive finance tasks, while emphasizing major practical barriers including immature algorithms, hardware limitations, and the need to reformulate finance problems into quantum-compatible forms such as QUBO or hidden Markov models. Claims of speedup, including quadratic improvements in some pricing and credit-risk settings, are presented as potential rather than demonstrated outcomes in this article.

**Performance claims:**
- Potential quadratic speedups in credit-risk and derivative-pricing computations
- Up to $622 billion in value for financial-services quantum use cases by 2035 (cited McKinsey projection)
- Industrial-scale quantum computers publicly targeted by IBM and Google before 2030 (as cited in the interview)
## Quantum advantage claim
**Classification:** speculative

The article is an interview-style discussion with no original empirical validation, no hardware results, and no quantitative benchmarking in the text. Speedup statements are framed as potential or future possibilities rather than demonstrated advantage.
## Limitations
- Commercially viable quantum computing applications in finance remain uncertain; the interview explicitly notes that nobody knows when quantum computers will have commercially viable applications.
- Scalable quantum hardware is not yet available, which is identified as a major barrier to practical financial use cases.
- Many pioneering quantum algorithms remain difficult to implement on current hardware even decades after their proposal.
- Progress in quantum algorithms is itself limited; the interview describes a 'quantum algorithm winter.'
- Quantum linear algebra methods may produce solutions as quantum states, creating a bottleneck because useful financial quantities must still be extracted from those states.
- Quantum annealing is currently the most reliable scaled hardware discussed, but only for finance problems that naturally fit the annealing/optimization formulation.
- Translating finance problems such as portfolio allocation into QUBO form requires compromises, potentially altering the original financial problem.
- Realistic continuous-time stochastic volatility diffusion models cannot be directly implemented on current quantum computers.
- Discretizing continuous asset-pricing models into implementable time steps can be very coarse and may require rethinking the underlying asset-pricing dynamics.
- Rewriting models into hardware-amenable families such as hidden Markov chain models may limit realism or fidelity to the original financial process.
- [inferred] The piece is an interview/Q&A rather than a technical study, so it provides no empirical benchmarks, experimental validation, or reproducible methodology.
- [inferred] No direct comparison is provided against state-of-the-art classical financial solvers, making practical advantage unclear.
- [inferred] Claims about potential speedups are not supported here by implementation details, complexity analysis, or real-world case studies.
- [inferred] The discussion relies partly on external industry forecasts (for example, McKinsey and vendor timelines), which may be speculative.
## Open questions
- When will quantum computers become commercially viable for financial services applications?
- Which financial problems will genuinely benefit from quantum computing rather than being forced into unsuitable formulations?
- How can salient numerical properties of quantum-state solutions be efficiently extracted for asset-pricing tasks?
- What new quantum algorithms are needed to move beyond the current slowdown in algorithmic progress for finance-relevant problems?
- Can realistic stochastic volatility and other continuous-time financial models be represented on quantum hardware without overly coarse discretization?
- How much model fidelity is lost when finance problems are rewritten into QUBO or hidden-Markov-chain forms?
- Will the reported quadratic speedups in credit risk and derivative pricing translate into practical end-to-end advantages on real hardware?
- What level of hardware scale, error rates, and architecture will be necessary for industrial-scale financial applications?
- How should finance and quantum expertise be combined in education and workforce development to support adoption?

**Future work:**
- Develop scalable quantum hardware capable of supporting practical financial applications.
- Advance quantum algorithms for finance, especially beyond currently limited implementations of older foundational ideas.
- Design methods for extracting financially relevant observables from quantum-state outputs of linear algebra and PDE solvers.
- Identify finance problems that naturally map to quantum annealing or other quantum paradigms without excessive reformulation.
- Improve formulations of portfolio optimization and related tasks to reduce the compromises required by QUBO mappings.
- Create quantum-compatible representations of asset-price dynamics that preserve more of the realism of continuous-time stochastic models.
- Further investigate hidden-Markov-chain and related model families as quantum-amenable alternatives for pricing and risk analysis.
- Validate proposed speedups for credit risk, derivative pricing, and portfolio optimization with concrete implementations and benchmarks against classical methods.
- Develop interdisciplinary training programs combining quantum computing, physics, and finance.
## Key ideas
- #idea:quantum-advantage — The interview argues that asset pricing, credit risk, and derivative-pricing tasks based on integrals, PDEs, or linear systems may eventually benefit from quantum linear algebra with possible quadratic speedups.
- #idea:quantum-advantage — Portfolio allocation is presented as reformulable into QUBO, making it a candidate for quantum annealing on combinatorial optimisation problems.
- #idea:near-term-feasibility — Quantum annealing is described as the most practically usable currently scaled quantum approach for finance problems that naturally fit annealing-compatible formulations.
- #idea:hybrid-approach — Practical deployment requires reformulating financial models into quantum-compatible structures such as QUBO or hidden Markov chains rather than directly implementing standard continuous-time models.
- #idea:hybrid-approach — Continuous-time stochastic volatility and asset-price models must be discretized, approximated, or redesigned, implying a hybrid modelling workflow between classical financial modelling and quantum computation.
## Contradictions
- The paper advances speculative quantum speedup claims for portfolio optimisation, credit risk, and derivative pricing, but simultaneously states that there is no empirical validation, no benchmarking against classical solvers, and unclear practical usefulness of quantum-state outputs, contradicting strong superiority narratives.
- The paper suggests near-term promise via quantum annealing and possible industrial impact before 2030, yet also emphasizes that realistic financial models require heavy reformulation, current hardware is inadequate, and algorithmic progress is in a 'quantum algorithm winter,' contradicting claims of scalability to real financial workloads.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
