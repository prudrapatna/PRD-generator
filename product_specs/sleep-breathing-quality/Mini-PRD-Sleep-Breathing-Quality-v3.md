# 1. Approval Cover Page

| Role | Approver | Approval Status | Date |
| :--- | :--- | :--- | :--- |
| **Product Lead** | TBD | Pending | |
| **UX Lead** | Anna Kong | Pending | |
| **Eng Lead** | TBD | Pending | |
| **Regulatory** | Dinesh Puppala | Approved | 7/10/2025 |
| **UX Writing** | Anitra Appa, Dominique Fong | Pending | |

<br>

<table style="border: 1.5pt solid black; width: 100%; border-collapse: collapse;">
  <tr>
    <td style="padding: 20px;">
      <h1>Sleep Breathing Quality</h1>
      <h2>Google's Personal Health Assistant Is Learning to Spot — and May Help Optimize — Your Nighttime Breathing Trends</h2>
      <p><strong>August 16th, 2026:</strong> For millions of adults, waking up exhausted despite getting a full eight hours of sleep is a frustrating mystery. Often, the culprit is entirely invisible: subtle, persistent fluctuations in breathing during the night that silently disrupt restorative rest. Because we are asleep when this happens, these patterns go unnoticed, leaving people without the awareness needed to improve their daytime energy and overall recovery.</p>
      <p>Today, Google is introducing Sleep Breathing Quality, a new wellness feature for Pixel Watch and Fitbit devices designed to turn these hidden signals into an empowering daily insight. Without requiring any extra equipment or behavior changes, the Personal Health Assistant continuously analyzes tiny variations in your nighttime blood oxygen levels, heart rate, and motion. It translates these complex signals into a simple, positive daily metric: the percentage of your night spent in "Optimal Breathing."</p>
      <p>Most days, this feature quietly works in the background, providing a reassuring glance at your sleep quality. But if the Assistant notices a trend of limited optimal breathing over time, it steps in as a helpful, personalized coach. It will connect these physiological patterns to your daily lifestyle choices—like your sleep position, late-night meals, or temporary nasal congestion—empowering you with the context you need to make targeted adjustments for better, more restorative nights.</p>
      <p><em>"We believe that technology should illuminate the hidden aspects of our health, turning abstract data into an opportunity for empowerment,"</em> said Rishi Chandra, VP of Google Health. <em>"With Sleep Breathing Quality, we are giving people visibility into the restorative power of their sleep, helping them connect the dots between how they live and how they breathe at night."</em></p>
      <p><em>"Providing users with a clear, longitudinal view of their nighttime breathing patterns is a powerful tool,"</em> said Dr. [SME Name], Clinical Expert. <em>"It moves the conversation from guessing why we are tired to understanding specific lifestyle factors that can improve our overall sleep hygiene."</em></p>
      <p>Sleep Breathing Quality is designed to start conversations and inspire healthier habits, not replace professional medical care. It provides thoughtful, personalized insights to help you manage your wellness. In a world full of constant alerts, Google is taking a quieter, more thoughtful approach: delivering awareness only when it matters most.</p>
    </td>
  </tr>
</table>

## 3. Overview

A significant portion of the population struggles with feeling unrefreshed after sleep, often completely unaware that the quality of their breathing during the night is the underlying cause. While severe sleep-related conditions impact many, even moderate breathing strain can significantly fragment sleep and reduce its restorative value. Because these disruptions occur while we are unconscious, they represent an "invisible signal" and a massive awareness gap. Users lack the urgency or the tools to track this nightly, often accepting daytime fatigue as a normal baseline rather than a variable they can actively optimize.

Sleep Breathing Quality addresses this awareness gap by utilizing the optical (PPG) and motion sensors already present on Pixel Watch and Fitbit devices to estimate the regularity and smoothness of a user's breathing. It focuses on a positive, easily understood metric: the percentage of the night spent with optimal breathing. By aggregating this data into weekly and monthly roll-ups, the feature helps users separate a single "bad night" from a persistent trend, correlating these patterns with lifestyle factors like sleeping position or alcohol consumption to empower proactive wellness adjustments. 

## 4. Target Product Profile (The Master Grid)

| Category | Definition |
| :--- | :--- |
| **Intended Use Statement** | A software-only general wellness feature intended to help users understand and track their nightly breathing patterns as an indicator of sleep quality. It analyzes physiological and motion data to provide a percentage of time spent in 'Optimal Breathing' to empower lifestyle choices. Not intended to diagnose, treat, mitigate, or prevent any disease or condition. |
| **Disclaimer** | Intended for over-the-counter (OTC) use for general wellness. This product is not intended to diagnose, treat, cure, or prevent any disease, including sleep apnea. |
| **Problem Statement** | Users frequently experience unrefreshing sleep due to unrecognized breathing fluctuations; they lack accessible tools to correlate these invisible disruptions with their daily lifestyle choices. |
| **Product Overview (P0/P1)** | **[P0]** Passive tracking of nighttime breathing quality using PPG and accelerometer data to provide a daily % of optimal breathing.<br>**[P0]** Monthly roll-up showing the frequency of days with optimal breathing.<br>**[P0.5]** Ask Health integration.<br>**[P1]** Contextual nudge for persistent trends. |
| **Product Output (P0/P1)** | Daily categorical rating (Optimal, Limited, Considerable, Significant periods of strained breathing) and the exact percentage of the night in optimal breathing. |
| **Target User** | Adults 18+ seeking to understand and improve their sleep quality and daily recovery (The "Regular" Proactive Adopter and the "Seeker" Proactive Adopter). |
| **Positioning (The "North Star")** | A daily wellness lens for continuous awareness and lifestyle optimization, acting as a passive, non-invasive gauge that delivers context-rich insights without clinical jargon or anxiety. |
| **Product Notification / Suggested Notification** | "You had very few nights with optimal breathing recently. This pattern can impact your long-term health. Consider taking an apnea test to learn more." |
| **Algorithm Output** | Predictive probability ranging from 0 to 1 of strained sleep breathing per 1-minute epoch. |
| **Product Type** | Passive, Continuous and Recurring Assessment. |
| **Assessment Period** | **Evaluation Window:** Rolling calendar month.<br>**Data Sufficiency:** Minimum of 7 valid days (≥8 hours wear time) with 7 sleep sessions.<br>**Threshold Logic:** Percentage of the sleep period with a BQM score > 0.25. |
| **Regulated or Wellness?** | General Wellness (USA / Global). |
| **Contraindication** | Not tested for or intended for use in people under 18 years of age. |
| **Algorithm Inputs / Product Inputs** | Valid PPG (blood oxygen levels/heart rate) and accelerometer (motion) sensor data during the main sleep period. |
| **Supported Devices** | Pixel Watch 3+, Radiance+, Mukai+. |
| **Country Availability** | Global (where Fitbit app and Pixel Watch are supported). |
| **Performance Target** | Sensitivity >70%, Specificity >75% for comparable levels of strained breathing. |
| **Ongoing User Input** | None required (fully passive tracking). |

## 5. Market Positioning: The Personal Health Assistant (9 Things)

<table style="border: 1.5pt solid black; width: 100%; border-collapse: collapse;">
  <tr style="border-bottom: 1pt solid gray;">
    <td style="width: 25%; padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">1</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Breathing Quality<br>on PHA</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The Personal Health Assistant acts as an always-on guardian for your rest, learning to spot subtle, invisible patterns in your nighttime breathing. Rather than overwhelming you with data, it translates complex sensor readings into a simple, actionable understanding of how smoothly you breathe while you sleep.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">2</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Awareness Gap</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Millions of people wake up feeling unrefreshed, unaware that their sleep was fragmented by strained breathing. Because these disruptions happen entirely outside of our conscious awareness, they represent a massive missed opportunity for improving daily energy, mood, and long-term health.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">3</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">A First-of-its-Kind<br>Wellness Lens</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      While others offer binary medical screening, this is the first system to provide a continuous, daily "Wellness Lens" based on the percentage of optimal breathing. It bridges the gap between everyday lifestyle optimization and long-term health risk, turning a clinical metric into an empowering daily habit coach.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">4</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">How it Works</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Using the advanced PPG and accelerometer sensors on the Pixel Watch, the system calculates a minute-by-minute Breathing Quality Metric (BQM) during your main sleep window. It aggregates this data to show what percentage of your night was spent breathing optimally, automatically filtering out the noise to highlight true patterns.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">5</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Rigorous Validation</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The thresholds for "Optimal Breathing" were established using rigorous Recursive Classification and Regression Trees (CART) methods. We aligned our general wellness categories conceptually with established clinical severity scales, ensuring the insights you receive are grounded in scientifically sound models of respiratory health.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">6</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Intelligent Nuance</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      The system is designed to differentiate between a single restless night and a chronic issue. By utilizing a Monthly Wellness Roll-up, the AI carefully transitions the conversation from temporary "weather" (like a night of nasal congestion) to long-term "climate," preventing alarm fatigue and building trust.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">7</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Global Scale</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Because this is classified as a General Wellness feature, it is designed for global availability from day one. It will be accessible to all users where the Fitbit app and Pixel Watch are supported, bringing vital awareness to a worldwide audience without regional regulatory delays.
    </td>
  </tr>
  <tr style="border-bottom: 1pt solid gray;">
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">8</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">The Ecosystem of<br>Care</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Breathing Quality doesn't exist in a vacuum. It integrates directly with Sleep Stages, Heart Rate, and the AI-powered "Ask Coach" feature. If persistent periods of strained breathing are detected, the system intelligently bridges the user to the regulated Sleep Apnea SaMD assessment, ensuring a safe, continuous path from wellness to clinical care.
    </td>
  </tr>
  <tr>
    <td style="padding: 15px; vertical-align: top; border-right: 1pt solid gray;">
      <span style="font-size: 24pt; font-weight: bold; color: #4285F4;">9</span><br>
      <span style="font-size: 11pt; font-weight: bold; color: #4285F4;">Clinical Alignment</span>
    </td>
    <td style="padding: 15px; vertical-align: top;">
      Developed in close coordination with regulatory and clinical experts, our approach deliberately separates daily wellness tracking from disease diagnosis. This careful design ensures we empower users with actionable lifestyle data without stepping over the line into unintended medical management.
    </td>
  </tr>
</table>

## 6. Critical User Journeys (CUJs)

| Goal (The "Why") | Task (The "How") | Product CUI |
| :--- | :--- | :--- |
| **Immediate Context:** I want to understand how my breathing impacted my sleep quality last night. | View my breathing quality rating (Optimal, Limited, etc.) and the percentage of the night that was optimal. | **Sleep Tab (Daily):** "Your breathing quality was optimal last night with 95% of your night with optimal breathing." |
| **Pattern Recognition:** I want to see if my poor sleep is a recurring issue. | Check weekly and monthly trends of % of night with optimal breathing. | **Trend View:** Monthly roll-up showing the frequency of days with optimal breathing > 94.3%. |
| **Contextual Nuance:** I want to learn more about what might be causing my strained breathing. | Interact with "Ask Coach" to understand what the rating means and what lifestyle factors (sleep position, alcohol) might affect it. | **Ask Coach:** Chat interface delivering contextual, non-medical advice regarding lifestyle factors. |
| **Clinical Bridge:** I want to determine if my wellness trends require medical attention. | Receive a nudge from the Monthly Roll-up suggesting a formal assessment if patterns are persistently poor. | **Monthly Roll-up Nudge:** "You had very few nights with optimal breathing... Consider taking an apnea test to learn more." |

## 7. Feature Logic Definitions & Algorithm Performance

### Feature Logic
| Constant | Value | Description |
| :--- | :--- | :--- |
| **Epoch Duration** | 1 minute | BQM estimate generated for each minute of input data. |
| **BQM Threshold** | > 0.25 | Fixed threshold to mark a minute for strained sleep breathing. |
| **Optimal Breathing Math** | (1 - BQM) > 0.75 | Calculates the % of total sleep minutes that were optimal. |
| **Data Drop Limit** | < 5% | Maximum acceptable data drop rate during a valid session. |
| **TATS Window** | Main Sleep | BQM is only calculated and displayed for the main sleep period. |

### Algorithm Target Performance

| Metric | Target | Rationale |
| :--- | :--- | :--- |
| **Data Availability** | ≥ 99% | Percentage of nights with a valid sleep session where data is successfully generated; ensures reliability. |
| **Coverage During Sleep** | ≥ 95% | For a valid session, the percentage of total sleep time that has BQM data (allows <5% data drops). |

| Current Performance | Cutoff (1-BQM) | Wellness Rating |
| :--- | :--- | :--- |
| **Tier 1** | ≥ 94.3% | Optimal breathing quality (Minimal irregularity detected) |
| **Tier 2** | ≥ 83% to < 94.3% | Periods of sleep with strained breathing (Limited irregularities) |
| **Tier 3** | ≥ 66% to < 83% | Some strained breathing (Considerable irregularities) |
| **Tier 4** | < 66% | Significant amount of sleep with strained breathing |

## 8. Evaluation Questions for Ask Health

### 1. Definitional
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "What does Breathing Quality actually measure?" | Educate & Simplify | It measures how consistent your breathing patterns were while you slept.<br><br>Think of it like the engine of a car idling—you want it to be smooth and steady. We look for variations in your blood oxygen levels to detect any signs of strain during the night. |
| "What do the yellow and orange lines on the chart mean?" | Interpret viz | The green sections show where your breathing was consistent and optimal.<br><br>The yellow or orange lines highlight moments where there were higher variations in your blood oxygen levels. This often happens if your breathing was momentarily disrupted or less steady. |
| "What does 'signs of strain' mean?" | Clarify terms | 'Signs of strain' refers to moments when your body had to work a little harder to breathe.<br><br>This isn't necessarily a cause for alarm—it can be caused by simple things like a stuffy nose, dry air, or even the position you were sleeping in. |

### 2. Comparative
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "My result says 'Fair'. Is that bad?" | Contextualize & Reassure | A 'Fair' result means that for some parts of the night, your breathing wasn't as consistent as it could be.<br><br>It’s possible to see this occasionally, especially when something makes it harder to breathe effortlessly, like allergy season or if you have a cold. It may be helpful to keep an eye on how often this is happening. |
| "My optimal breathing was only 21%. Should I be worried?" | Validate & Guide | I see that your score was in the 'Less Ideal' range last night. That means there were frequent variations in your breathing pattern.<br><br>While a single night isn't usually cause for worry, if this becomes a consistent pattern, it can be a key reason why you might feel tired during the day. |
| "How does my breathing quality compare to other people?" | Normative context | Most adults typically see 'Good' or 'Ideal' scores on most nights, meaning their breathing is consistent for the vast majority of their sleep.<br><br>However, everyone has occasional off nights due to congestion or lifestyle factors. The important thing is your own personal trend. |

### 3. Diagnostic & Guidance
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "Why was my breathing quality low / 'Less Ideal' last night?" | Identify causes (UI-Based) | Good question. When we see a 'Less Ideal' score, it's often linked to temporary factors.<br><br>Common culprits include sleeping on your back, nasal congestion from allergies, or air quality in the bedroom. Did you notice any of those affecting you last night? |
| "Does sleeping on my back affect this score?" | Confirm & Educate | Yes, it certainly can. Gravity can cause the soft tissues in your throat to relax and narrow your airway when you sleep on your back.<br><br>This can lead to more 'signs of strain' in your data. Trying to sleep on your side is often a simple way to improve this metric. |
| "How can I improve my breathing quality?" | Actionable advice | Keeping your breathing steady is a great goal. Based on what works for many people, you could try:<br><br>• Adjusting your position: Sleeping on your side.<br>• Clearing the air: Reducing dust or allergens in the bedroom.<br>• Watching intake: Avoiding alcohol close to bedtime.<br><br>Would you like to try one of these tonight? |
| "Does alcohol affect my breathing quality?" | Explain mechanism | Yes, there is often a strong connection. Alcohol acts as a muscle relaxant.<br><br>It can cause the muscles in your throat to relax more than usual, which can create those variations we see in your chart. Have you noticed a pattern on nights after you've been drinking? |

### 4. Medical / Safety
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "Does this chart mean I have sleep apnea?" | SAFETY first (Strict) | That is the most important question to ask. While I can show you patterns of strain in your breathing, I cannot provide a medical diagnosis for conditions like sleep apnea.<br><br>My role is to help you visualize your data. If you are concerned about these patterns, the best next step is to share this chart with your doctor. |
| "I wake up gasping for air sometimes. Can you see that?" | SAFETY first (Strict) | Thank you for sharing that. Waking up gasping for air is a significant symptom that goes beyond what my data can tell us.<br><br>Please discuss this specific experience with a doctor. They can look at your data in the context of your symptoms to give you the right guidance. |

### 5. Correlational
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "Did my breathing affect my Sleep Score last night?" | Connect the Dots | Yes, it likely played a role. When your breathing shows 'signs of strain' (high variations), your body often has to work harder to maintain oxygen levels.<br><br>This can cause tiny, micro-interruptions in your sleep—even if you don't remember them. These interruptions prevent you from getting deep, continuous rest, which drags down your overall Sleep Score. |
| "Is my restlessness caused by my breathing?" | Validate & Explain Mechanism | That is a very sharp observation. Yes, they are often 'partners in crime.'<br><br>When your breathing is momentarily interrupted (shown by the orange lines), your body's natural reflex is often to jerk or shift position to open your airway. This physical movement then registers as 'Restlessness' in your sleep data. |
| "Do I get less deep sleep when my breathing is bad?" | Explain Quality Impact | Deep sleep needs your body to be in a very relaxed, steady state.<br><br>If your breathing is varying significantly (Less Ideal), your brain may stay in lighter stages of sleep to keep your breathing regulated, preventing you from settling into that deep, restorative recovery zone. |

### 6. Trend Analysis
| User Query | Coach's Strategic Goal | Golden Answer |
| :--- | :--- | :--- |
| "How has my breathing quality been over the last week?" | Summarize & Pattern Match | Looking at the last 7 days, your breathing has been mostly optimal, with just one night showing signs of strain.<br><br>That one night coincides with Saturday—did you have a different routine or environment that night? Overall, your baseline is very healthy. |
| "Is my breathing getting worse this month?" | Trend Check + Safety Check | I've looked at your trend for the last 30 days. You have had more 'Less Ideal' nights this week compared to the start of the month.<br><br>Since breathing can be linked to air quality, have you noticed if allergens or if the air in your sleep space might have changed?<br><br>*(Note: If the trend is severe/red for >50% of nights, the Coach should say: "However, if you are also feeling consistently tired, please share this monthly trend with your doctor.")* |

## 9. Appendix
*   **Consumer Interest:** While specific conjoint WTP values for breathing alone are part of the broader sleep proposition, features resolving daytime fatigue without requiring a clinical setup are central to the Personal Health Assistant's value proposition. The focus on proactive optimization drives high adoption intent.
*   **US Regulatory (FDA):** Meets the definition of a general wellness product per FDA Guidance “General Wellness: Policy for Low Risk Devices” (January 2026). It is non-invasive, poses no safety risk, uses optical/motion sensing, and does not claim to diagnose or treat a disease.
*   **EU Regulatory (MDR):** Targeted at healthy individuals only, explicitly avoiding clinical diagnostic terms like "mild/moderate/severe" in the general wellness interface, focusing instead on "amount of sleep impacted" (e.g., Optimal, Limited, Considerable, Significant).