# PRD: Tidal (Blood Pressure Trends)

## 0. Project Metadata & Approvals

*   **Deliverable:** Full Product Requirements Document (PRD)
*   **Project Name:** Tidal (Blood Pressure Trends)
*   **Primary Objective:** Deliver a passive, calibration-free wellness feature that empowers users to spot out-of-range cardiovascular patterns.
*   **Regulatory Classification:** General Wellness (Non-SaMD)
*   **Target Launch:** 2026

| Role | Approver | Date | Status |
| :--- | :--- | :--- | :--- |
| **Product Manager** | Pramod Rudrapatna | 2026-03-25 | Draft |
| **Engineering Lead** | Ryan Davidson | TBD | Pending |
| **UX/Design Lead** | Cynthia Cruz | TBD | Pending |
| **Regulatory/Legal** | TBD | TBD | Pending |

---

## 1. Press Release

<table style="border: 1.5pt solid black; border-collapse: collapse; width: 100%;">
<tr>
<td style="padding: 20px;">

## Google Health Introduces Blood Pressure Trends: Your Invisible Cardiovascular Guardian
**Empowering millions to discover hidden cardiovascular patterns and optimize their proactive wellness.**

**What It Is:** 
Blood Pressure Trends is a first-of-its-kind wellness feature built into Google Health. Utilizing the optical sensors already on your wrist and the power of our WavesFM foundation model, it estimates underlying cardiovascular patterns completely passively—without the need for cumbersome calibration or inflation cuffs.

**The Experience:** 
It works like magic. Once activated, the system simply learns your body's rhythms in the background. There are no daily alarms or stressful alerts to manage. At the end of every month, Google Health provides a clear, empathetic assessment. If your patterns consistently trend out of range, the Personal Health Assistant will gently guide you to review your lifestyle factors—like sleep, stress, and activity—and encourage you to consult a healthcare provider for a clinical evaluation. It is the ultimate 7-Star experience: a guardian that knows you, understands your life, and quietly protects your peace of mind.

**Who It's For:** 
This feature is designed for the millions of adults—particularly the 20 million young adults—who have the desire to optimize their cardiovascular wellness but lack regular, frictionless visibility into their own health metrics.

**The Opportunity:**
Cardiovascular wellness is often invisible. Approximately 50% of adults have high blood pressure, and among those with uncontrolled metrics, nearly 60 million are completely unaware of their status. We saw a massive opportunity to empower people. Instead of waiting for an annual check-up, we are giving users continuous, effortless visibility into their health journey.

**The Solution:**
"We believe that understanding your body shouldn't require work," said the Google Health Product Lead. "With Blood Pressure Trends, we're not just providing a data point; we're providing a partner. It empowers you to see the invisible, make informed lifestyle choices, and partner with your doctor with unprecedented clarity."

**How to Get Started:**
The feature is seamlessly integrated into the new Google Health app. Simply confirm your height in the setup flow, wear your compatible smartwatch, and let your invisible guardian take it from there.

**What Users Are Saying:**
*"I always meant to keep an eye on my health, but life gets busy. Having this feature run in the background is incredible. It didn’t just give me a chart; it gave me the peace of mind to know my body is on the right track, and the agency to make better choices."*

For more information, visit health.google.com/trends.

</td>
</tr>
</table>

---

## 2. Overview

Cardiovascular health is often an invisible metric. Currently, approximately 50% of Americans have high blood pressure, yet the awareness gap is staggering. Among those with uncontrolled metrics, roughly 50% (approx. 60 million adults) are completely unaware of their status. This gap is even more pronounced in younger adults (aged 18-44), where ~70% (~20 million people) remain unaware. 

Traditional screening relies on high-friction methods: infrequent office visits that are susceptible to "White Coat" effects, or dedicated home ambulatory monitors (ABPM/cuffs) that require active user effort multiple times a day. As a result, the proactive, younger demographic simply does not check.

**Project Tidal** transforms this paradigm from active, infrequent screening to passive, recurring detection. By utilizing wrist-worn photoplethysmography (PPG) sensors and advanced foundation models, Tidal identifies long-term patterns associated with out-of-range blood pressure. It is designed strictly under FDA General Wellness guidelines—it does not monitor, diagnose, or treat hypertension. Instead, it empowers users with awareness, helping them spot trends, optimize their lifestyle, and engage in meaningful conversations with their healthcare providers.

---

## 3. Target Product Profile (The Master Grid)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | Blood Pressure Trends is intended for general wellness use to help users maintain a healthy lifestyle by estimating and spotting patterns associated with high blood pressure over time. |
| **Disclaimer** | This feature is not a medical device. It is not intended to diagnose, cure, mitigate, prevent, or treat any disease or condition, including hypertension. It should not replace clinical measurement or a healthcare professional's advice. |
| **Problem Statement** | Millions of adults lack visibility into their cardiovascular patterns due to the high friction of traditional screening methods, missing opportunities for proactive lifestyle optimization. |
| **Product Overview (P0)** | Passive, calibration-free estimation of blood pressure trends using wearable PPG and accelerometer sensors, processed by the WavesFM foundation model. |
| **Product Output (P0)** | A monthly wellness assessment indicating whether the user's cardiovascular patterns are "In-Range" or "Out-of-Range" based on the last 30 days. |
| **Positioning** | The Personal Health Agent for Cardiovascular Wellness. |
| **Product Type** | Software Function (General Wellness). |
| **Assessment Period** | Calendar Month (Requires a minimum of 14 days of valid data to generate a result). |
| **Regulated or Wellness?** | Wellness (Subject to FDA General Wellness Policy constraints; no diagnostic claims). |
| **Target Segment** | Proactive adults (18+) who want to optimize their long-term health span. |
| **Contraindication** | Not intended for individuals already diagnosed with severe clinical hypertension or those requiring active medical monitoring. |
| **Product Inputs** | Wrist-worn PPG sensor data, Accelerometer data, and User Height (confirmed via UI). |
| **Supported Devices** | Select 1P Wearables (e.g., Pixel Watch, capable Fitbit trackers). |
| **Country Availability** | 50+ countries. Gated by location: user must upload data from an eligible country during the assessment cycle. |
| **Performance Target** | Binary Classification against Office BP: Target Sensitivity 0.54, Specificity 0.90. |
| **Ongoing User Input** | Users must confirm their height via an initial education screen to ensure algorithm accuracy. |

---

## 4. Market Positioning: The Personal Health Assistant (9 Things)

| | |
| :--- | :--- |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">1</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Feature Overview</div> | **Passive Cardiovascular Awareness.** Blood Pressure Trends is a seamless wellness feature that runs quietly in the background, utilizing optical sensors to track cardiovascular patterns and provide a monthly assessment without any active user testing. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">2</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Human Significance</div> | **Illuminating the Invisible.** With nearly 60 million adults unaware of their out-of-range cardiovascular metrics, this tool shifts health management from reactive to proactive, empowering individuals to take control of their long-term vitality. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">3</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Innovation</div> | **Calibration-Free Performance.** Unlike existing market solutions that require regular calibration with a traditional cuff, Tidal is the first passive system to achieve performance comparable to clinical office measurements for identifying long-term trends. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">4</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">How it Works</div> | **Sensing to Synthesis.** The wearable captures raw PPG and accelerometer data. The system analyzes this over a 30-day window (requiring just 14 valid days) to map trends, delivering a simple, glanceable monthly report. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">5</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Rigorous Testing</div> | **Validated Against the Gold Standard.** The algorithm was fine-tuned using millions of hours of wearable data paired with 24-hour Ambulatory Blood Pressure Monitoring (ABPM) from thousands of real-world participants to ensure deep reliability. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">6</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Role of AI</div> | **Foundation Models for Health.** Powered by WavesFM, which was pre-trained on 1.3 million hours of data from 400,000 individuals, the AI acts as a sophisticated filter, distinguishing true physiological patterns from daily noise. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">7</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Launch Markets</div> | **Global Reach with Local Compliance.** Designed to launch in 50+ countries. The feature employs intelligent geo-gating to ensure assessments are only generated when data is synced from a legally eligible region. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">8</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Enhanced Peace of Mind</div> | **The Holistic Guardian Ecosystem.** Blood Pressure Trends joins Google Health’s comprehensive suite of wellness tools, creating a unified agent that looks out for your sleep, fitness, and cardiovascular longevity. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">9</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Expert Partners</div> | **Grounded in Science.** Developed in consultation with leading cardiologists and validated through rigorous internal and external clinical pathways to ensure the insights provided are both safe and highly actionable. |

---

## 5. Critical User Journeys (CUJ Maps)

**Target User:** The "Proactive Adopter" (Adults 18-44)
**Context:** Reviewing monthly wellness metrics in the Google Health App.

| Goal (The "Why") | Task (The "How") | Product/CUI (Instrumentation) |
| :--- | :--- | :--- |
| **I want to understand my cardiovascular baselines without interrupting my life.** | 1. I open Google Health and confirm my height on the feature introduction screen. | *Clicks "Confirm Height" CTA* |
| | 2. I wear my smartwatch normally during the month. | *Background Sync > 14 days* |
| **I want to check if my wellness habits are keeping me in a healthy range.** | 1. I receive a subtle evening brief at the start of a new month. | *Views Monthly Moment Card* |
| | 2. I tap the card to see if my patterns are "In-Range" or "Out-of-Range." | *Clicks into Assessment Details* |
| **I want to know how to improve my out-of-range patterns.** | 1. I read the contextual coaching tips regarding sleep and activity. | *Scrolls through Guidance UI* |
| | 2. I use Ask Coach to understand how my recent sleep debt affects my metrics. | *Submits query to Ask Coach* |
| **I want to stop tracking this metric if it causes me anxiety.** | 1. I navigate to my privacy/general data deletion settings. | *Opens Settings Menu* |
| | 2. I use General Data Deletion (GDD) to wipe my history. | *Executes Data Deletion* |

*Note: Usefulness measured by HaTS survey ("How helpful is this assessment?"). Usability measured by Successful Monthly Assessment Generation Rate (Target: >85% of eligible users).*

---

## 6. Algorithm Target Performance

### Target vs. Current Performance (Binary Classification)
*Ground Truth: ABPM. Prevalence Assumption: ~36.5%*

| Metric | Target (low 95% CI) | Current V1 (Raw) | Rationale |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | 0.54 (0.37, 0.70) | 0.67 (0.54, 0.76) | Target set based on U.S. Preventive Services Task Force (USPSTF) guidelines. Current raw model exceeds target. |
| **Specificity** | 0.90 (0.84, 0.95) | 0.90 (0.83, 0.94) | Must maintain high specificity to avoid false positive anxiety in a wellness context. |

*Note: Final 3-bin classification (Red/Yellow/Green) metrics will be locked following the March 4th checkpoint.*

---

## 7. Feature Logic & Program Timeline

### Table of Constants
| Variable | Value | Description |
| :--- | :--- | :--- |
| `ASSESSMENT_CYCLE` | Calendar Month | The period over which data is aggregated to form an assessment. |
| `MIN_VALID_DAYS` | 14 Days | The absolute minimum number of days with sufficient wear time required in a cycle to generate a result. |
| `UI_DELIVERY_TIME` | Evening Brief | Assessments are surfaced to the user in the evening flow on the 1st of the month to manage server compute load and align with user reflection time. |
| `LOCATION_GATE` | 1+ Valid Ping | If the user syncs data from an eligible country at least once during the `ASSESSMENT_CYCLE`, the assessment is generated. |

### Program Timeline
*   **Feb 17, 2026:** Algorithm 1st Checkpoint (Binary Classification Freeze).
*   **Mar 4, 2026:** Algorithm 2nd Checkpoint (3-Bin Classification Freeze).
*   **Mar 16, 2026:** Design and Architecture Alignment (Country gating, compute scheduling finalized).
*   **Q2 2026:** Dogfooding & UI Latency Testing.
*   **Q3 2026:** Launch alongside new hardware (Mukai / Pixel Watch 5).

---

## 8. Acceptance Criteria

### 1. Feature Logic Definitions
*   **Constant:** `ASSESSMENT_CYCLE` = 1 Calendar Month.
*   **Constant:** `MIN_VALID_DAYS` = 14 days.

### 2. Functional Acceptance Criteria

**Scenario 01: Successful Monthly Generation (Happy Path)**
*   **Given** the user has confirmed their height in the app.
*   **And** the user has accumulated `>= 14` days of valid PPG data in the current `ASSESSMENT_CYCLE`.
*   **When** the 1st of the subsequent month occurs.
*   **Then** the backend computes the assessment asynchronously.
*   **And** the UI displays the "Monthly Moment" card in the Evening Brief.

**Scenario 02: Insufficient Data (Edge Case)**
*   **Given** the user has accumulated `< 14` days of valid data in the current month.
*   **When** the 1st of the subsequent month occurs.
*   **Then** the system does NOT generate an assessment.
*   **And** the UI displays an educational "Wear your watch more often to get insights" prompt in place of the tile.

**Scenario 03: Country Gating - Eligible Travel**
*   **Given** the user spends 10 days in an ineligible country and 20 days in an eligible country during the month.
*   **When** the backend evaluates the `LOCATION_GATE` logic.
*   **Then** the system verifies at least 1 ping occurred in an eligible country.
*   **And** an assessment is successfully generated for that month.

**Scenario 04: Country Gating - Strictly Ineligible**
*   **Given** the user has 0 data syncs from an eligible country during the entire `ASSESSMENT_CYCLE`.
*   **And** the user has no historical assessments.
*   **When** the 1st of the month occurs.
*   **Then** no assessment is generated.
*   **And** the Blood Pressure Trends tile is hidden from the UI to prevent confusion.

### 3. Non-Functional Requirements
*   **NFR-01 (Compute Scalability):** The backend must utilize time-series embedding aggregation throughout the month to prevent system failure when batch-processing millions of assessments on the 1st of the month.
*   **NFR-02 (Privacy):** Geolocation logic (`LOCATION_GATE`) must rely on point-in-time GeoIP evaluation at ingest and must NOT store a continuous time-series history of the user's location.
*   **NFR-03 (Opt-Out):** The system must respect General Data Deletion (GDD) requests, allowing users to wipe their assessment history permanently without requiring a dedicated feature-level toggle, thereby simplifying the UX.

---

## 9. Appendix, Disclaimers & Change Log

### Consumer Interest
Internal surveys indicate high consumer willingness-to-pay (WTP) and strong interest in passive cardiovascular tracking, particularly as a differentiator for the Google Health subscription ecosystem. 

### Regulatory Disclaimers
*   **US / FDA:** This feature strictly adheres to the FDA General Wellness Policy. It is not an SaMD. All copy uses phrasing like "spot," "estimate," and "patterns" and explicitly avoids "diagnose," "monitor," or "hypertension."
*   **Global:** Feature availability is strictly gated to 50+ approved jurisdictions.

### Change Log
| Date | Section | Old Copy | New Copy |
| :--- | :--- | :--- | :--- |
| 2026-03-25 | All | N/A | Initial Draft v1 |
