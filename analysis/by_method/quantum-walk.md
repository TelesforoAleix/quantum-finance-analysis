# Quantum Walk

**Papers:** 8 | **Empirical:** 1 | **Theoretical:** 1 | **Review:** 1

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Ferro_DUpdateReview]] | 2023 | technical-report | derivatives-pricing, risk-modelling, asset-pricing | theoretical | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | preprint | portfolio-optimisation | speculative | high |
| [[2022_Wang_ClassicallyBoostedQuantum]] | 2022 | preprint | portfolio-optimisation | speculative | medium |
| [[2021_Slate_QuantumWalkBased]] | 2021 | peer-reviewed-empirical | portfolio-optimisation | speculative | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | other | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 7 |
| risk-modelling | 4 |
| derivatives-pricing | 3 |
| asset-pricing | 3 |
| fraud-detection | 2 |
| credit-scoring | 2 |
| quantum-cryptography | 2 |
| market-simulation | 1 |
| high-frequency-trading | 1 |

## Key Findings

- [supported] The review identifies portfolio optimization for mutual funds as a central NP-hard/combinatorial finance problem and synthesizes classical and quantum machine learning approaches applied to it. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The authors state that the literature search examined 44 papers from 2003 to 2023 for the review scope, while also reporting a broader survey corpus of 87 papers, indicating some inconsistency in corpus reporting. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review finds that most relevant papers use stocks or equities rather than actual mutual fund datasets, and identifies this as a major gap in the literature on mutual fund portfolio optimization. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review reports that quantum machine learning is a developing field, with approximately 67.81% of the collected papers published between 2019 and 2023. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Among machine-learning applications in quantitative finance, the review highlights return forecasting, portfolio design, and risk modeling as the most common use cases in the surveyed literature. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] For portfolio construction, multilayer perceptrons are identified as the most commonly used classical ML technique in the reviewed papers, followed by random forests/decision trees, LSTM, SVM, and Gaussian process regression. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review concludes that classical ML approaches for portfolio optimization face limitations including long training/simulation times, high computational cost, curse of dimensionality, and difficulty handling discrete constraints. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review identifies hybrid quantum-classical methods as the dominant near-term approach for portfolio optimization because current quantum hardware lacks enough high-quality qubits for fully quantum large-scale optimization. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Quantum annealing and QUBO formulations are presented in the reviewed literature as the main practical quantum approaches for NP-hard portfolio optimization problems. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review notes that benchmark classical comparators used in prominent quantum portfolio optimization papers include genetic algorithms, simulated annealing, Gekko, and exhaustive solvers. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review highlights research gaps including limited NISQ performance, difficulty validating noisy quantum outputs, constraints on applying quantum linear algebra methods, and unresolved issues in error correction, coherence time, and qubit stability. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The review finds that the specific application of quantum machine learning to mutual fund portfolio optimization remains underexplored despite perceived potential. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The report concludes that there have been no major breakthroughs in quantum computing for derivatives pricing and VaR since the prior 2022 review; most recent work is incremental and focused on adapting established methods to NISQ constraints. — [[2023_Ferro_DUpdateReview]]
- [supported] The report emphasizes that many proposed pricing and VaR algorithms require more qubits, lower noise, and deeper circuits than current hardware can support, making practical deployment difficult on present-day devices. — [[2023_Ferro_DUpdateReview]]
- [supported] For state initialization, no reviewed algorithm satisfies all desirable properties simultaneously (efficiency, robustness to noise, controllable precision, determinism, efficient compilation, phase preservation, and low ancilla use). — [[2023_Ferro_DUpdateReview]]
- [supported] Under NISQ constraints, approximate or variational state-preparation methods can outperform exact loading methods in practice because shorter circuits reduce noise accumulation. — [[2023_Ferro_DUpdateReview]]
- [supported] The report identifies noise, rather than qubit count alone, as the dominant practical limitation in many real-hardware experiments for finance-relevant quantum algorithms. — [[2023_Ferro_DUpdateReview]]
- [supported] The review states that when all error sources in QAMC are considered, a clean quadratic improvement over ideal classical Monte Carlo is not guaranteed by current analyses, though this does not definitively rule out practical speedups because the comparison conditions are asymmetric. — [[2023_Ferro_DUpdateReview]]
- [supported] Parallel amplitude estimation methods are generally more flexible in controlling circuit depth and are therefore considered more suitable for NISQ devices, while sequential methods tend to offer stronger theoretical guarantees. — [[2023_Ferro_DUpdateReview]]
- [supported] Simulations and hardware studies reviewed in the report indicate that noise can prevent amplitude-estimation-based methods from realizing their asymptotic quadratic speedup on realistic devices. — [[2023_Ferro_DUpdateReview]]
