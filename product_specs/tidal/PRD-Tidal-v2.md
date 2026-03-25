# PRD: Tidal (Blood Pressure Trends) - v2

## 0. Project Metadata & Approvals

| Category | Value |
| :--- | :--- |
| **Deliverable** | Full Product Requirements Document (PRD) |
| **Project Name** | Tidal (Blood Pressure Trends) |
| **Primary Objective** | Passive, calibration-free wellness feature for cardiovascular pattern awareness. |
| **Regulatory Classification** | General Wellness (Non-SaMD) |
| **Target Launch** | 2026 |

### Approval Matrix
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

## 2. Overview & Market Urgency

| Category | Description |
| :--- | :--- |
| **Market Gap** | ~50% of US adults have high blood pressure; ~50% of those remain unaware of their uncontrolled metrics (~60M adults). |
| **Demographic Pain Point** | ~70% of younger adults (18-44) with uncontrolled hypertension are unaware due to "Silent Killer" nature and high-friction screening. |
| **Current Friction** | Office visits (White Coat effect), Home ABPM (manual cuffs, 2x/day effort). |
| **Project Tidal Value** | Shifts from active, infrequent screening to passive, continuous detection using wrist-worn PPG and foundation models. |
| **Strategy Alignment** | Positioned as a wellness "North Star" under Google Health's mission to make invisible health signals visible. |

---

## 3. Target Product Profile (The Master Grid)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | General wellness use to help users maintain a healthy lifestyle by estimating and spotting patterns associated with high blood pressure over time. |
| **Disclaimer** | Not a medical device. Not intended to diagnose, cure, mitigate, prevent, or treat any disease (e.g., hypertension). |
| **Problem Statement** | Awareness gap in cardiovascular health due to friction in traditional clinical and home monitoring methods. |
| **Product Overview** | Passive, calibration-free blood pressure trend estimation using PPG and accelerometer sensors. |
| **Product Output** | Monthly wellness assessment: "In-Range" or "Out-of-Range" trends. |
| **Positioning** | The Personal Health Agent for Cardiovascular Wellness. |
| **Assessment Period** | Calendar Month. |
| **Regulated or Wellness?** | Wellness (FDA General Wellness Policy compliant). |
| **Supported Devices** | Select 1P Smartwatches (Pixel Watch / Radiance). |
| **Country Availability** | 50+ Countries (Gated by location-at-ingest logic). |
| **Ongoing User Input** | Height (verified at onboarding and periodically). |

---

## 4. Market Positioning: The Personal Health Assistant (9 Things)

| | |
| :--- | :--- |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">1</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Feature Overview</div> | **Passive Cardiovascular Awareness.** Runs quietly in the background tracking body rhythms via PPG sensors. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">2</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Human Significance</div> | **Illuminating the Invisible.** Bridges the awareness gap for the 60M adults unaware of their status. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">3</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Market Innovation</div> | **Calibration-Free Performance.** First passive system to achieve clinical-office-grade performance for spotting trends. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">4</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">How it Works</div> | **Sensing to Synthesis.** Maps trends over 30 days (requires 14 valid days) using user-level embeddings. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">5</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Rigorous Testing</div> | **Validated vs Gold Standard.** Fine-tuned on millions of hours paired with 24-hour ABPM clinical data. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">6</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Role of AI</div> | **Foundation Models for Health.** Powered by WavesFM, acting as a sophisticated filter for true physiological patterns. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">7</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Launch Markets</div> | **Global Compliance.** Launching in 50+ countries with intelligent geo-gating at the ingest layer. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">8</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Ecosystem Integration</div> | **Holistic Guardian.** Joins sleep, fitness, and heart rhythm tools to create a unified health agent. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">9</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Expert Partners</div> | **Grounded in Science.** Developed with leading cardiologists to ensure safe and actionable wellness insights. |

---

## 5. Critical User Journeys (CUJ Maps)

| Goal (The "Why") | Task (The "How") | Product/CUI | Health Metric |
| :--- | :--- | :--- | :--- |
| **Frictionless Baseline** | 1. Open app and confirm height. | *Height Input UI* | Onboarding Success % |
| | 2. Wear watch normally. | *Background Sync* | Valid Data Day Rate |
| **Wellness Check-in** | 1. Receive evening brief on the 1st. | *Monthly Moment Card* | Notification CTR |
| | 2. Review "In-Range" status. | *Assessment Detail Page* | Session Time on Task |
| **Pattern Context** | 1. Ask Coach about sleep impact. | *LLM Chat Interface* | Coach Engagement Score |
| | 2. Review personalized guidance. | *Wellness Insights* | Guided Action % |
| **Sync Management** | 1. Sync watch late on the 1st (14:00). | *Manual/Auto Sync* | Sync Completion % |
| | 2. Find result includes final day. | *Evening Brief (18:00)* | Data Freshness SAT |
| **Privacy Control** | 1. Access Privacy Settings. | *Settings Menu* | TSR (Time to Success) |
| | 2. Delete assessment history. | *GDD Interface* | Deletion Completion % |

---

## 6. Algorithm Requirements & Target Performance

### 6.1 Data Quality & Signal Hygiene (SQI)
| Requirement | Specification | Rationale |
| :--- | :--- | :--- |
| **Signal Quality Index (SQI)** | **SQI ≥ 0.5** (based on template matching) | Ensures PPG waveform is reliable enough for embedding generation. |
| **Preprocessing Filter** | DC removal + 4th-order Butterworth (0.5-12 Hz) | Removes motion artifacts and environmental noise. |
| **Normalization** | Exponential Moving Average (alpha=0.01) | Stabilizes signal variance across different skin tones and fit. |

### 6.2 Data Sufficiency
| Variable | Requirement | Description |
| :--- | :--- | :--- |
| **Valid Day** | **≥ 12 hours** of wear time | Minimum daily exposure needed for daily embedding. |
| **Assessment Cycle** | **≥ 14 valid days** in 30 days | Minimum data density required for longitudinal classification. |
| **Sleep Threshold** | **> 3 hours** total sleep | Determines whether to use the **All-day model** vs **Awake model**. |

### 6.3 Target Performance (Binary)
| Metric | Target (low 95% CI) | Status | Operating Point |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | **0.54** (0.37, 0.70) | Exceeds (Raw: 0.67) | Maximize sensitivity at Specificity = 94.5% |
| **Specificity** | **0.90** (0.84, 0.95) | On Track (Raw: 0.90) | Optimized to minimize false alarm fatigue. |

---

## 7. Feature Logic & Time Zone Normalization

| Logic Component | Specification |
| :--- | :--- |
| **Cycle Window** | **Current Local Time** (00:00:00 1st to 23:59:59 31st). |
| **Sync Buffer** | **12 Hours** (Ends at 12:00 on the 1st) to wait for "last day" data packets. |
| **UI Surface Time** | **18:00 Local** (Evening Brief) on the 1st of the month. |
| **Asynchronous Compute** | User-level embeddings are aggregated incrementally throughout the month to manage 1st-of-month load. |
| **Location Gate** | **1+ Valid Ping** from an eligible country (GeoIP check at ingest) triggers generation. |
| **Time Zone Shift** | If time zone changes cross-month, the cycle closure is determined by the device's local time at the point of first sync on the 1st. |

---

## 8. Acceptance Criteria (Technical)

| Scenario ID | Scenario Name | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | **SQI Rejection** | SQI score < 0.5 for a 10-minute window. | Ingest pipeline processes raw PPG. | Packet is discarded; data does not contribute to daily embedding. |
| **AC-02** | **Model Selection** | User sleep data ≤ 3 hours for the month. | 30-day classifier is triggered. | System routes user embedding to the **Awake Model** (9a-9p). |
| **AC-03** | **Sync Buffer Success** | 14 valid days met; 31st data synced at 11:00 on the 1st. | 18:00 Evening Brief occurs. | Assessment is generated including 31st data. |
| **AC-04** | **Geo-Eligibility** | User spend 29 days in unsupported country; 1 day in supported. | Location gate evaluates during month. | Assessment is generated due to "1+ valid ping" rule. |
| **AC-05** | **Privacy Adherence** | User requests GDD. | System processes deletion. | All Tidal assessment records are wiped; no persistent time-series location stored. |

---

## 9. Appendix & Change Log

### Program Timeline
| Milestone | Date |
| :--- | :--- |
| **Binary Checkpoint** | Feb 17, 2026 |
| **3-Bin Checkpoint** | Mar 4, 2026 |
| **Architecture Alignment** | Mar 16, 2026 |
| **GA Launch** | Q3 2026 |

### Change Log
| Date | Section | Old Copy | New Copy |
| :--- | :--- | :--- | :--- |
| 2026-03-25 | All | Initial v1 | Complete v2: Full table format, added SQI (≥0.5), Sleep (>3hr) model selection, and detailed TZ/Sync logic. |
