# Target Performance & Validation Plan: Tidal (Wellness Blood Pressure)

**Source:** [SaMD Product Proposal | FDA Guidance Presentation - Slide 25](https://docs.google.com/presentation/d/1h1glTpD7XYlEqP1WowBcbPP-0QQtpoEJkSPE5Itwe6o/edit?slide=id.g3c336939877_0_19&resourcekey=0-p0ngFOTBLaYWwq7YGEu4OQ#slide=id.g3c336939877_0_19)

---

## 1. Validation Targets

*   **Ground Truth:** Ambulatory Blood Pressure Monitoring (ABPM)
*   **Target Validation Size:** ~2000 participants

### Data Sources
*   **Tidal Preval** (Prevalence Analysis)
*   **Tidal Clinical**
*   **Tidal Labs**
*   **3A Smaller Clinical Validation** (Likely for hard-to-recruit cohort)

### Performance Checkpoints
1.  **1st Performance Checkpoint:** Week of 2/17 (Binary Classification)
2.  **2nd Performance Checkpoint:** 3/4 (3-Bin Classification: Red/Yellow/Green)

### Credibility Plan
*   Publication of results
*   Engagement with Experts

---

## 2. Target Performance Metrics

*   **Metric Basis:** Binary In-Range vs. Out-of-Range Classification (initially).
*   **Prevalence Assumption:** @36.5% Prevalence

| Performance Metric | Sensitivity* (95% CI) | Specificity* (95% CI) |
| :--- | :--- | :--- |
| **Our Target (Office BP)** | **0.54** (0.37, 0.70) | **0.90** (0.84, 0.95) |
| **V1 Algorithm (SPLAT)** (Tidal Clinical Dataset) | **0.53** (0.40, 0.64) | **0.93** (0.86, 0.96) |
| **V1 Algorithm (Raw)** (Tidal Clinical Dataset - Our Paper) | **0.67** (0.54, 0.76) | **0.90** (0.83, 0.94) |

\* *Target set based on U.S. Preventive Services Task Force (USPSTF) Guirguis-Blake et al., JAMA, 2021*

### Notes
*   Ongoing iterations of the algorithm are expected to improve performance further.
*   More analysis for 3-bin classification will be done in early March.
*   Final validation size (TBD) will be finalized after prevalence analysis (end of Feb).
