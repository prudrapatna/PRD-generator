# Project Metadata & Approvals

*   **Deliverable:** Mini PRD (Product Narrative)
*   **Resources:** PM (Dushyant Vipradas, Shamira Sridharan Weaver), UXR (Whargett, Suki B), UX Lead (Anna Kong), UX Writing (Anitra Appa, Dominique Fong)
*   **Localization:** Global (all users where Fitbit app & Pixel Watch are supported)
*   **Lock Dates:** TBD

| Role | Approver | Date | Status |
| :--- | :--- | :--- | :--- |
| **Product Lead** | TBD | TBD | Pending |
| **UX Lead** | Anna Kong | TBD | Pending |
| **Eng Lead** | TBD | TBD | Pending |
| **Regulatory** | Dinesh Puppala | 7/10/2025 | Approved |

<br>

<table style="border: 1.5pt solid black; width: 100%; border-collapse: collapse;">
  <tr>
    <td style="padding: 20px;">
      <h1>Sleep Breathing Quality</h1>
      <h2>Google's Personal Health Assistant Is Learning to Spot — and May Help Optimize — Your Sleep Breathing Quality Trends</h2>
      <p><strong>August 16th, 2026:</strong> For millions of people, waking up exhausted despite getting enough hours of sleep is a frustrating mystery. Often, the culprit is invisible: subtle, persistent irregularities in breathing during the night that disrupt restorative sleep. Because we are asleep when this happens, these patterns go unnoticed, leaving people without the awareness needed to improve their rest and daytime energy.</p>
      <p>Today, we're introducing Sleep Breathing Quality, a new wellness feature for Pixel Watch and Fitbit devices. Without requiring any extra equipment or behavior changes, the Personal Health Assistant continuously analyzes tiny variations in your nighttime breathing. It translates these complex signals into a simple, daily insight: the percentage of your night spent in "Optimal Breathing."</p>
      <p>Most days, this feature quietly works in the background, providing a reassuring glance at your sleep quality. But if the Assistant notices a trend of limited optimal breathing over time, it steps in as a helpful coach. It will connect these patterns to your daily lifestyle choices—like your sleep position, late-night meals, or temporary congestion—empowering you with the context you need to make targeted adjustments for better, more restorative nights.</p>
      <p><em>"We believe that technology should illuminate the hidden aspects of our health, turning abstract data into an opportunity for empowerment,"</em> said Rishi Chandra, VP of Google Health. <em>"With Sleep Breathing Quality, we are giving people visibility into the restorative power of their sleep, helping them connect the dots between how they live and how they breathe at night."</em></p>
      <p><em>"Providing users with a clear, longitudinal view of their nighttime breathing patterns is a powerful tool,"</em> said Dr. [SME Name], Clinical Expert. <em>"It moves the conversation from guessing why we are tired to understanding specific lifestyle factors that can improve our overall sleep hygiene."</em></p>
      <p>Sleep Breathing Quality is designed to start conversations and inspire healthier habits, not replace professional care. It provides thoughtful, personalized insights to help you manage your wellness, and if patterns persist, seamlessly guides you toward a clinical assessment when appropriate.</p>
    </td>
  </tr>
</table>

## Overview

A significant portion of the population struggles with feeling unrefreshed after sleep, often unaware that the quality of their breathing during the night is the underlying cause. While severe sleep-related breathing disorders impact many, even mild to moderate breathing irregularities can significantly fragment sleep and reduce its restorative value. Because these disruptions occur while we are unconscious, they represent an "invisible signal." Users lack the urgency or the tools to monitor this nightly, often accepting daytime fatigue as normal rather than a variable they can optimize.

Sleep Breathing Quality addresses this awareness gap by utilizing the optical (PPG) and motion sensors already present on Pixel Watch and Fitbit devices to estimate the regularity and smoothness of a user's breathing. It focuses on a positive, easily understood metric: the percentage of the night spent with optimal breathing. By aggregating this data into weekly and monthly roll-ups, the feature helps users separate a single "bad night" from a persistent trend, correlating these patterns with lifestyle factors like sleeping position or alcohol consumption to empower proactive wellness adjustments.

Why now? Because wearables have reached a level of sophistication where they can passively detect these subtle physiological patterns without the friction of specialized equipment. By integrating this capability into Google Health's Personal Health Assistant, we are shifting the paradigm from reactive, episodic clinical screening to continuous, empowering daily awareness, helping users optimize their recovery and understand their bodies better.

## Target Product Profile

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | A software-only general wellness feature intended to help users understand and track their nightly breathing patterns as an indicator of sleep quality. It analyzes physiological and motion data to provide a percentage of time spent in 'Optimal Breathing' to empower lifestyle choices. |
| **Disclaimer** | Intended for over-the-counter (OTC) use for general wellness. Not intended to diagnose, treat, mitigate, or prevent any disease or condition, including sleep apnea. |
| **Problem Statement** | Users frequently experience unrefreshing sleep due to unrecognized breathing irregularities; they lack accessible tools to correlate these invisible disruptions with their daily lifestyle choices. |
| **Product Overview (P0/P1)** | Passive tracking of nighttime breathing quality using PPG and accelerometer data; provides daily % of optimal breathing, weekly/monthly trend roll-ups, and integrates with "Ask Coach" for context. |
| **Product Output (P0/P1)** | Daily categorical rating (Optimal, Limited, Considerable, Significant irregularities) and exact percentage of night in optimal breathing; longitudinal trend graphs. |
| **Positioning (The "North Star")** | A daily wellness lens for continuous awareness and lifestyle optimization, acting as a bridge to clinical screening if persistent patterns are detected. |
| **Product Type** | Mobile Application Feature (within Google Health / Fitbit App). |
| **Assessment Period** | Minute-by-minute analysis during a valid sleep session; aggregated nightly, weekly, and monthly. |
| **Regulated or Wellness?** | General Wellness (Non-Regulated). |
| **Target Segment** | Adults 18+ seeking to understand and improve their sleep quality and daily recovery. |
| **Contraindication** | Not tested for or intended for use in people under 18 years of age. |
| **Product Inputs** | Valid PPG and accelerometer sensor data during sleep (Main sleep periods). |
| **Supported Devices** | Pixel Watch 3+, Radiance+, Mukai+. |
| **Country Availability** | Global (where Fitbit app and Pixel Watch are supported). |

## Market Positioning: The Personal Health Assistant

<table style="border: 1.5pt solid black; width: 100%; border-collapse: collapse;">
  <tr style="border-bottom: 1pt solid gray;">
    <td style="width: 25%; padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">1</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Breathing Quality<br>on PHA</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The Personal Health Assistant acts as an always-on guardian for your rest, learning to spot subtle, invisible patterns in your nighttime breathing. Rather than overwhelming you with data, it translates complex sensor readings into a simple, actionable understanding of how smoothly you breathe while you sleep.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">2</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Awareness Gap</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Millions of people wake up feeling unrefreshed, unaware that their sleep was fragmented by strained breathing. Because these disruptions happen entirely outside of our conscious awareness, they represent a massive missed opportunity for improving daily energy, mood, and long-term cardiovascular health.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">3</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">A First-of-its-Kind<br>Wellness Lens</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      While others offer binary medical screening, this is the first system to provide a continuous, daily "Wellness Lens" based on the percentage of optimal breathing. It bridges the gap between everyday lifestyle optimization and long-term health risk, turning a clinical metric into an empowering daily habit coach.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">4</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">How it Works</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Using the advanced PPG and accelerometer sensors on the Pixel Watch, the system calculates a minute-by-minute Breathing Quality Metric (BQM) during your main sleep window. It aggregates this data to show what percentage of your night was spent breathing optimally, automatically filtering out the noise to highlight true patterns.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">5</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Rigorous Validation</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The thresholds for "Optimal Breathing" were established using rigorous Recursive Classification and Regression Trees (CART) methods. We aligned our general wellness categories conceptually with established clinical severity scales, ensuring the insights you receive are grounded in scientifically sound models of respiratory health.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">6</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Intelligent Nuance</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The system is designed to differentiate between a single restless night and a chronic issue. By utilizing a Monthly Wellness Roll-up, the AI carefully transitions the conversation from temporary "weather" (like a night of nasal congestion) to long-term "climate," preventing alarm fatigue and building trust.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">7</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Global Scale</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Because this is classified as a General Wellness feature, it is designed for global availability from day one. It will be accessible to all users where the Fitbit app and Pixel Watch are supported, bringing vital awareness to a worldwide audience without regional regulatory delays.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">8</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Ecosystem of<br>Care</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Breathing Quality doesn't exist in a vacuum. It integrates directly with Sleep Stages, Heart Rate, and the AI-powered "Ask Coach" feature. If persistent irregularities are detected, the system intelligently bridges the user to the regulated Sleep Apnea SaMD assessment, ensuring a safe, continuous path from wellness to clinical care.
    </td>
  </tr>
  <tr>
    <td style="padding: 15px; vertical-align: top;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">9</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Clinical Alignment</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Developed in close coordination with regulatory and clinical experts, our approach deliberately separates daily wellness tracking from disease diagnosis. This careful design ensures we empower users with actionable lifestyle data without stepping over the line into unintended medical management.
    </td>
  </tr>
</table>

## Critical User Journeys (CUJs)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **Immediate Context:** Understand how my breathing impacted my sleep quality last night. | View my breathing quality rating (Optimal, Limited, etc.) and the percentage of the night that was optimal. | **Sleep Tab (Daily):** "Your breathing quality was optimal last night with 95% of your night with optimal breathing." |
| **Pattern Recognition:** See if my poor sleep is a recurring issue. | Check weekly and monthly trends of % of night with optimal breathing. | **Trend View:** Monthly roll-up showing the frequency of days with optimal breathing > 94.3%. |
| **Contextual Nuance:** Learn more about what might be causing my strained breathing. | Interact with "Ask Coach" to understand what the rating means and what lifestyle factors (sleep position, alcohol) might affect it. | **Ask Coach:** "Ask what the optimal breathing % for that user means. Provide lifestyle context, not medical advice." |
| **Clinical Bridge:** Determine if my wellness trends require medical attention. | Receive a nudge from the Monthly Roll-up suggesting a formal Sleep Apnea Assessment if patterns are persistently poor. | **Monthly Roll-up Nudge:** "You had very few nights with optimal breathing... Consider taking an apnea test to learn more." |

## Algorithm Target Performance

| Metric | Target | Rationale |
| :--- | :--- | :--- |
| **Data Availability** | ≥ 99% | Percentage of nights with a valid sleep session where data is successfully generated; ensures reliability. |
| **Coverage During Sleep** | ≥ 95% | For a valid session, the percentage of total sleep time that has BQM data (allows <5% data drops). |

| Current Performance | Cutoff (1-BQM) | Wellness Rating |
| :--- | :--- | :--- |
| **Tier 1** | ≥ 94.3% | Excellent / Optimal |
| **Tier 2** | ≥ 83% to < 94.3% | Good / Limited Irregularities |
| **Tier 3** | ≥ 66% to < 83% | Moderate / Considerable Irregularities |
| **Tier 4** | < 66% | Low / Significant Irregularities |

## Feature Logic & Program Timeline

| Variable | Value | Description |
| :--- | :--- | :--- |
| **Epoch Duration** | 1 minute | BQM estimate generated for each minute of input data. |
| **BQM Threshold** | > 0.25 | Fixed threshold to mark a minute for irregular sleep breathing. |
| **Optimal Breathing Math** | (1 - BQM) > 0.75 | Calculates the % of total sleep minutes that were optimal. |
| **Data Drop Limit** | < 5% | Maximum acceptable data drop rate during a valid session. |
| **TATS Window** | Main Sleep | BQM is only calculated and displayed for the main sleep period. |

*   **Teamfood:** Date TBD
*   **Dogfood:** June 2025 (Algo only, no UX)
*   **Public Preview:** December QPR 2025 (Pixel Watch 3/4)
*   **General Availability:** Q1 2026 (Google Health Rebrand launch)
*   **Device Expansion:** Q1-Q2 2026 (Radiance, Mukai)

## Summary: What's Next

*   **Finalize UX/UI:** Lock the visualizations for the daily view and the monthly trend roll-up, ensuring they align with the new Google Health design system.
*   **Refine "Ask Coach" Prompts:** Develop the specific conversational pathways for the AI coach to handle inquiries about breathing quality, ensuring strict adherence to wellness (non-diagnostic) guardrails.
*   **Bridge to SaMD Flow:** Map the exact user journey and notification triggers for when the Monthly Wellness Roll-up prompts users in cleared regions to take the formal Sleep Apnea Assessment.
*   **Regulatory Review of Copy:** Conduct a final review of all user-facing strings (especially the 4 category descriptions) to confirm they safely reflect "amount of sleep impacted" rather than clinical severity.