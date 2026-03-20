---
aliases:
- 'Quantum Computational Finance: Quantum Algorithm for Portfolio Optimization'
- Quantum Computational Finance Quantum
authors:
- Patrick Rebentrost
- Seth Lloyd
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1007/s13218-024-00870-9
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: KI - Künstliche Intelligenz
methodology_tags:
- HHL
- quantum-walk
- quantum-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers:
- 2020_Rebentrost_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-theoretical
source_type_confidence: high
step1_date: '2026-03-19T23:55:47.775282'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:55:51.888621'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:56:46.308843'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:57:54.850019'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:58:03.985729'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:58:08.071592'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/HHL
- method/quantum-walk
- method/quantum-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: 'Quantum Computational Finance: Quantum Algorithm for Portfolio Optimization'
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
This paper introduces a quantum algorithm designed for portfolio optimization in financial services, leveraging quantum computing to process market data and determine optimal risk-return tradeoffs. The authors propose a method that theoretically achieves logarithmic runtime relative to the number of assets, offering potential speedups over classical approaches. The work explores quantum access to financial data, efficient state preparation, and the application of quantum linear systems algorithms to solve quadratic optimization problems central to portfolio management.
## Methodology
The paper presents a theoretical framework for a quantum algorithm designed for portfolio optimization in financial services. The methodology is grounded in quantum linear systems algorithms, specifically leveraging the Harrow-Hassidim-Lloyd (HHL) algorithm and its variants to solve quadratic programming problems inherent in portfolio optimization. The theoretical model assumes quantum access to historical asset returns via quantum random access memory (qRAM), enabling efficient data loading and processing. The algorithm encodes financial data, such as expected return vectors and covariance matrices, into quantum states using amplitude encoding techniques. The core of the approach involves solving a linear system derived from the portfolio optimization problem, where the matrix comprises the covariance matrix, expected return vector, and price vector. The solution is obtained as a quantum state representing the optimal portfolio, which can then be sampled or measured to extract financially relevant information. The paper discusses the simulation of matrix exponentiation for the covariance matrix, expected returns, and prices, employing quantum walk methods and state exponentiation techniques. Theoretical assumptions include the availability of qRAM for data input, low-rank or sparse covariance matrices, and efficient state preparation methods. The methodology emphasizes potential quantum speedups, achieving logarithmic runtime in the number of assets under ideal conditions.

**Algorithms used:** HHL
## Findings
- [speculative] The quantum algorithm for portfolio optimization can attain a runtime of poly(log(N)), where N is the number of assets, compared to classical algorithms that take poly(N) time
- [speculative] The quantum algorithm leverages quantum random access memory (qRAM) to access market data in quantum parallel, enabling logarithmic runtime for data analysis once loaded
- [speculative] The algorithm determines the optimal risk-return tradeoff curve and samples from the optimal portfolio using quantum operations on historical asset returns
- [speculative] Quantum matrix inversion (HHL algorithm) is used to solve the quadratic programming problem underlying portfolio optimization, with runtime O(poly log(TN)) under ideal conditions
- [speculative] The algorithm prepares the optimal portfolio as a quantum state, allowing sampling of asset weights without full state measurement, potentially preserving logarithmic runtime advantages
- [speculative] The covariance matrix can be simulated efficiently using quantum state exponentiation techniques if it is low-rank, which is common in financial contexts due to underlying market factors
- [speculative] For sparse covariance matrices, quantum walk methods can simulate the matrix with query complexity O((sΣτ)^(1+o(1))/ε^o(1)), where sΣ is sparsity, τ is simulation time, and ε is accuracy
- [speculative] The algorithm can map out the efficient frontier (optimal risk-return tradeoff curve) in time O(log TN), where T is the time horizon and N is the number of assets
- [speculative] Sampling from the optimal portfolio state can provide insights into assets with the largest weights, though full reconstruction of the portfolio would require O(N) measurements
- [speculative] Under strong assumptions (sparsity and long/short correlation), sampling O(log N) copies of the portfolio state can reconstruct a close approximation of the optimal portfolio with bounded error
- [disputed] The paper claims potential exponential speedups via quantum matrix inversion, but notes that classical Monte Carlo methods and quantum-inspired algorithms can close such gaps under certain data preprocessing assumptions

**Results summary:** The paper presents a theoretical quantum algorithm for portfolio optimization that leverages quantum linear systems solvers (HHL algorithm) to achieve a claimed poly(log(N)) runtime for determining the optimal risk-return tradeoff curve and sampling from the optimal portfolio. The algorithm assumes quantum access to market data via qRAM and prepares the optimal portfolio as a quantum state, enabling efficient sampling and risk measurement without full state reconstruction. Key steps include quantum simulation of the covariance matrix (efficient for low-rank or sparse matrices), preparation of expected return and price vectors, and solving the quadratic programming problem underlying portfolio optimization. The authors discuss various measurement techniques on the output quantum state to extract financially relevant information while preserving potential quantum advantages. However, the paper acknowledges that classical methods, particularly those using importance sampling and low-rank assumptions, can achieve similar polylogarithmic runtimes, challenging the claimed quantum advantage.

**Performance claims:**
- Runtime of O(poly log(TN)) for determining the risk-return curve and optimal portfolio state, where T is the number of time steps and N is the number of assets
- O(log TN) time to map out the efficient frontier (optimal risk-return tradeoff curve)
- O((sΣτ)^(1+o(1))/ε^o(1)) query complexity for simulating sparse covariance matrices using quantum walks
- O(t²/ε) copies of the covariance matrix state required for quantum state exponentiation to accuracy ε
- O(log N/ε²) gate complexity for swap tests to measure portfolio risk or compare portfolios with additive accuracy ε
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical quantum advantage based on the potential for poly(log(N)) runtime for portfolio optimization, enabled by quantum linear systems algorithms and qRAM data access. However, this advantage is contingent on several assumptions: (1) efficient qRAM implementation, (2) low-rank or sparse covariance matrices, (3) efficient state preparation and measurement techniques, and (4) the absence of equally efficient classical algorithms. The authors acknowledge that classical methods using importance sampling and low-rank assumptions can achieve similar polylogarithmic runtimes, making the quantum advantage speculative rather than demonstrated.
## Limitations
- Assumes efficient quantum access to market data via quantum Random Access Memory (qRAM), which is not yet physically implemented [inferred]
- Logarithmic runtime (O(poly log(TN))) is only achievable after data is loaded into qRAM, which itself takes O(TN) time
- The algorithm returns the optimal portfolio as a quantum state, requiring O(N) measurements to determine exact composition, negating potential speedups [inferred]
- Success probability of preparing the optimal portfolio state (Pw) depends on matrix conditioning and may require multiple repetitions
- Assumes low-rank or sparse covariance matrices for efficient simulation, which may not hold in all market conditions
- Sampling approach for portfolio construction relies on strong assumptions (long/short assumption, sparsity of portfolio vector) that may not be realistic
- Noise and decoherence in near-term quantum hardware are not addressed, which could degrade performance [inferred]
- No empirical validation or comparison with state-of-the-art classical methods is provided [inferred]
- The paper acknowledges that classical methods (e.g., Monte Carlo, low-rank approximations) can achieve polylogarithmic runtime under similar assumptions, potentially closing the quantum advantage gap [inferred]
- Output problem remains a bottleneck: extracting useful classical information from the quantum state without full measurement is non-trivial and may limit practical advantages
## Open questions
- How does the algorithm perform under realistic market conditions where covariance matrices are neither low-rank nor sparse?
- What is the impact of noise and decoherence on the algorithm's performance in near-term quantum hardware?
- Can the algorithm maintain its theoretical speedup when accounting for the overhead of error correction in fault-tolerant quantum computing?
- How does the sampling-based portfolio construction perform when the long/short assumption or sparsity assumption is violated?
- What are the minimal hardware requirements (qubit count, coherence time, gate fidelity) for achieving a practical advantage over classical methods?
- How does the algorithm compare to quantum-inspired classical algorithms (e.g., Tang's algorithms) in terms of runtime and accuracy?
- What are the most effective measurement operators for extracting financially relevant information from the quantum portfolio state?
- Can the algorithm be extended to handle additional constraints (e.g., transaction costs, regulatory limits) without sacrificing its theoretical advantages?

**Future work:**
- Empirical validation of the algorithm on real quantum hardware or high-fidelity simulators
- Comparison with state-of-the-art classical and quantum-inspired algorithms for portfolio optimization
- Development of noise-resilient variants of the algorithm for near-term quantum devices
- Extension to multi-period portfolio optimization and dynamic rebalancing
- Exploration of alternative data input models that do not rely on qRAM
- Investigation of hybrid quantum-classical approaches to mitigate the output problem
- Development of new measurement techniques to extract more financially relevant information from the quantum portfolio state
- Application of the algorithm to other financial optimization problems (e.g., risk management, derivative pricing)
- Integration with quantum machine learning techniques for improved market data processing
## Key ideas
- #idea:quantum-advantage — Proposes a quantum algorithm for portfolio optimization with theoretical logarithmic runtime O(poly(log(TN))) vs. classical O(poly(TN)), leveraging HHL and qRAM for exponential speedup under idealized conditions
- #idea:near-term-feasibility — Assumes qRAM and fault-tolerant quantum computing, which are not yet available, but discusses potential for near-term hybrid approaches to bridge the gap
- #idea:hybrid-approach — Suggests future work on hybrid quantum-classical methods to address current hardware limitations and data encoding challenges
- #limitation:qubit-count — High qubit requirements and current hardware constraints limit practical applicability to small-scale problems (e.g., N < 100 assets)
- #limitation:noise — Noise and decoherence in current hardware may degrade solution quality, with no mitigation strategies discussed
- #limitation:data-encoding — Relies on qRAM for efficient data loading, which takes O(TN) time and undermines the logarithmic runtime advantage for data preparation
- #limitation:no-empirical-validation — Theoretical claims are not backed by empirical validation on real quantum hardware or comparison with classical state-of-the-art methods
## Contradictions
- #contradiction:classical-vs-quantum — Claims potential quantum speedups over classical sampling approaches, but acknowledges that quantum-inspired classical algorithms (e.g., importance-sampling) can achieve similar logarithmic runtime advantages (referenced in 2020_Rebentrost_QuantumAlgorithmsFinance)
- #contradiction:scalability — Theoretical speedup is contingent on efficient qRAM and well-conditioned matrices, but scalability to production-scale problems (N > 100 assets) is untested due to hardware constraints, contradicting claims of practical applicability
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
