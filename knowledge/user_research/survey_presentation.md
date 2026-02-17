# Blood Pressure Monitoring: User Research Synthesis
Wellness vs. SaMD Strategy Recommendation
February 14, 2026

---

# 01
## Executive Summary
**DRIs:** User Research Team

---

# A "one-size-fits-all" solution risks alienating both core user groups

*   **The Split:** Our user base is sharply divided: **50% prefer a Wellness Approach** (Concept A) while **40% demand a Medical Device** (Concept B).
*   **The Tension:** The "Wellness" approach feels unsafe to medically serious users, while the "Medical" approach induces anxiety in avoidant users.
*   **The Path Forward:** Success requires a hybrid or tiered model. We must balance "soft nudges" for the anxious with rigorous validation for the skeptics.

> "If it's not FDA cleared, it's just a toy." vs "I don't want to be pestered unless I'm actually dying."

*Footer: Confidential & Proprietary*

---

# 02
## User Preferences
**DRIs:** User Research Team

---

# Preference correlates strongly with health anxiety and technical literacy

| Concept | Audience Share | Key Archetypes | Primary Motivation |
| :--- | :--- | :--- | :--- |
| **Concept A (Wellness)** | **50%** | Tech-Savvy, Anxious Avoider, Busy Pro | Less scary, fits into routine, coaching focus. |
| **Concept B (Medical)** | **40%** | Skeptic, Chronic Patient, Data Analyst | Need for hard proof, existing condition management. |
| **Unsure** | **10%** | Cost-Conscious | Dependent on insurance/cost. |

*Footer: Confidential & Proprietary*

---

# The "Proof" Divide: Users are polarized on data depth

We cannot satisfy the Skeptic with a simple app, nor the Busy Pro with a complex one.

**The Skeptic & Analyst**
> "I need to know if you're using PPG or just calibration estimation. Open source the algo?"
> "It needs to let me export a PDF report for my cardiologist."

**The Busy Professional**
> "Give me 'bite-sized' actions. I can't read long studies."
> "Please don't make the alerts scary red colors."

*Footer: Confidential & Proprietary*

---

# 03
## Barriers & Drivers
**DRIs:** User Research Team

---

# Actionability relies on overcoming anxiety and enabling verification

*   **Barrier: Anxiety & Avoidance**
    *   Aggressive UI (red alerts) causes immediate churn for "Anxious Avoiders."
    *   *Implication:* Default experience must be non-threatening.
*   **Barrier: The "Wait and See" Protocol**
    *   40% of users' first instinct is to wait and re-measure at home to avoid "bothering" a doctor.
    *   *Implication:* We must build a "Verify with Cuff" flow into the app.
*   **Driver: Context is King**
    *   Explaining *why* a reading is high (e.g., "related to poor sleep") is the #1 driver for action.
    *   *Implication:* Alerts must never be context-free.

*Footer: Confidential & Proprietary*

---

# 04
## Recommendations
**DRIs:** Product & Engineering

---

# We must build a tiered experience to serve both personas

*   **Must Have: Contextual Alerts**
    *   *Why:* Users demand to know the "why" behind a reading to take it seriously.
*   **Must Have: "Soft Nudge" UI Mode**
    *   *Why:* To retain the 50% of users who are "Anxious Avoiders."
*   **Should Have: In-App Verification Flow**
    *   *Why:* To support the 40% who will otherwise wait and re-measure outside the ecosystem.
*   **Should Have: Tiered Experience**
    *   *Why:* To resolve the conflict between "Busy Professionals" (simplicity) and "Data Analysts" (transparency).

> "We noticed a high reading. Let's guide you through a cuff check to confirm."

*Footer: Confidential & Proprietary*
