# Contradiction Detection Report

Generated: 2026-03-25

## Summary

- Topics analyzed: 10
- Total contradictions found: 14
- High severity: 1
- Medium severity: 10
- Low severity: 3

## High Severity Contradictions

### methodology — [[2026_C_AdvancingStockPrice]] vs [[2026_C_AdvancingStockPrice]]

**Topic:** high-frequency-trading

**Paper A** ([[2026_C_AdvancingStockPrice]]):
> The paper reports a QSVM baseline accuracy of 85.4% in its comparison table and ablation study.

**Paper B** ([[2026_C_AdvancingStockPrice]]):
> The paper also states that QSVM achieved 92.5% accuracy versus 87.3% for an LSTM baseline.

**Analysis:** Within the same paper, QSVM is assigned two incompatible accuracy values, 85.4% and 92.5%, without clarifying that they come from different datasets, tasks, or experimental settings. These claims cannot both describe the same QSVM benchmark result.

---

## Medium Severity Contradictions

### quantum-advantage — [[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2025_ThirumalGunasekaran_ExploringRevolutionaryPotential]]):
> It states that quantum Monte Carlo methods can estimate expectation values with quadratic speedup over classical Monte Carlo by encoding scenarios in qubit amplitudes.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> The theoretical quadratic speedup of QAE over classical Monte Carlo is acknowledged, but this advantage was not realized in the reported practical experiments; in two option-pricing case studies both IAE and MLAE returned 0.00 USD while classical methods produced positive expected payoffs.

**Analysis:** The 2025 paper presents quadratic speedup for quantum Monte Carlo in a broad, theory-level way, while the 2026 empirical paper shows that in practical option-pricing experiments the QAE-based approach failed to deliver useful estimates or practical advantage. This is not a strict logical contradiction because one is a theoretical claim and the other is an implementation-specific result, but they are in clear tension regarding practical advantage for derivatives pricing.

---

### feasibility — [[2025_Kao_MixedSignalQuantum]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2025_Kao_MixedSignalQuantum]]):
> The authors argue that applying QAE to the proposed circuit could yield quantum advantages by requiring fewer measurements, but this was not empirically demonstrated in the reported experiments.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> In two empirical option-pricing case studies, QAE variants IAE and MLAE both returned 0.00 USD expected payoff while classical benchmarks produced positive payoffs, and the paper concludes the theoretical QAE advantage was not realized in practice.

**Analysis:** Kao presents QAE as a plausible route to quantum advantage for option pricing, whereas Barbaresco provides empirical evidence that QAE can fail badly in realistic pricing setups because of encoding limitations. These claims are not directly incompatible because Kao's statement is explicitly speculative and tied to a different architecture, but they create tension over the practical feasibility of QAE-based advantage in derivatives pricing.

---

### feasibility — [[2026_Prasad_QuantumAlgorithmsStochastic]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** derivatives-pricing

**Paper A** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> For linear and semilinear SDEs with Lipschitz coefficients, quantum algorithms estimate relevant quantities including option prices to accuracy ε in time ˜O(poly(d)polylog(1/ε)), versus classical O(poly(d)/ε²), with small-instance simulations showing speedups and resource estimates suggesting near-term feasibility for some finance problems.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> For the option-pricing Black-Scholes PDE case studied with a variational quantum algorithm, the estimated requirement is about 1.62 x 10^28 total quantum circuit evaluations and about 3.87 x 10^22 measurements per function evaluation, making the approach impractical on current hardware.

**Analysis:** Prasad argues that quantum methods for stochastic finance problems can have favorable scaling and may be feasible on near-term hardware for some dimensions, while Dechant's option-pricing resource analysis concludes that the studied quantum PDE approach is overwhelmingly impractical. This is tension rather than direct contradiction because the papers analyze different algorithmic families and formulations, but they point to sharply different conclusions about practical feasibility for derivative-pricing-related quantum methods.

---

### performance — [[2026_Prasad_QuantumAlgorithmsStochastic]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> Numerical simulations on small instances demonstrate polynomial-to-super-polynomial empirical speedups in accuracy for fixed runtime, including a 3x speedup for 2D Black-Scholes simulation and quadratic speedup in accuracy for a 2D Heston model.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> In simulated option-pricing experiments on AAPL European calls, QAE-based methods produced zero expected payoff while classical exact and Monte Carlo methods produced positive expected payoffs, so the theoretical quantum advantage was not realized.

**Analysis:** Prasad reports simulated speedups for derivative-pricing-related stochastic models, whereas Barbaresco reports simulated failure of a quantum pricing method on realistic option-pricing instances. These are not directly contradictory because they use different algorithms and problem encodings, but they are hard to reconcile at the level of overall practical performance claims for quantum derivatives pricing.

---

### quantum-advantage — [[2022_Herbert_QuantumMonteCarlo]] vs [[2023_Ferro_DUpdateReview]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Herbert_QuantumMonteCarlo]]):
> Fourier QMCI preserves the full quadratic quantum speedup in query complexity for derivative-pricing-style expectations, achieving MSE proportional to q^-2 when used with optimal QAE, while avoiding quantum arithmetic.

**Paper B** ([[2023_Ferro_DUpdateReview]]):
> When all error sources in QAMC are considered, a clean quadratic improvement over ideal classical Monte Carlo is not guaranteed by current analyses, and simulations/hardware studies indicate noise can prevent amplitude-estimation-based methods from realizing their asymptotic quadratic speedup on realistic devices.

**Analysis:** Herbert makes a strong theoretical claim that full quadratic speedup is retained by the Fourier-QMCI construction under its assumptions, whereas Ferro argues that for practical pricing/VaR settings the quadratic improvement is not guaranteed once realistic error sources are included. These are not a strict logical contradiction because Herbert's claim is asymptotic/theoretical and Ferro's is about realistic end-to-end conditions, but they are in clear tension about whether the advertised quadratic advantage should be expected in practice.

---

### feasibility — [[2021_Stamatopoulos_TowardsQuantumAdvantage]] vs [[2023_Ferro_DUpdateReview]]

**Topic:** derivatives-pricing

**Paper A** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Resource estimates suggest quantum advantage for the studied derivative-risk task could be achieved with about 5.5×10^7 T-depth, around 12,000 logical qubits, and a logical clock rate of about 7 MHz, or about 100 kHz per device with 60 QPUs.

**Paper B** ([[2023_Ferro_DUpdateReview]]):
> Even with fault-tolerant quantum computers, error-correction overhead may render the problem sizes needed for practical quadratic speedups in pricing and VaR unrealistically large, and expectations for near-term financial quantum advantage should be moderated.

**Analysis:** Stamatopoulos presents a concrete resource point at which quantum advantage appears achievable for a specific market-risk computation, while Ferro argues more broadly that fault-tolerant overhead may make practically relevant speedups unrealistically large. This is tension rather than direct contradiction because Stamatopoulos studies a specific task and Ferro gives a broader cautionary review, but the papers point to different conclusions about practical attainability.

---

### quantum-advantage — [[2021_Pistoia_QuantumMachineLearning]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** high-frequency-trading

**Paper A** ([[2021_Pistoia_QuantumMachineLearning]]):
> No end-to-end quantum machine learning application with exponential speedup over a classical counterpart has yet been discovered, and practical advantage is limited by data-loading and readout bottlenecks.

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> QML can provide exponential speedups through quantum parallelism and entanglement.

**Analysis:** Pistoia explicitly says end-to-end exponential speedup has not been established, while Deshmukh asserts that QML can provide exponential speedups in general. These are in tension because one emphasizes the absence of demonstrated end-to-end speedup and the other presents exponential speedup as an available capability, though Deshmukh's statement is broad and speculative rather than tied to a specific demonstrated finance workflow.

---

### quantum-advantage — [[2021_Pistoia_QuantumMachineLearning]] vs [[2026_C_AdvancingStockPrice]]

**Topic:** high-frequency-trading

**Paper A** ([[2021_Pistoia_QuantumMachineLearning]]):
> The review states that no end-to-end quantum machine learning application with exponential speedup over a classical counterpart has yet been discovered.

**Paper B** ([[2026_C_AdvancingStockPrice]]):
> The paper labels quantum advantage as demonstrated for its hybrid QML-HFT framework, reporting statistically significant gains in prediction accuracy and execution speed over listed baselines.

**Analysis:** Pistoia says no end-to-end QML application with exponential speedup has been discovered, whereas the 2026 HFT paper claims demonstrated quantum advantage in a concrete trading framework. These are not a clean direct contradiction because the 2026 paper reports empirical superiority on its benchmark rather than exponential speedup, but they are hard to reconcile as overall assessments of whether practical end-to-end advantage has been achieved.

---

### scalability — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2024_KrishnaPasupuleti_QuantumAlgorithmsSolving]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> A benchmark table describes portfolio optimization with QAOA on 3 assets only as a proof-of-principle, indicating finance applications remain early-stage.

**Paper B** ([[2024_KrishnaPasupuleti_QuantumAlgorithmsSolving]]):
> The chapter claims QAOA can handle portfolios with hundreds or thousands of assets more efficiently than classical optimization approaches.

**Analysis:** Benamer frames finance QAOA results as very small-scale proof-of-principle, while KrishnaPasupuleti suggests efficient handling of hundreds or thousands of assets. These claims create tension about current or near-term scalability, although KrishnaPasupuleti presents the larger-scale claim as prospective rather than empirically demonstrated.

---

### feasibility — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2026_C_AdvancingStockPrice]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Finance VQA applications are early-stage, with examples such as 3-asset proof-of-principle portfolio optimization and strong limitations from noise, measurement overhead, and scaling barriers.

**Paper B** ([[2026_C_AdvancingStockPrice]]):
> The hybrid QML-HFT framework is reported as demonstrated on real IBM Falcon 5-qubit and Eagle 16-qubit hardware with statistically significant performance gains over baselines.

**Analysis:** Benamer characterizes finance VQAs as still early and heavily constrained, whereas the 2026 HFT paper presents a real-hardware demonstration with strong performance claims. This is tension over the maturity and practical feasibility of quantum finance methods, though not a strict contradiction because one is a broad review and the other is a specific claimed experiment.

---

## Low Severity Contradictions

### quantum-advantage — [[2021_Pistoia_QuantumMachineLearning]] vs [[2023_Ferro_DUpdateReview]]

**Topic:** derivatives-pricing

**Paper A** ([[2021_Pistoia_QuantumMachineLearning]]):
> Amplitude estimation offers a theoretical quadratic speedup over classical Monte Carlo for derivative pricing once suitable probability distributions are prepared.

**Paper B** ([[2023_Ferro_DUpdateReview]]):
> A clean quadratic improvement over classical Monte Carlo is not guaranteed by current analyses once state initialization costs, noise, and other error sources are included; realistic devices may fail to realize the asymptotic speedup.

**Analysis:** Pistoia emphasizes the standard theoretical amplitude-estimation speedup, whereas Ferro emphasizes that this advantage may disappear in realistic implementations. These claims are not strictly incompatible because Pistoia's statement is explicitly theoretical and conditional on successful state preparation, but they frame the practical significance of the speedup quite differently.

---

### quantum-advantage — [[2022_Albareti_StructuredSurveyQuantum]] vs [[2023_Ferro_DUpdateReview]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Albareti_StructuredSurveyQuantum]]):
> Quantum amplitude estimation is the main source of potential advantage for derivative pricing and risk analysis, with a theoretical quadratic reduction in sample complexity relative to classical Monte Carlo.

**Paper B** ([[2023_Ferro_DUpdateReview]]):
> Current analyses do not guarantee a clean quadratic improvement for pricing and VaR once all error sources are included, and noise can eliminate the expected amplitude-estimation speedup on realistic hardware.

**Analysis:** Albareti summarizes the standard theoretical sample-complexity advantage, while Ferro stresses that this advantage may not survive realistic implementation constraints. This is a difference in emphasis rather than a direct contradiction because Albareti discusses theoretical potential and also notes severe hardware limitations.

---

### feasibility — [[2021_Pistoia_QuantumMachineLearning]] vs [[2025_JETIR_QuantumFinance]]

**Topic:** high-frequency-trading

**Paper A** ([[2021_Pistoia_QuantumMachineLearning]]):
> The review highlights that data input/output bottlenecks and QRAM assumptions can negate overall quantum advantage in finance applications.

**Paper B** ([[2025_JETIR_QuantumFinance]]):
> Quantum computing can reduce computational time for large-scale portfolio optimization and risk analysis, particularly as the number of assets increases, and industry adoption demonstrates measurable computational improvements using hybrid models.

**Analysis:** Pistoia stresses that practical bottlenecks may erase speedups, while JETIR emphasizes time reduction and measurable improvements from hybrid adoption. These are different overall readings of near-term feasibility rather than a direct factual contradiction, because JETIR is largely theoretical and does not directly rebut the bottleneck caveat.

---
