---
aliases:
- A Technical Review of Quantum Computing Use-Cases for Finance and Economics
- Technical Review Quantum Computing
authors:
- Manqoba Q. Hlatshwayo
- Manav Babel
- Dalila Islas-Sanchez
- Konstantinos Georgopoulos
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.20944/preprints202511.1802.v1
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Preprints.org
methodology_tags:
- HHL
- grover
- quantum-walk
- amplitude-estimation
- quantum-simulation
- quantum-ML
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-20T00:23:51.151835'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:24:00.666841'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:24:06.104629'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:25:00.239162'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:25:07.244628'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:25:20.281668'
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
- topic/risk-modelling
- topic/derivatives-pricing
- topic/fraud-detection
- topic/credit-scoring
- topic/high-frequency-trading
- topic/asset-pricing
- topic/quantum-cryptography
- topic/regulatory-compliance
- topic/market-simulation
- method/HHL
- method/grover
- method/quantum-walk
- method/amplitude-estimation
- method/quantum-simulation
- method/quantum-ML
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: A Technical Review of Quantum Computing Use-Cases for Finance and Economics
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
- fraud-detection
- credit-scoring
- high-frequency-trading
- asset-pricing
- quantum-cryptography
- regulatory-compliance
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
This preprint provides a technical review of quantum computing applications in finance and economics, targeting researchers and quantitative analysts. The paper surveys quantum algorithms relevant to financial and economic problems, maps specific use-cases to these algorithms, and discusses challenges in achieving practical quantum advantage. It aims to foster interdisciplinary collaboration to accelerate the adoption of quantum technologies in solving complex sector-specific problems.
## Methodology
This paper is a technical review article that systematically surveys quantum computing use-cases in finance and economics. The methodology involves a two-part structure: (i) a survey of quantum algorithms pertinent to problems in finance and economics, and (ii) a mapping of use-cases in these sectors to the potential quantum algorithms identified in part (i). The review categorizes quantum algorithms into four problem domains: simulation algorithms (e.g., Quantum Monte Carlo Integration, quantum solvers for Stochastic Differential Equations), optimization algorithms (e.g., combinatorial and convex optimization), quantum machine learning algorithms, and quantum cryptography methods. The use-cases in finance and economics are grouped into banking and investment, risk management and cybersecurity, and economics. The review also discusses challenges on the pathway to achieving quantum advantage and provides an interdisciplinary perspective to accelerate practical quantum advantage in these sectors.

**Algorithms used:** Quantum Phase Estimation (QPE), Quantum Amplitude Amplification (QAA), Quantum Amplitude Estimation (QAE), Quantum Unstructured Search (Grover's Algorithm), Discrete-Time Quantum Walk (DTQW), Continuous-Time Quantum Walk (CTQW), Harrow-Hassidim-Lloyd (HHL) Algorithm, Quantum Singular Value Transformation (QSVT)
## Findings
- [speculative] Quantum computing is expected to solve problems intractable for classical computing, such as simulation of complex quantum many-body systems, with linear scaling in system size compared to exponential scaling for classical methods
- [speculative] Quantum computing could provide speed-ups for classically tractable problems like searching, with proposed algorithms ranging from quadratic to exponential speed-ups over classical counterparts
- [speculative] Finance and economics, due to their reliance on complex calculations, large datasets, and optimization problems, are high-potential sectors for quantum computing applications, particularly in risk assessment, portfolio optimization, fraud detection, and high-frequency trading
- [speculative] Quantum computing could enable efficient handling of large-scale, high-dimensional problems in finance and economics without resorting to approximations or truncations required by classical methods, potentially improving accuracy and reducing computational time
- [speculative] Quantum computing may face bottlenecks in data loading and readout efficiency, limiting near-term practical gains
- [speculative] Three definitions of quantum advantage are proposed: Computational Advantage (quantum supremacy), Quantum Utility, and Practical Quantum Advantage (PQA), with PQA being the most relevant for real-world applications in finance and economics
- [speculative] Practical Quantum Advantage (PQA) in finance could contribute up to $622 billion globally by 2035, with the UK potentially seeing an 8.3% economy-wide productivity boost by 2055 due to quantum computing adoption
- [speculative] Quantum Phase Estimation (QPE) is a foundational quantum subroutine with applications in Shor’s algorithm, Hamiltonian diagonalization, and solving linear systems, but requires fault-tolerant quantum computing for high accuracy
- [speculative] Quantum Amplitude Amplification (QAA) and Quantum Amplitude Estimation (QAE) offer potential quadratic speed-ups over classical methods for tasks like Monte Carlo integration, with QAE enabling high-precision amplitude estimation
- [speculative] Quantum Unstructured Search (Grover’s algorithm) provides a quadratic speed-up for unstructured search problems, with applications in optimization, pattern matching, and homomorphic encryption, but requires deep circuits infeasible for current NISQ hardware
- [speculative] Quantum walks (discrete-time and continuous-time) exhibit ballistic propagation and faster diffusion compared to classical random walks, with potential polynomial speed-ups in mixing and hitting times for graph-based problems
- [speculative] The Harrow-Hassidim-Lloyd (HHL) algorithm for solving quantum linear systems could achieve exponential speed-ups over classical methods for sparse, well-conditioned matrices, but faces practical challenges in data encoding and readout

**Results summary:** This preprint provides a technical review of quantum computing use-cases in finance and economics, surveying key quantum algorithms and their potential applications. The authors discuss theoretical foundations, proof-of-concept implementations, and challenges in achieving Practical Quantum Advantage (PQA). Key quantum algorithms reviewed include Quantum Phase Estimation (QPE), Quantum Amplitude Amplification (QAA), Quantum Amplitude Estimation (QAE), Quantum Unstructured Search (Grover’s algorithm), quantum walks, and the Quantum Linear System Solver (HHL algorithm). The review highlights speculative claims about quantum speed-ups, improved computational efficiency, and economic impacts, while noting current bottlenecks such as data loading/readout and hardware limitations. The paper aims to bridge interdisciplinary gaps between quantum computing researchers and financial practitioners to accelerate the development of quantum-ready solutions.
## Quantum advantage claim
**Classification:** speculative

The paper discusses theoretical and speculative claims of quantum advantage across multiple algorithms and applications, but notes that these claims are not empirically validated. Quantum advantage is framed as a future milestone (Practical Quantum Advantage) rather than a demonstrated outcome, with current implementations limited by hardware constraints and lack of fault tolerance.
## Limitations
- Lack of peer review [inferred]
- Review is not comprehensive, covering only a subset of quantum algorithms and use-cases in finance and economics [author-stated]
- Assumes familiarity with quantum mechanics and related terminology, limiting accessibility to non-experts [author-stated]
- [inferred] Potential bias toward theoretical advantages without sufficient empirical validation on real-world financial datasets
- [inferred] No detailed analysis of hardware noise or qubit count constraints affecting practical implementation
- [inferred] Limited discussion on data loading and readout challenges, which are critical bottlenecks for quantum computing in finance
- Review focuses on simpler formulations of quantum algorithms, omitting more complex approaches [author-stated]
- [inferred] No direct comparison with state-of-the-art classical methods for the discussed financial use-cases
- [inferred] Lack of reproducibility guidelines for the proposed quantum algorithms in financial applications
- Potential recency bias, as the review may not cover the latest advancements post-November 2025 [inferred]
- No empirical validation of the quantum algorithms' performance on real quantum hardware [inferred]
- [inferred] Limited discussion on the scalability of quantum algorithms to production-level financial problems
## Open questions
- What are the specific engineering and algorithmic hurdles to overcome for achieving Practical Quantum Advantage (PQA) in finance and economics?
- How can quantum computing efficiently handle data loading and readout for large-scale financial datasets?
- What is the impact of decoherence and noise on the performance of quantum algorithms in real-world financial applications?
- How do quantum algorithms compare with classical methods in terms of accuracy, speed, and cost for specific financial use-cases?
- What are the most viable paths toward demonstrating quantum utility in finance, given current hardware limitations?
- How can interdisciplinary collaboration between quantum computing researchers and financial practitioners be accelerated?
- What are the potential risks and unintended consequences of integrating quantum computing into financial systems?

**Future work:**
- Extend the review to include more complex quantum algorithms and their applications in finance and economics
- Conduct empirical validation of quantum algorithms on real quantum hardware for financial use-cases
- Develop noise mitigation techniques tailored for quantum algorithms in financial applications
- Compare quantum algorithms with state-of-the-art classical methods to identify specific advantages and limitations
- Explore hybrid quantum-classical approaches to address current hardware constraints
- Investigate efficient data loading and readout methods for quantum computing in finance
- Expand the scope to include more use-cases in economics, such as macroeconomic forecasting and game theory
- Develop reproducibility guidelines and benchmarks for quantum algorithms in finance
- Foster interdisciplinary research collaborations to accelerate the development of practical quantum solutions for finance
- Assess the economic impact and feasibility of quantum computing adoption in the financial sector
## Key ideas
- #idea:quantum-advantage — Quantum computing is theorized to provide exponential or quadratic speed-ups for financial problems like portfolio optimization, risk modeling, and derivatives pricing, with potential for Practical Quantum Advantage (PQA) in real-world applications
- #idea:quantum-advantage — Quantum algorithms (e.g., QPE, QAA, QAE, Grover’s) offer theoretical speedups for Monte Carlo integration, optimization, and search in finance, though empirical validation is lacking
- #idea:near-term-feasibility — Speculative projections of quantum advantage in finance include economic impacts (e.g., $622B global productivity boost by 2035), but significant hardware and algorithmic hurdles remain
- #idea:hybrid-approach — Hybrid quantum-classical approaches are implied as a pathway to address current limitations (e.g., noise, qubit count) in achieving PQA
- #limitation:no-empirical-validation — Theoretical claims about quantum speed-ups are not backed by empirical validation on real quantum hardware, relying on simulations and projections
- #limitation:noise — Hardware noise and error rates are identified as critical bottlenecks for realizing quantum advantage in finance
- #limitation:data-encoding — Challenges in efficiently loading and reading out data from quantum computers are noted as a barrier to practical implementation
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
