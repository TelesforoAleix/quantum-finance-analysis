# Contradiction Detection Report

Generated: 2026-03-20

## Summary

- Topics analyzed: 11
- Total contradictions found: 84
- High severity: 39
- Medium severity: 40
- Low severity: 5

## High Severity Contradictions

### scalability — [[2021_Martin_TowardPricingFinancial]] vs [[2025_Chaudhary_PracticalQuantumSolver]]

**Topic:** asset-pricing

**Paper A** ([[2021_Martin_TowardPricingFinancial]]):
> qPCA algorithm achieved high fidelity (0.965) for 2×2 covariance matrix on IBMQX2 hardware, with meaningful results for 3×3 matrices but failed for 4×4 matrices due to decoherence and errors exceeding 100%

**Paper B** ([[2025_Chaudhary_PracticalQuantumSolver]]):
> Proposed quantum PDE solver algorithm scales to 14 qubits for 2D/3D PDEs (e.g., Black-Scholes) on noisy simulators and real hardware (ibm_torino), outperforming VQA-based solvers in accuracy and execution time

**Analysis:** Paper A explicitly states that qPCA fails for 4×4 matrices (equivalent to ~2 qubits per dimension) due to hardware limitations, while Paper B claims successful scaling to 14 qubits for higher-dimensional PDEs on similar hardware. This directly contradicts the scalability limits demonstrated in Paper A, as the latter's algorithm would require handling larger matrices than qPCA's demonstrated failure point.

---

### noise-resilience — [[2021_Martin_TowardPricingFinancial]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** asset-pricing

**Paper A** ([[2021_Martin_TowardPricingFinancial]]):
> For the 4×4 matrix, qPCA algorithm's depth exceeded IBMQX2 capabilities, leading to decoherence and errors >100%, rendering results meaningless without error mitigation

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA solved Markowitz’s mean-variance optimization for n=20 assets using 6 qubits, achieving 92% of classical benchmark accuracy on real hardware

**Analysis:** Paper A demonstrates that circuit depth and noise on NISQ devices (IBMQX2) make 4×4 matrix problems unsolvable without error mitigation, while Paper B claims QAOA successfully solved a 20-asset problem (likely requiring larger matrices) on similar hardware with 92% accuracy. This directly contradicts the noise resilience and feasibility claims, as the latter's problem size far exceeds the former's demonstrated failure point.

---

### performance — [[2023_Kobayashi_CrossSectionalStock]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** asset-pricing

**Paper A** ([[2023_Kobayashi_CrossSectionalStock]]):
> The quantum neural network (QCL) model shows lower risk-adjusted excess return than classical neural network models over the entire backtesting period (2008-2021), but outperforms them in the latest market environment (2016-2021), suggesting better adaptability to non-linearity and reduced overfitting.

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Quantum Neural Networks (QNNs) achieved 30% improved Sharpe ratios relative to classical Markowitz models and 12% higher Sharpe ratios than classical counterparts in backtesting of S&P 500 futures data.

**Analysis:** Paper A reports that the quantum neural network (QCL) underperforms classical neural networks over the full backtesting period (2008-2021) but outperforms in the later period (2016-2021). In contrast, Paper B claims QNNs consistently achieve 30% and 12% higher Sharpe ratios than classical models, implying superior performance across the board. The contradiction lies in the generalizability of quantum models' performance advantages: Paper A suggests conditional superiority, while Paper B asserts unconditional superiority.

---

### feasibility — [[2024_KI_QuantumFinance]] vs [[2025_Hlatshwayo_TechnicalReviewQuantum]]

**Topic:** asset-pricing

**Paper A** ([[2024_KI_QuantumFinance]]):
> Quantum algorithm for portfolio optimization achieves O(poly(log(TN))) runtime for analyzing data loaded into qRAM, with potential exponential speedup over classical O(poly(TN)) algorithms

**Paper B** ([[2025_Hlatshwayo_TechnicalReviewQuantum]]):
> Practical Quantum Advantage (PQA) requires overcoming data loading/readout challenges, noise in NISQ hardware, and the need for quantum error correction, with current algorithms (e.g., HHL) only outputting quantum states rather than full solutions

**Analysis:** Paper A claims theoretical exponential speedup for portfolio optimization assuming efficient qRAM and well-conditioned matrices, while Paper B explicitly states that such speedups are infeasible on NISQ devices due to data loading/readout limitations and noise. This is a direct contradiction: Paper A's claim relies on assumptions (e.g., qRAM) that Paper B argues are not met in practice, rendering the speedup unattainable with current hardware.

---

### feasibility — [[2025_NeelotpalDey_QuantumComputingFinancial]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2025_NeelotpalDey_QuantumComputingFinancial]]):
> Hybrid quantum-classical frameworks show strong potential for improving decision-making under uncertainty in financial services, with early adopters reporting measurable improvements in computational performance.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> Quantum advantage for solving differential equations using variational quantum algorithms (VQAs) is not demonstrated in this work; all results are based on simulations and theoretical error bounds, with no empirical validation on real quantum hardware.

**Analysis:** Paper A asserts that hybrid frameworks deliver measurable improvements in computational performance today, while Paper B explicitly states that quantum advantage for related tasks (e.g., solving differential equations) remains unproven and lacks empirical validation on real hardware. This is a direct contradiction regarding the current feasibility of quantum advantage in financial applications.

---

### quantum-advantage — [[2025_Vangibhuratha_QuantumMachineLearning]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2025_Vangibhuratha_QuantumMachineLearning]]):
> Quantum Principal Component Analysis (QPCA) can identify principal components of financial datasets exponentially faster than classical PCA, enhancing performance in high-frequency trading and risk decomposition.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> All results are based on simulations and theoretical error bounds, with no empirical validation on real quantum hardware. Quantum advantage remains speculative and unproven for variational quantum algorithms.

**Analysis:** Paper A claims exponential speedups for QPCA, while Paper B explicitly states that quantum advantage is unproven and lacks empirical validation. This is a direct contradiction regarding the current feasibility of exponential speedups in financial applications.

---

### quantum-advantage — [[2026_Mahmod_StateQuantumComputing]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2026_Mahmod_StateQuantumComputing]]):
> Google’s Sycamore and Willow quantum processors have shown quantum advantage in specific tasks, with Willow completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> Quantum advantage for solving differential equations using VQAs is not demonstrated in this work; all results are based on simulations and theoretical error bounds, with no empirical validation on real quantum hardware.

**Analysis:** Paper A cites Google’s Willow processor as demonstrating quantum advantage, while Paper B explicitly states that quantum advantage is not demonstrated for variational quantum algorithms. This is a direct contradiction regarding the current state of quantum advantage, as Paper A's claim is domain-general while Paper B's is specific to VQAs for differential equations.

---

### quantum-advantage — [[2026_Prasad_QuantumAlgorithmsStochastic]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> Quantum algorithms for simulating and solving stochastic differential equations (SDEs) can achieve polynomial and super-polynomial speedups over classical methods for high-dimensional systems, with numerical simulations on small instances (e.g., 2D Black-Scholes) demonstrating empirical speedups.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> Quantum advantage for solving differential equations using VQAs is not demonstrated in this work; all results are based on simulations and theoretical error bounds, with no empirical validation on real quantum hardware.

**Analysis:** Paper A claims empirical speedups for quantum algorithms solving SDEs, while Paper B explicitly states that quantum advantage is not demonstrated and lacks empirical validation. This is a direct contradiction regarding the current feasibility of quantum advantage for differential equations, as both papers address related tasks but reach opposing conclusions.

---

### scalability — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QNNs achieved 94.3% classification accuracy in thoracic CT scans, 8.2% higher than classical CNNs, with 60% fewer parameters, and 30% improved Sharpe ratios relative to classical Markowitz models in portfolio optimization.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems.

**Analysis:** Paper A reports empirical success of QNNs in both medical imaging and portfolio optimization, implying scalability and efficiency. Paper B, however, provides theoretical evidence that VQAs (including QNNs) face a quadratic scaling bottleneck in quantum circuit evaluations with the number of variational parameters. This directly contradicts Paper A's implied scalability, as the resource requirements would become prohibitive for larger problems despite the reported performance gains.

---

### noise-resilience — [[2023_Thakkar_ImprovedFinancialForecasting]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** credit-scoring

**Paper A** ([[2023_Thakkar_ImprovedFinancialForecasting]]):
> Quantum DPP sampling on IBM quantum hardware (ibmq_guadalupe) matched classical DPP performance for small batch dimensions (e.g., 4x2 matrices) but degraded as dimensions increased due to hardware noise.

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane) and maintains a 100% in-constraints rate (feasible solutions) on real hardware.

**Analysis:** Paper A explicitly states that quantum DPP sampling performance degrades with increased dimensions due to hardware noise on IBM quantum hardware, while Paper B claims significant performance improvements (379×) and feasibility on the same hardware platform (IBM Kyiv/Brisbane). This directly contradicts the noise-induced performance degradation observed in Paper A.

---

### quantum-advantage — [[2023_Thakkar_ImprovedFinancialForecasting]] vs [[2023_Thakkar_ImprovedFinancialForecasting]]

**Topic:** credit-scoring

**Paper A** ([[2023_Thakkar_ImprovedFinancialForecasting]]):
> Quantum DPP sampling may offer runtime advantages for large datasets (O(nd) gate complexity vs. O(d3) classical) once hardware noise is mitigated (speculative).

**Paper B** ([[2023_Thakkar_ImprovedFinancialForecasting]]):
> The paper disputes its own claim by noting that quantum circuits for DPP sampling have lower complexity (O(nd) gate count), but this is disputed by classical DPP sampling advances (e.g., O(poly(d)) runtime for exact sampling).

**Analysis:** The same paper (Paper A) first speculates about quantum DPP sampling's runtime advantage (O(nd) vs. O(d3)) but then disputes this claim by citing classical advances that achieve O(poly(d)) runtime, directly contradicting the potential quantum advantage.

---

### scalability — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2025_Hlatshwayo_TechnicalReviewQuantum]]

**Topic:** derivatives-pricing

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA solved Markowitz’s mean-variance optimization for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks, and QNNs achieved 12% higher Sharpe ratios in S&P 500 futures backtesting.

**Paper B** ([[2025_Hlatshwayo_TechnicalReviewQuantum]]):
> Variational quantum algorithms (e.g., QAOA) are limited by barren plateaus and noise in NISQ devices, making practical quantum advantage unlikely without error correction or significant hardware improvements.

**Analysis:** Benamer et al. report empirical success for QAOA and QNNs on NISQ devices (e.g., 20-asset optimization with 6 qubits), while Hlatshwayo et al. argue that barren plateaus and noise fundamentally limit VQAs, directly contradicting the feasibility of scaling such methods on current hardware.

---

### performance — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane) and is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) failed to capture non-zero expected payoffs for European call options, returning zero values despite classical methods (Black-Scholes and Monte Carlo) yielding positive payoffs ($17.60 and $17.06). The failure is attributed to limited resolution from 6 uncertainty qubits (64 bins), which inadequately encodes small-amplitude, in-the-money price regions.

**Analysis:** Paper A claims significant performance improvements and feasibility on real hardware for Rasengan in constrained optimization problems, while Paper B demonstrates a critical failure of QAE in derivatives pricing due to resolution limitations, directly contradicting the broader claims of quantum advantage in financial applications on real hardware.

---

### performance — [[2026_Mahmod_StateQuantumComputing]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2026_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> QAE variants (IAE and MLAE) failed to estimate non-zero expected payoffs for European call options, returning zero values despite classical methods yielding positive payoffs, due to resolution limitations.

**Analysis:** Paper A reports measurable improvements in bond trading optimization using quantum computing, while Paper B demonstrates QAE's failure to match classical benchmarks in derivatives pricing, creating a direct contradiction in the performance claims of quantum algorithms for financial applications.

---

### quantum-advantage — [[2022_Doriguello_QuantumAlgorithmStochastic]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Doriguello_QuantumAlgorithmStochastic]]):
> The quantum Least Squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm for stochastic optimal stopping problems, with a time complexity of ˜O(T²m⁴/ϵ) vs. classical ˜O(Tm⁶/ϵ²).

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> Quantum Amplitude Estimation (QAE) variants (IAE and MLAE) failed to estimate non-zero expected payoffs for European call options due to limited resolution from 6 uncertainty qubits, returning zero values despite classical methods yielding positive payoffs.

**Analysis:** Paper A claims a nearly quadratic speedup for quantum LSM in derivatives pricing, while Paper B demonstrates a practical failure of QAE (a key quantum algorithm for financial applications) to capture non-zero payoffs due to resolution limitations. This directly contradicts the feasibility of quantum advantage in derivatives pricing under current quantum hardware constraints.

---

### performance — [[2021_Stamatopoulos_TowardsQuantumAdvantage]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Quantum amplitude estimation (QAE) achieves quadratic error scaling advantage (O(1/ϵ)) over classical Monte Carlo methods (O(1/ϵ²)) for derivative pricing, with empirical results showing 200x lower oracle calls than theoretical bounds.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> QAE variants (IAE and MLAE) failed to estimate non-zero expected payoffs for European call options due to limited resolution from 6 uncertainty qubits, returning zero values despite classical methods yielding positive payoffs.

**Analysis:** Paper A claims a quadratic error scaling advantage and empirical success for QAE in derivative pricing, while Paper B demonstrates a practical failure of QAE to capture non-zero payoffs due to resolution limitations. This is a direct contradiction in the performance and feasibility of QAE for derivatives pricing.

---

### noise-resilience — [[2023_Thakkar_ImprovedFinancialForecasting]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** fraud-detection

**Paper A** ([[2023_Thakkar_ImprovedFinancialForecasting]]):
> Quantum DPP sampling on IBM quantum hardware (ibmq_guadalupe) matched classical DPP performance for small batch dimensions (e.g., 4x2 matrices) but degraded as dimensions increased due to hardware noise.

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> Quantum Support Vector Machines (QSVMs) achieved 92% accuracy on the MNIST dataset, implying robust performance on large-scale data.

**Analysis:** Paper A explicitly states that quantum hardware performance degrades with increasing problem dimensions due to noise, while Paper B claims high accuracy (92%) for QSVMs on a large-scale dataset (MNIST) without addressing noise limitations. This directly contradicts the noise-induced performance degradation observed in Paper A.

---

### quantum-advantage — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane) and is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware.

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> Google’s Willow quantum processor completed a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years, demonstrating quantum advantage in specific tasks.

**Analysis:** Paper A claims Rasengan achieves quantum advantage on real hardware by outperforming feasible solution baselines, while Paper B claims quantum advantage for Google’s Willow processor in a specific task. However, Paper A's claim is disputed as it does not compare Rasengan against the best classical solvers, whereas Paper B's claim is more narrowly defined and supported by a specific benchmark. This creates a direct contradiction in the scope and validation of quantum advantage claims.

---

### quantum-advantage — [[2025_Mahmod_StateQuantumComputing]] vs [[2025_Hlatshwayo_TechnicalReviewQuantum]]

**Topic:** market-simulation

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> Google’s Willow quantum processor completed a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years, demonstrating quantum advantage in specific tasks.

**Paper B** ([[2025_Hlatshwayo_TechnicalReviewQuantum]]):
> Claims of quantum advantage in random circuit sampling (e.g., Google’s Willow) are contested due to debates over classical simulation feasibility and benchmark fairness.

**Analysis:** Paper A presents Google’s Willow as a demonstrated case of quantum advantage, while Paper B explicitly disputes the validity of such claims, citing debates over benchmark fairness and classical simulation feasibility. This is a direct contradiction on the empirical evidence for quantum advantage.

---

### scalability — [[2024_KI_QuantumFinance]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2024_KI_QuantumFinance]]):
> The quantum algorithm can attain a logarithmic runtime poly(log(N)) in the number of assets N, potentially offering exponential speedup over classical poly(N) algorithms for portfolio optimization.

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Barren plateaus (exponential vanishing of cost function gradients with circuit depth) are a fundamental limitation of VQAs, though mitigation strategies exist.

**Analysis:** Paper A claims a theoretical exponential speedup for quantum portfolio optimization algorithms, while Paper B explicitly identifies barren plateaus as a fundamental scalability barrier for variational quantum algorithms (VQAs), which include QAOA. This directly contradicts the feasibility of achieving the claimed speedup on near-term hardware.

---

### quantum-advantage — [[2025_Innan_QuantumPortfolioOptimization]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Innan_QuantumPortfolioOptimization]]):
> The paper claims quantum advantage in portfolio optimization, but all results are from simulation only and no comparison with state-of-the-art classical methods is provided (disputed claim).

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> The paper claims Rasengan achieves quantum advantage on real hardware, but this is disputed as the results are compared to classical baselines and not demonstrated against the best classical solvers for the tested problems (disputed claim).

**Analysis:** Paper A explicitly disputes its own claim of quantum advantage due to lack of comparison with classical methods, while Paper B claims quantum advantage on real hardware but also acknowledges the lack of comparison with optimized classical solvers. Both papers dispute their own claims, creating a direct contradiction in the feasibility of demonstrated quantum advantage.

---

### scalability — [[2025_Innan_QuantumPortfolioOptimization]] vs [[2025_Uotila_HigherOrderPortfolio]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Innan_QuantumPortfolioOptimization]]):
> Quantum computing may offer superior scalability for portfolio optimization due to its ability to handle NP-hard problems more efficiently than classical methods (speculative).

**Paper B** ([[2025_Uotila_HigherOrderPortfolio]]):
> QAOA performance on HUBO problems degrades with increasing qubit counts (6-15 qubits tested), with only 3-23% of cases matching exact solutions (supported).

**Analysis:** Paper A speculatively claims superior scalability for quantum methods, while Paper B provides supported evidence that QAOA performance degrades as qubit counts increase, directly contradicting the scalability claim.

---

### scalability — [[2025_Dehn_ExtrapolationMethodOptimize]] vs [[2025_Uotila_HigherOrderPortfolio]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Dehn_ExtrapolationMethodOptimize]]):
> The linear-ramp QAOA (LR-QAOA) demonstrates superior runtime scaling compared to classical methods for portfolio optimization problems up to 28 qubits (supported).

**Paper B** ([[2025_Uotila_HigherOrderPortfolio]]):
> QAOA performance on HUBO problems degrades with increasing qubit counts (6-15 qubits tested), with only 3-23% of cases matching exact solutions (supported).

**Analysis:** Paper A demonstrates superior runtime scaling for QAOA up to 28 qubits, while Paper B shows QAOA performance degrades with increasing qubit counts (6-15 qubits), directly contradicting the scalability claims.

---

### quantum-advantage — [[2025_NeelotpalDey_QuantumComputingFinancial]] vs [[2025_JETIR_QuantumFinance]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_NeelotpalDey_QuantumComputingFinancial]]):
> The paper claims hybrid models can deliver quantum advantages today, but this contradicts broader literature suggesting quantum advantage in finance remains theoretical and unproven on real hardware (disputed).

**Paper B** ([[2025_JETIR_QuantumFinance]]):
> Industry adoption by firms like JPMorgan Chase, Goldman Sachs, and Nasdaq demonstrates measurable improvements in computational performance using hybrid quantum-classical models for tasks like option pricing and fraud detection (supported).

**Analysis:** Paper A disputes the claim of current quantum advantage in hybrid models, while Paper B cites industry adoption and measurable improvements as evidence of quantum advantage, creating a direct contradiction.

---

### performance — [[2021_Bennett_QuantumOptimisationVia]] vs [[2024_Leipold_TrainScalingQuantum]]

**Topic:** portfolio-optimisation

**Paper A** ([[2021_Bennett_QuantumOptimisationVia]]):
> MAOA outperforms QAOA and RGAS by amplifying optimal solutions more effectively without requiring computationally expensive variational procedures, making it more effective for near-term quantum devices.

**Paper B** ([[2024_Leipold_TrainScalingQuantum]]):
> QAOA with Train-and-Scale achieves high average quality solutions (approximation ratio below 0.4) for portfolio diversification problems with modest increases in circuit depth (p=54 for n=30).

**Analysis:** Paper A claims MAOA is superior to QAOA for near-term devices due to its avoidance of variational procedures and better amplification of optimal solutions. Paper B demonstrates QAOA's effectiveness with high-quality solutions for portfolio diversification, directly contradicting Paper A's claim about QAOA's limitations.

---

### performance — [[2021_Bennett_QuantumOptimisationVia]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2021_Bennett_QuantumOptimisationVia]]):
> MAOA achieves maximum amplification of optimal solutions by using a binary marking function and derived optimal parameters, avoiding the variational procedure of QAOA/QWOA.

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, and advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions.

**Analysis:** Paper A claims MAOA outperforms QAOA by avoiding variational procedures, while Paper B demonstrates QAOA's strong performance in combinatorial optimization problems, directly contradicting Paper A's assertion about QAOA's limitations.

---

### quantum-advantage — [[2021_Kerenidis_QuantumAlgorithmsPortfolio]] vs [[2024_KI_QuantumFinance]]

**Topic:** portfolio-optimisation

**Paper A** ([[2021_Kerenidis_QuantumAlgorithmsPortfolio]]):
> The quantum algorithm achieves a polynomial speedup over classical algorithms, with a runtime of O(poly(log(TN))) for analyzing data loaded into qRAM, compared to classical O(poly(TN)).

**Paper B** ([[2024_KI_QuantumFinance]]):
> The quantum algorithm can attain a logarithmic runtime poly(log(N)) in the number of assets N, but this is contingent on efficient qRAM implementation and well-conditioned covariance matrices, which are not yet demonstrated on real hardware.

**Analysis:** Paper A claims a proven polynomial speedup for quantum portfolio optimization, while Paper B and Paper C highlight that such speedups are contingent on unproven assumptions (e.g., efficient qRAM) and remain speculative due to hardware limitations, creating a direct contradiction.

---

### feasibility — [[2023_Fernandes_SystematicLiteratureReview]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** portfolio-optimisation

**Paper A** ([[2023_Fernandes_SystematicLiteratureReview]]):
> Quantum-assisted ML algorithms can provide real-time solutions for dynamic portfolio optimization, but this is contradicted by limitations in NISQ hardware (e.g., noise, decoherence, and error correction challenges).

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane) and maintains a 100% in-constraints rate (feasible solutions) on real hardware.

**Analysis:** Paper A argues that NISQ hardware limitations prevent real-time quantum solutions for dynamic portfolio optimization, while Paper B claims significant performance improvements and feasibility on real quantum hardware, directly contradicting Paper A's skepticism.

---

### quantum-advantage — [[2023_Giron_ApproachingCollateralOptimization]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2023_Giron_ApproachingCollateralOptimization]]):
> Quantum annealing (e.g., D-Wave) and classical simulated annealing failed to outperform branch-and-bound methods for certain combinatorial problems, contradicting claims of quantum advantage.

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks, and QNNs achieved 30% improved Sharpe ratios relative to classical Markowitz models.

**Analysis:** Paper A disputes quantum advantage claims by showing quantum annealing's inferiority to classical methods, while Paper B demonstrates QAOA and QNNs outperforming classical benchmarks in portfolio optimization, creating a direct contradiction.

---

### quantum-advantage — [[2024_Bhasin_EnhancingQuantumMachine]] vs [[2024_Mustafa_QuantumGraphNeural]]

**Topic:** quantum-ML

**Paper A** ([[2024_Bhasin_EnhancingQuantumMachine]]):
> The QSVM algorithm may offer exponential speedup for financial portfolio optimization due to quantum parallelism (speculative claim). The paper also claims a 'quantum advantage' in financial decision-making based on simulation results.

**Paper B** ([[2024_Mustafa_QuantumGraphNeural]]):
> All results are derived from noiseless quantum simulations, not real quantum hardware, and no clear advantage is demonstrated over classical methods in the tested regimes. Optimization challenges (e.g., barren plateaus) limit scalability in simulations.

**Analysis:** Paper A explicitly claims a 'quantum advantage' in financial decision-making and suggests exponential speedup potential, while Paper B demonstrates no clear advantage over classical methods and highlights scalability limitations (e.g., barren plateaus) that undermine claims of quantum advantage. Both papers rely on simulations, but Paper B's findings directly contradict Paper A's speculative claims of superiority.

---

### quantum-advantage — [[2025_Mahmod_StateQuantumComputing]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** quantum-cryptography

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> Google’s Willow quantum processor completed a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years, demonstrating quantum advantage in specific tasks.

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> Claims of quantum advantage in random circuit sampling (e.g., Google’s Willow) are contested due to debates over classical simulation feasibility and benchmark fairness.

**Analysis:** Paper A presents Google’s Willow processor as having demonstrated quantum advantage, while the same paper (in a disputed claim) acknowledges that such claims are contested due to debates over classical simulation feasibility and benchmark fairness. This creates a direct contradiction within the same paper about the validity of the quantum advantage claim.

---

### feasibility — [[2025_Mahmod_StateQuantumComputing]] vs [[2025_NeelotpalDey_QuantumComputingFinancial]]

**Topic:** quantum-cryptography

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications.

**Paper B** ([[2025_NeelotpalDey_QuantumComputingFinancial]]):
> The paper claims hybrid models can deliver quantum advantages today, but this contradicts broader literature suggesting quantum advantage in finance remains theoretical and unproven on real hardware.

**Analysis:** Paper A provides a supported claim of a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, while Paper B disputes that quantum advantage in finance remains theoretical and unproven on real hardware. This is a direct contradiction about the current feasibility of quantum advantage in financial applications.

---

### feasibility — [[2025_Mahmod_StateQuantumComputing]] vs [[2020_Kommadi_QuantumComputingSolutions]]

**Topic:** quantum-cryptography

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> Quantum computing has demonstrated experimental and commercial applications across diverse industries including finance as of 2025, with supported examples like HSBC and IBM’s bond trading optimization.

**Paper B** ([[2020_Kommadi_QuantumComputingSolutions]]):
> All claims about quantum computing applications in financial services are speculative due to the absence of empirical validation on real quantum hardware.

**Analysis:** Paper A provides supported evidence of quantum computing applications in finance (e.g., HSBC and IBM’s bond trading optimization), while Paper B states that all such claims are speculative due to the lack of empirical validation on real hardware. This is a direct contradiction about the current state of quantum computing feasibility in finance.

---

### quantum-advantage — [[2020_Kommadi_QuantumComputingSolutions]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** regulatory-compliance

**Paper A** ([[2020_Kommadi_QuantumComputingSolutions]]):
> Quantum advantage in financial services is projected to emerge with scalable quantum hardware (e.g., 50+ qubits), though current implementations rely on simulations

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> Google’s Willow quantum processor (105 qubits) has shown quantum advantage in specific tasks, completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years; D-Wave’s Advantage2 solves problems with up to 2 million variable constraints via hybrid solver

**Analysis:** Paper A claims quantum advantage is a future possibility contingent on scalable hardware (50+ qubits), while Paper B presents empirical evidence of quantum advantage achieved with current hardware (e.g., 105-qubit Willow processor and D-Wave’s 2M-variable solver). The contradiction lies in the feasibility timeline: Paper A treats quantum advantage as speculative and future-oriented, whereas Paper B demonstrates it as already realized in specific tasks.

---

### noise-resilience — [[2026_Gnal_ScenarioBasedMacroeconomic]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** regulatory-compliance

**Paper A** ([[2026_Gnal_ScenarioBasedMacroeconomic]]):
> Current quantum hardware limitations (noise, limited qubit counts, error propagation) constrain the scalability and reliability of quantum-enhanced forecasting models in the NISQ era

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> Google’s Willow processor (105 qubits) and D-Wave’s Advantage2 (2M-variable solver) demonstrate quantum advantage in specific tasks, with commercial deployments in finance, logistics, and healthcare

**Analysis:** Paper A emphasizes the constraints of NISQ-era hardware (noise, limited qubits) on quantum-enhanced models, while Paper B highlights successful deployments of quantum hardware (e.g., Willow, Advantage2) in real-world applications. The contradiction lies in the assessment of hardware readiness: Paper A focuses on limitations, whereas Paper B presents hardware as sufficiently advanced for practical use.

---

### feasibility — [[2021_Stamatopoulos_TowardsQuantumAdvantage]] vs [[2023_Fernandes_SystematicLiteratureReview]]

**Topic:** risk-modelling

**Paper A** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Quantum advantage threshold for financial risk computation is lowered from 50MHz to 7MHz logical clock rate (7x improvement) based on empirical resource estimates

**Paper B** ([[2023_Fernandes_SystematicLiteratureReview]]):
> The review claims that quantum-assisted ML algorithms can provide real-time solutions for dynamic portfolio optimization, but this is contradicted by limitations in NISQ hardware (e.g., noise, decoherence, and error correction challenges)

**Analysis:** Paper A claims empirical evidence for a lowered quantum advantage threshold, while Paper B disputes the feasibility of real-time solutions due to NISQ hardware limitations, directly contradicting the practical applicability of quantum advantage in financial risk computation.

---

### quantum-advantage — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2025_Dehn_ExtrapolationMethodOptimize]]

**Topic:** risk-modelling

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems

**Paper B** ([[2025_Dehn_ExtrapolationMethodOptimize]]):
> Linear-ramp QAOA (LR-QAOA) with extrapolation-based parameter optimization demonstrates superior runtime scaling compared to classical MQLib/Burer2002 for portfolio optimization problems up to 28 qubits, with quantum scaling exponent α = 0.219 vs. classical α = 0.323 in noiseless simulations

**Analysis:** Paper A claims Rasengan achieves quantum advantage on real hardware for small-scale problems, while Paper B demonstrates a quantum scaling advantage for LR-QAOA in noiseless simulations up to 28 qubits but does not validate this on real hardware. The contradiction is direct: Paper A's claim is hardware-validated but limited to small scales, whereas Paper B's claim is simulation-based and scalable but untested on hardware, making their quantum advantage claims incompatible in terms of empirical validation and problem size.

---

### quantum-advantage — [[2026_Mahmod_StateQuantumComputing]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** risk-modelling

**Paper A** ([[2026_Mahmod_StateQuantumComputing]]):
> Claims of quantum advantage in random circuit sampling (e.g., Google’s Willow) are contested due to debates over classical simulation feasibility and benchmark fairness.

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> Google’s Willow quantum processor completed a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years, demonstrating quantum advantage in specific tasks.

**Analysis:** Within the same paper, there is a direct contradiction: one claim asserts that Google’s Willow processor demonstrated quantum advantage, while another claim disputes such quantum advantage claims due to debates over classical simulation feasibility and benchmark fairness. This is a self-contradiction regarding the validity of quantum advantage.

---

### noise-resilience — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** risk-modelling

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real quantum platforms (IBM Kyiv and Brisbane) and reduces circuit depth by 1.96× compared to prior VQAs, making it deployable on NISQ devices

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Barren plateaus (exponential vanishing of cost function gradients with circuit depth) are a fundamental limitation of VQAs, though mitigation strategies exist

**Analysis:** Paper A claims significant performance improvements and deployability on NISQ devices, while Paper B argues that barren plateaus are a fundamental limitation of VQAs, directly contradicting the feasibility and scalability of Paper A's claims on real hardware.

---

## Medium Severity Contradictions

### performance — [[2023_Vishwakarma_QuantumComputingAlgorithms]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** asset-pricing

**Paper A** ([[2023_Vishwakarma_QuantumComputingAlgorithms]]):
> HQG-CA achieved 96.2% algorithmic speedup correlation, 97.5% accuracy correlation, and 98.3% scalability correlation in simulations, outperforming classical methods

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios relative to classical Markowitz models, with 12% higher Sharpe ratios in S&P 500 futures backtesting

**Analysis:** Paper A claims near-perfect performance correlations (96-98%) for HQG-CA in simulations, while Paper B reports more modest but still significant improvements (30% Sharpe ratio) in real-world-like scenarios. Paper C, however, shows only marginal improvements (0.23% MAPE reduction) for quantum-inspired methods. The tension arises from the disparity in claimed performance gains: Paper A's near-ideal results are hard to reconcile with Paper C's incremental improvements, suggesting either overestimation in simulations or context-dependent performance.

---

### quantum-advantage — [[2025_NeelotpalDey_QuantumComputingFinancial]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** asset-pricing

**Paper A** ([[2025_NeelotpalDey_QuantumComputingFinancial]]):
> Hybrid quantum-classical models can deliver quantum advantages today, with early adopters (e.g., JPMorgan Chase, Goldman Sachs, Nasdaq) reporting measurable improvements in computational performance for tasks like option pricing, portfolio optimization, and fraud detection.

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications (supported claim). However, the paper also notes that claims of quantum advantage in random circuit sampling (e.g., Google’s Willow) are contested due to debates over classical simulation feasibility and benchmark fairness (disputed claim).

**Analysis:** Paper A claims that hybrid models deliver quantum advantages today with measurable improvements, while Paper B provides specific evidence of a 34% accuracy improvement in bond trading but also highlights broader disputes over quantum advantage claims. The tension arises from Paper A's unqualified assertion of current quantum advantage versus Paper B's nuanced acknowledgment of both demonstrated improvements and ongoing debates about quantum advantage validity.

---

### scalability — [[2025_Vellaipandiyan_HybridQlstmFramework]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** asset-pricing

**Paper A** ([[2025_Vellaipandiyan_HybridQlstmFramework]]):
> The hybrid QLSTM framework achieved superior performance in stock price prediction (R² of 0.83 vs. 0.54 for classical LSTM) and demonstrated faster convergence, indicating better generalization and learning efficiency.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> The number of quantum circuit evaluations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems. Quantum advantage is not demonstrated and remains speculative.

**Analysis:** Paper A presents empirical evidence of superior performance for a hybrid quantum-classical model, while Paper B highlights scalability limitations (quadratic scaling of circuit evaluations) that could undermine the practicality of such models for large-scale financial applications. The tension arises from reconciling Paper A's performance gains with Paper B's scalability concerns.

---

### quantum-advantage — [[2025_KI_QuantumFinance]] vs [[2026_Prasad_QuantumAlgorithmsStochastic]]

**Topic:** asset-pricing

**Paper A** ([[2025_KI_QuantumFinance]]):
> The quantum algorithm for portfolio optimization achieves a runtime of O(poly(log(TN))) for analyzing data loaded into quantum random access memory (qRAM), where T is the number of time steps and N is the number of assets, compared to classical O(poly(TN)) runtime.

**Paper B** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> Quantum algorithms for simulating and solving stochastic differential equations (SDEs) can achieve polynomial and super-polynomial speedups over classical methods for high-dimensional systems, with empirical speedups demonstrated on small instances (e.g., 2D Black-Scholes with 10 qubits).

**Analysis:** Paper A claims a logarithmic runtime advantage for portfolio optimization contingent on efficient qRAM implementation, while Paper B demonstrates empirical speedups for SDEs but does not address qRAM or portfolio optimization. The tension arises from the differing assumptions about hardware prerequisites (qRAM vs. NISQ devices) and the lack of empirical validation for Paper A's claims, making it hard to reconcile the two papers' projections of quantum advantage.

---

### performance — [[2025_Vellaipandiyan_HybridQlstmFramework]] vs [[2023_Kobayashi_CrossSectionalStock]]

**Topic:** asset-pricing

**Paper A** ([[2025_Vellaipandiyan_HybridQlstmFramework]]):
> The hybrid QLSTM framework achieved superior performance in stock price prediction, with an R² score of 0.83, MSE of 85.16, and faster convergence compared to classical LSTM, which achieved an R² of 0.54 and MSE of 235.74.

**Paper B** ([[2023_Kobayashi_CrossSectionalStock]]):
> The quantum neural network (QCL) model shows lower risk-adjusted excess return than classical neural network models over the entire backtesting period (2008-2021), but outperforms them in the latest market environment (2016-2021).

**Analysis:** Paper A demonstrates that the hybrid QLSTM model outperforms classical LSTM in stock price prediction across all reported metrics. Paper B, however, shows that the quantum neural network (QCL) model underperforms classical neural networks over the full backtesting period but outperforms in a later sub-period. While the models and tasks differ slightly, the tension arises from the inconsistent performance advantages of quantum models: Paper A suggests unconditional superiority, while Paper B suggests conditional superiority.

---

### quantum-advantage — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2025_Mahmod_StateQuantumComputing]]

**Topic:** credit-scoring

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems.

**Paper B** ([[2025_Mahmod_StateQuantumComputing]]):
> Google’s Sycamore and Willow quantum processors have shown quantum advantage in specific tasks, with Willow completing a computation in under five minutes that would take the world’s fastest supercomputer an estimated 10^25 years.

**Analysis:** Paper A claims Rasengan achieves practical improvements on real hardware for constrained optimization, while Paper B highlights quantum advantage in a specific task (random circuit sampling) but does not address constrained optimization. The tension lies in the differing contexts (feasible solution quality vs. computational speedup) and the lack of direct comparison between Rasengan and Google's processors for the same problem type.

---

### quantum-advantage — [[2018_Rebentrost_QuantumComputationalFinance]] vs [[2022_Doriguello_QuantumAlgorithmStochastic]]

**Topic:** derivatives-pricing

**Paper A** ([[2018_Rebentrost_QuantumComputationalFinance]]):
> The quantum algorithm for Monte Carlo pricing achieves a quadratic speedup in error scaling (ζ_Q ≈ -0.982 vs. ζ_C = -0.5) and number of steps (O(λ/ϵ) vs. O(λ²/ϵ²)), validated via numerical simulations for European and Asian options.

**Paper B** ([[2022_Doriguello_QuantumAlgorithmStochastic]]):
> The quantum Least Squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime (˜O(T²m⁴/ϵ) vs. ˜O(Tm⁶/ϵ²)) for stochastic optimal stopping problems, but notes that exponential dependence on T in complexities may limit practical advantage.

**Analysis:** Both papers claim quadratic speedups for quantum algorithms in derivatives pricing, but Rebentrost et al. explicitly validate their speedup for European/Asian options with numerical simulations, while Doriguello et al. highlight potential limitations due to exponential dependence on T, suggesting the speedup may not hold universally for all problem instances or complexities.

---

### feasibility — [[2020_Miyamoto_ReductionQubitsQuantum]] vs [[2021_Stamatopoulos_TowardsQuantumAdvantage]]

**Topic:** derivatives-pricing

**Paper A** ([[2020_Miyamoto_ReductionQubitsQuantum]]):
> The quantum Monte Carlo algorithm using PRNG achieves a quadratic speedup (O(N^{-1}) error scaling) while reducing qubit requirements, but introduces a trade-off of increased circuit depth that may limit practical implementation on near-term hardware.

**Paper B** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Quantum amplitude estimation (QAE) achieves quadratic error scaling (O(1/ϵ)) and demonstrates empirical advantages (e.g., 200x lower oracle calls) for derivative pricing, with a 7x reduction in required logical clock rate (50MHz → 7MHz) for quantum advantage.

**Analysis:** Miyamoto et al. emphasize the trade-off between qubit reduction and increased circuit depth, suggesting near-term hardware limitations, while Stamatopoulos et al. present empirical results showing practical feasibility (e.g., reduced logical clock rate) without addressing circuit depth constraints, creating tension in the perceived readiness of these methods.

---

### methodology — [[2022_Saha_IntermediateQutritBased]] vs [[2025_Cibrario_AutocallableOptionsPricing]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Saha_IntermediateQutritBased]]):
> Qutrit-based arithmetic operations reduce Toffoli gate count (3 vs. 25), circuit depth (3 vs. 7), and eliminate T-depth (0 vs. 1), achieving a 40% reduction in error probability for Toffoli count of 30 and 162M CNOT-cost (vs. 12B T-cost) for derivative pricing.

**Paper B** ([[2025_Cibrario_AutocallableOptionsPricing]]):
> The proposed quantum algorithm achieves a ~50x reduction in T-depth and ~16x reduction in T-gates for autocallable options pricing, contingent on fault-tolerant hardware, but does not address qutrit-based approaches.

**Analysis:** Saha et al. demonstrate that qutrit-based methods eliminate T-depth entirely, while Cibrario et al. focus on T-depth reduction in qubit-only implementations, suggesting a methodological contradiction: qutrits may obviate the need for T-gate optimizations altogether, but this is not acknowledged in qubit-centric work.

---

### performance — [[2021_Stamatopoulos_TowardsQuantumAdvantage]] vs [[2022_Doriguello_QuantumAlgorithmStochastic]]

**Topic:** derivatives-pricing

**Paper A** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Quantum gradient estimation algorithms (GAW) demonstrate O(√k/ϵ) scaling for k-dimensional gradients, with empirical results showing 200x and 125x lower oracle calls than theoretical bounds for European and basket options, respectively.

**Paper B** ([[2022_Doriguello_QuantumAlgorithmStochastic]]):
> The quantum LSM algorithm achieves ˜O(T²m⁴/ϵ) runtime for stochastic optimal stopping problems, with exponential dependence on T noted as a potential limitation, and no explicit comparison to gradient-based methods.

**Analysis:** Stamatopoulos et al. present empirical evidence of quantum advantage in gradient estimation with polynomial scaling, while Doriguello et al. highlight exponential dependence on T as a bottleneck for their algorithm, suggesting that the two approaches may not be directly comparable but imply differing performance trade-offs for derivatives pricing.

---

### noise-resilience — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** derivatives-pricing

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan maintains a 100% in-constraints rate (feasible solutions) on real hardware, unlike penalty-term-based QAOA, which often violates constraints.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> The total error in VQAs for solving differential equations (DEs) is bounded by the sum of parameter error (from RKM truncation and shot noise) and representation error (from the quantum ansatz), with shot noise error scaling as O(1/√N_meas), highlighting significant resource bottlenecks for large-scale problems.

**Analysis:** Paper A claims Rasengan's robustness in maintaining feasible solutions on real hardware, while Paper B emphasizes the inherent noise and error challenges in VQAs, particularly shot noise, which could undermine the feasibility of maintaining high solution quality in noisy environments.

---

### scalability — [[2022_Doriguello_QuantumAlgorithmStochastic]] vs [[2026_Dechant_ErrorResourceEstimates]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Doriguello_QuantumAlgorithmStochastic]]):
> For n-times differentiable continuation values, the quantum LSM algorithm achieves a runtime of ˜O(5T/ϵ), showing a quadratic improvement over the classical ˜O((5T/ϵ)²) runtime.

**Paper B** ([[2026_Dechant_ErrorResourceEstimates]]):
> The number of quantum circuit evaluations in variational quantum algorithms (VQAs) for solving differential equations scales quadratically with the number of variational parameters (NV), highlighting a significant resource bottleneck for large-scale problems.

**Analysis:** Paper A claims a quadratic speedup for quantum LSM under smoothness assumptions, while Paper B highlights that VQAs (another class of quantum algorithms for financial problems) face quadratic scaling in circuit evaluations with problem size. This tension suggests that theoretical speedups may not translate to practical scalability due to resource constraints.

---

### feasibility — [[2022_Saha_IntermediateQutritBased]] vs [[2020_Miyamoto_ReductionQubitsQuantum]]

**Topic:** derivatives-pricing

**Paper A** ([[2022_Saha_IntermediateQutritBased]]):
> The qutrit-based approach reduces overall CNOT-cost to 162 million (vs. 12 billion T-cost in qubit-only) and circuit depth to 162 million (vs. 378 million in qubit-only) for derivative pricing, with a 40% reduction in error probability for Toffoli count of 30.

**Paper B** ([[2020_Miyamoto_ReductionQubitsQuantum]]):
> The trade-off for qubit reduction in quantum Monte Carlo simulations is increased circuit depth, which may limit practical implementation on near-term quantum hardware without error correction.

**Analysis:** Paper A claims significant resource reductions (CNOT-cost and circuit depth) using qutrits for derivative pricing, while Paper B argues that qubit reduction methods (for Monte Carlo) increase circuit depth, posing feasibility challenges. This tension arises from differing approaches (qutrits vs. qubit reduction) and their implications for near-term hardware.

---

### performance — [[2026_Jiang_RasenganTransitionHamiltonian]] vs [[2026_Barbaresco_QuantumAmplitudeEstimation]]

**Topic:** derivatives-pricing

**Paper A** ([[2026_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan achieves a 379× improvement in solution quality over baseline methods on real-world quantum platforms (IBM Kyiv and Brisbane) for constrained binary optimization problems, with a 100% in-constraints rate.

**Paper B** ([[2026_Barbaresco_QuantumAmplitudeEstimation]]):
> QAE variants failed to estimate non-zero expected payoffs for European call options due to resolution limitations, returning zero values despite classical methods yielding positive payoffs.

**Analysis:** Paper A claims empirical success for Rasengan in optimization problems on real hardware, while Paper B demonstrates a practical failure of QAE in derivatives pricing. This tension suggests that quantum algorithm performance may vary significantly across financial applications (optimization vs. pricing).

---

### feasibility — [[2016_Petrosyan_GroverSearchAlgorithm]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** fraud-detection

**Paper A** ([[2016_Petrosyan_GroverSearchAlgorithm]]):
> The Grover search algorithm achieves measurable success probabilities for correct outcomes in registers of k = 2, 3, and 4 atoms (N = 2^k) under realistic experimental conditions, with performance degrading as decay and dephasing rates increase.

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> Quantum Neural Networks (QNNs) achieved 95% accuracy on the Fashion-MNIST dataset in complex pattern recognition tasks, implying high performance on large-scale, high-dimensional data.

**Analysis:** Paper A demonstrates Grover's algorithm's success is limited to small-scale registers (k ≤ 4) due to decoherence, while Paper B claims high accuracy (95%) for QNNs on large-scale datasets without addressing decoherence or scalability constraints. This creates tension about the practical feasibility of quantum algorithms for high-dimensional tasks like fraud detection.

---

### performance — [[2025_Ganguly_HybridClassicalQuantum]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** fraud-detection

**Paper A** ([[2025_Ganguly_HybridClassicalQuantum]]):
> QLSTM test predictions for NVIDIA stock data were slightly superior to classical LSTM around volatile peaks, but classical LSTM achieved lower RMSE (12.8×10⁻³ vs. 15.09×10⁻³) and faster training times.

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> Quantum Reinforcement Learning (QRL) achieved 94% accuracy on Financial Time-Series Data, implying superior performance over classical methods.

**Analysis:** Paper A shows QLSTM underperforming classical LSTM in RMSE and training time, while Paper B claims high accuracy (94%) for QRL on financial time-series data without addressing classical benchmarks. This suggests differing conclusions about quantum advantage in temporal financial modeling.

---

### feasibility — [[2016_Petrosyan_GroverSearchAlgorithm]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** high-frequency-trading

**Paper A** ([[2016_Petrosyan_GroverSearchAlgorithm]]):
> The Grover search algorithm achieves measurable success probabilities for correct outcomes in registers of k = 2, 3, and 4 atoms (N = 2^k) under realistic experimental conditions, with performance degrading as decay and dephasing rates increase.

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems.

**Analysis:** While Paper A demonstrates Grover's algorithm working under realistic noise conditions for small-scale problems (k ≤ 4), it does not claim to outperform classical baselines or achieve high solution quality on real hardware. Paper B explicitly claims Rasengan is the first to outperform feasible solution baselines on real hardware, suggesting a tension in the feasibility and performance of quantum algorithms for optimization tasks on current hardware.

---

### noise-resilience — [[2016_Petrosyan_GroverSearchAlgorithm]] vs [[2026_Azfar_ShallowRobustQaoa]]

**Topic:** high-frequency-trading

**Paper A** ([[2016_Petrosyan_GroverSearchAlgorithm]]):
> The Grover algorithm's tolerance for moderate errors suggests that error correction may not be strictly necessary for small-scale implementations, as majority voting over multiple runs could yield correct results.

**Paper B** ([[2026_Azfar_ShallowRobustQaoa]]):
> Heavy post-processing error mitigation (e.g., ZNE, Pauli twirling) is less effective than lightweight error suppression (e.g., dynamical decoupling) for QAOA, contradicting some prior literature on mitigation strategies.

**Analysis:** Paper A suggests that error correction or mitigation may not be necessary for small-scale Grover implementations due to inherent error tolerance. Paper B, however, finds that heavy error mitigation techniques degrade performance for QAOA, implying that error resilience strategies are not universally effective and may depend on the algorithm or hardware context.

---

### quantum-advantage — [[2023_Vishwakarma_QuantumComputingAlgorithms]] vs [[2025_Gibadullin_QuantumAlgorithmsSolving]]

**Topic:** high-frequency-trading

**Paper A** ([[2023_Vishwakarma_QuantumComputingAlgorithms]]):
> HQG-CA achieved 96.2% algorithmic speedup correlation, 97.5% accuracy correlation, and 98.3% scalability correlation compared to classical methods in simulation experiments, outperforming classical alternatives.

**Paper B** ([[2025_Gibadullin_QuantumAlgorithmsSolving]]):
> Quantum algorithms, including VQE, Grover’s algorithm, and QAOA, are applied to dynamic control problems, showing numerical optimization results for differential equation-based systems with minimal objective function values (e.g., 0.4047 for linear systems).

**Analysis:** Paper A claims near-perfect performance correlations (96-98%) for HQG-CA in simulations, suggesting a strong quantum advantage. Paper B, however, presents quantum algorithms as tools for numerical optimization with modest results (e.g., minimal objective function values), without claiming comparable performance advantages. This creates tension in the perceived quantum advantage for optimization tasks.

---

### performance — [[2023_Vishwakarma_QuantumComputingAlgorithms]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** high-frequency-trading

**Paper A** ([[2023_Vishwakarma_QuantumComputingAlgorithms]]):
> HQG-CA demonstrated 97.5% accuracy correlation in solving nonlinear optimization problems in simulations, outperforming classical methods.

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan improves accuracy by 4.12× compared to the state-of-the-art QAOA (Choco-Q) on constrained binary optimization problems across 2000 cases from five domains, achieving a 379× improvement in solution quality on real quantum platforms.

**Analysis:** Paper A claims high accuracy correlation (97.5%) for HQG-CA in simulations, while Paper B claims a 4.12× accuracy improvement for Rasengan over QAOA on real hardware. Both papers suggest strong performance, but the lack of direct comparison between HQG-CA and Rasengan or classical methods makes it unclear whether their claims are reconcilable or represent competing approaches with different strengths.

---

### feasibility — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2026_Azfar_ShallowRobustQaoa]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware, achieving an approximation ratio gap (ARG) as low as 0.01 for small-scale problems.

**Paper B** ([[2026_Azfar_ShallowRobustQaoa]]):
> Linear-Ramp LC-QAOA improves convergence and feasibility compared to standard QAOA, achieving >2% feasibility and recovering the optimal VRP solution in several trials on real hardware (IBM Eagle/Heron).

**Analysis:** Paper A claims Rasengan is the first to outperform feasible solution baselines on real hardware, while Paper B demonstrates that LC-QAOA achieves >2% feasibility and recovers optimal solutions on similar hardware. This suggests that both algorithms may have achieved comparable milestones, but the lack of direct comparison or shared benchmarks creates tension in their claims of being 'first' or most effective.

---

### feasibility — [[2025_Mahmod_StateQuantumComputing]] vs [[2025_JETIR_QuantumFinance]]

**Topic:** market-simulation

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications.

**Paper B** ([[2025_JETIR_QuantumFinance]]):
> The paper claims hybrid models show 'strong potential' for financial decision-making under uncertainty, but acknowledges most studies remain theoretical with limited empirical validation on live financial data.

**Analysis:** Paper A reports a concrete, empirically validated improvement in bond trading optimization using quantum computing, while Paper B asserts that most quantum finance studies lack empirical validation on live data. This creates tension between demonstrated near-term feasibility (Paper A) and broader skepticism about empirical validation (Paper B).

---

### noise-resilience — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2026_Prasad_QuantumAlgorithmsStochastic]]

**Topic:** market-simulation

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Barren plateaus (exponential vanishing of cost function gradients with circuit depth) are a fundamental limitation of VQAs, though mitigation strategies exist.

**Paper B** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> Variational quantum schemes for nonlinear SDEs can avoid barren plateaus through problem-informed ansätze, shallow circuits, and layer-wise training.

**Analysis:** Paper A presents barren plateaus as a fundamental limitation of VQAs, while Paper B claims that specific mitigation strategies (e.g., problem-informed ansätze) can avoid them. This creates tension between the perceived severity of the limitation (Paper A) and the potential for overcoming it (Paper B).

---

### quantum-advantage — [[2024_KI_QuantumFinance]] vs [[2024_Leipold_TrainScalingQuantum]]

**Topic:** portfolio-optimisation

**Paper A** ([[2024_KI_QuantumFinance]]):
> The quantum algorithm achieves a runtime of O(poly(log(TN))) for analyzing data loaded into qRAM, where T is the number of time steps and N is the number of assets, compared to classical O(poly(TN)) runtime.

**Paper B** ([[2024_Leipold_TrainScalingQuantum]]):
> QAOA with Train-and-Scale shows lower empirical scaling exponent (0.044) compared to simulated annealing (0.057) for sampling complexity on instances up to n=100, but no logarithmic runtime advantage is demonstrated.

**Analysis:** Paper A claims a theoretical logarithmic runtime advantage (O(poly(log(TN)))) for quantum algorithms in portfolio optimization, contingent on qRAM implementation. Paper B demonstrates empirical polynomial scaling (not logarithmic) for QAOA on similar problems, highlighting a tension between theoretical claims and observed performance.

---

### feasibility — [[2024_KI_QuantumFinance]] vs [[2025_Autonomous_QAOA]]

**Topic:** portfolio-optimisation

**Paper A** ([[2024_KI_QuantumFinance]]):
> Quantum advantage for portfolio optimization is contingent on efficient qRAM implementation and well-conditioned covariance matrices, which are not yet demonstrated on real hardware.

**Paper B** ([[2025_Autonomous_QAOA]]):
> An agentic framework for end-to-end portfolio optimization using QAOA on cloud quantum simulators achieves consistent normalized measurement distribution means and identifies a dominant portfolio with a Sharpe ratio of 1.62.

**Analysis:** Paper A explicitly states that quantum advantage for portfolio optimization is contingent on qRAM and well-conditioned matrices, neither of which are demonstrated on real hardware. Paper B presents empirical results from QAOA simulations but does not address qRAM or matrix conditioning, creating tension about the feasibility of achieving quantum advantage in practice.

---

### scalability — [[2024_Leipold_TrainScalingQuantum]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2024_Leipold_TrainScalingQuantum]]):
> QAOA with Train-and-Scale shows lower empirical scaling exponent (0.044) compared to simulated annealing (0.057) for sampling complexity on instances up to n=100.

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA solved Markowitz’s mean-variance optimization problem for n=20 assets using 6 qubits, achieving solutions within 92% of classical benchmarks.

**Analysis:** Paper A demonstrates polynomial scaling for QAOA on instances up to n=100, while Paper B reports success for n=20 assets using only 6 qubits. The discrepancy in problem size and qubit efficiency suggests tension in scalability claims, as Paper B implies more efficient qubit usage but does not address larger instances.

---

### quantum-advantage — [[2025_Jiang_RasenganTransitionHamiltonian]] vs [[2025_Huot_CorrectionsEnhancingKnapsack]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan is the first quantum algorithm to outperform the mean quality of feasible solution baselines on real hardware (supported).

**Paper B** ([[2025_Huot_CorrectionsEnhancingKnapsack]]):
> The QAOA-based approach demonstrates potential for practical application in complex financial decision problems, though scalability to larger portfolios is not empirically validated (speculative).

**Analysis:** Paper A claims demonstrated superiority on real hardware, while Paper B highlights the lack of empirical validation for scalability in financial applications. The claims create tension regarding the practical quantum advantage in portfolio optimization.

---

### feasibility — [[2026_Ganguly_AutonomousQuantumAgents]] vs [[2026_Nawaz_ExploringQuantumMachine]]

**Topic:** portfolio-optimisation

**Paper A** ([[2026_Ganguly_AutonomousQuantumAgents]]):
> The agentic framework for quantum portfolio optimization achieved consistent performance (normalized measurement distribution mean of ~0.671) across AWS Tensor Network and QBraid QIR simulators, with the dominant bitstring appearing in 23.55% of shots (7.6x uniform baseline) and a Sharpe ratio of 1.62 for the dominant portfolio.

**Paper B** ([[2026_Nawaz_ExploringQuantumMachine]]):
> Challenges such as quantum noise, scalability, and hardware limitations remain significant barriers to the practical deployment of QML algorithms like QAOA for optimization tasks.

**Analysis:** Paper A presents empirical results demonstrating consistent performance and non-uniform output distributions for QAOA in portfolio optimization, suggesting practical feasibility on simulators. Paper B, however, emphasizes persistent challenges like quantum noise and scalability as significant barriers to real-world deployment, creating tension between demonstrated simulator success and broader feasibility concerns.

---

### feasibility — [[2026_Mahmod_StateQuantumComputing]] vs [[2026_Nawaz_ExploringQuantumMachine]]

**Topic:** portfolio-optimisation

**Paper A** ([[2026_Mahmod_StateQuantumComputing]]):
> Quantum computing has demonstrated experimental and commercial applications in finance, including a 34% accuracy improvement in bond trading optimization by HSBC and IBM using real market data.

**Paper B** ([[2026_Nawaz_ExploringQuantumMachine]]):
> Hybrid quantum-classical systems and advancements in quantum hardware are necessary to enable practical large-scale optimization using QML (speculative).

**Analysis:** Paper A highlights demonstrated commercial applications of quantum computing in finance (e.g., HSBC's 34% accuracy improvement), while Paper B suggests that practical large-scale optimization is still dependent on future advancements in hybrid systems and hardware. This creates tension between current successes and the need for further development.

---

### scalability — [[2021_Bennett_QuantumOptimisationVia]] vs [[2025_Uotila_HigherOrderPortfolio]]

**Topic:** portfolio-optimisation

**Paper A** ([[2021_Bennett_QuantumOptimisationVia]]):
> MAOA's performance is independent of the exact shape of the solution quality distribution, making it robust for large-scale combinatorial optimization problems where distribution tails are uncertain.

**Paper B** ([[2025_Uotila_HigherOrderPortfolio]]):
> QAOA struggles to match the solution quality of exact methods or classical algorithms for higher-order portfolio optimization (HUBO), particularly as qubit counts increase (6-15 qubits tested).

**Analysis:** Paper A claims MAOA is robust and scalable for large-scale combinatorial optimization, while Paper B highlights QAOA's (a related variational algorithm) challenges in scaling and solution quality for higher-order problems, suggesting potential limitations in MAOA's scalability claims.

---

### performance — [[2025_Uotila_HigherOrderPortfolio]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Uotila_HigherOrderPortfolio]]):
> QAOA performance on HUBO problems is benchmarked, with results indicating challenges in matching the solution quality of exact methods or classical algorithms, particularly as qubit counts increase (6-15 qubits tested).

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QAOA on 20-node Max-Cut problems achieved an approximation ratio of ~0.755 at depth p=1, and advanced QAOA variants with tailored mixer Hamiltonians at depth p=2 achieved approximation ratios >0.9 under ideal simulation conditions.

**Analysis:** Paper A highlights QAOA's struggles with solution quality and scalability for higher-order portfolio optimization, while Paper B demonstrates QAOA's strong performance in combinatorial optimization, suggesting tension in QAOA's effectiveness across different problem types.

---

### feasibility — [[2021_Bennett_QuantumOptimisationVia]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** portfolio-optimisation

**Paper A** ([[2021_Bennett_QuantumOptimisationVia]]):
> MAOA's threshold response curve analysis shows reliable navigation to a quality threshold within the low-convergence regime, ensuring maximum amplification of optimal solutions for restricted circuit depths.

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) and by 49× compared to Choco-Q, making it deployable on NISQ devices.

**Analysis:** Paper A claims MAOA is effective for restricted circuit depths, while Paper B argues that Rasengan's circuit depth reductions make it more feasible for NISQ devices, suggesting tension in which algorithm is better suited for near-term hardware.

---

### feasibility — [[2025_Mahmod_StateQuantumComputing]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** quantum-cryptography

**Paper A** ([[2025_Mahmod_StateQuantumComputing]]):
> Quantum computing in healthcare achieved over 97% accuracy in Alzheimer’s detection (vs. 92% classical), 70-75.66% accuracy in cancer radiomics (vs. 69% classical), and 98% accuracy in dermatology skin lesion classification (vs. 81-97% classical).

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> All results are derived from simulations rather than real quantum hardware, and no empirical validation on real quantum hardware is provided.

**Analysis:** Paper A presents supported claims of high accuracy in healthcare applications using quantum computing, while Paper B states that all such results are from simulations and lack empirical validation on real hardware. This creates tension about the current feasibility of quantum computing in healthcare.

---

### performance — [[2025_Vangibhuratha_QuantumMachineLearning]] vs [[2025_Deshmukh_QuantumMachineLearning]]

**Topic:** quantum-cryptography

**Paper A** ([[2025_Vangibhuratha_QuantumMachineLearning]]):
> Quantum machine learning reduces computational time for risk modeling significantly, as demonstrated by JPMorgan’s quantum-powered Monte Carlo simulations.

**Paper B** ([[2025_Deshmukh_QuantumMachineLearning]]):
> All results are derived from simulations rather than real quantum hardware, and challenges such as hardware limitations, noise, and data encoding inefficiencies are noted as barriers to practical deployment.

**Analysis:** Paper A claims significant reductions in computational time for risk modeling based on JPMorgan’s quantum-powered Monte Carlo simulations, while Paper B emphasizes that all such results are from simulations and highlights hardware limitations and noise as barriers. This creates tension about the practical performance of quantum machine learning in real-world settings.

---

### performance — [[2022_Biesner_SolvingSubsetSum]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** regulatory-compliance

**Paper A** ([[2022_Biesner_SolvingSubsetSum]]):
> Gradient descent on Hopfield Networks reliably finds solutions to the subset sum problem for real financial data (190 columns) with 100% accuracy under given constraints, using classical simulations

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications

**Analysis:** Paper A demonstrates 100% accuracy for a specific financial problem (subset sum) using classical methods, while Paper B claims quantum computing provides a 34% improvement in bond trading optimization. The tension arises from the implication that quantum methods may not universally outperform classical approaches in all financial tasks, as Paper A’s classical method achieves perfect accuracy for its problem domain, whereas Paper B’s quantum method shows incremental improvement in a different domain.

---

### quantum-advantage — [[2020_Kommadi_QuantumComputingSolutions]] vs [[2021_Stamatopoulos_TowardsQuantumAdvantage]]

**Topic:** risk-modelling

**Paper A** ([[2020_Kommadi_QuantumComputingSolutions]]):
> Quantum advantage in financial services is projected to emerge with scalable quantum hardware (e.g., 50+ qubits), though current implementations rely on simulations

**Paper B** ([[2021_Stamatopoulos_TowardsQuantumAdvantage]]):
> Quantum advantage threshold for financial risk computation is lowered from 50MHz to 7MHz logical clock rate (7x improvement) based on empirical resource estimates

**Analysis:** Paper A suggests quantum advantage requires 50+ qubits, while Paper B claims quantum advantage is achievable with significantly lower logical clock rates (7MHz) based on empirical resource estimates, indicating a tension in the hardware requirements for quantum advantage.

---

### performance — [[2021_Kolotouros_EvolvingObjectiveFunction]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** risk-modelling

**Paper A** ([[2021_Kolotouros_EvolvingObjectiveFunction]]):
> Ascending-CVaR achieves up to ten times greater overlap with the ideal state compared to standard objective functions and constant CVaR in Portfolio Optimization and Number Partitioning problems, and an 80% improvement in Max-Cut problems, based on simulation results with up to 20 qubits

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> Barren plateaus (exponential vanishing of cost function gradients with circuit depth) are a fundamental limitation of VQAs, though mitigation strategies exist

**Analysis:** Paper A demonstrates strong performance improvements in simulations, while Paper B highlights barren plateaus as a fundamental limitation of variational quantum algorithms (VQAs). This creates tension between the observed performance gains and the scalability challenges posed by barren plateaus.

---

### scalability — [[2025_Cai_EnhancingQuantumApproximate]] vs [[2025_Jiang_RasenganTransitionHamiltonian]]

**Topic:** risk-modelling

**Paper A** ([[2025_Cai_EnhancingQuantumApproximate]]):
> CNN-CVaR-QAOA maintains 93% approximation ratio on 26-qubit systems (3-regular graphs, p=3), demonstrating scalability beyond NISQ-era constraints in simulation

**Paper B** ([[2025_Jiang_RasenganTransitionHamiltonian]]):
> Rasengan reduces circuit depth by 1.96× compared to prior variational quantum algorithms (VQAs) and by 49× compared to Choco-Q, making it deployable on NISQ devices; claims 100% in-constraints rate on real hardware for small-scale problems but does not demonstrate scalability to 26 qubits

**Analysis:** Paper A claims CNN-CVaR-QAOA maintains high approximation ratios at 26 qubits in simulation, while Paper B emphasizes Rasengan's NISQ deployability but does not provide evidence of scalability to 26 qubits or comparable approximation ratios. The tension arises from Paper A's simulation-based scalability claim versus Paper B's focus on real-hardware feasibility for smaller problems without addressing larger-scale performance.

---

### performance — [[2026_Prasad_QuantumAlgorithmsStochastic]] vs [[2026_Gnal_ScenarioBasedMacroeconomic]]

**Topic:** risk-modelling

**Paper A** ([[2026_Prasad_QuantumAlgorithmsStochastic]]):
> Quantum algorithms for simulating and solving stochastic differential equations (SDEs) can achieve polynomial and super-polynomial speedups over classical methods for high-dimensional systems, with numerical simulations showing ~3x speedup for 2D Black-Scholes and estimated 10-20x speedup on real hardware.

**Paper B** ([[2026_Gnal_ScenarioBasedMacroeconomic]]):
> Current quantum hardware limitations (noise, limited qubit counts, error propagation) constrain the scalability and reliability of quantum-enhanced forecasting models in the NISQ era.

**Analysis:** Paper A presents theoretical and simulated evidence of quantum speedups for SDEs, including specific performance claims (e.g., 10-20x speedup), while Paper B highlights hardware limitations that could undermine such performance gains in practice. The tension lies in the juxtaposition of theoretical/simulated advantages against real-world hardware constraints.

---

### feasibility — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2020_Kommadi_QuantumComputingSolutions]]

**Topic:** risk-modelling

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QNNs reduced Value-at-Risk calculation time from hours to minutes for derivative portfolios with >500 assets, and variational quantum circuits for VaR calculations reduced calculation variance by 40% compared to classical Monte Carlo methods

**Paper B** ([[2020_Kommadi_QuantumComputingSolutions]]):
> Quantum computing could enable real-time fraud detection and risk optimization in banking, though empirical validation is lacking

**Analysis:** Paper A provides supported claims of specific performance improvements in VaR calculations using QNNs and variational circuits, while Paper B broadly speculates on real-time risk optimization without empirical validation. The tension arises from Paper A's concrete but limited results versus Paper B's unvalidated broader claims.

---

## Low Severity Contradictions

### quantum-advantage — [[2025_Vangibhuratha_QuantumMachineLearning]] vs [[2026_Mahmod_StateQuantumComputing]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Vangibhuratha_QuantumMachineLearning]]):
> Quantum machine learning reduces computational time for risk modeling significantly, as demonstrated by JPMorgan’s quantum-powered Monte Carlo simulations.

**Paper B** ([[2026_Mahmod_StateQuantumComputing]]):
> HSBC and IBM achieved a 34% accuracy improvement in bond trading optimization using quantum computing on real market data, showcasing near-term financial applications.

**Analysis:** Paper A emphasizes computational speedup in risk modeling, while Paper B highlights accuracy improvements in bond trading. Both papers suggest quantum advantage but focus on different metrics (speed vs. accuracy) and applications, making their claims complementary rather than contradictory. However, the different emphases could lead to different conclusions about the primary benefits of quantum computing in finance.

---

### performance — [[2025_Vellaipandiyan_HybridQlstmFramework]] vs [[2025_Vangibhuratha_QuantumMachineLearning]]

**Topic:** high-frequency-trading

**Paper A** ([[2025_Vellaipandiyan_HybridQlstmFramework]]):
> The hybrid QLSTM framework achieved superior performance in stock price prediction, with an R² score of 0.83, MSE of 85.16, and RMSE of 9.23, outperforming classical LSTM (R² of 0.54, MSE of 235.74).

**Paper B** ([[2025_Vangibhuratha_QuantumMachineLearning]]):
> Quantum machine learning offers significant improvements over classical methods in speed, accuracy, and scalability for financial forecasting and portfolio optimization, though current hardware limitations restrict model complexity.

**Analysis:** Paper A provides specific empirical results for QLSTM outperforming classical LSTM, while Paper B makes broader claims about QML's advantages without specifying benchmarks. Both papers agree on quantum improvements but differ in the level of detail and evidence provided, suggesting different emphases rather than a direct contradiction.

---

### performance — [[2024_Chou_QutritBasedQuantum]] vs [[2025_Benamer_VariationalQuantumAlgorithms]]

**Topic:** portfolio-optimisation

**Paper A** ([[2024_Chou_QutritBasedQuantum]]):
> The hybrid strategy combining LS and SS significantly reduces investment risk and improves the trend ratio, as measured by the regression trend line metric, using real-world DJIA index data (2013-2022).

**Paper B** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QNNs in quantum portfolio optimization attained 30% improved Sharpe ratios relative to classical Markowitz models.

**Analysis:** Paper A emphasizes risk reduction and trend ratio improvement using a qutrit-based hybrid strategy, while Paper B focuses on Sharpe ratio improvements using QNNs. Although not directly contradictory, the papers frame performance metrics differently (risk vs. risk-adjusted returns), suggesting different emphases rather than a direct contradiction.

---

### performance — [[2025_Benamer_VariationalQuantumAlgorithms]] vs [[2024_M_OptimizingMutualFund]]

**Topic:** portfolio-optimisation

**Paper A** ([[2025_Benamer_VariationalQuantumAlgorithms]]):
> QNNs achieved 30% improved Sharpe ratios relative to classical Markowitz models and 12% higher Sharpe ratios than classical counterparts in backtesting of S&P 500 futures data.

**Paper B** ([[2024_M_OptimizingMutualFund]]):
> The integrated Quantum-Inspired Evolutionary Algorithm (QEA) and Quantum Neural Network (QNN) framework achieved a Mean Absolute Percentage Error (MAPE) of 5.45% in portfolio return predictions, outperforming traditional methods (MAPE: 5.68%).

**Analysis:** Paper A emphasizes Sharpe ratio improvements using QNNs, while Paper B focuses on predictive accuracy (MAPE) using a quantum-inspired framework. The claims are not directly contradictory but highlight different performance metrics (risk-adjusted returns vs. prediction error), suggesting different emphases.

---

### quantum-advantage — [[2020_Milek_QuantumImplementationRisk]] vs [[2022_Doriguello_QuantumAlgorithmStochastic]]

**Topic:** risk-modelling

**Paper A** ([[2020_Milek_QuantumImplementationRisk]]):
> Quantum computing offers a quadratic speedup over classical Monte Carlo methods for risk measure quantification (e.g., VaR), as claimed by referenced works (Woerner and Egger, 2018)

**Paper B** ([[2022_Doriguello_QuantumAlgorithmStochastic]]):
> The proposed quantum Least Squares Monte Carlo (LSM) algorithm achieves a nearly quadratic speedup in runtime compared to the classical LSM algorithm for stochastic optimal stopping problems under mild assumptions

**Analysis:** Both papers claim a quadratic speedup for quantum methods over classical Monte Carlo, but they focus on different algorithms (VaR vs. LSM) and problem domains, leading to different emphases rather than a direct contradiction.

---
