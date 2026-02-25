# Insulin Resistance Levels: Product Requirements

## Overview
Insulin resistance is highly prevalent (40% of US adults Age 18 - 44 years) and reversible through lifestyle changes. Recent conjoint and UXR studies validate a high willingness to pay for metabolic health features, specifically insulin resistance and diabetes prevention coaching, which users value as critical early warning signs.

This document outlines the product requirements for a general wellness feature that provides users with an Insulin Resistance Level (High or Low). By leveraging passively collected wearable data, this feature aims to offer healthy users insights into their glucose management and metabolic efficiency.

---

## Target Product Profile

### Intended Use Statement
The Insulin Resistance feature is a general wellness tool intended to estimate insulin resistance level to promote positive lifestyle behavior changes in sleep, activity, stress and nutrition management by educating users and helping them understand how their daily habits correlate with estimated insulin resistance level.

**Disclaimer:** This product is not intended to diagnose, mitigate, treat, or cure any disease. This product is not a prescreener for diabetes nor is it intended to monitor glucose levels in real time. Do not use this product for diabetes management or rely on this product to alter any medications or insulin levels. Consult a medical professional for any questions about your metabolic health.

### Product Output
- **Insulin Resistance Level:** High or Low

### Positioning
Acting as a "metabolic efficiency" gauge for the body, it helps users understand how effectively their cells absorb energy (glucose). This feature helps a user understand the impact of their behaviors on metabolic health.

### Product Type
- Passive continuous assessment

### Assessment Period
- **Evaluation Window:** A recurring calendar month rolling window.
- **Data Sufficiency:** Requires a minimum of 7 valid days of data (≥8 hours of wear time/day) with 7 sleep sessions. Weight must be current within the last 180 days.
- **Threshold Logic:** If greater than half of the eligible calendar days within the calendar month have a predicted probability exceeding the HOMA-IR ≥ 2.9, the user is classified as "High Insulin Resistance."

### Regulated or Wellness?
- General Wellness (USA)

### User Experience (MVP)
- Metabolic Health L2
- Monthly Coaching Moment

### User Experience (Launch)
- Pixel Watch users on Android
- Fitbit users on Android and iOS

### Target Segment
- Eligible Pixel Watch: Pixel Watch 1-4
- Eligible Fitbit: Inspire 2-3; Luxe; Sense 1-2; Versa 2-4; Charge 5-6; Fitbit Air

---

## Contraindications
- Prior diagnosis of diabetes or prediabetes
- Pregnancy
- 6 months post-partum
- Under age 18

---

## Performance Target
- **High Insulin Resistance Definition:** HOMA-IR ≥ 2.9
- **Sensitivity:** 70% at HOMA-IR of >2.9
- **Specificity:** 75% at HOMA-IR of >2.9
- **Adjusted Specificity:** 90% at HOMA-IR of >1.5 (No more than 10% of insulin-sensitive individuals mis-classified)

**Rationale:** The CDC Prediabetes Risk Test has a sensitivity of ~58-81% and specificity of ~70-71%. Our targets align with or exceed these benchmarks for encouraging lifestyle changes.

---

## Product Inputs
- **Weight**
- **Wearable Data:** Heart Rate, Heart Rate at Rest, RR Percent Valid, RR 80th Percentile, RR 20th Percentile, RR Median, RMSSD, SDNN, Shannon Ent. RR, Shannon Ent. RR Diffs, Step Count, Jerk Autocorrelation Ratio, Log Energy, Covariance Condition, Log Energy Ratio, Zero Crossing St.Dev, Zero Crossing Avg, Axis Mean, Kurtosis, Sleep Coefficient, Skin Conductance Value, Skin Conductance Slope, Lead Contact Counts, Skin Temperature Value, Skin Temperature Slope, Altitude St.Dev. Norm
- **[Optional]** Continuous Glucose Monitor (CGM)
- **[Optional]** Personal Health Records (PHR): HbA1c, cholesterol, triglycerides

### Ongoing User Input
- Update weight every 180 days
- [Optional] Update CGM every 180 days
- [Optional] Update PHR every 365 days

---

## Algorithm Performance & Validation

| Study Size | Status | Results |
| :--- | :--- | :--- |
| **1P Wearable Validation** | Complete (233 participants) | Sensitivity: 73%, Specificity: 76%, Adj. Spec: 94% |
| **3P Wearable Validation** | In Progress | Data availability being assessed |
| **Real World Validation #1** | Nice to Have | Data from Tidal Pre-Validation (Not available) |
| **Real World Validation #2** | Nice to Have | Data from Abbott CGM Study (Not available) |

---

## Critical User Journeys (CUJs)

| CUJ | Feature Requirement(s) |
| :--- | :--- |
| **Onboarding** | User confirms no prediabetes/diabetes, not pregnant, not 6 months post-partum |
| **Calibration** | Show days remaining until insulin resistance level is unlocked |
| **Level Display** | Initial status in Metabolic Health L2; show data tiers (Wearable, CGM, Health Records) |
| **High IR (Today)** | Surface proactive insights to Coach; include status component |
| **High IR (Health Tab)** | Detailed context in Health Tab |
| **Low IR (Initial)** | Display in L2; no cards in Today/Health Tab |
| **Change to Low** | Surface proactive insights to Coach; detailed context/celebration in Health Tab |
| **Nudges** | Prompt "Improve insulin resistance" goal or CGM use for optimization |
| **Education** | Surface materials in Metabolic Health L2 explaining IR |
| **Data Staleness** | Mission to "Update weight" at 165 days; "Not available" status at 180 days |
| **Data Gaps** | Handle missing wearable/sleep data; downgrade algorithms if CGM/PHR stale |
| **History** | L3 should include monthly history charts |

---

## Strategic Questions
- How to uplevel data completeness tiers within Health Tab?
- How to surface data staleness systematically?
- How to ask about history of disease to unify across Age, IR, and Tidal?
- How to infer/ask about pregnancy?
- Combined reminders for stopped wearable use?
- Persistence of onboarding for users who have results but never onboarded?

---

## Evaluation Questions (Ask Health)
- What is insulin resistance?
- How accurate is the prediction?
- Do I have diabetes / prediabetes?
- How can my food/exercise/weight impact my IR?
- Why do you need annual blood labs?
- How does IR affect my health age or blood pressure?

---

## Appendix: Consumer Interest
- PHA conjoint study (July 2025): High willingness to pay for diabetes risk assessment ($1.15).
- UXR study (July 2025): 9/11 participants recognized IR as an important, yet invisible, health issue.
- Motivation improves with actionable insights and clear sub-metrics.
