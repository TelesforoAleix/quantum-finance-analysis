---
aliases:
- 'The State of Quantum Computing: Applications, Initiatives, Challenges and Ethical
  Concerns up to 2025'
- State Quantum Computing Applications
authors:
- Farial Mahmod
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: ''
methodology_tags:
- HHL
- QAOA
- VQE
- quantum-annealing
- grover
- quantum-ML
- quantum-SVM
- variational
- QUBO
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-18T23:29:57.164716'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T23:30:58.635755'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T23:31:08.058373'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T23:31:19.832197'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T23:31:33.003627'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T23:31:42.023468'
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
- method/QAOA
- method/VQE
- method/quantum-annealing
- method/grover
- method/quantum-ML
- method/quantum-SVM
- method/variational
- method/QUBO
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'The State of Quantum Computing: Applications, Initiatives, Challenges and
  Ethical Concerns up to 2025'
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
This review article provides a comprehensive overview of the current state of quantum computing, focusing on its experimental and commercial applications across diverse industries from 2016 to 2025. The paper systematically examines use cases, government initiatives, intergovernmental collaborations, and the technical and ethical challenges associated with quantum computing, aiming to map its global adoption and impact.
## Methodology
The paper implements a Systematic Literature Review (SLR) approach to synthesize existing knowledge on the use cases of quantum computing globally across industries. The methodology follows established guidelines for conducting structured reviews to ensure reproducibility and comprehensiveness. The review includes a search strategy combining keywords such as 'quantum computing applications,' 'quantum computing use case,' and 'quantum technology cooperation' across multiple databases, including peer-reviewed journals (Springer, Frontiers, Nature), open-access repositories (arXiv), blogs, case studies, white papers from quantum computing companies, and government publications. Inclusion criteria focused on studies published between 2016 and 2025 that address experimental and commercial use cases of quantum computing, while excluding non-peer-reviewed and non-English publications. The synthesis method involves classifying applications by industry and analyzing outcomes, initiatives, and challenges.

**Algorithms used:** Harrow–Hassidim–Lloyd (HHL), Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Grover's algorithm, Variational Quantum Computing (VQC), Quantum Support Vector Machine (QSVM), Quantum Gradient Descent (QGD), Quantum Annealing, Shor’s algorithm, Variational Quantum Imaginary Time Evolution (VarQITE), Quantum Neural Networks (QNNs), Quantum-inspired Recurrent Neural Networks (QRNNs), Quantum Machine Learning (QML)
**Frameworks:** Qiskit, Fire Opal, Ansys's LS-DYNA

**Experimental setup:** Experiments mentioned in the paper utilize a variety of quantum hardware and simulators, including IBM Quantum processors (e.g., IBM Eagle, Heron), IonQ hardware (e.g., Aria and Forte processors), D-Wave's Advantage2 quantum annealer, and quantum simulators like QasmSimulator. Hybrid quantum-classical approaches are commonly employed, integrating quantum circuits with classical optimizers (e.g., COBYLA) and classical preprocessing steps. Specific setups include the use of IBM's cloud-accessible quantum processors for financial and nuclear fusion applications, and D-Wave's hybrid solver for optimization problems in agriculture and logistics.

**Dataset:** The paper references several industry-specific datasets and real-world applications, including: (1) Agricultural data (e.g., soil quality, weather, pests) for precision agriculture in India; (2) MRI scans for Alzheimer's disease detection in healthcare; (3) PET imaging data for cancer characterization in radiomics; (4) ISIC 2019 dataset for skin lesion classification in dermatology; (5) Production-scale trading data for algorithmic bond trading in finance; (6) Historical and real-time data for LNG vessel routing optimization in transportation. Specific datasets are not always detailed, but the applications rely on real-world or simulated data relevant to each industry.
## Findings
- [supported] Quantum computing has demonstrated experimental performance surpassing classical computational power in specific tasks, such as Google's Sycamore and Willow quantum chips outperforming classical supercomputers in random circuit sampling benchmarks [supported]
- [supported] D-Wave’s Advantage2 quantum computer, operational in 2025, solves problems with up to 2 million variable constraints via hybrid solver [supported]
- [supported] Caltech's 6,100 neutral atom qubit array achieved 99.98% fidelity in single-qubit operations and maintained quantum coherence for 13 seconds [supported]
- [supported] A hybrid quantum-classical variational quantum computing (VQC) algorithm for precision agriculture in India achieved 96.26% prediction accuracy, 24-28% reductions in resource usage, and 24-26% yield improvements over classical methods [supported]
- [supported] The Australian Army and Q-CTRL’s hybrid quantum-classical algorithm reduced convoy deployment time by over two hours compared to classical methods, demonstrating a 12x improvement in optimal solution likelihood [supported]
- [supported] HSBC and IBM’s quantum-enabled algorithm for bond trading achieved a 34% accuracy improvement over classical approaches in real-time market data processing [supported]
- [supported] Hybrid classical-quantum neural networks (HCQNNs) for Alzheimer’s detection achieved 97% accuracy, surpassing classical models (92%) [supported]
- [supported] Quantum-enhanced Inception-ResNet-V1 models classified skin lesions with 98% accuracy, outperforming classical CNNs (81-97%) [supported]
- [speculative] Quantum computing is argued to provide exponential computational power over classical computers for specific problem sets, such as optimization and simulation [speculative]
- [speculative] Quantum advantage is claimed for problems like large-scale optimization in energy, logistics, and finance, though real-world scalability remains unproven [speculative]
- [disputed] Claims of quantum advantage in commercial applications (e.g., D-Wave’s 2 million variable constraints) are disputed due to reliance on hybrid solvers and lack of peer-reviewed validation for pure quantum advantage [disputed]
- [supported] Quantum Key Distribution (QKD) networks, such as Toshiba’s Quantum Secure Metro Network, demonstrate resistance to cyber and quantum attacks [supported]
- [speculative] Quantum computing is projected to revolutionize industries like agriculture, defense, energy, and healthcare through enhanced optimization and simulation capabilities [speculative]
- [speculative] Quantum algorithms like HHL and Grover’s are proposed to offer speed-ups for genetic analysis and genome assembly, but real-world implementations are lacking [speculative]

**Results summary:** This review article synthesizes the state-of-the-art applications, initiatives, and challenges of quantum computing across industries up to 2025. Key findings include demonstrated quantum advantage in specific benchmarks (e.g., Google’s Sycamore and Willow chips), operational hybrid quantum-classical systems solving large-scale optimization problems (e.g., D-Wave’s Advantage2), and high-fidelity quantum hardware advancements (e.g., Caltech’s 6,100-qubit array). Industry-specific applications show empirical success in finance (34% accuracy improvement in bond trading), agriculture (96.26% prediction accuracy), defense (logistics optimization), and healthcare (97-98% diagnostic accuracy). However, many claims of quantum advantage remain speculative or disputed due to reliance on hybrid approaches or lack of peer-reviewed validation. The review also highlights government initiatives, ethical concerns, and limitations like error correction and scalability.

**Performance claims:**
- Google’s Willow quantum chip completes a computation in under 5 minutes that would take the world’s fastest supercomputer 10^25 years
- D-Wave’s Advantage2 solves problems with up to 2 million variable constraints
- Caltech’s 6,100-qubit array achieves 99.98% fidelity in single-qubit operations and 13-second coherence
- Hybrid VQC algorithm for agriculture achieves 96.26% prediction accuracy, 24-28% resource reduction, and 24-26% yield improvement
- Australian Army’s quantum logistics solution reduces deployment time by over 2 hours (12x improvement in optimal solutions)
- HSBC/IBM quantum bond trading algorithm achieves 34% accuracy improvement over classical methods
- HCQNNs for Alzheimer’s detection achieve 97% accuracy (vs. 92% classical)
- Quantum-enhanced Inception-ResNet-V1 models achieve 98% skin lesion classification accuracy (vs. 81-97% classical)
## Quantum advantage claim
**Classification:** theoretical

The paper presents empirical demonstrations of quantum advantage in specific benchmarks (e.g., Google’s random circuit sampling) and hybrid quantum-classical systems solving large-scale problems (e.g., D-Wave, HSBC/IBM). However, most claims of quantum advantage are theoretical or speculative for broader industry applications, as they rely on simulations, hybrid approaches, or lack peer-reviewed validation for pure quantum advantage on real hardware.
## Limitations
- [inferred] Search coverage may be limited to English-language publications, excluding non-English research
- [inferred] Grey literature and non-peer-reviewed sources (e.g., blogs, case studies) may introduce bias or lack rigorous validation
- Exclusion of non-English publications may omit relevant regional advancements in quantum computing
- [inferred] The review's timeframe (2016–2025) may miss foundational work published before 2016 or emerging trends post-2025
- [inferred] Lack of critical appraisal of included sources (e.g., industry whitepapers may have vendor bias)
- [inferred] No explicit discussion of hardware noise or qubit coherence limitations in real-world financial applications (e.g., HSBC-IBM bond trading case)
- [inferred] Hybrid quantum-classical approaches (e.g., in finance) may not address scalability to production-scale problems due to current qubit constraints
- [inferred] Limited empirical validation of quantum advantage claims in financial services (e.g., HSBC-IBM results are preliminary and not benchmarked against state-of-the-art classical solvers)
- [inferred] No discussion of reproducibility challenges in quantum experiments (e.g., variability in hardware performance across runs)
- Quantum algorithms in finance (e.g., bond trading optimization) rely on noisy intermediate-scale quantum (NISQ) devices, limiting solution quality
- [inferred] Ethical concerns (e.g., quantum decryption risks) are mentioned but not deeply analyzed for financial services-specific implications
## Open questions
- How will quantum computing's exponential speedup translate into tangible economic benefits for financial services (e.g., cost savings, risk reduction)?
- What are the specific thresholds (e.g., qubit count, error rates) for quantum advantage in financial use cases like portfolio optimization or fraud detection?
- How do hybrid quantum-classical algorithms compare to purely classical state-of-the-art methods in real-world financial datasets?
- What are the long-term implications of quantum decryption (e.g., Shor’s algorithm) on financial infrastructure security, and how can institutions prepare?
- How can quantum computing address dynamic, real-time financial challenges (e.g., high-frequency trading) given current hardware limitations?
- What regulatory frameworks are needed to govern quantum computing applications in finance (e.g., algorithmic transparency, data privacy)?
- How will quantum computing impact workforce development in financial services (e.g., upskilling for quantum-ready roles)?
- What are the ethical risks of quantum computing in finance (e.g., market manipulation via quantum-powered predictive models)?

**Future work:**
- Expand review coverage to include non-English publications and grey literature to capture global advancements
- Conduct empirical benchmarks comparing quantum and classical solvers for financial problems (e.g., portfolio optimization, risk analysis)
- Investigate noise mitigation techniques (e.g., error correction, error mitigation) to improve quantum algorithm performance in finance
- Explore scalable hybrid architectures for financial applications (e.g., integrating quantum processors with classical HPC systems)
- Develop standardized metrics for evaluating quantum advantage in financial use cases (e.g., speedup, accuracy, cost efficiency)
- Assess the readiness of financial institutions for post-quantum cryptography (e.g., migration timelines, cost implications)
- Study the ethical and regulatory implications of quantum computing in finance, including potential misuse scenarios
- Extend research to emerging quantum hardware (e.g., photonic, trapped-ion) and their applicability to financial services
- Collaborate with industry partners to pilot quantum solutions in production environments (e.g., live trading, fraud detection)
## Key ideas
- #idea:quantum-advantage — Empirical demonstrations (e.g., Google’s Sycamore/Willow chips) show quantum advantage in specific benchmarks like random circuit sampling
- #idea:quantum-advantage — Hybrid quantum-classical algorithms (e.g., HSBC/IBM bond trading) achieve 34% accuracy improvement over classical methods in real-time market data processing
- #idea:near-term-feasibility — Hybrid VQC algorithms for precision agriculture and Alzheimer’s detection demonstrate near-term applicability of quantum-classical approaches in industry
- #idea:hybrid-approach — D-Wave’s Advantage2 solves problems with up to 2 million variable constraints via hybrid solvers, highlighting practical scalability in optimization tasks
- #idea:hybrid-approach — Quantum-enhanced models (e.g., Inception-ResNet-V1) outperform classical CNNs in skin lesion classification (98% vs. 81-97%), showcasing hybrid quantum-ML potential
- #limitation:noise — Quantum algorithms in finance rely on NISQ devices, limiting solution quality due to hardware noise and qubit coherence issues
- #limitation:no-empirical-validation — Claims of quantum advantage in commercial applications (e.g., D-Wave’s 2M variable constraints) are disputed due to lack of peer-reviewed validation for pure quantum advantage
- #limitation:data-encoding — Hybrid approaches in finance (e.g., bond trading) may not address scalability to production-scale problems due to qubit constraints and data encoding costs
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum advantage in bond trading (34% accuracy improvement), but lacks benchmarking against state-of-the-art classical solvers, leaving quantum superiority disputed
- #contradiction:scalability — While D-Wave’s Advantage2 solves 2M variable constraints, the reliance on hybrid solvers contradicts claims of pure quantum scalability for real-world financial problems
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
