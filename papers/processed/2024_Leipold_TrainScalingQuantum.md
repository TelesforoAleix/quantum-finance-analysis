---
aliases:
- Train-and-Scaling the Quantum Alternating Operator Ansatz to Solve Portfolio Diversification
- Train Scaling Quantum Alternating
authors:
- Hannes Leipold
- Sarvagya Upadhyay
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1109/QCE60285.2024.10266
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2024 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- QAOA
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_Marshall_QuantumAnnealingPortfolio
- 2022_Herman_QAOALimits
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-25T16:04:18.118028'
step1_model: gpt-5.1
step2_date: '2026-03-25T16:04:22.723256'
step2_model: gpt-5.1
step3_date: '2026-03-25T16:05:16.507903'
step3_model: gpt-5.4
step4_date: '2026-03-25T16:05:36.230321'
step4_model: gpt-5.4
step5_date: '2026-03-25T16:06:15.830645'
step5_model: gpt-5.4
step6_date: '2026-03-25T16:06:24.967896'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/portfolio-optimisation
- method/QAOA
- method/variational
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Train-and-Scaling the Quantum Alternating Operator Ansatz to Solve Portfolio
  Diversification
topic_tags:
- portfolio-optimisation
year: 2024
zotero_key: ''
---

## Abstract summary
The paper introduces a Train-and-Scale method for QAOA-style variational quantum algorithms, where parameters are learned on smaller problem instances and then transferred while gradually increasing both instance size and circuit depth. The authors apply this approach to a Maximum Independent Set formulation of the portfolio diversification problem using SP500 data, training on subgraphs up to 30 assets. They demonstrate that modestly increasing QAOA depth with problem size can maintain good approximation quality and manageable sampling complexity, suggesting a scalable route to applying QAOA to realistic financial optimization tasks.
## Methodology
This conference paper presents an empirical benchmarking study of a proposed training strategy called Train-and-Scale (TnS) for the Quantum Alternating Operator Ansatz applied to portfolio diversification. The financial problem is formulated by computing monthly Pearson correlation matrices from daily S&P 500 stock returns, thresholding correlations at a value λ to build unweighted asset graphs, and then mapping portfolio diversification to a Maximum Independent Set (MIS) problem. The authors use a constrained QAOA/Quantum Alternating Operator Ansatz for MIS, with an all-zero initial state, a cost Hamiltonian based on vertex selection, and a mixer that preserves the independent-set subspace. The core methodological contribution is an iterative curriculum-style training procedure: start with small graph instances and shallow depth, train QAOA parameters on a family of subgraph instances, then increase instance size and circuit depth together by transferring parameters, inserting new layers in the middle of the circuit, training the new layer, and retraining the full circuit. Experiments are conducted on families of subgraphs generated from larger correlation graphs, with 500 instances per size, and training uses parameter-shift-based finite-difference gradient updates with randomized parameter selection, learning-rate decay across 64 epochs, and instance weighting based on approximation-gap statistics. Performance is evaluated using approximation gap/ratio and sampling complexity (inverse success probability), with comparison to simulated annealing for λ = 0.1. The paper appears to be a conference paper with empirical results rather than a short theoretical note.

**Algorithms used:** QAOA, Quantum Alternating Operator Ansatz, Train-and-Scale, simulated annealing, parameter-shift rule

**Experimental setup:** The study uses classical simulation of constrained QAOA on MIS instances derived from S&P 500 correlation graphs. Experiments train on subgraph sizes from n=6 upward, with reported main scaling results up to n=30 for training and evaluation/transfer experiments up to n=100 for some settings. For each instance size, datasets of 500 graphs are generated. Multiple correlation thresholds λ in {0.1, 0.2, 0.3, 0.4, 0.5} are tested. The Train-and-Scale schedule starts at n_min=6 and p_min=6, then increases depth by 2 per size increment in the main experiments, reaching p=54 at n=30.

**Dataset:** Historical daily price data for S&P 500 stocks from a public Kaggle stock-market dataset. After cleaning, each month between 2010 and 2020 contains roughly 350 to 500 stocks. Daily returns are computed per asset, monthly Pearson correlations are estimated, and thresholded correlation graphs are constructed for portfolio diversification instances.
## Findings
- [supported] The paper proposes a Train-and-Scale method that incrementally increases QAOA depth while transferring and retraining parameters on progressively larger portfolio-diversification instances formulated as maximum independent set problems.
- [supported] On SP500-derived correlation graphs, Train-and-Scale produced high-quality solutions from instance sizes n=6 to n=30, with average approximation ratio below 0.4 and modest depth growth up to p=54 for n=30.
- [supported] The authors report that p-depth growing approximately linearly with problem size, described as p=O(n) and implemented as roughly QAOA-2n, maintained solution quality below 0.5 across tested correlation thresholds λ.
- [supported] For λ=0.1, parameters trained up to n=30 and p=54 transferred to larger instances up to n=100 with favorable empirical sampling-complexity scaling.
- [supported] In the reported comparison for λ=0.1, trained QAOA showed a lower empirical scaling exponent for sampling complexity than simulated annealing, 0.044 versus 0.057.
- [supported] The experiments were conducted on classically simulated QAOA using parameter-shift-based training over datasets of 500 graph instances per size, not on quantum hardware.
- [speculative] The authors argue that if the observed polynomial-like scaling in depth and sampling complexity continues to instances with hundreds of variables, the approach could become useful for real portfolio diversification tasks.
- [speculative] The paper suggests Train-and-Scale may help provide high-quality parameters for intermediate-scale quantum systems solving hard graph problems with hundreds of variables in the near future.
- [speculative] The claim that this work reports the largest-size hard optimization instances solved by QAOA-p to date is presented by the authors but is not independently validated within the paper.

**Results summary:** This conference paper introduces Train-and-Scale, a layer-growth and parameter-transfer training strategy for QAOA/Quantum Alternating Operator Ansatz applied to portfolio diversification mapped to maximum independent set on SP500 correlation graphs. Using classically simulated experiments, the authors train on subgraph families from size 6 to 30 and report that a modest, roughly linear increase in circuit depth up to p=54 yields high-quality solutions, with average approximation ratio below 0.4 and manageable sampling complexity for finding optimal solutions. For λ=0.1, the learned parameters also transfer to larger instances up to n=100, where the reported empirical sampling-complexity scaling exponent is lower than that of simulated annealing. The paper does not demonstrate quantum advantage on hardware; broader claims about usefulness at larger scales remain forward-looking.

**Performance claims:**
- Average approximation ratio below 0.4 on SP500-derived portfolio-diversification/MIS instances
- Depth increased to p=54 for n=30
- p-depth scaled approximately as QAOA-2n / p=O(n) while maintaining solution quality below 0.5 across tested λ values
- 500 graph instances used for each instance size
- Training used approximately 2^17 ≈ 130,000 finite-difference/parameter-shift gradient updates
- Sampling probability for solutions did not fall below about 2^-20 in the tested size range
- For λ=0.1, empirical sampling-complexity scaling exponent was 0.044 for trained QAOA versus 0.057 for simulated annealing
- Transferability evaluated from training up to n=30 and p=54, then tested on instances up to n=100
## Quantum advantage claim
**Classification:** speculative

The paper suggests QAOA/Train-and-Scale could be promising for quantum advantage and reports favorable empirical scaling versus simulated annealing, but results are based on classical simulation rather than real quantum hardware and do not establish a demonstrated quantum advantage.
## Limitations
- Experiments are limited to classically simulated QAOA rather than execution on real quantum hardware, so hardware noise, decoherence, gate errors, and connectivity constraints are not evaluated.
- The study only trains directly on subgraph sizes from n = 6 to n = 30, with larger-size behavior inferred through transferability and sampling experiments rather than full end-to-end training at those scales.
- For larger correlation thresholds λ, experiments are curtailed because of higher classical simulation cost; the paper notes 'less for larger λ due to higher classical simulation cost.'
- The dataset is restricted to historical SP500 stock data from 2010 to 2020 after cleaning, limiting coverage across markets, asset classes, and time regimes.
- The authors explicitly note that the dataset has survivorship bias.
- Portfolio diversification is studied through a discretized mapping to Maximum Independent Set using a fixed correlation threshold λ, which may oversimplify real portfolio construction objectives and constraints.
- The graph instances are generated via breadth-first search around randomly selected starting nodes, so results may depend on the induced subgraph generation procedure rather than reflecting the full original market graph structure.
- Training relies on knowledge of the minimum energy to compute the gap and weighting during training, which the authors note can become problematic when sampling complexity is too large.
- The mixer grouping is obtained with a simple randomized algorithm because finding optimal commuting partitions is NP-hard, so circuit depth may not be minimized.
- The work provides empirical evidence of good scaling trends but does not prove that polynomial scaling in depth or sampling complexity will persist to much larger instances.
- [inferred] No direct comparison is provided against stronger state-of-the-art classical portfolio optimization or MIS solvers beyond simulated annealing, limiting claims of competitive advantage.
- [inferred] No statistical significance testing or ablation study is reported to isolate the contribution of warm-start transfer, layer insertion strategy, dataset construction, and hyperparameter choices.
- [inferred] Reproducibility may be limited because the paper does not provide full implementation details such as random seeds, exact optimizer settings for all experiments, or code availability.
- [inferred] The use of parameter-shift/finite-difference-style training with about 130,000 updates suggests substantial training cost, which may hinder scalability in practice.
- [inferred] Because this is a conference paper, page-limit constraints may have restricted discussion of negative results, sensitivity analyses, and implementation details.
## Open questions
- Will the observed modest growth in p-depth and sampling complexity continue for instances with hundreds of variables, as hypothesized by the authors?
- How well does Train-and-Scale perform on real noisy quantum devices compared with classical simulation?
- Can the method avoid barren plateaus and remain trainable at substantially larger depths and problem sizes?
- How sensitive are results to the choice of correlation threshold λ and to different market regimes or asset universes?
- Does training on families of subinstances generalize robustly to unseen real-world portfolio instances outside the SP500-derived dataset?
- How much of the performance gain comes from parameter transfer across instance sizes versus simply increasing circuit depth?
- What is the best strategy for determining target depth p as instance size grows?
- How does the approach compare against stronger classical baselines such as exact branch-and-bound MIS solvers, commercial optimizers, or advanced heuristics tailored to portfolio diversification?
- Can the MIS formulation capture practical financial constraints such as cardinality, turnover, transaction costs, sector exposure, or risk-return tradeoffs without losing trainability?
- How robust is the method to alternative subgraph sampling schemes beyond breadth-first search?

**Future work:**
- Test whether the observed polynomial-like trends in depth and sampling complexity persist for problem instances with hundreds of variables.
- Apply Train-and-Scale on intermediate-sized and near-future quantum systems to solve hard graph problems relevant to portfolio diversification.
- Evaluate the method on real quantum hardware to assess practical performance under noise and hardware constraints.
- Extend Train-and-Scale beyond QAOA/MIS to other variational quantum algorithms and other size-parameterized optimization problems.
- Develop improved methods for selecting or adapting target depth as instance size increases.
- Investigate better mixer-grouping or circuit-compilation strategies to further reduce implementation depth.
- Study transferability of learned parameters across broader datasets, larger instance sizes, and different λ regimes.
- Incorporate more realistic financial formulations beyond thresholded-correlation MIS, including richer portfolio constraints and objectives.
- Benchmark against stronger classical optimization baselines to clarify where, if anywhere, practical quantum advantage may emerge.
- [inferred] Release code, seeds, and detailed experimental protocols to improve reproducibility and enable independent validation.
## Key ideas
- #idea:hybrid-approach — Proposes Train-and-Scale, a hybrid quantum-classical curriculum training strategy for QAOA on portfolio diversification instances mapped to Maximum Independent Set.
- #idea:near-term-feasibility — In classical simulation, gradually increasing depth with problem size (roughly p ≈ 2n) maintains good approximation quality on SP500-derived instances up to n = 30.
- #idea:near-term-feasibility — Parameters learned on smaller instances transfer to larger MIS instances up to n = 100 with favorable empirical sampling-complexity behavior.
- #idea:quantum-advantage — Reports a lower empirical sampling-complexity scaling exponent for trained QAOA than simulated annealing on λ = 0.1 instances, suggesting possible future advantage if trends persist.
- #idea:hybrid-approach — Uses constraint-preserving MIS mixers, warm-start parameter transfer, and layer insertion to improve trainability of deeper QAOA circuits.
## Contradictions
- The paper suggests scalable QAOA performance for portfolio diversification and possible usefulness on hundreds of variables, but the evidence is limited to noiseless classical simulation with full training only up to n = 30 and transfer tests up to n = 100; this conflicts with more skeptical scalability assessments such as 2022_Herman_QAOALimits.
- Its optimistic scaling narrative also contrasts with 2021_Marshall_QuantumAnnealingPortfolio, which reports degradation on larger portfolio-style optimization instances, indicating that favorable small-scale trends may not carry over to realistic problem sizes.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input data consists of historical S&P 500 daily stock prices from Kaggle, covering monthly windows from 2010 to 2020. After cleaning, each month contains approximately 350-500 stocks. Daily returns are computed as percentage price changes, then monthly mean returns, covariances, standard deviations, and Pearson correlations are estimated. For each month, an unweighted graph is created by connecting asset pairs whose absolute correlation exceeds threshold λ. Subgraph instances are generated by breadth-first search around a randomly selected starting node. For benchmarking, datasets D_n^500 with 500 graph instances per size are created for n between 6 and 100 and λ in {0.1, 0.2, 0.3, 0.4, 0.5}. The paper notes survivorship bias in the dataset.

### Process
1. Compute daily returns from cleaned S&P 500 price data and estimate monthly Pearson correlation matrices. 2. Threshold correlations at λ to form unweighted graphs representing portfolio diversification constraints. 3. Generate size-n MIS subgraph instances via breadth-first search from randomly selected seed nodes. 4. Initialize Train-and-Scale with n_min=6 and p_min=6. 5. Train QAOA on the dataset D_n^k for the current size using parameter-shift-based finite-difference gradient updates. 6. For each increase in problem size, transfer the learned parameters to size n+1. 7. Increase target depth, typically by 2 layers per size increment. 8. Insert a new identity layer in the middle of the circuit by inserting zeros into the alpha and beta parameter vectors. 9. Train the newly inserted layer with only the middle layer active, then retrain all circuit parameters jointly. 10. Use approximately 2^17 (~130,000) gradient updates per training stage, selecting one parameter uniformly at random per update. 11. Use an initial learning rate of 0.02, shift size 0.01, and exponentially decay the learning rate over 64 epochs to 0.002. 12. At each epoch, compute energies for each instance, derive approximation gaps, and weight instances according to the standard-deviation range of their gap using temperature parameter beta=1. 13. Evaluate approximation gap and success probability / inverse success probability, and compare sample complexity scaling against simulated annealing for λ=0.1.

### Output
Reported outputs include approximation gap/approximation ratio for QAOA as a function of instance size and correlation threshold, success probability and inverse success probability (sampling complexity) for finding the best solution, and empirical scaling comparisons against simulated annealing. Figures report medians and quartiles over 500 graph instances per size. The paper states average approximation ratio below 0.4 and modest sampling complexity, with p=54 at n=30, and compares empirical scaling exponents of QAOA and simulated annealing for λ=0.1.

### Parameters
- n_min: 6
- p_min: 6
- max_reported_training_size: 30
- max_reported_evaluation_size: 100
- depth_growth_per_size_step: 2
- final_reported_depth_at_n30: 54
- instances_per_size: 500
- lambda_values: [0.1, 0.2, 0.3, 0.4, 0.5]
- gradient_updates_per_training_stage: 131072
- epochs: 64
- initial_learning_rate: 0.02
- final_learning_rate: 0.002
- shift_size: 0.01
- instance_weight_temperature: 1
- initial_state: |0>^n

### Hardware
No real quantum hardware is reported. The experiments rely on classical simulation of QAOA circuits; the specific simulator software, compute environment, and transpilation/noise settings are not specified.

### Reproducibility
Data source is public and described (Kaggle S&P 500 stock dataset), and the paper provides substantial high-level methodological detail on graph construction and training. However, no code repository, simulator implementation details, exact optimizer implementation, or full hyperparameter/configuration details for all experiments are provided, so replication is only partially supported.
