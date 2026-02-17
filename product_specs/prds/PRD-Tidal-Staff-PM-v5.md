# PRD: Google Health Guardian (Project Tidal)
**Owner:** Google Health Product Team
**Status:** Draft (v5.1 - Staff PM Review)
**Last Updated:** February 17, 2026

---

## 1. TL;DR
**Google Health Guardian** is a general wellness feature for Pixel Watch and Radiance that provides passive, calibration-free blood pressure trend estimation. By leveraging a novel "Waveform Foundation Model" and Generative AI, it replaces the anxiety of the cuff with the peace of mind of continuous, background protection, targeting the "Proactive Adopter" segment.

---

## 2. Intended Use (Regulatory "North Star")
**Source:** `knowledge/Additional Context.md` | **Constraint:** General Wellness (Low Risk)

The Blood Pressure Notification feature is a general wellness tool intended to estimate blood pressure values and trends for **informational and educational purposes only**. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range.

**The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including hypertension.**

**Contraindications:** This feature is not intended for use by pregnant women due to significant hemodynamic changes during pregnancy. It is not a substitute for clinical diagnosis or monitoring.

---

## 3. The Press Release (Narrative)

**FOR IMMEDIATE RELEASE**

**Google Announces "Health Guardian": The End of the Silent Killer**

**MOUNTAIN VIEW, CA** — Today, Google introduces **Health Guardian**, a revolutionary new feature for Pixel Watch and Radiance that transforms your wearable into a silent protector of your heart health.

**The Problem:** For decades, tracking blood pressure meant stopping your life, putting on a tight, uncomfortable cuff, and waiting in anxious silence for a judgment. Because it was hard, millions didn't do it. And because they didn't do it, the "Silent Killer" (hypertension) went undetected in over 60 million adults.

**The Solution:** Health Guardian changes everything. There is no cuff. There is no calibration. There is no "start" button. You simply wear your watch. Using advanced PPG sensors and Google's new **Waveform Foundation Model**, Health Guardian learns the unique "song" of your blood flow, watching over you day and night to estimate your cardiovascular range.

**The Experience:**
*   **The Invisible Setup:** You put on your watch. That's it.
*   **The Weekly Check-In:** Every Monday, you get a "Weekly Range" card. It shows your trends calmly: *"Your range was stable last week. Your improved sleep (avg 7.5hrs) likely contributed."*
*   **The Contextual Nudge:** If life gets hectic and your trends drift persistently for a month, Guardian doesn't alarm you. It offers a path forward: *"I've noticed your range has been elevated for 4 weeks. Let's try a 14-day Sleep Coaching plan to see if we can bring it back to baseline."*

**Internal Quote:** *"We didn't just build a sensor; we built a guardian. We wanted to replace the anxiety of 'checking' with the comfort of 'knowing', democratizing peace of mind for everyone."* — VP, Google Health.

**Customer Quote:** *"I used to hate the cuff. It made me anxious. Now, I just live my life, and my watch tells me I'm okay. It feels like someone is looking out for me while I sleep."* — Sarah, 34, Early Tester.

---

## 4. Problem & Opportunity

### The Anxiety Gap
*   **Current State:** Hypertension affects 50% of adults, yet 20 million young adults (18-44) are unaware. The "Gold Standard" (Cuff) induces anxiety ("White Coat Syndrome") and friction.
*   **Insight:** "Proactive Adopters" (17% of population) want prevention but hate "maintenance." They don't want a dashboard; they want "Peace of Mind."
*   **Differentiation:** Competitors (Omron, Withings) require active spot-checks. Samsung requires calibration. **Google Health Guardian** is the only passive, calibration-free "World Model" that simulates consequences (e.g., "Sleep +1hr = Stable Range").

### Competitive & Performance Analysis

**Table 1: Tidal vs. Key Competitors**

| Feature | **Google Health Guardian (Tidal)** | **Apple Watch (Hypertension Notification)** | **Samsung Galaxy Watch (BP)** | **Omron HeartGuide** |
| :--- | :--- | :--- | :--- | :--- |
| **Method** | Passive, Calibration-Free (Waveform Model) | Passive, Calibration-Free (Pulse Feature Analysis) | Active, Calibration-Dependent (PTT) | Active, Cuff Inflation (Oscillometric) |
| **User Effort** | **Zero (Passive Background)** | Zero (Passive Background) | High (Monthly Cuff Calibration) | High (Manual Inflation) |
| **Ground Truth** | **24-Hour ABPM** (Captures Sleep Dipping) | Home BP (Waking Hours Only) | Home BP | Home BP / Office BP |
| **Output** | Wellness Range + Lifestyle Correlation | Notification (High/Normal) | Absolute Value (e.g., 120/80) | Absolute Value (Medical Grade) |
| **Regulatory** | General Wellness (FDA Enforcement Discretion) | De Novo / 510(k) Cleared | De Novo / 510(k) Cleared | FDA Cleared (Class II) |

**Table 2: Target vs. Current Performance**

| Metric | **Target (Comparability to Office BP)** | **Current V1 (Internal Clinical)** | **Gap / Status** |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | **0.54** (95% CI: 0.37, 0.70) | **0.53** (95% CI: 0.40, 0.64) | **On Track** (Within Margin) |
| **Specificity** | **0.90** (95% CI: 0.84, 0.95) | **0.93** (95% CI: 0.86, 0.96) | **Exceeds Target** |
| **Validation Size** | ~2000 Participants | 663 Participants (Training) | Need Pivotal Study (N=1600) |

### Validation Plan
*   **Pivotal Study:** N=1,600 participants (Representative US demographics).
*   **Ground Truth:** 24-Hour Ambulatory Blood Pressure Monitoring (ABPM).
*   **Objective:** Demonstrate statistical non-inferiority to Office BP for identifying sustained high blood pressure.
*   **Subgroups:** Validation across Age, BMI, and Skin Tone (Fitzpatrick Scale) to ensure equity.

---

## 5. App Overview (The "7-Star" Vision)

### The Health World Model
We are moving beyond "Logging" to "Simulating."
*   **Simulation:** The system runs a "Shadow Simulation" of the user's physiology. It predicts: *"If `Sleep_Duration` increases by 60m, `Vascular_Stiffness` proxy decreases by 4%."*
*   **Cost Function:** The system assigns a "Biological Cost" to user choices. It surfaces the path of least resistance (e.g., "A 10-minute walk is cheaper than a nap right now").

### Mobile Experience
*   **Reactive Weekly View:** Every Monday, users receive a "Weekly Summary." It shows the range for the past week and correlates it with lifestyle factors (Sleep, Activity, Stress).
    *   *Design:* "Wellness Range" gauge (Green/Amber). No red. No numbers.
*   **Proactive Monthly Nudge:** If the user is persistently "Out of Range" for >30 days, the system triggers a proactive notification.
    *   *Action:* Suggests a **Coaching Plan** (e.g., "Sleep Reset") or recommends consulting a healthcare provider.
*   **Latency:** "Day-Late" cadence. Data from Day `T` is processed overnight and available on Day `T+1`. This ensures complete data ingestion without real-time pressure.

---

## 6. Critical User Journeys (CUJs)

### Part A: CUJ Header
*   **Target User:** The "Regular" Proactive Adopter (Age 30-50, Tech-Forward, Anxiety-Prone).
*   **Critical Goal:** I want to enable protection without "medicalizing" my life.
*   **Context:** Unboxing a new device or browsing the Health app.

### Part B: The Journey Map (Goals & Tasks)

| Goal (The "Why") | Task (The "How") | Product/CUI (Instrumentation) | Health Score |
| :--- | :--- | :--- | :--- |
| **I want to enable protection effortlessly** | 1. I tap "Enable Guardian" in OOBE or Settings. | *Toggle Switch* | **Healthy** |
| | 2. I confirm my **Height** (Critical for algo). | *Height Picker / Confirm Button* | **Healthy** |
| | 3. I see a confirmation: "Learning your baseline (14 days)." | *Status Card: "Calibrating"* | **Healthy** |
| **I want to check my status (Weekly)** | 4. I receive a "Weekly Summary" notification on Monday. | *Push Notification* | **Healthy** |
| | 5. I see "Wellness Range: Stable" correlated with my avg sleep (7.5h). | *Dashboard Card* | **Healthy** |
| **I want to address a persistent issue** | 6. I receive a notification: "Persistent Range Shift detected (30 days)." | *Push Notification* | **At Risk** (Actionable) |
| | 7. I am offered a choice: "Start 2-week Sleep Coaching" or "Consult Provider." | *Action Sheet* | **Healthy** (Agency) |
| | 8. I choose "Sleep Coaching" and receive daily guidance. | *Coaching Plan UI* | **Healthy** |

### Part C: Health & Metrics
*   **Usefulness Metric:** CSAT "Did this give you peace of mind?" (Target: 4.5/5).
*   **Usability Metric:** % of users engaging with Weekly Summary (Target: 40%).

---

## 7. Functional Requirements (The Substance)

### Feature Logic Definitions (Constants)
*   **Constant:** `MIN_WEAR_DURATION` = 12 hours/day.
*   **Constant:** `MIN_VALID_DAYS_NOTIFICATION` = 14 days (in rolling 30-day window).
*   **Constant:** `MIN_VALID_DAYS_WEEKLY` = 7 days.
*   **Constant:** `HTN_THRESHOLD` = 0.5699 (Probability).
*   **Constant:** `HEIGHT_MIN` = 21.5 inches (1'9.5").
*   **Constant:** `HEIGHT_MAX` = 107 inches (8'11").
*   **Constant:** `PERSISTENT_DURATION` = 30 days.

### Structured Requirements Table

| ID | Category | Requirement / User Story | Acceptance Criteria (Gherkin Scenarios) | Error Handling |
| :--- | :--- | :--- | :--- | :--- |
| **FR-01** | **Sensing** | As a user, I accept a "Day-Late" view to ensure data completeness. | **Scenario 01: Latency Acceptance**<br>**Given** User wears watch on Day T<br>**When** Nightly processing runs at T+1 (02:00 AM)<br>**Then** Data for Day T becomes visible in the app.<br>**And** No partial/incomplete data is shown for Day T+1. | IF processing fails, Retry 3x. IF failure persists > 48h, Show "Data Delayed" banner. |
| **FR-02** | **Logic (Weekly)** | As a user, I want a reactive weekly summary of my range. | **Scenario 02: Weekly Reactive View**<br>**Given** User has >4 `valid_days` in the last week (Mon-Sun)<br>**When** It is Monday morning<br>**Then** Generate "Weekly Range Summary"<br>**And** Correlate with Sleep/Activity averages. | IF <4 `valid_days`, Show "Insufficient Data for Weekly View" card. |
| **FR-03** | **Logic (Monthly)** | As a user, I want to be notified only when a shift is persistent. | **Scenario 03: Monthly Persistent Check**<br>**Given** User has >20 `valid_days` in last 30 days<br>**And** `Hypertension_Score` > Threshold for >70% of those days<br>**When** Monthly check runs<br>**Then** Trigger "Persistent Shift" notification<br>**And** Offer Coaching/Provider options. | IF calculation ambiguous, Default to "Monitor" state (No alarm). |
| **FR-04** | **Profile** | As a system, I must exclude contraindicted users (Pregnancy). | **Scenario 04: Pregnancy Disclaimer**<br>**Given** User is onboarding<br>**When** They view the "Intended Use" screen<br>**Then** Display clear text: "Not intended for use during pregnancy."<br>**And** Require explicit acknowledgment. | N/A (Static UI Text). |

### Non-Functional Requirements
*   **NFR-01:** PPG Signal Quality Check: Discard if SQI < 0.5.
*   **NFR-02:** Heart Rate Bounds: Discard if HR < 30 or > 200 bpm.
*   **NFR-03:** Data Freshness: Dashboard must reflect Day T data by 08:00 AM local time on Day T+1.

---

## 8. Technical Architecture
1.  **Sensing (Watch):**
    *   PPG (Green, 25Hz) + Accel (25Hz).
    *   On-device compression (Tokenization) to save battery.
2.  **Ingestion (Cloud):**
    *   Google Cloud Dataflow decompresses tokens (Batch Process: Nightly).
    *   Signal Quality Check (SQI filter).
3.  **Inference (Vertex AI):**
    *   **Waveform Foundation Model:** Generates 256-d embeddings.
    *   **Hypertension Classifier:** Logistic Regression (All-day vs. Awake models).
4.  **Presentation (App):**
    *   Jetpack Compose / SwiftUI.
    *   Gemini API for Nudge generation (Weekly Summary text).

---

## 9. Regulatory Guardrails
*   **Classification:** FDA "General Wellness" (Low Risk).
*   **UI Constraints:**
    *   **NO** Red colors.
    *   **NO** Medical terminology ("Hypertension," "Diagnosis").
    *   **NO** absolute BP numbers (e.g., "135/90").
    *   **MUST** display: "Not a medical device. Consult a doctor."
    *   **MUST** display: "Not for use during pregnancy."

---

## 10. Success Metrics (HEART)
*   **Happiness:** CSAT > 4.5 on "Weekly Summary" cards.
*   **Engagement:** >40% of users opening the Weekly Summary notification.
*   **Adoption:** >15% of persistent "Out of Range" users starting a Coaching Plan.
*   **Retention:** <5% disable rate after receiving a "Persistent Shift" notification.
*   **Task Success:** >90% of users successfully acknowledge the "Not a Medical Device" disclaimer during onboarding.
