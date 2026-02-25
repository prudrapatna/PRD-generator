# Insulin Resistance Levels: Product Requirements

**Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — Insulin Resistance Trends**

**October 12th, 2026:** Most people don’t think about their metabolism until it stops working. Insulin resistance—a state where your cells stop responding efficiently to energy—affects over 40% of US adults, yet because it has no obvious symptoms, it remains a "silent" precursor to chronic conditions like type 2 diabetes. For the millions of people in this early window, the opportunity to reverse the trend is high, but the awareness is near zero.

Today, Google introduced **Insulin Resistance Levels**, a new wellness feature for Pixel Watch and Fitbit devices that makes metabolic efficiency visible. By analyzing physiological patterns during sleep and rest, the feature identifies if a user's insulin resistance level is high or low. It’s not a medical diagnosis; it’s a "metabolic fuel gauge" that helps users understand how their daily habits—from late-night snacks to inconsistent sleep—impact their body’s ability to process energy. 

When a "High" level is detected, Google’s Personal Health Agent doesn’t just flag the data; it connects the dots. It might highlight how a string of high-stress days and poor sleep sessions are correlating with a dip in metabolic efficiency, and suggest small, actionable changes to help bring those patterns back into a healthier range. "Metabolic health shouldn't be a mystery that only shows up in annual blood work," said Rishi Chandra, VP of Google Health. "We're turning the wearable into a proactive companion that helps you see the invisible shifts in your health before they become permanent."

---

## Overview
Insulin resistance is a highly prevalent (40% of US adults aged 18-44) and reversible state. Recent conjoint and user research (July 2025) demonstrate a high willingness to pay ($1.15) for diabetes risk assessment, with 9/11 participants in UXR identifying it as a critical early warning indicator.

This document outlines the product requirements for a general wellness feature providing **Insulin Resistance Levels (High/Low)**. By leveraging passively collected wearable data, this feature provides healthy users with insights to maintain or improve metabolic efficiency.

---

## Target Product Profile

### Intended Use Statement
The Insulin Resistance Levels feature is a general wellness tool intended to estimate insulin resistance levels to promote positive lifestyle behavior changes in sleep, activity, stress, and nutrition. It helps users understand how daily habits correlate with estimated metabolic efficiency.

The feature is intended to provide notifications when values suggest high resistance to prompt reflection on habits. It is not intended to diagnose, treat, cure, or prevent any disease, including diabetes or pre-diabetes.

**Disclaimer:** This product is not a prescreener for diabetes nor is it intended to monitor glucose levels in real time.

### Problem Statement
*   **The Invisible Efficiency Gap:** Metabolism is fundamentally imperceptible. Users cannot feel their cells becoming "resistant" to insulin until blood sugar levels rise to clinical pre-diabetic ranges.
*   **The Reversibility Window:** Insulin resistance is often reversible through lifestyle changes, but users lack a "feedback loop" to know if their changes are working.
*   **Behavioral Disconnect:** Users struggle to see how a poor night's sleep or high stress directly impacts their glucose management.

---

## Product Overview
Insulin Resistance Levels provides a monthly assessment of metabolic efficiency by analyzing physiological signals during rest and sleep.

*   **[P0] Monthly Level Notification:** Notification if the level is "High."
*   **[P0] Level Status:** Display of "High" or "Low" in the Metabolic Health L2.
*   **[P0] Data Staleness Handling:** Mission to update weight if older than 180 days.
*   **[P1] Correlation Insights:** PHA-driven insights connecting level to sleep/activity.
*   **[P1] CGM/PHR Integration:** Enhanced accuracy if CGM or Health Records are linked.

### Product Output
*   **P0:** High or Low (Binary)
*   **P1:** In Range, Moderately Out of Range, Out of Range (if using advanced data tiers)

### Positioning
A passive "metabolic fuel gauge" that helps users understand their body's energy efficiency and act on it through lifestyle changes without clinical jargon.

### Product Type
Passive, Recurring assessment.

### Assessment Period
*   **Evaluation Window:** Full Calendar Month.
*   **Data Sufficiency:** Minimum 7 valid days (≥8 hours wear time) + 7 sleep sessions. Weight must be <180 days old.
*   **Threshold Logic:** Classification as "High" if >50% of valid days exceed the HOMA-IR ≥ 2.9 probability threshold.

---

## Regulated or Wellness?
General Wellness (USA).

## Supported Devices
*   Pixel Watch 1-4
*   Fitbit (Sense 1-2, Versa 2-4, Charge 5-6, Inspire 2-3, Luxe)

---

## Performance Target
*   **Sensitivity:** >70% at HOMA-IR ≥ 2.9
*   **Specificity:** >75% at HOMA-IR ≥ 2.9
*   **Adjusted Specificity:** 90% at HOMA-IR > 1.5 (Minimizing false positives for sensitive users).

### Current Performance (1P Validation)
*   **N=233:** Sensitivity 73%, Specificity 76%, Adj. Spec 94%.

---

## Market Positioning: The Personal Health Assistant
1.  **Metabolic Insights on PHA:** PHA is learning to spot—and help reverse—Insulin Resistance. This feature brings the invisible signal of metabolic efficiency into everyday awareness.
2.  **The Awareness Gap:** ~50% of adults don't know their metabolic health is declining. This feature provides a sustained, monthly signal to overcome user inertia.
3.  **A Proactive Companion:** It closes the loop from identifying a "High" level to suggesting personalized lifestyle guidance (Sleep, Activity, Nutrition).
4.  **How it Works:** AI analyzes resting heart rate, heart rate variability (HRV), skin temperature, and motion patterns to estimate the body's response to energy.
5.  **Validation:** Tested on 200+ participants with 1P wearable data, showing performance exceeding typical pre-diabetes risk tests.
6.  **Peace of Mind:** Joins Blood Pressure Trends and Sleep Apnea as part of a comprehensive "Early Warning" system.

---

## Critical User Journeys (CUJs)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **Silent Setup:** I want to enable metabolic health tracking effortlessly. | 1. User taps "Metabolic Health" card during onboarding.<br>2. Confirms weight/height.<br>3. Agrees to "General Wellness" disclaimer. | Onboarding screen tap -> Weight confirm -> "Got it" tap. |
| **Calibration:** I want to know when my first result will be ready. | 1. User opens Metabolic Health L2.<br>2. Sees progress: "Collecting data. 5 more sleep sessions needed." | Progress bar display. |
| **Reassuring Glance:** I want to know my status at a glance. | 1. User checks "Metabolic Health" tile in Today tab.<br>2. Sees "Low" status. | Tile render: "Low Insulin Resistance." |
| **Contextual Nudge:** I want to understand why my level is "High." | 1. User receives "High" notification.<br>2. Taps to see PHA insight: "Your metabolic efficiency is lower this month. This often correlates with the 4-hour sleep average I'm seeing." | Push notification -> PHA Insight Card. |
| **Informed Share:** I want to discuss this with my doctor. | 1. User taps "Prepare for appointment."<br>2. Generates PDF summary of monthly levels vs. lifestyle data. | PDF generation -> Share sheet. |

---

## Feature Logic Definitions
| Constant | Value | Description |
| :--- | :--- | :--- |
| **MIN_WEAR_HOURS** | 8 hours | Minimum daily wear to count as a valid day. |
| **MIN_SLEEP_SESSIONS**| 7 sessions | Required sleep data within the window. |
| **WEIGHT_STALE_DAYS** | 180 days | Days before weight is considered invalid for assessment. |
| **HOMA_IR_THRESHOLD** | 2.9 | The clinical probability threshold for "High" classification. |

---

## Evaluation Questions (Ask Health)
### A. Understanding Metabolic Efficiency
*   What does "Insulin Resistance Level" actually mean?
*   How is this different from a glucose reading?
*   Why don't you show my HOMA-IR score?

### B. Longitudinal Thinking
*   How long does it take to learn my baseline?
*   Can I change my level from "High" to "Low" in one month?
*   Does this compare me to others?

### C. Lifestyle Linkage
*   How does sleep impact my insulin resistance?
*   Why does stress matter for my metabolism?
*   Can exercise improve my "Low" score?

### D. Trust & Preparation
*   How accurate is the "High" notification?
*   What should I tell my doctor about this "Level"?
*   Is this a test for diabetes?

---

## Appendix: Consumer Interest
*   **WTP (July 2025):** Users are willing to pay **$1.15/month** for Diabetes Risk Assessment.
*   **PA Value (US):** Proactive Adopters attribute **$1.08** in value specifically to risk detection.
*   **GTM Fit:** 86% fit with PHA core value proposition.
