# Algorithm Overview & Target Performance

Original Source: `blood_pressure_wellness_v11.md` (Section 9)

## 9. Target Performance & Validation

### 9.1 Current vs. Target Performance
*   **Metric Basis:** Binary Classification (In-Range vs. Out-of-Range).
*   **Prevalence Assumption:** 36.5%

| Performance Metric | Sensitivity (95% CI) | Specificity (95% CI) | Status |
| :--- | :--- | :--- | :--- |
| **Target (Office BP)** | **0.54** (0.37, 0.70) | **0.90** (0.84, 0.95) | *Goal* |
| **Current V1 (SPLAT Model)** | **0.53** (0.40, 0.64) | **0.93** (0.86, 0.96) | *On Track* |
| **Current V1 (Raw Model)** | **0.67** (0.54, 0.76) | **0.90** (0.83, 0.94) | *Exceeds Sensitivity* |

### 9.2 Validation Plan
*   **Ground Truth:** Ambulatory Blood Pressure Monitoring (ABPM).
*   **Target Sample Size:** ~2,000 participants.
*   **Checkpoints:** Feb 17 (Binary Freeze), Mar 4 (3-Bin Freeze).
