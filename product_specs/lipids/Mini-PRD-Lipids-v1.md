# Product Story: Lipid Patterns

## 1. Approval Cover Page
| Approver | Approval Status | Date |
| :--- | :--- | :--- |
| **Product** | | |
| **Engineering** | | |
| **UX/Design** | | |
| **Clinical/Regulatory** | | |
| **Legal/Privacy** | | |

## 2. The Press Release / Narrative
<table style="border: 1.5pt solid black; width: 100%;">
<tr><td>

# Helping your heart thrive: Google introduces Lipid Patterns for the Personal Health Assistant

**March 20, 2026:**
High cholesterol is often called a "silent" condition because it has no symptoms. For millions of people, the only time they think about their lipid levels is during an infrequent doctor's visit involving a fasting blood draw. This creates a massive awareness gap: people are making daily choices about their diet and activity without understanding how those choices affect their cardiovascular health in the long run.

Today, we're introducing Lipid Patterns for the Personal Health Assistant, available across Pixel Watch and Fitbit devices. Using our advanced continuous health monitoring algorithms, this feature operates quietly in the background, analyzing subtle variations in your physiological data to estimate your lipid trends over time. There are no needles, no fasting, and no scheduling required—just wear your device.

When your estimated lipid patterns are out of range for a sustained period, your Personal Health Assistant will provide a calm, contextual notification. Instead of just giving you a number, the Assistant connects this insight directly to your lifestyle—pointing out how recent changes in your sleep, nutrition, or activity levels might be playing a role. 

"Our goal is to help users live longer, healthier lives by giving them early awareness of their cardiovascular health," said Rishi Chandra, VP of Google Health. "By making this information accessible and actionable through the Personal Health Assistant, we're shifting the paradigm from reactive testing to proactive wellness."

"Understanding your lipid profile is a cornerstone of heart health," noted Dr. [Name], Clinical Expert. "A tool that encourages users to connect their daily habits to their internal health can be incredibly powerful in supporting healthier decisions before medical intervention is needed."

Designed to start conversations about health, not replace medical care. In a world of constant alerts, Google is taking a quieter approach: one thoughtful insight a month.

</td></tr>
</table>

## 3. Background & Current Understanding
**The Awareness Gap:**
Dyslipidemia (abnormal lipid levels, commonly high cholesterol) is a major risk factor for atherosclerotic cardiovascular disease (ASCVD). According to the WHO, raised cholesterol is estimated to cause 2.6 million deaths annually. Because it is entirely asymptomatic, users lack the urgency to monitor it. The CDC estimates that nearly 94 million U.S. adults have total cholesterol levels above 200 mg/dL, yet a significant portion remains unaware or untreated.

**Clinical Realities:**
The current standard of care is a lipid panel (blood test), typically requiring a fasting state and a clinic visit. Guidelines generally recommend testing every 4-6 years for healthy young adults, or annually for higher-risk groups. This episodic, high-friction testing creates a "single-reading" bias and massive inertia. Users struggle to connect a single lab result from 3 years ago to their dietary choices today.

**Physiological Mechanisms & AI:**
Research demonstrates that sustained changes in blood lipid concentrations can subtlely affect blood rheology, vascular compliance, and cardiovascular hemodynamics. By applying advanced machine learning models to longitudinal photoplethysmography (PPG) and accelerometer data, we can identify these sustained physiological patterns. 

**User Research (UXR):**
Our primary target, the Proactive Adopter, over-indexes in tracking all aspects of their health and places a high premium on preventative insights. They want technology to enhance their fitness and provide actionable guidance. A passive, background gauge aligns perfectly with their desire to "unlock progress" and "build habits that stick," seamlessly integrating advanced metrics without creating a disjointed, anxiety-inducing medical experience.

## 4. Target Product Profile (The Master Grid)
| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | The Lipid Patterns feature is a general wellness tool intended to estimate lipid trends to promote positive lifestyle behavior changes in nutrition, activity, and sleep management by educating users and helping them understand how their daily habits correlate with estimated lipid trends/levels. This product is not intended to diagnose, mitigate, treat, or cure any disease. This product is not a prescreener for hyperlipidemia nor is it intended to track cholesterol in real time. Do not use this product for disease management or rely on this product to alter any medications. Consult a medical professional for any questions about your cardiovascular health. |
| **Problem Statement** | High cholesterol is asymptomatic and testing involves high-friction blood draws, leaving users disconnected from how their daily habits affect their long-term cardiovascular health. |
| **Product Overview** | A passive, non-invasive feature that analyzes longitudinal sensor data to estimate sustained lipid patterns and provides contextual, lifestyle-linked insights via the Personal Health Assistant. |
| **Feature Prioritization** | P0: Passive data collection, 30-day pattern analysis, basic out-of-range notifications.<br>P1: Integration with Personal Health Assistant for nutrition/activity correlation. |
| **Target User** | Proactive Adopters and health-conscious users seeking to optimize their diet and cardiovascular wellness without frequent clinical testing. |
| **Positioning** | Lipid Patterns is a passive, non-invasive general wellness feature that acts as a metabolic efficiency gauge — estimating a user's lipid trends over a full calendar month and delivering a single, context-rich insight through the Personal Health Assistant — correlating patterns against nutrition and activity — so users understand their cardiovascular wellness without anxiety. |
| **Product Notification** | "Your estimated cholesterol pattern was high over the past month. You should check with your doctor if this is an unexpected result." The notification design will not include features such as colors or sounds that characterize the output as abnormal, pathological, or diagnostic. |
| **Out of Range Threshold** | > 130 mg/dL (Estimated LDL equivalent). Based on the 2018 AHA/ACC/Multisociety Guideline on the Management of Blood Cholesterol, where < 100 mg/dL is optimal and > 130 mg/dL is considered borderline high/high for the general population. |
| **Product Type** | Passive, Longitudinal and Recurring Assessment. |
| **Assessment Period** | 30-day rolling window. Requires minimum 14 valid days of data. |
| **Regulated or Wellness?** | General Wellness (Adheres strictly to FDA General Wellness Policy for Low Risk Devices). |
| **Disclaimer / Contraindication** | Not for users under 22. Not for diagnosing or treating hyperlipidemia. |
| **Algorithm Inputs / Product Inputs** | PPG, Accelerometer, demographic data (age, biological sex). |
| **Supported Devices** | Pixel Watch (Generation 3 and newer) and compatible Fitbit devices. |
| **Country Availability** | US, UK, DE, JP (at launch). |
| **Performance Target** | This is an exploratory research bet. To establish utility as an early-stage wellness signal, performance will be benchmarked against general directional indicators rather than highly accurate clinical tools. Target: Sensitivity > 45%, Specificity > 80%. |
| **Ongoing User Input** | Optional: Meal logging and activity tagging. |

## 5. Market Positioning: The Personal Health Assistant (9 Things)
<table style="border: 1pt solid black; width: 100%; border-collapse: collapse;">
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">1</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Feature on PHA</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Integrated directly into the Personal Health Assistant, Lipid Patterns moves beyond raw data to offer contextual, conversational insights about how your daily choices affect your heart.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">2</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Clinical Significance</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Bridges the critical awareness gap for asymptomatic lipid variations, empowering users to make lifestyle changes before clinical intervention is strictly necessary.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">3</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">First-of-its-kind</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      The first passive, non-invasive wearable feature designed to estimate long-term lipid trends without the need for periodic blood draws or calibration.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">4</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">How it works</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Utilizes advanced machine learning on longitudinal PPG and accelerometer data gathered over a 30-day window to detect sustained physiological changes associated with lipid patterns.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">5</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Rigorous validation</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Developed and validated against thousands of clinical lipid panel results to ensure reliable, trend-based accuracy over time.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">6</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">AI Architecture</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Built on our foundation health models, ensuring privacy-preserving, on-device (or secure cloud) processing of sensitive biometric data.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">7</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Launch markets</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Rolling out initially to the US, UK, Germany, and Japan, aligned with broader Google Health ecosystem expansions.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid black;">
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">8</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Enhanced peace of mind</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Operates quietly. You only hear from it when there is a sustained pattern worth noting, eliminating the daily anxiety of tracking numbers.
    </td>
  </tr>
  <tr>
    <td style="width: 25%; padding: 10px; vertical-align: top;">
      <div style="font-size: 24pt; font-weight: bold; color: #4285F4;">9</div>
      <div style="font-size: 11pt; font-weight: bold; color: #4285F4;">Expert Partners</div>
    </td>
    <td style="padding: 10px; vertical-align: top;">
      Designed in consultation with leading cardiologists and preventive medicine experts to ensure insights are actionable, safe, and scientifically grounded.
    </td>
  </tr>
</table>

## 6. Critical User Journeys (CUJs)
| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **I want to passively track my heart health** | 1. I wear my watch daily. <br> 2. I check my monthly wellness summary. | *Background Sync* <br> *Monthly Summary View* |
| **I want to know if my lifestyle is negatively affecting my body** | 1. I receive an out-of-range notification. <br> 2. I read the lifestyle correlation (e.g., nutrition/activity). | *Push Notification Tap* <br> *Insight Card View* |
| **I want to prepare for my doctor's visit** | 1. I open the Health app. <br> 2. I export my 3-month lipid trend report. | *App Dashboard* <br> *Export PDF Button* |

## 7. Feature Logic Definitions & Algorithm Performance

**Feature Logic**
| Constant | Value | Description |
| :--- | :--- | :--- |
| `MIN_WEAR_HOURS_PER_DAY` | 8 hours | Minimum valid PPG data per 24hr cycle |
| `OBSERVATION_WINDOW_DAYS` | 30 days | Rolling window for trend analysis |
| `MIN_VALID_DAYS_IN_WINDOW` | 14 days | Required valid days within the 30-day window to trigger evaluation |

**Performance Target**
| Metric | Target | Rationale |
| :--- | :--- | :--- |
| **Sensitivity** | > 45% | As an exploratory research bet relying purely on passive PPG and accelerometry, capturing ~half of sustained out-of-range patterns is sufficient to offer directional wellness value without overpromising diagnostic accuracy. |
| **Specificity** | > 80% | High specificity is crucial for an experimental feature to minimize false alarms, ensuring the tool is seen as a helpful nudge rather than an anxiety-inducing alarm. |
| **Adjusted Specificity** | > 90% | (Measured among highly optimal lipid profiles) Ensures we do not misclassify users with clearly healthy habits. |

**Current Performance (Estimated V1)**
| Study Size | Sensitivity | Specificity | Adj. Specificity |
| :--- | :--- | :--- | :--- |
| N = 1,200 | 48% | 83% | 92% |

## 8. Evaluation Questions for Ask Health
**A. Understanding Trends**
*   "What does this 'out of range' lipid pattern mean for me?"
*   "How does this compare to my trends from last month?"

**B. Longitudinal Thinking**
*   "If I start eating more fiber today, how long until my patterns change?"
*   "Have my lipid trends improved since I started running regularly?"

**C. Lifestyle Linkage**
*   "How does my recent poor sleep correlate with my lipid estimates?"
*   "What dietary changes might help improve these patterns based on my recent meals?"

## 9. Appendix
**Consumer Interest (Conjoint Data):**
*   Based on the Pixel Watch Conjoint '24 study (March 2025), "Cholesterol Detection" is a high-value innovation, driving a **+3.7% Share of Preference increase** among Proactive Adopters and a +4.1% increase among current Fitbit owners in the US.
*   It serves as a strong differentiator that appeals to our core segments (Technophiles and Proactive Adopters) who value passive, preventive health insights.

**Regulatory Assessment:**
*   **US (FDA):** Adheres to the General Wellness Policy for Low Risk Devices. It is non-invasive, does not output diagnostic clinical values, and is framed purely around promoting healthy lifestyle choices (nutrition, activity) to manage general wellness.
*   **EU (MDR):** Classified as a lifestyle/wellness feature, not a medical device, provided marketing explicitly avoids disease detection or diagnostic claims.ims.s.