# Waveform Foundation Readout

**Presentation Title:** Waveform Foundation Readout
**Presentation ID:** 1QB1MHLxUtkfnN1GQ7hTKVTYmg-0eWjlNJiOmwWWfjnM

---

## Slide 1
![Slide 1 Thumbnail](./thumbnails/slide_01.png)

**WavesFM**
**Readout**
**Ming Zher Po, Paolo Achille, Pramod Rudrapatna**

---

## Slide 2
![Slide 2 Thumbnail](./thumbnails/slide_02.png)

**Confidential & Proprietary**
1. Overview of Waveform Foundation
2. Tidal Preval Readout
3. Early promising for other cardiometabolic indicators
4. Next steps

**Agenda**

---

## Slide 3
![Slide 3 Thumbnail](./thumbnails/slide_03.png)

**Confidential & Proprietary**
**What are we building**
Multimodal Waveform Foundation model to enable us to unlock cardiometabolic insights to make PHA more actionable

---

## Slide 4
![Slide 4 Thumbnail](./thumbnails/slide_04.png)

**WavesFM: A multimodal, multiscale waveform foundation model**
A foundation model that creates representations of multimodal waveform time series across multiple time resolutions, from seconds to days.
- Chronic-condition Downstream task (e.g. hypertension, diabetes detection)
- Time-varying Downstream task (e.g. continuous BP, glucose pred)
- ACC: seconds to minutes
- Days to weeks
1. Flexible inputs, multimodal waveforms
2. Multi-scale resolutions

---

## Slide 5
![Slide 5 Thumbnail](./thumbnails/slide_05.png)

**Why is waveform shape important?**
Our previous study has shown that BP info is captured in PPG and BCG (from accel) shape changes.
*Di Achille et al. (Manuscript under review at Nature)*

---

## Slide 6
![Slide 6 Thumbnail](./thumbnails/slide_06.png)

**Behavioral and derived health features alone are likely insufficient to infer certain health conditions**
- Systolic BP
- Hyperlipidemia (self report)
- Prediabetes (HbA1c ≥ 5.7%)
*LSM-v3 Performance on WEAR-ME dataset. Naraswarmy et al., Manuscript in preparation, 2026*

---

## Slide 7
![Slide 7 Thumbnail](./thumbnails/slide_07.png)

**WavesFM complements SPLAT and LSM**
Together, they capture a fuller space of sensor data to create powerful embeddings for health applications.
- SPLAT Tokens (LSM-v4)
- Sensor Compression (SPLAT)
- Large Sensor Model (LSM)
- Waveform Foundation Model (WavesFM)

---

## Slide 8
![Slide 8 Thumbnail](./thumbnails/slide_08.png)

**WavesFM is on par with state of the art foundation models**
Scaled from pretraining on N=1k (0.5M hours) for v0 to N=400k (1.3M hours) individuals for v1.

---

## Slide 9
![Slide 9 Thumbnail](./thumbnails/slide_09.png)

**Tidal is the first direct application of WavesFM**
Embeddings from WavesFM allows detection of high BP (hypertension).
- Tidal Algo
- Logistic Regression
- HTN score
- On-device vs Backend

---

## Slide 10
![Slide 10 Thumbnail](./thumbnails/slide_10.png)

**Criteria for HTN & Target Performance**
Based on global standards (ISH 2020) and target performance chosen to be on par with office blood pressure.
- Target: Lower 95% CI: Sensitivity ≥ 37%, Specificity ≥ 84%
- Office BP Screening: Sensitivity 54% (37, 70), Specificity 90% (84, 95)

---

## Slide 11
![Slide 11 Thumbnail](./thumbnails/slide_11.png)

**Development and Validation of Tidal Algo**
Three distinct study cohorts:
- Tidal Datafood (Training): N=663
- Tidal Clinical (Validation #1): N=196
- Tidal Preval (Validation #2): N=259

---

## Slide 12
![Slide 12 Thumbnail](./thumbnails/slide_12.png)

**Demographics of Study Populations (Part 1)**
- Comparison of Age, BMI, 24H SBP/DBP, and Skin Tone (MST) across Training, Validation #1, and Validation #2 cohorts.

---

## Slide 13
![Slide 13 Thumbnail](./thumbnails/slide_13.png)

**Demographics of Study Populations (Part 2)**
- Comparison of Race/Ethnicity, ITA/Fitzpatrick skin types across cohorts.

---

## Slide 14
![Slide 14 Thumbnail](./thumbnails/slide_14.png)

**Demographics of Study Populations (Part 3)**
- Comparison of Office BPM vs 24h/Daytime/Nighttime ABPM and HTN prevalence (ISH/JNC7 vs ACC/AHA).

---

## Slide 15
![Slide 15 Thumbnail](./thumbnails/slide_15.png)

**Validation #1: Tidal Clinical**
Version 0 of WavesFM met KPIs in a prospective, multicenter study (N=196).
- WavesFM-v0-G met targets for Sensitivity (>37% low CI) and Specificity (>84% low CI).

---

## Slide 16
![Slide 16 Thumbnail](./thumbnails/slide_16.png)

**Validation #1: Tidal Clinical (v1)**
Version 1 also met KPIs and showed comparable performance to office BP.

---

## Slide 17
![Slide 17 Thumbnail](./thumbnails/slide_17.png)

**Validation #2: Tidal Prevalidation**
Interim analysis: WavesFM meets endpoints (N=259).
- WavesFM-v1-G: Sensitivity 60.9% (✔48.4, 72.4), Specificity 90.0% (✔84.8, 93.9).

---

## Slide 18
![Slide 18 Thumbnail](./thumbnails/slide_18.png)

**Office BPM Performance**
Performance in Tidal Clinical was pooled across multiple devices, whereas in Preval only a single model (Welch Allyn ProBP 2000) was used.

---

## Slide 19
![Slide 19 Thumbnail](./thumbnails/slide_19.png)

**Office BPM Low Sensitivity**
Low sensitivity of Office BPM was also observed in the Masked Hypertension Study with a very similar participant cohort.

---

## Slide 20
![Slide 20 Thumbnail](./thumbnails/slide_20.png)

**WavesFM captures health information across multiple tasks**
Outperforms models trained on demographic info on many tasks.

---

## Slide 21
![Slide 21 Thumbnail](./thumbnails/slide_21.png)

**WavesFM captures health information (Linear probing)**
Regression tasks with gold standard reference.

---

## Slide 22
![Slide 22 Thumbnail](./thumbnails/slide_22.png)

**WavesFM may unlock more cardiometabolic conditions**
- Prediabetes (HbA1c ≥ 5.7%): WavesFM-v1-MW AUROC 0.788
- Borderline High LDL (≥ 130 mg/dL): Signs of life with AUROC 0.636

---

## Slide 23
![Slide 23 Thumbnail](./thumbnails/slide_23.png)

**Improving SPLAT reconstructions**
Hypothesis: Better reconstructions will lead to improvements in downstream tasks without changing the on-device encoder.

---

## Slide 24
![Slide 24 Thumbnail](./thumbnails/slide_24.png)

**Limiters that impact velocity**
- Storage/Compute capacity for Tier 2 ARDS (10s of PB).
- TPU allocation.
- Accelerating PHL + PHR ingestion.

---

## Slide 25
![Slide 25 Thumbnail](./thumbnails/slide_25.png)

**Key Takeaways & Next Steps**
1. Passed KPIs for Tidal Algo across datasets.
2. Integrate waveform AI to production pipeline.
3. Early promising for other cardiometabolic indicators.
4. Continue to improve waveform AI.
