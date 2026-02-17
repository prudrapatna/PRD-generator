# User Research Synthesis: Blood Pressure Feature Concepts

**Date:** February 14, 2026
**Based on:** 14 User Interviews (Concept Testing - Q1 2026)
**Objective:** Synthesis of findings to inform SaMD vs. Wellness strategy for BP monitoring.

---

## 1. Executive Summary
The clear winner for driving actionability and credibility was **Concept 3 (Wellness + Daily Calibration)**, preferred by **50% of participants (7/14)**. This concept succeeded by combining the "personal validation" of cuff calibration with the "granularity" of daily data to explain *why* BP was high.

**Concept 1 (SaMD)** followed with **36% (5/14)**, driven by FDA clearance and "medical tone" for high-risk users. **Concept 2 (Weekly Wellness)** lagged with **14% (2/14)**, failing to provide enough detail to drive urgency.

**Key Insight:** Users trust what they can verify. While FDA clearance is a strong "credential," the ability to **calibrate with a personal cuff** and see **daily trends** was a more powerful driver of day-to-day trust and behavior change.

## 2. Key Themes

### Theme 1: Calibration = Credibility
*   **Insight:** Users trust a device that "checks its work" against a known standard (their home cuff).
*   **Evidence:** 7/14 participants cited **cuff calibration** as a primary credibility driver.
*   **Quote:** "Calibrating with a cuff is a 'genius thing'. It makes me feel like I'm double checking it." (P6)
*   **Implication:** Even for a "Wellness" feature, integrating a hardware calibration step significantly boosts trust over a purely algorithmic "black box" approach (even one with FDA clearance).

### Theme 2: Granularity Drives Action
*   **Insight:** Weekly summaries (Concept 2) are too vague. Daily data (Concept 3) allows users to correlate BP spikes with specific behaviors (poor sleep, salty meal), which drives immediate lifestyle changes.
*   **Evidence:** Participants praised the "day-level view" for offering upfront evidence to support the notification.
*   **Quote:** "The detailed view of the week makes this seem believable... broken down by days highlights that something is wrong." (P4)
*   **Implication:** Aggregated weekly data hides the "cause and effect" relationship users need to modify behavior.

### Theme 3: The Power of "Red"
*   **Insight:** Contrary to earlier assumptions about "soft nudges," users *need* visual alarm (Red/Orange colors) to feel urgency.
*   **Evidence:** Concept 2's "soft headline" failed to drive urgency for many. Concept 3's "repeated red color" worked.
*   **Quote:** "Seeing a lot of red on my screen... adds onto me wanting to take more action." (P4)
*   **Implication:** Use distinct color coding for "Out of Range" states. Do not shy away from red for significant deviations, even in a wellness product.

### Theme 4: The "Estimation" Mental Model
*   **Insight:** Users fundamentally view watch-based BP as an *estimation*, not a diagnosis.
*   **Evidence:** Participants were willing to accept a **5-10 point variance** from their cuff.
*   **Implication:** We can be transparent about "estimated BP" without losing trust, *provided* we show the trend data that backs it up.

## 3. Recommendations

### Must-Have (P0)
1.  **Daily Data Granularity:** Move away from weekly aggregates. Users need daily data points to correlate with lifestyle choices.
2.  **Cuff Calibration Flow:** Implement the 28-day calibration cycle (Concept 3). This is a critical trust builder.
3.  **Urgency-Based Visuals:** Use Red/Orange color coding for out-of-range data. "Soft nudges" are too passive for this use case.
4.  **Contextual Education:** Explain *how* the data is calculated (e.g., "Validated against 20k datasets"). Users are asking for this transparency.

### Should Have (P1)
1.  **Direct HCP Call-to-Action:** Adopt the "Discuss with your Doctor" language from Concept 1, even in the Wellness feature (where regulatory permits).
2.  **Trend Visualization:** Show "Days Out of Range" clearly to highlight persistence, which drives the decision to seek care.

### Validation Strategy
*   **Validate the "Unwilling":** A minority (P10, P11) were unwilling to calibrate. We need to test if a "calibration-free" mode (with lower confidence) is viable for them, or if we accept this friction as a filter for high-intent users.
*   **Test "Estimated" Label:** Ensure the term "Estimated BP" doesn't degrade trust below the threshold of actionability.

## 4. Open Questions
*   **Calibration Compliance:** Will users actually complete a 28-day calibration cycle in the wild? (vs. in a study setting).
*   **Regulatory Line:** Can we use "Red" alerts and "Hypertension" references in a General Wellness product without crossing into SaMD territory?
