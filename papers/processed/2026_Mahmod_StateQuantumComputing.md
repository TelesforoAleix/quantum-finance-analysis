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
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-20T00:58:05.093229'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:58:08.258212'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:58:12.470543'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:58:27.956808'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:58:36.930464'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:58:48.032649'
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
This review article provides a comprehensive overview of the current state of quantum computing, focusing on its experimental and commercial applications across diverse industries such as finance, healthcare, and energy from 2016 to 2025. The paper systematically examines government initiatives, inter-governmental collaborations, and the technological advancements driving quantum computing adoption. It also highlights key challenges, limitations, and ethical concerns associated with the widespread deployment of quantum technologies.
## Methodology
This review article implements a Systematic Literature Review (SLR) approach to synthesize existing knowledge on the use cases of quantum computing globally across industries. The methodology follows established guidelines for conducting structured reviews to ensure reproducibility and comprehensiveness in source selection. The review covers applications, government initiatives, challenges, and ethical concerns related to quantum computing from 2016 to 2025. Data sources include peer-reviewed journals (e.g., Springer, Frontiers, Nature), open-access repositories (e.g., arXiv), blogs, case studies, white papers from quantum computing companies, and government publications. The search strategy employed keywords such as 'quantum computing applications,' 'quantum computing use case,' 'quantum technology cooperation,' 'quantum computing limitations,' and 'quantum computing initiatives.' Inclusion criteria focused on studies published between 2016 and 2025 that address experimental and commercial use cases of quantum computing, while excluding non-peer-reviewed or non-English publications. The synthesis method involves a thematic analysis of quantum computing applications across industries, government initiatives, and inter-governmental collaborations, along with a classification taxonomy of challenges and ethical concerns.

**Algorithms used:** Harrow–Hassidim–Lloyd (HHL), Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Grover's algorithm, Quantum Gradient Descent (QGD), Quantum Support Vector Machine (QSVM), Variational Quantum Imaginary Time Evolution (VarQITE), Quantum Annealing, Shor’s algorithm, Quantum Neural Networks (QNNs), Quantum-inspired Recurrent Neural Networks (QRNNs), Quantum Machine Learning (QML), Quantum Convolutional Neural Networks
**Frameworks:** Qiskit, D-Wave's constrained quadratic model (CQM) hybrid quantum solver, Ansys's LS-DYNA, Fire Opal (Q-CTRL), QasmSimulator (IBM)
## Findings
- [supported] Quantum computing has demonstrated practical applications across multiple industries, including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology, with quantified performance improvements in specific use cases
- [supported] Google's Willow quantum chip achieved real-time error correction on a superconducting system with 105 qubits, completing a computation in under five minutes that would take the world's fastest supercomputer an estimated 10^25 years
- [supported] D-Wave’s Advantage2 hybrid solver demonstrated the ability to solve problems with up to 2 million variable constraints, accessible via cloud service from over 40 countries as of 2025
- [supported] Caltech researchers built an array of 6,100 neutral atom qubits with 99.98% fidelity in single-qubit operations and maintained quantum coherence for about 13 seconds, showing progress toward scalable quantum computers
- [supported] A hybrid quantum-classical approach for precision agriculture in India achieved 96.26% prediction accuracy, 24-28% reductions in resource usage, and 24-26% yield improvements compared to classical methods like GWO
- [supported] The Australian Army and Q-CTRL reduced convoy deployment time by over two hours using a hybrid quantum-classical algorithm for logistics optimization, demonstrating a 12x increase in the likelihood of achieving optimal solutions
- [supported] HSBC and IBM demonstrated a quantum-enabled algorithm for bond trading that achieved up to 34% accuracy improvement over traditional approaches on production-scale trading data using IBM's Heron quantum processor
- [supported] Quantum-enhanced medical models achieved 97%+ accuracy in Alzheimer's detection (vs. 92% classical), 98% accuracy in skin lesion classification (vs. 81-97% classical), and 98.36% accuracy in knee osteoarthritis classification
- [supported] ExxonMobil and IBM's quantum optimization for LNG vessel routing demonstrated trade-offs between QAOA (better for sampling) and VQE (better for success rates with fewer samples) in solving combinatorial problems
- [supported] NTT DOCOMO achieved a 15% reduction in paging signals and enabled handling 20% more active devices using D-Wave’s hybrid quantum solver for telecommunication network optimization
- [supported] Volkswagen’s quantum-powered traffic-routing system in Lisbon reduced passenger waiting times by optimizing bus routes, and their quantum algorithm improved paint shop efficiency in manufacturing
- [supported] Origin Wukong, a 72-qubit quantum computer, improved AI model training with a 15% reduction in training loss for psychological counseling tasks and increased mathematical reasoning accuracy from 68% to 82%
- [supported] Quantum Key Distribution (QKD) technology, such as Toshiba’s Quantum Secure Metro Network, demonstrated resistance to cyber and quantum attacks by leveraging quantum physics for encryption
- [speculative] Quantum computing is argued to offer exponential computation power over classical computers for specific problem sets, with potential applications in solving problems intractable for classical systems
- [speculative] Quantum advantage is claimed to emerge in scenarios with millions of interdependent variables, such as energy sector optimization, where classical supercomputers may require years or centuries to solve
- [speculative] Quantum computing is proposed to revolutionize fields like renewable energy forecasting, grid management, and energy storage, though no empirical validation is provided for these claims
- [speculative] Quantum computing is suggested to accelerate drug discovery, genomic analysis, and personalized medicine, but specific performance claims lack empirical backing in this review
- [disputed] The claim that quantum computing has already outperformed classical computational power by a wide margin is disputed, as most cited examples are either simulations or limited to specific tasks without broad empirical validation
- [disputed] The assertion that quantum computers are transitioning from experiment to reality as a 'useful scientific tool' is disputed, given the reliance on hybrid approaches and the lack of large-scale, fault-tolerant quantum computers

**Results summary:** This review article synthesizes the state-of-the-art applications, initiatives, and challenges of quantum computing across industries up to 2025. Key findings highlight empirical successes in quantum computing, including Google's Willow chip achieving a computation intractable for classical supercomputers, D-Wave’s hybrid solver handling 2 million variable constraints, and Caltech’s 6,100-qubit array with high fidelity. Industry-specific applications demonstrate quantified performance improvements, such as 96.26% accuracy in precision agriculture, 34% better bond trading predictions, and 98%+ accuracy in medical diagnostics. Government initiatives and inter-governmental collaborations, with over $55.7 billion in global investment, underscore the strategic importance of quantum technology. However, the review also notes challenges like high development costs, limited accessibility, and ethical concerns, including cryptography risks and socioeconomic impacts. While quantum computing shows promise in solving complex problems, many claims of quantum advantage remain speculative or disputed due to reliance on simulations or hybrid approaches.

**Performance claims:**
- Google's Willow quantum chip: 105 qubits completed a computation in under 5 minutes vs. 10^25 years for classical supercomputers
- D-Wave’s Advantage2: Solves problems with up to 2 million variable constraints
- Caltech’s 6,100-qubit array: 99.98% fidelity in single-qubit operations, 13-second coherence
- Precision agriculture (India): 96.26% prediction accuracy, 24-28% resource reduction, 24-26% yield improvement
- Australian Army logistics: 2+ hour reduction in deployment time, 12x increase in optimal solution likelihood
- HSBC bond trading: 34% accuracy improvement over classical methods
- Alzheimer's detection: 97%+ accuracy (vs. 92% classical)
- Skin lesion classification: 98% accuracy (vs. 81-97% classical)
- Knee osteoarthritis classification: 98.36% accuracy
- NTT DOCOMO telecommunication: 15% reduction in paging signals, 20% more active devices supported
- Volkswagen traffic routing: Reduced passenger waiting times
- Origin Wukong AI model: 15% reduction in training loss, 68% to 82% accuracy improvement in mathematical reasoning
## Quantum advantage claim
**Classification:** theoretical

The review presents several empirical demonstrations of quantum computing outperforming classical systems on specific tasks (e.g., Google's Willow chip, D-Wave’s hybrid solver). However, these examples are limited to narrow problem sets and often rely on hybrid quantum-classical approaches or simulations. The broader claim of quantum advantage is classified as theoretical, as it hinges on the potential for exponential speedups in solving problems intractable for classical computers, but this has not been empirically validated at scale or for general-purpose computing.
## Limitations
- [inferred] Search coverage may be limited to English-language publications, excluding non-English research
- [inferred] Grey literature (e.g., technical reports, preprints not indexed in major databases) may be excluded due to inclusion criteria
- Exclusion of non-peer-reviewed sources (e.g., blogs, case studies without official citations) may omit emerging industry practices
- [inferred] Recency bias: Focus on 2016–2025 may overlook foundational work predating this period
- High development cost of quantum computers limits accessibility and scalability
- Quantum computers are applicable only to a limited number of complex problems, restricting their broader utility
- Limited accessibility of quantum computing services, available physically or online in only a handful of countries
- Shortage of specialized workforce with expertise in quantum technology
- [inferred] Lack of empirical validation for many proposed quantum applications in finance (e.g., portfolio optimization, risk analysis)
- [inferred] Overreliance on vendor-provided case studies (e.g., D-Wave, IBM) may introduce bias in reported outcomes
- [inferred] No direct comparison of quantum solutions with state-of-the-art classical methods in some domains (e.g., finance)
- Quantum algorithms like Shor’s pose cryptographic risks to current encryption methods (e.g., RSA), threatening data security
- [inferred] Ethical concerns (e.g., military applications, job displacement) are discussed but lack actionable mitigation strategies
- [inferred] Environmental impact of energy-intensive quantum computing operations is noted but not quantified
## Open questions
- How will quantum computing perform in financial services with real-world, large-scale datasets beyond synthetic or small-scale tests?
- What are the long-term economic and operational trade-offs between quantum and classical solutions for financial optimization problems?
- How can quantum computing be integrated into existing financial infrastructure without disrupting legacy systems?
- What are the specific barriers to adopting quantum computing in finance (e.g., regulatory, technical, cost)?
- How will quantum computing impact global financial inequality, given its high resource requirements?
- What are the implications of quantum computing for financial privacy and security, particularly in light of cryptographic vulnerabilities?
- How can quantum computing be made more accessible to developing nations and smaller financial institutions?
- What are the ethical frameworks needed to govern quantum computing in finance (e.g., algorithmic bias, market manipulation)?
- How will quantum computing affect job displacement in financial services, and what reskilling initiatives are needed?
- What are the environmental trade-offs of quantum computing in finance compared to classical high-performance computing?

**Future work:**
- Expand research to include non-English publications and grey literature to broaden coverage of global quantum initiatives
- Conduct empirical studies to validate quantum computing applications in finance (e.g., portfolio optimization, fraud detection) with real-world data
- Develop hybrid quantum-classical frameworks tailored for financial services to bridge the gap between current capabilities and practical needs
- Investigate noise mitigation techniques and error correction methods to improve quantum computing reliability in finance
- Explore quantum-resistant cryptographic solutions to address security risks posed by quantum algorithms like Shor’s
- Assess the scalability of quantum computing for large-scale financial problems (e.g., real-time risk analysis, high-frequency trading)
- Study the socioeconomic impact of quantum computing in finance, including job displacement and skill requirements
- Develop ethical guidelines and regulatory frameworks for quantum computing in financial services
- Investigate the environmental impact of quantum computing and explore sustainable practices for its deployment
- Foster international collaborations to democratize access to quantum computing resources and expertise in finance
- Compare quantum computing performance with state-of-the-art classical methods in financial applications to identify true quantum advantage
- Explore the integration of quantum computing with emerging technologies (e.g., AI, blockchain) in financial services
## Key ideas
- #idea:quantum-advantage — Empirical demonstrations (e.g., Google’s Willow chip) show quantum advantage in specific benchmarks, with potential applications in financial modeling like portfolio-optimisation and derivatives-pricing
- #idea:quantum-advantage — Hybrid quantum-classical approaches (e.g., HSBC/IBM bond trading) achieve 34% accuracy improvement over classical methods, suggesting near-term quantum advantage in financial use cases like risk-modelling and asset-pricing
- #idea:near-term-feasibility — Hybrid VQC algorithms (e.g., QAOA, VQE) demonstrate near-term applicability in financial services, including bond trading and portfolio optimization
- #idea:hybrid-approach — D-Wave’s Advantage2 solves problems with up to 2 million variable constraints via hybrid solvers, highlighting practical scalability for financial optimization tasks like portfolio-optimisation and risk-modelling
- #idea:hybrid-approach — Quantum-enhanced models (e.g., hybrid quantum-ML) outperform classical methods in classification tasks, with applications in fraud-detection and credit-scoring
- #limitation:noise — Quantum algorithms in finance rely on NISQ devices, limiting solution quality due to hardware noise and qubit coherence issues, particularly in risk-modelling and derivatives-pricing
- #limitation:no-empirical-validation — Claims of quantum advantage in commercial applications (e.g., D-Wave’s 2M variable constraints) lack peer-reviewed validation for pure quantum advantage in financial contexts like high-frequency-trading and market-simulation
- #limitation:data-encoding — Hybrid approaches in finance (e.g., bond trading) may not scale to production-scale problems due to qubit constraints and data encoding costs, affecting high-frequency-trading and market-simulation
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum advantage in bond trading (34% accuracy improvement), but lacks benchmarking against state-of-the-art classical solvers, leaving quantum superiority disputed for portfolio-optimisation and derivatives-pricing
- #contradiction:scalability — While D-Wave’s Advantage2 solves 2M variable constraints, the reliance on hybrid solvers contradicts claims of pure quantum scalability for real-world financial problems like risk-modelling and asset-pricing
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
