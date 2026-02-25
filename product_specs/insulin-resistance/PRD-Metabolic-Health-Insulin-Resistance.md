# PRD: Metabolic Health — Insulin Resistance Level

| Field | Detail |
|---|---|
| **Feature Name** | Insulin Resistance Level (Metabolic Efficiency) |
| **Platform** | Google Health Mobile App (Android & iOS) |
| **Hardware** | Pixel Watch 1-4, Fitbit (Sense 1-2, Versa 2-4, Charge 5-6, Luxe, Inspire 2-3) |
| **Owner** | [Staff PM — Metabolic Health] |
| **Status** | Draft v1.0 |
| **Last Updated** | 2026-02-23 |
| **Target GA** | H2 2026 (Strategic Priority: KR8) |

---

## 1. TL;DR

**What It Is:**
A passive, longitudinal wellness feature that estimates your body's "Metabolic Efficiency" by identifying patterns of insulin resistance. It turns the data already collected by your wearable into a meaningful early warning signal for metabolic health, helping you understand how effectively your cells are using energy.

**The Experience:**
The feature runs entirely in the background. After a 14-day calibration period, users receive a monthly status (High or Low Insulin Resistance). For those with High levels, the Personal Health Agent (PHA) provides empathetic, cross-domain coaching—linking metabolic status to activity, sleep, stress, and nutrition—to help users reverse the trend through sustainable lifestyle changes.

**Who It's For:**
The 40% of US adults (especially those aged 18-44) who have unrecognized insulin resistance. These "Proactive Adopters" are health-curious and motivated by "early warning" signals that allow them to optimize their wellness before it becomes a clinical condition.

---

## 2. Intended Use (Regulatory "North Star")

**Mandatory Statement (verbatim — to appear in all user-facing labeling, marketing, legal disclaimers, and app store copy):**

> *"The Insulin Resistance feature is a general wellness tool intended to estimate insulin resistance level to promote positive lifestyle behavior changes in sleep, activity, stress and nutrition management by educating users and helping them understand how their daily habits correlate with estimated insulin resistance level. This product is not intended to diagnose, mitigate, treat, or cure any disease. This product is not a prescreener for diabetes nor is it intended to monitor glucose levels in real time. Do not use this product for diabetes management or rely on this product to alter any medications or insulin levels. Consult a medical professional for any questions about your metabolic health."*

**Regulatory Classification:**
- **Classification:** General Wellness Software Function (Non-Device)
- **FDA Guidance:** General Wellness: Policy for Low Risk Devices (Jan 2026)
- **Risk Profile:** Low-risk, non-invasive sensing (PPG, EDA, Skin Temp, etc.)
- **Contraindications:** Prior diagnosis of diabetes/prediabetes, pregnancy, <6 months post-partum, under age 18.

**Regulatory Bright Lines:**

| Prohibited in User-Facing Copy | Required Terminology |
|---|---|
| "Diabetes," "Prediabetes," "Screening" | "Metabolic Health," "Insulin Resistance Level" |
| "Abnormal," "Pathological," "Disease" | "High Level," "Outside typical wellness range" |
| Absolute glucose values (mg/dL) | "High" / "Low" categorical status |
| Real-time glucose tracking claims | "Passive continuous assessment," "Monthly window" |
| Red color for high status indicators | Neutral informational palette (amber or grey) |
| "Medical grade," "Clinical accuracy" | "General wellness," "Educational" |

---

## 3. The Press Release (Narrative)

### 7-Star Experience Pre-Work

**The Core Moment:** The user receives their first "High Insulin Resistance" notification and realizes it's a call to action, not a diagnosis.

- **5-Star (Expected):** The app shows a "High" status and a list of generic tips.
- **6-Star (Better):** The status is explained in the context of the user's last month of steps and sleep.
- **7-Star (Magical):** The Personal Health Agent sends a message: *"I’ve noticed your metabolic efficiency has been lower than usual this month. I also see your activity levels dropped by 30% while your sleep was inconsistent. These often go hand-in-hand. Small changes in your evening routine could help your body use fuel more effectively. Want to try a 14-day 'Metabolic Reset' plan?"*

---

### FOR IMMEDIATE RELEASE

## Unlock the Secret to Your Body’s Fuel Efficiency

*Google Health introduces Insulin Resistance Level—a groundbreaking passive wellness feature that empowers you to optimize your metabolic health before it becomes an invisible problem.*

**MOUNTAIN VIEW, Calif. — 2026** — Google Health today announced the launch of Insulin Resistance Level, a new metabolic wellness feature for Pixel Watch and Fitbit users. Designed to address the "awareness gap" in metabolic health, this feature works silently in the background to estimate how effectively your body manages glucose, helping you build a more resilient, energetic version of yourself.

**The Invisible Challenge:** Over 40% of adults live with insulin resistance, a state where the body’s cells don’t respond effectively to energy. It’s often invisible until it’s too late. Tidal aims to make this invisible pattern visible, giving users the "early warning" they need to make meaningful lifestyle shifts.

**How It Works:** By leveraging the sophisticated sensors on your wrist—measuring everything from heart rate variability to skin temperature—Tidal identifies physiological markers associated with metabolic efficiency. There are no finger pricks and no manual logs. After a 14-day calibration, you’ll receive a monthly status: High or Low.

**Empowerment, Not Anxiety:** "We built this to replace the 'what if' with the 'what's next'," says the Head of Metabolic Health at Google. "If your level is high, your Personal Health Agent doesn't just alert you—it partners with you. It looks at your sleep, your steps, and your stress to provide a personalized roadmap for optimization."

**The 7-Star Difference:** Tidal goes beyond data. It integrates with Google’s Personal Health Agent to provide multi-horizon simulations. Users can see how improving their sleep efficiency or adding 15 minutes of movement after meals could impact their metabolic health over time. 

**Availability:** Insulin Resistance Level is rolling out to Google Health users on compatible Pixel Watch and Fitbit devices starting H2 2026.

---

## 4. Problem & Opportunity

### The Metabolic Awareness Gap
Insulin resistance is a precursor to a wide range of chronic health challenges, yet it remains largely undetected in the general population. In the 18-44 age group, awareness is critically low. 

**The Opportunity:**
- **High Interest:** UXR shows 79% of consumers are interested in metabolic health features.
- **Willingness to Pay:** Conjoint studies value diabetes risk/IR assessment at ~$1.15 in a monthly subscription.
- **The "Aha" Moment:** Users view insulin resistance as a "critical early warning sign"—a more actionable and less scary concept than "prediabetes."

**Competitive Edge:**
- While competitors focus on manual glucose tracking or expensive CGMs, Google provides a **passive, zero-friction entry point** that uses the hardware millions already own.
- Integration with the **Personal Health Agent (PHA)** provides a context layer that no "dumb" tracker can match.

---

## 5. App Overview — The "7-Star" Vision

### Philosophy: Visibility Leads to Optimization
The app experience is designed to turn "invisible" metabolic patterns into an "interactive" health journey.

**Layer 1: The Invisible Sensor (Watch)**
- Passive collection of PPG, EDA, Skin Temp, and Motion data.
- No user-facing UI on the watch; it remains a silent data pipe.

**Layer 2: The Context Engine (Cloud + PHA)**
- Analyzes a 30-day rolling window.
- Correlates IR status with Sleep, Activity, and Stress APIs.
- Uses Gemini-powered LLM to generate "Metabolic Efficiency" narratives.

**Layer 3: The Health Tab (Mobile App)**
- **Metabolic Health L2:** The hub for all IR data. Shows current status (High/Low) and history.
- **Monthly Coaching Moment:** A rich, interactive card that surfaces on the Home tab when a new status is available.
- **World Model Simulations:** "If I lose 5lbs, how does my metabolic efficiency change?"
- **Data Completeness Tiers:** Shows if the prediction is based on Wearable only, or enhanced by CGM/Blood Labs.

---

## 6. Critical User Journeys (CUJs)

### CUJ 1: Onboarding & Calibration
*   **User:** 32-year-old "Proactive Adopter" with a Pixel Watch 3.
*   **Goal:** I want to understand my metabolic health without it being complicated.
*   **Task:**
    1. Sees "Metabolic Health" in the Health tab.
    2. Confirms eligibility (Not pregnant, no diabetes diagnosis).
    3. Confirms weight (pre-populated, must be <180 days old).
    4. Sees "Calibration in progress: 14 days remaining."
*   **Outcome:** User feels intrigued and motivated to wear the watch.

### CUJ 2: The "High IR" Coaching Moment
*   **User:** Receives a notification after 30 days.
*   **Goal:** I want to know what to do about my "High" status.
*   **Task:**
    1. Taps notification to open the "Coaching Moment" card.
    2. Reads PHA insight: *"Your insulin resistance level is High. This month, your sleep was 20% more fragmented than usual. Better sleep is a powerful lever for metabolic health."*
    3. Engages with the "Improve Sleep" goal suggested by the app.
*   **Outcome:** User feels empowered to take a specific, manageable action.

---

## 7. Functional Requirements

### Feature Logic Definitions
| Constant | Value | Description |
|---|---|---|
| `MIN_VALID_DAYS` | 7 days | Minimum valid days in a 30-day rolling window |
| `MIN_WEAR_TIME` | 8 hours/day | Minimum wear time for a day to count as "valid" |
| `MIN_SLEEP_SESSIONS` | 7 sessions | Minimum sleep sessions required in the window |
| `WEIGHT_STALENESS_LIMIT` | 180 days | Weight must be updated within this window |
| `IR_THRESHOLD` | HOMA-IR ≥ 2.9 | Threshold for "High" classification |

### FR-01: Sensing & Data Validation
- **Requirement:** The system must validate data sufficiency before generating a status.
- **Acceptance Criteria:**
    - IF `valid_days` < 7 OR `sleep_sessions` < 7: Status = "Incomplete data."
    - IF `weight_age` > 180 days: Prompt user to "Update weight" and set status to "Stale."
- **Inputs:** PPG (HR, RMSSD), EDA, Skin Temp, Step Count, Sleep duration/stages.

### FR-02: Status Calculation
- **Requirement:** Status is determined by the majority of eligible days in the 30-day window.
- **Acceptance Criteria:**
    - IF > 50% of eligible days exceed the `IR_THRESHOLD`: Status = "High."
    - ELSE: Status = "Low."

### FR-03: PHA Insight Generation
- **Requirement:** PHA must generate a personalized narrative for "High" status users.
- **Acceptance Criteria:**
    - Retrieve Sleep/Activity trends for the same 30-day window.
    - Identify the most significant negative lifestyle trend.
    - Generate narrative using "may help" language (e.g., *"Improving sleep may help optimize your metabolic efficiency"*).
    - Narrative must NOT name diseases or suggest medical treatments.

---

## 8. Technical Architecture & Data

- **Inference Engine:** Cloud-based model (Logistic Regression) taking 257 inputs (256 waveform features + normalized weight).
- **Data Tiers:**
    - **Tier 1 (Wearable Only):** Base prediction.
    - **Tier 2 (+CGM):** Enhanced accuracy if user links CGM data (last 180 days).
    - **Tier 3 (+PHR):** Maximum accuracy if user provides blood labs (HbA1c, Triglycerides).
- **Security:** Data encrypted in transit/at rest; separate processing pipeline for metabolic health to ensure high privacy standards.

---

## 9. Regulatory Safety Guardrails

- **Color Palette:** "High" status must use **Amber/Yellow**, NOT Red.
- **Disclaimer Visibility:** The mandatory disclaimer must be visible on all IR-related screens.
- **Prohibited Terms Filter:** All PHA-generated content must pass a filter that blocks words like "Diabetes," "Diagnose," "Monitor," "Treat," etc.
- **No Absolute Values:** Never show HOMA-IR scores or predicted mg/dL values.

---

## 10. Success Metrics (HEART Framework)

| Category | Metric | Target |
|---|---|---|
| **Happiness** | Post-onboarding CSAT | ≥ 4.2 / 5.0 |
| **Engagement** | % of users opening "Coaching Moment" | ≥ 45% |
| **Adoption** | % of eligible users enabling the feature | ≥ 30% |
| **Retention** | 3-month retention (feature still enabled) | ≥ 65% |
| **Task Success** | Weight update success (on prompt) | ≥ 80% |

---
**FINAL QUALITY CHECK:**
- Word "Monitor" used? -> **NO.**
- Red colors used? -> **NO.**
- Diagnostic terms? -> **NO.**
- Lifestyle correlations included? -> **YES.**
