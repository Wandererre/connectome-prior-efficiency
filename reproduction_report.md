# Flyvis Reproduction and Connectome Architecture Benchmark Report

> **Paper**: *Connectome-constrained deep learning models of the fruit fly visual system* (Lappalainen et al., Nature 2024)  
> **Framework**: `flyvis` (PyTorch + `datamate` + `hydra-core`)  
> **Environment**: Windows 11 | NVIDIA GeForce RTX 4050 Laptop GPU (CUDA 12.1) | PyTorch 2.5.1  

---

## 1. Day 1: Connectome Graph Compilation

The 64-cell-type *Drosophila* optic lobe connectome graph was compiled locally across a 15-column hexagonal lattice extent using `ConnectomeFromAvgFilters`:

- **Total Modeled Neurons (Nodes)**: `45,669`
- **Total Modeled Synapses (Edges)**: `1,513,231`
- **Cell Types Included**: 64 cell types across Lamina (L1-L5, R1-R6), Medulla (Mi1, Mi4, Mi9, Tm1, Tm2, Tm4, Tm9, etc.), and Lobula/Lobula Plate (T4a-d, T5a-d).
- **Synaptic Signs**: Biologically mapped excitation (`+1.0`) and inhibition (`-1.0`) derived from neurotransmitter/receptor profiling.

---

## 2. Day 2: Flash Response Simulation (Nature Fig. 1 and 2)

Simulated neural voltage traces for key visual pathway cells in response to full-field and localized ON/OFF flash stimuli (`Flashes` dataset, 4 conditions, 600 time steps):

```carousel
![L1 Flash Responses](file:///C:/Users/Manjunath/.gemini/antigravity/brain/da9e51d6-e737-44fe-967b-a421aa0ce3b0/l1_flash_responses.png)
<!-- slide -->
![Mi1 Flash Responses](file:///C:/Users/Manjunath/.gemini/antigravity/brain/da9e51d6-e737-44fe-967b-a421aa0ce3b0/mi1_flash_responses.png)
```

- **L1 Neurons**: Show clear biphasic hyperpolarization/depolarization responses characteristic of OFF/ON contrast transitions.
- **Mi1 Neurons**: Demonstrate strong ON-pathway selectivity with transient depolarization to luminance increases.

---

## 3. Day 3: Moving Edge and Direction Selectivity (Nature Fig. 2)

Simulated 144 stimulus conditions across 24 cardinal angles using `MovingEdge` to evaluate motion vision circuits (T4/T5 directional cells):

```carousel
![T4a ON Directional Responses](file:///C:/Users/Manjunath/.gemini/antigravity/brain/da9e51d6-e737-44fe-967b-a421aa0ce3b0/t4a_moving_edge_responses.png)
<!-- slide -->
![T5a OFF Directional Responses](file:///C:/Users/Manjunath/.gemini/antigravity/brain/da9e51d6-e737-44fe-967b-a421aa0ce3b0/t5a_moving_edge_responses.png)
```

- **T4a Neurons**: Exhibit sharp directional tuning to ON moving edges along preferred cardinal vectors.
- **T5a Neurons**: Exhibit sharp directional tuning to OFF moving edges along preferred cardinal vectors.

---

## 4. Days 4-5 Plan: Constrained vs. Unconstrained Ablation Experiment

**Core Thesis**: *"Efficiency of Biological Priors"*

We will compare the connectome-constrained Deep Mechanistic Network (DMN) against an unconstrained/randomly wired baseline on the **Optic Flow Estimation Task**:

1. **Constrained Model**: 64-cell-type optic lobe graph (around 734 trainable parameters, 2,959 fixed connectivity weights).
2. **Unconstrained Baseline**: Equal-parameter / equal-sparsity randomly rewired graph with scrambled cell-type connectivity.
3. **Metrics**:
   - Training loss and End-Point Error (EPE) convergence curves over epochs.
   - Sample efficiency (performance when trained on 10%, 25%, 50%, 100% of optic flow frames).
   - Parameter efficiency ratio.
