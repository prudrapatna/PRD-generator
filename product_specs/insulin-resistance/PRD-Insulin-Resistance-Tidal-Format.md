# Insulin Resistance Levels

**Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — Insulin Resistance Trends**

**October 12th, 2026:** Most people don’t think about their metabolism until it stops working. Insulin resistance—a state where your cells stop responding efficiently to energy—affects over 40% of US adults, yet because it has no obvious symptoms, it remains a "silent" precursor to chronic conditions like type 2 diabetes. For the millions of people in this early window, the opportunity to reverse the trend is high, but the awareness is near zero.

Today, Google introduced **Insulin Resistance Levels**, a new wellness feature for Pixel Watch and Fitbit devices that makes metabolic efficiency visible. By analyzing physiological patterns during sleep and rest, the feature identifies if a user's insulin resistance level is high or low. It’s not a medical diagnosis; it’s a "metabolic fuel gauge" that helps users understand how their daily habits—from late-night snacks to inconsistent sleep—impact their body’s ability to process energy. 

Most months, users won’t hear from it. But when metabolic patterns appear to be consistently high, Google’s Personal Health Agent delivers a calm, personalized message that connects the change to the user’s real life — highlighting how shifts in sleep, activity, or routine may be moving in the same direction, and suggesting small lifestyle changes that may help bring patterns back toward a healthier range. 

“Our mission is to help people live longer, healthier lives by turning everyday devices into tools for earlier awareness,” said Rishi Chandra, Vice President of Google Health. “Metabolic health is one of the most important signals of health, and it’s also one of the easiest to miss. We want to help people understand their patterns earlier and also help them take small steps that add up over time.”

“Looking at metabolic patterns over time can provide valuable insight for both patients and clinicians,” said Dr. Stephen Juraschek. “Tools that help people engage with these trends may support healthier lifestyle decisions before they lead to chronic disease.”

Insulin Resistance Levels is designed to start conversations, not replace care. It does not provide medical readings or replace clinical blood glucose testing. When patterns appear consistently out of range, the feature encourages users to speak with a healthcare professional for proper evaluation.

In a world full of constant alerts, Google is taking a quieter approach: one thoughtful insight a month, delivered only when it matters. For a signal most people never feel, that small moment of awareness could be the first step toward meaningful change.

---

## Overview
Insulin resistance is the #1 risk factor for metabolic decline and it’s reversible, yet ~40% of adults including younger adults (18-44) don’t know when their metabolic efficiency goes out of range. Because it is asymptomatic, users lack urgency to check. 

Recent conjoint and user research (UXR) studies demonstrate high interest and high willingness to pay ($1.15) for metabolic health features, with users placing particular value on insulin resistance insights as an essential early warning indicator.

This document outlines the product requirements for a general wellness feature that provides users with Insulin Resistance Levels (High/Low). By leveraging passively collected wearable data, this feature aims to offer healthy users insights which may keep their metabolic health within range.

---

## Target Product Profile

### Intended Use Statement
The Insulin Resistance Levels feature is a general wellness tool intended to estimate insulin resistance levels to promote positive lifestyle behavior changes in sleep, activity, stress, and nutrition management by educating users and helping them understand how their daily habits correlate with estimated metabolic efficiency. 

The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including pre-diabetes or diabetes.

**Disclaimer:** This product is not intended to monitor glucose levels in real-time or alter any medications.

### Problem Statement
*   **The "Silent" Efficiency Gap:** Metabolism is fundamentally imperceptible. You cannot feel your cells becoming resistant to insulin. Your body gives no warning until the damage (pre-diabetes) is done.
*   **The "Single-Point" Bias:** Users often misinterpret a single high blood sugar reading as an outlier. This feature aggregates data over a calendar month to provide a sustained, credible signal.
*   **Lifestyle Disconnect:** Users struggle to connect abstract lab results to daily choices. We bridge this gap by correlating trends directly with sleep, nutrition, and stress data.

---

## Product Overview
Insulin Resistance Levels provides monthly metabolic insights by analyzing physiological data throughout the day and leveraging advanced AI. Unlike traditional blood tests, Google’s Insulin Resistance uses sensor-derived estimates.

[P0] Monthly notification if it is out of range (High)  
[P0] Supporting evidence by showing the threshold and where they are  
[P0] Month to Month trends  
[P1] Correlation with Lifestyle  
[P1] Weekly overview  

### Product Output
*   **P0:** High or Low (Binary)
*   **P1:** In Range, Moderately Out of Range, Out of Range

### Positioning
A passive, calibration-free general wellness feature that estimates a user's metabolic efficiency range over a full calendar month and delivers a single, context-rich insight — correlating patterns against sleep, stress, and activity — so users understand their metabolic wellness without clinical jargon.

### Product Type
Passive, Opportunistic and Recurring assessment

### Assessment Period
*   **Evaluation Window:** Full Calendar Month.
*   **Data Sufficiency:** Requires a minimum of 7 valid days of data in a calendar month (≥8 hours of wear time/day) with 7 sleep sessions.
*   **Threshold Logic:** Classification as "High" if >50% of valid days exceed the HOMA-IR ≥ 2.9 probability threshold.

---

## Regulated or Wellness?
General Wellness

## Target Segment
*   Pixel watch users on Android
*   Fitbit users starting Radiance on Android and iOS

## Contraindication
*   Prior diagnosis of Hypertension/Diabetes
*   Pregnancy / 6 months post-partum
*   Under age 18

## Product Inputs
*   Weight (Update every 180 days)
*   PPG / Accelerometer / Skin Temperature / HRV

---

## Performance Target
*   **High Insulin Resistance Definition:** HOMA-IR ≥ 2.9
*   **Sensitivity:** >70% at HOMA-IR of >2.9
*   **Specificity:** >75% at HOMA-IR of >2.9
*   **Adjusted Specificity:** 90% at HOMA-IR of >1.5 (Minimizing false positives).

---

## Market Positioning: The Personal Health Assistant

1.  **Metabolic Health on PHA:** Google’s Personal Health Assistant (PHA) is learning to spot — and may help reverse — Insulin Resistance Trends. This feature brings that invisible signal into everyday awareness.
2.  **Significance:** Millions of adults live for years without knowing their metabolism is failing because it is fundamentally imperceptible. Insulin Resistance Levels solves this by providing a sustained, monthly signal.
3.  **A first-of-its-kind agent:** This is the first passive, calibration-free system to identify metabolic efficiency using only wearable sensors. It closes the loop from pattern identification to personalized lifestyle guidance.
4.  **How it works:** Over a full calendar month, AI analyzes pulse timing, heart rate variability, and sleep-state skin temperature to estimate metabolic trends. If "High" patterns appear, you’re notified.
5.  **Rigorous testing:** Developed using WavesFM, a state-of-the-art AI model trained on thousands of users. Validated in 1P studies showing performance exceeding standard pre-diabetes risk assessments.
6.  **AI in Metabolic Trends:** The feature uses a multimodal AI foundation model that interprets the "shape" of the blood pulse and metabolic response patterns beneath the skin.
7.  **Launch markets:** Support for 50+ countries including USA, UK, Canada, Japan, Australia, and EU-20.
8.  **Enhanced peace of mind:** Joins features like Blood Pressure Trends and Sleep Apnea to help users stay safe and informed about their long-term wellness.
9.  **Partners:** Google worked with leading metabolic researchers to ensure the insights are clinically grounded and support healthier lifestyle decisions.

---

## Critical User Journeys (CUJs)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **Silent Onboarding:** I want to consent to all new features and forget about it. | 1. Sees overlay in PHA on new features.<br>2. Reads intended use (wellness tool).<br>3. Confirms weight/height. | Banner render -> Feature tap -> Height field confirm. |
| **Reassuring Glance:** I want to feel informed and calm, not alarmed. | 1. Sees the "Metabolic Health" tile: "Low" for that month.<br>2. Sees visual trend showing "In Range" across most of the month. | Tile render -> Health Tab -> Trend chart view. |
| **Contextual Nudge:** I want to act on the message, not panic. | 1. Receives push notification: "Your metabolic patterns are high. PHA has a note for you."<br>2. Reads insight: "High resistance correlates with your 5-hour sleep average." | Push notification -> Deep link -> PHA insight card. |
| **Informed Share:** I want to arrive at my appointment prepared. | 1. Taps "Prepare for my appointment."<br>2. Reviews 3-month pattern summary.<br>3. Generates PDF summary for sharing. | CTA tap -> Summary scroll -> PDF generation tap. |

---

## Feature Logic Definitions
| Constant | Value | Description |
| :--- | :--- | :--- |
| **MIN_WEAR_HOURS_PER_DAY** | 8 hours | Minimum daily wear for a day to count as "valid" |
| **MIN_VALID_DAYS_FOR_NOTIFICATION**| 7 days | Minimum valid days in the 30-day window |
| **WEIGHT_VALIDITY_DAYS** | 180 days | Weight must be updated within this window |
| **SQI_MIN** | 0.5 | Minimum Signal Quality Index for valid PPG segments |

---

## Evaluation Questions for Ask Health
**A. Understanding “Levels” vs Readings**
*   What does “Insulin Resistance Level” actually mean?
*   Why don’t you just show my blood sugar numbers?
*   What makes my level change?

**B. Longitudinal Thinking**
*   How long does it take to learn my baseline?
*   Will the levels get more accurate over time?
*   Does this compare me to other people?

**C. Lifestyle Linkage**
*   How do sleep and metabolism connect?
*   Why did the notification mention my late-night activity?
*   Can small changes in my diet improve my level?

[... Exhaustive Categories D through J follow same pattern as Tidal Master ...]

---

## Appendix A: Consumer Interest
*   **WTP (July 2025):** Diabetes Risk Assessment is a top performer ($1.15).
*   **PA Engagement:** 79% of Proactive Adopters want a holistic view of metabolic health.
