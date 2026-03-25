# HHL

**Papers:** 14 | **Theoretical:** 1 | **Review:** 3

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2026_Prasad_QuantumAlgorithmsStochastic]] | 2026 | preprint | derivatives-pricing, asset-pricing, market-simulation | speculative | high |
| [[2025_Berkowitz_QuantumComputingMeets]] | 2025 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, asset-pricing | speculative | high |
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2026_Mahmod_StateQuantumComputing]] | 2025 | review-article | quantum-cryptography, high-frequency-trading | speculative | medium |
| [[2022_Dalzell_EndEndResource]] | 2024 | preprint | portfolio-optimisation | speculative | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, quantum-cryptography | speculative | medium |
| [[2022_Albareti_StructuredSurveyQuantum]] | 2022 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, market-simulation, quantum-cryptography | speculative | high |
| [[2022_Sun_PortfolioOptimizationBased]] | 2022 | conference-paper | portfolio-optimisation | theoretical | high |
| [[2021_Pistoia_QuantumMachineLearning]] | 2021 | preprint | asset-pricing, fraud-detection, credit-scoring, high-frequency-trading, derivatives-pricing, risk-modelling | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | speculative | medium |
| [[2019_Kerenidis_QuantumAlgorithmsPortfolio]] | 2019 | conference-paper | portfolio-optimisation | theoretical | high |
| [[2019_Li_ResearchQuantumComputing]] | 2019 | conference-paper | quantum-cryptography | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 10 |
| risk-modelling | 7 |
| derivatives-pricing | 6 |
| quantum-cryptography | 6 |
| asset-pricing | 5 |
| market-simulation | 3 |
| fraud-detection | 3 |
| credit-scoring | 3 |
| high-frequency-trading | 3 |

## Key Findings

- [supported] For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities (option prices, expected hitting times, moments) to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Quantum simulation of the Fokker-Planck equation achieves accuracy ε in time ˜O(d · log(1/ε)), compared to classical finite-difference solvers at O(n^{d+1}_s). — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Numerical simulations on small instances (e.g., 2D Black-Scholes, 3D Langevin) demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] Resource requirements for d-dimensional SDEs: ~150 qubits for d=10, ε=10⁻³, and δx=10⁻² in finance applications. — [[2026_Prasad_QuantumAlgorithmsStochastic]]
- [supported] The review identifies finance as one of the major industry domains where quantum computing applications have emerged by 2025, alongside agriculture, defense, energy, healthcare, infrastructure, manufacturing, and technology. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] In financial services, the review highlights two main themes in the cited literature: quantum-secure transaction infrastructure via quantum tokens/QKD and quantum-enhanced trading optimization for bond markets. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that Quantinuum and Mitsui demonstrated transmission of quantum tokens over a 10 km fiber-optic network in Tokyo for ultra-secure transaction verification, positioning no-cloning-based token schemes as a potential anti-forgery and anti-double-spending mechanism. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review reports that HSBC and IBM presented a quantum-enabled algorithm for algorithmic bond trading in European corporate bond markets, using IBM Heron hardware with Qiskit and classical computing on production-scale trading data. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] Across reviewed application areas, the paper’s synthesis suggests that near-term quantum use in industry is predominantly hybrid quantum-classical rather than fully quantum. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review suggests that many practical quantum applications across sectors, including finance, currently focus on optimization, machine learning, and secure communications rather than fault-tolerant large-scale quantum computation. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] A recurring theme across the reviewed literature is that current demonstrations are often proof-of-concept, pilot, or early commercial deployments rather than mature large-scale production systems. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review finds broad consensus that quantum computing remains constrained by high development cost, limited accessibility, hardware scaling challenges, and shortage of specialized workforce. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review identifies cryptography and privacy disruption as a major ethical concern, with Shor-type threats to conventional encryption motivating quantum-safe and quantum-secure financial communication approaches. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The review notes strong global public-sector momentum behind quantum technology, citing worldwide government investment exceeding $55.7 billion by 2025 and multiple international cooperation agreements. — [[2026_Mahmod_StateQuantumComputing]]
- [supported] The paper provides an end-to-end logical resource analysis of a quantum interior point method (QIPM) for second-order cone programming applied to portfolio optimization, including explicit circuit-level estimates for logical qubits, T-count, and T-depth. — [[2022_Dalzell_EndEndResource]]
- [supported] For a portfolio optimization instance with n = 100 assets and target precision ϵ = 10^-7, the authors estimate about 8 × 10^6 logical qubits, 7 × 10^29 total T gates, and 2 × 10^24 T-depth layers. — [[2022_Dalzell_EndEndResource]]
- [supported] The authors conclude that the analyzed QIPM is far from practical and would require fundamental improvements before yielding practical quantum advantage, citing large constant prefactors, poorly conditioned linear systems, and costly quantum state tomography. — [[2022_Dalzell_EndEndResource]]
- [supported] Numerical simulations on portfolio instances up to n = 120 suggest that both the Frobenius condition number κ_F and the inverse tomography precision ξ^-1 tend to grow with problem size n. — [[2022_Dalzell_EndEndResource]]
- [supported] The numerical experiments were performed by classical simulation of the algorithm and tomography noise, not on real quantum hardware. — [[2022_Dalzell_EndEndResource]]
- [supported] A simple row-normalization preconditioning scheme reduced the effective condition number by more than an order of magnitude for the portfolio optimization instances studied. — [[2022_Dalzell_EndEndResource]]
