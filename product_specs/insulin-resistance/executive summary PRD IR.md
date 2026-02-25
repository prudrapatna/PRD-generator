# Executive Summary: Metabolic Health — Insulin Resistance Level

## 1. The Vision
**Your Body’s Fuel Efficiency, Revealed.**
Insulin Resistance Level is a revolutionary, passive wellness feature that makes the "invisible" state of metabolic health visible. By leveraging the sensors on a user's wrist, it estimates their body's "Metabolic Efficiency"—how effectively cells absorb glucose—without a single finger prick or manual log.

**The Problem:** 40% of US adults (18-44) are insulin resistant but have zero awareness. Existing solutions are either too medical (CGMs) or too late (prediabetes diagnosis).
**The PHA Solution:** The Personal Health Agent (PHA) doesn't just alert users to a "High" status; it acts as a **Metabolic Partner**. It identifies *why* a user's level shifted—linking it to poor sleep, low activity, or high stress—and uses multi-horizon simulations to show how small lifestyle changes *may* restore metabolic resilience.

---

## 2. Intended Use & Positioning
**Intended Use:** A general wellness tool to estimate insulin resistance level and promote lifestyle changes in sleep, activity, and nutrition. It is **not** a diagnostic tool for diabetes and is **not** a substitute for medical advice.

**Positioning:** This is an **Early Warning System** for health-curious "Proactive Adopters." It pivots the conversation from "avoiding disease" to "optimizing efficiency."

---

## 3. Pushing the Frontier: PHA Integration
While competitors focus on raw data logging, Google leverages its **AI World Model** to:
1.  **Synthesize Across Domains:** Automatically correlates metabolic status with Sleep, Activity, and Stress APIs.
2.  **Narrative Coaching:** Replaces numeric scores with empathetic, LLM-generated insights: *"Your metabolic efficiency is lower this month. Improving your sleep by 15 minutes could be the key to turning this around."*
3.  **Future-State Simulation:** Models the impact of weight loss or activity increases on metabolic health, giving users a "cost function" for their daily choices.

---

## 4. Key Performance & Validation
Tidal's algorithm (SPLAT) outperforms traditional screening methods by focusing on **longitudinal stability** rather than spot-checks.

| Metric | Target | Current Performance |
| :--- | :--- | :--- |
| **Sensitivity** | 70% (@ HOMA-IR > 2.9) | **73%** |
| **Specificity** | 75% (@ HOMA-IR > 2.9) | **76%** |
| **Adj. Specificity** | 90% (@ HOMA-IR > 1.5) | **94%** |

**Validation:** Successfully validated in a 1P study (N=233). 3P validation is currently in progress to ensure performance across a broader wearable portfolio.

---

## 5. Critical User Journeys (CUJs)
1.  **Invisible Setup:** 2-minute onboarding (Eligibility check + Weight confirm) → 14-day silent calibration.
2.  **Monthly Coaching Moment:** If status is High, the PHA delivers a rich, contextual notification at the start of the new window.
3.  **Data Tiering:** Users can "level up" their prediction accuracy by connecting a CGM or sharing blood lab records (HbA1c/Triglycerides).

---

## 6. Regulatory & Safety Guardrails
- **Neutral Palette:** High status uses Amber/Yellow; Red is strictly prohibited.
- **Verbatim Disclaimer:** Visible on all screens to maintain non-diagnostic "General Wellness" status.
- **Language Filter:** Automated check to ensure no medical/diagnostic terms (e.g., "Screening," "Condition") are ever used in PHA narratives.
- **Fixed Cadence:** Notifications are limited to once per month to avoid the "active monitoring" classification.
