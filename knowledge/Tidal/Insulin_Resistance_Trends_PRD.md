# Insulin Resistance Trends

**Google's Personal Health Assistant Is Learning to Spot — and May Help Reverse — Insulin Resistance Trends**

**October 12th, 2026:** More than 40% of American adults are living with insulin resistance — quietly, unknowingly, and often for years. Unlike a broken bone or a fever, insulin resistance carries no sensation. Cells gradually lose their ability to respond to insulin, glucose accumulates in the bloodstream, and the body compensates in ways entirely invisible from the outside. Energy metabolism shifts, long-term risk compounds, and yet nothing in everyday life sends a warning. By the time most people receive a clinical diagnosis, the condition has frequently been progressing for a decade.

This week, Google introduced Insulin Resistance Trends, a new wellness feature for Pixel Watch and Fitbit devices designed to bring that invisible metabolic signal into everyday awareness. No needles, no blood draws, no lab appointments — just the device people already wear, working continuously in the background to estimate insulin resistance levels based on patterns in heart rate variability, sleep architecture, physical activity, and physiological signals across an entire month.

Most months, users won't hear from it. But when patterns appear consistently elevated, Google's Personal Health Agent delivers a calm, personalized message — connecting the metabolic signal to the user's real life, highlighting how shifts in sleep, physical activity, body weight, or daily routine may be affecting how their cells respond to insulin, and suggesting small lifestyle changes that may help bring patterns back toward a healthier range.

"Our mission is to help people live longer, healthier lives by giving them earlier awareness of the signals that matter most," said Rishi Chandra, Vice President of Google Health. "Insulin resistance is one of the most widespread and most overlooked metabolic conditions. We believe that by surfacing this signal — quietly, without alarm — we can help people make small changes before they become large problems."

"Insulin resistance often progresses silently for years before it's detected through routine labs," said Dr. Gerald Shulman, Professor of Medicine and Physiology at Yale School of Medicine. "Tools that help people understand their metabolic trends over time, and connect those trends to their daily behaviors, have the potential to meaningfully support healthier choices."

Insulin Resistance Trends is designed to start conversations, not replace care. It does not provide a clinical diagnosis of insulin resistance, prediabetes, or diabetes. When patterns appear consistently out of range, the feature encourages users to discuss their metabolic health with a healthcare professional for proper evaluation and, where appropriate, standard clinical testing.

In a world full of constant alerts, Google is taking a quieter approach: one thoughtful insight a month, delivered only when it matters. For a condition most people never feel until it has become something else entirely, that single moment of awareness could be the first step toward meaningful change.

---

## 2. OVERVIEW

Insulin resistance affects more than 40% of US adults — including a significant proportion of younger adults (18–44) — yet the vast majority have no idea. Because it is asymptomatic and only detectable through lab testing, users lack both urgency and opportunity to check. Unlike blood pressure or heart rate, there is no consumer-facing wearable signal for glucose response; the condition remains entirely hidden beneath the surface of daily life.

Recent conjoint and user research (UXR) studies demonstrate high interest and high willingness to pay for metabolic health features, with users placing particular value on insulin resistance insights and diabetes prevention coaching as critical early warning indicators. In the PHA conjoint study (July 2025), Diabetes Risk Assessment — anchored in insulin resistance detection — was rated among the highest-value features, with users willing to pay $1.15/month for this capability.

This document outlines the product requirements for a general wellness feature that provides users with an Insulin Resistance Level (High or Low). By leveraging passively collected wearable data — including heart rate variability, sleep architecture, activity patterns, and thermal signals — this feature aims to offer healthy users insights into their glucose management and metabolic efficiency, without any behavior change required.

---

## 3. TARGET PRODUCT PROFILE (THE MASTER GRID)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | The Insulin Resistance Trends feature is a general wellness tool intended to estimate insulin resistance level to promote positive lifestyle behavior changes in sleep, activity, stress and nutrition management by educating users and helping them understand how their daily habits correlate with estimated insulin resistance level. |
| **Disclaimer** | This product is not intended to diagnose, mitigate, treat, or cure any disease. This product is not a prescreener for diabetes nor is it intended to monitor glucose levels in real time. Do not use this product for diabetes management or rely on this product to alter any medications or insulin levels. Consult a medical professional for any questions about your metabolic health. |
| **Problem Statement** | **The "Invisible Metabolism" Problem:** Insulin resistance has no perceptible symptoms. Unlike pain or fatigue, users cannot feel their cells becoming less responsive to insulin. **The "Lab-Only" Awareness Gap:** The only standard clinical measure (HOMA-IR) requires a fasting blood draw, leaving most people unaware of their metabolic trajectory between annual checkups. **Lifestyle Disconnect:** Users struggle to connect abstract metabolic concepts to their sleep quality, daily movement, or eating patterns. |
| **Product Overview (P0/P1)** | [P0] Monthly notification if out of range; Supporting evidence via threshold visualization; Month-to-month trends. [P1] Correlation with Lifestyle factors (sleep, activity, weight, stress); 3-tier classification; Weekly metabolic overview. |
| **Product Output (P0/P1)** | P0: High or Low (Binary). P1: Low, Borderline, High. |
| **Positioning (The "North Star")** | Insulin Resistance Trends is a passive, non-invasive general wellness feature that acts as a "metabolic efficiency" gauge — estimating a user's insulin resistance level over a full calendar month and delivering a single, context-rich insight — correlating patterns against sleep, activity, and weight — so users understand their metabolic wellness without anxiety. |
| **Product Type** | Passive, Continuous and Recurring Assessment |
| **Assessment Period** | **Evaluation Window:** A recurring calendar month rolling window. **Data Sufficiency:** Requires a minimum of 7 valid days of data (≥8 hours of wear time/day) with 7 sleep sessions. Weight must be current within the last 180 days. **Threshold Logic:** Classification as "High Insulin Resistance" if greater than half of eligible calendar days within the calendar month have a predicted probability exceeding the HOMA-IR ≥ 2.9 threshold. |
| **Regulated or Wellness?** | General Wellness (USA); General Wellness / Well-being (EU — targeted at healthy individuals only) |
| **Target Segment** | Pixel Watch users on Android; Fitbit users on Android and iOS |
| **Contraindication** | Prior diagnosis of diabetes or prediabetes; Pregnancy; 6 months post-partum; Under age 18 |
| **Product Inputs** | Weight (confirm or manual entry, must be current within 180 days); Heart Rate; Heart Rate Variability (RMSSD, SDNN); RR Intervals (80th/20th Percentile, Median); Step Count; Sleep Sessions; Skin Temperature; Accelerometer |
| **Supported Devices** | Pixel Watch 1–4; Inspire 2–3; Luxe; Sense 1–2; Versa 2–4; Charge 5–6; Fitbit Air |
| **Country Availability** | 50+ countries including USA, UK, Canada, Japan, Australia, New Zealand, EU (20 member countries) |

---

## 4. MARKET POSITIONING: THE PERSONAL HEALTH ASSISTANT (9 THINGS)

| Item | Title | Description |
| :--- | :--- | :--- |
| **1** | **Insulin Resistance Trends on PHA** | Google's Personal Health Assistant (PHA) is learning to spot — and may help reverse — Insulin Resistance Trends. It works quietly in the background to notify you when your monthly metabolic patterns are out of range, guides you toward lifestyle changes, and helps you prepare for meaningful health conversations. |
| **2** | **Insulin Resistance Trend significance** | More than 40% of American adults live with insulin resistance without knowing it, because it is completely asymptomatic and detectable only through lab testing. Insulin Resistance Trends closes the metabolic awareness gap by aggregating wearable signals over a calendar month — making the invisible visible before it becomes prediabetes. |
| **3** | **A first-of-its-kind metabolic assessment** | Represents a significant breakthrough as the first passive, non-invasive wearable system to estimate insulin resistance trends without blood draws or continuous glucose monitors. It closes the loop from metabolic pattern identification to personalized lifestyle guidance. |
| **4** | **How Insulin Resistance Trends on PHA works** | Over a full calendar month, AI analyzes heart rate variability patterns, sleep architecture, activity rhythms, skin temperature, and weight to estimate insulin sensitivity trends. If sustained high-resistance patterns appear, you're notified and connected to actionable lifestyle insights. |
| **5** | **Rigorous testing approach and validation** | Developed and validated in a clinical study of 233+ participants, benchmarked against the gold-standard HOMA-IR (Homeostatic Model Assessment for Insulin Resistance). Performance targets align with or exceed the CDC Prediabetes Risk Test benchmarks for lifestyle change encouragement. |
| **6** | **AI in Insulin Resistance Trends** | Uses a multimodal model trained on millions of hours of wearable data, interpreting combinations of cardiac, sleep, activity, and thermal signals. Fine-tuned to minimize false positives by distinguishing transient lifestyle fluctuations from persistent metabolic patterns. |
| **7** | **Launch markets** | Support for 50+ countries including United States, United Kingdom, 20 EU member countries, Japan, Australia, New Zealand, and Canada. |
| **8** | **Enhanced metabolic peace of mind with PHA** | Joins features like Blood Pressure Trends, irregular heart rhythm notifications, and Sleep Coaching to build a holistic picture of health — helping users stay proactive and feel more confident about their long-term wellbeing. |
| **9** | **Insulin Resistance Trends partners** | Google worked with leading endocrinologists, metabolic researchers, and clinical scientists to ensure the technology is rigorously validated, clinically meaningful, and safely positioned to support healthier lifestyle decisions through proactive metabolic awareness. |

---

## 5. CRITICAL USER JOURNEYS (CUJS)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **The Invisible Setup:** I want to opt in to metabolic tracking in under 2 minutes and not have to think about it again. | 1. User sees an overlay in PHA introducing Insulin Resistance Trends. 2. Reads intended use screen and contraindication checklist. 3. Confirms current weight. | Banner render / Feature card tap → Intended use screen scroll → Contraindication check → Weight field confirm. |
| **The Reassuring Glance:** I want to feel informed about my metabolic health without anxiety or effort. | 1. Opens Google Health Home. 2. Sees "Metabolic Health" tile: "Low Insulin Resistance." 3. Views month-to-month trend showing stable, healthy pattern. | Tile render — glanceable status → Health Tab render → Monthly trend chart display. |
| **The Contextual Nudge:** I want to understand this notification about elevated insulin resistance and feel equipped to act, not alarmed. | 1. Receives monthly push notification. 2. Taps notification to deep-link to detail card. 3. Reads PHA-generated insight connecting metabolic pattern to recent sleep, activity, and weight trends. | Push notification render → Deep link → PHA metabolic insight card render. |
| **The Informed Share:** I want to arrive at my next appointment prepared and confident about my metabolic health. | 1. Taps "Prepare for my appointment." 2. Reviews 3-month insulin resistance pattern summary. 3. Generates shareable PDF summary including lifestyle correlations. | CTA tap → Summary card render → PDF generation tap. |

---

## 6. ALGORITHM PERFORMANCE & VALIDATION REQUIREMENTS

| Metric | Target (low 95% CI) | Rationale |
| :--- | :--- | :--- |
| **Sensitivity** | >70% at HOMA-IR ≥ 2.9 | Comparable to or exceeding the CDC Prediabetes Risk Test (58–81% sensitivity range) for identifying high insulin resistance. |
| **Specificity** | >75% at HOMA-IR ≥ 2.9 | Comparable to CDC Prediabetes Risk Test benchmarks for encouraging lifestyle changes. |
| **Adjusted Specificity** | >90% at HOMA-IR ≥ 1.5 | No more than 10% of insulin-sensitive individuals mis-classified as high resistance. |

### Current Performance

| Study Size | Sensitivity | Specificity | Adj. Specificity |
| :--- | :--- | :--- | :--- |
| **1P Wearable Validation (N=233)** | 73% | 76% | 94% |
| **3P Wearable Validation** | In Progress | In Progress | In Progress |
| **Real World Validation #1** | Nice to Have | — | — |
| **Real World Validation #2** | Nice to Have | — | — |

---

## 7. FEATURE LOGIC & PROGRAM TIMELINE

| Constant | Value | Description |
| :--- | :--- | :--- |
| **MIN_WEAR_HOURS_PER_DAY** | 8 hours | Minimum daily wear for a day to count as "valid" |
| **MIN_VALID_DAYS_FOR_RESULT** | 7 days | Minimum valid days in the rolling calendar month window |
| **MIN_SLEEP_SESSIONS** | 7 sessions | Minimum qualifying sleep sessions in the observation window |
| **OBSERVATION_WINDOW_DAYS** | Calendar Month (Rolling) | Analysis window for insulin resistance estimation |
| **WEIGHT_STALENESS_DAYS** | 180 days | Maximum age of last recorded weight for a valid result |
| **WEIGHT_MISSION_TRIGGER_DAYS** | 165 days | Trigger "Update weight" mission at this staleness threshold |
| **HOMA_IR_CLASSIFICATION_THRESHOLD** | ≥ 2.9 | Predicted probability threshold for "High Insulin Resistance" classification |
| **CLASSIFICATION_MAJORITY_RULE** | >50% of eligible days | Majority of eligible days must exceed threshold to trigger a notification |

### Timeline
*   ✅ Algorithm ready for handoff.

---

## 8. APPENDIX

**Appendix A: Consumer Interest**
In the PHA conjoint study (July 2025), Diabetes Risk Assessment (Insulin Resistance-based) was rated among the highest-value features, with a willingness to pay of $1.15/month (US total sample) — tied with Unusual Trend Detection and Respiratory Illness Insights. For Proactive Adopters specifically, WTP reaches $1.08 (US), $1.16 (Japan), $1.24 (UK), and $1.46 (Germany). A generative UXR study found 9/11 participants recognized insulin resistance as an important yet invisible health issue, and motivation improved significantly when users were shown actionable lifestyle insights alongside their results. CGM adoption interest reaches 56–59% among users who receive insulin resistance awareness.

**Appendix B: US Regulatory (FDA)**
Meets the definition of a general wellness product per FDA Guidance "General Wellness: Policy for Low Risk Devices" (January 2026) because it: is non-invasive and not implanted; does not pose a safety risk; is not intended for diagnosis or treatment; does not guide specific clinical action; and uses non-invasive optical and thermal sensing which is lower risk than existing glucose monitoring examples (microneedles). A 513(g) is not required; internal determination is sufficient.

**Appendix C: EU Regulatory (MDR)**
Targeted at healthy individuals only to maintain the wellness/lifestyle category. Explicitly states the product is not for individuals with metabolic disorders. Does not include: references to screening/managing diabetes or prediabetes; labeling glucose as "abnormal"; prompts to see a medical professional based on specific thresholds; or claims of real-time glucose tracking.
