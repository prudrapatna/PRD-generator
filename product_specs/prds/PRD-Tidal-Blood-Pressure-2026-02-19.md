# PRD: Project Tidal - Passive Blood Pressure Insights (Wellness Approach)

**Date:** February 19, 2026
**Status:** Draft
**Owner:** Staff PM, Google Health

---

## 0. EXECUTIVE SUMMARY
**"What is this and why does it matter?"**

Google Health Guardian introduces Project Tidal: the world’s first passive, cuffless blood pressure (BP) estimation system integrated directly into the daily wearable experience. By leveraging existing optical sensors and advanced proprietary algorithms, we provide users with high-fidelity insights into their heart health patterns without the friction of traditional cuffs or manual data entry. This feature transforms the "silent killer" of elevated blood pressure into a visible, manageable wellness metric, empowering users to make proactive lifestyle choices that slow biological aging.

## 1. INTENDED USE
**"Who is this for and what can it claim?"**

**Target User:** General wellness-conscious individuals (The "Proactive Adopters") who want to track health trends and patterns.
**Intended Use Statement:** This feature is a **general wellness tool** intended for informational and educational purposes only. It provides estimates of blood pressure ranges and patterns based on passive wearable data.
**Regulatory Boundary:** This is NOT a medical device. It is NOT intended to:
- Diagnose, treat, cure, or prevent any medical condition (e.g., Hypertension).
- Replace traditional medical-grade monitoring.
- Provide real-time alerts for acute medical events.
**Disclaimer:** "Values provided are estimates. Consult a healthcare expert for any medical concerns or diagnosis."

## 2. STRATEGY LADDER
**"Why does this matter to our mission?"**

- **Mission:** Democratize health management by making advanced monitoring accessible and anxiety-free.
- **Strategic Alignment:**
    - **Democratization:** Removes the economic barrier ($100+ cuff) and physical barrier (white coat syndrome) to BP tracking.
    - **Passive Insights:** Shifts from episodic "spot checks" to continuous, passive observation.
    - **Retention:** Deepens the value proposition of the Google/Fitbit ecosystem by providing unique, high-value metrics.

## 3. HEALTH IMPACT
**"What changes in users' lives?"**

- **Increased Awareness:** Users become aware of elevated BP patterns that often lack symptoms, encouraging earlier screening by professionals.
- **Behavioral Change:** By visualizing the correlation between sleep, activity, and BP, users are empowered to adopt healthier habits.
- **Biological Age Alignment:** Managing heart health patterns is the #1 lever for maintaining healthspan and slowing the effects of cardiovascular aging.

## 4. PRESS RELEASE (WORKING BACKWARDS)
**"What's the dream experience?"**

### FOR IMMEDIATE RELEASE: The End of the Silent Killer
**Google Health Guardian Unlocks Cuffless Blood Pressure Insights for Everyone**

**MOUNTAIN VIEW, CA** — Today, Google Health announced a breakthrough in cardiovascular wellness: Passive Blood Pressure Insights for the Google Health Guardian ecosystem. For the first time, users can understand their heart health patterns simply by wearing their watch—no cuffs, no squeezing, and no interruptions.

"High blood pressure is known as the silent killer because it often has no symptoms until it's too late," said the Lead Product Manager for Project Tidal. "By making these insights passive and invisible, we're giving people the power to see the invisible and take action before it becomes a crisis."

The feature uses advanced optical sensing to estimate BP ranges while the user sleeps or rests. After a simple 14-day calibration period, users receive weekly "Peace of Mind" reports. If patterns drift, a "Gentle Nudge" provides educational insights into how lifestyle factors like sleep or stress might be impacting their heart.

"This isn't about medicalizing your life; it's about empowering your wellness," added the PM. "It's about having the peace of mind that your heart is in the right range, and the tools to keep it there."

## 5. PROBLEM & OPPORTUNITY
**"Why is the status quo broken?"**

- **The Problem:** 50% of people with elevated blood pressure are unaware of it. Traditional cuffs are bulky, anxiety-inducing, and only provide a "snapshot" in time, often missing nocturnal or stress-induced spikes.
- **The Opportunity:** Wearables are already on millions of wrists. By converting passive PPG data into BP estimates, we can reach an underserved population (Proactive Adopters) who care about wellness but avoid medical-grade hardware.

## 6. VALIDATION RIGOR
**"How do we know this works?"**

- **Algorithm Foundation:** Based on the Tidal Clinical Trial data, using 24-hour Ambulatory Blood Pressure Monitoring (ABPM) as the ground truth.
- **Calibration Protocol:** Requires a 14-day "Quiet Period" of nightly wear to establish a personal baseline.
- **Target Performance:**
    - **90% Sensitivity** in identifying "Out of Range" trends.
    - **85% Specificity** to minimize false alarms and anxiety.
- **Regulatory Check:** All copy has been audited against prohibited terms (e.g., using "Estimate" instead of "Diagnose").

## 7. CRITICAL USER JOURNEYS (CUJs)
**"How do users experience the magic?"**

1.  **Peace of Mind Onboarding:** User wears the watch for 14 days without any setup. On day 15, they receive their first "In Range" report, providing instant relief and trust.
2.  **The Gentle Nudge:** When BP trends drift upward over a 30-day period, the user receives a soft notification correlating the trend with "3 nights of low sleep," prompting a lifestyle adjustment.
3.  **The Doctor Connection:** A user shares their 90-day trend report with their physician during a routine check-up. The doctor uses the data to validate the need for a formal medical screening.

## 8. FUNCTIONAL REQUIREMENTS
**"What exactly must we build?"**

- **FR1: Passive Sensing Engine:** System must capture high-fidelity PPG data during "Resting" and "Sleep" states.
- **FR2: Baseline Calibration:** Logic to establish a personal BP baseline over 14 consecutive nights of wear.
- **FR3: Range Categorization:** Map estimated values to "In Range," "Elevated," or "Out of Range" based on wellness guidelines.
- **FR4: Narrative Insights:** Correlation engine linking BP trends to activity, sleep, and stress data.
- **FR5: Regulatory Guardrails:** Hard-coded disclaimers and terminology checks to ensure no diagnostic claims are made.

---
**Context Note:** This PRD was generated using the following context:
- Company Mission: Accessible BP management.
- User Personas: Proactive Adopters.
- Regulatory: Wellness Focus (No SaMD).
- Performance: ABPM Ground Truth.
