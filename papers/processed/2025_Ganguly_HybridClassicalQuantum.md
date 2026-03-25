---
aliases:
- Hybrid Classical-Quantum Generative Algorithms for Financial Modelling and Prediction
- Hybrid Classical Quantum Generative
authors:
- Santanu Ganguly
- Xing Liang
- Dimitrios Makris
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1109/IC363308.2025.10956507
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 International Conference on Intelligent Control, Computing
  and Communications (IC3)
methodology_tags:
- quantum-ML
- QUBO
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:08:32.474580'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:08:36.866840'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:09:15.013313'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:09:39.365703'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:10:07.634133'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:10:23.314628'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/asset-pricing
- topic/portfolio-optimisation
- topic/market-simulation
- method/quantum-ML
- method/QUBO
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Hybrid Classical-Quantum Generative Algorithms for Financial Modelling and
  Prediction
topic_tags:
- asset-pricing
- portfolio-optimisation
- market-simulation
year: 2025
zotero_key: ''
---

## Abstract summary
The paper investigates several hybrid classical-quantum machine learning models for financial applications, focusing on generative and sequence prediction tasks. It implements a qGAN on real cryptocurrency data, a QLSTM versus classical LSTM comparison on NVIDIA stock prices, and a QCBM on a synthetic bars-and-stripes dataset, using GPU-accelerated quantum simulators. The study aims to assess potential quantum advantages in modelling financial distributions and time series, finding modest predictive benefits for QLSTM and demonstrating feasibility of these quantum-inspired approaches for financial modelling and asset selection.
## Methodology
This conference paper presents a proof-of-concept empirical study of three hybrid classical-quantum generative/sequence models for finance: a quantum generative adversarial network (qGAN) for cryptocurrency distribution learning and downstream asset selection, a hybrid quantum long short-term memory model (QLSTM) for stock-price time-series prediction benchmarked against a classical LSTM, and a quantum circuit Born machine (QCBM) evaluated on a synthetic bars-and-stripes dataset as a generative modeling testbed. The qGAN uses a parameterized variational quantum circuit as generator and a classical binary neural-network discriminator, trained on real Binance cryptocurrency data after percentile-based outlier trimming and discretization; the learned distribution is then passed to a QUBO optimization stage using pyqubo and cvxpy/CLARABEL to identify the most promising crypto asset. The QLSTM follows the architecture of Chen et al., replacing classical LSTM cells with variational quantum circuit blocks that include data encoding, variational, and measurement layers; it is trained on 210 days of NVIDIA stock data and compared with a classical LSTM using loss curves, RMSE, prediction plots, and a paired t-test on RMSE values. The QCBM is implemented as a layered parameterized quantum circuit with adjustable one-qubit gates and fixed two-qubit gates, trained on a synthetic 2x2 BAS dataset and evaluated by comparing learned and target probability distributions under different optimizers. Experiments are conducted on simulators rather than real quantum hardware, with software including Qiskit, PennyLane, PyTorch, CUDA-Q, cuQuantum/lightning.gpu, and hardware platforms including NVIDIA RTX GPUs and an Apple M3 GPU for performance comparisons.

**Algorithms used:** qGAN, QLSTM, LSTM, QCBM, QUBO, VQC, Adam, SPSA, COBYLA, Nelder-Mead
**Frameworks:** Qiskit, Qiskit Aer, PennyLane, PyTorch, CUDA-Q, cuQuantum, lightning.gpu, pyqubo, cvxpy, CLARABEL

**Experimental setup:** All implementations were run in simulation. qGAN and QCBM coding/simulations were performed on Linux Ubuntu 22.04 LTS using an NVIDIA RTX 3070 GPU with CUDA-Q support; LSTM and QLSTM were run both on NVIDIA-powered platforms and on an Apple M3 MacBook with 30-core GPU. Qiskit simulator/Qiskit Aer was used for quantum circuit simulation, PennyLane for hybrid QML components, PyTorch for classical ML and tensor handling, and lightning.gpu/cuQuantum/CUDA-Q to accelerate quantum simulation. The paper also reports per-epoch training-time comparisons across RTX 3060, RTX 3070, Apple M3 GPU, and CUDA-Q-enabled configurations.

**Dataset:** Three datasets were used: (1) real-world cryptocurrency market data from Binance API for five trading pairs—BNBBTC, ETHBTC, LTCBTC, NEOBTC, and QTUMETH—with more than 5,000 samples for qGAN; (2) real NVIDIA stock-price time-series data covering 210 days up to August 28, 2024 for LSTM/QLSTM forecasting; and (3) a synthetic bars-and-stripes (BAS) binary image dataset of size 2x2 for QCBM.
## Findings
- [supported] On NVIDIA stock data over 210 days, QLSTM achieved lower test loss than classical LSTM (5.5×10^-3 vs 6.8×10^-3), while LSTM achieved lower training loss (4.5×10^-3 vs 7.2×10^-3).
- [supported] On the same stock task, QLSTM had worse RMSE than LSTM on both training and test sets according to the reported table (training RMSE 19.05×10^-3 vs 7.5×10^-3; test RMSE 15.09×10^-3 vs 12.8×10^-3), which conflicts with the paper's narrative that QLSTM predictions were more accurate.
- [disputed] The paper claims QLSTM test predictions are slightly superior to classical LSTM for financial time-series forecasting, but this is only partially supported because the reported test loss favors QLSTM while the reported test RMSE favors LSTM.
- [supported] QLSTM training was substantially slower than classical LSTM across hardware platforms; per-epoch training times without CUDA-Q were 1600s vs 18s on RTX 3060, 780s vs 12s on RTX 3070, and 22s vs 0.05s on Apple M3.
- [supported] CUDA-Q acceleration greatly reduced simulated QLSTM training time, e.g., from 780s to 18s per epoch on RTX 3070 and from 1600s to 500s on RTX 3060.
- [supported] The qGAN was trained on real Binance cryptocurrency data from five pairs with over 5000 samples, using batches of 1000 and 2000 training epochs, and the generator/discriminator losses reportedly behaved as expected and approached equilibrium.
- [supported] After qGAN-based distribution learning and subsequent QUBO optimization, the method selected BNBBTC as the cryptocurrency predicted to offer the maximum return in the studied snapshot.
- [speculative] The authors argue that qGAN produced expected results in fewer iterations than a classical GAN, but no direct classical GAN baseline metrics are reported in the paper.
- [supported] For the QCBM experiment on a synthetic 2×2 bars-and-stripes dataset, SPSA produced a simulated distribution visually close to the target distribution.
- [supported] The QCBM comparison found that SPSA gave the closest simulated distribution to the real distribution, while the text also states COBYLA gave better optimizer results overall, indicating some ambiguity in optimizer ranking.
- [speculative] The paper suggests hybrid combinations of qGAN, QLSTM, and QCBM could yield future benefits for financial modeling, but this integration was not empirically tested here.
- [speculative] Claims of future quantum advantage in finance are based on simulator studies and hardware-acceleration arguments rather than demonstrated end-to-end advantage on quantum hardware.

**Results summary:** This conference paper presents proof-of-concept hybrid quantum-classical generative and sequence models for finance, evaluated primarily in simulation. A qGAN was trained on real Binance cryptocurrency data and, after QUBO optimization, identified BNBBTC as the preferred asset in the examined period; however, no quantitative accuracy or baseline comparison against a classical GAN is reported. For NVIDIA stock prediction over 210 days, QLSTM showed lower reported test loss than classical LSTM but higher training loss and higher RMSE on both train and test sets, making the claimed predictive superiority mixed and internally inconsistent. The paper also reports that QLSTM is much slower to train than LSTM, though CUDA-Q and stronger GPUs substantially reduce simulation time. A QCBM was tested on a synthetic bars-and-stripes dataset, where SPSA produced a distribution visually close to the target. Overall, the work provides simulation-based evidence that hybrid quantum-classical models are feasible for financial tasks, but it does not demonstrate quantum advantage on real quantum hardware.

**Performance claims:**
- QLSTM test loss: 5.5×10^-3 vs LSTM test loss: 6.8×10^-3
- QLSTM training loss: 7.2×10^-3 vs LSTM training loss: 4.5×10^-3
- QLSTM training RMSE: 19.05×10^-3 vs LSTM training RMSE: 7.5×10^-3
- QLSTM test RMSE: 15.09×10^-3 vs LSTM test RMSE: 12.8×10^-3
- QLSTM per-epoch training time on RTX 3060: 1600.0s vs LSTM 18.0s
- QLSTM per-epoch training time on RTX 3070: 780.0s vs LSTM 12.0s
- QLSTM per-epoch training time on Apple 30-core M3 GPU: 22.0s vs LSTM 0.05s
- With CUDA-Q, QLSTM per-epoch training time on RTX 3060: 500.0s vs LSTM 0.5s
- With CUDA-Q, QLSTM per-epoch training time on RTX 3070: 18.0s vs LSTM 0.04s
- qGAN used >5000 cryptocurrency samples, batch size 1000, and 2000 training epochs
- QLSTM used 6 VQCs with 4 qubits each and 292 parameters; LSTM used hidden size 7 and 288 parameters
- VQCs for QLSTM were trained for 50 epochs
## Quantum advantage claim
**Classification:** speculative

The paper discusses potential future quantum advantage and reports simulator-based proof-of-concept results for qGAN, QLSTM, and QCBM, but all experiments are simulation-based rather than on real quantum hardware, and no clear end-to-end advantage over strong classical baselines is demonstrated.
## Limitations
- The study is explicitly presented as a proof-of-concept rather than a production-scale evaluation.
- Most experiments were conducted on simulators (Qiskit simulator, PennyLane, CUDA-Q simulation) rather than on real quantum hardware, so hardware noise and device constraints were not empirically validated.
- QLSTM was evaluated on only 210 days of NVIDIA stock data, which is a small and narrow dataset for financial time-series forecasting.
- The qGAN experiment used only five cryptocurrencies from Binance, limiting generalizability across broader asset classes and market regimes.
- The QCBM evaluation used a synthetic BAS toy dataset rather than real financial data, limiting the relevance of conclusions for practical finance applications.
- For qGAN, samples below the 5th percentile and above the 95th percentile were discarded to reduce qubit requirements, which may remove important tail events that are especially relevant in finance.
- The qGAN representation used only 5 qubits (32 discrete values), constraining distribution fidelity and limiting scalability to richer financial distributions.
- The QLSTM implementation used only 4 qubits per variational circuit and 6 VQCs, indicating a small-scale setup that may not reflect performance on larger realistic problems.
- Training efficiency for QLSTM was substantially worse than classical LSTM and highly dependent on GPU/simulation stack, raising concerns about practical scalability.
- The paper reports mixed performance signals: QLSTM had slightly better test predictions, but LSTM performed marginally better over 50 epochs and had lower training RMSE, making the claimed advantage inconclusive.
- The paper does not report extensive robustness checks across multiple stocks, longer horizons, or repeated runs under different random seeds. [inferred]
- No direct benchmarking against stronger classical baselines beyond standard LSTM is provided (e.g., GRU, Transformer, ARIMA, XGBoost, modern time-series models). [inferred]
- The statistical significance analysis is only briefly mentioned and not fully detailed, limiting reproducibility and confidence in the reported differences. [inferred]
- The qGAN claim that it achieved expected results in fewer iterations than a classical GAN is not supported by a direct controlled experimental comparison in the paper. [inferred]
- The study does not provide enough implementation detail such as hyperparameter search protocol, seed control, and full training configuration to ensure full reproducibility. [inferred]
- No experiments assess behavior under real market frictions, transaction costs, slippage, or deployment constraints, limiting financial applicability. [inferred]
- The conference-paper format likely constrains methodological and experimental detail due to page limits. [inferred]
## Open questions
- Will the reported QLSTM advantage on test predictions persist on larger, more diverse financial datasets and across multiple assets?
- How would qGAN, QLSTM, and QCBM perform on real quantum hardware under realistic noise, decoherence, and connectivity constraints?
- Can these hybrid models scale beyond the small qubit counts and toy/small datasets used in this study?
- Does discarding tail observations to fit qubit constraints undermine the usefulness of qGAN for risk-sensitive financial tasks such as option pricing and stress analysis?
- Under what conditions, if any, do hybrid quantum models provide a consistent advantage over stronger classical forecasting baselines?
- Can QCBM trained on real financial distributions outperform classical generative models such as RBMs or other deep generative approaches in practice?
- How stable are the reported results across different random initializations, train/test splits, and market regimes? [inferred]
- What is the true source of the slight QLSTM improvement: quantum expressivity, simulation artifacts, or implementation choices? [inferred]
- Can the proposed integration of qGAN, QLSTM, and QCBM yield measurable end-to-end benefits for financial decision-making rather than isolated proof-of-concept gains?
- What are the computational cost trade-offs between any predictive gain and the much higher training burden of QLSTM?

**Future work:**
- Test the proposed methods on real quantum hardware rather than only simulators.
- Further investigate combinations of qGAN, QLSTM, and QCBM to improve training and prediction performance.
- Explore tighter integration between QLSTM and qGAN for potentially better efficiency.
- Extend research toward temporal financial data applications where combined hybrid models may provide benefits.
- Leverage more advanced quantum simulation and hardware stacks such as NVIDIA DGX Quantum/CUDA-Q for improved performance.
- Apply QCBM beyond the synthetic BAS dataset to more realistic financial datasets.
- Increase training time and fine-tuning of QLSTM to assess whether stronger performance gains emerge.
- Validate the methods on broader real-world financial datasets, including more stocks, longer time periods, and additional asset classes. [inferred]
- Benchmark against stronger state-of-the-art classical models to determine whether any quantum advantage is genuine. [inferred]
- Study robustness, reproducibility, and statistical significance more systematically across repeated experiments. [inferred]
- Investigate noise-aware and hardware-aware implementations to bridge the gap between simulation results and deployable quantum finance workflows. [inferred]
## Key ideas
- #idea:hybrid-approach — The paper studies hybrid quantum-classical models (qGAN, QLSTM, QCBM) for financial distribution learning, time-series prediction, and downstream decision support.
- #idea:near-term-feasibility — qGAN was trained on real cryptocurrency data and QLSTM on real NVIDIA stock data, suggesting proof-of-concept applicability of hybrid QML to finance in the NISQ/simulation era.
- #idea:hybrid-approach — A learned qGAN distribution is fed into a QUBO-based optimization stage to select a cryptocurrency asset, illustrating an end-to-end hybrid modelling-plus-optimization pipeline.
- #idea:quantum-advantage — The paper suggests QLSTM may offer slight predictive benefits on stock forecasting based on lower reported test loss and qualitative prediction behavior in volatile regions.
- #idea:near-term-feasibility — GPU-accelerated simulators and CUDA-Q substantially reduce training time for simulated quantum models, which the paper frames as a practical enabler for experimentation.
- #idea:hybrid-approach — QCBM is explored as a variational generative model testbed, though only on a synthetic bars-and-stripes dataset rather than real financial data.
## Contradictions
- The paper implies QLSTM can outperform classical LSTM, but its own reported RMSE values favor the classical LSTM on both train and test sets, so the superiority claim is internally inconsistent. This supports #contradiction:classical-vs-quantum.
- The paper discusses potential quantum advantage, yet all experiments are performed via classical simulation and the quantum models are far slower to train than classical baselines, undermining any practical superiority claim. This supports #contradiction:classical-vs-quantum.
- The work speculates about broader financial usefulness, but the experiments use very small qubit counts, a narrow 210-day single-stock dataset, only five crypto assets, and a toy BAS dataset, which conflicts with implications of scalability to realistic finance problems. This supports #contradiction:scalability.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
For qGAN, Binance API data for five cryptocurrencies (BNBBTC, ETHBTC, LTCBTC, NEOBTC, QTUMETH) with >5,000 samples were used; samples below the 5th percentile and above the 95th percentile were discarded to reduce qubit requirements, then values were discretized into 2^5 = 32 bins/discrete values and converted to tensors in PyTorch. For QLSTM/LSTM, NVIDIA stock data spanning 210 days until 2024-08-28 were used as a time-series prediction task with the same number of features for both models, though the exact feature set and preprocessing beyond quantum encoding are not fully specified. For QCBM, a synthetic 2x2 BAS dataset of binary images was generated following Benedetti et al.; basis encoding was used to map binary pixel values to qubits.

### Process
For qGAN: (1) load Binance cryptocurrency data; (2) trim extreme values outside the 5th-95th percentile range; (3) discretize samples into 32 values; (4) convert arrays to PyTorch tensors; (5) construct a parameterized quantum generator circuit and a classical discriminator; (6) create a Qiskit Aer quantum instance where batch size defines the number of shots; (7) train using batches of 1,000 for 2,000 epochs with Adam optimization; (8) inspect generator/discriminator loss convergence and histogrammed learned distributions; (9) pass trained outputs to a QUBO optimization stage using pyqubo and cvxpy with CLARABEL to select the crypto asset with maximum predicted return. For QLSTM/LSTM: (1) implement a classical LSTM in PyTorch and a QLSTM inspired by Chen et al.; (2) in QLSTM, replace LSTM cells with 6 variational quantum circuit blocks, each including a data-encoding layer with Hadamard and Ry/Rz rotations, a variational layer, and a measurement layer; (3) encode classical stock inputs into quantum states; (4) train both models for 50 epochs using Adam; (5) compare training and test predictions, loss curves, RMSE, and training time across GPU platforms; (6) perform a paired t-test on RMSE values for significance assessment. For QCBM: (1) generate synthetic BAS data; (2) basis-encode binary images into qubit states; (3) define a layered QCBM ansatz with 5 layers of adjustable one-qubit and fixed two-qubit gates; (4) verify state-vector/histogram properties; (5) optimize the model using alternative optimizers (COBYLA, SPSA, Nelder-Mead); (6) compare simulated and target probability distributions, with SPSA reported as closest to the real distribution.

### Output
The qGAN outputs generator and discriminator loss curves and histogram-based learned distributions over discretized crypto variables, followed by a downstream asset-selection result indicating BNBBTC as the best predicted crypto asset. The QLSTM/LSTM experiments report training loss, test loss, RMSE for train and test sets, prediction plots against real NVIDIA stock data, GPU-dependent training time per epoch, and a paired t-test on RMSE values; the main baseline is classical LSTM, with QLSTM reported as slightly better on test prediction accuracy but slower in training. The QCBM outputs histogram/state-vector checks, circuit decomposition visualizations, and comparisons between learned and true probability distributions under different optimizers, with SPSA visually closest to the target distribution.

### Parameters
- qGAN: {'qubits': 5, 'discretization_levels': 32, 'batch_size': 1000, 'epochs': 2000, 'optimizer': 'Adam', 'data_filtering': 'discarded samples below 5th percentile and above 95th percentile'}
- QLSTM: {'epochs': 50, 'optimizer': 'Adam', 'num_vqcs': 6, 'qubits_per_vqc': 4, 'total_parameters': 292}
- LSTM: {'hidden_size': 7, 'total_parameters': 288, 'epochs': 50, 'optimizer': 'Adam'}
- QCBM: {'layers': 5, 'optimizers_compared': ['COBYLA', 'SPSA', 'Nelder-Mead'], 'encoding': 'Basis encoding', 'dataset_image_size': '2x2'}

### Hardware
No real QPU was used. Quantum experiments were simulated with Qiskit simulator/Qiskit Aer. qGAN and QCBM were run on NVIDIA RTX 3070 GPU under Linux Ubuntu 22.04 LTS with CUDA-Q; QLSTM/LSTM were also run on Apple M3 30-core GPU and NVIDIA RTX 3060/3070 platforms. lightning.gpu and cuQuantum were used to accelerate PennyLane/QML workloads. Reported per-epoch times include: RTX 3060 (QLSTM 1600.0s, LSTM 18.0s), RTX 3070 (QLSTM 780.0s, LSTM 12.0s), Apple M3 GPU (QLSTM 22.0s, LSTM 0.05s), RTX 3060 with CUDA-Q (QLSTM 500.0s, LSTM 0.5s), RTX 3070 with CUDA-Q (QLSTM 18.0s, LSTM 0.04s).

### Reproducibility
The paper provides substantial methodological detail on datasets, software stack, model types, some hyperparameters, and hardware timing, but reproducibility is only partial. No public code repository is mentioned in the provided text. Data sources are partly public (Binance API, NVIDIA stock data), and synthetic BAS data is reproducible in principle. However, several implementation details are missing or underspecified, such as exact NVIDIA feature engineering, train/test split procedure, circuit depth/ansatz specifics for all models, shot counts beyond the qGAN batch-size-as-shots statement, and full optimizer settings.
