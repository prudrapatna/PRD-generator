# Blood Pressure Trends

**Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — Blood Pressure Trends**

**August 16th, 2026:** Millions of adults live for years without knowing how their blood pressure is changing — not because they don’t care, but because nothing in everyday life gives them a reason to check. Blood pressure rarely causes symptoms and doesn’t send reminders, even as sleep, stress, activity, and daily routines quietly shape it over time. These everyday patterns influence overall wellbeing and are closely connected to long-term cardiovascular health, yet for many people the signal remains invisible.

This week, Google introduced Blood Pressure Trends, a new wellness feature for Pixel Watch and Fitbit devices designed to bring that invisible signal into everyday awareness. The idea is deliberately simple: no cuffs, no scheduled readings, no behavior change. Just the device people already wear, working quietly in the background to estimate long-term blood pressure patterns across daily life and sleep.

Most months, users won’t hear from it. But when patterns appear to be consistently high, Google’s Personal Health Agent delivers a calm, personalized message that connects the change to the user’s real life — highlighting how shifts in sleep, activity, or routine may be moving in the same direction, and suggesting small lifestyle changes that may help bring patterns back toward a healthier range.

“Our mission is to help people live longer, healthier lives by turning everyday devices into tools for earlier awareness,” said Rishi Chandra, Vice President of Google Health. “Blood pressure is one of the most important signals of health, and it’s also one of the easiest to miss. We want to help people understand their patterns earlier and also help them take small steps that add up over time.”

“Looking at patterns over time can provide valuable insight for both patients and clinicians,” said Dr. Stephen Juraschek. “Tools that help people engage with these trends may support healthier lifestyle decisions.”

Blood Pressure Trends is designed to start conversations, not replace care. It does not provide medical readings or replace traditional blood pressure cuffs. When patterns appear consistently out of range, the feature encourages users to measure their blood pressure with a clinical grade BP cuff and speak with a healthcare professional for proper evaluation.

In a world full of constant alerts, Google is taking a quieter approach: one thoughtful insight a month, delivered only when it matters. For a signal most people never feel, that small moment of awareness could be the first step toward meaningful change.

---

## 2. OVERVIEW
High Blood Pressure #1 risk factor for cardiovascular death and its reversible, yet ~50% of adults including younger adults (18-44) don’t know when their blood pressure goes out of range. Because it is asymptomatic, users lack urgency to check.

Recent conjoint and user research (UXR) studies demonstrate high interest, high willingness to pay for blood pressure features, with users placing particular value on insulin resistance insights and diabetes prevention coaching as essential early warning indicators.

This document outlines the product requirements for a general wellness feature that provides users with Blood Pressure Trends (In Range/ Out of Range). By leveraging passively collected wearable data, this feature aims to offer healthy users insights which may keep the blood pressure within range.

---

## 3. TARGET PRODUCT PROFILE (THE MASTER GRID)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | The Blood Pressure Trends feature is a general wellness tool intended to estimate blood pressure trends to promote positive lifestyle behavior changes in sleep, activity, stress and nutrition management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range. |
| **Disclaimer** | This product has not been validated for Blood pressure <90/60. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including hypertension. |
| **Problem Statement** | **The "Silent Killer" & Awareness Gap:** Blood pressure is fundamentally imperceptible. Unlike pain or fatigue, you cannot feel your systolic pressure at 145 mmHg versus 120 mmHg. **The "Single-Reading" Bias:** Users often misinterpret a single high reading from a cuff as a "spike". **Lifestyle Disconnect:** Users struggle to connect abstract BP numbers to daily choices. |
| **Product Overview (P0/P1)** | [P0] Monthly notification if out of range; Supporting evidence via threshold visualization; Month to Month trends. [P1] Correlation with Lifestyle; 3 Bins for Classification; Weekly overview. |
| **Product Output (P0/P1)** | P0: In Range or Out of Range (Binary). P1: In Range, Moderately Out of Range, Out of Range. |
| **Positioning (The "North Star")** | Blood Pressure Trends is a passive, calibration-free general wellness feature that estimates a user's blood pressure range over a full calendar month and delivers a single, context-rich insight — correlating patterns against sleep, stress, and activity — so users understand their cardiovascular wellness without anxiety. |
| **Product Type** | Passive, Opportunistic and Recurring assessment |
| **Assessment Period** | **Evaluation Window:** Full Calendar Month. **Data Sufficiency:** Requires a minimum of 14 valid days of data in a calendar month (≥12 hours of wear time/day). **Threshold Logic:** Classification as "out of range" if signs suggestive of out of range are seen in a calendar month. |
| **Regulated or Wellness?** | General Wellness |
| **Target Segment** | Pixel watch users on Android; Fitbit users starting Radiance on Android and iOS |
| **Contraindication** | Prior diagnosis of Hypertension; Pregnancy; Under age 18 |
| **Product Inputs** | Height (confirm or manual entry); PPG; Accelerometer |
| **Supported Devices** | Pixel Watch 3+; Radiance 1+; Charge 7+ (incl moraine) |
| **Country Availability** | 50+ countries including USA, UK Canada, Japan, Australia, New Zealand, EU (20 member countries) |

---

## 4. MARKET POSITIONING: THE PERSONAL HEALTH ASSISTANT (9 THINGS)

| Item | Title | Description |
| :--- | :--- | :--- |
| **1** | **Blood Pressure Trends on PHA** | Google’s Personal Health Assistant (PHA) is learning to spot — and may help reverse — Blood Pressure Trends. It works quietly in the background to notify you when your monthly trends are out of range, guides you towards lifestyle changes, and helps with clinical consultation preparation. |
| **2** | **Blood Pressure Trend significance** | Millions of adults live for years without knowing their blood pressure is going out of range because it is imperceptible though it’s reversible. BP Trends solves this by aggregating data over a calendar month to overcome the awareness gap. |
| **3** | **A first-of-its-kind agent** | Represents a significant breakthrough as the first passive, calibration-free system to achieve performance comparable to professional office measurement. It closes the loop from pattern identification to personalized lifestyle guidance. |
| **4** | **How Blood Pressure Trend on PHA works** | Over a full calendar month, AI analyzes pulse timing, blood-flow patterns, and motion data to estimate blood-pressure trends. If sustained out-of-range patterns appear, you’re notified and connected to lifestyle insights. |
| **5** | **Rigorous testing approach and validation** | Developed using WavesFM, a state of the art AI model trained on hundreds of thousands of users. Tested against Gold Standard 24-hour Ambulatory Blood Pressure Monitoring (ABPM) in studies involving 450+ participants. |
| **6** | **AI in Blood Pressure Trends** | Uses a multimodal foundation model (WavesFM) that interprets pulse "shape" and travel speed. Fine-tuned with millions of hours of wearable data to minimize false positives by distinguishing temporary spikes. |
| **7** | **Launch markets** | Support for 50+ countries including United States, United Kingdom, 20 EU member countries, Japan, Australia, New Zealand, and Canada. |
| **8** | **Enhanced peace of mind with PHA** | Joins features like irregular heart rhythm notifications, Loss of Pulse Detection, and Fall Detection to help users stay safe and connected and feel more confident in their day-to-day well-being. |
| **9** | **Blood Pressure Trends partners** | Google worked with leading cardiologists and clinical researchers to ensure the technology is validated and impactful, helping people support healthier lifestyle decisions through proactive awareness. |

---

## 5. CRITICAL USER JOURNEYS (CUJS)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **The Invisible Setup:** I want to consent to all new health features in under 2 minutes and forget about it. | 1. User sees an overlay in PHA on the new features. 2. Reads intended use screen. 3. Confirms height. | Banner render / Feature card tap -> Intended use screen scroll -> Height field confirm. |
| **The Reassuring Glance:** I want to feel informed and calm, not alarmed. | 1. Opens Google Health Home. 2. Sees "Blood Pressure Wellness" tile: "In range/Out of Range". 3. Sees visual trend showing "In Range". | Tile render — glanceable status -> Health Tab render -> Trend chart display. |
| **The Contextual Nudge:** I want to understand this message and feel equipped to act on it, not panicked. | 1. Receives push notification. 2. Taps notification to deep-link to detail card. 3. Reads PHA-generated insight connecting BP to sleep/activity. | Push notification render -> Deep link -> PHA insight card render. |
| **The Informed Share:** I want to arrive at my appointment prepared and confident. | 1. Taps "Prepare for my appointment". 2. Reviews 3-month pattern summary. 3. Generates PDF summary. | CTA tap -> Summary card render -> PDF generation tap. |

---

## 6. ALGORITHM PERFORMANCE & VALIDATION REQUIREMENTS

| Metric | Target (low 95% CI) | Rationale |
| :--- | :--- | :--- |
| **Sensitivity** | >37% | Comparable to current professional office blood pressure measurement. |
| **Specificity** | >84% | Comparable to status quo for encouraging lifestyle changes. |

### Current Performance
| Study Size | Sensitivity | Specificity |
| :--- | :--- | :--- |
| **Tidal Clinical (N=196)** | 52.6% (40.8, 64.2) | 92.5% (86.2, 96.5) |
| **Tidal Preval (N=259)** | 50.1% (38.4, 63.0) | 93.2% (88.6, 96.3) |

---

## 7. FEATURE LOGIC & PROGRAM TIMELINE

| Constant | Value | Description |
| :--- | :--- | :--- |
| **MIN_WEAR_HOURS_PER_DAY** | 12 hours | Minimum daily wear for a day to count as "valid" |
| **MIN_VALID_DAYS_FOR_NOTIFICATION**| 14 days | Minimum valid days in the 30-day window |
| **OBSERVATION_WINDOW_DAYS** | Calendar Month | Analysis window |
| **MIN_VALID_DAYS_FOR_WEEKLY_INSIGHT**| 7 days | Minimum days for a weekly in-app insight |
| **PPG_SAMPLE_RATE_HZ** | 25 Hz | Required PPG sampling frequency |
| **SQI_MIN** | 0.5 | Minimum Signal Quality Index for valid PPG |

### Timeline
*   ✅ Algorithm ready for handoff.

---

## 8. APPENDIX
**Appendix A: Consumer Interest**
In the PHA conjoint study in July 2025, hypertension was rated as highly important. Users are willing to pay for hypertension features.

**Appendix B: Whoop Country Availability**
(Based on Whoop availability)

**Appendix C: Apple Performance**
(Reference to Apple performance data)
