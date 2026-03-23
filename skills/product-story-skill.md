---
name: product-story-skill
description: Generates a visionary Product Story imitating the exact structure, color, table format, and writing style of the Tidal Blood Pressure and Insulin Resistance narrative documents.
version: 1.0.0
triggers: product story, product narrative, tidal product story, product proposal
---

# Product Story Skill

## Capability
This skill defines the exact structure, formatting, colors, and writing style to generate a comprehensive "Product Story" (also known as a Product Narrative or PRD-lite) following the exact template of the Tidal Blood Pressure and Insulin Resistance documents.

## Writing Style & Tone Guidelines
1.  **Empathetic & Empowering:** Frame the feature as an empowering tool ("metabolic efficiency gauge," "peace of mind," "start conversations") rather than a diagnostic alarm.
2.  **The "Quiet Approach":** Emphasize passive monitoring. "No cuffs, no scheduled readings," "one thoughtful insight a month," "operates quietly in the background."
3.  **Non-Diagnostic Language:** For wellness features, strictly use terms like "estimates," "patterns," "trends," and "out of range." Avoid "diagnose," "detect disease," or "medical grade."
4.  **Connect to Lifestyle:** Always highlight how the physiological signal connects to daily habits (sleep, activity, stress, nutrition).

## Output Structure & Formatting Requirements

The output MUST strictly follow this ordered structure and these exact table/formatting constraints:

### 1. Approval Cover Page
*   **Format:** **[REQUIRED: TABLE]**
*   **Columns:** `Approver` | `Approval Status` | `Date`
*   Add 4-5 empty rows for sign-offs.

### 2. The Press Release / Narrative
*   **Format:** **[REQUIRED: NARRATIVE — FULL BORDER BOX]**
*   **Formatting Details:** Enclose the entire PR section (title to closing) inside a single-cell table with a **1–1.5pt solid black border** on all four sides.
*   **Header 1 (Title):** Catchy, consumer-friendly title (e.g., "Helping your heart thrive: Google introduces...").
*   **Dateline:** "[Month Day, Year]:" in bold.
*   **Body Paragraphs:**
    *   **Para 1 (The Problem):** Explain the nature of the health signal and why users miss it.
    *   **Para 2 (The Solution):** Introduce the feature for Pixel Watch and Fitbit. Emphasize the passive, background nature of the AI.
    *   **Para 3 (The Insight):** Describe the notification experience—calm, personalized coaching connecting signals to real-life habits.
*   **Quotes:**
    *   Quote 1: Rishi Chandra, VP of Google Health (Visionary focus on living longer/healthier, early awareness).
    *   Quote 2: Clinical Expert / Doctor (Clinical validation focus, supporting healthier decisions).
*   **Closing:** "Designed to start conversations about health, not replace medical care... In a world of constant alerts, Google is taking a quieter approach: one thoughtful insight a month."

### 3. Background & Current Understanding
*   **Format:** **[REQUIRED: NARRATIVE]**
*   **Skill Chaining [CRITICAL]:** You MUST activate and use the `web-search` skill to gather authoritative clinical, scientific, and epidemiological data before writing this section. Do not rely solely on your internal knowledge.
*   **Content:** Define the problem space robustly, mirroring the depth of clinical whitepapers. 
    *   **Epidemiology & Guidelines:** Ground the problem in data from authoritative sources (e.g., WHO, Lancet, JAMA, USPSTF). Cite prevalence, awareness gaps, and current screening recommendations.
    *   **Clinical Realities:** Discuss the current standard of care and provide specific statistical comparisons (e.g., sensitivities, specificities, AUROCs) of existing methods versus the proposed approach.
    *   **Physiological Mechanisms:** Explain the underlying science of the signal being measured, citing seminal studies or recent research to justify the technical approach.
    *   **User Research (UXR):** Combine clinical rigor with UXR data explaining why users struggle with current solutions. 
    *   **Citations:** Use inline citations for all claims (e.g., (Author et al., Journal, Year)).

### 4. Target Product Profile (The Master Grid)
*   **Format:** **[REQUIRED: TABLE]**
*   **Style:** 2-column table (`Category` | `Definition`). No empty cells.
*   **Required Rows:**
    *   **Intended Use Statement:** Must strictly follow this template unless it is Software as a Medical Device (SaMD):
        > "The [Feature Name] feature is a general wellness tool intended to estimate [metric] to promote positive lifestyle behavior changes in [lifestyle factors, e.g., sleep, activity, stress and nutrition management] by educating users and helping them understand how their daily habits correlate with estimated [metric] trends/levels. This product is not intended to diagnose, mitigate, treat, or cure any disease. This product is not a prescreener for [related disease] nor is it intended to track [clinical metric] in real time. Do not use this product for [disease] management or rely on this product to alter any medications... Consult a medical professional for any questions about your [health area] health."
    *   Problem Statement
    *   Product Overview
    *   Feature Prioritization (P0/P1 lists)
    *   Target User
    *   **Positioning:** Must strictly follow this template:
        > "[Feature Name] is a passive, [calibration-free/non-invasive] general wellness feature that acts as a [concept] gauge — estimating a user's [metric] over a full calendar month and delivering a single, context-rich insight — correlating patterns against [lifestyle factors] — so users understand their [health area] wellness without anxiety."
    *   Product Notification / Suggested Notification
    *   Algorithm Output
    *   Product Type (e.g., Passive, Longitudinal and Recurring Assessment)
    *   Assessment Period (Evaluation Window, Data Sufficiency, Threshold Logic)
    *   Regulated or Wellness?
    *   Disclaimer / Contraindication
    *   Algorithm Inputs / Product Inputs
    *   Supported Devices
    *   Country Availability
    *   Performance Target
    *   Ongoing User Input

### 5. Market Positioning: The Personal Health Assistant (9 Things)
*   **Format:** **[REQUIRED: 2-COLUMN TABLE]**
*   **Styling Details (CRITICAL):**
    *   **Outer & Inner Borders:** Each row must have a visible horizontal border line separating it from the next. The table must have an outer border.
    *   **Left Column (~1.5 inches wide):** 
        *   Line 1: The item number (1, 2, 3... 9). Must be **large font (20–24pt), bold, and blue (#4285F4)**.
        *   Line 2: The short tagline (e.g., "A first-of-its-kind agent"). Must be **smaller font (10–11pt), bold, and blue (#4285F4)**, stacked directly beneath the number in the *same cell*.
    *   **Right Column (~5 inches wide):** The descriptive paragraph. Normal body font, black text.
*   **The 9 Points:** (1) The Feature on PHA, (2) Clinical Significance, (3) First-of-its-kind claim, (4) How it works, (5) Rigorous testing/validation, (6) AI Architecture, (7) Launch markets, (8) Enhanced peace of mind (ecosystem), (9) Expert Partners.

### 6. Critical User Journeys (CUJs)
*   **Format:** **[REQUIRED: TABLE]**
*   **Columns:** `Goal (The "Why")` | `Task (The "How")` | `Product CUI`
*   **Typical Rows:**
    *   The Invisible Setup (Onboarding to silent calibration)
    *   The Reassuring Glance (Calendar month status check)
    *   The Contextual Nudge (Out-of-range notification & lifestyle link)
    *   The Informed Share (Pre-appointment prep / PDF export)

### 7. Feature Logic Definitions & Algorithm Performance
*   **Format:** **[REQUIRED: TABLES]**
*   **Feature Logic Table:** `Constant` | `Value` | `Description` (e.g., `MIN_WEAR_HOURS_PER_DAY`, `OBSERVATION_WINDOW_DAYS`).
*   **Performance Target Table:** `Metric` | `Target (low 95% CI)` | `Rationale`
*   **Current Performance Table:** `Study Size` | `Sensitivity` | `Specificity` | `Adj. Specificity`

### 8. Evaluation Questions for Ask Health
*   **Format:** **[REQUIRED: LISTS]**
*   Categorized lists of user queries the AI coach must be able to handle (e.g., A. Understanding trends, B. Longitudinal thinking, C. Lifestyle linkage curiosity).

### 9. Appendix
*   **Format:** **[REQUIRED: NARRATIVE/BULLETED]**
*   Include Consumer Interest (WTP data, conjoint insights), US Regulatory (FDA), and EU Regulatory (MDR) assessments.nts.clude Consumer Interest (WTP data, conjoint insights), US Regulatory (FDA), and EU Regulatory (MDR) assessments.egulatory (FDA), and EU Regulatory (MDR) assessments.nts.clude Consumer Interest (WTP data, conjoint insights), US Regulatory (FDA), and EU Regulatory (MDR) assessments.