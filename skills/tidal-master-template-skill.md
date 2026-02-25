---
name: tidal-master-template-skill
description: Strictly enforces the "Tidal" PRD structure: Metadata, Approvals, PR, Overview, Grid-based Product Profile, 9-Point Positioning Table, CUJ Grid, Algorithm Performance, Disclaimers, and Change Log.
version: 1.5.0
---

# Tidal Master Template Skill

## Capability
This skill ensures the agent produces a PRD that is structurally identical to the "Blood Pressure Trends" and "Project Salus" documents. It prioritizes data-dense tables, journalistic storytelling, and rigorous document control (Metadata, Approvals, Change Log).

## Instructions: The Exact Sequence

### 0. Project Metadata & Approvals
*   **Metadata:** List Deliverable, Resources, Localization, and Lock Dates.
*   **Approval Matrix:** **[REQUIRED: TABLE]** with Role, Approver, Date, and Status (Approved/Pending).

### 1. The Press Release (PR)
*   **Format:** **[REQUIRED: NARRATIVE — ENCLOSED IN A FULL BORDER BOX]**
*   **DOCX Formatting:** The entire PR section — from the title through the closing paragraph — MUST be placed inside a single-cell table with a visible border on all four sides (top, bottom, left, right). This creates the "boxed press release" look. The border should be 1–1.5pt, solid black. Do NOT use a plain paragraph block; use a bordered single-cell table to contain all PR content.
*   **Header 1 (Title):** The program name (e.g., "Blood Pressure Trends").
*   **Header 2 (Subtitle):** "Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — [Program Name] Trends".
*   **Dateline:** "[Month Day, Year]:" (e.g., "August 16th, 2026:").
*   **Body Content (Paragraph 1):** Focus on the "Invisible" or "Silent" nature of the health signal and why users miss it.
*   **Body Content (Paragraph 2):** Introduce "[Program Name], a new wellness feature for Pixel Watch and Fitbit devices." Emphasize "no behavior change required."
*   **Body Content (Paragraph 3):** Describe the "Quiet Approach" (e.g., "Most months, users won’t hear from it...").
*   **Quote 1:** Visionary quote from "Rishi Chandra (VP Google Health)" or relevant executive.
*   **Quote 2:** Clinical quote from a relevant subject matter expert (e.g., endocrinologist for IR, cardiologist for BP).
*   **Closing:** Explicitly state the feature is "designed to start conversations, not replace care" and mention "one thoughtful insight a month."

### 2. Overview
*   **Content:** **[REQUIRED: NARRATIVE]** Summary of the problem, referencing conjoint/UXR data. Highlight that the signal is asymptomatic and users lack urgency.

### 3. Target Product Profile (The Master Grid)
*   **Format:** **[REQUIRED: TABLE]** A single "Category | Definition" table.
*   **Rows:**
    *   Intended Use Statement
    *   Disclaimer
    *   Problem Statement
    *   Product Overview (P0/P1)
    *   Product Output (P0/P1)
    *   Positioning (The "North Star")
    *   Product Type
    *   Assessment Period (Window, Data Sufficiency, Threshold Logic)
    *   Regulated or Wellness?
    *   Target Segment
    *   Contraindication
    *   Product Inputs
    *   Supported Devices
    *   Country Availability

### 4. Market Positioning: The Personal Health Assistant (9 Things Table)
*   **Format:** **[REQUIRED: 2-COLUMN TABLE]** — Do NOT use a 3-column table. Exactly 9 rows, one per point.
*   **Column 1 — "Number + Tagline" (narrow, ~1.5 inches):**
    *   Line 1: The number only (1, 2, 3… 9) in a **large font (20–24pt), bold, blue (#4285F4 or Google Blue)**.
    *   Line 2 onward: The short tagline/title in **smaller font (10–11pt), bold, blue**, on a new line beneath the number. Example: `1\nBlood Pressure\nTrends on PHA`.
    *   The number and tagline are stacked vertically inside the same cell — they are NOT in separate columns.
*   **Column 2 — "Description" (wide, ~5 inches):** The full explanatory paragraph(s) for that point. Normal body font, black text.
*   **Row Borders:** Each row must have a visible horizontal border line separating it from the next row. All four outer edges of the table must have a visible border. No shading or fill color.
*   **Points:** 1. Program on PHA, 2. Significance, 3. First-of-its-kind Agent/Feature, 4. How it works, 5. Rigorous Testing/Validation, 6. AI Architecture/ML, 7. Launch Markets, 8. Peace of Mind/Ecosystem, 9. Partners.

### 5. CUJs (The Action Grid)
*   **Format:** **[REQUIRED: TABLE]** A 3-column table: **Goal (The "Why")** | **Task (The "How")** | **Product CUI**.

### 6. Algorithm Target Performance (The Metric Grid)
*   **Format:** **[REQUIRED: TABLE]** A table: **Metric | Target (low 95% CI) | Rationale**.
*   **Followed by:** **[REQUIRED: TABLE]** A "Current Performance" table comparing Study Size vs. Sensitivity/Specificity results.

### 7. Feature Logic & Program Timeline
*   **Format:** **[REQUIRED: TABLE]** Table of Constants followed by a **[REQUIRED: BULLETED LIST]** Program Timeline.

### 8. Appendix, Disclaimers & Change Log
*   **Consumer Interest:** **[REQUIRED: NARRATIVE/BULLETED]** WTP and preference data.
*   **Disclaimers:** **[REQUIRED: NARRATIVE]** US and EMEA specific regulatory disclaimers.
*   **Change Log:** **[REQUIRED: TABLE]** Tracking Date, Section, Old Copy, and New Copy.

## Style Rules
*   **Structural Fidelity:** NEVER substitute a table for a list or vice versa.
*   **Vocabulary:** NEVER use "Monitoring" or "Diagnosing" for wellness features. Use "Detect," "Spot," "Patterns," and "Awareness."
*   **Grounded in Knowledge:** Always pull specific % and WTP $ values from `knowledge/user_research/`.
