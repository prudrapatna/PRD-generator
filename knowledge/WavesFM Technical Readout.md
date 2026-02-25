# WavesFM: Waveform Foundation Model - Technical Readout

## 1. Overview
**WavesFM** is a multimodal, multiscale waveform foundation model designed to unlock cardiometabolic insights for the Personal Health Assistant (PHA). It captures high-fidelity sensor data (PPG, ACC) to create powerful embeddings for downstream health tasks.

## 2. Key Attributes
- **Multimodal Inputs:** Processes PPG (Green), 3-axis Accelerometer (ACC), and height.
- **Multiscale Resolution:** Analyzes data across time scales from seconds (for time-varying tasks like meal detection) to days/weeks (for chronic conditions like hypertension).
- **Shape Importance:** Research proves BP info is captured in the *shape changes* of PPG and BCG (Ballistocardiogram from Accelerometer) waveforms.

## 3. Data & Scale
- **Pretraining Scale:** Scaled from 1k individuals (0.5M hours) in v0 to **400k individuals (1.3M hours)** in v1.
- **Complements SPLAT/LSM:** WavesFM works alongside SPLAT (Sensor Compression) and Large Sensor Models (LSM) to capture the full space of sensor data.

## 4. Performance Validation (Hypertension)
WavesFM-v1 meets or exceeds target KPIs for detecting hypertension (HTN) defined as 24-hr ABPM ≥130/80 mmHg.

| Study | N | Sensitivity | Specificity |
| :--- | :--- | :--- | :--- |
| **Tidal Clinical** | 196 | 61.8% | 92.5% |
| **Tidal Prevalidation** | 259 | 60.9% | 90.0% |

**Note on Office BPM:** Clinical validation shows that WavesFM-v1 is more sensitive than traditional Office Blood Pressure Measurements in certain cohorts (Office BP sensitivity was as low as 20.3% in the Preval study).

## 5. Cardiometabolic Expansion
The foundation model shows early promise for indicators beyond blood pressure:
- **Prediabetes (HbA1c ≥ 5.7%):** AUROC 0.77 - 0.78 (Outperforms demographics-only models).
- **Borderline High LDL (≥ 130 mg/dL):** AUROC 0.61 - 0.63 (Early stage development).

## 6. Technical Components
- **Waveform Encoder:** Converts raw sensor data into embeddings.
- **Temporal Encoder:** Processes embeddings over longitudinal windows.
- **On-Device/Backend:** Embeddings can be generated on-device or on the backend for HTN scoring via Logistic Regression.

## 7. Development Limiters
- **Storage/Compute:** Requires 10s of petabytes capacity for raw sensor data in Tier 2 ARDS.
- **TPU Allocation:** Critical for training velocity and inference.
- **Ingestion:** Needs acceleration of PHL/PHR ingestion paired with PPG-FM.

## 8. 2026 Key Takeaways
1. **KPI Success:** Passed KPIs for Tidal Algo across all major datasets.
2. **Production:** Integrating waveform AI into the production pipeline.
3. **Future:** Continuing to improve the AI to unlock more cardiometabolic indicators.
