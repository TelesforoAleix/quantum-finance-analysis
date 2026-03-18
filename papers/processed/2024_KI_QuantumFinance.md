---
authors:
- Patrick Rebentrost
- Seth Lloyd
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.1007/s13218-024-00870-9
evidence_type: ''
idea_tags: []
journal_or_venue: KI - Künstliche Intelligenz
methodology_tags: []
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: ''
relevance_phase3: not-yet-assessed
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T20:42:55.877421'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T20:42:58.932348'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T20:48:37.976472'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T20:48:49.848123'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T20:49:02.717007'
step5_model: Mistral-Large-3
step6_date: ''
step6_model: ''
steps_completed:
- 1
- 2
- 3
- 4
- 5
title: 'Quantum Computational Finance: Quantum Algorithm for Portfolio Optimization'
topic_tags: []
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum algorithm designed for portfolio optimization in financial services, leveraging quantum computing to process market data and determine optimal risk-return tradeoffs. The authors propose a method that potentially achieves logarithmic runtime relative to the number of assets, offering a theoretical speedup over classical approaches. The work focuses on constructing the risk-return curve and sampling from the optimal portfolio using quantum states, addressing key computational challenges in financial data analysis.
## Methodology
The paper presents a quantum algorithm for portfolio optimization in financial services, leveraging the Harrow-Hassidim-Lloyd (HHL) algorithm and its variants to solve an equality-constrained quadratic programming problem. The methodology involves quantum access to historical asset returns via quantum Random Access Memory (qRAM), enabling efficient preparation of the expected return vector and covariance matrix. The algorithm constructs the risk-return tradeoff curve and identifies the optimal portfolio as a quantum state, which can be sampled or measured. The study assumes quantum parallel access to financial data through qRAM, facilitating logarithmic runtime complexity in the number of assets and time steps. The solution is derived by solving a linear system using the HHL algorithm, with the optimal portfolio represented as a quantum state. The paper also discusses the preparation of input data structures, including expected returns and covariance matrices, and addresses challenges related to data loading, matrix conditioning, and output state utilization.

**Algorithms used:** HHL, Quantum Fourier Transform, Amplitude Amplification, Quantum Walk Hamiltonian Simulation, Quantum State Exponentiation

**Experimental setup:** The proposed algorithm assumes the use of quantum Random Access Memory (qRAM) for efficient data loading and access. The quantum computations are described theoretically, with no explicit mention of hardware (simulator or real QPU). The runtime complexity is analyzed under the assumption of qRAM availability, enabling logarithmic time operations for data analysis once loaded. The study does not report empirical experiments on actual quantum hardware but focuses on theoretical runtime advantages over classical methods.

**Dataset:** Historical asset returns for multiple assets over a defined time horizon, stored in qRAM. The dataset includes asset prices Πs(t) for s ∈ [N] assets and t ∈ [T] time steps, from which returns y(t) and the covariance matrix Σ are derived. The paper assumes the availability of precomputed expected returns and covariance matrices for the quantum algorithm.
## Findings
- [supported] The quantum algorithm for portfolio optimization can determine the optimal risk-return tradeoff curve and sample from the optimal portfolio using quantum operations on historical asset returns.
- [supported] The algorithm achieves a runtime of O(poly(log(TN))) for analyzing data loaded into quantum random access memory (qRAM), where T is the number of time steps and N is the number of assets, compared to classical O(poly(TN)) runtime.
- [speculative] The quantum algorithm can attain a logarithmic runtime poly(log(N)) in the number of assets N, potentially offering exponential speedup over classical poly(N) algorithms for portfolio optimization.
- [supported] The algorithm prepares the optimal portfolio as a quantum state, allowing sampling of asset weights with probability proportional to their squared portfolio weights, and measurements to determine sector allocations or sub-optimality.
- [supported] The quantum state encoding the covariance matrix can be prepared and measured to identify assets with the largest variances and pairs with the largest covariances.
- [speculative] Quantum advantage for portfolio optimization is contingent on efficient qRAM implementation and well-conditioned covariance matrices, which are not yet demonstrated on real hardware.
- [disputed] The paper claims potential quantum speedups over classical sampling approaches, but notes that quantum-inspired classical algorithms using importance-sampling data structures can also achieve logarithmic runtime for similar problems.

**Results summary:** The paper presents a quantum algorithm for portfolio optimization that leverages quantum linear systems algorithms (e.g., HHL) to solve the equality-constrained quadratic programming problem. The algorithm processes market data via quantum random access memory (qRAM) and achieves a theoretical runtime of O(poly(log(TN))) for determining the risk-return curve and optimal portfolio, compared to classical O(poly(TN)). The optimal portfolio is represented as a quantum state, enabling efficient sampling and measurement of portfolio properties. However, the results are based on simulations and theoretical assumptions, such as efficient qRAM access and well-conditioned matrices, with no empirical validation on real quantum hardware. The paper also acknowledges competing quantum-inspired classical algorithms that achieve similar logarithmic runtime advantages.

**Performance claims:**
- O(poly(log(TN))) runtime for quantum algorithm vs. O(poly(TN)) for classical algorithms
- Success probability P_χ = Ω(1) for preparing the quantum state encoding returns, assuming most returns are Θ(1)
- Success probability P_R = Ω(1) for preparing the expected return vector state
- Error bound ε_κ = O(ε) for pseudoinverse approximation when κ = O(poly(log d))
- Success probability P_w for preparing the portfolio state, with user-specified C = O(1/κ)
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical exponential speedup (logarithmic vs. polynomial runtime) for portfolio optimization under idealized conditions, including efficient qRAM access and well-conditioned covariance matrices. However, the advantage is not demonstrated on real hardware, and the practical feasibility of qRAM remains an open challenge. The claimed advantage is also contingent on the absence of efficient classical alternatives, though the paper notes quantum-inspired classical algorithms with similar runtime advantages.
## Limitations
- Assumes quantum access to market data via quantum Random Access Memory (qRAM), which is not yet physically implemented [inferred]
- Algorithm relies on the Harrow-Hassidim-Lloyd (HHL) algorithm, which requires error correction and fault-tolerant quantum computing, currently unavailable [inferred]
- Small qubit count constraints limit practical applicability to small-scale portfolio optimization problems (e.g., N assets where N is small due to hardware limitations) [inferred]
- Dependence on efficient qRAM data loading, which takes O(TN) time, undermining the logarithmic run-time advantage for data preparation [inferred]
- Noise and decoherence in current quantum hardware may significantly degrade solution quality, but no noise mitigation techniques are discussed [inferred]
- Assumes historical returns and covariance matrices are adequate proxies for future returns, ignoring non-stationarity in financial markets [inferred]
- Success probabilities of ancilla measurements (e.g., P_χ, P_R) are assumed to be Ω(1), but may be low in practice for certain datasets [inferred]
- Algorithm outputs the optimal portfolio as a quantum state, requiring O(N) time to determine exact composition, limiting practical utility [inferred]
- Conditioning on eigenvalues λ_j ≥ 1/κ may exclude relevant solutions if the matrix M is ill-conditioned [inferred]
- No empirical validation or comparison with classical state-of-the-art portfolio optimization methods (e.g., convex optimization solvers) [inferred]
- Scalability to production-scale problems (e.g., N > 100 assets) is untested due to hardware constraints [inferred]
- Reproducibility is limited by the lack of access to qRAM and fault-tolerant quantum hardware [inferred]
## Open questions
- How does the algorithm perform with real-world financial datasets, which may exhibit non-Gaussian returns, fat tails, or structural breaks?
- What is the impact of decoherence and hardware noise on the quality of the optimal portfolio solution?
- Can the algorithm be adapted to handle constraints beyond equality constraints (e.g., inequality constraints for no short-selling)?
- How does the quantum algorithm compare to quantum-inspired classical algorithms (e.g., those using importance sampling) in terms of run-time and accuracy?
- What are the minimal hardware requirements (qubit count, gate fidelity, coherence time) for achieving a practical quantum advantage?
- How sensitive is the algorithm to errors in the input data (e.g., noisy or incomplete historical returns)?
- Can the algorithm be extended to multi-period portfolio optimization or dynamic rebalancing?
- What is the trade-off between the approximation error (ε) and the condition number (κ) in practical settings?

**Future work:**
- Empirical validation on real quantum hardware (e.g., IBM Quantum or Rigetti) to assess performance under noise
- Comparison with classical and quantum-inspired algorithms to benchmark speedups and solution quality
- Extension to handle inequality constraints (e.g., no short-selling) using quantum interior point methods or variational algorithms
- Development of noise mitigation techniques to improve robustness on near-term quantum devices
- Exploration of hybrid quantum-classical approaches to bridge the gap between theoretical speedups and practical implementation
- Investigation of alternative data input models (e.g., streaming data) to reduce the O(TN) data loading overhead
- Application to multi-period portfolio optimization and dynamic asset allocation
- Integration with quantum machine learning techniques for improved return and risk modeling
## Key ideas
<!-- Step 6 output — bullet list with idea tags -->

## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
