# User Research: Investment Priorities & User Needs (2026-2028)

**Source:** Health Research Priorities Deck (Slides 27-37)
**Status:** Q4 2025 Review

## 1. Feature Recommendations & User Sentiment (Slide 27)

### **Proposed New Features (Invest vs. Stop)**
*   **Invest:**
    *   **Body Composition:** High appeal/WTP. Recommendation: Leverage 3P/Health Connect instead of 1P hardware.
    *   **Elderly Segment:** Start market assessment for malignancy/neurodegenerative detection.
*   **Stop/Deprioritize:**
    *   **CPR Assist:** Low PHA alignment, Safety-focused.
    *   **Intoxication Safety:** Unclear business impact.
    *   **Buds Body Temp:** Waiting on tech feasibility and appeal data.

### **Improvements (Addressing Pain Points)**
*   **Heart Rate (Cadence Lock):** Negative quality feedback. **Plan:** QPR update Mar/June 2026.
*   **Swim Metrics:** "Table stakes" gap. **Plan:** Advanced metrics (Stroke, Distance, SWOLF).
*   **LLOB (Off-Body):** Critical for safety features on trackers.

## 2. Areas NOT Investing In (Slide 28)
*   **Hydration:** No viable sensing path (disagreement on standards).
*   **Fatigue/Alertness:** Mixed appeal, unclear actionability.
*   **Cough/Snore (Watch):** Prioritize Phone/Nest integration first.
*   **Clinical Mental Health Screening:** Focus on "General Wellness" first.
*   **SpO2 Spot Check:** High investment for limited wellness use case.
*   **Afib Burden:** Niche user base (paroxysmal AFib).

## 3. Strategic Pillars & Differentiation (Slide 29)
*   **Fitness:** Table stakes (Vo2Max, HR) -> **Bet:** Real-time performance coaching.
*   **Sleep:** Table stakes (Stages, Apnea) -> **Bet:** Sleep Score + Circadian Coaching.
*   **Nutrition:** Table stakes (Logging) -> **Bet:** Assessment + Coaching.
*   **Mental Wellbeing:** Table stakes (Stress) -> **Bet:** MWB Sub-agent + Chronic Stress.
*   **Cardio-Metabolic:** **Bet:** Pre-diabetes/IR, Hypertension, Breathing Emergency.

## 4. Metabolic Health Strategy (Slide 30)
*   **No 1P Glucose Sensing:** We are **NOT** building a non-invasive glucose sensor internally.
*   **Focus:**
    *   **2026:** Glucose response prediction (Meals).
    *   **GA:** 3P CGM Integration (Abbott partnership).
    *   **Wellness:** Insulin Resistance (IR) assessment + Coaching.

## 5. User Appeal Data (MaxDiff) (Slide 31)
*   **Top 13 Features:** Hypertension, Trends, Summaries, Coaching, Emergency.
*   **Proactive Adopters:** Over-index on **Fitness Coaching** and **Performance Coaching**.
*   **Gen Z (18-34):** **Breathing Emergency Alert** is the #1 feature.
*   **Regional Nuance:**
    *   **UK/DE:** High interest in **Hypertension Trends/Alerts**.
    *   **Japan:** Prefers **Sleep Need** and **Symptom Search**.

## 6. Hypertension Feature Prioritization (Slide 32)
*   **Top Performer:** Hypertension features consistently rank highest across KPIs.
*   **User Preference:**
    *   **"Alert With Calibration":** "Your wearable monitors... calibrated for accuracy with your connected BP device." (Aligned with our PRD direction).
    *   **"Screening":** "Use your wearable to screen for high blood pressure."

## 7. Foundation Models (Slide 34-35)
*   **SPLAT:** 32x sensor compression for Activity Recognition.
*   **MSEL:** Motion encoding for Fall Detection / Running Dynamics.
*   **LSM (Large Sensor Model):** 100M+ hours training data. Enables generative tasks (imputation) and discriminative tasks (activity recog).
*   **PPG Foundation (Tidal):** >1M hours. Pre-trained for BP, Stiffness, Hypertension.

## 8. Specific Feature Deep Dives (Slides 36-37)
*   **Sleep Apnea (SaMD):** 14.5% US prevalence. Target 2026 MBG.
*   **Unusual Trend Detection (UTD):**
    *   **Concept:** Monitor physiological shifts -> "Significant Strain" -> "Rest Mode."
    *   **CUJs:** "Monitor sickness signs," "Adjust my week."
    *   **Target:** Q2 2026.
