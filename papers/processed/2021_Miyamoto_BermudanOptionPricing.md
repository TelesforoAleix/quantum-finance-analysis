---
aliases:
- Bermudan option pricing by quantum amplitude estimation and Chebyshev interpolation
- Bermudan option pricing quantum
authors:
- Koichi Miyamoto
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: ''
evidence_type: ''
idea_tags:
- idea:quantum-advantage
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-25T15:54:50.015695'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:54.120538'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:55:06.140700'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:33.884317'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:55:59.386302'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:10.990133'
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
- idea/quantum-advantage
- contradiction/scalability
title: Bermudan option pricing by quantum amplitude estimation and Chebyshev interpolation
topic_tags:
- derivatives-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
The paper proposes a quantum algorithm for pricing Bermudan options by combining quantum amplitude estimation with Chebyshev interpolation of the continuation value. Given an oracle for simulating the underlying asset price dynamics, the method estimates continuation values at Chebyshev nodes via quantum Monte Carlo and constructs an interpolant to drive the backward induction. The author derives error bounds and shows that, in terms of calls to the asset-path oracle, the complexity scales as Õ(ε⁻¹) in the target pricing error ε, yielding a quadratic speed-up over classical Monte Carlo-based approaches such as least-squares Monte Carlo.
## Methodology
This preprint is primarily theoretical/methodological, proposing a quantum algorithm for Bermudan option pricing rather than reporting empirical benchmark experiments. The method combines Chebyshev interpolation with quantum amplitude estimation (QAE) to approximate continuation values in the backward dynamic-programming recursion for Bermudan options. At each exercise date, the continuation value is approximated on a hyper-rectangular domain using tensorized Chebyshev polynomials; the values at Chebyshev nodes are estimated via QAE applied to conditional expectations of future option values under a Markov asset-price process. The paper formalizes assumptions on oracle access to conditional asset-price evolution, boundary/out-of-domain approximations, and analyticity of continuation values, then presents a full algorithmic pipeline (Algorithm 1), derives error bounds for the resulting option-price estimate, and proves complexity results showing oracle-call scaling of approximately O(1/epsilon) up to logarithmic factors, compared with classical Monte Carlo methods such as least-squares Monte Carlo (LSM) with O(1/epsilon^2) scaling. The work includes theorem statements, proofs, and asymptotic complexity analysis, but no numerical experiments or hardware implementation. As a preprint, it should be flagged as non-peer-reviewed.

**Algorithms used:** Quantum Amplitude Estimation, Chebyshev interpolation, Monte Carlo integration, Least-Squares Monte Carlo
## Experiment details
<!-- Step 3 output — experiment replication details -->

## Findings
- [speculative] The paper proposes a quantum algorithm for Bermudan option pricing that approximates continuation values via Chebyshev interpolation, with nodal values estimated using quantum amplitude estimation (QAE).
- [speculative] The authors claim the number of calls to the oracle generating underlying asset price paths scales as O~(epsilon^-1) for target pricing error epsilon, versus O~(epsilon^-2) for classical Monte Carlo-based methods such as least-squares Monte Carlo (LSM).
- [speculative] This scaling is presented as a quadratic speedup in error dependence relative to classical Monte Carlo approaches for Bermudan option pricing.
- [speculative] The method appears to be the first proposed quantum algorithm specifically for Bermudan option pricing, according to the author.
- [speculative] The algorithm relies on assumptions including access to a quantum oracle for conditional asset-price evolution, tractable handling of states outside interpolation domains, and analyticity/boundedness of continuation values on generalized Bernstein ellipses.
- [speculative] The paper derives an error bound for the final option price that decomposes into interpolation error, out-of-boundary approximation error, and QAE estimation error accumulated across exercise dates.
- [speculative] Under a parameter setting in Corollary 1 and assuming zero out-of-boundary approximation error, the algorithm is claimed to output an estimate with absolute error at most epsilon times Vmax_1 with probability greater than 0.99.
- [speculative] The derived total oracle complexity is O(epsilon^-1 log^d(epsilon^-1) polyloglog(epsilon^-1)), which the author argues eventually outperforms LSM's O~(epsilon^-2) complexity for sufficiently small epsilon.
- [speculative] The paper notes that the formal error bound contains a factor growing exponentially with the number of exercise dates K, but argues this may be an artifact of the bound rather than actual practical error growth.
- [speculative] An alternative error analysis based on analyticity assumptions for the intermediate quantity Q-hat rather than the true continuation value removes the exponential-in-K factor from the bound, though the author notes this is less self-contained.
- [speculative] The paper suggests that a quantum version of LSM may also be possible using quantum linear regression methods, but emphasizes that dependence on explanatory-variable dimension and condition number could limit practical advantage.

**Results summary:** This preprint presents a theoretical quantum algorithm for Bermudan option pricing that combines Chebyshev interpolation with quantum amplitude estimation. The core idea is to estimate continuation values at Chebyshev nodes using QAE and interpolate between them to approximate the dynamic programming recursion for early exercise. The paper derives error bounds and oracle-query complexity under several assumptions, including oracle access to conditional asset-price evolution and analyticity of continuation values. The main claim is a theoretical quadratic improvement in error dependence over classical Monte Carlo-based methods, reducing oracle complexity from O~(epsilon^-2) to O~(epsilon^-1), up to logarithmic factors. However, the work is analytical only, with no numerical experiments or hardware demonstrations, so all advantage claims remain speculative for this preprint.

**Performance claims:**
- Oracle-call complexity scales as O~(epsilon^-1) to achieve pricing error tolerance epsilon
- Classical Monte Carlo / LSM benchmark complexity stated as O~(epsilon^-2)
- Corollary 1 claims output error |V0 - V~0| <= epsilon * Vmax_1 with probability > 0.99 under stated assumptions
- QAE subroutine theorem states estimation error <= 7 / N_QAE <= epsilon with probability > 1 - gamma when N_QAE >= 7/epsilon and N_rep >= 12*ceil(log(gamma^-1)) + 1
- Derived total oracle complexity stated as O(epsilon^-1 log^d(epsilon^-1) polyloglog(epsilon^-1))
- LSM error rate cited from prior literature as E[|V^_0 - V0|] = O~(N_samp^(-n(p-2)/(2n(p+2)+d(p-2)))) under technical assumptions, approaching O~(N_samp^-1/2) as n,p -> infinity
## Quantum advantage claim
**Classification:** speculative

The paper claims a theoretical quadratic speedup in oracle-query complexity for Bermudan option pricing via QAE-based Monte Carlo integration, but provides no empirical validation, numerical experiments, or real-hardware demonstration. As a preprint, the advantage claim is therefore speculative.
## Limitations
- Preprint only; the results and claims have not undergone peer review
- The method requires strong assumptions, including access to an oracle that prepares the conditional distribution of next-step asset prices (Assumption 1)
- The approach assumes discretized asset-price dynamics with finitely many possible values at each step; continuous models require approximation/discretization
- The method relies on Assumption 2, requiring known and easily computable boundary/out-of-domain approximations or flat extrapolation for option values outside chosen hyper-rectangles
- The error analysis assumes analyticity and boundedness of continuation values on generalized Bernstein ellipses (Assumption 3), which may not hold or may be hard to verify in realistic financial models
- Practical parameter selection is difficult because key quantities such as rho_k and B_k are usually unknown, so the theoretically sufficient interpolation degrees cannot be set directly
- The proven error bound in Theorem 3 contains a factor that grows exponentially with the number of exercise dates K, suggesting potentially poor worst-case scaling as K increases
- The alternative error bound without the exponential factor (Theorem 4) depends on assumptions about intermediate algorithm-dependent quantities (hat Q_k), making the analysis less self-contained
- The complexity result is measured mainly by oracle calls for asset-path generation and does not fully account for the cost of implementing arithmetic circuits, controlled rotations, state preparation, and other subroutines
- No empirical or numerical experiments are provided to validate the theoretical speedup or quantify constants in realistic Bermudan pricing settings
- No implementation on actual quantum hardware is presented, so the impact of noise, decoherence, finite precision, and error mitigation is untested
- The paper does not benchmark against strong classical Bermudan pricing methods on practical instances, beyond asymptotic comparison to Monte Carlo/LSM
- [inferred] The method may suffer from curse-of-dimensionality effects through Chebyshev interpolation, since the number of interpolation nodes scales as (m_k+1)^d
- [inferred] The claimed quadratic speedup may be offset in practice by expensive state preparation/oracle construction for realistic stochastic models
- [inferred] Reproducibility is limited because the work is purely theoretical and does not provide code, experiments, or implementation details sufficient for end-to-end replication
- [inferred] The need for upper bounds such as 	ilde V_k^{max} and accurate payoff normalization may be nontrivial in complex products and models
## Open questions
- Whether an error bound similar to Theorem 4 can be derived under assumptions on Q_k and/or other quantities determined independently from the pricing algorithm
- Whether the actual pricing error truly grows exponentially with the number of exercise dates K, or whether the exponential factor is only an artifact of the proof technique
- How well the proposed method performs in realistic high-dimensional Bermudan option problems and under practical market models
- How costly it is to implement the required path-generation oracle O_step,k for common financial models in fault-tolerant quantum settings
- How sensitive the method is to discretization choices for continuous-time and continuous-state asset dynamics
- How to choose the interpolation domains D_k and polynomial degrees m_k effectively in practice when analyticity parameters are unknown
- Whether combining Chebyshev interpolation with quantum versions of non-Monte-Carlo continuation-value computation methods could be advantageous
- Whether a quantum version of the dynamic Chebyshev method of prior classical work could provide better reuse across pricing many options under the same model
- Whether quantum linear regression methods can make LSM genuinely advantageous once dependence on explanatory dimension D and condition number kappa is taken into account
- What basis-function choices in quantum LSM would minimize the condition number and make the approach practical
- [inferred] How robust the algorithm would be under realistic hardware noise and finite-precision arithmetic
- [inferred] At what problem sizes, if any, the asymptotic quantum advantage would overcome classical overheads in production finance settings

**Future work:**
- Investigate quantum versions of other Chebyshev-interpolation-based Bermudan pricing approaches, including methods that combine interpolation with non-Monte-Carlo continuation-value computation
- Consider the quantum version of the approach in which conditional expectations of Chebyshev polynomials are computed and reused across multiple options under the same model
- Derive a more desirable error bound similar to Theorem 4 under assumptions on Q_k and/or other algorithm-independent quantities
- Study quantization of least-squares Monte Carlo (LSM) using quantum linear regression methods
- Evaluate the dependence of quantum LSM on explanatory-variable dimension D and condition number kappa
- Find basis-function sets for quantum LSM that make the condition number as small as possible
- Extend the proposed method to other dynamic programming problems beyond Bermudan option pricing
- [inferred] Provide numerical experiments and practical benchmarks against classical Bermudan pricing methods
- [inferred] Test the method under realistic financial models and larger-dimensional option pricing instances
- [inferred] Analyze full resource requirements, including state preparation, arithmetic, precision, and fault-tolerance overheads
## Key ideas
- #idea:quantum-advantage — Proposes a quantum algorithm for Bermudan option pricing using quantum amplitude estimation to estimate continuation values within backward induction.
- #idea:quantum-advantage — Claims oracle-query complexity of approximately O(epsilon^-1) up to logarithmic factors, versus classical Monte Carlo / LSM scaling of approximately O(epsilon^-2).
- #idea:quantum-advantage — Combines Chebyshev interpolation with QAE to approximate continuation values at exercise dates and derive end-to-end pricing error bounds.
- #idea:quantum-advantage — Frames the contribution as a theoretical quadratic speedup in error dependence for Bermudan option pricing under strong oracle and analyticity assumptions.
## Contradictions
- The paper claims a theoretical quantum speedup for Bermudan option pricing, but this is undermined by its own limitations: no empirical validation, no hardware implementation, and complexity accounting focused mainly on oracle calls rather than full state-preparation and arithmetic costs.
- The asymptotic advantage is in tension with scalability concerns, since the interpolation grid scales exponentially with dimension through tensorized Chebyshev nodes and one error bound grows exponentially with the number of exercise dates K.
- The claimed superiority over classical methods is only against asymptotic Monte Carlo / LSM error scaling and does not include benchmarking against strong practical classical Bermudan pricing methods, so the practical advantage remains unsubstantiated.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
