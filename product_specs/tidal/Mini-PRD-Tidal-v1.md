# Mini Product Narrative: Tidal

## 1. Approval Cover Page
| Approver | Approval Status | Date |
| :--- | :--- | :--- |
| | | |
| | | |
| | | |
| | | |

## 2. The Press Release / Narrative
<table style="border: 1.5pt solid black; padding: 10px; width: 100%;">
<tr><td>

# Helping your heart thrive: Google introduces a quieter way to understand your blood pressure

**[October 15, 2026]:**

High blood pressure is often called the silent killer because it rarely shows symptoms until it's too late. Millions of people go about their days—working, sleeping, living—unaware that their cardiovascular system is under sustained stress. Traditional spot-checks with cuffs are a hassle and only capture a single moment in time, leaving a massive gap in our understanding of our own heart health.

Today, we're introducing Tidal for Pixel Watch and Fitbit, a general wellness feature designed to estimate blood pressure trends quietly in the background. No cuffs to pump, no schedules to remember. By leveraging passive, longitudinal monitoring using the optical sensors already on your wrist, Tidal analyzes your data over 30 days to build a continuous picture of your heart's efficiency.

When Tidal notices your estimated blood pressure range is trending higher, it doesn't just alert you; it coaches you. By connecting these trends to your daily habits—like how you slept last week or changes in your activity levels—Tidal empowers you to make informed lifestyle choices.

"Our vision is to help people live longer, healthier lives by making the invisible, visible," says Rishi Chandra, VP of Google Health. "By moving from occasional checks to continuous, background understanding, we can foster early awareness before problems become severe."

"This feature is designed to start conversations between users and their doctors, rather than replace medical care," notes an expert clinician. "It gives people the context they need to make healthier decisions every day."

Designed to start conversations about health, not replace medical care. In a world of constant alerts, Google is taking a quieter approach: one thoughtful insight a month.

</td></tr>
</table>

## 3. Overview
**The "Silent Killer" & Awareness Gap:** High blood pressure is the #1 risk factor for cardiovascular death, yet ~60-70% of younger adults (18-44) with uncontrolled high blood pressure are unaware of their condition. Because it is asymptomatic, users lack urgency to check.

**The "Single-Reading" Bias:** Users often misinterpret a single high reading from a cuff as a "spike" or error. Tidal solves this by aggregating data over 14+ days, providing a sustained, credible signal that overcomes user inertia.

**Lifestyle Disconnect:** Users struggle to connect abstract numbers to daily choices. Tidal bridges this gap by correlating trends directly with sleep, nutrition, and stress data.

## 4. Target Product Profile (The Master Grid)
| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | A general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. Designed to promote positive lifestyle behavior changes by helping users understand how daily habits correlate with estimated blood pressure range. |
| **Problem Statement** | Users lack awareness of sustained high blood pressure due to its asymptomatic nature and the friction of traditional cuff-based spot checks. |
| **Product Overview** | A passive, longitudinal monitoring feature on wrist-worn devices that estimates blood pressure trends and range over a 30-day window without calibration. |
| **Feature Prioritization** | P0: Passive 30-day range estimation, Out-of-range notifications. P1: Lifestyle correlation insights (sleep, stress, activity). |
| **Target User** | Proactive wellness seekers and individuals looking to understand the impact of lifestyle on cardiovascular health. |
| **Positioning** | "Health Guardian" - Focus on inferred trends, lifestyle correlations, and peace of mind. |
| **Suggested Notification** | "Your estimated blood pressure range has been trending higher over the last month. Let's look at how your recent sleep patterns might be playing a role." |
| **Algorithm Output** | Binary Classification: In-Range vs. Out-of-Range. |
| **Product Type** | Passive, Continuous and Recurring Assessment. |
| **Assessment Period** | 30-day rolling window, requiring ≥14 valid days of data (≥8 hours wear time/day). Out of range triggered if ≥14 days exceed threshold (Systolic ≥ 130 mmHg OR Diastolic ≥ 80 mmHg). |
| **Regulated or Wellness?** | General Wellness (Not intended to diagnose, treat, cure, or prevent any disease). |
| **Disclaimer / Contraindication** | Not intended to diagnose or treat hypertension. Not a replacement for a medical professional or traditional blood pressure cuff. |
| **Algorithm Inputs** | PPG + Accelerometer. |
| **Supported Devices** | Pixel Watch and Fitbit devices with compatible sensors. |
| **Country Availability** | TBD (Pending regional wellness feature guidelines). |
| **Performance Target** | Non-inferiority to Office Blood Pressure Measurement (OBPM). Target Sensitivity: 54%, Specificity: 90%. |
| **Ongoing User Input** | Passive wear; occasional prompts to review lifestyle correlations. |

## 5. Market Positioning: The Personal Health Assistant (9 Things)
<table style="border: 1pt solid black; border-collapse: collapse;">
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 1.5in; padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">1</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Feature on PHA</div>
    </td>
    <td style="width: 5in; padding: 10px;">Tidal operates quietly as a core component of the Personal Health Assistant, automatically analyzing your data in the background to provide a single, thoughtful insight a month.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">2</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Clinical Significance</div>
    </td>
    <td style="padding: 10px;">Tidal is validated against the clinical gold standard of 24-Hour Ambulatory Blood Pressure Monitoring (ABPM), capturing true 24-hour heart health including sleep, unlike spot-checks that miss nocturnal variability.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">3</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">First-of-its-kind</div>
    </td>
    <td style="padding: 10px;">A truly passive, calibration-free wellness tool that moves beyond simple alerts to provide contextual coaching based on your unique lifestyle data.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">4</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">How it works</div>
    </td>
    <td style="padding: 10px;">Utilizing advanced optical (PPG) and accelerometer sensors, Tidal aggregates your physiological data over a 30-day window to identify sustained patterns rather than temporary spikes.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">5</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Rigorous testing</div>
    </td>
    <td style="padding: 10px;">Our pivotal study involves ~2,000 participants undergoing head-to-head comparison of Tidal against Office BP and ABPM to ensure robust, non-inferior performance.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">6</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">AI Architecture</div>
    </td>
    <td style="padding: 10px;">Tidal's V1 SPLAT Model uses advanced machine learning to classify trends into In-Range vs. Out-of-Range with high specificity (93%), minimizing false alarms.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">7</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Launch markets</div>
    </td>
    <td style="padding: 10px;">Targeting key global markets aligned with local wellness regulatory guidelines to ensure broad accessibility.</td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">8</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Enhanced peace of mind</div>
    </td>
    <td style="padding: 10px;">Integrated into the broader Google Health ecosystem, Tidal offers reassurance by giving you visibility into a previously invisible health metric.</td>
  </tr>
  <tr>
    <td style="padding: 10px;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">9</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Expert Partners</div>
    </td>
    <td style="padding: 10px;">Developed with input from clinical experts to ensure the guidance provided empowers users and supports, rather than replaces, traditional medical advice.</td>
  </tr>
</table>

## 6. Critical User Journeys (CUJs)
| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **I want to seamlessly monitor my health without adding chores to my day** | 1. I wear my watch as usual without performing manual calibrations. | *Passive Background Data Collection* |
| **I want reassurance that my cardiovascular health is stable** | 1. I open the app to check my monthly status summary. | *Monthly Status Dashboard View* |
| **I want to know if my lifestyle is negatively impacting my heart** | 1. I review a notification indicating my range is trending higher. <br> 2. I read the insight connecting this trend to my recent poor sleep. | *Contextual Nudge Notification Tap* |
| **I want to have a more informed conversation with my doctor** | 1. I export a summary of my 30-day trends to show at my next appointment. | *PDF Export Button Click* |

## 7. Feature Logic Definitions & Algorithm Performance

**Feature Logic**
| Constant | Value | Description |
| :--- | :--- | :--- |
| `MIN_WEAR_HOURS_PER_DAY` | 8 hours | Minimum required wear time to constitute a valid day. |
| `MIN_VALID_DAYS` | 14 days | Minimum valid days required within the observation window. |
| `OBSERVATION_WINDOW_DAYS` | 30 days | The rolling window used to calculate sustained trends. |
| `OUT_OF_RANGE_THRESHOLD` | ≥14 days | Number of days exceeding Systolic ≥ 130 mmHg OR Diastolic ≥ 80 mmHg probability threshold. |

**Performance Target vs. Clinical Status Quo (OBPM)**
| Metric | Target (low 95% CI) | Rationale |
| :--- | :--- | :--- |
| **Sensitivity** | 54% (37%, 70%) | Goal is non-inferiority to Office BP benchmark for identifying sustained high blood pressure. |
| **Specificity** | 90% (84%, 95%) | Maintain high specificity to minimize false positive nudges. |

**Current Performance (V1 SPLAT Model)**
| Study Size | Prevalence | Sensitivity (95% CI) | Specificity (95% CI) |
| :--- | :--- | :--- | :--- |
| ~2,000 (Target) | 36.5% | 53% (40%, 64%) | 93% (86%, 96%) |

## 8. Evaluation Questions for Ask Health
*   **A. Understanding trends:** "Why did my estimated blood pressure range change this month?" "What does 'out of range' mean for my general wellness?"
*   **B. Longitudinal thinking:** "How has my range looked over the last 6 months?" "Is this a temporary spike or a sustained trend?"
*   **C. Lifestyle linkage curiosity:** "How is my sleep affecting my estimated blood pressure?" "If I start walking more, will my trends improve?"

## 9. Appendix
*   **Consumer Interest:** Hypertension is the #1 risk factor for cardiovascular death, and ~60-70% of younger adults (18-44) with uncontrolled hypertension are unaware of it. The "single-reading" bias limits traditional spot checks. Users need continuous, passive insights tied to their lifestyle.
*   **Regulatory Status:** Guided by the FDA General Wellness Policy. Tidal is not intended to diagnose, treat, cure, or prevent any disease, including hypertension. It provides estimates of trends and ranges to encourage positive lifestyle choices and peace of mind. Language strictly avoids "diagnose," "detect," or "medical grade," using terms like "spot," "estimate," "patterns," and "trends."
