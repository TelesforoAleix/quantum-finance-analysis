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
- amplitude-estimation
- grover
- quantum-ML
- quantum-simulation
- QPE
- QAA
- QAE
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-18T23:20:17.261507'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:20:20.191611'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:20:27.120513'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:20:40.539570'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:20:53.338932'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:22:00.824684'
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
- method/amplitude-estimation
- method/grover
- method/quantum-ML
- method/quantum-simulation
- method/QPE
- method/QAA
- method/QAE
- method/classical-simulation
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
This preprint provides a technical review of quantum computing applications in finance and economics, targeting researchers and practitioners in quantum computing and financial modeling. The paper surveys quantum algorithms relevant to financial and economic problems and maps specific use-cases—such as option pricing and risk management—to these algorithms. It also discusses challenges in achieving practical quantum advantage, aiming to foster interdisciplinary research to accelerate the adoption of quantum technologies in these sectors.
## Methodology
This preprint is a technical review article that systematically surveys quantum algorithms pertinent to finance and economics, mapping use-cases in these sectors to potential quantum computing solutions. The review is structured into three parts: (i) a survey of key quantum algorithms (simulation, optimization, quantum machine learning, and quantum cryptography), including primitive algorithms like Quantum Phase Estimation (QPE) and Quantum Amplitude Amplification/Estimation (QAA/QAE); (ii) a mathematical formulation of use-cases in finance and economics, such as asset pricing, portfolio optimization, risk management, and macroeconomic forecasting; and (iii) a discussion of challenges and pathways toward Practical Quantum Advantage (PQA). The methodology is theoretical and descriptive, synthesizing existing literature and proof-of-concept implementations without original empirical experimentation. The review assumes familiarity with quantum mechanics and focuses on interdisciplinary collaboration to accelerate quantum computing adoption in financial services.

**Algorithms used:** Quantum Phase Estimation (QPE), Quantum Amplitude Amplification (QAA), Quantum Amplitude Estimation (QAE), Grover's Search Algorithm, Quantum Monte Carlo Integration, Quantum Solvers for Stochastic Differential Equations (SDEs), Quantum Machine Learning (QML) algorithms (supervised, unsupervised, reinforcement learning), Quantum Singular Value Transformation (QSVT), Harrow-Hassidim-Lloyd (HHL) algorithm (implied via QPE and QAA)
## Findings
- [speculative] Quantum computing is expected to solve problems intractable for classical computing, such as simulation of complex quantum many-body systems, with linear scaling compared to exponential scaling for classical methods
- [speculative] Quantum computing could provide speed-ups for classically tractable problems like searching, with proposed advantages ranging from quadratic to exponential
- [speculative] Finance and economics may benefit from quantum computing due to complex calculations, large datasets, and optimization problems, with potential applications in risk assessment, portfolio optimization, fraud detection, and high-frequency trading
- [speculative] Quantum computing could handle large-scale, high-dimensional problems in finance and economics more efficiently, reducing computational time and improving accuracy for certain problem categories
- [speculative] Quantum advantage in finance is categorized into three types: Computational Advantage (Quantum Supremacy), Quantum Utility, and Practical Quantum Advantage (PQA), with PQA being the most impactful for real-world applications
- [speculative] Practical Quantum Advantage (PQA) could contribute up to 8.3% to the UK's economy-wide productivity by 2055 and generate £5.9 billion to £12.9 billion in gross value added to the UK's GDP
- [speculative] Globally, quantum computing applications in finance are projected to contribute $622 billion by 2035, with financial services expected to be one of the first industries to benefit
- [speculative] Quantum Phase Estimation (QPE) is a key subroutine for quantum algorithms, enabling exponential speed-ups in problems like factoring, Hamiltonian diagonalization, and solving linear systems, but requires fault-tolerant quantum hardware
- [speculative] Quantum Amplitude Amplification (QAA) and Quantum Amplitude Estimation (QAE) offer quadratic speed-ups over classical methods for tasks like search and Monte Carlo estimation, with applications in finance and economics
- [speculative] Current bottlenecks to realizing quantum advantage in finance include efficient data loading and readout from quantum computers, as well as the need for error correction in near-term quantum devices
- [speculative] Quantum algorithms like QPE, QAA, and QAE are foundational for more complex quantum applications in finance, including portfolio optimization, risk analysis, and fraud detection
- [speculative] The review identifies use-cases in finance and economics where quantum computing could have high impact, including asset pricing, derivatives pricing, risk management, macroeconomic forecasting, and cybersecurity

**Results summary:** This preprint provides a technical review of quantum computing use-cases in finance and economics, surveying key quantum algorithms and mapping them to potential applications in the sector. The authors discuss theoretical foundations, proof-of-concept implementations, and future implications, highlighting both opportunities and challenges. While quantum computing is speculated to offer significant advantages—such as linear scaling for complex simulations and quadratic to exponential speed-ups for optimization and search problems—these claims remain largely theoretical or speculative due to the lack of empirical validation on real hardware. The review categorizes quantum advantage into three types, with Practical Quantum Advantage (PQA) being the most impactful for real-world applications. However, current bottlenecks, including data loading/readout inefficiencies and the need for fault-tolerant quantum hardware, hinder progress toward PQA. The paper also outlines foundational quantum subroutines like Quantum Phase Estimation (QPE) and Quantum Amplitude Amplification/Estimation (QAA/QAE), which underpin more complex algorithms for finance-related tasks.
## Quantum advantage claim
**Classification:** speculative

The paper presents quantum advantage claims as speculative, as they are based on theoretical propositions and simulations rather than empirical validation on real quantum hardware. While exponential and quadratic speed-ups are theorized for problems like simulation, optimization, and search, the review acknowledges significant technical challenges, such as error correction and data handling, that must be overcome to achieve Practical Quantum Advantage (PQA).
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
- #idea:quantum-advantage — Quantum algorithms (e.g., QPE, QAA, QAE) are foundational for complex financial applications, including asset pricing and fraud detection, though empirical validation is lacking
- #idea:near-term-feasibility — The paper discusses speculative projections of quantum advantage in finance, including economic impacts (e.g., £5.9–£12.9 billion UK GDP contribution by 2055), but acknowledges significant hardware and algorithmic hurdles
- #idea:hybrid-approach — Hybrid quantum-classical approaches are implied as a pathway to address current limitations (e.g., noise, qubit count) in achieving PQA
- #limitation:no-empirical-validation — Theoretical claims about quantum speed-ups are not backed by empirical validation on real quantum hardware, relying instead on simulations and speculative projections
- #limitation:noise — Hardware noise and error rates are identified as critical bottlenecks for realizing quantum advantage in finance, though not deeply explored
- #limitation:data-encoding — Challenges in efficiently loading and reading out data from quantum computers are noted as a barrier to practical implementation
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
