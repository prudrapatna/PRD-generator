# Insulin Resistance Levels

**Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — Insulin Resistance Trends**

**October 12th, 2026:** Most people don’t think about their metabolism until it stops working. Insulin resistance—a state where your cells stop responding efficiently to energy—affects over 40% of US adults, yet because it has no obvious symptoms, it remains a "silent" precursor to chronic conditions like type 2 diabetes. For the millions of people in this early window, the opportunity to reverse the trend is high, but the awareness is near zero.

This week, Google introduced Insulin Resistance Levels, a new wellness feature for Pixel Watch and Fitbit devices designed to bring that invisible signal into everyday awareness. The idea is deliberately simple: no finger pricks, no fasting tests, no behavior change. Just the device people already wear, working quietly in the background to estimate metabolic efficiency patterns across daily life and sleep.

Most months, users won’t hear from it. But when patterns appear to be consistently high, Google’s Personal Health Agent delivers a calm, personalized message that connects the change to the user’s real life — highlighting how shifts in sleep, activity, or routine may be moving in the same direction, and suggesting small lifestyle changes that may help bring patterns back toward a healthier range.

“Our mission is to help people live longer, healthier lives by turning everyday devices into tools for earlier awareness,” said Rishi Chandra, Vice President of Google Health. “Metabolic health is one of the most important signals of health, and it’s also one of the easiest to miss. We want to help people understand their patterns earlier and also help them take small steps that add up over time.”

“Looking at metabolic patterns over time can provide valuable insight for both patients and clinicians,” said Dr. Stephen Juraschek. “Tools that help people engage with these trends may support healthier lifestyle decisions.”

Insulin Resistance Levels is designed to start conversations, not replace care. It does not provide medical readings or replace traditional blood glucose monitoring. When patterns appear consistently out of range, the feature encourages users to speak with a healthcare professional for proper evaluation.

In a world full of constant alerts, Google is taking a quieter approach: one thoughtful insight a month, delivered only when it matters. For a signal most people never feel, that small moment of awareness could be the first step toward meaningful change.

---

## Overview
Insulin Resistance is the #1 risk factor for metabolic syndrome and its reversible, yet ~40% of adults including younger adults (18-44) don’t know when their metabolic efficiency goes out of range. Because it is asymptomatic, users lack urgency to check.

Recent conjoint and user research (UXR) studies demonstrate high interest, high willingness to pay ($1.15) for insulin resistance features, with users placing particular value on metabolic insights and diabetes prevention coaching as essential early warning indicators.

This document outlines the product requirements for a general wellness feature that provides users with Insulin Resistance Levels (High/ Low). By leveraging passively collected wearable data, this feature aims to offer healthy users insights which may keep the metabolism within range.

---

## Target Product Profile

### Intended Use Statement
The Insulin Resistance Levels feature is a general wellness tool intended to estimate insulin resistance trends to promote positive lifestyle behavior changes in sleep, activity, stress and nutrition management by educating users and helping them understand how their daily habits correlate with estimated metabolic efficiency.

The feature is intended to provide notifications when values suggest a high resistance level to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition, including pre-diabetes or diabetes.

**Disclaimer:** This product is not intended for use by individuals with a prior diagnosis of diabetes.

### Problem Statement
**The "Silent Killer" & Awareness Gap:** Metabolic decline is fundamentally imperceptible. Unlike pain or fatigue, insulin resistance exists in silence. You cannot feel your cells becoming resistant to glucose. Your body gives no warning until the damage is done.

**The "Single-Reading" Bias:** Users often misinterpret a single high glucose reading as an outlier. This feature solves this by aggregating data over a calendar month, providing a sustained, credible signal that overcomes user inertia.

**Lifestyle Disconnect:** Users struggle to connect abstract metabolic numbers to daily choices. This feature bridges this gap by correlating trends directly with sleep, nutrition, and stress data.

---

### Product Overview
Insulin Resistance Levels provides weekly and monthly metabolic insights by analyzing physiological data throughout the day and leveraging advanced AI. Unlike traditional blood tests, Google’s Insulin Resistance uses sensor-derived estimates.

[P0] Monthly notification if it is out of range (High)
[P0] Supporting evidence by showing the threshold and where they are
[P0] Month to Month trends
[P1] Correlation with Lifestyle
[P1] 2 Bins for Classification (High / Low)
[P1] Weekly overview

---

### Product Output
**P0:** High or Low (Binary)
**P1:** High, Moderate, Low (Trinary)

**Note:** This Product does not track glucose levels directly and has not been validated for disease management.

---

### Positioning
Insulin Resistance Levels is a passive, calibration-free general wellness feature that estimates a user's metabolic efficiency over a full calendar month and delivers a single, context-rich insight — correlating patterns against sleep, stress, and activity — so users understand their metabolic wellness and act on it with lifestyle changes without anxiety, clinical jargon, or daily alarms.

---

### Product Type
Passive, Opportunistic and Recurring assessment

---

### Assessment Period
**Evaluation Window:** Full Calendar Month.
**Data Sufficiency:** Requires a minimum of 7 valid days of data in a calendar month (≥8 hours of wear time/day) with 7 sleep sessions.
**Threshold Logic:** If in a calendar month, if we see signs suggestive of high resistance (>50% of valid days), we classify them for "High."

---

### Program Specifications (The Grid)

| Category | Definition |
| :--- | :--- |
| **Regulated or Wellness?** | General Wellness |
| **Target Segment** | Pixel watch users on Android; Fitbit users starting Radiance on Android and iOS |
| **Contraindication** | Prior diagnosis of Diabetes/Pre-diabetes; Pregnancy; 6 months post-partum; Under age 18 |
| **Product Inputs** | Weight (updated <180 days); PPG; Accelerometer; Skin Temperature; HRV |
| **Supported Devices** | Pixel Watch 1-4; Radiance 1+; Charge 7+ (incl moraine) |
| **Country Availability** | 50+ countries including USA, UK Canada, Japan, Australia, New Zealand, EU (20 member countries) |

---

### Performance Target
Insulin Resistance "High" is defined as a HOMA-IR ≥ 2.9 (estimated via wearable sensors).
Validation uses HOMA-IR from clinical blood draws as ground truth.

| Metric | Target (low 95% CI) |
| :--- | :--- |
| **Sensitivity** | >70% at HOMA-IR of >2.9 |
| **Specificity** | >75% at HOMA-IR of >2.9 |
| **Adjusted Specificity** | 90% at HOMA-IR of >1.5 |

**Rationale:** This exceeds the performance of standard CDC Prediabetes Risk Tests for encouraging lifestyle intervention.

---

### Current Performance
| Study | Sensitivity | Specificity |
| :--- | :--- | :--- |
| **1P Wearable Validation** | 73% (61.2, 84.8) | 76% (68.4, 83.6) |
| **HOMA-IR Adjusted** | 75% | 94% (Adj. at 1.5) |

---

### Ongoing User Input
*   Weight logging (mandatory every 180 days)
*   Any change in status (eg: Diabetes diagnosis, medications etc)

---

## Market Positioning: The Personal Health Assistant

**1. Insulin Resistance Levels on PHA**
Google’s Personal Health Assistant (PHA) is learning to spot — and may help reverse — Insulin Resistance Trends. This new wellness feature brings that invisible signal into everyday awareness. It works quietly in the background to notify you when your monthly trends are high, guides you towards meaningful lifestyle changes and helps you with clinical consultation preparation.

**2. Metabolic Trend significance**
Metabolic efficiency is a critical biomarker that impacts wellness and longevity. Millions of adults live for years without knowing their insulin resistance is climbing because it is fundamentally imperceptible. IR Levels solves this by providing a sustained, monthly signal that overcomes the awareness gap.

**3. A first-of-its-kind agent**
This represents a significant breakthrough as the first passive, calibration-free system to identify metabolic health using only wearable sensors. It closes the loop from pattern identification to personalized lifestyle guidance and clinical consultation preparation.

**4. How Insulin Resistance on PHA works**
Over a full calendar month, AI analyzes pulse timing, heart rate variability, and skin temperature to estimate metabolic response. If sustained high patterns appear, you’re notified. Your PHA then connects trends to your lifestyle, suggests adjustments, and creates a shareable summary for your provider.

**5. Rigorous testing approach and validation**
Developed using WavesFM, a state of the art AI model trained on a massive dataset of wearable and clinical data. The algorithm underwent rigorous validation in multiple studies involving over 233 participants and tested against Gold Standard HOMA-IR blood measurements.

**6. AI in Insulin Resistance**
The feature uses a multimodal state of the art AI foundation model that interprets the "shape" of the blood pulse and metabolic response patterns. This AI-based architecture is designed to minimize false positives by distinguishing between temporary shifts and sustained metabolic decline.

**7. Launch markets**
Support for 50+ countries including USA, UK, Canada, Japan, Australia, New Zealand, and 20 EU member countries.

**8. Enhanced peace of mind with the Personal Health Assistant**
Joins features like Blood Pressure Trends and Sleep Apnea to help users stay safe and connected. By providing context on patterns in your overall health and recovery, the Pixel Watch and Fitbit devices help you feel more confident in your day-to-day well-being.

**9. Insulin Resistance partners**
Google worked with leading metabolic researchers and clinical endocrinologists to ensure the technology is validated and impactful, helping people support healthier lifestyle decisions through proactive awareness.

---

## CUJs

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **The Invisible Setup:** I want to consent to all new health features in under 2 minutes. | 1. Sees overlay in PHA on new features.<br>2. Reads what the feature does and doesn't do.<br>3. Confirms weight/height. | Banner render / Feature card tap -> Intended use screen scroll -> Height field confirm. |
| **The Reassuring Glance:** I want to feel informed and calm, not alarmed. | 1. Sees the "Metabolic Health" tile: "Low" for that month.<br>2. Sees visual trend showing "Low" across most of the month. | Tile render — glanceable status -> Health Tab render -> Trend chart display. |
| **The Contextual Nudge:** I want to act on the message, not panic. | 1. Receives push notification: "Your metabolic patterns are high. PHA has a note for you."<br>2. Taps notification to see PHA insight: "High resistance correlates with your 5-hour sleep average." | Push notification render -> Deep link -> PHA insight card render. |
| **The Informed Share:** I want to arrive at my appointment prepared. | 1. Taps "Prepare for my appointment."<br>2. Reviews 3-month pattern summary.<br>3. Generates PDF summary. | CTA tap -> Summary card render -> PDF generation tap. |

---

## Feature Logic Definitions

| Constant | Value | Description |
| :--- | :--- | :--- |
| **MIN_WEAR_HOURS_PER_DAY** | 8 hours | Minimum daily wear for a day to count as "valid" |
| **MIN_VALID_DAYS_FOR_NOTIFICATION**| 7 days | Minimum valid days in the 30-day window |
| **WEIGHT_VALIDITY_DAYS** | 180 days | Days before weight is considered stale |
| **MIN_SLEEP_SESSIONS** | 7 sessions | Minimum sleep sessions required in the window |

---

## [WiP] Evaluation Questions for Ask Health
[... Categorized FAQ sections A through J as per Tidal Standard ...]
