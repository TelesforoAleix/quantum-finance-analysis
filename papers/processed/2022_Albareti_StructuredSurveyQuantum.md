---
aliases:
- A Structured Survey of Quantum Computing for the Financial Industry
- Structured Survey Quantum Computing
authors:
- Franco D. Albareti
- Thomas Ankenbrand
- Denis Bieri
- Esther Hänggi
- Damian Lötscher
- Stefan Stettler
- Marcel Schöngens
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
journal_or_venue: arXiv
methodology_tags:
- QAOA
- VQE
- quantum-annealing
- HHL
- amplitude-estimation
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:56:16.696661'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:56:21.782784'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:56:34.956651'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:57:08.809752'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:58:05.220506'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:58:27.135759'
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
- topic/market-simulation
- topic/quantum-cryptography
- method/QAOA
- method/VQE
- method/quantum-annealing
- method/HHL
- method/amplitude-estimation
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: A Structured Survey of Quantum Computing for the Financial Industry
topic_tags:
- portfolio-optimisation
- risk-modelling
- derivatives-pricing
- market-simulation
- quantum-cryptography
year: 2022
zotero_key: ''
---

## Abstract summary
The paper surveys proposed applications of quantum computing in financial services, focusing on optimization, simulation/Monte Carlo, and (to a lesser extent) machine learning. It introduces a layered framework that links financial use cases (e.g., portfolio optimization, transaction settlement, derivative pricing, risk measurement, crash prediction) to methodologies, quantum algorithms, and hardware types, and applies this to 13 peer-reviewed studies. The authors also discuss the current state and limitations of quantum hardware and software, emphasizing that while some prototype implementations exist, substantial advances in qubit scale and error rates are needed before large-scale practical impact in finance is realized.
## Methodology
This paper is a preprint survey/review rather than an original empirical study, and it explicitly proposes a structured review methodology for analyzing quantum computing applications in finance. The authors conduct a literature search using Google Scholar as the main source, apply exclusion criteria to remove panel introductions, non-English/non-German papers, and teaching or pedagogical papers, and then retain only papers that describe a concrete financial application of quantum computing or its implementation on relevant hardware. They further restrict inclusion to peer-reviewed papers published by 2021, resulting in a final sample of 13 papers. To synthesize the literature, they introduce a layered analytical framework with four dimensions: (1) financial use case, (2) methodology category, (3) quantum algorithm, and (4) quantum hardware. They classify reviewed studies across use cases such as portfolio optimization, transaction settlement, derivative pricing, risk estimation, and crash prediction; methodologies such as optimization, Monte Carlo/simulation, and machine learning; algorithms including HHL, QAE/QPE, QAOA, VQE, QUBO-based approaches, and QIPM; and hardware categories including gate-based quantum computers and quantum annealers. The paper then applies this taxonomy descriptively to the 13 selected studies using counts, tables, and a morphological box rather than conducting new experiments. As a preprint, it should be flagged accordingly.

**Algorithms used:** HHL, QAE, QPE, QPA, QAOA, VQE, QUBO, qPCA, QIPM
**Frameworks:** Qiskit, Cirq, ProjectQ, pyQuil, Quantum Development Kit, Amazon Braket SDK, QCompute, XACC
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The survey identifies optimization and Monte Carlo/simulation as the dominant quantum computing application areas in finance, with no peer-reviewed finance use cases found for quantum machine learning by 2021.
- [supported] Among the 13 selected papers reviewed, 5 address portfolio optimization, 3 derivative pricing, 2 risk estimation, 2 financial crash prediction, and 1 transaction settlement.
- [supported] Of the 13 reviewed papers, 8 use optimization methodologies, 5 use Monte Carlo methods, and 0 use machine learning.
- [supported] Of the reviewed implementations, 9 target gate-based quantum computers and 4 target quantum annealers.
- [speculative] Portfolio optimization is presented as a particularly promising finance use case for quantum computing, but the survey concludes that more research is needed to establish clear practical benefit for industry.
- [speculative] For unconstrained portfolio optimization, HHL-based approaches are claimed to offer poly(log N) runtime versus poly(N) classical scaling, but this depends on strong assumptions and is not demonstrated end-to-end in practice.
- [supported] In portfolio optimization on quantum annealers, current devices were reported to approach the performance of commercial solvers on small example instances.
- [supported] In one reviewed portfolio optimization study, optimized reverse quantum annealing was reported to be more than 100 times faster on average than forward quantum annealing.
- [speculative] For constrained portfolio optimization reduced to SOCPs, quantum interior-point methods are claimed to scale better than classical complexity, but the speedup depends on problem-specific parameters.
- [supported] For portfolio rebalancing, simulator experiments highlighted the importance of input scaling for QAOA-like methods and showed performance advantages of the quantum alternating operator ansatz over the compared QUAO approach.
- [supported] For transaction settlement, a hybrid quantum-classical heuristic was shown on cloud-based quantum hardware for mixed binary optimization instances, extending VQE/QAOA-style methods beyond standard QUBO formulations.
- [speculative] Quantum amplitude estimation is presented as the main source of potential advantage for derivative pricing and risk analysis, with a theoretical quadratic reduction in sample complexity relative to classical Monte Carlo.
- [supported] In option pricing experiments on real quantum hardware, a simple error mitigation scheme reduced average pricing error over initial spot prices from 62% to 21%.
- [supported] Reviewed derivative pricing experiments found that current hardware is limited by readout errors, circuit execution errors, gate fidelity, connectivity, and qubit count.
- [supported] For risk analysis, a small two-asset example for VaR/CVaR estimation was implemented on real gate-based quantum hardware, but the example was too simple for industry relevance.
- [speculative] Practical quantum advantage for risk analysis is pushed further out because classical Monte Carlo can be massively parallelized, raising the threshold for outperforming classical systems.
- [supported] For financial crash prediction, the reviewed work formulated the problem as a QUBO and implemented it on a quantum annealer, but larger and more relevant networks require next-generation processors.
- [speculative] The survey concludes that breakthroughs in hardware—especially more qubits and lower error rates—are necessary before the full potential of quantum finance algorithms can be realized.
- [speculative] The paper argues that faster derivative pricing could improve market liquidity and more accurate risk estimation could improve financial stability, but these impacts are not empirically established in the survey.

**Results summary:** This preprint is a structured survey rather than an original empirical study. It reviews 13 peer-reviewed papers on quantum computing in finance published through 2021 and organizes them by use case, methodology, algorithm, and hardware. The surveyed literature is concentrated in portfolio optimization, derivative pricing, risk estimation, transaction settlement, and financial crash prediction, with optimization and Monte Carlo methods dominating and no peer-reviewed finance applications of quantum machine learning identified. The survey reports that some small-scale experiments have been run on real gate-based devices and quantum annealers, including option pricing and risk-analysis toy examples, but current hardware limitations remain severe. The strongest recurring performance claim across the reviewed literature is a theoretical quadratic sample-complexity advantage from quantum amplitude estimation for Monte Carlo-style finance tasks; however, the survey emphasizes that practical, end-to-end quantum advantage in financial services has not yet been established and remains dependent on substantial hardware and algorithmic advances.

**Performance claims:**
- 13 peer-reviewed papers selected and analyzed
- 5 papers on portfolio optimization, 3 on derivative pricing, 2 on risk estimation, 2 on financial crash prediction, 1 on transaction settlement
- 8 papers use optimization methodologies, 5 use Monte Carlo, 0 use machine learning
- 9 implementations target gate-based quantum computers, 4 target quantum annealers
- HHL-based unconstrained portfolio optimization claimed runtime scaling of poly(log N) versus poly(N) classically
- Reverse quantum annealing reported as more than 100 times faster on average than forward quantum annealing in one portfolio optimization study
- Quantum amplitude estimation claimed quadratic sample-complexity improvement for derivative pricing/risk estimation
- For desired error epsilon, the survey states classical methods require O(1/epsilon^2) samples while the quantum method requires O(1/epsilon) samples
- Option pricing error mitigation reduced average error from 62% to 21% over initial spot prices
- A real-hardware VaR/CVaR example involved only 2 assets
## Quantum advantage claim
**Classification:** speculative

As a preprint survey, the paper mainly summarizes theoretical and early experimental claims from prior literature. It highlights theoretical advantages such as quadratic sample-complexity improvements from amplitude estimation and possible better scaling for some optimization methods, but it does not demonstrate practical end-to-end quantum advantage in finance and repeatedly notes current hardware limitations.
## Limitations
- As a preprint, the survey has not undergone peer review.
- The literature selection excludes papers not available in English or German, introducing potential language bias.
- The review relies primarily on Google Scholar as the main search source, which may miss relevant studies indexed elsewhere.
- The final sample is restricted to papers published by 2021, so more recent developments are not covered.
- The survey excludes quantum-inspired approaches such as tensor networks, narrowing scope.
- The review includes only papers that describe a concrete application or implementation, potentially omitting relevant conceptual or methodological work.
- The selected sample contains only 13 papers, limiting comprehensiveness.
- No machine-learning finance use case papers were found in the selected sample, leaving that area underrepresented.
- Current quantum hardware is a major limitation across surveyed applications: more qubits are needed and hardware errors must be reduced.
- Many current quantum architectures have limited qubit connectivity, coherence constraints, and scalability challenges.
- Classical simulation of quantum systems is exponentially expensive and only feasible for small systems.
- Software workarounds such as swap operations increase circuit depth and noise, which can make algorithms unusable in practice.
- Quantum error correction requires substantial additional qubits, creating large overhead before practical fault-tolerant use is possible.
- It remains uncertain whether current leading quantum technologies will scale to future large-scale quantum computers.
- For many proposed finance applications, there is no rigorous end-to-end assessment showing practical quantum advantage.
- For most problems, it remains open whether quantum computers truly outperform classical computers in practice.
- Many theoretical speedups depend on restrictive assumptions or problem formulations that may be hard to realize for realistic financial tasks.
- Quantum machine learning approaches often require full-scale quantum computers and possibly QRAM, which may be difficult to construct.
- Portfolio optimization results are limited because some approaches only handle unconstrained problems, whereas practical portfolios usually involve constraints.
- Binary/QUBO portfolio formulations only allow assets to be included or excluded, limiting practical realism compared with arbitrary portfolio weights.
- For reverse annealing portfolio optimization, the theoretical speedup over classical methods is unclear.
- For constrained portfolio optimization via SOCP/QIPM, the reported speedup depends on problem-dependent parameters.
- Portfolio rebalancing experiments were run on ideal simulators, limiting conclusions about real-hardware performance.
- For portfolio rebalancing approaches such as QAOA/quantum alternating operator ansatz, the theoretical speedup over classical methods is not yet clear.
- Transaction settlement experiments address only part of the full settlement problem.
- Derivative pricing experiments on real hardware are strongly affected by readout and circuit execution errors.
- Practical derivative pricing would require much larger quantum devices with more qubits and deeper reliable circuits than currently available.
- Risk analysis demonstrations use only very small examples, e.g. two-asset cases, with low complexity and without nonlinear payoff structures.
- Monte Carlo methods are massively parallelizable classically, raising the threshold for practical quantum advantage in risk analysis.
- Credit risk and economic capital estimation circuit-depth requirements are well beyond current gate-based hardware capabilities.
- Financial crash prediction implementations require next-generation processors or problem-specific annealers for industry-relevant network sizes.
- The financial crash prediction approach has not yet been shown to predict crashes with high confidence on historical data.
- There is little literature estimating the actual economic impact, timing, and operating cost of quantum computing in finance.
- [inferred] The survey does not describe a systematic review protocol in full detail (e.g., search strings, screening workflow, inter-rater procedures), which may limit reproducibility.
- [inferred] Restricting inclusion to peer-reviewed papers while the survey itself is a preprint may create inconsistency in evidentiary standards.
- [inferred] The review does not appear to assess study quality or risk of bias for included papers.
- [inferred] There is limited discussion of comparisons against state-of-the-art classical baselines across the surveyed applications.
- [inferred] Many cited advantages are theoretical or based on toy problems, limiting external validity for production financial services settings.
## Open questions
- Which financial problems can actually be solved efficiently on quantum computers, as opposed to only theoretically?
- For which problems are current and near-term quantum computers genuinely useful once hardware constraints are taken into account?
- Whether quantum computers have a practical advantage over classical computers for most finance problems remains open.
- Can noisy intermediate-scale quantum devices deliver useful financial applications before fault-tolerant quantum computing arrives?
- When will quantum computing significantly impact the financial services industry?
- What will be the cost of maintaining and operating quantum computing infrastructure for financial applications?
- Can QUBO-based portfolio optimization be adapted to allow arbitrary asset weights rather than binary inclusion decisions?
- What theoretical speedup, if any, can reverse quantum annealing portfolio optimization achieve over classical approaches?
- Can QAOA or quantum alternating operator ansatz provide a genuine quantum advantage for portfolio rebalancing?
- How can quantum linear system solvers and quantum linear algebra be redesigned to reduce hardware requirements for optimization?
- Can practical constrained portfolio optimization achieve robust speedups under realistic market constraints?
- How can mixed binary optimization methods be extended to cover the full real-world transaction settlement problem?
- Will problem-specific variational forms materially improve transaction settlement performance?
- Can quantum derivative pricing achieve practical relevance on real hardware with acceptable error rates?
- How much can error mitigation or error correction improve option pricing accuracy in realistic settings?
- Can qPCA-based approaches scale to full Heath-Jarrow-Morton simulations for interest-rate derivatives?
- How many qubits and what circuit depths are needed before risk measures such as VaR, CVaR, and economic capital become practically tractable?
- Can quantum risk analysis outperform highly parallel classical Monte Carlo in real production environments?
- Can the proposed nonlinear network model for financial crash prediction reliably predict crashes with high confidence?
- How well do quantum crash-prediction methods perform under back-testing on historical financial data?
- Why are there no identified quantum machine learning finance papers in the selected sample despite the importance of machine learning in finance?

**Future work:**
- Develop larger, less noisy quantum hardware with more qubits and better connectivity to realize the potential of finance applications.
- Advance quantum software and algorithms to reduce qubit requirements and circuit depth for financial use cases.
- Investigate whether noisy intermediate-scale quantum computers can support practically useful finance applications in the near term.
- Conduct more rigorous end-to-end analyses of quantum advantage for financial applications.
- Expand research on quantum machine learning applications in finance, an area identified as missing in the surveyed literature.
- Extend portfolio optimization methods to more realistic constrained settings relevant to practice.
- Adapt QUBO-based portfolio methods so that assets can be weighted arbitrarily rather than selected only in binary form.
- Clarify the theoretical and practical speedup of reverse annealing and other portfolio optimization approaches relative to classical methods.
- Further investigate critical steps needed for QAOA and quantum alternating operator ansatz to achieve quantum advantage in portfolio rebalancing.
- Develop improved quantum linear system solvers and linear algebra methods with reduced hardware demands.
- Further develop transaction settlement algorithms to represent the full settlement problem rather than only a subset.
- Explore problem-specific variational forms, such as QAOA-inspired ansätze, to improve mixed binary optimization performance.
- Test derivative pricing methods on larger quantum hardware capable of deeper circuits and more qubits.
- Improve and apply error mitigation and eventually error correction for derivative pricing experiments.
- Develop a general quantum algorithm to fully simulate the Heath-Jarrow-Morton model for pricing interest-rate derivatives.
- Reduce qubit counts and circuit depth for risk analysis algorithms so they become feasible on earlier hardware generations.
- Scale risk analysis from toy examples to industry-relevant portfolios with nonlinear payoff structures.
- Build next-generation or problem-specific quantum annealers for larger financial network crash-prediction problems.
- Validate financial crash prediction approaches through back-testing on historical data.
- Study the economic viability and cost-effectiveness of operating quantum computing for financial services.
- [inferred] Update the survey with post-2021 literature to reflect the rapidly evolving state of quantum computing in finance.
- [inferred] Broaden future reviews to include additional databases, grey literature, and non-English studies where feasible.
- [inferred] Incorporate formal quality assessment and reproducible systematic-review procedures in future survey work.
- [inferred] Benchmark proposed quantum finance methods more consistently against strong classical baselines and production-relevant datasets.
## Key ideas
- #idea:hybrid-approach — The paper proposes a four-layer survey framework linking financial use cases, methodology classes, quantum algorithms, and hardware to organize quantum-finance literature.
- #idea:quantum-advantage — It synthesizes theoretical advantage claims for HHL-style portfolio optimisation, QAE-based derivative pricing and risk estimation, and quantum interior-point methods, especially asymptotic speedups under strong assumptions.
- #idea:near-term-feasibility — The survey concludes that current NISQ hardware restricts demonstrated finance applications to toy or small benchmark instances because of qubit, noise, connectivity, and depth limitations.
- #idea:hybrid-approach — Hybrid quantum-classical workflows dominate practical optimisation studies, including QAOA/VQE-style methods, annealer-based QUBO formulations, and mixed-binary transaction-settlement heuristics.
- #idea:quantum-advantage — Quantum amplitude estimation is identified as the main recurring source of potential advantage in finance via quadratic Monte Carlo sample-complexity improvement for pricing and risk tasks.
- #idea:near-term-feasibility — The paper emphasizes that no end-to-end practical quantum advantage in financial services has yet been established in the reviewed peer-reviewed literature.
- #idea:near-term-feasibility — It finds no peer-reviewed finance applications of quantum machine learning in the selected literature through 2021, despite broader interest in ML for finance.
- #idea:quantum-advantage — The survey reports annealing-based portfolio studies with competitive small-instance performance and one reverse-annealing result over 100 times faster than forward annealing, while noting this is not evidence of superiority over classical methods.
- #idea:near-term-feasibility — For risk modelling and derivative pricing, the survey stresses that classical Monte Carlo parallelism and variance-reduction methods raise the bar for realizing practical quantum advantage.
- #idea:quantum-advantage — The paper also notes financial relevance of quantum threats to existing cryptography, motivating post-quantum or quantum-safe financial infrastructure discussions.
## Contradictions
- The survey summarizes many prospective quantum speedup claims in portfolio optimisation, derivatives pricing, and risk modelling, but concludes that none of the reviewed papers demonstrates empirically validated end-to-end quantum superiority over strong classical baselines on realistic financial problems.
- Claims of favorable asymptotic scaling for HHL, quantum interior-point methods, qPCA-related simulation, and amplitude-estimation-based finance workflows are contradicted by the survey's assessment that data-loading assumptions, circuit depth, qubit requirements, and error rates make these approaches impractical on current hardware.
- Annealing and variational portfolio-optimisation studies report promising small-instance results, yet the survey argues that embedding overhead, binary/QUBO simplifications, qubit limits, and noise undermine extrapolation to industry-scale constrained portfolios.
- For QAE-based pricing and risk analysis, theoretical quadratic sample-complexity gains are tempered by the survey's observation that classical Monte Carlo is massively parallelizable and highly optimized, contradicting simplistic narratives of clear practical quantum advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
