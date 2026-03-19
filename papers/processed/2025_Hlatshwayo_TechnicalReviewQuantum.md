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
- QAOA
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
step1_date: '2026-03-18T23:20:17.261507'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T13:32:35.102357'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T13:32:49.443002'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T13:33:35.604007'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:20:53.338932'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T13:36:29.937488'
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
- topic/market-simulation
- method/HHL
- method/QAOA
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
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
This preprint provides a technical review of quantum computing applications in finance and economics, targeting researchers and practitioners in quantum computing and quantitative finance. The paper surveys key quantum algorithms relevant to financial and economic problems, then maps specific use-cases—such as portfolio optimization, risk management, and economic modeling—to these algorithms. It also discusses challenges in achieving practical quantum advantage and aims to foster interdisciplinary collaboration to accelerate progress in the field.
## Methodology
This preprint presents a technical review of quantum computing use-cases in finance and economics, structured as a survey-based analysis. The methodology involves two main parts: (i) a survey of quantum algorithms pertinent to finance and economics, categorized into simulation, optimization, quantum machine learning, and quantum cryptography; and (ii) a mapping of financial and economic use-cases to these quantum algorithms. The review synthesizes existing literature, mathematical formulations of use-cases, and theoretical foundations of quantum algorithms. It does not involve original empirical experimentation or dataset analysis but rather consolidates proof-of-concept implementations and theoretical proposals from prior work. The focus is on identifying potential quantum advantage, challenges, and pathways to practical quantum advantage (PQA) in financial services and economics.

**Algorithms used:** Quantum Phase Estimation (QPE), Quantum Amplitude Amplification (QAA), Quantum Amplitude Estimation (QAE), Quantum Unstructured Search (Grover's Algorithm), Discrete-Time Quantum Walk (DTQW), Continuous-Time Quantum Walk (CTQW), Harrow-Hassidim-Lloyd (HHL) Algorithm, Quantum Monte Carlo Integration, Quantum Singular Value Estimation (QSVE), Quantum Approximate Optimization Algorithm (QAOA)
## Findings
- [speculative] Quantum computing has the potential to accelerate computation for solving complex problems in finance and economics, particularly those with computationally heavy requirements like risk assessment, portfolio optimization, fraud detection, and high-frequency trading.
- [speculative] Quantum computing could handle large-scale, high-dimensional problems efficiently without resorting to approximations or truncations required by classical methods.
- [speculative] Quantum computing may significantly reduce computational time and improve accuracy for certain categories of problems in finance and economics.
- [speculative] Quantum advantage in finance is projected to contribute up to $622 billion globally by 2035, with the UK potentially seeing an 8.3% economy-wide productivity boost by 2055.
- [speculative] The financial services sector is predicted to be one of the first industries to reap the benefits of quantum technologies.
- [speculative] Quantum algorithms such as Quantum Phase Estimation (QPE), Quantum Amplitude Amplification (QAA), Quantum Amplitude Estimation (QAE), and Quantum Unstructured Search (Grover’s Algorithm) offer theoretical speedups for problems like Monte Carlo integration, optimization, and search.
- [speculative] Quantum walks (discrete-time and continuous-time) could provide quadratic speedups in mixing and hitting times compared to classical random walks, with applications in search algorithms and diffusion processes.
- [speculative] The Quantum Linear Systems Problem (QLSP) could achieve exponential speedups over classical methods for solving linear systems, particularly when the matrix is sparse and well-conditioned.
- [speculative] The Harrow-Hassidim-Lloyd (HHL) algorithm for QLSP could offer exponential speedups in matrix inversion problems, though it only outputs a quantum state proportional to the solution rather than the full solution vector.
- [speculative] Practical Quantum Advantage (PQA) is considered a monumental milestone for quantum computing, where quantum computers solve real-world problems more efficiently than the most advanced classical methods.
- [speculative] Current bottlenecks to achieving quantum advantage include data loading/readout challenges, noise in near-term quantum hardware, and the need for quantum error correction.
- [speculative] Variants of quantum algorithms (e.g., Iterative Quantum Phase Estimation, low-depth QAE) are being developed to make them feasible for Noisy Intermediate-Scale Quantum (NISQ) devices.

**Results summary:** This preprint provides a technical review of quantum computing use-cases in finance and economics, surveying key quantum algorithms and their potential applications. The authors discuss theoretical foundations, proof-of-concept implementations, and future implications for areas like option pricing, risk management, and economic modeling. While the paper highlights the speculative potential for quantum advantage—such as exponential speedups in solving linear systems or quadratic speedups in search and optimization—it acknowledges significant challenges, including hardware limitations, data loading issues, and the need for fault-tolerant quantum computing. The review emphasizes the importance of interdisciplinary collaboration to accelerate the realization of Practical Quantum Advantage (PQA) in financial services.
## Quantum advantage claim
**Classification:** speculative

The paper presents quantum advantage claims as speculative, as they are based on theoretical speedups (e.g., exponential or quadratic) without empirical validation on real quantum hardware. Claims of practical impact, such as economic productivity boosts or industry adoption timelines, are also speculative and rely on projections rather than demonstrated results.
## Limitations
- Lack of peer review, which may affect the rigor and validity of the findings [inferred]
- Review is not comprehensive, focusing only on a subset of use-cases with high potential impact and published proof-of-concept research [author-stated]
- Assumes familiarity with quantum mechanics and related terminology, limiting accessibility to non-specialist audiences [author-stated]
- Technical challenges in efficiently loading and reading out data from quantum computers are noted but not deeply explored [author-stated]
- [inferred] No empirical validation or experimental results on real quantum hardware are provided to support theoretical claims
- [inferred] Potential bias toward optimistic projections of quantum advantage without sufficient discussion of current hardware limitations (e.g., qubit count, noise, error rates)
- [inferred] Limited discussion on the gap between theoretical speedups and practical performance in financial applications
- [inferred] No detailed comparison with state-of-the-art classical methods for the use-cases discussed
- Review does not cover all quantum algorithms or use-cases in finance and economics, potentially missing emerging or niche applications [author-stated]
- [inferred] Lack of discussion on the economic or operational feasibility of integrating quantum computing into existing financial systems
## Open questions
- What is a viable path toward achieving Practical Quantum Advantage (PQA) in finance and economics?
- What are the specific engineering and algorithmic hurdles that must be overcome to realize PQA?
- How can interdisciplinary collaboration be accelerated to bridge the gap between quantum computing research and financial applications?
- What are the trade-offs between quantum utility and practical quantum advantage for real-world financial problems?
- How will quantum computing impact the security and encryption protocols currently used in financial services?
- What are the implications of quantum noise and error rates on the accuracy and reliability of financial computations?
- How do quantum algorithms perform on real-world financial datasets compared to synthetic or simplified models?
- What are the scalability limits of current quantum algorithms for large-scale financial problems (e.g., portfolio optimization with thousands of assets)?
- How can quantum computing be integrated into existing classical computational pipelines in finance?
- What are the ethical and regulatory considerations for adopting quantum computing in financial services?

**Future work:**
- Develop and test quantum algorithms on real quantum hardware for financial use-cases (e.g., IBM Eagle processor or other NISQ devices)
- Extend the review to include a broader range of quantum algorithms and financial/economic use-cases
- Conduct empirical studies to validate theoretical claims about quantum speedups in finance
- Explore hybrid quantum-classical approaches to address current hardware limitations
- Investigate noise mitigation and error correction techniques tailored for financial applications
- Develop benchmarks to compare quantum and classical methods for specific financial problems
- Expand interdisciplinary research to include economists, financial practitioners, and quantum computing experts
- Assess the economic and operational feasibility of integrating quantum computing into financial systems
- Explore quantum-safe cryptography protocols to prepare for future cybersecurity threats
- Investigate the potential of quantum machine learning for real-world financial datasets and applications
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
