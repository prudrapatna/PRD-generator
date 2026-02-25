# Tidal: Blood Pressure General Wellness — Executive Summary

## 1. The Vision (Press Release)
**Your Wrist Knows. Now Your Phone Empowers You.**
Tidal transforms the Pixel Watch and Fitbit into a passive, longitudinal blood pressure wellness companion. It is a zero-friction, background feature that estimates blood pressure patterns over a 30-day window. 

**What we are solving for:** ~20 million "Proactive Adopters" (adults 18–44) have an untapped opportunity to understand their cardiovascular patterns. Traditional cuffs are active, anxiety-inducing, and capture isolated moments that miss the crucial nocturnal dipping period. Users lack the context to connect their daily habits to their heart health.

**How the Personal Health Agent (PHA) solves this:** We aren't just delivering a notification; we are delivering an *explanation*. When Tidal detects patterns running outside typical wellness ranges, Google's PHA cross-references this data with the user's Sleep, Activity, and Nutrition APIs. Instead of a blunt medical alarm, the PHA delivers an educational narrative: *"Your patterns are running higher this month. I also noticed your sleep averaged 5 hours. These often move together."* Using our World Model, the PHA simulates possibilities, illustrating how shifting lifestyle habits *may* guide them back to a healthier range.

**What it is NOT for:** Tidal is not a medical device. It does not diagnose hypertension, it does not replace a doctor, and it does not provide absolute mmHg readings or on-demand spot checks. It replaces health anxiety with contextual awareness.

---

## 2. Intended Use (Regulatory "North Star")
*"The Blood Pressure General Wellness Notification feature is a general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range. The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition."*

---

## 3. Product Positioning & FDA Frontier
Tidal shifts our wearables from "Activity Trackers" to **"Health Guardians."** We are targeting the Proactive Adopter who is health-curious but lacks the motivation for clinical routines. 

**Pushing the FDA Frontier:** We are operating strictly within the FDA's Jan 2026 General Wellness guidelines (using neutral colors, categorical "In Range / Out of Range" outputs, and "may help" language). However, we are pushing the frontier of *value* by leveraging the PHA. While competitors stop at "Your BP is high," Tidal uses an LLM to dynamically generate personalized lifestyle correlations and multi-horizon simulations. By framing these insights as educational possibilities (e.g., *"Users with similar profiles who improved sleep by 2 hours saw healthier BP ranges"*), we provide unprecedented, AI-driven health coaching without crossing the line into medical prescription or diagnosis.

---

## 4. Critical User Journeys (CUJs) & Key Requirements
The wearable is a passive sensor pipe; the entire experience lives on the mobile app to ensure intentional engagement.

*   **CUJ 1: The Invisible Setup:** User opts in and confirms their height. The watch silently calibrates in the background. 
    *   *Requirement:* Requires ≥ 14 "valid days" (≥ 8 hours of wear/day) within a 30-day rolling window to generate a baseline.
*   **CUJ 2: The Reassuring Glance:** Most months, the user checks the Google Health app and sees a neutral, glanceable tile indicating patterns are "In Range."
    *   *Requirement:* No absolute numbers or red colors are ever displayed.
*   **CUJ 3: The Contextual Nudge & PHA Insight:** If patterns are "Out of Range" for the 30-day window, the user receives a single monthly push notification. 
    *   *Requirement:* The PHA generates a <120-word narrative linking the BP trend to specific, localized lifestyle data (Sleep/Activity) and suggests discussing patterns with a healthcare provider.

---

## 5. Target Performance vs. Current State
Our algorithm (SPLAT) identifies sustained elevated blood pressure patterns by analyzing 15-second PPG and accelerometer segments. Our target is non-inferiority to the clinical standard of care: Office Blood Pressure Measurement (OBPM).

| Metric | Target (OBPM Benchmark)* | Current V1 Algorithm | Status |
| :--- | :--- | :--- | :--- |
| **Sensitivity** | 54% (95% CI: 37–70%) | **53%** (95% CI: 40–64%) | **Matched** |
| **Specificity** | 90% (95% CI: 84–95%) | **93%** (95% CI: 86–96%) | **Exceeding** |

*\*Benchmark based on USPSTF systematic review comparing Office BP to 24-hr ABPM.*

---

## 6. Competitive Analysis: The Ground Truth Advantage
Our primary differentiator against Apple is not just the AI integration; it is the fundamental standard of clinical evidence we are building upon.

| Feature | Tidal (Google) | Apple Notifications | The Google Advantage |
| :--- | :--- | :--- | :--- |
| **Ground Truth Standard** | **24-Hour ABPM** (Ambulatory Blood Pressure Monitoring) | Home BP Cuff (HBPM) | **Massive Clinical Win:** ABPM is the gold standard. It captures nocturnal dipping (sleep BP), which HBPM completely misses. Apple's waking-only model cannot capture true 24/7 cardiovascular health. |
| **Pivotal Study Size** | **N = 1,600** (Multi-site, diverse) | ~N = 800 - 1,000 (Est.) | High-confidence validation across a massive, demographically diverse cohort. |
| **Sensing Method** | **Longitudinal** (30-day window, All-day & Sleep) | Opportunistic (Waking only) | We capture the holistic picture, eliminating the noise of temporary stress spikes. |
| **AI / Lifestyle Integration** | **Yes** (PHA cross-domain synthesis) | No (Binary alerts) | Apple alerts you to a problem. Tidal explains the *why* and models the lifestyle *solution*. |