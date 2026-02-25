# Blood Pressure Trends (Project Tidal) - Product Requirements Document

## Executive Summary
**Google’s Personal Health Assistant (PHA)** is evolving to identify "invisible" health signals. **Blood Pressure Trends** is a passive, calibration-free wellness feature for Pixel Watch and Fitbit. It estimates long-term patterns (In Range / Out of Range) without requiring cuffs or manual logging, aiming to promote lifestyle changes in sleep, activity, and stress management.

## 1. Problem Statement: The "Silent Killer"
- **Awareness Gap:** ~50% of adults (including younger demographics 18-44) don't know when their BP is out of range because it is asymptomatic.
- **Single-Reading Bias:** Users often ignore single high cuff readings as "spikes." Tidal aggregates 14 days of data to provide a sustained, credible signal.
- **Lifestyle Disconnect:** Users struggle to connect abstract BP numbers to daily choices. Tidal correlates trends directly with sleep, nutrition, and stress data.

## 2. Target Product Profile (TPP)
- **Intended Use:** A general wellness tool to promote lifestyle behavior changes by correlating daily habits with estimated BP ranges.
- **Classification:** General Wellness (not a medical device; not intended to diagnose or treat hypertension).
- **Target Segment:** Pixel Watch and Fitbit users (Android & iOS).
- **Contraindications:** Prior hypertension diagnosis, pregnancy, under 18, and BP < 90/60.

## 3. Product Positioning & Category
- **New Category:** Personal Health Agent for Cardiovascular Wellness.
- **The Loop:** Pattern Identification → Lifestyle Guidance → Progress Tracking → Healthcare Consultation.
- **Moat:** Passive sensing, gold-standard ABPM validation, and longitudinal intelligence (monthly vs. daily) to avoid "alarm fatigue."

## 4. Feature Logic & Definitions
| Constant | Value | Description |
| :--- | :--- | :--- |
| **Observation Window** | Calendar Month | Analysis period (e.g., Jan, Feb). |
| **Min Wear Time** | 12 hours/day | Required for a day to be "valid." |
| **Data Sufficiency** | 14 valid days | Minimum required within the calendar month for an insight. |
| **Out of Range Threshold** | > 130/80 mmHg | Based on 2020 ISH Global Guidelines and FDA standards. |
| **Notification Cadence** | Monthly | Once per month, delivered only if patterns are consistently out of range. |

## 5. Algorithm & Performance
- **Model:** **WavesFM** (Multimodal Waveform Foundation Model) using PPG and Accelerometer data.
- **Development:** 
    - **Pretraining:** WavesFM foundation built on data from 400,000 individuals.
    - **Fine-Tuning:** Specifically optimized for BP using **millions of hours of wearable data** paired with **clinical gold-standard ABPM** from thousands of users.
- **Validation Standard:** Compared against 24-hour **Ambulatory Blood Pressure Monitoring (ABPM)** as ground truth.
- **Target Performance:** Sensitivity > 37%, Specificity > 84% (Comparable to office BPM status quo).
- **Current Stats (Tidal Preval):** Sensitivity 50.1%, Specificity 93.2%.

## 6. Critical User Journeys (CUJs)
- **CUJ 1: The Invisible Setup:** 2-minute onboarding, single toggle, 14-day silent calibration.
- **CUJ 2: The Reassuring Glance:** Monthly status check (In/Out of Range) with context ribbons for sleep/activity.
- **CUJ 3: The Contextual Nudge:** Push notification for out-of-range patterns. Insights connect BP to lifestyle (e.g., "Your BP is up; your sleep is down 2 hours").
- **CUJ 4: The Informed Share:** Generate a plain-language PDF summary for doctor appointments.

## 7. Product Roadmap & Milestones
- **Algorithm Handoff:** Complete.
- **Waveform AI Integration:** Moving to production pipeline.
- **Next Horizon:** Multi-horizon prediction (e.g., "If I sleep more, my range improves with 80% probability").
- **Future Indicators:** Potential for prediabetes and lipid detection using the same foundation model.
