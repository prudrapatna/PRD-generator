# Health Research Priorities (2026)

**Source Document:** [2026 | Health Research Priorities](https://docs.google.com/presentation/d/16NKnmRMkLCwJ8zVkHr5WRunnzM6sgXMKAMmacENkOco/edit#slide=id.g3a5af1d2114_0_0)

## 1. Mission & Vision
**Mission:** To empower users to live longer, healthier lives by building a proactive, predictive Personal Health Coach that deeply understands user context.
**Vision:** Shift the paradigm by expanding data inputs (3P, PHR, user entered context, geospatial, etc.), accelerating with sensor foundational models (Large Sensor Models - LSM, PPG, SPLAT), and exploring predictive coaching.

## 2. Target Segment: Proactive Adopters
*   **Size:** 17% of global population.
*   **Demographics:** Skews Age 18-44 (many Gen Z), 43% Female / 57% Male. 44% have 1+ chronic conditions. High trust in Google & Fitbit. Over-index in Pixel ownership.
*   **Behavior:** Very active, spend most in health & fitness. 63% own a wearable or intend to purchase within 12 months.
*   **Goals:** Increase strength, physical activity, energy level.
*   By focusing on Proactive Adopters, the product addresses 51% of the general population's needs.

## 3. Key Investment Pillars
1.  **Prioritize investments in areas that augment and drive PHA mission:** longer, healthier lives. Power hyper-personalized and proactive health coaching.
2.  **Develop experiences that are high appeal and drive subscription & hardware sales:** Establish Google Health App as core H&F 1P app.
3.  **Leverage device best suited for capabilities:** Extend health to the entire wearable portfolio.
4.  **Invest in SaMD strategically:** Prioritize high ROI initiatives and Tier 1 regions. Revamp to optimize quality and speed to market.
5.  **Focus on Big Bets:** Prioritize strategic differentiators over incremental improvements.

## 4. Cardiometabolic Health Focus
Cardiometabolic diseases have high prevalence, underdiagnosis, and high impact with lifestyle changes:
*   **Hypertension:** 150M total prevalence. 46% underdiagnosis rate. High lifestyle lever (Nutrition, Activity, Metabolic).
*   **Prediabetes:** 149M total prevalence. 80% underdiagnosis rate. High lifestyle lever.
*   **Type 2 Diabetes:** 93M total prevalence. 30% underdiagnosis rate. High lifestyle lever.
*   **Sleep Apnea:** 95M total prevalence. 85% underdiagnosis rate. High lifestyle lever.

## 5. Areas We Are NOT Investing In
*   **Other Thematic Areas:** Musculoskeletal (including posture), Children/kids.
*   **Lifestyle:** Hydration sensing, Calorie algo update, Sedentary, Fatigue sensing, UWB Contactless Sleep.
*   **Health / SaMD:** Daytime cough, Clinical/SaMD mental health screening, Inflammation screening, SpO2 (wellness continuous/spotcheck), ECG/Afib new algo (burden, etc.), COPD/Asthma screening.
*   **Female Health:** Hot flash detection, Anemia, PCOS screening (sensing).

## 6. The 2026 Roadmap (Holistic PHA Coach & Differentiated Guardian)
### Q2 2026 (GA)
*   **Accurately Track & Assess:** Activity AR (SC1.1 dark mode), Radiance (+ racket sports, golf, cardio, swim, location), Nutrition multi-modal logging.
*   **Guardian (Early Risk / Safety):** Hypertension screening [SaMD], Safety: Breathing Emergency [SaMD].
*   **Coaching:** Sleep score, Add Nutrition (questions, insights).
*   **X-Pillar:** Insights V2, Health Companion (symptoms, appt. prep/follow up), Cycle Health (Coach adaptation, insights, Menopause Lab).

### Q3 2026 (MBG)
*   **Accurately Track & Assess:** Activity AR (Air FM) + new activities, 1P biometric cycle prediction.
*   **Guardian:** [Wellness] Unusual trend detection, [Wellness] Blood Pressure Notification, [Wellness] Insulin Resistance Assessment, [SaMD - EU] Safety: Breathing Emergency, [SaMD - EU] Apnea screening.
*   **Coaching:** Sleep need, Fitness real-time coaching (Audio cues), Nutrition Assessment.
*   **X-Pillar:** Health Snapshot (Health Age, Pace of Aging).

### Q4 2026+
*   **Accurately Track & Assess:** Expand AR, Swim adv metrics, Strength, Vo2max (Walk, run).
*   **Guardian:** [SaMD US Clearance] Hearing Test / Aid, [SaMD - US] Safety: Breathing Emergency, [SaMD - US] Apnea screening.
*   **Coaching:** Add MWB subagent, Circadian rhythm coaching.

## 7. Deep Dives into Key Initiatives
### Foundational Models
*   **SCM (Sensor Compression Model) / SPLAT:** Highly compress signal 32x & stream raw data to cloud. Productized for Activity Recognition (Launch Menary/Seluna Q3 2025, Radiance Q2 2026).
*   **Health Large Sensor Model:** Generative and discriminative tasks (imputation, interpolation, activity recognition) trained on over 100M hours of sensor data.
*   **PPG Foundational Model (TIDAL):** Learns generalized physiological representations from large-scale waveform data. Applicable to BP, pulse wave velocity, hypertension, and stillness detection.

### Guardian Features
*   **Sleep Apnea:** Passively screens for signs of moderate-severe apnea. Target Launch: 2026 MBG (SaMD).
*   **Unusual Trend Detection (UTD):** Monitors shifts in health metrics to detect physiological changes ("signs of strain"). Offers "Rest mode." Target Launch: Q2 2026 (Wellness).
*   **Symptom Checker ("DDx"):** Integrated with AskHealth. Links wearable data and PHR for condition matching.
*   **Breathing Emergency Detection ("Carom"):** Passively tracks rapid oxygen desaturation (e.g., from drug toxicity) and initiates emergency call. Target Launch: Q4 2026 (SaMD).
*   **Hypertension Screening:** Wearable screens for high BP. Target Launch: EOY 2026 / Q1 2027 (SaMD).
*   **Insulin Resistance (Odin):** Notifies user when signs of insulin resistance are detected (passive, repeated every 3 months) with lifestyle coaching. Target: 2027 (SaMD).

### X-Pillar & Metabolic
*   **Health Age / Pace of Aging:** Provides a picture of general health based on metrics from the last 6 months and projects evolution over the next 6 months. Target Launch: Q2 2026.
*   **CGM (3P + 1P) Insights:** Integrates 3P CGM data (Abbott partnership) with sleep, activity, and nutrition for personalized insights on glucose optimization. Target GA: 2027. Note: No internal work on continuous point-in-time glucose sensing from a wearable; focusing on screening and response prediction instead.

### Tracking & Assessment Upgrades
*   **New RetroAR (SPLAT):** Replaces legacy system to auto-recognize 30+ activities, supporting multi-segment workouts and individual exercises (e.g., burpees).
*   **VO2Max Update:** New walking VO2Max and updated running VO2Max models to improve accuracy and deprecate confusing demographic-based scores.
*   **Swimming:** Porting HR and Pythagoras algorithms to deliver a functional swim experience (lap count, duration, HR).
*   **Sleep Algorithms:** Rebuilding the sleep sensing pipeline to improve accuracy and offer new insights into sleep need and circadian coaching.

## 8. User Feature Prioritization (MaxDiff)
*   **Top Features for Proactive Adopters:** Hypertension Trends/Alerts, Personal Health Summary, Fitness Coaching, Performance Coaching.
*   **Regional Differences:** UK and DE prioritize Hypertension and Fitness Coaching. Japan prioritizes Sleep Need & Schedule, Symptom Search, and Category Summaries. Breathing Emergency Alert is #1 among ages 18-34.
