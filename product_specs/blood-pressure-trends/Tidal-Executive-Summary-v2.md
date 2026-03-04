# Blood Pressure Trends

## Google's Personal Health Assistant Is Learning to Spot — and May Help Reverse — Blood Pressure Trends

---

> **FOR IMMEDIATE RELEASE**
>
> **August 16th, 2026:** Most people don't think about their blood pressure until something goes wrong. High blood pressure affects nearly half of all American adults — but among those with uncontrolled levels, roughly 70% of adults aged 18–44 are completely unaware. There are no symptoms. No alarm. No warning. Blood pressure runs silently elevated for years, quietly accelerating risk for heart attack, stroke, and kidney disease — long before a diagnosis. For the estimated 20 million younger adults in this window, the opportunity to intervene is high. The awareness is near zero.
>
> Today, Google introduced **Blood Pressure Trends**, a new wellness feature for Pixel Watch and Fitbit devices that makes cardiovascular patterns visible without requiring any behavior change. By passively analyzing physiological waveforms during everyday wear, the feature estimates whether a user's blood pressure patterns are running within or outside of typical wellness ranges across a full calendar month. It's not a medical diagnosis — it's a passive health compass that helps users understand how their daily habits connect to their cardiovascular health.
>
> Most months, users won't hear from it. The silence is itself a signal: peace of mind. But when patterns appear to be consistently outside typical ranges, Google's Personal Health Agent delivers a calm, personalized message — connecting what it observed in blood pressure patterns to what it knows about the user's sleep, activity, and stress — and suggesting one clear next step. One thoughtful insight a month, delivered only when it matters.
>
> *"Our mission is to help people live longer, healthier lives by turning everyday devices into tools for earlier awareness,"* said Rishi Chandra, Vice President of Google Health. *"Blood pressure is one of the most important signals of cardiovascular health, and it's also one of the easiest to miss. Tidal gives people a passive, trustworthy signal they can act on — before a crisis."*
>
> *"Longitudinal blood pressure monitoring provides clinically meaningful information about sustained cardiovascular risk that single-point readings simply cannot capture,"* said Dr. Stephen Juraschek, hypertension researcher. *"Tools that help people understand their patterns over time may support healthier decisions well before those patterns become a clinical problem."*
>
> Blood Pressure Trends is designed to start conversations, not replace care. It does not provide blood pressure readings or replace clinical diagnosis. When patterns appear consistently out of range, the feature encourages users to speak with a healthcare professional for proper evaluation. In a world full of constant alerts, Google is taking a quieter approach: one thoughtful insight a month, delivered only when it matters.

---

## Overview

High blood pressure is the leading modifiable risk factor for cardiovascular disease and the leading cause of preventable death globally — yet it remains profoundly invisible. Among the 60 million Americans with uncontrolled elevated blood pressure, nearly half don't know. For adults aged 18–44, the awareness gap is even starker: approximately 70% (~20 million) are unaware their patterns are elevated. Because hypertension is entirely asymptomatic, there is no signal that prompts action. Users don't feel it. They don't check. And traditional screening requires hardware, appointments, and active effort most younger adults simply won't sustain. Recent conjoint and UXR studies confirm strong willingness-to-pay ($0.90+) for hypertension awareness features, with this demographic placing particular value on passive, background health insights.

Blood Pressure Trends solves the awareness problem without adding friction. Using the wrist-worn sensors already present in Pixel Watch and Fitbit devices, the feature passively captures PPG and accelerometer data across a full calendar month and applies a Waveform Foundation Model to estimate whether blood pressure patterns are running within or outside of typical wellness ranges. No cuff. No calibration. No scheduled readings. The feature aggregates 14+ days of longitudinal wear data to distinguish sustained patterns from temporary spikes — the kind of signal that single-point office readings routinely miss. When patterns are in range, the user sees peace of mind. When they're not, the Personal Health Agent delivers one contextual, lifestyle-linked insight.

Why Google, why now: the wearable device is already there, already sensing, already trusted. What has been missing is a feature that closes the loop between passive sensing and meaningful cardiovascular awareness. Blood Pressure Trends is the keystone of Google Health's 2026 sensing portfolio — directly advancing OKR O3/KR8 (sensing innovations equivalency across all devices) and making the Personal Health Agent the only AI health companion in the market capable of connecting blood pressure patterns to sleep, activity, and stress in a single integrated insight.

---

## Target Product Profile

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | The Blood Pressure General Wellness Notification feature is a general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range. The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including hypertension. |
| **Disclaimer** | This product is not intended to measure clinical blood pressure values or replace ambulatory blood pressure monitoring. |
| **Problem Statement** | (1) **Awareness Gap:** ~70% of adults aged 18–44 with uncontrolled blood pressure patterns are unaware due to zero symptoms. (2) **Single-Reading Bias:** Users dismiss isolated cuff spikes as outliers — Tidal aggregates 14+ days to produce a credible, sustained signal. (3) **Lifestyle Disconnect:** Users cannot connect abstract BP numbers to daily habits — Tidal bridges this by correlating patterns with sleep, activity, and stress via the PHA. |
| **Product Overview** | **[P0]** Monthly notification when patterns are Out of Range. **[P0]** Trend visualization showing In Range / Out of Range across the 30-day window. **[P0]** PHA-generated insight linking patterns to sleep and activity data. **[P1]** Weekly in-app insight card (non-push) after 7+ valid days. **[P1]** Multi-horizon lifestyle simulation ("If sleep improves, patterns may shift"). |
| **Product Output** | **[P0]** In Range / Out of Range (binary). **[P1]** In Range / Borderline / Out of Range (3-bin). |
| **Positioning (The "North Star")** | A passive, calibration-free general wellness feature that estimates a user's blood pressure range across a full calendar month and delivers a single, context-rich insight — correlating patterns against sleep, stress, and activity — so users understand their cardiovascular wellness without clinical jargon. |
| **Product Type** | Passive, opportunistic, and recurring assessment. |
| **Assessment Period** | **Evaluation Window:** Rolling 30-day calendar month. **Data Sufficiency:** Minimum 14 valid days (≥8 hours wear/day) in the 30-day window. **Threshold Logic:** Out-of-Range classification if predicted probability exceeds 0.5699 (Systolic ≥130 mmHg / Diastolic ≥80 mmHg, per ISH 2020 Global Guidelines). |
| **Regulated or Wellness?** | General Wellness (Non-Device) — 21st Century Cures Act §520(o)(1)(B); FDA General Wellness Guidance (updated Jan 6, 2026). |
| **Target Segment** | Proactive Adopters aged 18–44 on Pixel Watch and Fitbit (Android-first; iOS post-GA). Premium subscription required. |
| **Contraindication** | Prior hypertension diagnosis; pregnancy or 6 months post-partum; age under 18; resting BP < 90/60 mmHg. |
| **Product Inputs** | Height (required at onboarding; re-validated every 180 days); Green PPG (528nm, 25Hz); Tri-axial Accelerometer (25Hz). |
| **Supported Devices** | Pixel Watch 5 (Goteria); Fitbit Radiance ("Fitbit Air"); Fitbit Mukai ("Fitbit Edge"). |
| **Country Availability** | GA: USA, UK, Canada, Japan, Australia, EU-20 (50+ countries). Post-GA: additional APAC and LATAM expansion. |

---

## Market Positioning: The Personal Health Assistant

| | |
| :--- | :--- |
| **1**<br>**Blood Pressure Trends on PHA** | Google's Personal Health Assistant is learning to spot — and may help reverse — blood pressure trends. Blood Pressure Trends brings the single most important invisible cardiovascular signal into everyday awareness for the first time, embedded directly in the device users already wear. |
| **2**<br>**Significance** | Elevated blood pressure patterns affect nearly 50% of American adults — but among adults aged 18–44, approximately 70% with uncontrolled patterns (~20 million people) are entirely unaware. Because high blood pressure is asymptomatic, no feedback loop exists to prompt action. Tidal creates that loop. |
| **3**<br>**A First-of-its-Kind Passive Agent** | Blood Pressure Trends is the first calibration-free, passive blood pressure wellness feature validated against 24-hour Ambulatory Blood Pressure Monitoring (ABPM) — the clinical gold standard. Apple validates against home BP monitors taken during waking hours. Only Tidal captures nocturnal patterns during sleep, where BP dipping (or its absence) is most clinically meaningful. |
| **4**<br>**How Blood Pressure Trends on PHA Works** | Over a full calendar month, AI analyzes the shape of the user's pulse waveform (PPG) and motion signals to estimate blood pressure trends. The Waveform Foundation Model produces a 256-dimensional physiological embedding for each valid measurement window. After 14 valid wear days, the system classifies the user's pattern as In Range or Out of Range. If Out of Range, the Personal Health Agent is invoked to generate a single, contextual monthly insight. |
| **5**<br>**Rigorous Testing & Validation** | The V1 algorithm (SPLAT) achieves Sensitivity 53% (95% CI: 40%–64%) and Specificity 93% (95% CI: 86%–96%) against 24-hr ABPM ground truth — meeting or exceeding the USPSTF benchmark for office blood pressure measurement (Sens. 54%, Spec. 90%). Pivotal validation study targets N=1,600 participants across diverse age, sex, race, BMI, and skin tone cohorts. |
| **6**<br>**AI in Blood Pressure Trends** | The feature uses WavesFM, a multimodal Waveform Foundation Model (EfficientNet B1, ~5.1M parameters) pretrained on ~500,000 hours of consented wrist sensor data. The model learns to recognize vascular stiffness signatures in PPG morphology — the b-d area, b/a ratio, and maximum systolic slope — without requiring explicit BP labels during pretraining. Two models handle different wear patterns: All-day (users who sleep with their device) and Awake (daytime-only wearers). |
| **7**<br>**Launch Markets** | Available at GA in 50+ countries including USA, UK, Canada, Japan, Australia, and EU-20. Regulatory framing: General Wellness (Non-Device) in all markets. Post-GA expansion to additional APAC and LATAM geographies, aligned with broader Google Health international rollout. |
| **8**<br>**Enhanced Peace of Mind with PHA** | Blood Pressure Trends joins Sleep Apnea Detection and Breathing Emergency Detection as part of Google Health's 2026 sensing innovations portfolio — making Google the only wearable ecosystem that passively monitors cardiovascular, respiratory, and metabolic signals and integrates them into a single, unified Personal Health Agent. Together, they transform the wrist-worn device from a fitness tracker into a proactive health guardian. |
| **9**<br>**Blood Pressure Trends Partners** | Google worked with leading cardiovascular researchers and hypertension specialists to ensure insights are clinically grounded. Validation conducted against FDA-aligned ABPM gold standard across 44 US states in IRB-approved free-living studies. Expert panel includes hypertension researchers and cardiologists engaged for credibility review and planned peer-reviewed publication of results. |

---

## Summary: What's Next

- **Pivotal Validation Study (N=1,600):** Final study size to be confirmed after Tidal Preval prevalence analysis (end of Feb 2026). Diverse representation across age (18–75), sex, race/ethnicity, BMI, and Monk Skin Tone scale is required before GA approval.
- **3-Bin Classification (P1):** Second performance checkpoint (3/4) will evaluate In Range / Borderline / Out of Range output. Unlocks a more nuanced user-facing experience — resolves the current binary notification into a gradient that reduces both false alarm anxiety and false reassurance.
- **PHA Insight Engine Compliance Filter:** LLM-generated notifications must pass automated prohibited-term filtering before delivery. Fallback message protocol needs sign-off from Legal before GA.
- **iOS Support:** Android-first at GA. iOS post-GA requires separate Health Connect integration planning — dependency on iOS Health Connect API availability.
- **OKR Alignment Checkpoint:** Blood Pressure Trends is a named deliverable under O3/KR8. Equivalency across Radiance, Mukai, and Pixel Watch 5 required by H2 2026 hardware launch dates (Radiance Q1, Mukai/Goteria Q3).
