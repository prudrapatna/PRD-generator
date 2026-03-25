# PRD: Tidal (Blood Pressure Trends) - Full Technical Specification

## 0. Project Metadata & Approvals

### Project Identification
| Category | Value |
| :--- | :--- |
| **Deliverable** | Full Product Requirements Document (PRD) |
| **Project Name** | Tidal (Blood Pressure Trends) |
| **Primary Objective** | Deliver a passive, calibration-free wellness feature for cardiovascular pattern awareness. |
| **Regulatory Status** | General Wellness (FDA Low-Risk Policy compliant; Non-SaMD) |
| **Primary Technology** | WavesFM Foundation Model (Multimodal Waveform AI) |
| **Hardware Targets** | Radiance (2026), Mukai (2026), Pixel Watch 5 (2026) |

### Approval Matrix
| Role | Approver | Date | Status |
| :--- | :--- | :--- | :--- |
| **Product Manager** | Pramod Rudrapatna | 2026-03-25 | Final Draft |
| **Engineering Lead** | Ryan Davidson | TBD | Pending |
| **UX/Design Lead** | Cynthia Cruz | TBD | Pending |
| **Regulatory/Legal** | TBD | TBD | Pending |

---

## 1. Press Release: The 7-Star Experience

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

</td>
</tr>
</table>

---

## 2. Overview & Market Context

| Category | Definition |
| :--- | :--- |
| **Problem Definition** | Awareness gap: ~50% of adults with uncontrolled hypertension are unaware of their status due to the "Silent Killer" (asymptomatic) nature of the condition. |
| **Market Friction** | Office visits (infrequent, White Coat bias) and Home Monitoring (high effort, cuff calibration requirements). |
| **Strategic Goal** | Transition cardiovascular screening from active/infrequent to passive/continuous. |
| **Data Grounding** | ~20 million young adults (18-44) currently lack any reliable screening mechanism. |
| **Core Value** | Agency and empowerment through longitudinal pattern identification. |

---

## 3. Target Product Profile (The Master Grid)

| Category | Definition |
| :--- | :--- |
| **Intended Use** | A general wellness tool to promote lifestyle behavior changes by identifying long-term patterns associated with out-of-range blood pressure. |
| **Disclaimer** | Not intended to diagnose or treat hypertension. Not a replacement for clinical devices or medical advice. |
| **Problem Statement** | Invisible cardiovascular patterns leading to late-stage health interventions. |
| **Positioning** | The Personal Health Agent for Cardiovascular Wellness. |
| **Assessment Period** | Calendar Month (Reset at 00:00 local time on the 1st). |
| **Inputs** | Raw PPG (Green, 528nm), Tri-axial Accelerometer, and User Height. |
| **Height Constraints** | Minimum: 1' 9.5" | Maximum: 8' 11". |
| **Data Sufficiency** | ≥ 14 valid days per cycle. |
| **Valid Day** | ≥ 12 hours of wear time within 24 hours. |
| **Supported Devices** | Pixel Watch (Series 3+), Radiance, Mukai. |
| **Country Support** | 50+ Jurisdictions (Geo-gated at ingest). |

---

## 4. Market Positioning (The 9 Things)

| | |
| :--- | :--- |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">1</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Feature Overview</div> | **Passive Awareness.** A background wellness feature that identifies body rhythms without active user intervention. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">2</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Human Significance</div> | **Bridging the Gap.** Targets the 60M adults currently "flying blind" regarding their cardiovascular trends. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">3</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Market Innovation</div> | **Calibration-Free.** First passive system to achieve clinical-grade trend spotting without a secondary cuff. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">4</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">How it Works</div> | **Sensing to Synthesis.** PPG analysis optimized via WavesFM multimodal foundation model. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">5</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Rigorous Testing</div> | **ABPM Validation.** Validated against the 24-hour gold-standard Ambulatory Blood Pressure Monitoring. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">6</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">The Role of AI</div> | **Foundation Model Power.** Pre-trained on 1.3M hours of physiological data to ignore "motion noise." |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">7</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Launch Markets</div> | **Global Reach.** Available in 50+ countries with local regulatory alignment. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">8</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Enhanced Peace of Mind</div> | **Holistic Guardian.** Integrates with sleep and activity coaching for total health visibility. |
| <div style="color: #1a73e8; font-size: 24pt; font-weight: bold;">9</div><div style="color: #1a73e8; font-size: 11pt; font-weight: bold;">Expert Partners</div> | **Clinically Informed.** Built in consultation with leading global cardiologists. |

---

## 5. Critical User Journeys (CUJ Maps)

| Goal (The "Why") | Task (The "How") | Product/CUI | Health Metric |
| :--- | :--- | :--- | :--- |
| **I want a guardian that requires zero effort.** | 1. Confirm height during app onboarding. | *Height Input Table* | Completion Rate |
| | 2. Wear watch for at least 14 days. | *Background Ingest* | Wear Compliance |
| **I want to know if my trends are healthy.** | 1. View "In-Range" status in the Evening Brief on the 1st. | *Monthly Moment Card* | Notification Open Rate |
| | 2. Tap to see detailed monthly analysis. | *L3 Detail Page* | Session Depth |
| **I want to understand the "Why" behind a spike.** | 1. Review correlation with sleep/stress metrics. | *Insights Ribbon* | Feature Attribution |
| | 2. Query Ask Coach about lifestyle impact. | *PHA Chat UI* | Query Relevance Score |
| **I want my data to be fresh, even if I sync late.** | 1. Sync data at 11:00 on the 1st. | *Manual Sync* | Sync Latency % |
| | 2. See result updated at 18:00 delivery. | *Evening Brief* | Data Freshness SAT |
| **I want to travel without losing my assessment.** | 1. Sync data at least once from a supported country. | *Location Gate* | Geo-Eligibility % |
| **I want control over my health data.** | 1. Access Privacy menu and request GDD. | *Settings > GDD* | Deletion TSR |

---

## 6. Algorithm Principles & Target Performance

### 6.1 Data Quality & SQI (The Ingest Gate)
| Requirement | Specification | Rationale |
| :--- | :--- | :--- |
| **Signal Quality Index (SQI)** | **SQI ≥ 0.5** | Based on template matching to exclude noise. |
| **On-Device Filter** | 4th-order Butterworth (0.5-12 Hz) | Initial DC removal and pulse contour preservation. |
| **Cloud Filter (PPG)** | Bandpass 1-12 Hz | Optimized for user-level embedding extraction. |
| **Cloud Filter (ACCEL)** | Bandpass 0.5-50 Hz | Magnitude: `sqrt(x^2 + y^2 + z^2)`. |
| **Sampling Rate** | 25 Hz (Concomitant) | Mandatory for foundation model compatibility. |

### 6.2 Logic & Model Selection
| Decision | Threshold / Rule | Definition |
| :--- | :--- | :--- |
| **Hypertension Threshold** | **0.5699093902474069** | Probability score above which a notification triggers. |
| **All-day Model** | **Sleep > 3 hours** | Uses data from the full 24-hour cycle. |
| **Awake Model** | **Sleep ≤ 3 hours** | Restricted to 9a-9p data to avoid baseline shifts. |
| **Normalization** | Z-score (User Height) | Height is concatenated as the 257th element. |

### 6.3 Target Performance (Binary)
| Metric | Target (low 95% CI) | Rationale |
| :--- | :--- | :--- |
| **Sensitivity** | **0.54** (0.37, 0.70) | Comparative to clinical office BP performance. |
| **Specificity** | **0.90** (0.84, 0.95) | Minimal false positives to preserve user trust. |
| **Operating Point** | **94.5% Specificity** | Threshold selected to maximize sensitivity at this specificity. |

---

## 7. Feature Logic: Time Zone & Sync Synchronization

| logic Component | Specification |
| :--- | :--- |
| **Cycle Anchoring** | **User Local Time.** Cycles close at 23:59:59 on the last day of the month. |
| **Sync Buffer Window** | **12 Hours.** Computation is held until 12:00 local on the 1st to allow for late syncs. |
| **UI Delivery Moment** | **18:00 Local.** Assessments appear in the "Evening Brief" flow. |
| **Cross-TZ Logic** | Cycle closure determined by the local time of the device at the point of first sync on the 1st. |
| **Data Completeness** | If `MIN_VALID_DAYS` (14) are met, assessment proceeds using all available data at the end of the buffer. |
| **Location Gate** | **1+ Valid Ping.** At least one sync must originate from an eligible GeoIP during the cycle. |

---

## 8. Acceptance Criteria (Technical Gherkin)

| Scenario ID | Scenario | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | **SQI Rejection** | SQI < 0.5 for 10 consecutive mins. | Raw PPG is processed. | Packet is discarded; no embedding generated. |
| **AC-02** | **Model Selection** | Total sleep > 3 hrs in cycle. | Classifier is triggered. | User routed to **All-day Model**. |
| **AC-03** | **Delayed Sync** | 14 valid days met; 31st synced at 10:00 on 1st. | 18:00 delivery occurs. | 31st data is included in the monthly score. |
| **AC-04** | **Geo-Ping Rule** | User travels to unsupported region for 20 days. | Sync occurs 1x in supported region. | `LOCATION_GATE` passes; assessment generated. |
| **AC-05** | **Privacy Wipe** | User requests GDD. | System processes deletion. | All Tidal historical scores and location pings are wiped. |
| **AC-06** | **Height Bound** | User enters height = 9' 0". | Ingest check occurs. | Value is rejected; user prompted for valid input. |

---

## 9. Appendix & Change Log

### Program Timeline
| Milestone | Date |
| :--- | :--- |
| **Binary Operating Point Freeze** | Feb 17, 2026 |
| **3-Bin (Red/Yellow/Green) Freeze** | Mar 4, 2026 |
| **Architecture Alignment (TZ/Sync)** | Mar 16, 2026 |
| **GA Launch** | Q3 2026 |

### Change Log
| Date | Section | Old Copy | New Copy |
| :--- | :--- | :--- | :--- |
| 2026-03-25 | All | N/A | Initial Draft v1 |
| 2026-03-25 | All | Condensed v2 | Exhaustive v3: Added SQI details, Filter specs, Sleep thresholds, and Technical ACs. |
