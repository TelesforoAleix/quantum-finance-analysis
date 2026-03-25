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
- quantum-ML
- quantum-SVM
- variational
- grover
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: medium
relevance_phase3: low
source_type: review-article
source_type_confidence: high
step1_date: '2026-03-25T16:15:26.652831'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:15:30.001820'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:15:38.016511'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:16:09.158989'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:16:39.796942'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:16:53.645282'
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
- topic/high-frequency-trading
- method/HHL
- method/QAOA
- method/VQE
- method/quantum-annealing
- method/quantum-ML
- method/quantum-SVM
- method/variational
- method/grover
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'The State of Quantum Computing: Applications, Initiatives, Challenges and
  Ethical Concerns up to 2025'
topic_tags:
- quantum-cryptography
- high-frequency-trading
year: 2025
zotero_key: ''
---

## Abstract summary
This review synthesizes experimental and commercial applications of quantum computing across major industries between 2016 and 2025, including agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology. It also surveys government initiatives and inter-governmental collaborations supporting quantum technologies, and discusses current technical limitations, high development costs, workforce constraints, and ethical concerns such as cryptographic risk, military use, inequality of access, job displacement, and environmental impact.
## Methodology
The paper adopts a Systematic Literature Review (SLR) approach to synthesize global evidence on quantum computing applications, initiatives, challenges, and ethical concerns up to 2025. The review is explicitly structured around five research questions covering industrial applications, solved problems, government initiatives, inter-governmental cooperation, technical limitations, and ethical issues. The search draws on multiple source types rather than only academic databases, including peer-reviewed journals (e.g., Springer, Frontiers, Nature), open-access repositories such as arXiv, blogs/case studies/white papers from major quantum computing companies, and government publications. Search queries reportedly combined terms such as “quantum computing applications,” “quantum computing use case,” “quantum technology cooperation,” “quantum computing limitations,” and “quantum computing initiatives.” Inclusion criteria were studies published between 2016 and 2025 that focused on experimental and commercial use cases of quantum computing, while exclusion criteria removed articles lacking an official source or peer review and non-English publications. The synthesis is narrative and mapping-oriented: the author organizes findings by industry sectors (agriculture, defense, energy, finance, healthcare, infrastructure, manufacturing, and technology), and additionally compiles descriptive summaries of government funding initiatives, international cooperation agreements, challenges, limitations, and ethical concerns. No formal meta-analysis, quality appraisal protocol, PRISMA flow, or exact count of included studies is reported in the provided text.

**Algorithms used:** HHL, QAOA, VQE, Grover's algorithm, VQC, QGD, QSVM, quantum annealing, QNN, QRNN, VarQITE, Shor's algorithm
**Frameworks:** Qiskit
## Findings
- [supported] The review identifies finance as one of the major industry domains where quantum computing applications have emerged by 2025, alongside agriculture, defense, energy, healthcare, infrastructure, manufacturing, and technology.
- [supported] In financial services, the review highlights two main themes in the cited literature: quantum-secure transaction infrastructure via quantum tokens/QKD and quantum-enhanced trading optimization for bond markets.
- [supported] The review reports that Quantinuum and Mitsui demonstrated transmission of quantum tokens over a 10 km fiber-optic network in Tokyo for ultra-secure transaction verification, positioning no-cloning-based token schemes as a potential anti-forgery and anti-double-spending mechanism.
- [supported] The review reports that HSBC and IBM presented a quantum-enabled algorithm for algorithmic bond trading in European corporate bond markets, using IBM Heron hardware with Qiskit and classical computing on production-scale trading data.
- [supported] Across reviewed application areas, the paper’s synthesis suggests that near-term quantum use in industry is predominantly hybrid quantum-classical rather than fully quantum.
- [supported] The review suggests that many practical quantum applications across sectors, including finance, currently focus on optimization, machine learning, and secure communications rather than fault-tolerant large-scale quantum computation.
- [supported] A recurring theme across the reviewed literature is that current demonstrations are often proof-of-concept, pilot, or early commercial deployments rather than mature large-scale production systems.
- [supported] The review finds broad consensus that quantum computing remains constrained by high development cost, limited accessibility, hardware scaling challenges, and shortage of specialized workforce.
- [supported] The review identifies cryptography and privacy disruption as a major ethical concern, with Shor-type threats to conventional encryption motivating quantum-safe and quantum-secure financial communication approaches.
- [supported] The review notes strong global public-sector momentum behind quantum technology, citing worldwide government investment exceeding $55.7 billion by 2025 and multiple international cooperation agreements.
- [speculative] The paper frames quantum computing as capable of tackling problems beyond supercomputers and offering exponential computational power for selected tasks, but this is presented as a general proposition rather than established across financial-service workloads reviewed here.
- [speculative] The review implies that quantum computing could provide competitive advantage in financial services through better handling of real-time market conditions and risk assessment, though this depends on further scaling and broader validation.
- [disputed] The paper states that experimental quantum computation has been tested to outperform classical computational power by a wide margin and cites broad quantum advantage language; such generalization is disputed because advantage is benchmark- and task-specific in the wider literature.

**Results summary:** This review article synthesizes quantum computing applications from 2016 to 2025 across multiple industries and, for financial services, emphasizes two principal use cases: quantum-secure transaction mechanisms and quantum-enhanced trading optimization. It cites a 10 km Tokyo trial of quantum tokens by Quantinuum and Mitsui and an HSBC-IBM demonstration of quantum-enabled bond-trading optimization on IBM Heron hardware using hybrid workflows. The broader synthesis argues that most near-term industrial applications are hybrid quantum-classical, focused on optimization, machine learning, and secure communications, while also stressing persistent limitations such as cost, access, workforce shortages, and hardware immaturity. The review presents strong optimism about future impact, but many cross-sector claims remain based on pilots, vendor case studies, or early demonstrations rather than settled large-scale evidence.

**Performance claims:**
- 10 km quantum token transmission network in Tokyo for secure transaction verification
- Up to 34% accuracy improvement in bond-trade fill prediction versus traditional approaches on production-scale trading data
- Global government investment in quantum technologies exceeds $55.7 billion as of 2025
## Quantum advantage claim
**Classification:** speculative

As a review article, it summarizes external demonstrations and repeatedly suggests strategic or computational advantage, including in finance, but does not itself establish a general quantum advantage. The finance-specific evidence cited is limited to early hybrid demonstrations and vendor-reported case studies rather than broad, independently validated advantage across financial workloads.
## Limitations
- The review excludes non-English publications, introducing language bias.
- The review is limited to studies published between 2016 and 2025, so earlier foundational work and post-2025 developments are not covered.
- The source selection includes peer-reviewed journals, arXiv, blogs, case studies, white papers, and government publications, creating heterogeneous evidence quality across included sources.
- Although the exclusion criteria state that articles lacking official source or peer review were excluded, the references include company press releases, blogs, case studies, Medium posts, and ResearchGate items, indicating inconsistent application of inclusion/exclusion criteria.
- Many cited application examples rely on vendor or institutional case studies and press releases rather than independent peer-reviewed validation.
- The paper is broad and cross-sectoral, so finance-specific analysis is relatively shallow and limited to a small number of examples.
- The review does not report key SLR details such as search strings in full, screening counts, reviewer agreement, or a PRISMA-style flow, limiting reproducibility.
- The review does not present a formal quality appraisal or risk-of-bias assessment of included sources.
- The paper emphasizes successful use cases and quantified gains, but gives limited critical discussion of failed, null, or negative results.
- Author-stated limitation: quantum computers are highly expensive to develop and operate.
- Author-stated limitation: quantum computers are applicable only to a limited number of problems requiring extensive computational power.
- Author-stated limitation: quantum computers or quantum computing services are available physically or online only in a handful of countries.
- Author-stated limitation: there is a shortage of specialized workforce with expertise in quantum technology.
- Author-stated limitation: current devices still face stabilization and scaling challenges before reaching classical-computer-like scale.
- Author-stated limitation: current quantum devices have limitations in capturing chaotic dynamics in applications such as fusion modeling.
- Author-stated limitation: some proposed applications show early promise but have no real-world implementations yet.
- [inferred] The review likely has publication and publicity bias because highly visible industrial demonstrations and government announcements are easier to find than unpublished or unsuccessful projects.
- [inferred] Grey literature inclusion without systematic weighting may overstate maturity and performance claims, especially for commercial finance applications.
- [inferred] The review does not clearly distinguish quantum computing from adjacent quantum technologies such as QKD and atomic clocks, which may blur scope for readers focused strictly on computing applications.
- [inferred] No dedicated comparison framework is provided to assess whether reported quantum advantages in finance outperform state-of-the-art classical baselines under fair conditions.
- [inferred] Recency risk remains high because the field is evolving rapidly; claims labeled current up to 2025 may become outdated quickly.
## Open questions
- Which quantum computing applications across industries, especially finance, will translate from demonstrations into sustained production use?
- How much of the reported performance improvement in industrial and financial case studies comes from the quantum component versus the surrounding classical or hybrid pipeline?
- Under what conditions do quantum methods provide a genuine advantage over best-in-class classical optimization and machine learning methods in financial services?
- How scalable are current finance use cases, such as bond trading optimization and quantum token transmission, to broader market settings and larger transaction volumes?
- Can current and near-term hardware be stabilized and scaled enough to support reliable commercial deployment across major industries?
- Which classes of problems are truly suitable for quantum computing, and where are classical methods likely to remain superior?
- How can access disparities between wealthy nations/corporations and the rest of the world be reduced as quantum technologies mature?
- What governance and international coordination mechanisms are needed to manage military, cybersecurity, and privacy risks associated with quantum technologies?
- How should ethical concerns such as cryptographic disruption, labor displacement, and environmental impact be mitigated?
- What standards should be used to independently validate vendor-reported quantum performance claims?

**Future work:**
- Further research to stabilize and scale quantum computers for broader practical deployment.
- Development of improved quantum error correction and error mitigation methods.
- Expansion of hybrid quantum-classical approaches for near-term industrial applications.
- More real-world implementations of currently proposed applications that have only shown early promise.
- Broader international cooperation, workforce development, and capacity building in quantum technologies.
- Research addressing ethical concerns, including privacy, military use, access inequality, socioeconomic disruption, and environmental sustainability.
- Extension of quantum applications into additional sectors and more complex operational settings.
- [inferred] Conduct finance-specific systematic reviews focused on use cases such as trading, portfolio optimization, risk analysis, fraud detection, and secure payments rather than treating finance as one small subsection of a broad review.
- [inferred] Introduce formal evidence grading and source-quality assessment to separate peer-reviewed results from vendor claims and media reports.
- [inferred] Update the review regularly or convert it into a living review to keep pace with rapid developments.
- [inferred] Include non-English studies and a more systematic grey-literature strategy to reduce language and selection bias.
- [inferred] Benchmark reported quantum finance applications against strong classical baselines using transparent, reproducible evaluation protocols.
- [inferred] Investigate production-readiness questions in finance, including latency, regulatory compliance, integration with legacy systems, and robustness under noisy market conditions.
## Key ideas
- #idea:near-term-feasibility — The review portrays current finance applications as early-stage but practically oriented, centered on hybrid quantum-classical workflows rather than fault-tolerant quantum computing.
- #idea:hybrid-approach — The main finance example is HSBC/IBM bond-trading optimization using IBM Heron hardware with Qiskit plus classical computation on production-scale data.
- #idea:quantum-advantage — The paper reports vendor-linked evidence of improved bond-trade fill prediction (up to 34%), suggesting possible competitive benefit in trading applications, but only speculatively.
- #idea:hybrid-approach — Across sectors, including finance, the review argues that optimization, machine learning, and secure communications are the dominant near-term application modes.
- #idea:near-term-feasibility — Quantum-secure transaction infrastructure, including QKD/quantum-token demonstrations, is presented as one of the clearest finance-adjacent deployment paths.
- #idea:quantum-advantage — The review uses broad language about quantum outperforming classical systems on selected tasks, but does not establish this specifically for financial workloads.
## Contradictions
- The paper uses broad quantum-advantage language, yet its own finance evidence is limited to early hybrid demonstrations and vendor case studies; this creates a #contradiction:classical-vs-quantum because superiority over strong classical baselines is not shown.
- The review highlights practical finance use cases, but also emphasizes hardware immaturity, scaling challenges, and proof-of-concept status, creating a #contradiction:scalability between optimistic deployment narratives and current real-world readiness.
- The reported 34% improvement in bond-trade fill prediction is not accompanied by a transparent comparison framework against state-of-the-art classical methods, so claims of quantum superiority remain disputed.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
