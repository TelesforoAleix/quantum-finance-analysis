---
aliases:
- Quantum Computation for Pricing the Collateralized Debt Obligations
- Quantum Computation Pricing Collateralized
authors:
- Hao Tang
- Anurag Pal
- Tian-Yu Wang
- Lu-Feng Qiao
- Jun Gao
- Xian-Min Jin
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:52:12.405430'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:52:16.938438'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:53:00.564313'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:53:28.411265'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:54:08.375421'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:54:18.620286'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- topic/derivatives-pricing
- method/amplitude-estimation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Quantum Computation for Pricing the Collateralized Debt Obligations
topic_tags:
- risk-modelling
- derivatives-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
The paper presents a quantum circuit implementation for pricing collateralized debt obligations (CDOs) using IBM Qiskit. The authors encode two copula-based credit risk models—the single-factor Gaussian copula and the Normal Inverse Gaussian copula—via a conditional independence framework, construct circuits to load correlated default distributions and tranche loss functions, and then apply quantum amplitude estimation as a Monte Carlo alternative. They compare quantum results (including iterative QAE under noise) with classical Monte Carlo simulations for a multi-asset CDO, and discuss accuracy, robustness, and circuit scaling issues relevant to quantum finance applications.
## Methodology
This preprint presents an empirical quantum-finance implementation for pricing collateralized debt obligations (CDOs) by replacing classical Monte Carlo simulation with quantum amplitude estimation. The authors formulate CDO pricing under two copula-based credit risk models: a single-factor Gaussian copula and a Normal Inverse Gaussian (NIG) copula. Using the conditional independence approach, they express each asset's default probability as a function of a latent systematic risk factor Z and encode this correlated default structure into quantum circuits. The circuit architecture consists of: (1) loading independent asset default probabilities with Y-rotations (operator LX), (2) loading the discretized systematic risk distribution for Z with an uncertainty model circuit (operator UZ), (3) applying affine-mapped controlled rotations to transform unconditional default probabilities into conditional probabilities pi(z) (operator LZ), (4) summing loss-given-default values across assets with a weighted sum circuit (operator S), and (5) using comparators plus piecewise linear rotations (operator C&R) to encode tranche loss relative to lower and upper attachment points. The probability amplitude of an objective qubit is then estimated using iterative quantum amplitude estimation (IQAE), from which expected tranche losses and fair tranche spreads are recovered. The implementation is demonstrated in IBM Qiskit and evaluated on a toy CDO portfolio with four assets and three tranches, with results compared against exact matrix-calculated circuit outputs and classical Monte Carlo simulations. Additional robustness analyses vary the scaling factor in the payoff rotation, IQAE precision/confidence parameters, and input credit parameters to assess sensitivity and circuit behavior.

**Algorithms used:** Quantum Amplitude Estimation, Iterative Quantum Amplitude Estimation, Monte Carlo simulation
**Frameworks:** IBM Qiskit, Qiskit Aqua, SciPy

**Experimental setup:** The study implements the quantum circuits in IBM Qiskit and demonstrates results using the QASM cloud backend in a noisy intermediate-scale quantum (NISQ) simulation environment. Circuit outputs are also validated via exact matrix calculation of the quantum circuits. The workflow compares IQAE-based tranche loss estimates with classical Monte Carlo simulation and deterministic wavefunction/matrix results.

**Dataset:** Synthetic/example CDO portfolio data defined in the paper rather than an external market dataset. The main example uses a 4-asset portfolio with specified default probabilities, correlations to systematic risk, and loss-given-default values, plus tranche attachment points for Equity, Mezzanine, and Senior tranches.
## Experiment details
### Input
Example CDO input consists of 4 assets with parameters: asset 1 (lambda=2, p0=0.3, gamma=0.05), asset 2 (lambda=2, p0=0.1, gamma=0.15), asset 3 (lambda=1, p0=0.2, gamma=0.1), asset 4 (lambda=2, p0=0.1, gamma=0.05). Tranche attachment points are Equity [0,1], Mezzanine [1,2], Senior [2,7]. Systematic risk Z is discretized using 4 qubits into 16 slots over approximately -3 sigma to 3 sigma for both Gaussian (mean 0, variance 1) and NIG distributions; the NIG example is parameterized to produce mean 0, variance 1, skewness 1, kurtosis 6. No external time period or preprocessing pipeline is reported because the experiment uses constructed model inputs.

### Process
1. Encode each asset's unconditional default probability p0_i into nx qubits using RY rotations (LX). 2. Encode the systematic risk distribution Z into nz qubits as a superposition over discretized probability masses using an uncertainty model circuit (UZ). 3. Apply controlled affine-mapped rotations to transform p0_i into conditional default probabilities p_i(z) according to the conditional independence formula for either Gaussian or NIG copulas (LZ). 4. Aggregate portfolio loss using a weighted sum circuit over loss-given-default values lambda_i (S). 5. Compare cumulative loss against tranche lower and upper attachment points using comparator circuits and encode tranche payoff/loss with piecewise linear rotations on an objective qubit (C&R), using a scaling factor c typically set to 0.1. 6. Estimate the objective-qubit amplitude P1 with iterative quantum amplitude estimation (IQAE). 7. Convert P1 into expected tranche loss and then into fair tranche spread/return using the tranche notional. 8. Compare quantum estimates with exact matrix-calculated circuit outputs and classical Monte Carlo results. 9. Perform robustness checks by varying c, IQAE epsilon and alpha, and perturbing p0_i and gamma_i up to 50%. Monte Carlo benchmarking is performed using 20 independent runs of 1000 random repetitions each to obtain a result range.

### Output
Outputs are expected tranche losses and tranche returns/spreads for Equity, Mezzanine, and Senior tranches. Reported comparisons include IQAE estimates from the QASM simulator, exact matrix-calculated quantum circuit results, and classical Monte Carlo ranges. For the NIG example, tranche losses are reported approximately as 52.0% (Equity), 41.7% (Mezzanine), and 23.8% (Senior), with corresponding tranche returns of 52.0%, 41.7%, and 4.76% after dividing by tranche notionals. The paper also reports qualitative comparison between Gaussian and NIG copula outputs and sensitivity/robustness plots for algorithmic and model parameters.

### Parameters
- qubits_assets_nx: 4
- qubits_systematic_risk_nz: 4
- qubits_loss_register_ns: 3
- systematic_risk_slots: 16
- max_portfolio_loss: 7
- iqae_epsilon: 0.001
- iqae_alpha: 0.05
- reported_qasm_result_epsilon: 0.002
- scaling_factor_c: 0.1
- monte_carlo_repetitions_per_run: 1000
- monte_carlo_runs: 20
- gaussian_distribution: {'mean': 0, 'variance': 1}
- nig_distribution_target_moments: {'mean': 0, 'variance': 1, 'skewness': 1, 'kurtosis': 6}
- nig_distribution_parameters: {'alpha': -1.6771, 'beta': 0.75, 'mu': -0.6, 'delta': 1.2}

### Hardware
{'backend': 'IBM Qiskit QASM cloud backend', 'environment': 'Noisy Intermediate-Scale Quantum (NISQ) simulation environment', 'simulator_type': 'QASM simulator', 'additional_validation': 'Exact matrix calculation / wavefunction calculation of quantum circuits'}

### Reproducibility
Preprint. The paper states that Qiskit code was written by one author and that data supporting plots are available from the corresponding author upon reasonable request, but no public code repository is provided in the text. The paper gives substantial circuit-level detail, equations, parameter values, and appendices sufficient for partial replication, though full reproducibility would be improved by released source code and explicit scripts/configurations.
## Findings
- [supported] The paper implements quantum circuits for pricing CDO tranches under both a single-factor Gaussian copula model and a Normal Inverse Gaussian (NIG) copula model using IBM Qiskit.
- [supported] Using a conditional independence approach, the authors encode correlated asset default distributions into quantum circuits and use iterative quantum amplitude estimation (IQAE) to estimate tranche losses.
- [supported] For a 4-asset example CDO with 3 tranches, IQAE results on the QASM simulator match both matrix-calculated quantum-circuit outputs and classical Monte Carlo estimates for tranche losses under both Gaussian and NIG systematic risk distributions.
- [supported] In the example studied, the NIG model produces slightly lower tranche losses than the Gaussian model, with senior tranche loss reported as 0.2233 under NIG versus 0.2301 under Gaussian.
- [supported] The authors report expected tranche losses under the NIG example of 52.0% for the equity tranche, 41.7% for the mezzanine tranche, and 23.8% for the senior tranche; corresponding tranche returns are 52.0%, 41.7%, and 4.76%.
- [supported] Robustness analysis indicates that smaller scaling factor c in the comparator/rotation block improves approximation accuracy, and that IQAE precision parameter epsilon strongly affects result quality while alpha has limited influence.
- [supported] The senior tranche is the most sensitive to approximation and parameter choices, including scaling factor c and IQAE precision settings.
- [supported] Sensitivity analysis shows tranche losses increase with higher independent default probabilities p0_i and decrease with higher correlation parameters gamma_i, consistent with the conditional independence formulation used in the paper.
- [supported] Circuit-scaling analysis suggests that the UZ distribution-loading operator and the weighted-sum operator S dominate circuit depth and are the main bottlenecks for scaling.
- [speculative] The use of quantum amplitude estimation for CDO pricing may offer a promising alternative to classical Monte Carlo because of the theoretically expected quadratic speedup.
- [speculative] The work is presented as broadening the application scope of quantum computing in finance and as a promising approach for pricing various derivatives, but this broader practical impact is not empirically demonstrated beyond small simulated examples.
- [speculative] The paper claims to present the first quantum circuit implementation for CDO pricing.

**Results summary:** This preprint presents a Qiskit-based quantum workflow for pricing collateralized debt obligations using Gaussian and Normal Inverse Gaussian copula models. The authors encode correlated default risk via a conditional independence construction, compute portfolio loss with quantum arithmetic, and estimate tranche losses using iterative quantum amplitude estimation. In a small 4-asset, 3-tranche example evaluated in a noisy QASM simulation environment, the quantum results align with matrix-calculated circuit outputs and with ranges from repeated classical Monte Carlo simulations. The paper also reports that the NIG model yields slightly lower tranche losses than the Gaussian model in the example, and provides robustness and circuit-scaling analyses showing sensitivity to approximation parameters and identifying distribution loading and summation as the main depth bottlenecks. Because the study is a preprint and relies on simulation rather than demonstrated hardware speedups, any quantum advantage claim remains speculative.

**Performance claims:**
- 4-asset CDO example with nx = 4 qubits for assets, nz = 4 qubits for systematic risk discretization (16 slots), and ns = 3 qubits for loss encoding
- IQAE settings reported include epsilon = 0.001 and alpha = 0.05; figure results also show epsilon = 0.002 and alpha = 0.05
- Senior tranche loss: 0.2233 under NIG vs 0.2301 under Gaussian (matrix-calculated quantum-circuit results)
- Expected tranche losses under NIG example: Equity 52.0%, Mezzanine 41.7%, Senior 23.8%
- Corresponding tranche returns: Equity 52.0%, Mezzanine 41.7%, Senior 4.76%
- Monte Carlo benchmark constructed from 20 runs of 1000 random repetitions each
- Robustness analysis claims satisfactory IQAE results only when epsilon is reduced to 0.002 or below
- Canonical QAE error scaling is stated as O(M^-1) versus classical Monte Carlo O(M^-1/2), implying quadratic convergence improvement
## Quantum advantage claim
**Classification:** speculative

The paper invokes the standard theoretical quadratic speedup of quantum amplitude estimation over classical Monte Carlo, but the evidence here is limited to small Qiskit/QASM simulations and matrix calculations rather than real-hardware or large-scale empirical advantage.
## Limitations
- The study is a preprint and has not undergone peer review.
- Demonstration is limited to a very small toy CDO example with only four assets, which limits evidence for realistic portfolio-scale applicability.
- Results are demonstrated using IBM Qiskit and the QASM noisy simulator rather than execution on real quantum hardware.
- Monte Carlo benchmarking is based on only 20 sets of simulations with 1000 repetitions each, which provides a relatively weak classical reference.
- The authors note that the scaling factor c in the comparator/rotation operator must be small for the approximation sin^2(g0) = 1/2 - c to hold, so accuracy depends on this approximation.
- The implementation of the conditional default loading uses a first-order Taylor approximation; the paper shows this is an approximation choice rather than an exact encoding.
- The authors report that the senior tranche is especially sensitive to parameter choices such as c and IQAE precision epsilon, indicating reduced robustness for tail-risk tranches.
- The authors state that iterative QAE does not return a definite value but a confidence range, and satisfactory results were obtained only when epsilon is reduced to about 0.002 or below.
- The canonical QAE approach is acknowledged to require inverse QFT and exponentially increasing circuit depth, making it inefficient in practice.
- The authors identify that the UZ and S operators consume heavy circuit depth and require further optimization.
- The paper uses discretization of the systematic risk distribution into 2^nz slots over a truncated range (e.g., -3 sigma to 3 sigma), which introduces approximation error.
- The case study ignores recovery rates in the main setup to focus on the essential structure, reducing realism of tranche return estimates.
- The tranche returns in the example are acknowledged to be unrealistically high partly because default probabilities are high and recovery is ignored.
- Data availability is limited because supporting data are only available from the corresponding author upon reasonable request rather than fully open and packaged for reproduction.
- [inferred] No comparison is provided against state-of-the-art classical CDO pricing methods beyond basic Monte Carlo, so practical quantum advantage is not established.
- [inferred] No runtime, resource, or wall-clock benchmarking is reported to substantiate the claimed practical benefit of QAE for this use case.
- [inferred] The study does not demonstrate scalability to realistic CDO structures with many obligors, multiple factors, or production calibration workflows.
- [inferred] The use of a single-factor copula framework may be too restrictive for real credit markets with richer dependence structures.
- [inferred] The NISQ suitability claim remains only partially validated because the work relies on simulation and does not quantify hardware noise, decoherence, or error-mitigation effects on real devices.
- [inferred] Calibration to real market data is discussed conceptually, but the paper does not present an end-to-end empirical calibration and pricing study on actual market CDO data.
## Open questions
- How can the optimal parameters for iterative QAE, especially epsilon and alpha, be chosen for reliable financial pricing tasks?
- How can the heavy circuit-depth costs of the UZ and S operators be reduced or optimized?
- How well does the approach scale as the number of assets nx, uncertainty qubits nz, and sum-register qubits ns increase?
- How accurate and robust is the method for senior tranche pricing, given its higher sensitivity to approximation and QAE parameters?
- What performance would the method achieve on real quantum hardware rather than simulators?
- How much practical advantage remains once state preparation, comparator logic, and error effects are included?
- Can more realistic credit models, such as variance gamma or other non-Gaussian dependence structures, be encoded efficiently in quantum circuits?
- How should real-market distributions and calibration procedures be loaded into quantum circuits in a scalable way?
- [inferred] At what portfolio size, if any, would the quantum approach outperform advanced classical pricing methods in practice?
- [inferred] How robust is the method under realistic market calibration error, model misspecification, and changing correlation structures?

**Future work:**
- Optimize the UZ and S operators to reduce circuit depth.
- Investigate improved or alternative QAE methods that reduce circuit complexity below the canonical inverse-QFT-based approach.
- Study how to choose optimal iterative QAE parameters for this application.
- Extend the framework to other improved CDO pricing models, such as the variance gamma model.
- Use quantum generative adversarial networks to load more general probability distributions into quantum circuits.
- Explore parameter-shift-rule-based techniques to facilitate gradient encoding and machine-learning-based quantum finance models.
- Apply variational quantum algorithms suitable for NISQ devices to a broader range of finance tasks.
- Explore quantum annealing approaches for financial optimization problems.
- [inferred] Validate the method on real quantum hardware with noise mitigation and hardware-aware compilation.
- [inferred] Test the approach on larger, more realistic CDO portfolios and real market-calibrated datasets.
- [inferred] Compare against stronger classical baselines, including advanced variance-reduction and quasi-Monte-Carlo methods.
- [inferred] Incorporate recovery rates and more realistic tranche structures into the main experimental setup.
## Key ideas
- #idea:quantum-advantage — The paper replaces classical Monte Carlo for CDO tranche pricing with iterative quantum amplitude estimation, invoking the standard quadratic convergence advantage of QAE.
- #idea:near-term-feasibility — It provides a concrete Qiskit circuit design for copula-based credit risk pricing under Gaussian and NIG models, implemented in a NISQ-style simulator.
- #idea:quantum-advantage — On a 4-asset toy CDO, IQAE estimates align with exact circuit calculations and classical Monte Carlo ranges, supporting correctness of the quantum encoding rather than practical superiority.
- #idea:near-term-feasibility — The study explicitly analyzes circuit bottlenecks, identifying systematic-risk distribution loading and weighted-sum loss aggregation as dominant depth costs.
## Contradictions
- The paper suggests quantum advantage via QAE's theoretical quadratic speedup, but its own evidence is limited to tiny simulated examples with no real-hardware or runtime advantage, contradicting strong claims of practical quantum superiority.
- The paper presents the approach as promising for broader derivative and credit applications, yet also shows that circuit depth is dominated by distribution loading and summation blocks and only validates a 4-asset case, contradicting any implication of near-term scalability to realistic CDO portfolios.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
