---
aliases:
- Research on Quantum Computing Technology and Application
- Research Quantum Computing Technology
authors:
- Meng-liang LI
- Hong YANG
- Xiong GUO
auto_detected: true
classification: ''
contradiction_flags: []
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: International Conference on Modeling, Analysis, Simulation Technologies
  and Applications (MASTA 2019)
methodology_tags:
- quantum-annealing
- HHL
- grover
- quantum-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T15:51:49.340149'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:51:51.941391'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:52:00.631186'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:52:20.001487'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:52:45.865779'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:52:51.830873'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/quantum-cryptography
- method/quantum-annealing
- method/HHL
- method/grover
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Research on Quantum Computing Technology and Application
topic_tags:
- quantum-cryptography
year: 2019
zotero_key: ''
---

## Abstract summary
The paper surveys the field of quantum computing, outlining its basic concepts, main hardware and algorithmic technologies, and current global research and industrial efforts. It discusses potential applications in areas such as communication security, data processing, and scientific simulation, and highlights emerging standardization activities. The authors also describe anticipated development trends, particularly around commercialization and the impact on encryption and information technology.
## Methodology
This conference paper is a high-level narrative overview rather than an empirical study. Its approach is descriptive and synthetic: the authors summarize the history, basic concepts, current international research status, major technical components, standardization activities, application areas, and future development trends of quantum computing. The paper classifies quantum computing into gate-based quantum computing and quantum annealing, and it discusses enabling technology areas such as quantum hardware, quantum coding, and quantum algorithms. It also identifies representative algorithms from the literature, including Shor's algorithm, Grover's algorithm, the HHL algorithm, and Hamiltonian simulation, but does not implement, test, or compare them. The paper further surveys policy and standardization efforts by organizations such as ITU-T and ISO/IEC JTC 1 and comments on potential applications including encryption, data computing, scientific research, and finance. As a conference paper, it appears to function as a short survey or position-style overview rather than a formal experimental or theoretical contribution with a methods section, proofs, datasets, or evaluation protocol.

**Algorithms used:** Shor's algorithm, Grover's algorithm, HHL algorithm, Hamiltonian simulating algorithm, Quantum annealing
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper is a high-level overview of quantum computing concepts, technology status, applications, and development trends rather than an empirical study with original experimental results.
- [speculative] Quantum computing is claimed to improve computational efficiency through superposition and entanglement, especially for problems such as factorization and complex path search.
- [speculative] The authors distinguish two main paradigms: gate-based quantum computing and quantum annealing, identifying D-Wave as the first quantum annealer product.
- [speculative] Hybrid quantum-classical algorithms are presented as a practical near-term approach in which classical systems perform most computation and quantum hardware handles a smaller subproblem.
- [speculative] Quantum hardware is identified as the main bottleneck for large-scale commercial application, with hardware realization, error correction/coding, and algorithms described as core technical areas.
- [speculative] The paper claims quantum computing has broad application prospects in communication security, data computing, scientific research, government, finance, and national security.
- [speculative] The authors state that current cryptographic systems could be broken by sufficiently powerful quantum computers and that quantum-safe and quantum-encryption methods are therefore important future directions.
- [speculative] The paper claims quantum simulation is likely to become one of the first practical quantum-computing technologies because it is comparatively easier to implement under existing technical conditions.
- [speculative] The authors describe global momentum in quantum computing, citing national and regional investments and programs in the United States, China, Europe, and other countries.
- [speculative] The paper argues that quantum computing is approaching commercialization and may enable new business models, but provides no direct evidence or quantified validation.

**Results summary:** This conference paper is primarily a narrative review of quantum computing rather than a paper reporting new empirical or theoretical results. It summarizes basic concepts such as qubits, superposition, entanglement, gate-based quantum computing, and quantum annealing; outlines major technical challenges including hardware and error correction; and surveys applications in encryption, data processing, and scientific simulation. The paper also discusses international research activity and standardization efforts. Its claims about computational speedups, cryptographic disruption, commercialization, and future use in finance and other sectors are broad and forward-looking, with little direct quantitative evidence presented in the paper itself.

**Performance claims:**
- China University of Science and Technology and Zhejiang University jointly announced 10-bit entanglement manipulation based on a superconducting quantum computing scheme
- The European Union had provided long-term support for quantum technology for 20 years, with a total investment of 550 million euros
- The paper claims ferredoxin metabolism in photosynthesis, difficult to simulate classically, could theoretically be simulated in one hour on a quantum computer
- The paper claims quantum computers are exponentially more efficient than digital computers for factorization/decomposition problems
## Quantum advantage claim
**Classification:** speculative

The paper makes broad claims that quantum computing can greatly improve efficiency and provide exponential advantages for tasks such as factorization and simulation, but it does not present original empirical benchmarks, controlled comparisons, confidence intervals, or demonstrated financial-service use cases. Most advantage statements are general or literature-based and therefore remain speculative in this paper.
## Limitations
- The paper is a high-level overview of quantum computing concepts, status, applications, and trends rather than an empirical study, so it provides no experimental evaluation or quantitative evidence for the claims made.
- Author-stated: Quantum hardware is described as the main bottleneck for large-scale commercial applications of quantum computing.
- Author-stated: Quantum teleportation technology is still in the exploratory stage of experimental research.
- Author-stated: The value and business impact of quantum computing mainly depend on the development of hardware and the progress of software.
- [inferred] No finance-specific analysis is provided despite mentioning finance as an application area; there are no concrete financial services use cases, datasets, benchmarks, or implementation details.
- [inferred] No comparison is made between quantum approaches and state-of-the-art classical methods, so practical advantage is not demonstrated.
- [inferred] The paper makes broad claims about computational speedups and application potential without specifying problem classes, complexity assumptions, or boundary conditions under which such advantages hold.
- [inferred] No discussion of hardware noise, error rates, qubit count limitations, or reproducibility is included, even though these are central practical constraints for near-term quantum computing.
- [inferred] The treatment of applications is largely descriptive and speculative, with limited critical assessment of technical readiness or deployment barriers.
- [inferred] As a conference paper, the short format likely constrains depth, technical detail, and coverage of limitations.
## Open questions
- When will quantum hardware mature enough for large-scale commercial applications?
- Which quantum computing architectures and technical paths will prove most viable for scalable practical systems?
- How can decoherence be sufficiently controlled to ensure reliable quantum computation in real-world settings?
- Which application areas will achieve practical quantum advantage first?
- How and when can quantum computing be applied effectively in finance beyond general claims of potential impact?
- What new encryption methods will remain secure against future quantum attacks?
- Will dedicated quantum simulators or general-purpose quantum computers become practical first at commercial scale?
- To what extent can hybrid classical-quantum algorithms deliver useful near-term business value before fault-tolerant quantum computers arrive?

**Future work:**
- Advance quantum hardware to enable large-scale commercial applications.
- Develop core hardware capabilities such as small- and medium-scale qubit integration, high-fidelity and high-speed quantum logic gates, and long-term quantum storage.
- Improve quantum coding and error-correction methods to overcome decoherence and increase computational reliability.
- Develop new quantum algorithms and hybrid classical-quantum algorithms for practical problem solving.
- Continue research and standardization activities for quantum computing, quantum key distribution networks, quantum random number generation, and quantum-safe security.
- Pursue practical deployment of quantum technologies in information technology, encryption, and decoding.
- Explore quantum simulation as an early practical application area under existing technical conditions.
- [inferred] Conduct domain-specific studies for financial services with concrete use cases, benchmarks, and comparisons against classical baselines.
- [inferred] Validate claimed application benefits with empirical experiments on real or realistic hardware rather than relying on broad theoretical or strategic projections.
## Key ideas
- #idea:quantum-advantage — The paper broadly claims quantum computing can deliver major efficiency gains, especially for factorization, search, and simulation, with possible downstream implications for finance.
- #idea:hybrid-approach — It presents hybrid quantum-classical computing as the most practical near-term deployment model, where classical systems handle most computation and quantum hardware solves smaller subproblems.
- #idea:near-term-feasibility — It suggests early practical value is more likely in quantum simulation and quantum communication/security than in large-scale general-purpose applications.
- #idea:quantum-advantage — It highlights the threat of future quantum computers to current public-key cryptography, motivating quantum-safe and quantum-based security approaches relevant to financial institutions.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
