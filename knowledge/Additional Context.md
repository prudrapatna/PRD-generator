# Product Overview: Tidal Wellness Blood Pressure Offering

## 1. Product Description
Tidal is a general wellness feature designed to estimate blood pressure trends and range, helping users understand the link between their lifestyle and cardiovascular health. Unlike traditional spot-check cuffs, Tidal leverages passive, longitudinal monitoring (PPG + Accelerometer) on the wrist to provide a continuous picture of heart health without calibration.

## 2. Intended Use
The Blood Pressure Notification feature is a general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range.

The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including hypertension.

## 3. What Problem Are We Solving?
*   **The "Silent Killer" & Awareness Gap:** Hypertension is the #1 risk factor for cardiovascular death, yet ~60-70% of younger adults (18-44) with uncontrolled hypertension are unaware of their condition. Because it is asymptomatic, users lack urgency to check.
*   **The "Single-Reading" Bias:** Users often misinterpret a single high reading from a cuff as a "spike" or error. Tidal solves this by aggregating data over 14 days, providing a sustained, credible signal that overcomes user inertia.
*   **Lifestyle Disconnect:** Users struggle to connect abstract BP numbers to daily choices. Tidal bridges this gap by correlating trends directly with sleep, nutrition, and stress data.

## 4. Go-to-Market & Value Proposition
**Messaging Strategy:** Pivot from "Medical Detector" to "Health Guardian."
*   **Do:** Focus on "Inferred Blood Pressure" trends, lifestyle correlations (e.g., "Your BP is out of range; let's look at your sleep"), and peace of mind.
*   **Don't:** Use diagnostic terms like "Hypertension detection" or "Screening" in user-facing copy.

**Core Value Proposition:**
*   **Passive & Calibration-Free:** No cuffs, no manual logging. Works in the background.
*   **Longitudinal Intelligence:** Distinguishes sustained patterns from temporary stress spikes using a 30-day analysis window.
*   **Actionable Feedback:** Moves beyond just "alerting" to "coaching" by linking out-of-range values to specific lifestyle behaviors (e.g., sodium intake, sleep quality).

## 5. Definition: "Out of Range"
The system defines a user as "Out of Range" based on a rigorous assessment of sustained blood pressure elevation, differentiating it from transient variability.
*   **Evaluation Window:** A recurring 30-day rolling window.
*   **Data Sufficiency:** Requires a minimum of 14 valid days of data (≥8 hours of wear time/day).
*   **Threshold Logic:** If ≥14 days within the window have a predicted probability exceeding the threshold for Systolic ≥ 130 mmHg OR Diastolic ≥ 80 mmHg, the user is classified as "Out of Range."

## 6. Performance Target vs. Clinical Status Quo
Our goal is to demonstrate non-inferiority to the current clinical standard: Office Blood Pressure Measurement (OBPM).

| Metric | Tidal Performance (V1 Algorithm - SPLAT) | OBPM Benchmark (Standard of Care)* |
| :--- | :--- | :--- |
| **Sensitivity** | 53% (95% CI: 40%, 64%) | 54% (95% CI: 37%, 70%) |
| **Specificity** | 93% (95% CI: 86%, 96%) | 90% (95% CI: 84%, 95%) |
| **Ground Truth** | 24-Hour ABPM | 24-Hour ABPM |

*Benchmark based on USPSTF systematic review (Guirguis-Blake et al., JAMA 2021) comparing Office BP to the gold standard ABPM. Tidal V1 performance based on internal clinical dataset @ 36.5% prevalence.

## 7. Validation Plan
Our strategy proves rigor superior to consumer competitors by measuring against the highest clinical standard.
*   **Pivotal Study (N=1,600):** A head-to-head comparison of Tidal vs. Office BP.
*   **Ground Truth:** All participants undergo 24-hour Ambulatory Blood Pressure Monitoring (ABPM).
*   **Objective:** Demonstrate that Tidal is statistically non-inferior to Office BP for identifying sustained high blood pressure, effectively capturing nocturnal dipping and variability that spot-checks miss.

## Appendix: Competitive Performance Context

| Feature | Tidal (Google) | Apple Hypertension Notifications |
| :--- | :--- | :--- |
| **Ground Truth** | 24-Hour ABPM (Clinical Gold Standard) | Home Blood Pressure (HBPM) |
| **Benchmark** | Comparability to Office BP | Standard deviation < 10mmHg |
| **Calibration?** | No (Calibration-free) | No (Calibration-free) |
| **Method** | Longitudinal (14+ days of data) | Pulse Feature Analysis (Opportunistic) |
| **Key Win** | Validated against ABPM, capturing true 24hr heart health (including sleep). | Validated against Home BP, which misses nocturnal hypertension. |
