# PRD: Tidal (Blood Pressure Trends) - Staff Technical Specification (v4)

## 0. Project Metadata & Approvals

### Project Overview
| Category | Value |
| :--- | :--- |
| **Deliverable** | Full Product Requirements Document (PRD) |
| **Project Code Name** | Tidal |
| **Feature Name** | Blood Pressure Trends |
| **Target Launch** | Q3 2026 (Launch with Radiance/Mukai/PW5) |
| **Localization** | 50+ Countries (Global Ingest Gating) |
| **Lock Dates** | Binary Freeze: Feb 17 | 3-Bin Freeze: Mar 4 | Architecture: Mar 16 |

### Approval Matrix
| Role | Approver | Date | Status |
| :--- | :--- | :--- | :--- |
| **Product Management** | Pramod Rudrapatna | 2026-03-25 | **Draft** |
| **Engineering** | Ryan Davidson | TBD | Pending |
| **Design / UX** | Cynthia Cruz | TBD | Pending |
| **Regulatory / Clinical** | TBD | TBD | Pending |
| **Legal / Privacy** | TBD | TBD | Pending |

---

## 1. Press Release [PR]

<table style="border: 1.5pt solid black; border-collapse: collapse; width: 100%;">
<tr>
<td style="padding: 30px;">

## Google Health Introduces Blood Pressure Trends: The Invisible Guardian for Cardiovascular Wellness
**Empowering millions to bridge the awareness gap and discover their hidden body rhythms through the power of WavesFM.**

**The Problem:**
Cardiovascular wellness is often invisible until it’s too late. Today, nearly 50% of American adults have high blood pressure, yet half of those with uncontrolled metrics—approximately 60 million people—are completely unaware of their status. For younger adults aged 18-44, the awareness gap is even wider, with 70% flying blind. Traditional screening is high-friction, infrequent, and often stressful. We believe it's time for a change.

**The Solution:**
Google Health is proud to announce Blood Pressure Trends (Project Tidal), a revolutionary, calibration-free wellness feature that works entirely in the background. By utilizing the sensors already on your wrist, Tidal estimates underlying cardiovascular patterns without the need for cumbersome inflation cuffs or manual entries. It doesn't just track; it protects.

**The 7-Star Experience:**
"We believe that understanding your body shouldn't require work," said the Google Health Product Lead. "Tidal isn't just a feature; it's a partner. It works like magic—learning your body's unique rhythms while you sleep and move. At the end of every month, it provides a clear, empathetic assessment of your cardiovascular range. If patterns trend out of range, your Personal Health Assistant is there to help you connect the dots with your sleep, activity, and stress, empowering you to have a more informed conversation with your doctor."

**Grounded in Science:**
Tidal is powered by WavesFM, our state-of-the-art multimodal foundation model, pre-trained on over 1.3 million hours of physiological data. Validated against the clinical gold-standard Ambulatory Blood Pressure Monitoring (ABPM), Tidal achieves performance comparable to traditional office measurements, but with the convenience of a passive wearable.

**Availability:**
Blood Pressure Trends will be available in over 50 countries starting in 2026, launching alongside our newest line of Google and Fitbit wearables. Join the millions taking a proactive step toward long-term vitality.

*Google Health: Your journey to a healthier life, simplified.*

</td>
</tr>
</table>

---

## 2. Overview

The "Silent Killer" is a global crisis. Hypertension accounts for 10.4 million deaths annually, yet its asymptomatic nature means most people—especially the "invincible" 18-44 demographic—ignore the signs until a major health event occurs. Our research shows that **~50% of US adults** have high blood pressure, and among those with uncontrolled metrics, **60 million adults** remain unaware.

Current solutions suffer from significant friction:
1.  **Clinical Inertia:** Infrequent office visits are prone to "White Coat Hypertension," providing a skewed snapshot of health.
2.  **User Burden:** Home monitoring (ABPM/Cuffs) requires active calibration and twice-daily effort for a week, leading to low long-term compliance.

**Project Tidal** solves this by moving from **active, infrequent screening** to **passive, recurring detection**. By leveraging the WavesFM foundation model and wrist-worn PPG/Accelerometer sensors, Tidal identifies stable patterns associated with out-of-range blood pressure over a 30-day window. This shifts the user's role from a "patient performing a test" to an "individual gaining awareness," enabling early intervention and behavioral optimization in sleep, stress, and activity.

---

## 3. Target Product Profile (The Master Grid)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | General wellness use to help users maintain a healthy lifestyle by estimating and spotting patterns associated with high blood pressure over time. |
| **Disclaimer** | This feature is not a medical device. It is not intended to diagnose, cure, mitigate, prevent, or treat any disease or condition, including hypertension. |
| **Problem Statement** | Millions of adults lack visibility into cardiovascular patterns due to high friction in traditional screening methods, missing early optimization opportunities. |
| **Product Overview (P0)** | Passive, calibration-free estimation of blood pressure trends using PPG and accelerometer sensors, processed by WavesFM. |
| **Product Output (P0)** | A monthly wellness assessment: "In-Range" or "Out-of-Range" patterns based on 30-day longitudinal data. |
| **Positioning** | The Personal Health Assistant for Cardiovascular Wellness. |
| **Product Type** | Software-only wellness function. |
| **Assessment Period** | Calendar Month (minimum 14 valid days required). |
| **Regulated or Wellness?** | Wellness (FDA General Wellness Policy compliant). |
| **Target Segment** | Proactive adults (18+) focused on long-term health span and vitality. |
| **Contraindication** | Not for individuals with diagnosed severe clinical hypertension or those requiring active medical monitoring. |
| **Product Inputs** | Wrist PPG (528nm), Tri-axial Accelerometer, and User Height. |
| **Supported Devices** | Pixel Watch (Series 3+), Radiance (2026), Mukai (2026). |
| **Country Availability** | 50+ Countries (Gated via ingest GeoIP). |
| **Performance Target** | Sensitivity > 0.54 | Specificity > 0.90 (vs. Office BP). |
| **Ongoing User Input** | Height confirmation required at setup and periodically for algorithm accuracy. |

---

## 4. Market Positioning: The Personal Health Assistant (9 Things)

<table style="border: 1.5pt solid black; border-collapse: collapse; width: 100%;">
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">1</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Feature Overview</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Passive Awareness.** Tidal runs quietly in the background, utilizing optical sensors to track cardiovascular patterns and provide a monthly assessment without any active user testing or cuff-based calibration.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">2</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Human Significance</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Illuminating the Invisible.** With nearly 60 million adults unaware of their out-of-range cardiovascular metrics, this tool shifts health management from reactive to proactive, empowering individuals to take control of their long-term vitality.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">3</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Innovation</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Calibration-Free Performance.** Unlike existing market solutions that require regular calibration with a traditional cuff, Tidal is the first passive system to achieve performance comparable to clinical office measurements for identifying long-term trends.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">4</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">How it Works</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Sensing to Synthesis.** The wearable captures raw PPG data. The system analyzes this over a 30-day window (requiring just 14 valid days) to map trends, delivering a simple, glanceable monthly report.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">5</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Rigorous Testing</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Validated Against the Gold Standard.** The algorithm was fine-tuned using millions of hours of wearable data paired with 24-hour Ambulatory Blood Pressure Monitoring (ABPM) from thousands of real-world participants.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">6</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Role of AI</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Foundation Models for Health.** Powered by WavesFM, which was pre-trained on 1.3 million hours of data, the AI acts as a sophisticated filter, distinguishing true physiological patterns from daily motion noise.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">7</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Launch Markets</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Global Compliance.** Designed to launch in 50+ countries. The feature employs intelligent geo-gating to ensure assessments are only generated when data is synced from a legally eligible region.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">8</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Peace of Mind</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Enhanced Holistic Health.** Blood Pressure Trends joins Google Health’s comprehensive suite of wellness tools, creating a unified agent that looks out for your sleep, fitness, and cardiovascular longevity.
</td>
</tr>
<tr>
<td style="width: 1.5in; padding: 15px; border: 1pt solid black; vertical-align: top;">
<div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">9</div>
<div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Expert Partners</div>
</td>
<td style="padding: 15px; border: 1pt solid black; vertical-align: middle;">
**Grounded in Science.** Developed in consultation with leading cardiologists and validated through rigorous clinical pathways to ensure insights are safe and actionable.
</td>
</tr>
</table>

---

## 5. Critical User Journeys (CUJ Maps)

**Target User:** Proactive Adopter (Adults 18-44) seeking structural early warning signs.

| Goal (The "Why") | Task (The "How") | Product/CUI | Health Metric |
| :--- | :--- | :--- | :--- |
| **Invisible Onboarding** | 1. Open Google Health app. | *Intro Education Screen* | Completion Rate |
| | 2. Confirm pre-populated height. | *Height Verification UI* | TSR (Time to Success) |
| **Monthly Moment** | 1. Receive Evening Brief on the 1st. | *Push Notification / Tile* | Open Rate |
| | 2. View 30-day assessment result. | *L3 Detail Assessment* | Session Depth |
| **Causal Insight** | 1. Review correlation with sleep data. | *Insights Ribbon* | Feature Attribution |
| | 2. Query Ask Coach about lifestyle. | *LLM Assistant Chat* | Engagement Score |
| **Sync Confidence** | 1. Sync data at 14:00 on the 1st. | *Force Sync Action* | Data Freshness % |
| | 2. Find result updated in Evening Brief. | *Evening Delivery (18:00)* | Data Integrity SAT |
| **Privacy Mastery** | 1. Request data deletion via settings. | *Settings > GDD* | Deletion Success Rate |

*Note: Usefulness measured by HaTS survey ("How empowered do you feel?"). Health score measured by TSR per task.*

---

## 6. Algorithm Target Performance

### 6.1 Performance Targets (Binary Classification)
*Ground Truth: ABPM. Assume 36.5% Prevalence.*

| Metric | Target (low 95% CI) | Current V1 (Raw) | Rationale |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | **0.54** (0.37, 0.70) | 0.67 (0.54, 0.76) | Target set based on USPSTF screening benchmarks. |
| **Specificity** | **0.90** (0.84, 0.95) | 0.90 (0.83, 0.94) | Mandatory high specificity to avoid false alarm fatigue. |
| **Operating Point**| **94.5% Spec** | Achieved | Optimized to maximize sensitivity at a fixed high specificity. |

### 6.2 Technical Gates & SQI
| Data Step | Specification | Rationale |
| :--- | :--- | :--- |
| **Signal Quality (SQI)**| **SQI ≥ 0.5** | Template matching gate; prevents embedding noise. |
| **Model Selection** | **Sleep > 3 hrs** → All-day | Accounts for dips in nighttime blood pressure. |
| **Sampling Rate** | **25 Hz** | Mandatory for WavesFM EfficientNet-B1 backbone. |
| **Valid Day** | **≥ 12 hours** wear | Minimum daily data density for embedding stability. |

---

## 7. Feature Logic & Program Timeline

### Table of Constants
| Variable | Value | Description |
| :--- | :--- | :--- |
| `ASSESSMENT_CYCLE` | Calendar Month | Anchored to User Local Time. |
| `SYNC_BUFFER` | 12 Hours | Ends at 12:00 local on the 1st to capture "last day" syncs. |
| `UI_DELIVERY` | 18:00 Local | Assessments surfaced in the Evening Brief moment. |
| `LOCATION_GATE` | 1+ Valid Ping | 1+ sync from an eligible country during the cycle triggers result. |
| `HEIGHT_MIN` | 1' 9.5" | Global anthropometric floor for algorithm safety. |
| `HEIGHT_MAX` | 8' 11" | Global anthropometric ceiling for algorithm safety. |

### Program Milestones
*   **Feb 17, 2026:** Binary Operating Point Freeze.
*   **Mar 4, 2026:** 3-Bin (Red/Yellow/Green) Logic Freeze.
*   **Mar 16, 2026:** Architecture Alignment (TZ/Sync logic finalized).
*   **Q2 2026:** Engineering Team Food & Dogfooding.
*   **Q3 2026:** GA Launch alongside Radiance & Pixel Watch 5.

---

## 8. Acceptance Criteria (Technical)

**Scenario 01: Core Logic - SQI Reject**
*   **Given** the user's PPG data has an `SQI < 0.5` for a 15-second segment.
*   **When** the Ingest pipeline processes the packet.
*   **Then** the system must discard the segment.
*   **And** the segment must NOT contribute to the user-level embedding.

**Scenario 02: State Transition - Awake vs. All-day**
*   **Given** the user has accumulated 14 valid days.
*   **And** the total sleep duration recorded is **2 hours** for the cycle.
*   **When** the classifier is triggered on the 1st.
*   **Then** the system must route the 257-element vector to the **Awake Model** (9a-9p).
*   **And** the assessment status is generated based on daytime-only baselines.

**Scenario 03: Edge Case - Cross-Month Time Zone Shift**
*   **Given** the user is in London (UTC+0) on the 31st and Sydney (UTC+11) on the 1st.
*   **When** the device performs its first sync on the 1st.
*   **Then** the `ASSESSMENT_CYCLE` closure is determined by Sydney local time.
*   **And** the 12-hour `SYNC_BUFFER` is anchored to Sydney (UTC+11).

**Scenario 04: Error Handling - Height Modification**
*   **Given** the user modifies their height in the Fitbit profile during the month.
*   **When** the monthly classifier runs.
*   **Then** the system must repeat the height validation check (`HEIGHT_MIN/MAX`).
*   **And** the most recent valid height must be Z-normalized as the 257th embedding element.

---

## 9. Appendix, Disclaimers & Change Log

### Consumer Interest & WTP
*   **US Willingness to Pay:** Total Sample $0.99 | Proactive Adopters **$1.03**.
*   **Global Preference:** Japan shows the highest incremental WTP for detection features at **$1.27**.
*   **Strategic Lift:** Rebranding from Fitbit to Google + the 2026 feature set provides a **+15pt** global increase in share of preference.

### Disclaimers
*   **US / FDA:** Strictly Wellness. Copy must use "estimate," "patterns," and "spot." Do NOT use "detect hypertension."
*   **EMEA:** Regulatory alignment for 50+ jurisdictions required prior to GA.

### Change Log
| Date | Section | Old Copy | New Copy |
| :--- | :--- | :--- | :--- |
| 2026-03-25 | All | N/A | Initial Draft v1 |
| 2026-03-25 | All | v2/v3 | Exhaustive v4: Full table format, HTML styling for 9-Things, deep SQI/Filtering logic, and technical Gherkin scenarios. |
