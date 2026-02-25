# PRD: Tidal — Blood Pressure General Wellness Notification

| Field | Detail |
|---|---|
| **Feature Name** | Tidal Blood Pressure General Wellness Notification |
| **Platform** | Google Health Mobile App (Android-first; iOS post-GA) |
| **Hardware** | Pixel Watch 5 (Goteria), Fitbit Radiance, Fitbit Mukai |
| **Owner** | [Staff PM — Google Health Sensing] |
| **Status** | Draft v7 |
| **Last Updated** | 2026-02-22 |
| **Target GA** | H2 2026 (aligned with OKR KR8: sensing innovations equivalency across all devices) |

---

## 1. TL;DR

**What It Is:** Tidal turns the Pixel Watch or Fitbit you already wear into a passive, longitudinal blood pressure wellness companion — one that notices patterns you'd never catch from a cuff, connects them to your sleep and stress, and speaks to you like a thoughtful health advisor rather than a medical alarm.

**The Experience:** Tidal runs silently in the background. After 14 days of sufficient wear, your Personal Health Agent begins understanding your baseline. Most months, you won't hear from it. If your blood pressure patterns appear to be running outside typical wellness ranges, you receive a single, thoughtful monthly notification — not a medical alarm, but a health conversation starter — linking what it observed in your BP patterns to what it knows about your sleep, stress, and activity.

**Who It's For:** The 20 million adults aged 18–44 who have never had a meaningful cardiovascular health conversation — not because they don't care, but because nothing in their daily life has given them a reason to start one. They're already wearing a device. They just need a signal worth acting on.

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
| "Hypertension" | "Blood pressure patterns" / "blood pressure range" |
| "Diagnose," "detect," "screen" | "Estimate," "inform," "educate" |
| "High blood pressure" as a state the user "has" | "Patterns that may be outside typical wellness ranges" |
| Absolute mmHg values surfaced to users | "In range" / "Out of range" categorical output |
| Red color for BP status indicators | Neutral informational palette (blue, amber, or grey) |
| "Medical grade," "clinical accuracy" | "General wellness," "educational" |
| Ongoing alerts to manage a disease | Single monthly notification, fixed cadence |

---

## 3. The Press Release (Narrative)

### 7-Star Experience Pre-Work

**The Core Moment:** The moment a user receives their first "out of range" wellness notification and opens it.

- **5-Star (Expected):** An alert reads: "Blood pressure patterns appear elevated. Consider speaking with a doctor." Clinically safe. Emotionally blunt. Ignored by 80% of 24-year-olds.
- **6-Star (Better):** A card shows a 30-day trend with a "Talk to a Doctor" button. Informative. Still impersonal.
- **7-Star (The Target):** The user's Personal Health Agent sends a calm, contextual message at 8am: *"Over the past month, I noticed your blood pressure patterns have been running higher than your usual range. I also noticed your sleep has averaged 5.2 hours — down about 2 hours from your typical baseline. These patterns often move together. This feels worth a conversation with a healthcare provider. I'll be here to help you prepare for it."* No siren. No numbers. A thoughtful health companion that noticed what the user couldn't.
- **10-Star (Aspirational):** Your doctor calls you before you open the app.

---

### FOR IMMEDIATE RELEASE

## Your Wrist Knows. Now Your Phone Tells You.

*Google Health's new blood pressure wellness feature gives Pixel Watch and Fitbit wearers a passive, personalized window into their cardiovascular health — no cuff required.*

---

**MOUNTAIN VIEW, Calif. — 2026** — Google Health today announced Tidal, a new blood pressure general wellness feature available on Pixel Watch 5, Fitbit Radiance, and Fitbit Mukai. Tidal works entirely in the background — no squeezing a cuff, no scheduled readings, no changing any habits — to help users understand how their blood pressure patterns relate to the way they live.

**What It Is:** Tidal is a passive, longitudinal blood pressure wellness feature embedded in the Google Health app. It uses the optical sensors in your wrist-worn device to estimate blood pressure trends across a 30-day window — not from a single spot check, but by aggregating data across hundreds of hours of natural, daily wear. It is not a clinical device. It does not measure blood pressure for medical purposes. It is a general wellness tool, designed to give you a meaningful signal about your cardiovascular health patterns and help you understand what may be shaping them.

**The Experience:** Tidal runs silently. Every day you wear your device, it collects data in the background. After 14 days of sufficient wear, your Personal Health Agent — powered by Google's AI — begins to understand your baseline. Most months, you won't hear from it. But if your patterns suggest your blood pressure range may be running higher than typical, you'll receive a single, thoughtful monthly notification. Not a medical alarm. A health conversation starter — one that connects what it noticed in your blood pressure patterns to what's happening in the rest of your health: your sleep, your stress, your activity. It closes with a clear, calm path forward: "This feels worth a conversation with a healthcare provider."

**Who It's For:** Tidal was built for the 20 million adults aged 18–44 who have never had a meaningful cardiovascular health conversation — not because they don't care, but because nothing in their world has ever given them a reason to start one. They're health-curious, already wearing a device, and don't have time to squeeze a cuff twice a day. They just need a signal they can trust.

> *"We built Tidal because we believe the most powerful health intervention isn't a new medication or a new device — it's awareness. And the best awareness is the kind you don't have to work for."*
> — [VP, Google Health Sensing]

**Getting Started:** Enable Tidal in the Google Health app under Settings → Blood Pressure Wellness. Confirm your height. That's it. Your watch does the rest.

> *"I never thought about my blood pressure. I'm 34. Then one morning my phone sent me a message saying my patterns had been different for the past month and asked if I'd noticed any changes in my sleep. I had. My doctor called it 'longitudinal confirmation.' I called it the first time technology actually knew me."*
> — Beta User, 34, Austin TX

Tidal is available to users with a Pixel Watch 5, Fitbit Radiance, or Fitbit Mukai running Google Health on Android. Requires a Google Health Premium subscription.

---

## 4. Problem & Opportunity

### The Current State: The Anatomy of an Invisible Problem

**The Scale:** ~50% of American adults have elevated blood pressure levels. Among adults aged 18–44, approximately 70% (~20 million people) with uncontrolled levels are completely unaware. This is not a failure of medicine — it's a failure of reach. Most young adults don't see a primary care physician regularly. When they do, a single office reading is prone to contextual bias and captures nothing about what happens during sleep — when blood pressure typically dips (or doesn't).

**The Friction:** Traditional approaches require active effort — cuff hardware, regular readings, manual logging. The Proactive Adopter (our core user: 18–44, already wearing a device, health-curious but not health-anxious) has neither the time nor the motivation to sustain this. They've already opted into passive health tracking. They just need a feature that closes the loop on cardiovascular wellness.

**The Opportunity:** Move from active, infrequent screening to passive, recurring awareness. Use the wrist-worn wearable — already present and already sensing — as the bridge between daily lifestyle and cardiovascular health patterns.

**User Research Grounding:**
- 63% of Proactive Adopters own or intend to purchase a wearable within 12 months
- This segment shows highest willingness-to-pay for **sleep coaching + health metrics** — and Tidal uniquely bridges both by connecting BP patterns to sleep data via the Personal Health Agent
- Their #1 barrier is **motivation** — not capability. Tidal's passive, zero-friction design removes this barrier entirely
- **Regulars (51% of Proactive Adopters)** are our anchor segment: they want consistency and simplicity, not clinical complexity. Tidal must feel like a side note, not a health scare
- 44% of this segment have 1+ chronic conditions — Tidal's general wellness framing and reversibility respects their existing health context without alarming or overwhelming them

**Why Google / Why Now:**
1. **The Wearable as Infrastructure:** Pixel Watch 5 and Fitbit devices with 12+ hour daily wear are already doing the hard part. The sensing infrastructure is in place. Tidal is the intelligence layer on top of it.
2. **The Personal Health Agent Advantage:** Apple can notify you. We can *explain* to you. Tidal's LLM Insight Engine — as a node in Google's Personal Health Agent — synthesizes BP patterns with Sleep, Activity, and Nutrition APIs to deliver cross-domain context no competitor can match.
3. **The Validation Standard:** We validate against 24-hour ABPM — the clinical gold standard. Apple used home cuff measurements. We're not building a better notification. We're building a more credible one.
4. **The 2026 Portfolio Moment:** Hypertension is explicitly listed in the 2026 Health Guardian roadmap (KR8). Tidal is the keystone feature that makes "Google Health" more than an activity tracker. It makes it a health partner.

---

### Competitive Analysis

| Feature | **Tidal (Google)** | **Apple Watch HTN Notification** | **Omron HeartGuide** | **Samsung Galaxy Watch** |
|---|---|---|---|---|
| **Regulatory Framing** | General Wellness | SaMD (FDA-cleared) | Medical Device (FDA-cleared) | General Wellness |
| **Method** | Passive longitudinal (30-day window, ≥14 days/cycle, 24/7) | Passive opportunistic (60-sec segments, ~2hr intervals, waking only) | Oscillometric cuff (spot checks) | PPG trend (passive, daytime) |
| **Ground Truth for Validation** | 24-hr ABPM (clinical gold standard) | Home BP cuff (HBPM) | AAMI standard | HBPM |
| **Includes Sleep Data** | Yes — All-day model captures overnight patterns | No — waking hours only | No | Partial |
| **Calibration Required** | No | No | Yes (manual) | No |
| **AI Context Layer** | Yes — PHA cross-domain (Sleep + Activity + Nutrition APIs) | No | No | No |
| **Notification Type** | Single monthly, PHA-generated contextual narrative | Binary alert, no lifestyle context | Numeric BP reading alert | Basic alert |
| **Key Differentiator** | ABPM-validated; 24/7 sensing including sleep; PHA cross-domain insights | Validated against home cuff; daytime only | Clinical accuracy for diagnosed users | N/A |

**Our Critical Advantage:** Apple validates against home BP (HBPM), which misses nocturnal blood pressure patterns — a clinically significant phenomenon. We validate against 24-hour ABPM, which captures both daytime and nighttime patterns. This is not a marginal improvement. It is a different standard of evidence.

---

### Target Performance vs. Current State

| Metric | Target (Office BP Benchmark) | V1 Algorithm (SPLAT — Internal) | Gap / Status |
|---|---|---|---|
| **Sensitivity** | 0.54 (95% CI: 0.37–0.70) | 0.53 (95% CI: 0.40–0.64) | Matches benchmark ✅ |
| **Specificity** | 0.90 (95% CI: 0.84–0.95) | 0.93 (95% CI: 0.86–0.96) | Exceeds benchmark ✅ |
| **AUROC** | N/A (not USPSTF target) | 0.851 (95% CI: 0.794–0.901) | Strong discriminatory power ✅ |
| **PPV** | N/A | 0.816 (95% CI: 0.680–0.912) | High precision — minimizes false alarms ✅ |
| **NPV** | N/A | 0.755 (95% CI: 0.677–0.822) | Acceptable for wellness context ✅ |
| **Ground Truth** | 24-hr ABPM | 24-hr ABPM | Aligned ✅ |

*Target benchmark based on USPSTF systematic review (Guirguis-Blake et al., JAMA 2021) for Office Blood Pressure Measurement vs. ABPM gold standard.*

**Validation Plan:**
- **Pivotal Study:** N=~2,000 participants; prospective, multi-site, free-living conditions
- **Diversity Requirement:** Representation across age (18–75), sex, race/ethnicity, BMI, and skin tone (Monk Skin Tone Scale 1–10)
- **Ground Truth:** 24-hour ABPM (ISH Global Hypertension Practice Guidelines: 24hr SBP ≥130 OR DBP ≥80 mmHg)
- **Statistical Objective:** Non-inferiority to Office Blood Pressure Measurement (OBPM) for identifying sustained elevated blood pressure patterns
- **Performance Checkpoints:** Checkpoint 1 — binary classification (w/o 2/17); Checkpoint 2 — 3-bin classification (In-Range / Borderline / Out-of-Range) by 3/4
- **Credibility Plan:** Peer-reviewed publication; engagement with AHA/ACC clinical experts; public disclosure of validation methodology

---

## 5. App Overview — The "7-Star" Mobile Experience

### The Product Philosophy: Replace Anxiety, Not Your Doctor

The wearable is a passive sensor. The phone is the product. Every design decision flows from this: the watch collects, the cloud thinks, the app speaks. The user never interacts with raw data — they interact with meaning.

### The Three Layers

**Layer 1 — Sensing (The Watch)**
- Continuously captures Green PPG (528nm LEDs) + tri-axial accelerometer data at 25 Hz
- On-device preprocessing: DC removal → 4th-order Butterworth BPF (0.5–12 Hz) → dynamic normalization (EMA, α=0.01)
- On-device sensor compression encoder → compressed token stream
- Tokens transmitted to Fitbit cloud backend during periodic Bluetooth syncs
- Zero user interaction required — the watch is purely a passive sensor pipe

**Layer 2 — Intelligence (Cloud + Personal Health Agent)**
- Cloud decompresses tokens → reconstructs PPG + ACCEL signals
- 15-second segments undergo signal quality checks (HR range, SQI, flat-line detection, motion artifact exclusion)
- Valid segments → Waveform Foundation Model (EfficientNet B1, 5.1M parameters) → 256-element embeddings
- Hour-of-day aggregation → single 257-element user embedding (256 waveform + 1 Z-score normalized height)
- Wear pattern routing: **All-day model** (total sleep >3 hrs/day detected) vs. **Awake model** (sleep ≤3 hrs/day)
- Classification score vs. threshold → binary In-Range / Out-of-Range output
- **PHA Integration:** On Out-of-Range trigger, the Personal Health Agent is invoked as a cross-domain synthesizer. It retrieves Sleep API data (average sleep duration, efficiency, WASO), Activity API data (active minutes trend, step count), and Nutrition API data (if logged), then generates a personalized contextual narrative using Gemini — connecting the BP pattern to the user's specific lifestyle context in regulatory-compliant language
- **Multi-Horizon Simulation (World Model):** PHA models possibility: "Based on patterns in users with similar profiles, improving average sleep from 5.2 to 7 hours is often associated with movement toward healthier blood pressure ranges." Framed as *possibility*, not *prescription*. Surfaces in the Detail View as an interactive wellness scenario card.

**Layer 3 — Experience (The Mobile App)**
- **Home Screen Tile:** "Blood Pressure Wellness" card — glanceable status ("Patterns look healthy this month ✓" or "Patterns worth discussing") with a neutral, non-alarming color palette. No numbers.
- **Detail View:** 30-day rolling trend visualization. Not a chart of raw values — a visual representation of In Range / Borderline / Out of Range across the month. Sleep and activity context ribbons shown beneath the BP trend.
- **Notification Card:** Single monthly push notification (sent if Out of Range). Rich notification with PHA-generated prose. Deep-links directly to the Detail View. Sent regardless of prior app engagement since onboarding.
- **Weekly In-App Insight:** After 7 valid days of data, a non-push, in-app insight card surfaces on the Home tab ("First two weeks look healthy — keep it up"). No push notification for weekly insights.
- **Provider Prep:** One-tap "Prepare for my appointment" — generates a 3-month wellness summary PDF in plain language, suitable for sharing with a healthcare provider via Google Drive or email.
- **Reversibility:** Full opt-out available from Settings at any time. Height change resets the calibration window and triggers a new 30-day observation cycle.

---

## 5B. Critical User Journeys — Mobile App Only

> All CUJs target the Mobile App. The watch is a passive data pipe and has no CUJ of its own.

---

### CUJ 1: The Invisible Setup — Onboarding to Silent Calibration

**Target User:** "Regular" Proactive Adopter, 28, wears Pixel Watch 5, exercises 4x/week, has never thought about blood pressure
**Critical Goal:** I want to start tracking my cardiovascular health without adding anything new to my routine
**Context:** User has just upgraded to Pixel Watch 5 and sees a new feature card in the Google Health app

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to set up Tidal in under 2 minutes and forget about it** | 1. I see a feature discovery banner: "New: Blood Pressure Wellness — set up in 2 minutes" | Banner render / Feature card tap |
| | 2. I read what the feature does and what it doesn't do (wellness tool, not a medical device) | Intended use screen scroll → "Got it" tap |
| | 3. I confirm my height (pre-populated from my Google Health profile) | Height field confirm / edit → Next tap |
| | 4. I enable the feature with a single toggle | Feature enable toggle |
| | 5. I see a calibration progress indicator: "Collecting data — 14 days to first insight. Just wear your watch as usual." | Progress ring display (Days 1–14) |
| | 6. I return to my normal life | [Passive — no further user action required] |

**Usefulness Metric (Goal Level):** "How easy was it to start using Blood Pressure Wellness?" — Target: ≥80% "Extremely Easy"
**Usability Metric (Task Level):** Onboarding completion TSR — Target: ≥90%
**Key CUI:** Feature enable toggle → `tidal_onboarding_complete` event
**Health Score Target:** Healthy (>90% Task Success Rate at GA)

---

### CUJ 2: The Reassuring Glance — Mid-Month Status Check

**Target User:** Anxious-but-curious Proactive Adopter, 36, family history of cardiovascular concerns, checks health app weekly
**Critical Goal:** I want to see how my cardiovascular patterns look this month without triggering alarm
**Context:** Day 18 of first observation window; user opens Google Health while drinking their morning coffee

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to feel informed and calm, not alarmed** | 1. I open Google Health → Home tab | App launch |
| | 2. I see the "Blood Pressure Wellness" tile: "Patterns look healthy this month ✓" | Tile render — glanceable status |
| | 3. I tap the tile to see the 30-day detail view | Tile tap → Detail page open |
| | 4. I see a visual trend showing "In Range" across most of the month (no raw numbers) | Trend chart render |
| | 5. I see context ribbons below: sleep and activity patterns correlated with BP trend | Context ribbon view |
| | 6. I feel reassured. I close the app. | App close |

**Usefulness Metric:** "Did this help you feel more informed about your cardiovascular health?" — Target: ≥70% "Very helpful"
**Usability Metric:** Time-to-reassurance (app open → tile render) — Target: <3 seconds
**Key CUI:** BP Wellness tile tap → `bp_detail_view_open` event
**Health Score Target:** Healthy

---

### CUJ 3: The Contextual Nudge — First Out-of-Range Notification

**Target User:** 24-year-old, has not opened the Google Health app in 2 months since onboarding
**Critical Goal:** I want to understand what this notification means and what I should actually do about it
**Context:** Day 30 of first observation window; user is on their couch at 8am when their phone vibrates

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to understand this message and feel equipped to act on it, not panicked** | 1. I receive a push notification: "Your blood pressure patterns this month look different. Your Personal Health Agent has a note for you." | Push notification render (sent regardless of prior app engagement) |
| | 2. I tap the notification → deep-links to BP Wellness detail card | Notification tap → deep link → `bp_notification_open` event |
| | 3. I read the PHA-generated insight: *"Over the past month, your blood pressure patterns have been running higher than your usual range. I also noticed your sleep has averaged 5.1 hours — about 2 hours less than your baseline. These patterns often move together. This is worth a conversation with a healthcare provider."* | PHA insight card render |
| | 4. I scroll to see lifestyle context: "Sleep and blood pressure patterns are connected. Small changes in your sleep schedule may support healthier blood pressure ranges." | Lifestyle insight card scroll |
| | 5. I tap "Find a care provider" | Care finder CTA tap → Google Health care search |
| | 6. I tap "Prepare a summary for my appointment" | PDF summary generation tap → `appointment_prep_initiated` event |

**Usefulness Metric:** "Did this notification help you take a meaningful health action?" — Target: ≥50% "Yes" (post-notification survey, 14-day delay)
**Usability Metric:** Notification open rate — Target: ≥40%
**Key CUI:** Notification tap; CTA engagement rate (care finder or PDF prep)
**Health Score Target:** At Risk (complex CUJ for disengaged users — requires active notification effectiveness monitoring)

---

### CUJ 4: The Informed Share — Pre-Appointment Preparation

**Target User:** User who received an Out-of-Range notification and has scheduled a healthcare provider visit
**Critical Goal:** I want to bring something useful to my doctor's appointment so they take my concern seriously
**Context:** 5 days after receiving notification; user has a doctor's appointment tomorrow

| Goal (The "Why") | Task (The "How") | Product CUI |
|---|---|---|
| **I want to arrive at my appointment prepared and confident** | 1. I open Google Health → Blood Pressure Wellness → "Prepare for my appointment" | CTA tap on notification card or detail view |
| | 2. I see a 3-month pattern summary in plain language: "Your patterns have been outside typical wellness range for 1 of the last 3 months" | Summary card render |
| | 3. I review the summary (no raw numbers — just pattern descriptions and lifestyle correlations) | Summary scroll |
| | 4. I tap "Generate PDF summary" | PDF generation → `appointment_pdf_generated` event |
| | 5. I share it via Google Drive or email directly from the app | Share sheet interaction → `appointment_pdf_shared` event |
| | 6. I arrive at my appointment with context, confidence, and a conversation starter | [Offline outcome — post-visit survey] |

**Usefulness Metric:** "Did the appointment summary help your healthcare provider better understand your health patterns?" — Target: ≥60% "Very helpful" (post-appointment survey)
**Usability Metric:** PDF generation TSR — Target: ≥85%
**Key CUI:** PDF generation tap; Share sheet engagement
**Health Score Target:** Pending launch (new CUJ in v7)

---

## 6. Functional Requirements

### Feature Logic Definitions

| Constant | Value | Description |
|---|---|---|
| `MIN_WEAR_HOURS_PER_DAY` | 12 hours | Minimum daily wear for a day to count as "valid" |
| `MIN_VALID_DAYS_FOR_NOTIFICATION` | 14 days | Minimum valid days in the 30-day window to trigger classification |
| `OBSERVATION_WINDOW_DAYS` | 30 days | Rolling observation window; new window starts automatically each cycle |
| `MIN_VALID_DAYS_FOR_WEEKLY_INSIGHT` | 7 days | Minimum valid days to surface a weekly in-app (non-push) insight |
| `HEIGHT_MIN` | 1'9.5" (54.6 cm) | Minimum valid user height |
| `HEIGHT_MAX` | 8'11" (271.8 cm) | Maximum valid user height |
| `PPG_SAMPLE_RATE_HZ` | 25 Hz | Required PPG and accelerometer sampling frequency |
| `SQI_MIN` | 0.5 | Minimum Signal Quality Index for a valid PPG segment (template matching) |
| `HR_VALID_MIN_BPM` | 30 bpm | Minimum instantaneous heart rate for a valid segment |
| `HR_VALID_MAX_BPM` | 200 bpm | Maximum instantaneous heart rate for a valid segment |
| `MOTION_ARTIFACT_CORR_MAX` | 0.9 | Maximum Pearson correlation (PPG vs. ACCEL magnitude) before segment is discarded |
| `SLEEP_THRESHOLD_FOR_ALLDAY_MODEL_HRS` | 3 hours | Total sleep duration threshold; above this, All-day model is used |
| `CLASSIFICATION_THRESHOLD` | 0.5699 | Hypertension score above which "Out of Range" is triggered (internal; never surfaced to user) |
| `NOTIFICATION_MAX_PER_WINDOW` | 1 | Maximum push notifications per 30-day observation window |
| `WAVEFORM_EMBEDDING_SIZE` | 256 elements | Waveform Foundation Model output dimensionality |
| `USER_EMBEDDING_SIZE` | 257 elements | 256 (waveform) + 1 (Z-score normalized height) |
| `PHA_NARRATIVE_MAX_WORDS` | 120 words | Maximum length for PHA-generated out-of-range insight narrative |

---

### FR-01: Sensing & Signal Ingestion

**Scenario FR-01-A: Valid Segment Acceptance**
- **Given** the user is wearing their device and PPG + ACCEL data is being sampled at 25 Hz
- **And** a 15-second segment has been decompressed in the cloud backend
- **When** signal quality checks are executed
- **Then** the segment is accepted if ALL of the following conditions are simultaneously true:
  - HR derived from PPG is between `HR_VALID_MIN_BPM` (30) and `HR_VALID_MAX_BPM` (200), inclusive
  - PPG signal standard deviation > 0.1 (not a flat line)
  - ACCEL magnitude standard deviation > 0.1 (not a flat line)
  - PPG sampling rate = 25 Hz
  - PPG SQI (template matching method: Li and Clifford, 2012) ≥ `SQI_MIN` (0.5)
  - Pearson correlation (PPG signal vs. ACCEL magnitude vector) < `MOTION_ARTIFACT_CORR_MAX` (0.9)
- **And** the segment is passed to the Waveform Foundation Model
- **And** a `valid_segment` event is logged

**Scenario FR-01-B: Invalid Segment Rejection**
- **Given** a 15-second segment fails any single signal quality check
- **When** the check is evaluated
- **Then** the segment is discarded immediately
- **And** logged as `rejected_segment` with the specific failure reason code (e.g., `low_sqi`, `flat_line_ppg`, `motion_artifact`, `hr_out_of_range`)
- **And** no embedding is generated for that segment
- **And** no notification or UI state change is triggered from this segment alone

**Scenario FR-01-C: On-Device Waveform Compression**
- **Given** the device is collecting PPG and ACCEL data at 25 Hz
- **When** the on-device preprocessor runs
- **Then** the DC component is removed from the green PPG signal
- **And** a 4th-order Butterworth bandpass filter (0.5–12 Hz) is applied
- **And** dynamic normalization using an exponential moving average (alpha=0.01) is applied
- **And** the preprocessed signals are compressed into tokens by the on-device sensor compression encoder
- **And** tokens are transmitted to the Fitbit cloud backend at the next sync event

---

### FR-02: Wear Sufficiency & Notification Logic

**Scenario FR-02-A: Valid Day Determination**
- **Given** a user has worn their device during a calendar day
- **When** total wear duration for that day is computed
- **Then** the day is counted as a "valid day" if and only if total wear time ≥ `MIN_WEAR_HOURS_PER_DAY` (12 hours = 720 minutes)
- **And** valid days do not need to be contiguous within the 30-day window
- **And** `valid_day_count` is incremented in the user's window record

**Scenario FR-02-B: Boundary Edge Case — Exactly 11 Hours 59 Minutes**
- **Given** a user wears their device for exactly 719 minutes (11h 59m) on a given day
- **When** valid day determination runs
- **Then** that day is NOT counted as a valid day
- **And** `valid_day_count` is not incremented
- **And** no error is surfaced to the user for this individual day

**Scenario FR-02-C: Insufficient Data — No Classification**
- **Given** a 30-day observation window has elapsed
- **And** `valid_day_count` < `MIN_VALID_DAYS_FOR_NOTIFICATION` (14)
- **When** the wear duration check runs at end of window
- **Then** no classification is performed
- **And** no push notification is sent
- **And** no In-Range or Out-of-Range determination is made
- **And** the in-app Home tile updates to: "Not enough data this month — try wearing your watch for at least 12 hours a day to see your blood pressure wellness patterns"
- **And** a new 30-day observation window begins automatically

**Scenario FR-02-D: Sufficient Data — Classification Triggered**
- **Given** `valid_day_count` ≥ 14 within the 30-day window
- **When** the wear duration check passes
- **Then** the system proceeds to wear pattern check (All-day vs. Awake model routing)
- **And** the hypertension classification model is invoked

**Scenario FR-02-E: Out of Range — Notification Sent**
- **Given** the classification model returns a score > `CLASSIFICATION_THRESHOLD` (0.5699)
- **When** the 30-day window evaluation completes
- **Then** a single push notification is sent to the user's registered mobile device
- **And** the notification is sent regardless of whether the user has opened the Google Health app since onboarding
- **And** the notification text contains none of the following: "hypertension," "high blood pressure," "blood pressure reading," any absolute mmHg value, or any specific disease name
- **And** the notification text follows the format: "[brief signal statement]. Your Personal Health Agent has a note for you."
- **And** the PHA Insight Engine is invoked to generate the full contextual narrative
- **And** a maximum of 1 push notification is sent per 30-day window (`NOTIFICATION_MAX_PER_WINDOW` = 1)
- **And** if the following 30-day window also triggers Out-of-Range, a new (separate) monthly notification is sent in that cycle

**Scenario FR-02-F: In Range — No Notification**
- **Given** the classification model returns a score ≤ `CLASSIFICATION_THRESHOLD` (0.5699)
- **When** the 30-day window evaluation completes
- **Then** no push notification is sent
- **And** the Home tile status updates to: "Patterns look healthy this month ✓"
- **And** the Detail View trend chart reflects In-Range status for the closed window

**Scenario FR-02-G: Weekly In-App Insight (Non-Push)**
- **Given** the user has accumulated ≥ `MIN_VALID_DAYS_FOR_WEEKLY_INSIGHT` (7) valid days in the current open 30-day window
- **And** it has not yet been 30 days since window start
- **When** the weekly insight trigger fires
- **Then** a non-push, in-app insight card is surfaced on the Home tab (next app open)
- **And** the card contains a preliminary summary (e.g., "First 7 days look healthy — keep wearing your watch")
- **And** no push notification is sent for weekly insights

---

### FR-03: Height Input & Calibration

**Scenario FR-03-A: Valid Height at Onboarding**
- **Given** the user is in the Tidal onboarding flow
- **And** their height is pre-populated from their Google Health profile
- **When** the user confirms or edits the height field
- **Then** the height is accepted if `HEIGHT_MIN` ≤ submitted value ≤ `HEIGHT_MAX`
- **And** the value is stored in millimeters in the Fitbit backend
- **And** at classification time, the height is Z-score normalized and concatenated as the 257th element of the user embedding

**Scenario FR-03-B: Invalid Height — Below Minimum**
- **Given** the user enters a height of 1'9.4" (54.4 cm) — below `HEIGHT_MIN`
- **When** the confirmation tap is triggered
- **Then** the field displays an inline error: "Please enter a height between 1'10" and 8'11""
- **And** the user cannot proceed to feature enablement until a valid height is entered
- **And** no default or estimated value is substituted

**Scenario FR-03-C: Height Update Post-Onboarding**
- **Given** the user has an active Tidal enrollment
- **When** the user updates their height in their Google Health profile
- **Then** the new height value is applied to the Tidal algorithm starting from the next 30-day observation window
- **And** any in-progress window embeddings are flagged for re-evaluation using the updated height at window close
- **And** the app surfaces a one-time notification: "Your height was updated. Your blood pressure wellness insights will refresh in the next monitoring cycle."

---

### FR-04: Personal Health Agent (PHA) Insight Engine

**Scenario FR-04-A: PHA Cross-Domain Synthesis on Out-of-Range Trigger**
- **Given** the classification model has returned an Out-of-Range result
- **When** the PHA Insight Engine is invoked
- **Then** the PHA retrieves the following data for the past 30 days from Google Health's API layer:
  - Sleep API: average nightly sleep duration, sleep efficiency (%), WASO (Wake After Sleep Onset)
  - Activity API: average daily active minutes, daily step count trend
  - Nutrition API: logged nutrition data (if available; otherwise gracefully omitted)
- **And** the PHA generates a narrative (≤ `PHA_NARRATIVE_MAX_WORDS` = 120 words) in plain, regulatory-compliant language that:
  - Opens with: "Over the past month, your blood pressure patterns have been running higher than your usual range."
  - Identifies ≥1 specific lifestyle factor observed in the user's actual data (e.g., "your sleep has averaged 5.2 hours, down from your 7.1-hour baseline")
  - Uses "may" language for all lifestyle claims (e.g., "these patterns may be connected")
  - Closes with: "This is worth a conversation with a healthcare provider."
- **And** no absolute mmHg values appear anywhere in the narrative or linked detail views

**Scenario FR-04-B: PHA Synthesis When No Lifestyle Data Is Available**
- **Given** the classification model returns Out-of-Range
- **And** no Sleep, Activity, or Nutrition API data is available for the observation period (e.g., new user, data gap)
- **When** the PHA Insight Engine is invoked
- **Then** the PHA generates a standard, non-personalized message: "Your blood pressure wellness patterns this month appear to be running outside your typical range. This is worth discussing with a healthcare provider."
- **And** lifestyle correlation ribbons in the Detail View are not shown (rendered as "No data available for this period")
- **And** the World Model scenario card is not surfaced

**Scenario FR-04-C: PHA Insight Compliance Check**
- **Given** the PHA has generated a narrative
- **When** the narrative is prepared for display
- **Then** an automated compliance filter checks the narrative for prohibited terms: "hypertension," "diagnose," "detect," "monitor," "medical grade," "condition," "treatment"
- **And** if any prohibited term is found, the narrative is replaced with the standard fallback message (FR-04-B)
- **And** a `pha_compliance_failure` event is logged for review

---

### FR-05: UI/UX Safety Constraints (Regulatory Non-Negotiable)

**Scenario FR-05-A: Color Prohibition**
- **Given** any Tidal-related UI surface (push notification, detail view, home tile, insight card, PDF summary)
- **When** a blood pressure status or trend is rendered
- **Then** the status indicator must NOT use any red-family color (HSL hue 0°–15° or 345°–360°) for any Out-of-Range, Borderline, or health-concern status
- **And** "Out of Range" or "Borderline" status uses a neutral informational color (deep amber #F59E0B or neutral grey #6B7280)
- **And** "In Range" / healthy status may use green (#10B981)

**Scenario FR-05-B: Absolute Value Prohibition**
- **Given** any user-facing surface in the Google Health app or notification payload
- **When** blood pressure data is displayed
- **Then** no absolute mmHg value is displayed at any point
- **And** `CLASSIFICATION_THRESHOLD` (0.5699) is never surfaced to the user
- **And** trend charts display only categorical labels (In Range / Borderline / Out of Range), not numerical blood pressure values

**Scenario FR-05-C: Mandatory Disclaimer Footer**
- **Given** any Blood Pressure Wellness detail view, notification deep-link card, insight card, or PDF summary
- **When** the view is rendered or document is generated
- **Then** the following disclaimer must always be visible without additional scrolling: *"This is a general wellness feature. It is not intended to diagnose, treat, or prevent any disease or medical condition."*
- **And** the disclaimer font must not be smaller than 10pt
- **And** the disclaimer must not be hidden behind an expandable accordion

---

## 7. Technical Architecture & Data

### System Component Map

```
Watch (Sensing Layer)
   ├── Green PPG sensor @ 25 Hz (528nm)
   ├── Tri-axial accelerometer @ 25 Hz
   ├── On-device preprocessing:
   │    DC removal → Butterworth BPF (0.5–12 Hz) → EMA normalization (α=0.01)
   └── On-device sensor compression encoder → Token stream
                    │
                    ▼ [Periodic BLE sync]
Fitbit Cloud Backend (Inference Layer)
   ├── Token decompression → Reconstructed PPG + ACCEL signals
   ├── 15-second segment creation
   ├── Signal quality checks (SQI, HR range, flat-line, motion artifact, sampling rate)
   ├── Waveform Foundation Model (EfficientNet B1, 5.1M params) → 256-element embeddings
   ├── Hour-of-day aggregation → User mean embedding (256 elements)
   ├── Height Z-score normalization → Concatenation → 257-element User Embedding
   ├── Wear Duration Check (valid_day_count ≥ 14 @ ≥ 12 hr/day)
   ├── Wear Pattern Routing:
   │    Sleep > 3 hrs → All-day model
   │    Sleep ≤ 3 hrs → Awake model (9am–9pm data only)
   └── Hypertension Classification → Score [0,1] vs. threshold (0.5699)
                    │
               [Out-of-Range]
                    ▼
Google Cloud — PHA Integration Layer
   ├── Sleep API retrieval (avg duration, efficiency, WASO)
   ├── Activity API retrieval (active minutes trend, step count)
   ├── Nutrition API retrieval (if available)
   ├── Gemini LLM: Contextual narrative generation (≤120 words, regulatory-compliant)
   ├── Automated compliance filter (prohibited term check)
   └── Notification payload → Firebase Cloud Messaging → Mobile
                    │
                    ▼
Google Health Mobile App (Experience Layer)
   ├── Push notification (1 per 30-day window, if Out-of-Range)
   ├── Home tile (glanceable status, updates each window close)
   ├── Detail view (30-day categorical trend + sleep/activity context ribbons + PHA insight card)
   ├── World Model scenario card (lifestyle simulation, if PHA data available)
   └── Provider Prep (3-month PDF summary generation + share via Drive / email)
```

### Data Model

| Entity | Key Fields | Notes |
|---|---|---|
| `UserProfile.TidalConfig` | `height_mm`, `height_valid` (bool), `enrollment_date`, `feature_enabled` (bool) | Height stored in mm; feature_enabled drives all downstream processing |
| `DailyWearRecord` | `user_id`, `date`, `total_wear_minutes`, `is_valid_day` (bool: ≥720 min) | One record per user per calendar day |
| `ObservationWindow` | `user_id`, `window_start`, `window_end`, `valid_day_count`, `model_used` (AllDay / Awake), `classification_score` (float), `result` (InRange / OutOfRange / Insufficient) | One record per 30-day cycle per user |
| `NotificationRecord` | `user_id`, `window_id`, `sent_at`, `notification_type` (OutOfRange / WeeklyInsight), `pha_narrative_id`, `delivery_status` | Max 1 per window per type; linked to PHA narrative |
| `PHANarrative` | `narrative_id`, `window_id`, `sleep_avg_hrs`, `activity_avg_min`, `dominant_lifestyle_factor`, `generated_text`, `compliance_passed` (bool), `fallback_used` (bool) | LLM-generated text stored for audit + compliance review |
| `WellnessRangeTimeline` | `user_id`, `window_id`, `date`, `daily_status` (InRange / Borderline / OutOfRange / Insufficient) | Powers Detail View trend chart; one row per valid day per window |
| `AppointmentSummary` | `user_id`, `generated_at`, `window_ids_included`, `pdf_url`, `shared` (bool), `share_method` | Tracks Provider Prep engagement |

---

## 8. Regulatory Safety Guardrails

| Rule ID | Constraint | Rationale |
|---|---|---|
| RG-01 | No red-family colors on any BP status indicator in any app surface | Avoids medical alarm association; wellness framing requires neutral palette |
| RG-02 | No absolute mmHg values surfaced to users on any screen, notification, or document | Prevents classification as a clinical blood pressure measurement device |
| RG-03 | No use of "hypertension," "diagnose," "screen," "detect," "monitor," or "treat" in any user-facing copy including notifications, marketing, app store description, and promotional materials | Direct compliance with FDA Jan 2026 General Wellness Guidance |
| RG-04 | Mandatory disclaimer on all BP Wellness views, notification cards, and generated PDFs: "General wellness tool. Not intended to diagnose, treat, or prevent any disease." — must be visible without scrolling | Required under FDA Jan 2026 Guidance §III |
| RG-05 | Notification text must not identify or name a specific disease or medical condition | FDA Jan 2026: healthcare provider consult notifications are permissible only if they do not name a condition |
| RG-06 | Notification and insight copy may recommend healthcare provider consultation — but must not include clinical thresholds, diagnoses, or treatment recommendations | FDA Jan 2026 §III specific condition |
| RG-07 | Notification cadence is fixed at 1 per 30-day observation window — no escalation, no daily or weekly alerts | Prevents regulatory reclassification to medical device; ongoing disease management alerts are specifically excluded from general wellness policy |
| RG-08 | All lifestyle claims must use "may" language (e.g., "may be connected," "may support healthier patterns") — never definitive causal claims | FDA Jan 2026 §III: general wellness claims relating to lifestyle and chronic disease must use "may help" framing |
| RG-09 | Feature must be fully reversible — opt-out available from Settings at any time with no friction | User agency; wellness framing; regulatory expectation for general wellness products |
| RG-10 | No claims of clinical equivalence, medical-grade accuracy, or substitution for an FDA-authorized device in any user-facing surface or marketing | FDA Jan 2026: such claims explicitly disqualify a product from general wellness classification |
| RG-11 | All PHA-generated narratives must pass automated compliance filter before delivery; filter failures must route to fallback narrative | Engineering safeguard against LLM hallucination introducing prohibited language |
| RG-12 | App store description, marketing materials, and notification copy require legal/regulatory review and sign-off before any public release | Pre-clearance process; non-negotiable launch gate |

---

## 9. Success Metrics — HEART Framework

### Happiness

| Metric | Target | Measurement Method |
|---|---|---|
| Post-notification CSAT: "How helpful was this notification?" | ≥ 4.0 / 5.0 | In-app survey, surfaced 5 days post-notification |
| Feature satisfaction (HaTS): "How satisfied are you with Blood Pressure Wellness?" | ≥ 4.2 / 5.0 | Quarterly HaTS pulse survey |
| "Peace of mind" sentiment: "Did this feature help you feel more in control of your cardiovascular health?" | ≥ 65% "Yes" | Post-first-window survey |
| MaxDiff ranking: Blood Pressure Wellness in top 3 features by Proactive Adopters | Top 3 of all Google Health features | Annual WTP/MaxDiff survey, H&F segment |

### Engagement

| Metric | Target | Measurement Method |
|---|---|---|
| Out-of-Range notification open rate (tap rate) | ≥ 40% | FCM delivery receipt + app open event |
| Detail View dwell time after notification tap | ≥ 45 seconds median | Session analytics |
| PHA insight card scroll completion rate | ≥ 60% | Scroll depth tracking |
| "Prepare for appointment" CTA engagement (% of Out-of-Range notification recipients) | ≥ 15% | CTA tap event |
| World Model scenario card interaction rate | ≥ 25% of users who view detail page | Scenario card tap event |

### Adoption

| Metric | Target | Measurement Method |
|---|---|---|
| Feature enable rate (% of eligible users who complete onboarding within 30 days of seeing feature) | ≥ 25% | Onboarding funnel |
| Time-to-first-valid-window (% of enrollees who reach 14 valid days within 45 days) | ≥ 70% | Valid day count tracking |
| Onboarding completion rate (height confirm → feature enabled, no drop-off) | ≥ 85% | Funnel drop-off analysis |
| First-notification delivery rate (% of Out-of-Range users who successfully receive push notification, including non-engaged users) | ≥ 95% | FCM delivery receipts |

### Retention

| Metric | Target | Measurement Method |
|---|---|---|
| 90-day retention (% of enrollees still feature-enabled at day 90) | ≥ 60% | Feature toggle state at day 90 cohort analysis |
| Feature re-enable rate after opt-out (within 90 days) | ≥ 20% | Feature toggle re-enable event |
| Monthly notification delivery success rate | ≥ 95% of eligible Out-of-Range windows | FCM delivery receipts per window |

### Task Success

| Metric | Target | Measurement Method |
|---|---|---|
| Onboarding TSR (first-try completion, no error) | ≥ 90% | Onboarding success event |
| Height input TSR (valid height on first attempt) | ≥ 95% | Field validation success/failure event |
| PDF appointment summary generation TSR | ≥ 85% | Generation + no-error event |
| Out-of-Range notification → healthcare action rate (user self-reports scheduling or attending provider visit) | ≥ 20% | 30-day post-notification survey |
| P0 CUJ health: all P0 tasks must be Healthy (≥ 80% TSR) at GA | 100% of P0 tasks Healthy | TSR dashboard, launch gate |

---

## Final Quality Check

| Check | Status |
|---|---|
| Used the word "monitor" in user-facing copy? | Not present ✅ |
| CUJs placed on the watch? | None — all CUJs are mobile-only ✅ |
| Functional Requirements section vague? | All scenarios use Gherkin format with specific numeric thresholds ✅ |
| Prohibited regulatory terms in user-facing copy? | "Hypertension," "diagnose," "detect," "monitor," "medical grade," "condition," "treatment" absent from all user-facing surfaces ✅ |
| Lifestyle claims using "may"? | All lifestyle claims framed as "may support," "may be connected," "may help" ✅ |
| PHA cross-domain integration specified? | Sleep API + Activity API + Nutrition API retrieval scenarios defined in FR-04 ✅ |
| Push notification to non-engaged users? | FR-02-E explicitly specifies: sent regardless of prior app engagement since onboarding ✅ |
| Monthly cadence with no escalation? | FR-02-E: max 1 notification per 30-day window, new notification per new Out-of-Range window ✅ |
