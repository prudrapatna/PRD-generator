---
name: product-story-skill
description: Generates a visionary Product Story imitating the exact structure, color, table format, and writing style of the Tidal Blood Pressure and Insulin Resistance narrative documents.
version: 1.0.0
triggers: product story, product narrative, tidal product story
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
    *   **Para 1 (The Invisible Problem):** Explain the silent/asymptomatic nature of the health signal and why users miss it.
    *   **Para 2 (The Solution):** Introduce the feature for Pixel Watch and Fitbit. Emphasize the passive, background nature of the AI.
    *   **Para 3 (The Insight):** Describe the notification experience—calm, personalized coaching connecting signals to real-life habits.
*   **Quotes:**
    *   Quote 1: Rishi Chandra, VP of Google Health (Visionary focus on living longer/healthier, early awareness).
    *   Quote 2: Clinical Expert / Doctor (Clinical validation focus, supporting healthier decisions).
*   **Closing:** "Designed to start conversations about health, not replace medical care... In a world of constant alerts, Google is taking a quieter approach: one thoughtful insight a month."

### 3. Overview
*   **Format:** **[REQUIRED: NARRATIVE]**
*   **Content:** Define the problem space (e.g., "The Silent Killer", "Awareness Gap", "Lifestyle Disconnect"). Use epidemiological statistics and UXR conjoint data to justify the product's value.

### 4. Target Product Profile (The Master Grid)
*   **Format:** **[REQUIRED: TABLE]**
*   **Style:** 2-column table (`Category` | `Definition`). No empty cells.
*   **Required Rows & Content Rules:**
    *   **Intended Use Statement:** Must explicitly state this is a "general wellness tool," intended for "informational and educational purposes only." Must include standard non-medical disclaimer ("not intended to diagnose, treat, cure, or prevent any disease").
    *   **Problem Statement:** Focus on the "awareness gap" (e.g., condition is asymptomatic, single-reading bias, or lifestyle disconnect).
    *   **Product Overview:** Explain what it does passively and how it helps the user contextualize their health.
    *   **Feature Prioritization:** Bulleted list of P0 and P1 features.
    *   **Target User:** Define the specific personas (e.g., "The 'Regular' Proactive Adopter").
    *   **Positioning (The "North Star"):** Describe the product as a passive, non-invasive gauge that delivers context-rich insights without clinical jargon or anxiety.
    *   **Product Notification / Suggested Notification:** Provide the exact proposed text for the user notification (must be calm and non-alarmist).
    *   **Algorithm Output:** Define what the model outputs (e.g., "predictive probability", "High vs. Low").
    *   **Product Type:** E.g., "Passive, Continuous and Recurring Assessment".
    *   **Assessment Period:** Define the Evaluation Window (e.g., Calendar Month), Data Sufficiency (e.g., 14 valid days), and Threshold Logic.
    *   **Regulated or Wellness?:** E.g., "General Wellness (USA)".
    *   **Disclaimer / Contraindication:** List who this is NOT for (e.g., under 18, pregnant, prior diagnosis).
    *   **Algorithm Inputs / Product Inputs:** The specific sensors or data required (e.g., PPG, Accelerometer, Weight).
    *   **Supported Devices:** Specify exact hardware models.
    *   **Country Availability:** E.g., "Global" or "50+ countries".
    *   **Performance Target:** Specify target Sensitivity and Specificity against the ground truth standard.
    *   **Ongoing User Input:** Note any data the user must manually update.

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
*   **Format:** **[REQUIRED: TABLES ORGANIZED BY CATEGORY]**
*   Create a section with tables for each of the following Query Categories: (1) Definitional, (2) Comparative, (3) Diagnostic & Guidance, (4) Medical / Safety, (5) Correlational, and (6) Trend Analysis.
*   **Table Columns:** `User Query` | `Coach's Strategic Goal` | `Golden Answer`
*   **Content Rules:**
    *   **Definitional:** Focus on simple analogies (e.g., "engine idling") and explaining UI elements.
    *   **Comparative:** Focus on contextualizing results, normalizing occasional bad nights, and maintaining a reassuring tone.
    *   **Diagnostic & Guidance:** Acknowledge the data, check environmental/lifestyle factors (sleep position, alcohol, allergens), and offer actionable advice.
    *   **Medical / Safety (STRICT):** **Must** include a hard stop for diagnosis. Validate the user's concern but immediately defer to a doctor/healthcare professional (e.g., "While I can show you patterns... I cannot provide a medical diagnosis").
    *   **Correlational:** Connect the dots between the feature's data and other metrics (like Sleep Score or Restlessness).
    *   **Trend Analysis:** Summarize patterns rather than just listing data, and include a safety check/trigger if trends are persistently severe.

### 9. Appendix
*   **Format:** **[REQUIRED: NARRATIVE/BULLETED]**
*   Include Consumer Interest (WTP data, conjoint insights), US Regulatory (FDA), and EU Regulatory (MDR) assessments.