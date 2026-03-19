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
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-19T14:10:04.922640'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T14:10:10.366585'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T14:10:28.177841'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T14:11:22.615979'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T14:11:47.594659'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T14:12:00.998041'
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
This review article provides a comprehensive overview of the current landscape of quantum computing, focusing on its experimental and commercial applications across diverse industries from 2016 to 2025. The paper systematically maps use cases, government initiatives, and inter-governmental collaborations while analyzing outcomes, limitations, and ethical concerns. It aims to synthesize global research to highlight how quantum computing is being leveraged to solve complex problems beyond classical computational capabilities.
## Methodology
This review article implements a Systematic Literature Review (SLR) approach to synthesize existing knowledge on the use cases of quantum computing globally across industries from 2016 to 2025. The methodology follows established guidelines for conducting structured reviews, ensuring reproducibility and comprehensiveness in the selection of sources. The review includes multiple data sources such as peer-reviewed journals (Springer, Frontiers, Nature), open-access repositories (arXiv), blogs, case studies, white papers from major quantum computing companies, and government publications. The search strategy combined keywords like 'quantum computing applications,' 'quantum computing use case,' 'quantum technology cooperation,' 'quantum computing limitations,' and 'quantum computing initiatives.' Inclusion criteria focused on studies published between 2016 and 2025 that address experimental and commercial use cases of quantum computing, while excluding non-peer-reviewed articles and non-English publications. The synthesis method involved classifying applications across various industries, analyzing government initiatives, and discussing challenges, limitations, and ethical concerns.

**Algorithms used:** Harrow–Hassidim–Lloyd (HHL), Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE), Grover's Algorithm, Variational Quantum Computing (VQC), Quantum Support Vector Machine (QSVM), Quantum Gradient Descent (QGD), Quantum Neural Networks (QNNs), Hybrid Adiabatic Quantum Computing, Variational Quantum Imaginary Time Evolution (VarQITE), Quantum Annealing, Shor’s Algorithm
**Frameworks:** Qiskit, D-Wave's Hybrid Solver, Fire Opal (Q-CTRL), Quantinuum's Quantum Origin, PennyLane (implied by hybrid quantum-classical approaches)

**Experimental setup:** The review discusses various experimental setups across different industries, including the use of IBM Eagle and IonQ hardware via the Qiskit framework for agricultural data analysis, D-Wave’s Advantage2 quantum computer for hybrid solver applications, IBM’s Heron quantum processor for financial bond trading optimization, and IonQ’s Aria and Forte processors for biomedical engineering simulations. Additionally, quantum simulators and real quantum processing units (QPUs) were utilized in several case studies, such as Google’s Sycamore and Willow quantum chips, and Caltech’s 6,100 neutral atom qubit array.

**Dataset:** The review mentions several datasets and real-world data used in quantum computing applications, including: (1) Agricultural datasets for crops like wheat and rice used in smart farming experiments; (2) MRI scans (6400 samples) for Alzheimer’s disease detection in healthcare; (3) PET imaging data for cancer characterization in radiomics; (4) Historical and real-time market data for bond trading optimization in finance; (5) LNG transportation data for maritime inventory routing optimization; (6) Telecommunication network data from NTT DOCOMO for paging signal optimization; (7) Psychological counseling dialogues and mathematical reasoning datasets for AI model fine-tuning.
## Findings
- [supported] Quantum computing has demonstrated experimental and commercial applications across diverse industries including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology as of 2025
- [supported] Google’s Sycamore and Willow quantum processors have shown quantum advantage in specific tasks, with Willow completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years
- [supported] D-Wave’s Advantage2 quantum computer can solve problems with up to 2 million variable constraints via hybrid solver, accessible online from over 40 countries
- [supported] Caltech researchers built an array of 6,100 neutral atom qubits with 99.98% fidelity in single-qubit operations and 13 seconds of quantum coherence, showing progress toward scalable quantum computers
- [supported] In agriculture, hybrid quantum-classical approaches achieved 96.26% prediction accuracy, 24-28% reductions in resource usage, and 24-26% yield improvements compared to classical methods for crops like wheat and rice
- [supported] The Australian Army and Q-CTRL reduced convoy deployment time by over two hours using hybrid quantum-classical optimization for logistics, demonstrating practical military applications
- [supported] HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications
- [supported] Quantum computing in healthcare achieved over 97% accuracy in Alzheimer’s detection (vs. 92% classical), 70-75.66% accuracy in cancer radiomics (vs. 69% classical), and 98% accuracy in dermatology skin lesion classification (vs. 81-97% classical)
- [supported] ExxonMobil and IBM optimized LNG vessel routing for 500+ ships using quantum algorithms, demonstrating quantum advantage in large-scale logistical problems
- [supported] NTT DOCOMO reduced paging signals by 15% and increased network capacity by 20% using D-Wave’s quantum solver, outperforming classical methods in telecommunication optimization
- [supported] Volkswagen demonstrated quantum-powered traffic routing in Lisbon, reducing passenger waiting times and improving traffic flow efficiency
- [supported] Quantum random number generation (Quantum Origin by Quantinuum) provides provably secure cryptographic keys, addressing vulnerabilities in traditional RNGs
- [supported] Global government investment in quantum technologies exceeds $55.7 billion as of 2025, with China ($10B+), Germany ($3.3B), and the US ($3B+) leading funding initiatives
- [speculative] Quantum computing may provide exponential speedups for solving large-scale linear equation systems in animal breeding and genetics using algorithms like HHL
- [speculative] Quantum advantage is expected to emerge in high-dimensional simulations for nuclear fusion research, though current devices struggle with chaotic dynamics
- [speculative] Quantum computing could revolutionize energy grid management, including renewable energy forecasting and demand prediction, but real-world implementations are still in early stages
- [speculative] Quantum computing may accelerate AI model training, with experiments showing 15% reduction in training loss and 14% accuracy improvement in mathematical reasoning tasks
- [disputed] Claims of quantum advantage in random circuit sampling (e.g., Google’s Willow) are contested due to debates over classical simulation feasibility and benchmark fairness

**Results summary:** This review article synthesizes the state-of-the-art applications of quantum computing across multiple industries up to 2025, highlighting both demonstrated successes and speculative potential. Key supported findings include quantum advantage in specific tasks (e.g., Google’s Willow processor), hybrid quantum-classical solutions achieving measurable improvements in agriculture (96.26% accuracy), finance (34% better bond trading predictions), healthcare (97%+ disease detection accuracy), and logistics (2-hour reduction in military deployment time). The paper also documents significant government investments ($55.7B globally) and commercial deployments (e.g., D-Wave’s 2M-variable solver). However, many applications remain speculative, particularly in areas like nuclear fusion and large-scale AI acceleration, while some quantum advantage claims face disputes over benchmark validity.

**Performance claims:**
- Google’s Willow quantum processor: 105 qubits, computation completed in <5 minutes vs. 10^25 years for classical supercomputer
- D-Wave’s Advantage2: Solves problems with up to 2 million variable constraints
- Caltech’s 6,100-qubit array: 99.98% single-qubit fidelity, 13 seconds coherence time
- Agriculture (smart farming): 96.26% prediction accuracy, 24-28% resource reduction, 24-26% yield improvement
- Australian Army logistics: 2+ hour reduction in deployment time vs. classical methods
- HSBC bond trading: 34% accuracy improvement over classical approaches
- Healthcare (Alzheimer’s detection): 97%+ accuracy vs. 92% classical
- Healthcare (radiomics): 70-75.66% accuracy vs. 69% classical
- Healthcare (dermatology): 98% skin lesion classification accuracy vs. 81-97% classical
- ExxonMobil LNG routing: Optimization for 500+ vessels with quantum algorithms
- NTT DOCOMO: 15% reduction in paging signals, 20% increase in network capacity, 40-second solution time vs. >1 day classical
- Volkswagen traffic routing: Reduced passenger waiting times in Lisbon
- Quantum AI (China): 15% reduction in training loss, 14% accuracy improvement (68%→82%) in mathematical reasoning
## Quantum advantage claim
**Classification:** speculative

While the paper cites multiple instances of quantum processors outperforming classical systems (e.g., Google’s Willow, D-Wave’s Advantage2), these claims are primarily based on simulations or specialized benchmarks. Most demonstrated advantages are either task-specific (e.g., random circuit sampling) or achieved via hybrid quantum-classical approaches. The review notes that scalable, general-purpose quantum advantage remains unproven, with many applications still in early experimental or proof-of-concept stages. Some claims (e.g., Google’s 2019 quantum supremacy) are explicitly disputed in the broader literature.
## Limitations
- Search coverage may be limited to studies published between 2016–2025, potentially excluding earlier foundational work or emerging trends beyond this timeframe [inferred]
- Exclusion of non-English publications introduces language bias, potentially overlooking relevant research from non-English-speaking regions [inferred]
- Grey literature (e.g., technical reports, dissertations, non-peer-reviewed industry documents) is excluded, which may omit practical insights or emerging applications [inferred]
- Reliance on peer-reviewed journals, open-access repositories, and industry whitepapers may introduce selection bias toward well-documented or commercially promoted use cases [inferred]
- The review focuses on experimental and commercial use cases but may not fully capture theoretical advancements or niche applications in financial services [inferred]
- High development cost of quantum computers limits accessibility and scalability, particularly for smaller organizations or developing nations (author-stated)
- Quantum computers are applicable only to a limited number of complex problems, restricting their utility in domains where classical solutions suffice (author-stated)
- Limited accessibility of quantum computing services, available physically or online in only a handful of countries (author-stated)
- Shortage of specialized workforce with expertise in quantum technology hinders widespread adoption and innovation (author-stated)
- [inferred] Lack of detailed comparative analysis between quantum and classical solutions for financial services use cases (e.g., portfolio optimization, risk analysis)
- [inferred] No discussion on the reproducibility of results from industry whitepapers or proprietary case studies (e.g., HSBC-IBM bond trading, D-Wave applications)
- [inferred] Limited exploration of hardware-specific constraints (e.g., qubit count, error rates) in financial applications, despite their critical impact on performance
## Open questions
- How will quantum computing perform in financial services when scaled beyond current qubit limitations (e.g., >1000 qubits)?
- What are the long-term economic and operational trade-offs between hybrid quantum-classical approaches and purely classical solutions in finance?
- How can quantum computing be integrated into existing financial infrastructure without disrupting legacy systems?
- What are the specific noise mitigation techniques required to achieve reliable results in financial modeling on near-term quantum hardware?
- How will quantum computing impact regulatory frameworks in financial services, particularly for risk assessment and fraud detection?
- What are the implications of quantum computing for financial inclusion, given its high cost and limited accessibility?
- How can the financial services industry address the shortage of quantum-literate professionals to accelerate adoption?
- What are the potential unintended consequences of quantum computing in finance, such as market manipulation or systemic risks?

**Future work:**
- Expand research to include multi-period portfolio optimization and dynamic risk assessment in financial services
- Develop standardized benchmarks for comparing quantum and classical solutions in finance (e.g., Monte Carlo simulations, option pricing)
- Investigate noise-resilient quantum algorithms tailored for financial applications to improve practical performance
- Explore quantum machine learning techniques for fraud detection and real-time market analysis
- Assess the feasibility of quantum-secure cryptographic protocols for financial transactions to mitigate post-quantum threats
- Conduct longitudinal studies on the cost-effectiveness of quantum computing in finance, including hardware and operational expenses
- Develop educational and training programs to address the quantum skills gap in the financial sector
- Investigate inter-governmental and public-private partnerships to democratize access to quantum computing resources for financial institutions
- Explore the integration of quantum computing with emerging technologies (e.g., blockchain, IoT) for innovative financial products
- Address ethical concerns related to quantum computing in finance, such as data privacy, algorithmic bias, and equitable access
## Key ideas
- #idea:quantum-advantage — Empirical demonstrations (e.g., Google’s Willow) show quantum advantage in specific benchmarks like random circuit sampling, with potential implications for financial modeling
- #idea:quantum-advantage — Hybrid quantum-classical approaches (e.g., HSBC/IBM bond trading) achieve 34% accuracy improvement over classical methods in real-time market data processing, suggesting near-term quantum advantage in finance
- #idea:near-term-feasibility — Hybrid VQC algorithms demonstrate near-term applicability in industry, including financial use cases like bond trading and portfolio optimization
- #idea:hybrid-approach — D-Wave’s Advantage2 solves problems with up to 2 million variable constraints via hybrid solvers, highlighting practical scalability for financial optimization tasks (e.g., portfolio-optimisation, risk-modelling)
- #idea:hybrid-approach — Quantum-enhanced models (e.g., hybrid quantum-ML) outperform classical methods in classification tasks, with potential applications in fraud-detection and credit-scoring
- #limitation:noise — Quantum algorithms in finance rely on NISQ devices, limiting solution quality due to hardware noise and qubit coherence issues, particularly in risk-modelling and derivatives-pricing
- #limitation:no-empirical-validation — Claims of quantum advantage in commercial applications (e.g., D-Wave’s 2M variable constraints) are disputed due to lack of peer-reviewed validation for pure quantum advantage in financial contexts
- #limitation:data-encoding — Hybrid approaches in finance (e.g., bond trading) may not scale to production-scale problems due to qubit constraints and data encoding costs, affecting high-frequency-trading and market-simulation
## Contradictions
- #contradiction:classical-vs-quantum — The paper claims quantum advantage in bond trading (34% accuracy improvement), but lacks benchmarking against state-of-the-art classical solvers, leaving quantum superiority disputed for portfolio-optimisation and derivatives-pricing
- #contradiction:scalability — While D-Wave’s Advantage2 solves 2M variable constraints, the reliance on hybrid solvers contradicts claims of pure quantum scalability for real-world financial problems like risk-modelling and asset-pricing
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
