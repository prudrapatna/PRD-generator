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