# Sleep Breathing Quality PRD

## PRD Summary
**Overview of key requirements for Sleep Quality Breathing**
**Owners:** 
**Status:** Draft | Reviewed | In Development | Launched

## Overview
### Product Overview
Our goal is to move beyond simply tracking sleep and towards helping users truly understand your sleep quality. We want to empower users with the insights needed to take meaningful steps toward more restorative rest. A key, often overlooked, aspect of great sleep quality is how smoothly and consistently users breathe throughout the night. To help users see this connection, we are introducing a new way to understand and improve your sleep: Optimal Breathing.

This feature shows users the percentage of the night that they spent breathing easily and restfully. By focusing on the amount of time they spend in this optimal state, rather than an abstract score, we can get an intuitive sense of how restorative their sleep truly was.

This insight is a powerful tool for sleep coaching. By tracking your percentage of optimal breathing over time, the user and Proactive Health Assistant (PHA) can begin to connect daily habits to nightly rest. Users can see how factors like alcohol consumption, late-night meals, or even your sleeping position might be impacting breathing while sleeping and thus sleep quality. This data provides a concrete starting point for personalized recommendations, helping you make targeted adjustments for more consistently restful nights.

It is important to understand that this feature is designed to help you recognize patterns and make informed lifestyle choices for better sleep. It is not intended to diagnose sleep-related health issues or to suggest that there is something wrong with your health. The goal is to empower you with actionable information for your personal wellness journey.

### Why this matters 
Sleep Quality Breathing offers a clear, actionable metric to enhance user understanding of why their sleep may have been less restful. It enables data-driven, personalized insights and recommendations across multiple touchpoints, focusing on a key factor affecting sleep quality: breathing effort.

Integrating Sleep Quality Breathing into sleep insights will provide users with a more comprehensive and actionable understanding of why they may not be feeling rested after sleep. Here's how it enhances the user experience:
*   **Deeper Understanding of Sleep Restfulness:** Currently, sleep insights provide data on sleep stages, duration, and other metrics. Sleep Quality Breathing adds a critical layer by explaining why sleep might have been restful or not. A higher Sleep Quality Breathing score, indicating increased breathing effort, will directly correlate with less restful sleep, providing users with a tangible explanation of a core reason behind their sleep quality.
*   **Actionable Insights into Reasons for Poor Sleep:** By highlighting the impact of breathing effort on sleep quality, Sleep Quality Breathing empowers users to understand a key reason for poor sleep and take proactive steps. This could include:
    *   Prompting users to explore potential contributing factors to increased breathing effort, such as positional changes, allergies, or congestion.
    *   Encouraging users to take the sleep apnea assessment as one of the tools to learn about the reason for higher Sleep Quality Breathing (when apnea is available).
*   **Proactive Identification of Factors Affecting Sleep:** Integrating Sleep Quality Breathing across Ask Health and proactive insights enables users to monitor a key factor affecting their sleep quality over time. This can facilitate early identification of potential breathing-related issues that may be impacting sleep and encourage timely intervention.
*   **Personalized Guidance Focused on Improving Restfulness:** Sleep Quality Breathing data will enable more personalized sleep coaching experiences. Recommendations can be tailored based on individual breathing patterns and the level of breathing effort during sleep, leading to more effective interventions and improved sleep restfulness.

### Devices
Sleep Quality Breathing is an on-device algorithm and requires a software update to be made available and will be available only on Pixel 3+ and Radiance+, Mukai+.
*   **Phase 1 (December QPR 2025):** Pixel Watch 3, Pixel Watch 4
*   **2026 (exact timeline TBD):** Radiance, Mukai

### Proposed Intended Use/Indications for Use
The Sleep Quality Breathing feature is a software-only feature intended to help users understand and track their nightly breathing patterns as an indicator of sleep quality. The feature analyzes physiological and motion data acquired from compatible consumer wrist-worn products to provide a percentage of time the user spent in 'Optimal Breathing,' defined as breathing easily and restfully.

The Sleep Quality Breathing feature is intended for over-the-counter (OTC) use for general wellness and to empower users with information to make lifestyle choices for more restorative sleep. A high percentage of Optimal Breathing is not intended to rule out the presence of sleep-related breathing disorders. Rather, the feature is intended to help users recognize patterns between their lifestyle choices (such as diet, alcohol consumption, and sleep position) and their nightly breathing quality.

These data are only analyzed when the underlying sensor signals are of sufficient quality. The feature may encourage users to explore contributing factors to increased breathing effort or to take a separate sleep apnea assessment. The feature is not intended to diagnose, treat, mitigate, or prevent any disease or condition, including sleep-related breathing disorders like sleep apnea. It is not intended to replace traditional methods of diagnosis or treatment by a healthcare professional.

The feature has not been tested for and is not intended for use in people under 18 years of age. 

### Labeling (Precautions / Warnings)

Device labeling will make clear to users that Sleep Quality Breathing is not for:
*   **Use for diagnostic purposes:** The feature is an informational and wellness tool and should not be used to diagnose any medical condition. A healthcare professional must be consulted for the diagnosis of sleep-related health issues.
*   **Use for treatment decisions:** The feature is not intended to guide or replace clinical judgment for treatment decisions. Individuals should not make changes to their medication or treatment plan based solely on the feature's output.

## Product Details and Requirements
### Primary CUJs
While there are multiple utilities for Sleep Quality Breathing, we will adopt a phased approach to delivering this feature.
*   **Phase 1 (December QPR 2025):** Visually show the Sleep Quality Breathing trend with % of night with optimal breathing in Public Preview. This will be available for all free and premium users. 
*   **Phase 2 (2026):** Integration into sleep insights and ask health (incl proactive insights) in PHA app

### Use Case and Feature Requirements
Describe the key features of this product and their priority. Frame requirements as AAU (as a user). Indicate priority for each requirement.

**Priority definition**
*   **P0:** Features that must be part of the initial launch. Describe each P0 feature related to this use case in detail. 
*   **P1:** Features that should be part of initial launch. Describe each P1 feature related to this use case in detail. 
*   **P2:** Features explicitly punted until later. Describe each P2 feature related to this user case in detail. 

#### Feature Area 1: As a user, I want to know how my breathing disturbance impacted my sleep.

**Features & Priorities**

| # | Pri | User Story | CUJ Task | Issue |
|---|---|---|---|---|
| 1.1 | P0 | As a user, I want to know how my breathing impacted my sleep quality the previous night. | View my breathing quality for the past night. | AC 1: The user shall be able to access a visualization in the form of a graph of their breathing quality data for the most recent sleep session.<br><br>AC 2: Sleep Quality Breathing time series must be such that users are able to see the relationship between their sleep stages and heart rate. (eg:For example, users should be able to see Sleep Quality Breathing go up and the corresponding HR, Sleep Stage change) |
| 1.2 | P0 | As a user, I want to understand my breathing quality at a glance | See if it was breathing regularity was optimal | AC 1:<br>EXCELLENT: Good breathing quality for almost all of your sleep<br>GOOD: Good breathing quality for most of your sleep.<br>FAIR: “some” sleep with good breathing quality<br>LOW: “limited amount” of sleep with good breathing quality<br><br>Here are the cutoff points:<br>Excellent - [1-BQM] ≥ 94.3%<br>Good - ≥ 83% [1-BQM] < 94.3%<br>Moderate - ≥ 66% [1-BQM] < 83%<br>Low - ≤ 66% |
| 1.3 | P0 | As a user, I want to understand what parts of my night was optimal | Understand what % of night was optimal | AC 1: The summary shall include a % of minutes night that was optimal for the user.<br><br>AC 2: For each minute of input data, the component shall generate a corresponding Sleep Quality Breathing estimate.<br><br>AC 3: The calculation for x% of night should follow the below:<br>x% = Epochs of sleep with (1-Sleep Quality Breathing) > 0.75 / epochs of sleep<br><br>AC 4: The user interface shall clearly indicate if the breathing quality for the night was optimal or not based on the threshold comparison. |
| 1.4 | P0 | As a user, I want to understand my Sleep Quality Breathing trends. | See the trend breathing quality against the optimal threshold. | AC 1: The trend should be for weekly and monthly.<br><br>AC 2: For weekly trend:<br>Show the average % of night with optimal breathing for the entire week.<br>Day by day trend for that week for the % of night with optimal breathing.<br><br>AC 3: For monthly trend:<br>Show the average % of night with optimal breathing for the entire month.<br>Week by Week average trend for that week for the % of night with optimal breathing. |
| 1.5 | P0 | As a user, I want to be understand my Sleep Quality Breathing irrespective of where I live | Get graph and description in the choice of my language and country | AC 1: Sleep Quality Breathing should be available to all users where Fitbit app and Pixel Watch is supported.<br><br>AC 2: The Sleep Quality Breathing description should be in the language set with the Fitbit mobile app. |
| 1.6 | P0 | As a PM, BQM must be shown only for the Sleep session (TATS window) | Show BQM for the TATS window. | AC 1: BQM must be displayed only during TATS period<br><br>AC 2: Any BQM outside of TATS should not be displayed<br><br>AC 3: This should be visible only to Public Preview. |
| 1.7 | P0 | As a user, I should get my sleep breathing quality for my main sleep | | AC 1: There should be just one BQSS value per user per main sleep period<br><br>AC 2: The BQSS should be for all sleep sessions that overlaps with typical sleep window /main sleep. If there are two sessions within the typical sleep window which are glued, then the BQSS should be for for the two glued sessions.<br><br>AC 3: If there is only one session > 3 hours then calculate BQSS only for that session within that day. |
| 1.8 | P0 | As a user, I must be able to delete my data if I choose to | When the user deletes sleep under data deletion options, the sleep breathing quality should also be deleted | AC 1: When the user deletes the sleep data, all the sleep breathing metrics including BQM must be deleted. |
| 1.9 | P0 | As a user, I must be able to takeout my sleep quality breathing data | When the user chooses to takeout their fitbit data, they should also get a sleep quality breathing data | AC 1: User sees percentage of time that was optimal.<br><br>AC 2: User sees duration of time that was optimal. |
| 1.10| P0 | As a user, I must be able to interact with “ask coach” to learn more about the feature | The user should be able to interact with “Ask Coach” to learn more about the feature, how it works, how is the rating done. | AC 1: The user should be able to ask questions around:<br>- What is the feature, what is it measuring?<br>- What does it mean for the user?<br>- What are the ratings and what does it mean?<br>- Why would someone get this rating<br>This should just focus on lifestyle and not talk about health conditions or offer medical advise. |
| 1.11| P1 | As a user, I want to understand my Sleep Quality Breathing for naps | See the Sleep Quality Breathing when the user takes a nap | AC 1: For any sleep <60 mins, Sleep Quality Breathing should be computed. Visualization TBD |

#### Feature Area 2: As a user, I want to get insights on how my breathing disturbance impacted my sleep quality.

| # | Pri | User Story | CUJ Task | Issue |
|---|---|---|---|---|
| 2.1 | P0 | As a user I must be able learn more about sleep breathing through a conversation | Ask questions about the feature or ask about their breathing quality and what it means | AC 1: Users must be able to ask questions and learn more about the feature including what does the feature indicate, how was it developed.<br><br>AC 2: Ask what the optimal breathing % for that user means. Answer questions about the trends of the % optimal breathing. |
| 2.2 | P1 | As a premium user, I want to understand how my breathing quality correlates with other sleep metrics. | View breathing quality in relation to sleep stages, heart rate, and restlessness. | AC 1: Generate an insight for the user, such that they can see the association between sleep stages, heart rate and Sleep Quality Breathing. (eg: relationship between sleep fragmentation and breathing quality metric)<br><br>AC 2: Users should get proactive insight but also have the ability to use ask health for a more deep dive.<br><br>AC 3: Ask health should be able to generate a graph based on user prompt, to show the relationship in a single graph |
| 2.3 | P2 | As a premium user, I want to receive proactive insights based on my breathing quality patterns over time. | Receive personalized recommendations or insights based on trends in their breathing quality data. | AC 1: The system shall analyze Sleep Quality Breathing data over multiple sleep sessions to identify patterns and trends.<br>AC 2: Based on identified patterns, the system shall provide personalized insights or recommendations to the user aimed at improving sleep restfulness. |
| 2.4 | P2 | As a premium user, I want suggestions on factors that might be impacting my breathing quality. | See potential contributing factors for increased breathing effort based on their Sleep Quality Breathing data and other available information. | AC 1: The system shall suggest potential factors that could contribute to increased breathing effort (e.g., positional changes) based on the user's Sleep Quality Breathing data and potentially other relevant data sources (if available and approved). |

## Success Metrics

| Category | KPI | Target | Source |
|---|---|---|---|
| User facing metrics | Clarity of Breathing Quality: Percentage of users who find the breathing quality categories (Excellent, Good, Fair, Low) to be a clear and accurate representation of their sleep quality. | >= 50% of nights agree or strongly agree. | Dogfood |
| Product Metrics | Data Availability: Percentage of nights with a valid sleep session where Sleep Quality Breathing data is successfully generated and displayed. | >= 99%. This high target ensures reliability and user trust | Dogfood |
| Product Metrics | Coverage During Sleep: For a given valid sleep session, the percentage of the total sleep time that has BQM data. | >= 95% coverage. This allows for a drop-off rate of up to 5%, accounting for minor, unavoidable data interruptions while ensuring a robust and reliable dataset for analysis. | Dogfood |
| Algorithm | Given valid PPG and accelerometer sensor data as input, the component shall calculate a "Sleep Quality Breathing" estimate representing the probability (expressed as a value between 0 and 1, inclusive) that a desaturation event of 4% or greater SpO2 occurred within that minute. | A desaturation event of 4% or greater SpO2 occurred within that minute. | PSG Dataset |
| Data Coverage | Percentage of users for whom sleep stages for that night are shown, for whom Sleep Quality Breathing is also shown. | 100% | User Requirement |
| Performance | Latency for Sleep Quality Breathing calculation and display after a sleep session ends. | Same as Sleep Stages and SpO2 availability | User Requirement |
| User Engagement | Percentage of target users who view their Sleep Quality Breathing data at least once per week. | To be determined. | Derived from User Goal |
| User Engagement | Percentage of target users who engage with personalized insights related to Sleep Quality Breathing. | To be determined. | Derived from User Goal |

**Metrics to track:**
*   Number of nights Sleep Quality Breathing was available for users.
*   Number of unique users for whom Sleep Quality Breathing was calculated and displayed, split by age, BMI, and sex.
*   Distribution of Sleep Quality Breathing scores among the target user population.
*   Correlation of Sleep Quality Breathing with user-reported sleep quality.
*   Impact of personalized insights on user behavior and Sleep Quality Breathing trends over time.
*   User feedback related to the Sleep Quality Breathing feature.

## Launch Plan and Launch Considerations

*   **Teamfood:** Enter teamfood (date x)
*   **Dogfood:** Enter dogfood: June, 2025 w/ exception to only upload data from pre-trial group. No UX. Only algo.
*   **December QPR (Pixel Watch 3+ Only):**
    *   Leave things as is in DF for the upcoming December release.
    *   The BQM algorithm will continue to run locally on the device (but its output will not be sent to the backend).
    *   No new code changes or flag reversions will be made, as this would add unnecessary risk so close to the release.
    *   The change to enable data upload (and potentially full dark launch) will be targeted for ahead of the March QPR instead. 
    *   The change is gated by NL a phenotype flag and must NOT be enabled without approval from leads.
*   **GA:** Dec QPR
*   **Radiance, Mukai:** TBD (Q1-Q2 2026)