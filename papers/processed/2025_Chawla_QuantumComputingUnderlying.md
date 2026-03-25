---
aliases:
- Quantum Computing-The Underlying Principle Behind it
- Quantum Computing Underlying Principle
authors:
- Ansh Chawla
- Sankalp Mathur
- Harshit Rao
- Naman Mudgal
- Vanita Bhardwaj
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.33889/PMSL.2025.4.2.020
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Prabha Materials Science Letters
methodology_tags:
- QAOA
- VQE
- quantum-ML
- quantum-SVM
- amplitude-estimation
- grover
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-25T16:07:35.456933'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:07:39.910285'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:07:51.395808'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:08:16.115485'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:08:52.573402'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:09:03.980214'
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
- topic/fraud-detection
- topic/credit-scoring
- topic/quantum-cryptography
- topic/market-simulation
- method/QAOA
- method/VQE
- method/quantum-ML
- method/quantum-SVM
- method/amplitude-estimation
- method/grover
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Quantum Computing-The Underlying Principle Behind it
topic_tags:
- portfolio-optimisation
- risk-modelling
- fraud-detection
- credit-scoring
- quantum-cryptography
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
This paper provides a broad theoretical overview of quantum computing, explaining its physical principles such as superposition, entanglement, and coherence, and how these underpin qubits, quantum gates, and key algorithms like Shor’s, Grover’s, and Deutsch–Jozsa. It surveys prospective applications across healthcare, finance, cryptography, AI, materials science, and quantum networking, while also detailing current limitations in qubit stability, scalability, error correction, and hardware. The authors conclude with a discussion of future directions, emphasizing the need for fault-tolerant architectures and highlighting optimization, climate science, and secure quantum communication as major areas of impact.
## Methodology
The paper is a peer-reviewed theoretical/conceptual overview rather than an empirical study. Its methodology consists of a narrative, literature-based exposition of the principles, history, algorithms, applications, and limitations of quantum computing. The theoretical framework is grounded in standard quantum mechanics and quantum information concepts, especially qubits represented in Hilbert space, superposition, entanglement, coherence, unitary gate operations, measurement-induced state collapse, and Bloch-sphere state representation. The paper presents formal qubit state expressions such as |psi> = alpha|0> + beta|1> with the normalization assumption |alpha|^2 + |beta|^2 = 1, and the Bloch-sphere parameterization |psi> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>. It also gives conceptual algorithmic descriptions of Shor's algorithm, Grover's algorithm, and the Deutsch-Jozsa algorithm, emphasizing asymptotic speedup claims and oracle/period-finding reasoning rather than proving new theorems or deriving novel formal results. The paper further discusses assumptions and propositions common in the field, such as the no-cloning theorem, the need for ancilla qubits in quantum error correction, fault-tolerance thresholds, and the expected relevance of algorithms like QAOA and VQE for optimization and finance. Overall, the approach is descriptive and synthesizing, with no original formal proof technique, no new mathematical model beyond standard textbook formulations, and no experimental validation.

**Algorithms used:** Shor's algorithm, Grover's algorithm, Deutsch-Jozsa algorithm, QAOA, VQE, Quantum Amplitude Estimation, Quantum Monte Carlo, Quantum Phase Estimation, Variational Quantum Classification, Quantum Fourier Transform
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper argues that quantum computing can outperform classical computing on certain problem classes by exploiting superposition, entanglement, and coherence.
- [speculative] The paper claims Shor’s algorithm factors integers in polynomial time, contrasting this with exponential-time classical approaches.
- [speculative] The paper claims Grover’s algorithm provides a quadratic speedup for unstructured search, reducing complexity from O(N) to O(√N), although one passage incorrectly states O(N) for the quantum runtime.
- [speculative] The paper claims the Deutsch-Jozsa algorithm determines whether a function is constant or balanced with one oracle query, versus O(2^n) classical evaluations in the worst case.
- [speculative] For finance, the paper claims quantum amplitude estimation can provide a quadratic speedup over classical Monte Carlo methods for Value at Risk and related risk-simulation tasks, contingent on constructing suitable task-specific quantum circuits.
- [speculative] The paper proposes that quantum computing could improve fraud detection in banking by processing large datasets and identifying patterns beyond the reach of classical methods, including via variational quantum classification.
- [speculative] The paper proposes that quantum computing could improve portfolio optimization, market simulation, and broader financial risk analysis using algorithms such as QAOA and quantum Monte Carlo.
- [speculative] The paper claims quantum computing may improve credit risk scoring by enabling faster scenario simulation and richer predictive modeling, but acknowledges implementation remains immature.
- [speculative] The paper argues that large-scale fault-tolerant quantum computing is limited by decoherence, qubit instability, scalability constraints, and high error-correction overhead.
- [speculative] The paper states that fault-tolerant quantum computing may require thousands of physical qubits per logical qubit and gate error rates below roughly 10^-3 to 10^-4.
- [speculative] The paper claims current qubit technologies typically maintain coherence only for microseconds to milliseconds, constraining computation depth.
- [speculative] The paper argues that Shor’s algorithm threatens RSA and ECC, motivating migration toward post-quantum cryptography and quantum-safe communication methods.
- [speculative] The paper suggests quantum networking, including QKD and teleportation-enabled quantum internet infrastructure, could support ultra-secure communication relevant to finance and other sectors.
- [speculative] The paper presents finance as a promising application domain for quantum computing, but does not provide original financial experiments, proofs, or validated implementations.

**Results summary:** This is a broad theoretical overview of quantum computing rather than a finance-specific analytical paper. It summarizes core principles such as superposition, entanglement, coherence, qubits, and quantum gates, and reviews canonical algorithms including Shor’s, Grover’s, and Deutsch-Jozsa. For financial services, the main claims are that quantum methods could improve fraud detection, risk management, portfolio optimization, and credit risk analysis, with particular emphasis on quadratic speedups from quantum amplitude estimation for Monte Carlo-style risk calculations such as VaR/CVaR. However, the paper does not present original theorems, derivations, empirical experiments, or finance-specific benchmarks; its claims are largely literature-based and forward-looking. It also emphasizes that practical realization remains constrained by decoherence, scalability, hardware cost, and the substantial overhead required for quantum error correction.

**Performance claims:**
- Shor’s algorithm claimed to factor integers in polynomial time versus exponential-time classical methods
- Grover’s algorithm claimed to reduce unstructured search complexity from O(N) to O(√N)
- Deutsch-Jozsa algorithm claimed to solve the constant-vs-balanced problem in O(1) oracle queries versus O(2^n) classical evaluations
- Quantum amplitude estimation claimed to provide a quadratic speedup over classical Monte Carlo for financial risk estimation tasks
- Quantum teleportation over distances exceeding 1,200 km cited from prior literature
- IBM roadmap cited for processors of 1,386 qubits ('Flamingo') and 4,158 qubits ('Kookaburra') by 2025
- Fault-tolerant operation claimed to require gate error rates below approximately 10^-3 to 10^-4
- Quantum error correction claimed to require thousands of physical qubits per logical qubit
- Current qubit coherence times described as microseconds to milliseconds
## Quantum advantage claim
**Classification:** theoretical

The paper makes literature-based theoretical claims of quantum speedups in factoring, search, and Monte Carlo-style financial risk estimation, but it does not demonstrate quantum advantage with original proofs, experiments, simulations, or hardware results in this paper.
## Limitations
- The paper explicitly notes that the physical realization of a quantum computer remains a major challenge.
- Qubit stability and decoherence severely limit computation, with current qubits maintaining coherence only for milliseconds to microseconds.
- Quantum systems require extremely controlled environments, including temperatures near absolute zero and advanced shielding, increasing operational complexity and cost.
- Scalability is a major limitation: practical applications would require millions of high-quality qubits, while larger systems exacerbate coherence loss, cross-talk, and engineering complexity.
- Quantum error correction imposes massive resource overhead, with thousands of physical qubits needed to maintain one stable logical qubit.
- Current hardware error rates remain too high for large-scale fault-tolerant computation, and keeping error rates below critical thresholds is still unresolved.
- Specialized hardware requirements such as cryogenic cooling, ultra-high vacuum chambers, and precision control electronics make quantum systems expensive and difficult to deploy.
- Manufacturing stable and consistent qubits at scale remains an unresolved materials and fabrication challenge.
- There is no consensus on which qubit technology will ultimately support large-scale fault-tolerant quantum computing.
- Practical quantum algorithm development remains limited; the paper states that finding useful algorithms for significant real-world problems is still an active research area.
- Quantum programming languages and software tools are still nascent, and programming often requires low-level hardware-specific expertise.
- Verification of correctness and reliability of quantum computations remains an open problem due to the probabilistic nature of quantum mechanics.
- Quantum computing platforms remain financially inaccessible to most organizations, with access concentrated in major research institutions, governments, and large technology firms.
- Cloud-based quantum services currently offer only limited qubit counts, stability, and computational power.
- The paper notes that practical implementation in finance, especially for credit risk scoring, remains in its infancy due to hardware constraints and algorithmic development challenges.
- [inferred] The paper is largely a broad conceptual overview and does not provide empirical validation, experiments, benchmarks, or case studies demonstrating claimed advantages in financial services.
- [inferred] Claims of exponential or major speedups are presented without discussing the assumptions under which these asymptotic advantages translate into practical end-to-end performance.
- [inferred] The discussion of finance applications is high-level and does not compare quantum methods against state-of-the-art classical financial models or solvers.
- [inferred] The paper assumes that theoretical algorithmic advantages will generalize to real financial workloads, but does not address data loading, model calibration, or integration overheads.
- [inferred] No concrete resource estimates are provided for financial use cases such as portfolio optimization, fraud detection, or risk analysis, limiting practical interpretability.
- [inferred] The treatment of financial applications does not address regulatory, auditability, explainability, or operational constraints that are central in financial services deployment.
- [inferred] The paper is not finance-specific, so its usefulness for a systematic review on quantum computing in financial services is limited by broad scope and lack of domain depth.
## Open questions
- How can scalable and fault-tolerant quantum systems be achieved in practice?
- Which qubit technology—superconducting, trapped-ion, photonic, topological, or another approach—will ultimately prove most viable for large-scale quantum computing?
- How can decoherence and environmental noise be reduced enough to support long and reliable computations?
- How can quantum error correction be made efficient enough to avoid the enormous physical-qubit overhead currently required?
- Can hardware error rates be reduced below fault-tolerance thresholds while simultaneously scaling up system size?
- What practical quantum algorithms can be developed for significant real-world problems beyond canonical examples like Shor's and Grover's algorithms?
- How can reliable verification and validation of probabilistic quantum computations be performed?
- When and under what conditions will quantum computing deliver practical advantages over classical methods in finance?
- How effective will quantum approaches such as amplitude estimation, QAOA, and VQE be for real financial tasks like VaR/CVaR estimation, portfolio optimization, and fraud detection?
- Can quantum methods support real-time fraud detection rather than only post hoc identification of fraudulent activity?
- How can task-specific quantum circuits for financial simulation be designed efficiently and robustly?
- What is the realistic timeline for migration to post-quantum cryptography in response to future large-scale quantum computers?
- [inferred] Will theoretical speedups in financial modeling persist once data encoding, error mitigation, and hybrid orchestration costs are included?
- [inferred] What problem sizes in finance are needed before quantum methods outperform optimized classical baselines in practice?
- [inferred] How should financial institutions evaluate the trade-off between quantum advantage, implementation cost, and regulatory risk?

**Future work:**
- Develop more stable qubits through approaches such as superconducting circuits, trapped ions, and topological qubits.
- Advance quantum error correction techniques, including surface codes and cat qubits, to make practical quantum computing feasible.
- Build scalable quantum processors with improved connectivity and lower error rates.
- Continue innovation in hardware design, noise reduction, error correction, and quantum algorithm design to address current barriers.
- Expand research into optimization applications, including logistics, supply chains, and financial modeling.
- Apply quantum algorithms such as QAOA and VQE to portfolio optimization, fraud detection, and market simulation in finance.
- Develop quantum communication networks and a quantum internet for ultra-secure communication.
- Pursue post-quantum cryptographic methods and quantum-safe security protocols.
- Integrate quantum computing with existing digital infrastructures to support broader adoption.
- Promote interdisciplinary collaboration to accelerate progress across hardware, software, and application domains.
- [inferred] Conduct empirical studies and benchmarks on real or realistic financial datasets to validate proposed finance use cases.
- [inferred] Compare quantum approaches with state-of-the-art classical financial methods to determine whether practical advantage exists.
- [inferred] Produce resource estimates and implementation studies for specific financial applications such as VaR/CVaR, credit scoring, and fraud detection.
- [inferred] Investigate hybrid quantum-classical workflows tailored to financial services, where near-term hardware limitations are significant.
- [inferred] Study deployment issues in finance, including explainability, governance, compliance, and operational integration.
## Key ideas
- #idea:quantum-advantage — The paper maps canonical quantum speedup arguments, especially amplitude estimation, to financial use cases such as VaR/CVaR estimation, portfolio optimisation, fraud detection, and credit risk analysis.
- #idea:quantum-advantage — It claims quantum amplitude estimation could quadratically accelerate Monte Carlo-style risk calculations relevant to financial risk modelling.
- #idea:near-term-feasibility — It presents variational quantum classifiers, QNN-style methods, and QSVMs as plausible NISQ-era approaches for fraud detection and related financial ML tasks.
- #idea:hybrid-approach — It suggests hybrid quantum-classical workflows as the most practical route for early finance applications, embedding quantum subroutines inside classical optimisation and risk pipelines.
- #idea:quantum-advantage — It frames QAOA and VQE as promising methods for optimisation-oriented finance problems, especially portfolio optimisation, once hardware matures.
- #idea:quantum-advantage — It highlights the financial-security relevance of Shor’s algorithm by arguing that future quantum computers threaten RSA/ECC and motivate post-quantum cryptography and QKD.
## Contradictions
- The paper advances theoretical claims of quantum advantage for finance, especially via amplitude estimation and optimisation algorithms, but simultaneously states that scalable fault-tolerant hardware requires millions of qubits and remains a distant goal, undermining practical applicability to real financial workloads.
- The paper discusses NISQ-relevant methods such as variational classifiers, QAOA, and VQE for finance, yet also emphasizes severe decoherence, short coherence times, and high error-correction overhead, which contradict optimistic implications about near-term deployment.
- The paper presents speedup claims for financial tasks without empirical benchmarks, resource estimates, or comparisons to strong classical baselines, creating tension with stronger application-focused papers that imply practical superiority.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
