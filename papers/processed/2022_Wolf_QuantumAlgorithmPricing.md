---
aliases:
- A Quantum Algorithm for Pricing Asian Options on Valuation Trees
- Quantum Algorithm Pricing Asian
authors:
- Mark-Oliver Wolf
- Roman Horsky
- Jonas Koppe
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.3390/risks10120221
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Risks
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-25T15:58:43.630744'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:58:47.328654'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:58:58.441813'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:59:33.579239'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:00:01.671983'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:00:18.287785'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- method/amplitude-estimation
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: A Quantum Algorithm for Pricing Asian Options on Valuation Trees
topic_tags:
- derivatives-pricing
year: 2022
zotero_key: ''
---

## Abstract summary
The paper proposes a quantum algorithm to approximate prices of discrete floating-strike Asian options using valuation trees. It encodes entire price paths and their probabilities into quantum states, and implements the payoff and positive-part operator via amplitude-based arithmetic and a quantum unit-step construction. The authors analyze circuit structure, resource requirements, and demonstrate the approach on a binomial model using a quantum simulator, highlighting potential quadratic speed-up via amplitude estimation once suitable hardware is available.
## Methodology
The paper develops a theoretical quantum-finance framework for pricing discrete floating-strike Asian options on valuation trees. The authors begin from the risk-neutral pricing formula under an equivalent martingale measure and approximate the underlying stochastic process by a discretized scenario/valuation tree with time discretization and state-space discretization at each time step. They formally decompose the option price into three components over tree paths: path probabilities f(x_k), payoff values g(x_k), and a positivity indicator q(x_k). The core methodological contribution is a quantum circuit construction that encodes tree paths in a qubit state register, loads path probabilities via quantum state preparation, implements the payoff using amplitude-based arithmetic (including amplitude addition and subtraction), and approximates the positive-part operator through an amplitude-based unit-step function built from repeated gearbox-style transformations and a Fourier approximation. The resulting circuit produces an amplitude proportional to the desired expectation, which is then recoverable by rescaling measured probabilities. The framework is designed to be compatible with quantum amplitude estimation, yielding a theoretical quadratic speedup over classical Monte Carlo. The paper also provides formal resource reasoning, including qubit requirements, controlled-gate counts, scaling arguments, and a circuit-splitting strategy to reduce depth by decomposing the payoff and Fourier terms into subcircuits. The theoretical development relies on assumptions of no arbitrage, existence of an equivalent martingale measure, existence of the first moment of the underlying, zero interest rate for simplicity, known underlying dynamics, and availability of an efficient state-preparation operator for the path distribution.

**Algorithms used:** Quantum Amplitude Estimation
**Frameworks:** Qiskit
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes a novel quantum algorithm to approximate the price of discrete floating-strike Asian options on valuation trees by decomposing pricing into three modules: path-probability loading, payoff evaluation, and positive-part indicator encoding.
- [speculative] By encoding path probabilities in amplitudes rather than discretizing the underlying into a fixed bit representation across time, the method is claimed to require substantially fewer qubits per time step and smaller circuits.
- [speculative] The algorithm is compatible with quantum amplitude estimation, which the authors claim could provide a quadratic speed-up over classical Monte Carlo methods for expectation estimation under fault-tolerant quantum computing assumptions.
- [speculative] The construction applies to general discrete scenario/valuation trees, not only binomial trees, provided an efficient state-preparation operator for path probabilities is available.
- [speculative] The payoff module uses amplitude arithmetic to encode the quantity S(T) - (1/n)∑ S(t_i) into measurement probabilities, with rescaling recovering the option value.
- [speculative] The positive-part condition is implemented approximately via an amplitude-based unit-step function using a gearbox/Fourier-series construction, with approximation quality controlled by parameters D and n_f.
- [supported] Simulator experiments on a 5-step Rendleman-Bartter binomial model show the circuit can reproduce expected Asian option pricing behavior and that increasing the positive-part approximation level from D=1 to D=2 reduces bias near zero payoff regions.
- [supported] The authors show a trade-off in the indicator approximation: higher approximation level D improves the step-function approximation, but requires more Fourier terms n_f to control outer-region errors.
- [supported] In full-circuit simulator experiments, D=1 produces noticeable bias, while D=2 reduces bias; however, increasing Fourier terms from n_f=5 to n_f=8 can increase total bias because compensation effects across payoff regions change.
- [speculative] Splitting the full circuit into subcircuits for g+(x_k) and g-(x_k), and separately for Fourier terms, can reduce circuit depth and remove the 1/4 scaling penalty from amplitude subtraction, making the approach more suitable for NISQ constraints.
- [speculative] The dominant resource cost arises from uniformly controlled rotations for payoff encoding, which scale as O(2^n) in cX-gate count for the chosen implementation.
- [speculative] The method may generalize to other derivative-pricing problems sensitive to discretization errors and could be advantageous on hardware with limited qubit counts.

**Results summary:** This peer-reviewed theoretical paper develops a quantum algorithm for pricing discrete floating-strike Asian options on valuation trees. The method encodes all tree paths into a quantum state register, loads path probabilities into amplitudes, computes the payoff through amplitude arithmetic, and approximates the positive-part operator with an amplitude-based unit-step construction using a Fourier/gearbox approach. The main theoretical claim is that, when combined with quantum amplitude estimation, the algorithm could achieve the standard quadratic Monte Carlo speed-up in estimating option prices, although this is not demonstrated experimentally in the paper. The authors validate the circuit design on a quantum simulator using a 5-step Rendleman-Bartter binomial model, showing that the algorithm reproduces expected pricing behavior and that approximation parameters materially affect bias. They also analyze resource requirements, reporting rapidly growing cX-gate counts with time steps and linear growth in qubit width, and argue that circuit decomposition into subcircuits can help mitigate depth limitations on near-term devices.

**Performance claims:**
- Quantum amplitude estimation would estimate the target amplitude with convergence O(1/N_s), versus classical Monte Carlo convergence O(1/sqrt(N_s)) [theoretical claim]
- For single-path tests, circuit results were compared against analytical values using 10^7 simulator shots
- For full pricing experiments, each histogram used 100 data points, each based on 10^6 simulator shots; the displayed mean corresponds to 10^8 total circuit executions
- For n=5 time steps, approximation level D=1 showed noticeable bias; D=2 reduced bias in simulator results
- Resource table for a single subcircuit: with parameters (a) D=1, n_f=4, cX counts for n=2,3,4,5,6 were 67, 141, 243, 473, 847; widths were 13, 15, 16, 18, 19
- Resource table for a single subcircuit: with parameters (b) D=2, n_f=5, cX counts for n=2,3,4,5,6 were 89, 187, 337, 663, 1229; widths were 17, 19, 20, 22, 23
- Resource table for a single subcircuit: with parameters (c) D=2, n_f=8, cX counts for n=2,3,4,5,6 were 89, 187, 337, 663, 1229; widths were 17, 19, 20, 22, 23
- Number of subcircuits used: 8 for (a) D=1, n_f=4; 10 for (b) D=2, n_f=5; 16 for (c) D=2, n_f=8
- The paper states current state-of-the-art hardware can execute circuits with reliable results up to about 30 cX-gate applications
## Quantum advantage claim
**Classification:** theoretical

The paper claims a potential quadratic speed-up via quantum amplitude estimation relative to classical Monte Carlo, but this advantage is argued theoretically and not demonstrated experimentally. The reported results are from simulation only, and the authors explicitly state they could not employ amplitude estimation in their implementation due to circuit-depth restrictions.
## Limitations
- The algorithm is evaluated only on a quantum computer simulator; the full end-to-end method is not demonstrated on real quantum hardware.
- The authors state that current hardware is not powerful enough to run the whole problem at once, so the practical applicability is deferred to future devices.
- Quantum speed-up is only theoretical in this work; the paper notes that quantum speed-up must still be shown in practice.
- Amplitude estimation, which is required for the claimed quadratic speed-up over classical Monte Carlo, could not be used in their implementation due to circuit depth restrictions of the simulator.
- The method relies on a valuation-tree approximation of the underlying process, introducing discretization/approximation error relative to the continuous model.
- The positive-part indicator q(x_k) is only approximated via a Fourier/gearbox construction, creating approximation bias that depends on the approximation level D and number of Fourier terms n_f.
- The results show noticeable bias for some parameter settings, especially around payoff values near zero, indicating sensitivity of accuracy to approximation choices.
- The approach assumes an arbitrage-free model with a known distribution, existence of an equivalent martingale measure, and existence of the first moment of the asset price process.
- For simplicity, the paper assumes a zero-interest-rate setting (B(t)=1 and effectively r=0 in the main formulation/example), limiting direct realism of the presented formulation.
- The implementation assumes an appropriate quantum state-preparation operator P is available, even though arbitrary state preparation generally requires an exponential number of gates.
- The dominant gate cost comes from uniformly controlled rotations requiring O(2^n) cX gates, which creates a gap between the compact theoretical formulation and practical circuit efficiency.
- Even in the reported small examples, cX-gate counts are far above what the authors describe as reliably executable on current NISQ hardware, limiting near-term feasibility.
- To manage depth, the main circuit is split into multiple subcircuits and recombined classically, which weakens the case for an immediate end-to-end quantum advantage.
- The empirical study is limited to a specific binomial/Rendleman-Bartter model instance with small time-step counts, rather than a broad range of realistic market models.
- Data/code reproducibility is limited because the Python code is only available upon request rather than openly archived.
- [inferred] There is no direct empirical comparison against state-of-the-art classical Asian option pricing methods in runtime, accuracy, or resource cost.
- [inferred] The paper does not quantify total error decomposition across tree discretization, payoff scaling, Fourier approximation, sampling error, and any future amplitude-estimation error.
- [inferred] No hardware-noise analysis or error-mitigation study is provided, so performance on real noisy devices remains uncertain.
- [inferred] Scalability to realistic financial problem sizes is unclear, since experiments are shown only for small n and resource growth appears steep.
- [inferred] The method is demonstrated for discrete floating-strike Asian options, so generality to broader classes of path-dependent products is not empirically validated.
## Open questions
- When will fault-tolerant or sufficiently large quantum hardware make the full algorithm practically executable?
- Can the proposed circuit achieve a real, end-to-end quantum advantage over classical pricing methods once amplitude estimation and larger hardware are available?
- How does the algorithm scale in accuracy and resource usage for larger numbers of time steps and more realistic valuation trees?
- What is the optimal trade-off between approximation level D and number of Fourier terms n_f for minimizing bias and circuit cost?
- How robust is the method on real noisy hardware, especially given the high two-qubit-gate counts?
- Can efficient, problem-specific state-preparation methods be found for general valuation-tree path distributions without exponential overhead?
- How large are the combined errors from valuation-tree discretization and the approximate positive-part implementation in realistic pricing settings?
- Would the observed bias behavior persist under other payoff ranges, market parameters, or alternative tree constructions?
- Can the amplitude-based positive-part technique be integrated effectively with bit-based quantum finance algorithms to reduce depth and qubit requirements?
- How well does the approach extend to other path-dependent derivatives beyond the specific Asian option studied?

**Future work:**
- Run the full algorithm on real quantum hardware once more powerful devices become available.
- Use quantum amplitude estimation within the proposed framework to realize the theoretical quadratic speed-up over classical Monte Carlo.
- Apply the method to different option types, explicitly including cliquet options.
- Investigate alternative quantum circuits for more optimized implementation of the probability, payoff, and indicator-function modules.
- Combine the amplitude-based positive-part construction with established bit-based quantum algorithms to reduce circuit depth and qubit counts.
- Generalize the approach to other derivative pricing algorithms that are sensitive to discretization errors.
- [inferred] Develop more efficient state-preparation routines tailored to valuation-tree distributions.
- [inferred] Perform empirical benchmarking against classical solvers on realistic financial instances.
- [inferred] Study noise-aware implementations and error-mitigation strategies for NISQ execution.
- [inferred] Analyze scalability and total error bounds for larger trees, more time steps, and richer market models.
## Key ideas
- #idea:quantum-advantage — The paper constructs an amplitude-estimation-compatible quantum circuit for pricing discrete floating-strike Asian options on valuation trees, with a theoretical quadratic convergence advantage over classical Monte Carlo.
- #idea:quantum-advantage — Path probabilities, payoff values, and the positive-part operator are encoded into amplitudes so the option value can be recovered from measurement probabilities.
- #idea:near-term-feasibility — The authors argue qubit width grows roughly linearly with time steps, but practical execution remains limited to small simulator examples because circuit depth is too large for current hardware.
- #idea:hybrid-approach — The full pricing circuit is decomposed into subcircuits with classical recombination to reduce depth and make execution more plausible under near-term constraints.
- #idea:near-term-feasibility — Simulator studies on a small 5-step binomial/Rendleman-Bartter model show the method reproduces expected pricing behavior and that approximation parameters D and n_f materially affect bias.
## Contradictions
- The paper claims potential quantum advantage through amplitude estimation, but this is not implemented experimentally; all results are simulator-based, so the superiority claim remains theoretical.
- The paper suggests near-term relevance via modest qubit scaling, yet its own resource analysis shows controlled-gate counts growing steeply and exceeding what current hardware can reliably execute, contradicting practical scalability.
- The end-to-end complexity story depends on efficient state preparation for valuation-tree path distributions, but the paper acknowledges this may require exponential overhead, undermining the claimed scalable advantage.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
