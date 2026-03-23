# Mini-PRD: Sleep Breathing Quality - Monthly Weighted Score

## 1. Overview & Goal
Currently, the Sleep Breathing Quality (SBQ) feature provides a daily rating based on the percentage of a given night the user spends in "optimal breathing." However, a single night's rating does not effectively communicate a user's long-term respiratory health trend. 

The goal of this feature is to provide a **Monthly Wellness Rollup** that accurately reflects the *intensity and frequency* of a user's breathing disruptions over a 30-day period. Based on specific guidance from clinical experts (Logan Schneider), this feature implements a **Weighted Average Monthly Score** to provide a scaled level of concern that is resistant to gaps in device wear time.

## 2. The Problem
* **Alarm Fatigue vs. Ignored Signals:** A simple linear average of daily percentages or an absolute cutoff count (e.g., "X bad nights") is flawed. It penalizes users who wear the device less frequently or fails to distinguish between a user who has 20 "moderate" nights versus a user who has 5 "severe" nights.
* **Terminology Confusion:** Using the same terms for daily and monthly ratings (e.g., "Excellent," "Fair") is confusing. Daily ratings describe *duration* (how much of a single night was affected), while monthly ratings describe *frequency and intensity* (how often and how severely the user is affected over time).

## 3. Proposed Solution: The Weighted Monthly Score
We will introduce a Monthly Wellness UX framework utilizing a glancible card for insights. The core of this insight is powered by a new weighted average scoring system designed to ensure severe nights disproportionately impact the monthly rating.

### 3.1. Monthly Thresholds (Clinical Heuristic Approach)
Because we do not currently possess a validated 30-day longitudinal dataset, we cannot train a regression model to definitively optimize the exact cutoffs for the 0.0 to 3.0 scale. 

Instead, we rely on the clinical heuristic consensus established by Logan Schneider regarding when a user's breathing quality shifts based on frequency and intensity. We map this heuristic onto the 0.0 to 3.0 scale to define our UX terminology bins.

**Data-Driven Bins & Terminology Mapping:**
*Note: Because higher scores indicate worse breathing, the frequency of "Optimal" breathing decreases as the score increases.*

| Weighted Monthly Score | UX Copy | Threshold Rationale |
| :--- | :--- | :--- |
| **0.0 to < 0.5** | **Optimal breathing: Most nights** | **Baseline:** Less than half of the user's nights showed non-optimal breathing. (e.g., heavily weighted toward 0-point Excellent nights). |
| **0.5 to 1.5** | **Optimal breathing: Some nights** | **Moderate Shift:** At least half of the nights were non-optimal (e.g., "Good" / 1 point), or a few nights were severe ("Low" / 3 points). |
| **> 1.5** | **Optimal breathing: Few nights** | **Significant Shift:** The vast majority of nights were "Moderate" (2 points) or "Low" (3 points). Optimal breathing is a rarity. |

### 3.2. UX & Terminology Rollup
The terminology for the monthly rollup must be distinct from the daily ratings to avoid confusing duration with frequency.
*   **Daily Ratings:** Describe *Duration* (how much of a single night was affected: "Excellent," "Good," "Moderate," "Low").
*   **Monthly Ratings:** Describe *Frequency* (how often the user achieves optimal breathing over the month, factoring in severity). 
    *   *Monthly Terms:* "Most nights," "Some nights," "Few nights."
    *   *Rationale:* "Most" clearly indicates a healthy baseline. "Some" implies inconsistency. "Few" carries a heavier connotation—indicating that optimal breathing is a rarity, which effectively flags chronic strain.

## 4. Critical User Journeys & Acceptance Criteria

**Target User:** Proactive Adopter (adults 18+ seeking to optimize their daily recovery)
**Context:** During a monthly wellness review in the Health app.

### 4.1. Combined CUJ & AC Table

| Pri | User Story | Goal (The "Why") | Task (The "How") | Product/CUI | Acceptance Criteria (Gherkin) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P0** | As a system, I need to calculate the weighted monthly score so that users receive accurate long-term insights based on clinical heuristics. | **I want to compute the Monthly Score** | 1. Tally the number of valid days.<br>2. Assign points to each valid day.<br>3. Calculate the weighted average. | *Backend Algorithm* | **Scenario 00: Calculation Logic**<br>• **Constant:** `MIN_VALID_DAYS` = 7<br>• **Point Values:** `EXCELLENT` (0 points, ≥ 94.3%), `GOOD` (1 point, 83%-94.2%), `MODERATE` (2 points, 66%-82.9%), `LOW` (3 points, < 66%)<br>• **Calculation:** `Weighted_Monthly_Score` = `Sum of (Daily Points) / (Total valid days)`<br>• **State:** If `<0.5` return "Most nights". If `>=0.5 and <=1.5` return "Some nights". If `>1.5` return "Few nights". |
| **P0** | As a user checking my daily stats, I want a quick summary of my monthly breathing quality so I know my long-term baseline at a glance. | **I want to see my trend at a glance** | 1. I open the Health app Today tab.<br>2. I view the glanceable card. | *Today Tab view*<br>*Glanceable Card* | **Scenario 01: Glanceable View (Today Tab)**<br>• **Given** user has a calculated Monthly Score state<br>• **When** the Today tab loads<br>• **Then** display the corresponding high-level monthly rating (e.g., "Optimal breathing: Most nights") on the glanceable card. |
| **P0** | As a user with a healthy baseline, I want to dig into my detailed metrics so I can verify my trend and see which specific nights were optimal. | **I want to see more information about that month** | 1. I tap the glanceable card to view the Health Tab L3.<br>2. I review my detailed 30-day timeline and tally of excellent nights.<br>3. I tap a specific day to view its daily sleep details. | *Health Tab L3*<br>*Within-Month Trend Chart* | **Scenario 02: Within-Month Detail View - Most Nights**<br>• **Given** user's state is "Most nights"<br>• **When** Health Tab L3 loads<br>• **Then** display "Optimal breathing: Most nights"<br>• **And** display the 30-day timeline chart<br>• **And** display a tally of the total number of nights with "Excellent" breathing<br>• **And** provide links from the chart to the respective daily Sleep L3 pages<br>• **And** surface the universal Sleep Apnea Assessment CTA. |
| **P0** | As a user with moderate breathing disruptions, I want to see detailed metrics and lifestyle nudges so I can understand why my trend is shifting. | **I want to know why my trend is shifting within the month** | 1. I view the Health Tab L3.<br>2. I read the explanation of the "Some nights" rating.<br>3. I review the suggested lifestyle factors (alcohol, position). | *Health Tab L3*<br>*Insight Expansion* | **Scenario 03: Within-Month Detail View - Some Nights**<br>• **Given** user's state is "Some nights"<br>• **When** Health Tab L3 loads<br>• **Then** display "Optimal breathing: Some nights"<br>• **And** surface the moderate shift insight card detailing lifestyle nudges<br>• **And** surface the universal Sleep Apnea Assessment CTA. |
| **P0** | As a user with severe breathing disruptions, I want to see my detailed trend so I can take action to improve my rest and avoid health risks. | **I want to take action to improve my rest** | 1. I view the Health Tab L3.<br>2. I see a warning about my severe trend.<br>3. I choose to take the Sleep Apnea Assessment. | *Health Tab L3*<br>*Assessment CTA* | **Scenario 04: Within-Month Detail View - Few Nights**<br>• **Given** user's state is "Few nights"<br>• **When** Health Tab L3 loads<br>• **Then** display "Optimal breathing: Few nights"<br>• **And** surface the significant shift insight card<br>• **And** surface the universal Sleep Apnea Assessment CTA. |
| **P0** | As a user who rarely wears my device to bed, I want to know why I don't have a monthly score so I can track it better next month. | **I want to know why data is missing** | 1. I navigate to the Health Tab L3.<br>2. I see a message explaining I need more data. | *Health Tab L3* | **Scenario 05: Insufficient Data**<br>• **Given** user has `total_valid_days` < `MIN_VALID_DAYS`<br>• **When** Health Tab L3 loads<br>• **Then** display "Not enough data"<br>• **And** prompt the user to wear the device more consistently. |
| **P0.5** | As a user, I want to compare my breathing quality across multiple months so I can see if my lifestyle changes are having a long-term impact. | **I want to see my month-over-month trend** | 1. I view the Health Tab L3.<br>2. I toggle the chart from the 30-day view to the broader historical view.<br>3. I see my month-over-month historical ratings. | *Health Tab L3*<br>*Month-over-Month Chart* | **Scenario 06: Month-over-Month Historical View**<br>• **Given** the user navigates to the historical view in Health Tab L3<br>• **When** the chart loads<br>• **Then** display a bar or line chart showing the monthly aggregated scores for previous months<br>• **And** allow the user to swipe/scroll back to view past monthly states (Most/Some/Few). |

### 4.2. Health & Metrics
*   **Usefulness Metric (Goal Level):** "How helpful was the monthly breathing insight in understanding your sleep quality?" (Extremely / Moderately / Slightly Helpful) via in-app survey.
*   **Usability Metric (Task Level):** % of users who click through the insight card to view educational content or take the assessment. (Target: > 15% click-through rate).

## 5. Open Questions & Next Steps
*   **UX Research:** Validate the proposed monthly terminology with users to ensure it does not cause undue medical anxiety.
*   **UI Constraints:** Ensure the Flex charting component can clearly visualize this weighted monthly aggregation.