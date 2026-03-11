# Sleep Apnea SaMD and BQM Design Considerations

### How does the Sleep Apnea software as a medical device (SaMD) operate?
In a simplified sense:
*   Each minute of the night is assigned a breathing quality metric (BQM) score
*   The score ranges from 0 (lowest probability) to 1 (highest probability) of sleep apnea being present in that minute
*   A score is derived for a given sleep session
    *   By averaging all of the relevant minute-level BQM values
*   A sleep session is determined to be positive or negative for moderate-to-severe sleep apnea (ie, AHI ≥ 15)
    *   If the average BQM > 0.25, then the sleep session is considered positive
    *   If the average BQM ≤ 0.25, then the sleep session is considered negative
*   Sleep sessions may “inconclusive” if there are data limitations
*   A 10-day monitoring period is determined to be positive or negative for moderate-to-severe sleep apnea (ie, expected clinical diagnosis if assessed via in-lab PSG using AHI4% criteria)
    *   If 2 valid sessions in the 10-day period are both positive (average session BQM > 0.25)

### Some current design considerations for BQM in the non-regulated experience:
*Have a striking similarity to the representation within the SaMD.*

I believe this puts us at risk of regulatory scrutiny of our usage of the BQM time series in the non-regulated domain of the app, suggesting that we may be trying to deploy a regulated SaMD to general users (analogous to putting a prescription medication on the pharmacy shelves without appropriate labeling).

### Concerning similarities and potential mitigations:
*   **The same BQM cutoff usage in the SaMD and consumer product (~0.25 per 1-minute epoch)**
    *   This suggests a similar intent between the unregulated and SaMD experiences
    *   *Potential mitigation:* “flip the sign”, where in the SaMD is using the >0.25 cutoff to define an epoch with a high likelihood of sleep disordered breathing, the inverse could be shown to highlight “easy” breathing as the positive/upward direction
*   **Reporting on the summary (average) BQM for the sleep session:**
    *   This falls squarely into the SaMD’s intelligence (ie, choice of aggregation method per sleep session)
    *   *Potential mitigation:* don’t use the same method (average BQM) to summarize the night; instead consider a different aggregation method (eg, total minutes/percent of sleep with BQM above/below threshold). A clear argument can be made that the percentage of the night with BQM above/below threshold does not equate to the average BQM (as there’s a deliberate loss of magnitude of the BQM when talking instead about the time above/below threshold).
*   **A focus on a binary categorization (based on the BQM cutoff):**
    *   This suggests a similar intent between the unregulated and SaMD experiences
    *   *Potential mitigation:* since the SaMD is only differentiating between none-to-mild OSA (AHI < 15) and moderate-to-severe OSA (AHI ≥ 15), we could deliberately interpret the BQM differently for this product experience, aligning it with the OSA severity classification system (events/hr of sleep) as that’s a more natural analogy to the time-series representation anyhow:
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