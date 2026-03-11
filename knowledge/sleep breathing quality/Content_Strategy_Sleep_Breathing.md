# Content Strategy: Breathing Quality

This strategy outlines the approach to communicating the user's nightly Breathing Quality metric within the Sleep tab, aiming for clarity, relevance, and a supportive tone, while appropriately positioning its relationship to the formal Sleep Apnea Assessment feature. 

The language will adopt a coach-like tone, focusing on the user's data and experience ("your breathing," "your patterns").

## 1. What is Breathing quality?

*   **User-facing definition:** Breathing Quality is a metric that measures the regularity and smoothness of your breathing patterns throughout the night.
*   **How it's measured (Simplified):** Your device tracks tiny variations in your breathing patterns while you sleep, assessing how consistent and relaxed they are.
*   **Why it matters:** Regular, relaxed breathing during sleep is important for restorative sleep and overall health. Significant irregularities or "strained" breathing patterns can sometimes be a signal for underlying conditions that affect sleep, such as irregular sleep breathing (like sleep apnea).

## 2. Approach to the card content (Title & Body)

**Overall goal:** To provide a concise, understandable, and contextually relevant summary of your nightly breathing quality, presented in a conversational and non-alarming tone — similar to the Vitals card that Dominique designed!

**Alignment with Vitals Card:**
*   **Conversational title:** Use an interpretive, observation-based title that feels like a personalized insight from your data.
*   **Descriptive body copy:** The body should explain what your observed breathing quality means for this specific night and briefly touch upon potential implications or contributing factors, referencing the underlying health context (sleep apnea) cautiously.
*   **Tone:** Adopt the friendly, supportive, and informative tone of a personal health coach.

**Content components:**
*   **Title:** A concise, conversational headline that captures the essence of your night's breathing quality. There are 3 scenarios that we have sketched out for this 
*   **Body text:**
    *   Explain your observed result for the night (Examples: "Your breathing was mostly smooth and relaxed," "Your breathing patterns showed some signs of strained breathing").
    *   Briefly suggest what this might mean or be related to. For non-ideal scenarios, connect it cautiously to the general concept that breathing irregularities can impact sleep quality and can sometimes be associated with conditions like irregular sleep breathing/sleep apnea.
    *   Avoid providing specific, actionable recommendations solely based on this card's data.
*   **Visual:** Retain the graph visualization as shown in the current card — the one that Taalib has designed 
*   **"About Breathing Quality" section:** Keep the static, factual explanation of how the metric is measured as a reference point.
*   **No forward-facing suggestions on this card:** Explicitly exclude calls to action or advice (like "Try breathing exercises," "Adjust sleep position," or "See a doctor") from the main body text of this card — something for us to include in the prompt

**Handling apnea risk:**
*   This card should not deliver the formal "Signs of potential sleep apnea detected" result from the Sleep Apnea Assessment feature. That is a separate, regulated process! 
*   This card can mention that breathing irregularities (what this metric measures) are sometimes associated with conditions like irregular sleep breathing/sleep apnea, particularly in the non-ideal scenarios. This serves as education and context without being a personal warning from this metric alone.
*   Formal warnings or calls to action related to potential sleep apnea risk (based on the assessment feature's results) will appear on a separate "stream" card on the Today tab — this is potentially an area for an occasional insight 

## 3. Tone of voice

Consistent with Sleep Need, Vitals, and overall health features, specifically adopting a personal coaching approach:
*   **Personalized:** Frame observations around "your" data and body.
*   **Friendly & Supportive:** Acknowledge your effort in tracking your health.
*   **Informative:** Clearly explain your data and its potential meaning using plain English.
*   **Non-judgmental:** Present your data factually without implying blame or failure.
*   **Empathetic:** Acknowledge your potential concerns (e.g., related to fatigue) when discussing breathing irregularities.
*   **Cautious (for non-ideal scenarios):** Use careful language when linking breathing irregularities to potential underlying conditions, emphasizing "can be," "sometimes associated with," etc., to avoid alarming you unnecessarily from a single night's data point.

---

## 4. Scenarios & Content Golden Examples (Revised)

### (A) Scenario: Healthy Range (None Elevated)
*   **Implicit Level:** Healthy / Optimal (0% elevated)
*   **Prompt Data would include:** Result indicates breathing within optimal range, Percentage of night elevated = 0%.
*   **Content Draft:**
    *   **Title:** Your breathing quality was in range last night
    *   **Body:** Your breathing patterns were smooth and relaxed throughout the night, staying in your healthy range. Consistent breathing quality supports more restful and restorative sleep.

### (B) Scenario: Mildly Strained (Mild Elevation)
*   **Implicit Level:** Mild Irregularity (e.g., 1-X% elevated - percentage threshold TBD clinically)
*   **Prompt Data would include:** Result indicates mild signs of strained breathing, Percentage of night elevated is mild (e.g., Y%), Note that it might impact how refreshed they feel.
*   **Content Draft:**
    *   **Title:** Signs of strained breathing detected
    *   **Body:** Last night, your breathing showed mild signs of strain. It wasn't as consistently smooth or relaxed as it could be, which might impact how refreshed you feel when you wake up. Occasional variations are normal, and can sometimes relate to factors like temporary nasal congestion or sleep position. Keeping an eye on this metric over time is helpful.

### (C) Scenario: Moderately Strained (Moderate Elevation)
*   **Implicit Level:** Moderate Irregularity (e.g., X-Y% elevated - percentage threshold TBD clinically)
*   **Prompt Data would include:** Result indicates strained breathing detected, Percentage of night elevated is moderate (e.g., Z%), Note that it might impact how refreshed they feel.
*   **Content Draft:**
    *   **Title:** Moderately strained breathing detected
    *   **Body:** Your breathing patterns were moderately strained for a portion of the night. This level of irregularity can disrupt sleep quality and might explain why you don't feel fully refreshed. Moderate strain can be associated with various factors, including nasal congestion, sleep position, or perhaps lifestyle factors like alcohol use before bed. Persistent irregularities during sleep can sometimes be associated with irregular sleep breathing.

### (D) Scenario: Severely Strained (Severe Elevation)
*   **Implicit Level:** Significant Irregularity (e.g., >Y% elevated - percentage threshold TBD clinically)
*   **Prompt Data would include:** Result indicates severely strained breathing detected, Percentage of night elevated is severe (e.g., >Z%), Note that it might impact how refreshed they feel. This is potentially an area for an occasional insight card on Today linked here.
*   **Content Draft:**
    *   **Title:** Severely strained breathing detected last night
    *   **Body:** Severely strained breathing patterns were detected for a significant portion of your sleep last night. This level of irregularity can disrupt sleep quality and might explain why you don't feel fully refreshed. Significant and persistent strain can be linked to a variety of factors, including nasal congestion, sleep position, changes in altitude, certain medications, or underlying sleep-disordered breathing. Keeping an eye on this is important for your sleep health.

---

## Update Jul 10, 2025

Based on Logan’s comments

**A focus on a binary categorization (based on the BQM cutoff):**
*   This suggests a similar intent between the unregulated and SaMD experiences
*   **Potential mitigation:** since the SaMD is only differentiating between none-to-mild OSA (AHI < 15) and moderate-to-severe OSA (AHI ≥ 15), we could deliberately interpret the BQM differently for this product experience, aligning it with the OSA severity classification system (events/hr of sleep) as that’s a more natural analogy to the time-series representation anyhow:
    *   Establish cutoffs of percent of the sleep period with BQM >0.25 to identify 4 categories instead of 2:
        *   “No” OSA: AHI < 5
        *   Mild OSA: 5 ≤ AHI < 15
        *   Moderate OSA: 15 ≤ AHI < 30
        *   Severe OSA: 30 ≤ AHI
    *   Talk in “positive”/healthiness-focused terms and avoid clinical descriptors (ie, “mild”, “moderate”, “severe”) and focus on the “amount of the sleep impacted”:
        *   **Positive focus:**
            *   No OSA: “almost all” of sleep with good breathing quality
            *   Mild: “most” of sleep with good breathing quality
            *   Moderate: “some” sleep with good breathing quality
            *   Severe: “limited amount” of sleep with good breathing quality
        *   **Negative focus:**
            *   No OSA: “negligible”/”minimal” amount of sleep with strained breathing
            *   Mild: “some”/”limited amount of” sleep with strained breathing
            *   Moderate: “modest” amount of sleep with strained breathing
            *   Severe: “substantial”/”significant” amount of sleep with strained breathing

**The Why for percentage and 4 categories:** This document provides the strong regulatory justification for why we must use "percentage of the night with BQM > 0.25" and create 4 categories based on that percentage. 
It's a deliberate choice to differentiate the unregulated BQM summary from the SaMD's core logic (which uses the average BQM and a binary outcome for its primary function). 
Using percentage of time is a different aggregation method, and having 4 categories is a different categorization scheme than the SaMD's binary assessment (mod-severe vs. not). This distinction is key to mitigating regulatory risk.

**Explicit avoidance of clinical terms for categories:** The document strongly suggests aligning conceptually with OSA severity levels (None, Mild, Moderate, Severe) but explicitly recommends avoiding using these clinical descriptors ("mild", "moderate", "severe") directly in the user-facing category names or primary descriptions for the non-regulated BQM feature. 
This is crucial to prevent the perception that the BQM metric itself is providing a clinical diagnosis or severity assessment.

**Framing based on "Amount of Sleep Impacted":** The document proposes focusing language on the "amount of the sleep impacted" or the "amount of time" with good/strained breathing quality. 
This is a safer way to describe the categories based on percentage than using severity terms.

**How this impacts the "Scenarios & content examples":**
Our previous revision correctly adopted the 4 categories and the percentage-of-night concept based on the specialist feedback. However, this new document clarifies that we need to be even more careful with the naming and framing of these categories and the body text, specifically avoiding the clinical terms "mild," "moderate," "severe" as descriptors for the BQM results themselves.
We should lean into the language suggested: focus on the amount or percentage of time with the detected pattern.
Let's refine the "Scenarios & content examples" again, incorporating the "amount of sleep impacted" framing and explicitly avoiding the clinical severity terms in the category titles/descriptions:

### Revised scenarios & content examples (Integrating SaMD Risk Mitigation):

| Scenario / Category | Implicit Level (Based on % time) | Title content | Body content |
| :--- | :--- | :--- | :--- |
| **Optimal breathing quality (Minimal irregularity detected) 🟢** | **User-Facing Concept:** Almost all of the night with smooth, relaxed breathing patterns.<br><br>**Implicit Level:** Very low percentage of night with elevated BQM (e.g., 0-X%) | Your breathing quality was optimal last night | Your breathing patterns were smooth and relaxed throughout almost all of the night, staying in your optimal range. Consistent breathing quality supports more restful and restorative sleep. |
| **Periods of sleep with strained breathing last night 🟡** | **User-Facing Concept:** Some limited periods of strained breathing patterns.<br><br>**Implicit Level:** Small percentage of the night with elevated BQM (e.g., X-Y%) | Limited breathing irregularities detected | Last night, your breathing patterns showed limited irregularities, meaning they weren't consistently smooth or relaxed for short periods. <br><br>Limited variations like these are common and can sometimes influence how refreshed you feel. They may be related to factors such as temporary congestion, sleep position, or how deeply you were sleeping. Keeping an eye on this over time is helpful. |
| **Some strained breathing last night 🟠** | **User-Facing Concept:** A noticeable portion of the night with strained breathing patterns.<br><br>**Implicit Level:** Moderate percentage of the night with elevated BQM (e.g., Y-Z%) | Considerable breathing irregularities detected | Considerable breathing pattern irregularities were detected for a noticeable portion of your sleep last night. This can sometimes disrupt sleep quality and might contribute to feeling less refreshed. <br><br>Factors that can influence breathing patterns at night include allergies, changes in altitude, certain medications, your sleep position, or underlying conditions that affect breathing during sleep. Tracking this metric over time can provide helpful insights. |
| **Significant amount of sleep with strained breathing last night 🔴** | **User-Facing Concept:** A considerable amount of the night with strained breathing patterns.<br><br>**Implicit Level:** Significant percentage of the night with elevated BQM (e.g., Z+%) | Significant amount of sleep with strained breathing last night | Significant irregularities were detected in your breathing patterns during a considerable portion of your sleep last night. Breathing patterns at this level of irregularity can significantly impact sleep quality and might contribute to feeling unrefreshed, or affecting your daytime mood and energy levels. <br><br>Such patterns can be influenced by a range of factors, including allergies, nasal congestion, changes in sleep position, certain medications, altitude, or underlying conditions that affect breathing during sleep. Consistent patterns like these may warrant closer attention over time. |

We will use 4 scenarios based on the percentage of the night with BQM exceeding the internal threshold (which correlates conceptually to the levels of irregularity but is presented based on amount of time).

**Key adjustments made in this revision:**
*   **Category naming:** Avoids "Mild," "Moderate," "Severe" as the primary descriptor for the category level itself. Instead, uses "Optimal," "Occasional," "Moderate," "Significant" Irregularities Detected.
*   **Body text framing:** Explicitly mentions the amount or portion of the night affected ("almost all," "occasional/short periods," "noticeable portion," "considerable portion") to align with the percentage-of-time aggregation and the "amount of sleep impacted" concept.
*   **Consistency:** Maintains the "sea of possibilities" list in the body text for non-optimal scenarios (B, C, D) as agreed upon from the first specialist feedback.
*   **Clarity:** Reinforces that the metric detects irregularities or patterns, not clinical conditions.

### Logan notes

This seems like a "frequency-only" adjective, instead of a percentage of the night adjective.

**Some Gemini considerations:**

*   **For Low Quantities:** Scant, Minimal, Trace, Limited, Sparse, Slight, Meager, Negligible, Paltry.
*   **For Medium Quantities:** Average, Typical, Standard, Intermediary, Mid-range, Normal, Common, Regular, Substantial, Adequate.
*   **For High Quantities:** Ample, Abundant, Extensive, Generous, Substantial, Significant, Considerable, Copious, Plentiful, Elevated.

I'm partial to: "Optimal", "Limited", "Considerable", "Substantial"