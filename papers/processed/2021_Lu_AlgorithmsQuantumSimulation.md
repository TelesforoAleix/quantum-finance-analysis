---
aliases:
- Algorithms for Quantum Simulation at Finite Energies
- Algorithms Quantum Simulation at
authors:
- Sirui Lu
- Mari Carmen Bañuls
- J. Ignacio Cirac
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PRXQuantum.2.020321
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: PRX Quantum
methodology_tags:
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: low
relevance_phase3: low
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-25T15:54:22.551908'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:28.393970'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:54:45.643743'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:39.207221'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:56:17.059219'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:24.944602'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Algorithms for Quantum Simulation at Finite Energies
topic_tags: []
year: 2021
zotero_key: ''
---

## Abstract summary
The paper introduces two quantum algorithms to study many-body systems at finite energies and temperatures using cosine-based energy filters. The first is a provably efficient hybrid quantum-classical method to compute expectation values in narrow energy windows around efficiently preparable states, while the second is a quantum-assisted Monte Carlo scheme that uses a quantum device to obtain sampling probabilities for microcanonical and canonical observables without encountering the sign problem. Both approaches are designed to work on near-term digital or analog quantum simulators using interferometric measurements and are benchmarked on Ising-type models.
## Methodology
The paper develops a theoretical framework for quantum simulation of finite-energy and finite-temperature properties of many-body systems. It introduces two algorithmic families: (1) a hybrid quantum-classical method for estimating expectation values in narrow energy windows around the mean energy of an efficiently preparable state, and (2) a quantum-assisted Monte Carlo sampling approach for microcanonical and canonical observables. The formal setup assumes an N-spin lattice Hamiltonian H = sum_n h_n with efficiently implementable real-time evolution and access to interferometric measurements of overlap-like quantities such as <psi|A e^{-iHt}|psi> and <psi|e^{-iHt}|psi>. The core theoretical tool is a cosine-filtering operator P_delta(E) = [cos((H-E)/N)]^{M}, with M chosen as the nearest even integer to N^2/delta^2, which is shown to approximate a Gaussian energy filter exp(-(H-E)^2/2 delta^2). The authors derive expansions of the filter in terms of short-time evolutions and use these to express filtered expectation values as classical postprocessing of measured time-series data. The main proof technique combines operator approximations, error propagation bounds, and lower bounds on the filtered-state normalization to establish polynomial-time scaling in system size N, inverse filter width, and inverse target error for the first algorithm. The analysis explicitly addresses assumptions on state preparation, measurement access, spectral bounds, and locality/finite-correlation-length behavior. The paper also formulates propositions about convergence to microcanonical and canonical quantities, discusses when constant versus shrinking filter width is sufficient, and provides alternative interferometric constructions for analog simulators under symmetry or control constraints. Numerical illustrations on an exactly solvable Ising/fermionic model and exact-diagonalization studies of a nonintegrable tilted-field Ising chain are used to support the theoretical claims, but the central contribution is the formal algorithmic and complexity analysis.

**Algorithms used:** cosine filtering, quantum phase estimation, quantum-assisted Monte Carlo, Metropolis-Hastings, importance sampling
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes a hybrid quantum-classical algorithm to compute expectation values of observables in finite energy intervals around the mean energy of an efficiently preparable state using cosine filtering and interferometric measurements, without preparing the filtered state explicitly.
- [speculative] The authors claim the first algorithm runs in time polynomial in the number of qubits N, the inverse filter width (or prescribed variance), and the inverse target error, under the assumptions that the initial state can be efficiently prepared and the required interferometric measurements can be efficiently implemented.
- [speculative] A formal result states that for any efficiently preparable state ψ and observable A with ||A||∞ ≤ 1, one can find an energy E within a window around the mean energy Eψ such that the filtered expectation values Aδ,ψ(E) and A'δ,ψ(E) can be estimated to additive error ϵ in time poly(N, 1/δ, 1/ϵ).
- [speculative] The polynomial-time guarantee holds only under specific conditions: efficient state preparation, efficient measurement of correlators like ⟨ψ|Ae^{-iHt}|ψ⟩ and ⟨ψ|e^{-iHt}|ψ⟩, and access to an energy interval where the filter denominator remains at least inverse-polynomially large.
- [speculative] The cosine filter is argued to approximate a Gaussian energy filter, suppressing contributions from eigenstates with energies far from the target energy by an amount controlled by δ.
- [speculative] The paper claims no known classical algorithm achieves the same polynomial scaling for computing these finite-energy filtered observables.
- [speculative] A second family of algorithms combines quantum simulation with classical Monte Carlo sampling to estimate microcanonical and canonical observables by sampling states with probabilities proportional to filtered local densities of states.
- [speculative] The quantum-assisted Monte Carlo approach is claimed to circumvent the classical quantum Monte Carlo sign problem, provided one can efficiently prepare states with suitable energies and estimate the required sampling probabilities on a quantum device.
- [supported] Numerical studies on an exactly solvable Ising/fermionic model indicate that practical variants of the algorithms can approximate local densities of states, microcanonical observables, and canonical observables for systems up to N = 100 spins.
- [supported] The practical implementations trade long coherent evolution for many measurements: the authors report that the algorithm can be arranged to use evolution times of order 6/δ while increasing the number of repeated measurements.
- [supported] The paper presents several alternative interferometric measurement schemes, including methods using conditional dynamics, additional internal states, catlike states, sequential measurements without cat states, and symmetry-based simplifications, with the latter two argued to be more resilient to decoherence at the cost of more measurements.
- [supported] Numerical experiments suggest the quantum-assisted Monte Carlo methods remain accurate under certain noise levels in the tested model, though no universal robustness theorem is established.
- [speculative] For microcanonical observables defined via diagonal filtering over the full trace, the authors argue that constant filter width δ may suffice in the thermodynamic limit because only intensive energy resolution δ/N needs to vanish.
- [supported] Exact-diagonalization studies on a nonintegrable tilted-field Ising chain provide evidence that for the state-dependent filtered quantity A'δ,ψ(E), δ must decrease with system size to approach true microcanonical values, and δ proportional to 1/N^2 appears sufficient in the tested cases.
- [speculative] The accessible energy range of the algorithms depends on the family of efficiently preparable states; product states cover only an extensive subinterval of the spectrum, while more expressive ansätze such as block-product states, matrix product states, adiabatically prepared states, or variational states could extend the reachable energies.

**Results summary:** This peer-reviewed theoretical paper introduces two quantum algorithmic frameworks for studying finite-energy and finite-temperature properties of many-body systems. The main theoretical contribution is a hybrid quantum-classical algorithm based on cosine filtering that estimates expectation values in narrow energy windows without explicitly preparing the filtered state. The authors prove a polynomial-time complexity bound in N, 1/δ, and 1/ϵ under assumptions of efficient state preparation and efficient interferometric measurement access. They also propose quantum-assisted Monte Carlo methods for microcanonical and canonical observables, arguing that these methods avoid the sign problem by using a quantum device to estimate positive sampling weights. The paper supplements the theory with numerical demonstrations on an exactly solvable Ising/fermionic model up to 100 spins, showing practical feasibility, shorter required evolution times than naive filtering, and reasonable robustness to some noise. Additional exact-diagonalization evidence on a nonintegrable model suggests that convergence to true microcanonical values for certain filtered pure-state observables requires decreasing filter width with system size.

**Performance claims:**
- The first algorithm is claimed to estimate filtered observables to additive error ϵ in time poly(N, 1/δ, 1/ϵ).
- For the guaranteed energy search, the target energy can be found within E ∈ [Eψ - rσψ, Eψ + rσψ] with r = {3 log[2(1 + 2σψ^2/δ^2)]}^(1/2).
- The proof establishes a lower bound on the filter denominator q of order inverse-polynomial in N and 1/δ, specifically via q ≥ (1/4)[δ^2/(δ^2 + 2σψ^2)]^(3/2) on a suitable interval.
- The guaranteed interval width for a suitable energy is at least ΔE ≥ δ^2/(6N).
- In the practical local-density-of-states example with N = 100 and δ = 0.1, the optimized method with r = 0.4 uses 120 measurements of aψ(t) and maximum evolution time t = 60.
- In the same example with N = 100 and δ = 1, the optimized method requires 12 measurements and maximum evolution time t = 6.
- For the practical first algorithm, the simulator is claimed to need evolution times ≤ 6/δ when taking x ≈ 3 and r ≈ 1.
- The measurement cost for sums like Eq. (26) is estimated as Rϵ^-2 ≈ 3√N/(δϵ^2).
- For N = 100, δ = 1, and ϵ = 10^-2, the paper estimates about 3 × 10^5 measurements, with possible optimization down to order 10^4 measurements.
- Monte Carlo demonstrations use 10^5 samples per point for microcanonical and canonical magnetization estimates in systems with N = 20 and N = 100 spins.
- Exact-diagonalization evidence on a nonintegrable Ising chain up to N = 28 suggests δ ∝ 1/N^2 yields fast convergence of A'δ,ψ(E) to microcanonical values, while δ ∝ 1/N gives reasonably close values.
## Quantum advantage claim
**Classification:** theoretical

The paper makes theoretical complexity claims that the first hybrid algorithm achieves polynomial scaling in system size, inverse filter width, and inverse error, and states that no known classical algorithm achieves the same scaling for the targeted finite-energy filtered observables. However, this is not an empirical demonstration of quantum advantage; the claims rely on assumptions about efficient state preparation and interferometric measurements, and the numerical results are illustrative rather than comparative advantage benchmarks.
## Limitations
- The first algorithm requires access to interferometric measurements or equivalent conditional-evolution primitives, which may be challenging on existing analog quantum simulators.
- The efficient-scaling guarantee applies only when the initial state can be efficiently prepared and the relevant observables can be efficiently measured.
- The provable efficiency result only guarantees access to energies within an interval around the mean energy of an efficiently preparable state, not arbitrary target energies across the full spectrum.
- Access to energies outside the range covered by product states requires more expressive but still efficiently preparable states, such as block-product states, matrix product states, adiabatically prepared states, or variational states.
- Although the algorithm is polynomial-time in theory, in practice it requires a significant number of measurements to obtain sensible results.
- The Monte Carlo-based second algorithm is explicitly not proven to be efficient.
- The quantum-assisted Monte Carlo method avoids the sign problem only as long as one can prepare states with suitable energies.
- For microcanonical observables, convergence to the true microcanonical value may require decreasing the filter width δ with system size; constant δ is not generally sufficient for the filtered-state observables in Eqs. (17).
- The authors note that for low energies near or below the minimum energy reachable by the chosen easy-to-prepare states, Dδ,ψ(E) becomes very small, causing convergence and numerical stability problems.
- The numerical demonstrations are carried out on simple benchmark models, especially an exactly solvable Ising/fermionic model, limiting evidence for broader practical applicability.
- The exact numerical benchmarks themselves suffer from precision problems for some energies because they involve very large and very small numbers.
- The practical variants that avoid cat states or simplify interferometric measurements become more resilient to decoherence only at the expense of requiring a larger number of measurements.
- Some alternative measurement schemes require additional internal states, catlike-state preparation, or special Hamiltonian symmetries, which restricts general applicability.
- [inferred] The paper provides only numerical simulations and theoretical analysis, not experimental validation on real quantum hardware or analog simulators.
- [inferred] The gap between asymptotic polynomial complexity and near-term practicality may be substantial because measurement overheads (e.g., 10^4-10^5 shots) can dominate runtime.
- [inferred] Robustness to realistic hardware noise is only partially explored; the paper mentions robustness against certain noises for one algorithm but does not provide a comprehensive noise analysis.
- [inferred] No direct comparison is given against state-of-the-art classical finite-temperature or spectral methods on nontrivial many-body instances, so practical quantum advantage remains unverified.
- [inferred] The work is theoretical and not finance-specific, so its relevance to quantum computing in financial services is indirect and would require substantial problem mapping.
## Open questions
- How small must the filter width δ be, as a function of system size, to reliably recover microcanonical expectation values for generic nonintegrable systems and observables?
- Under what conditions can constant δ suffice, and for which quantities does δ need to decrease with N?
- How broadly can the proposed algorithms be implemented on existing analog quantum simulators with realistic control limitations?
- What are the best practical strategies for preparing suitable initial states that access wider energy ranges than product states?
- How effective are the proposed methods on genuinely nonintegrable, higher-dimensional, long-range, or disordered systems beyond the benchmark models studied?
- What is the true practical scaling of the quantum-assisted Monte Carlo algorithm, given that no efficiency proof is available?
- How severe is the trade-off between shorter coherence times and increased measurement counts in realistic devices?
- To what extent do realistic decoherence, readout errors, and control imperfections affect the quality of reconstructed microcanonical and canonical observables?
- Can the sampling methods remain effective in low-energy regimes where Dδ,ψ(E) becomes exponentially small for accessible initial states?
- What is the most effective choice of filter expansion or coefficients for different hardware platforms and error models?

**Future work:**
- Optimize the quantum-assisted sampling algorithms using standard Monte Carlo strategies to speed up convergence.
- Explore alternative filter constructions, such as Chebyshev expansions, low-pass filters, or hardware-adapted coefficient choices.
- Use information collected during Monte Carlo sampling to estimate additional quantities, such as higher moments, without extra computations.
- Use adiabatic or variational algorithms to prepare lower-variance initial states, improving efficiency and enabling access to energies beyond those reachable with product states.
- Extend the methods to other quantities of interest, including Green functions and structure factors.
- Apply the framework to fermionic systems, longer-range interacting systems, and disordered setups, provided the quantum device can emulate the relevant Hamiltonians.
- Investigate more practical replacements for interferometric measurements tailored to different experimental platforms.
- Further study the convergence of filtered-state observables to microcanonical and canonical values in nonintegrable models as system size grows.
- [inferred] Validate the algorithms experimentally on real digital or analog quantum hardware.
- [inferred] Benchmark against advanced classical methods to clarify where practical quantum advantage, if any, may emerge.
- [inferred] Develop noise-aware and error-mitigated versions of the algorithms for near-term devices.
- [inferred] Design improved state-preparation schemes specifically targeting hard-to-reach low-energy regions where current easy-to-prepare states are insufficient.
## Key ideas
- #idea:hybrid-approach — Proposes a hybrid quantum-classical cosine-filtering method that reconstructs finite-energy expectation values from interferometric time-evolution measurements without explicitly preparing filtered states.
- #idea:hybrid-approach — Introduces a quantum-assisted Monte Carlo workflow where a quantum device estimates sampling probabilities and a classical Metropolis-Hastings sampler performs microcanonical/canonical importance sampling.
- #idea:near-term-feasibility — Frames the methods as suitable for near-term digital or analog quantum simulators by trading longer coherent evolution for more measurements and offering alternative interferometric constructions.
- #idea:quantum-advantage — Claims polynomial scaling in system size, inverse filter width, and inverse precision for the first algorithm, with no known classical algorithm matching this scaling for the targeted filtered observables.
- #idea:near-term-feasibility — Numerical studies on Ising-type models suggest practical variants can approximate local densities of states and thermal observables for systems up to about 100 spins under simulated conditions.
## Contradictions
- The paper suggests potential quantum advantage via complexity-theoretic scaling, but this is not empirically validated and lacks direct benchmarking against state-of-the-art classical methods, creating a contradiction with stronger practical quantum-superiority claims often made in application papers.
- The paper presents near-term feasibility claims, yet its own limitations note substantial measurement overhead, challenging interferometric requirements, restricted accessible energy ranges, and no efficiency proof for the Monte Carlo variant, which contradicts broad claims of scalability to realistic problems.
- Although the first algorithm is proven polynomial under assumptions, the evidence is based on theory and classical emulation rather than real hardware, contradicting any interpretation that practical large-scale deployment is already demonstrated.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
