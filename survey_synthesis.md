# User Research Synthesis: Blood Pressure Monitoring Features

**Date:** February 14, 2026
**Data Source:** 10 Simulated User Interviews
**Objective:** To assess user preference between Wellness vs. SaMD approaches and understand barriers/drivers to actionability.

---

### 1. Executive Summary
The user base is sharply divided, with **50% preferring a Wellness/Coaching approach** and **40% demanding a Medical/Diagnostic (SaMD) tool**. The single most important insight is that a "one-size-fits-all" solution risks alienating both groups: "Wellness" feels unsafe to the medically serious, while "Medical" feels too anxious for the avoidant. Success requires a hybrid or tiered model that balances soft engagement with rigorous validation.

### 2. Key Themes

#### Theme 1: Anxiety & Avoidance
*   **Frequency:** Mentioned by 4 of 10 respondents (The Anxious Avoider, "Ignorance is Bliss", Senior, Busy Pro).
*   **Representative Quotes:**
    *   "Please don't make the alerts scary red colors. Soft nudges are better."
    *   "I don't want to be pestered unless I'm actually dying."
    *   "Fear of diagnosis."
*   **Implications:** Aggressive or alarmist UI will cause immediate churn for a large segment. The default experience must be non-threatening ("soft nudges").

#### Theme 2: The "Proof" Divide
*   **Frequency:** 5 of 10 respondents expressed strong opposing views on data depth (Skeptic, Data Analyst, Chronic Patient vs. Busy Pro).
*   **Representative Quotes:**
    *   "If it's not FDA cleared, it's just a toy."
    *   "I need to know if you're using PPG or just calibration estimation."
    *   *Contrast with:* "Give me 'bite-sized' actions. I can't read long studies."
*   **Implications:** We cannot satisfy the Skeptic/Analyst with a simple "Wellness" app. Transparency (showing the algo/inputs) is a key trust driver for high-value users.

#### Theme 3: Verification Loop
*   **Frequency:** 4 of 10 respondents explicitly cited "Wait and re-measure" as their primary reaction to an alert.
*   **Representative Quotes:**
    *   "I would prefer to wait and re-measure at home first."
    *   "Uncertainty about the app's accuracy."
*   **Implications:** The user journey must formally include a "Verify with Cuff" flow. Pushing a user to a doctor immediately after one reading will result in non-compliance.

### 3. Quantitative Patterns
*   **Preference Split:** 50% Wellness (Concept A) vs. 40% Medical (Concept B).
*   **Knowledge Correlation:** Users with high self-reported knowledge (4-5/5) tended to prefer the Medical approach. Users with low knowledge (1-2/5) preferred Wellness.
*   **Top Motivator:** "Context" (explaining *why* a reading is high) was the strongest driver for actionability among engaged users.

### 4. Recommendations
*   **Must Have:** Contextual Alerts — Based on users demanding to know *why* a reading is unusual (e.g., "related to poor sleep").
*   **Must Have:** "Soft Nudge" UI Mode — Based on explicit feedback to avoid "scary red colors" from anxious users.
*   **Should Have:** In-App Verification Flow — Based on the 40% of users whose first instinct is to "wait and re-measure."
*   **Should Have:** Tiered Experience (Wellness vs. Pro) — Based on the irreconcilable differences between the "Busy Professional" and the "Data Analyst."
*   **Could Have:** PDF Export for Doctors — Based on the Chronic Patient's need to share data with a cardiologist.

### 5. Open Questions
*   **Insurance Coverage:** Will the "Medical" version be reimbursable? (Raised by the Cost-Conscious user).
*   **Retention of "Ignorance is Bliss" users:** How do we engage users who explicitly "don't want to be pestered" without compromising safety?
*   **Legal/Regulatory Line:** Can we provide the specific data requested by the "Data Analyst" (raw inputs, algorithms) without triggering SaMD classification in the "Wellness" tier?
