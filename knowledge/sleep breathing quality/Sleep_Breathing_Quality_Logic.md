# Sleep Breathing Quality Logic

## Slide 1
**Reviewed with Regulatory on 7/10/2025**
**Attendees:** Dinesh Puppala, R K Neelakandan, Faiza Harji, Logan S, Taalib, Pramod Rudrapatna

**Key areas of alignment:**
* No concern on this approach by regulatory.
* Document in the PRD that if BQM changes, then apnea algo has to be validated to ensure it is non-inferior.
* Add disclaimer that this is not meant to be used for any health purposes
* We could provide an option for users to take assessment if 
* Lean in on more of % of minutes above a certain threshold and use that for rating instead of using session level BQM

## Slide 2
| % of Minutes of optimal breathing | Rating |
| --- | --- |
| >= 94.3% | Excellent |
| >=83% [1-BQM] <94.3% | Good |
| >=66% [1-BQM] <83% | Moderate |
| <=66% | Low |

These ratings are based on entire sleep session and consistent with what Oura does
% of night = total minutes of >0.75/ total minutes of sleep

*Note: This is calculated at a minute level*

## Slide 3
x% = Total minutes of sleep with (1-BQM) > 0.75 / Total minutes of sleep

**Insight:** x% of your night with optimal breathing
A fixed threshold (approximately 0.25, based on algorithm training and testing in the development dataset) has been set for the BQM to mark a sleep session for irregular sleep breathing

**Acceptance Criteria:**
* **AC1.1:** Given valid PPG and accelerometer sensor data as input, the component shall calculate a "BQM" estimate representing the probability (expressed as a value between 0 and 1, inclusive) that a desaturation event of 4% or greater SpO2 occurred within that minute.
* **AC1.2:** For each minute of input data, the component shall generate a corresponding BQM estimate.
* **AC 3:** < 5% data drops

To screen yourself and learn more consider taking a screen 
Add a small disclaimer

## Slide 4
| 1. Excellent (>= 93.2% Optimal) | 2. Good (83% - 93.1% Optimal) | 3. Moderate (66% - <83% Optimal) | 4. Low (<66% Optimal) |
| --- | --- | --- | --- |
| **Title:** Optimal breathing | **Title:** Good breathing quality | **Title:** Fair breathing quality | **Title:** Less optimal breathing |
| **Metric:** 95% of night with optimal breathing | **Metric:** 90% of night with optimal breathing | **Metric:** 82% of night with optimal breathing | **Metric:** 65% of night with optimal breathing |
| **Body:** This is a great sign of restorative sleep | **Body:** A solid night for breathing that supports quality rest | **Body:** This means only some periods of you night were optimal, which can affect how refreshed you feel | **Body:** This means limited parts of your night were optimal. It's helpful to keep an eye on this pattern over time. |
| **Badge:** Ideal | **Badge:** Ideal | **Badge:** Less ideal | **Badge:** Less ideal |

Copy

## Slide 5
← less severe OSA
higher percentage of the night with “quality breathing” (ie, 1-BQM > 0.75) →

Higher percentage of “quality breathing” correlates with less severe OSA
CART-identified cutoffs of %TST cutoffs reasonably differentiate OSA severities

higher percentage of the night with “quality breathing” (ie, 1-BQM > 0.75) →
Proportion of population

A different BQM interpretation still reasonably captures sleep breathing quality
Colab

## Slide 6
The cutoffs were established based on Recursive Classification and Regression Trees (CART) method
Colab

## Slide 7
Excellent
Good
Moderate
Low
Colab

## Slide 8
| % of Minutes of optimal breathing | OSA Severity |
| --- | --- |
| >= 93.2% | No OSA |
| >=87.634% [1-BQM] <93.202% | Mild OSA |
| >=75.897% [1-BQM] <87.634% | Moderate OSA |
| <=75.897% | Severe OSA |

| % of Minutes of optimal breathing | Rating |
| --- | --- |
| 93% | Normal - Mild |
| 87% | Mild - Moderate |
| 79% | Moderate - Severe |

CART Approach
ROC Optimization to meet Se/Sp
The cutoff points are comparable across two different approaches
Colab

## Slide 9
Confusion Matrix with CART
Confusion Matrix with percentile approach
The CART approach yields significantly better performance in terms of true positive and false positives 

## Slide 10
Normal sleeper:  BQM, Stages, restlessness and HR

## Slide 11
Mild to Moderate apnea BQM, Stages, restlessness and HR

## Slide 12
Severe apnea BQM, Stages, restlessness and HR

## Slide 13
*(No text content)*

## Slide 14
*(No text content)*

## Slide 15
Elevated
Not Elevated
SAMD → This is only for someone with a positive assessment

## Discussion Notes (Logan / Pramod - Mar 5, 2026)

**Summary:**
Training data transparency for publications and charting constraints for optimal breathing percentage, with development of a weighted average for monthly breathing quality score.

**Next steps:**
* Someone in Forrest Gump (us-cam-5cc) will update their deck to reflect the new cut points for BQM.
* Logan Schneider will advocate for improving how sleep is represented because the flex model is confusing for sleep.

**Details:**

* **Framing Training Data Transparency for Publications:** The speakers discussed the challenge of maintaining transparency regarding the training data set, specifically for a white paper, while adhering to restrictions on certain data sources. Logan Schneider noted that while a blog post might permit a general statement about the data set, a peer-reviewed standard demands explicit transparency about the data used in development, which is currently complicated by the prohibition on using NSRR data sets for commercial product development. A proposed approach is to state that models developed on restricted data sets were then trained and tuned on their own data set, using a transfer learning approach.
* **Implementation of New BQM Cut Points:** The speaker confirmed they have received the new cut points for BQM and will update their deck to reflect those new points for use in their materials.
* **Addressing Charting Constraints for Optimal Breathing Percentage:** A charting issue related to the flex component makes it difficult to visually show multiple layers of data, such as when BQM was calculated versus when the user was awake, and the percentage of optimal breathing during sleep. For V1, the proposed solution is to simplify the representation by providing a wellness rating (e.g., excellent, optimal, fair, pay attention) and displaying "x percentage of night was optimal breathing," with an optional click-through to educational content. The participants agreed that they must operate within current constraints to communicate clearly, despite the flex model being inadequate for representing sleep.
* **Monthly Aggregation and Visualization of Breathing Quality:** The discussion moved to a monthly wellness UX framework that uses a glancible card for insights and attention flags. They agreed that setting arbitrary cut points for monthly reporting is necessary since they cannot validate them. A consensus was reached that a simple, defensible position is that if more than half of a person's nights are not characterized by optimal breathing, a "pay attention" threshold is triggered, moving beyond a simple absolute cutoff that would be meaningless for people who do not wear their device every night.
* **Developing a Weighted Average for Monthly Breathing Quality Score:** To create a more sophisticated monthly score that is resistant to the total number of days collected, Logan Schneider proposed a weighted average using a point system for the daily ratings (zero points for excellent, three points for low). This scoring system aggregates the intensity of poor breathing nights, meaning one severe night would contribute more to the final monthly score than 20 moderate nights, allowing for a scaled level of concern. The weighted average calculation would be the sum of the points multiplied by the number of nights at that level, divided by the total number of days represented in the data.
* **Terminology for Daily vs. Monthly Rating Rollups:** The participants decided that the terminology for the monthly rollup should be different from the daily ratings to avoid confusion since they represent two different time-scale ratings: daily ratings describe duration (how much of the night was affected), while monthly ratings describe frequency (how often the user is affected). Instead of "excellent/good/moderate," the monthly score should use terms reflecting frequency or level of urgency, such as "often, seldom, sometimes" or "significant, modest".
* **Critique of the Sleep Score and Submetrics:** Logan Schneider expressed concern over the "unvalidated metric" of the sleep score, particularly the submetric of "time to persistent sleep," which they noted is confusing because a zero-minute result could represent a healthy outcome or a pathological state such as narcolepsy. The metric is currently unvalidated in terms of its health implications, its ability to separate disease from health, and its coachability, making it unclear how to advise users on improvement.
* **Coherence Issues from Mixing Sleep Metrics:** Combining the time to persistent sleep metric with sleep onset latency creates a further coherence issue because one part is controllable by the user (sleep onset latency) and the other is not understood, making the coaching guidance useless and potentially confusing for the user. The speakers agreed this situation creates a significant cognitive load for the user, who would have to read a wall of text from the coach to understand what is not visually present in the metrics.
* **Advocacy for Visual Metrics Over Coach Text:** Both speakers strongly agreed that user experience research (UXR) demonstrates that users prefer to find their key metrics visually rather than reading long texts from the coach, supporting the need for transparency and understandability. They believe that relying too heavily on the coach to parse out complex metrics is a failed approach and they will push back on forcing a single metric, suggesting that UXR should determine if a single metric is truly glancible for users.
