---
name: tidal-master-template-skill
description: Strictly enforces the "Tidal" PRD structure: PR, Overview, Grid-based Product Profile, 9-Point Positioning Table, CUJ Grid, Algorithm Performance, and Program Timeline.
version: 1.1.0
---

# Tidal Master Template Skill

## Capability
This skill ensures the agent produces a PRD that is structurally identical to the "Blood Pressure Trends" document. It prioritizes data-dense tables and journalistic storytelling.

## Instructions: The Exact Sequence

### 1. The Press Release (PR)
*   **Format:** Dated ("October 2026"), bold headline, journalistic body text.
*   **Quotes:** Must include a Visionary quote from "Rishi Chandra (VP Google Health)" and a Clinical quote from "Dr. Stephen Juraschek."

### 2. Overview
*   **Content:** Summary of the problem, the market urgency (referencing conjoint data), and the proposed solution.

### 3. Target Product Profile (The Master Grid)
*   **Format:** A single "Category | Definition" table.
*   **Rows:**
    *   Intended Use Statement
    *   Disclaimer
    *   Problem Statement
    *   Product Overview (P0/P1)
    *   Product Output (P0/P1)
    *   Positioning (The "North Star")
    *   Product Type (e.g., Passive, Recurring)
    *   Assessment Period (Window, Data Sufficiency, Threshold Logic)
    *   Regulated or Wellness?
    *   Target Segment
    *   Contraindication
    *   Product Inputs
    *   Supported Devices
    *   Country Availability

### 4. Market Positioning: The 9 Things (Table)
*   **Format:** An "Item | Description" table with exactly 9 points.
*   **Points:** 1. Program on PHA, 2. Significance, 3. First-of-its-kind Agent, 4. How it works, 5. Rigorous Testing, 6. AI Architecture, 7. Launch Markets, 8. Peace of Mind, 9. Partners.

### 5. CUJs (The Action Grid)
*   **Format:** A 3-column table: **Goal (The "Why")** | **Task (The "How")** | **Product CUI**.

### 6. Algorithm Target Performance (The Metric Grid)
*   **Format:** A table: **Metric | Target (low 95% CI) | Rationale**.
*   **Followed by:** A "Current Performance" table comparing Study Size vs. Sensitivity/Specificity results.

### 7. Feature Logic & Program Timeline
*   **Format:** Table of Constants (MIN_WEAR_HOURS, etc.) followed by a bulleted Program Timeline.

### 8. Appendix
*   **Content:** Consumer Interest data (WTP from conjoint reports) and Competitive Benchmarks.

## Style Rules
*   **No "Monitoring":** Use "Detect," "Spot," "Patterns," and "Awareness."
*   **Grounded in Knowledge:** Always pull specific % and WTP $ values from the `knowledge/user_research/` files.
