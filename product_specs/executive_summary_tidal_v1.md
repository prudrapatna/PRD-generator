# Tidal: Blood Pressure General Wellness
### Executive Summary — Google Health | February 2026 | Confidential

---

## The Opportunity

**20 million Americans aged 18–44 have uncontrolled blood pressure patterns they know nothing about.** Not because they don't care — because nothing in their daily life has ever given them a reason to check. Annual office visits are infrequent and miss what happens during sleep. Home cuffs require discipline no one sustains. And for a generation that already wears a device every day, this is not a hardware problem. It's an intelligence problem.

**Tidal solves it.** By transforming the Pixel Watch or Fitbit wearable into a passive, longitudinal blood pressure wellness feature — requiring zero behavior change, no cuffs, no logs — Tidal delivers the first meaningful cardiovascular awareness signal most of these users will ever receive. After 14 days of natural wear, Google's Personal Health Agent understands their blood pressure patterns well enough to know when something is worth a conversation. And when it is, it doesn't just alert. It *explains* — connecting blood pressure patterns to the sleep, activity, and lifestyle data that may be shaping them.

**What it is not:** A diagnostic tool. A blood pressure monitor. A substitute for clinical care. Tidal is a general wellness feature, calibrated to the FDA's January 2026 framework for non-invasive optical sensing, and designed to start conversations with healthcare providers — not replace them.

---

## Intended Use

> *"The Blood Pressure General Wellness Notification feature is a general wellness tool intended to estimate blood pressure values and trends for informational and educational purposes only. It is designed to promote positive lifestyle behavior changes in sleep, activity, nutrition, and stress management by educating users and helping them understand how their daily habits correlate with estimated blood pressure range. It is not intended to diagnose, treat, cure, or prevent any disease or medical condition."*

**Regulatory classification:** General Wellness Software Function (Non-Device) under 21st Century Cures Act §520(o)(1)(B) and FDA Jan 2026 General Wellness Guidance. Output type: categorical trends and ranges only — no absolute clinical values surfaced to users.

---

## Product Positioning: Beyond Detection

Most wearable blood pressure features answer one question: *Is something out of range?* Tidal is built to answer the harder question every user actually has: **Why?**

The sensing layer is the watch — passive, 24/7, including sleep, when blood pressure patterns are most clinically meaningful and most competitors go dark. The intelligence layer is Google's Personal Health Agent, operating as a cross-domain synthesizer: when blood pressure patterns fall outside wellness ranges, PHA retrieves the user's sleep quality, activity trends, and nutrition data to generate a contextual narrative — not a generic alert, but a personalized insight. *"Your patterns this month look different. Your sleep has averaged 5.1 hours — down from your 7.1-hour baseline. These patterns often move together. This is worth a conversation with a healthcare provider."*

This is the frontier: not just passive detection, but passive **comprehension.** FDA's January 2026 General Wellness guidance explicitly permits contextualizing wellness outputs "in relation to sleep, activity, stress, recovery, or similar wellness domains." Tidal is the first product to operationalize this at scale — using a foundation model trained on 500,000 hours of consented wrist sensor data, synthesized through Google's LLM infrastructure, delivered as a calm and credible health companion.

---

## Critical User Journeys

| CUJ | User Goal | Key Requirement |
|---|---|---|
| **The Invisible Setup** | Start tracking without changing any habit | Height confirm → single toggle → 14-day passive calibration. Zero friction. |
| **The Reassuring Glance** | Check status without alarm | Home tile renders categorical status ("Patterns look healthy") in <3s. No numbers. |
| **The Contextual Nudge** | Understand WHY patterns changed | Single monthly push notification (sent even if user hasn't opened app since onboarding); PHA narrative links BP pattern to ≥1 observed lifestyle factor. ≤120 words. |
| **The Informed Share** | Prepare for a healthcare provider visit | One-tap 3-month PDF summary in plain language; shareable via Drive or email. |

---

## Performance: Where We Are vs. Where We Need to Be

Validated against 24-hour Ambulatory Blood Pressure Monitoring (ABPM) — the clinical gold standard — on an independent test cohort of 196 participants across demographic subgroups.

| Metric | Target (Office BP Benchmark)* | Tidal V1 (SPLAT) | Status |
|---|---|---|---|
| **Sensitivity** | 0.54 (95% CI: 0.37–0.70) | **0.53** (95% CI: 0.40–0.64) | Matches benchmark ✅ |
| **Specificity** | 0.90 (95% CI: 0.84–0.95) | **0.93** (95% CI: 0.86–0.96) | Exceeds benchmark ✅ |
| **AUROC** | — | **0.851** (95% CI: 0.794–0.901) | Strong discriminatory power ✅ |
| **PPV** | — | **81.6%** (95% CI: 68.0–91.2%) | High precision; minimizes false alarms ✅ |

*\*Benchmark: USPSTF systematic review (Guirguis-Blake et al., JAMA 2021), Office BP vs. ABPM gold standard.*

**Pivotal validation plan:** N=~2,000 participants; prospective, multi-site, free-living; full demographic diversity (age, sex, race, Monk Skin Tone 1–10); ground truth = 24-hr ABPM. Statistical objective: non-inferiority to Office Blood Pressure Measurement. Publication and expert engagement planned.

---

## Competitive Analysis: Tidal vs. Apple Watch Hypertension Notification

Apple's feature, FDA-cleared as a Software Medical Device in 2025, establishes the competitive baseline. The table below shows why our approach is meaningfully different — on evidence rigor, clinical completeness, and the intelligence layer.

| Dimension | **Tidal (Google)** | **Apple Watch HTN Notification** |
|---|---|---|
| **Regulatory Framing** | General Wellness (Non-Device) | SaMD (FDA-cleared medical device) |
| **Validation Ground Truth** | **24-hr ABPM** (ambulatory, clinical gold standard — captures daytime + nocturnal BP) | **Home BP cuff (HBPM)** — twice-daily spot checks; misses nocturnal dipping, the most clinically meaningful signal |
| **Validation Sample Size** | Training N=663; Independent test N=**196** (held-out, demographically diverse) | N=2,229 enrolled; **N=1,863** in analysis set |
| **Sensitivity (Overall)** | **52.6%** (95% CI: 40.8–64.2%) | **41.2%** (95% CI: 37.2–45.3%) |
| **Specificity** | **92.5%** (95% CI: 86.2–96.5%) | **92.3%** (95% CI: 90.6–93.7%) |
| **Data Collection Window** | **24/7 including sleep** — All-day model captures nocturnal patterns | **Waking hours only** (~2-hr intervals; user must be still) — no nocturnal data |
| **Lifestyle Context Layer** | **PHA cross-domain synthesis** — Sleep, Activity, and Nutrition APIs; personalized narrative | None — binary alert, no lifestyle context |
| **Notification Intelligence** | PHA-generated contextual insight; links BP pattern to observed lifestyle factors | Standard alert: "Signs of high blood pressure detected" |
| **Calibration** | None required | None required |

**The critical distinction:** Apple validated against home BP measurements (HBPM), which averages twice-daily readings and misses nocturnal blood pressure — a clinically significant phenotype. Our validation uses 24-hour ABPM, the same gold standard used in peer-reviewed clinical literature and recommended by the International Society of Hypertension. Higher-quality ground truth means a more credible product. And with 12+ points of sensitivity advantage against a weaker standard, the gap in real-world clinical relevance is wider than the table suggests.

**Our moat is not just the algorithm. It is the only blood pressure wellness feature in the world that knows what you slept last night — and tells you why it matters.**

---

*Tidal | Google Health Confidential | For internal review only | Target GA: H2 2026*
