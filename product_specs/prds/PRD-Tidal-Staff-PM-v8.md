# PRD: Tidal — Blood Pressure General Wellness Notification

| Field | Detail |
|---|---|
| **Feature Name** | Tidal Blood Pressure General Wellness Notification |
| **Platform** | Google Health Mobile App (Android-first; iOS post-GA) |
| **Hardware** | Pixel Watch 5 (Goteria), Fitbit Radiance, Fitbit Mukai |
| **Owner** | [Staff PM — Google Health Sensing] |
| **Status** | Draft v8 |
| **Last Updated** | 2026-02-23 |
| **Target GA** | H2 2026 (aligned with OKR KR8: sensing innovations equivalency across all devices) |

---

## 1. TL;DR

**What It Is:** Tidal turns the Pixel Watch or Fitbit you already wear into a passive, longitudinal blood pressure wellness companion — one that notices health patterns you'd never catch from a spot-check, connects them to your sleep and stress, and speaks to you like a thoughtful health advisor to provide peace of mind.

**The Experience:** Tidal runs silently in the background. After 14 days of sufficient wear, your Personal Health Agent begins understanding your baseline. Most months, you won't hear from it. If your blood pressure patterns appear to be running outside typical wellness ranges, you receive a single, thoughtful monthly notification — an educational health conversation starter linking what it observed in your patterns to what it knows about your sleep, stress, and activity.

**Who It's For:** The 20 million adults aged 18–44 who are Proactive Adopters and have an opportunity to understand their cardiovascular patterns and optimize their wellness. They're already wearing a device. They just need an educational signal to empower their health journey.

---

## 2. Intended Use (Regulatory "North Star")

**Mandatory Statement (verbatim — to appear in all user-facing labeling, marketing, legal disclaimers, and app store copy):**

> *"The Blood Pressure General Wellness Notification feature is a general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range. The feature is intended to provide notifications when values fall outside of general wellness ranges to prompt users to reflect on their habits. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition."*

**Regulatory Classification:**
- **Classification:** General Wellness Software Function (Non-Device) under 21st Century Cures Act §520(o)(1)(B) and FDA Jan 2026 General Wellness Guidance
- **Risk Profile:** Low-risk, non-invasive optical sensing (PPG + Accelerometer)
- **FDA Guidance:** General Wellness: Policy for Low Risk Devices (updated Jan 6, 2026)
- **Output Type:** Trends, ranges, and longitudinal summaries — NOT absolute clinical BP values

**Regulatory Bright Lines:**

| Prohibited in User-Facing Copy | Required Terminology |
|---|---|
| "Hypertension," "Diagnose," "Detect" | "Health Patterns," "Estimate," "Inform," "Educate" |
| "High blood pressure," "Condition" | "Patterns that may be outside typical wellness ranges" |
| Absolute mmHg values surfaced to users | "In range" / "Out of range" categorical output |
| Red color for BP status indicators | Neutral informational palette (blue, amber, or grey) |
| "Medical grade," "Clinical accuracy" | "General wellness," "Educational" |
| Ongoing alerts to "monitor" or "treat" | Single monthly notification, fixed cadence for "peace of mind" |

---

## 3. The Press Release (Narrative)

### FOR IMMEDIATE RELEASE

## Your Wrist Knows. Now Your Phone Empowers You.

*Google Health's new blood pressure wellness feature gives Pixel Watch and Fitbit wearers a passive, personalized window into their cardiovascular health — offering true peace of mind.*

**MOUNTAIN VIEW, Calif. — 2026** — Google Health today announced Tidal, an educational blood pressure general wellness feature available on Pixel Watch 5, Fitbit Radiance, and Fitbit Mukai. Tidal works entirely in the background — no squeezing a cuff, no scheduled readings, no changing any habits — to help users understand how their health patterns relate to the way they live.

**What It Is:** Tidal is a passive, longitudinal general wellness feature embedded in the Google Health app. It uses the optical sensors in your wrist-worn device to estimate blood pressure trends across a 30-day window — not from a single spot check, but by aggregating data across hundreds of hours of natural, daily wear. It is an educational tool, designed to give you a meaningful signal about your cardiovascular health patterns and help you understand what may be shaping them.

**The Experience:** Tidal runs silently. Every day you wear your device, it collects data in the background. After 14 days of sufficient wear, your Personal Health Agent — powered by Google's AI — begins to understand your baseline. Most months, you won't hear from it, giving you peace of mind. But if your patterns suggest your blood pressure range may be running higher than typical, you'll receive a single, thoughtful monthly notification. Not an alarm. A health conversation starter — one that connects what it noticed in your health patterns to what's happening in the rest of your wellness: your sleep, your stress, your activity. It closes with a clear, calm path forward: "This feels worth a conversation with a healthcare provider."

**Who It's For:** Tidal was built for the 20 million Proactive Adopters aged 18–44 who have an immense opportunity to understand their cardiovascular patterns and optimize their wellness. They're health-curious, already wearing a device, and simply want an educational tool they can trust to give them visibility into their own health.

> *"We built Tidal because we believe the most powerful health intervention isn't a new prescription or a clinical test — it's empowerment through awareness. And the best awareness is the kind you don't have to work for."*
> — [VP, Google Health Sensing]

**Getting Started:** Enable Tidal in the Google Health app under Settings → Blood Pressure Wellness. Confirm your height. That's it. Your watch does the rest.

> *"I never thought about my blood pressure. I'm 34. Then one morning my phone sent me a message saying my patterns had been different for the past month and asked if I'd noticed any changes in my sleep. I had. I called it the first time technology actually partnered with me to optimize my wellbeing."*
> — Beta User, 34, Austin TX

Tidal is available to users with a Pixel Watch 5, Fitbit Radiance, or Fitbit Mukai running Google Health on Android. Requires a Google Health Premium subscription.

---

## 4. Problem & Opportunity

### The Current State: The Awareness Gap

**The Scale:** Approximately 20 million Proactive Adopters aged 18–44 have an untapped opportunity to understand their cardiovascular patterns. Most young adults don't see a primary care physician regularly, leading to an awareness gap. When they do, a single office reading is prone to contextual bias and captures nothing about what happens during sleep — when blood pressure typically dips (or doesn't).

**The Friction:** Traditional approaches require active effort — cuff hardware, regular readings, manual logging. The Proactive Adopter (our core user: 18–44, already wearing a device, health-curious) has neither the time nor the motivation to sustain this. They've already opted into passive health tracking. They just need a feature that closes the loop on cardiovascular wellness.

**The Opportunity:** Move from active, infrequent screening to passive, recurring awareness. Use the wrist-worn wearable — already present and already sensing — as the bridge between daily lifestyle and cardiovascular health patterns to empower the user.

**User Research Grounding:**
- 63% of Proactive Adopters own or intend to purchase a wearable within 12 months.
- This segment shows highest willingness-to-pay for **sleep coaching + health metrics** — and Tidal uniquely bridges both by connecting BP patterns to sleep data via the Personal Health Agent.
- Their #1 barrier is **motivation**. Tidal's passive, zero-friction design removes this barrier entirely.
- **Regulars (51% of Proactive Adopters)** are our anchor segment: they want consistency and simplicity. Tidal must feel like a side note, providing peace of mind.
- 44% of this segment have 1+ existing health considerations — Tidal's general wellness framing respects their context without overwhelming them.

**Why Google / Why Now:**
1. **The Wearable as Infrastructure:** Pixel Watch 5 and Fitbit devices with 8+ hour daily wear are already doing the hard part. 
2. **The Personal Health Agent Advantage:** We can use our LLM Insight Engine to act as a World Model, synthesizing BP patterns with Sleep, Activity, and Nutrition APIs to deliver multi-horizon simulations (e.g., "If I sleep more, my range may improve").
3. **The Validation Standard:** We validate against 24-hour ABPM — the clinical gold standard. 
4. **The 2026 Portfolio Moment:** Tidal is the keystone feature that makes "Google Health" a proactive health partner.

---

### Competitive Analysis

| Feature | **Tidal (Google)** | **Apple Watch Notifications** | **Omron HeartGuide** |
|---|---|---|---|
| **Regulatory Framing** | General Wellness | SaMD (FDA-cleared) | Medical Device |
| **Method** | Passive longitudinal (30-day window, ≥14 days/cycle) | Passive opportunistic (60-sec segments) | Oscillometric cuff |
| **Ground Truth for Validation**| 24-hr ABPM (clinical gold standard) | Home BP cuff (HBPM) | AAMI standard |
| **Includes Sleep Data** | Yes — All-day model captures overnight patterns | No — waking hours only | No |
| **Calibration Required** | No | No | Yes (manual) |
| **AI Context Layer** | Yes — PHA cross-domain (World Model) | No | No |

---

### Target Performance vs. Current State

| Metric | Target (Office BP Benchmark) | V1 Algorithm (SPLAT — Internal) | Gap / Status |
|---|---|---|---|
| **Sensitivity** | 0.54 (95% CI: 0.37–0.70) | 0.53 (95% CI: 0.40–0.64) | Matches benchmark ✅ |
| **Specificity** | 0.90 (95% CI: 0.84–0.95) | 0.93 (95% CI: 0.86–0.96) | Exceeds benchmark ✅ |
| **Ground Truth** | 24-hr ABPM | 24-hr ABPM | Aligned ✅ |

**Validation Plan:**
- **Pivotal Study:** N=1,600 participants; prospective, multi-site, free-living conditions.
- **Diversity Requirement:** Representation across age (18–75), sex, race/ethnicity, BMI, and skin tone.
- **Ground Truth:** 24-hour ABPM.
- **Statistical Objective:** Non-inferiority to Office Blood Pressure Measurement (OBPM) for estimating sustained elevated blood pressure patterns.

---

## 5. App Overview — The "7-Star" Mobile Experience

### The Product Philosophy: Replace Anxiety, Empower with Insight
The wearable is a passive sensor. The phone is the product. The user never interacts with raw data — they interact with meaning.

### The Three Layers

**Layer 1 — Sensing (The Watch)**
- Continuously captures Green PPG (528nm LEDs) + tri-axial accelerometer data at 25 Hz.
- Zero user interaction required — the watch is purely a passive sensor pipe.

**Layer 2 — Intelligence (Cloud + Personal Health Agent)**
- Cloud reconstructs PPG + ACCEL signals.
- Valid segments passed to Waveform Foundation Model to generate embeddings.
- Hour-of-day aggregation yields a single user embedding.
- **PHA Integration:** On Out-of-Range trigger, the Personal Health Agent is invoked as a cross-domain synthesizer.
- **World Model / Multi-Horizon Simulation:** The PHA models physiological outcomes as a cost function: "Based on patterns in users with similar profiles, improving average sleep from 5.2 to 7 hours is often associated with movement toward healthier blood pressure ranges." Framed as *possibility* to empower choice.

**Layer 3 — Experience (The Mobile App)**
- **Home Screen Tile:** Glanceable status ("Patterns look healthy this month ✓") providing peace of mind.
- **Detail View:** 30-day rolling trend visualization showing In Range / Borderline / Out of Range across the month. 
- **Notification Card:** Single monthly push notification with PHA-generated prose.
- **Weekly In-App Insight:** After 7 valid days, a non-push, in-app insight card surfaces on the Home tab.

---

## 5B. Critical User Journeys — Mobile App Only

> All CUJs target the Mobile App. The watch is a passive data pipe.

### CUJ 1: The Invisible Setup — Onboarding to Silent Calibration
*   **Target User:** Proactive Adopter, 28, wears Pixel Watch 5.
*   **Critical Goal:** I want to gain visibility into my cardiovascular health without adding anything new to my routine.
*   **Context:** User sees a new feature card in the Google Health app.

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to set up Tidal in under 2 minutes and forget about it** | 1. I see a discovery banner: "New: Blood Pressure Wellness" | Banner render / Feature card tap |
| | 2. I read what the feature does (educational wellness tool) | Intended use screen scroll → "Got it" |
| | 3. I confirm my height | Height field confirm / edit → Next tap |
| | 4. I enable the feature | Feature enable toggle |
| | 5. I see a progress indicator: "14 days to first insight" | Progress ring display |

**Usefulness Metric:** "How helpful was it to start using Blood Pressure Wellness?" — Target: ≥80% "Extremely Helpful"
**Usability Metric:** Onboarding completion TSR — Target: ≥90% (Healthy)

### CUJ 2: The Reassuring Glance — Mid-Month Status Check
*   **Target User:** Health-curious Proactive Adopter, 36.
*   **Critical Goal:** I want to check my health patterns to gain peace of mind.
*   **Context:** Day 18 of first observation window.

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to feel informed and empowered** | 1. I open Google Health → Home tab | App launch |
| | 2. I see the tile: "Patterns look healthy this month ✓" | Tile render |
| | 3. I tap the tile to see the 30-day detail view | Tile tap → Detail page open |
| | 4. I see a visual trend showing "In Range" (no numbers) | Trend chart render |

**Usefulness Metric:** "Did this help you feel more informed about your wellness?" — Target: ≥70% "Extremely helpful"
**Usability Metric:** Time-to-reassurance — Target: <3 seconds (Healthy)

### CUJ 3: The Contextual Nudge — First Out-of-Range Notification
*   **Target User:** 24-year-old, has not opened the app in 2 months.
*   **Critical Goal:** I want to understand what this notification means and how I can optimize my wellness.
*   **Context:** Day 30; user is at home when their phone vibrates.

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to understand this message and feel equipped to act** | 1. I receive a push notification: "Your health patterns this month look different." | Push notification render |
| | 2. I tap the notification | Notification tap → deep link |
| | 3. I read the PHA insight linking patterns to my sleep data | PHA insight card render |
| | 4. I see the World Model simulation on sleep improvements | Lifestyle insight card scroll |
| | 5. I tap "Find a care provider" | Care finder CTA tap |

**Usefulness Metric:** "Did this notification empower you to take action?" — Target: ≥50% "Yes"
**Usability Metric:** Notification open rate — Target: ≥40%

---

## 6. Functional Requirements

### Feature Logic Definitions

| Constant | Value | Description |
|---|---|---|
| `MIN_WEAR_HOURS_PER_DAY` | 8 hours | Minimum daily wear for a day to count as "valid" |
| `MIN_VALID_DAYS_FOR_NOTIFICATION` | 14 days | Minimum valid days in the 30-day window |
| `OBSERVATION_WINDOW_DAYS` | 30 days | Rolling observation window |
| `MIN_VALID_DAYS_FOR_WEEKLY_INSIGHT` | 7 days | Minimum valid days to surface a weekly in-app insight |
| `HEIGHT_MIN` | 1'9.5" (54.6 cm) | Minimum valid user height |
| `HEIGHT_MAX` | 8'11" (271.8 cm) | Maximum valid user height |
| `PPG_SAMPLE_RATE_HZ` | 25 Hz | Required PPG sampling frequency |
| `SQI_MIN` | 0.5 | Minimum Signal Quality Index for a valid PPG segment |

### FR-01: Sensing & Signal Ingestion
**Scenario 01: Valid Segment Acceptance**
*   **Given** the user is wearing their device and PPG + ACCEL data is sampled at 25 Hz
*   **And** a 15-second segment is decompressed in the cloud
*   **When** signal quality checks are executed
*   **Then** the segment is accepted IF: HR is 30–200 bpm, PPG std dev > 0.1, ACCEL std dev > 0.1, SQI ≥ 0.5, and Pearson correlation < 0.9.
*   **And** a `valid_segment` event is logged.

**Scenario 02: Invalid Segment Rejection**
*   **Given** a 15-second segment fails any single signal quality check
*   **When** the check is evaluated
*   **Then** the segment is discarded immediately and logged as `rejected_segment`.

### FR-02: Wear Sufficiency & Logic Core
**Scenario 03: Valid Day Determination**
*   **Given** a user has worn their device during a calendar day
*   **When** total wear duration for that day is computed
*   **Then** the day is counted as a "valid day" if total wear time ≥ `MIN_WEAR_HOURS_PER_DAY` (8 hours = 480 minutes).

**Scenario 04: Insufficient Data**
*   **Given** a 30-day observation window has elapsed
*   **And** `valid_day_count` < 14
*   **When** the wear duration check runs
*   **Then** no classification is performed and no push notification is sent.

**Scenario 05: Out of Range — Notification Sent**
*   **Given** `valid_day_count` ≥ 14 within the 30-day window
*   **And** the classification model returns a score > 0.5699
*   **When** the 30-day window evaluation completes
*   **Then** a single push notification is sent to the user's mobile device
*   **And** the notification text contains NO prohibited terms.

### FR-03: User Profile & Calibration
**Scenario 06: Height Update**
*   **Given** the user updates their height in their profile
*   **When** the new height is saved
*   **Then** the algorithm resets the calibration for the next 30-day window
*   **And** an in-app message states: "Your height was updated. Your wellness insights will refresh in the next cycle."

### FR-04: The LLM Insight Engine
**Scenario 07: PHA Cross-Domain Synthesis**
*   **Given** an Out-of-Range trigger
*   **When** the PHA Insight Engine is invoked
*   **Then** the PHA retrieves Sleep and Activity API data
*   **And** generates a narrative (≤ 120 words) using "may" language linking patterns to lifestyle.
*   **And** the narrative passes an automated filter checking for prohibited words ("diagnose," "condition," etc.). If it fails, a generic fallback message is used.

---

## 7. Technical Architecture & Data

### System Component Map
- **Watch (Ingest):** Green PPG sensor + Accelerometer → On-device preprocessing (DC removal, BPF) → Token stream via BLE.
- **Cloud (Inference/LLM):** Token decompression → 15s segments → Quality checks → Waveform Foundation Model → User embedding → Classification.
- **PHA Integration Layer:** Sleep/Activity API retrieval → Gemini LLM contextual narrative generation → Compliance filter.
- **Phone (Display):** Mobile app receives payload → Displays Home tile, Detail view, and World Model scenario card.

### Data Model
- `UserProfile.TidalConfig`: `height_mm`, `feature_enabled` (bool).
- `DailyWearRecord`: `user_id`, `date`, `total_wear_minutes`, `is_valid_day` (bool: ≥480 min).
- `ObservationWindow`: `window_start`, `window_end`, `valid_day_count`, `result` (InRange / OutOfRange / Insufficient).
- `PHANarrative`: `generated_text`, `compliance_passed` (bool), `fallback_used` (bool).

---

## 8. Regulatory Safety Guardrails

- **UI Constraints:** No red-family colors on any BP status indicator. Uses neutral colors (amber/grey) for "Out of Range" and green for "In Range."
- **Data Display:** No absolute mmHg values surfaced to users anywhere.
- **Copy Restrictions:** No use of "diagnose," "detect," "medical grade," "condition," "treatment," or "hypertension."
- **Disclaimer:** Mandatory footer: "General wellness tool. Not intended to diagnose, treat, cure, or prevent any disease."
- **Cadence:** Max 1 notification per 30-day window to maintain general wellness non-diagnostic intent.
- **Action Framing:** All claims regarding lifestyle outcomes must use "may help" or "may be connected."

---

## 9. Success Metrics — HEART Framework

- **Happiness:** Post-notification CSAT ≥ 4.0/5.0; "Peace of mind" sentiment ≥ 65% "Yes".
- **Engagement:** Out-of-Range notification open rate ≥ 40%; World Model scenario card interaction rate ≥ 25%.
- **Adoption:** Feature enable rate ≥ 25% of eligible users.
- **Retention:** 90-day retention ≥ 60%.
- **Task Success:** Onboarding TSR ≥ 90%; Height input TSR ≥ 95%.
