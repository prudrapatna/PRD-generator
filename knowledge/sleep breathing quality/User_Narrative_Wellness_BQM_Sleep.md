# User Narrative: Wellness BQM & Sleep Apnea SaMD

**Authors:** <add your name>

This framework defines how we communicate the relationship between daily sleep quality and long-term respiratory health. By separating daily wellness from periodic clinical screening, we provide a cohesive journey that balances lifestyle optimization with medical safety.

## The Two-Lens Approach
To help users understand their breathing data, we utilize two distinct features that look at the same raw data through different lenses:

1. **The Wellness Lens (BQM)**
Captures immediate fluctuations in breathing stability to help users connect their sleep quality with daily habits like sleeping position or lifestyle choices. It is designed for continuous awareness and lifestyle optimization.

2. **The Clinical Lens (SaMD)**
Identifies signs suggestive of moderate-to-severe sleep apnea for 2 days in a 10 day assessment window. It filters out daily "noise" to assess serious health risks that require professional medical attention.

**Why they coexist:** While the Wellness Lens helps users manage their sleep quality, the Clinical Lens provides a regulated safety net. Coexistence ensures that frequent wellness "symptoms" are automatically channeled into a clinically validated risk assessment when a threshold is met.

## The Bridge: Monthly Wellness Roll-up
The essential connection between these two is the Monthly Wellness Roll-up. By providing a weighted monthly breathing score that aggregates the intensity and frequency of poor breathing nights in a calendar month, we transition the conversation from "one bad night" to "a persistent trend." This prepares the user for the 4-month clinical check-in, making the SaMD result feel like a logical conclusion based on their own observed data.

## The Conversion Path: From Wellness to Apnea
To transition users from a wellness mindset to a clinical assessment without causing undue alarm, we follow a path of Increasing Evidence:

* **Awareness (The Roll-up):** The glanceable view of the weighted monthly breathing score (which uses a point system to aggregate the intensity of poor breathing nights) validates the user's lived experience (e.g., "I have been feeling tired"). A "pay attention" threshold is triggered if more than half of a person's nights are not characterized by optimal breathing.
* **Education (The Context):** We explain that while these disruptions impact daily "health" and "recovery," they are also the primary indicators used in our clinical Sleep Apnea screening.
* **Direct Call to Action (The Upsell):** For users in cleared regions who have not yet assessed for Apnea, the “frequency” glanceable view could include a specific prompt: "Since these disruptions are frequent, consider using Sleep Apnea Assessment to see if a medical follow-up is needed."
* **Activation (The SaMD Trigger):** If the user is already opted-in, the Roll-up serves as the "Pre-heat," informing them that their next scheduled 4-month assessment will prioritize this recent trend.

## Coordinated Messaging Strategy

| Feature Property | Sleep Breathing Quality (BQM) | Sleep Breathing Quality Monthly Roll-up | Sleep Apnea Assessment |
| --- | --- | --- | --- |
| **Trigger** | Every morning after sleep. | Once per month (weighted average score of daily ratings).<br><br>Terminology based on frequency/urgency:<br>- Often / Significant<br>- Sometimes / Modest<br>- Seldom | Initial Opt-in, User-initiated via Roll-up, or 4-month recurrence. |
| **Feature Category** | Wellness (Global) | Wellness (Global / The Bridge) | SaMD (Cleared Regions Only) |
| **User Narrative** | "Your breathing quality was Good with 85% of your night with optimal breathing." | "You had very few nights with optimal breathing. This pattern can impact your long-term health. Consider taking an apnea test to learn more." | "Signs suggestive of Moderate-to-Severe Sleep Apnea detected. Share this report with your doctor." |
| **Strategic Intent** | Provide immediate context for the previous night's rest. Focus on lifestyle factors. | Transition the user from daily "weather" to medium-term "climate." | Deliver a clinically validated risk assessment and medical call-to-action. |
| **User Mental Model** | "How did I sleep last night?" | "Is there a pattern I should notice?" | "Do I have a health risk I need to treat?" |
| **User Framing (Differentiation)** | Daily Feedback: A tool for immediate behavior change (e.g., changing position). | Pattern Recognition: A tool for acknowledging that disruptions are becoming a chronic health factor. | Clinical Validation: A tool for medical screening that transitions from self-tracking to professional care. |
| **Call to Action (CTA)** | "Try sleeping on your side." | "Assess your Sleep Apnea risk."<br><br>AND/OR<br>“Doctor Prep” | "Download PDF report for your doctor." |

## The Coexistence Logic
* **Wellness BQM (The "Symptoms"):** Documents individual instances of disrupted breathing without assigning a disease-state label.
* **The Monthly Roll-up (The "Frequency"):** Aggregates wellness data to show that disruptions aren't anomalies, but a recurring trend.
* **SaMD Assessment (The "Verdict"):** The regulated layer that interprets the frequency and severity of those disruptions through a clinical lens to identify specific risk.