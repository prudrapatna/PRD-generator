# User Research Analysis: Blood Pressure Concept Testing

**Date:** Q1 2026
**Report Type:** Mini Report
**Stakeholders:**
*   **UXR:** Whargett, Suki B
*   **PMs:** Dushyant Vipradas, Shamira Sridharan Weaver
*   **Consumer Insights:** Virginia Newton (Health Age Lead)
*   **UX Lead:** Anna Kong (Health/Metabolic Age)
*   **UX Writing:** Anitra Appa, Dominique Fong

---

## 1. Study Overview
**Business Goal:** Decide between a **Software as a Medical Device (SaMD)** approach vs. a **Wellness** approach (coaching/awareness).
**Research Questions:**
1.  What are barriers/drivers to **Actionability** (screening, lifestyle changes, calibration)?
2.  What are barriers/drivers to **Credibility** (FDA clearance, validation, expert endorsements)?

**Biases & Limitations:**
*   Qualitative study (n=14), not statistically representative.
*   **Skew:** 4/14 participants check BP once a year or less, potentially skewing preference for "Concept 3" (calibration-heavy).
*   Visualizations of "next steps" were partial, limiting some feedback.

---

## 2. Participant Demographics (n=14)

| ID | Age | Gender | Condition / Goal | Family History | Current Habits | Competitor Usage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P9** | 36 | Male | Hypertension | ? | Monthly (has cuff) | Whoop |
| **P1** | 25 | Male | POTS Syndrome | Yes | Hourly (on body) | Whoop |
| **P2** | 28 | Female | Anemia | Yes | Annual (no cuff) | Apple Alerts |
| **P10** | 33 | Female | High Cholesterol | ? | Annual (has cuff) | Apple Alerts |
| **P6** | 47 | Female | High BP/White Coat | ? | Monthly (has cuff) | Apple Alerts |
| **P3** | 33 | Female | Post-partum BP | ? | Monthly (has cuff) | Apple Alerts |
| **P4** | 22 | Male | Incr. Activity | Yes | Annual (no cuff) | N/A |
| **P11** | 36 | Male | Monitor Health | Yes | Annual (no cuff) | N/A |
| **P8** | 24 | Female | Monitor Health | Yes | Annual (no cuff) | N/A |
| **P13** | 37 | Female | Monitor Health | Yes | Every 2-3 mos | N/A |
| **P5** | 51 | Female | Prevent Illness | Yes | Monthly (has cuff) | N/A |
| **P14** | 37 | Female | Lose Weight | Yes | Monthly (no cuff) | N/A |
| **P12** | 48 | Male | Heart Health | Yes | Weekly (has cuff) | N/A |
| **P7** | 53 | Male | Chronic Condition | Yes | Daily (has cuff) | N/A |

**Key Segment:** 7 participants already use Apple/Whoop BP features. 7 are open to it but don't currently use wearable BP tools.

---

## 3. Concepts Tested

| Feature | **Concept 1: SaMD** | **Concept 2: Weekly Wellness** | **Concept 3: Daily Wellness + Calibration** |
| :--- | :--- | :--- | :--- |
| **Type** | FDA-Cleared (SaMD) | General Wellness | General Wellness |
| **Frequency** | 30-day training / 31-day notification | Weekly assessment / notification | Daily assessment / Weekly notification |
| **Data Required** | 30 days of wear | 7 days of wear | 1 day wear + Calibration (Day 1 & Day 28) |
| **Hypothesis** | Direct, medical association with "Hypertension" drives screening. | Ranges & thresholds are easy to understand; less anxiety. | Daily connection to behavior drives action; Calibration drives trust. |

---

## 4. Detailed Findings by Concept

### Concept 1 (SaMD) - Preferred by 5/14
**Most Credible for:** P2, P6 (tie), P7, P9, P11
**Most Actionable for:** P2, P6, P7, P11, P13

| Pros (Building Trust/Action) | Cons (Barriers) |
| :--- | :--- |
| **FDA Clearance:** Lowers risk; "Clinical trials" + "Legacy" = Trust (P7, P9). | **Mixed Track Record:** Some skeptics cite FDA failures; prefer AHA endorsements. |
| **30-Day Data:** Seen as statistically significant; ignores "noise" and spikes. | **Timing Risk:** 30-day report might be "stale" by doctor appointment (P14). |
| **Medical Tone:** "Hypertension" label + Warning Icon (!) = Urgency/Alarm. | **Fear-Led Urgency:** Lack of specific numbers caused anxiety for some. |
| **Directness:** Explicit "Discuss with HCP" instruction is clear. | **Low BP Ignored:** Less useful for users with low BP concerns (e.g., Anemia). |
| **Population Stats:** "44% don't know they have it" drove importance. | **"Don't Change Regimen":** Warning created hesitation for minor healthy habit changes. |

### Concept 2 (Weekly Wellness) - Preferred by 2/14
**Most Credible for:** P10, P13
**Most Actionable for:** P9, P10

| Pros (Building Trust/Action) | Cons (Barriers) |
| :--- | :--- |
| **Transparency:** Clearly states "General Wellness" (not diagnostic). | **Vague:** "Estimated BP" viewed as less accurate/reliable. |
| **Ranges:** Matched mental models for estimates; easy to understand. | **Lack of Detail:** No detailed readings to judge severity. |
| **Low Anxiety:** Softer headline ("Out of Range") good for sensitive users. | **Passive:** "Share results" language didn't drive urgency. |
| **Simplicity:** Single weekly value prevents "bombardment" of info. | **Low Insight:** Weekly data hides daily triggers (sleep/food). |

### Concept 3 (Daily Wellness + Calibration) - Preferred by 7/14 (Winner)
**Most Credible for:** P1, P3, P4, P5, P8, P14, P6 (tie)
**Most Actionable for:** P1, P3, P4, P5, P8, P14, P12

| Pros (Building Trust/Action) | Cons (Barriers) |
| :--- | :--- |
| **Calibration:** "Cuff-based calibration" = personalized 2nd source (P1, P5, P14). | **Cuff Variability:** Users with inconsistent home cuffs distrusted the baseline (P9). |
| **Granularity:** Daily view offered "upfront evidence" to support the alert. | **Effort:** Some (P10, P11) unwilling to calibrate every 28 days. |
| **Correlation:** Link habits/events to daily readings. | **Over-reach:** Specific numbers for an "estimate" felt like false precision. |
| **Urgency:** Repeated **RED** color + "# of days out of range" = High Action. | **Confusion:** Specific numbers without ranges were confusing for less knowledgeable users (P14). |

---

## 5. Cross-Cutting Themes & Insights

### Actionability Drivers
1.  **Color Coding:** **RED** is the primary signal for "Out of Range" urgency. Absence of red (Concept 2) obscured urgency.
2.  **Specific Numbers:** Needed to judge severity. "Out of Range" is too vague without a number (e.g., "140/90").
3.  **Direct Language:** "Discuss with HCP" works. Passive language ("You may find it helpful") does not.
4.  **Context:** Users want to see *why* (Data Visuals correlating behaviors to trends).
5.  **Frequency:** Weekly reports provided clearer context than 30-day summaries.

### Credibility Drivers
1.  **FDA vs. Calibration:** FDA is a "credential," but **Calibration** is "verification." 7/14 found calibration more credible because it personalized the data.
2.  **Dataset Confusion:** Users missed the significance of "20,000 datasets." They asked:
    *   *How is watch/cuff data used to validate?*
    *   *How many days must I wear it?*
    *   *How reliable is it vs. a cuff?*
3.  **Variance Tolerance:** 5-10 points difference from a cuff is "acceptable." More than that breaks trust.

### The "Ideal Feature" Checklist (from Slide 16)
**To Build Trust:**
1.  **Upfront Info:** State it's "General Wellness."
2.  **"How it Works":** Explain validation/calibration clearly.
3.  **Validation Proof:** Cite 20k datasets and impartial scientific studies.
4.  **Clear Proposition:** "See impact of habits."
5.  **Doctor-Ready Report:** "Good enough to share."

**To Drive Action:**
1.  **Color-Coding:** Indicate urgency (Red/Orange).
2.  **Direct Language:** "BP is High" (Urgent) vs "Out of Range" (Less Urgent).
3.  **Evidence:** Correlate to sleep/activity/eating.
4.  **Cuff Guidance:** Teach users how to take an accurate reading.
5.  **Longitudinal Data:** Show weeks of data to prove statistical significance.
6.  **Journaling:** Option to log feelings/events to explain outliers.

---

## 6. Recommendations & Next Steps

### Product Strategy
*   **Evaluate "No-Calibration" Mode:** P10/P11 liked daily data but wouldn't calibrate. Test a version for them.
*   **Refine "Estimated" Label:** Ensure it doesn't degrade trust too much.
*   **Hybrid Notification:** If lifestyle coaching is supported, notifications must be:
    *   Weekly (for context)
    *   Color-coded (for urgency)
    *   Correlated (to habits)
    *   Directive ("Check with cuff/doctor")

### Content & Education
*   **Explain the Algo:** Create accessible content explaining how "20,000 datasets" and "watch sensors" calculate the result.
*   **Cuff Education:** Offer guidance on *how* to take a valid cuff reading to reduce user error during calibration.

### Further Research
*   **Non-Cuff Users:** Evaluate Concept 2 & 3 specifically with people who *don't* currently own/use a cuff to test friction.
