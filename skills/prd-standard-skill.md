---
name: prd-standard-skill
description: Defines the comprehensive structure, formatting, and content rules for a Full PRD. Used by the prd-agent orchestrator when the user asks for a complete product requirements document.
version: 3.0.0
triggers: full PRD, complete PRD, detailed PRD
---

# PRD Standard Skill — Full PRD Format

## Scope
This skill defines the **Full PRD** format. It produces a comprehensive, engineering-ready document that includes a Press Release, Master Grid, 9 Things, full CUJ maps, algorithm performance, feature logic, detailed acceptance criteria (Gherkin), and appendices.

---

## When This Skill is Active
Triggered by `prd-orchestrator-agent.md` in Full PRD mode. Do NOT use this skill for Mini PRDs or Product Narratives.

---

## Output Structure

The output MUST strictly follow this ordered structure and these exact formatting constraints:

### 0. Project Metadata & Approvals
*   **Format:** Lists and a **[REQUIRED: TABLE]**
*   **Metadata:** Deliverable, Resources, Localization, Lock Dates
*   **Approval Matrix table:** Role | Approver | Date | Status

### 1. Press Release [PR]
*   **Format:** **[REQUIRED: NARRATIVE — FULL BORDER BOX]**
*   Enclose the entire PR in a single-cell bordered table (1–1.5pt solid black, all four sides).
*   Follow the visionary, positive tone defined in the `product-narrative-skill.md`.

### 2. Overview
*   **Format:** **[REQUIRED: NARRATIVE]**
*   Problem definition + market urgency. Ground every claim using data from `knowledge/user_research/`.

### 3. Target Product Profile (The Master Grid)
*   **Format:** **[REQUIRED: TABLE]** Two columns: Category | Definition
*   Rows include: Intended Use Statement, Disclaimer, Problem Statement, Product Overview (P0/P1), Product Output (P0/P1), Positioning (The "North Star"), Product Type, Assessment Period, Regulated or Wellness?, Target Segment, Contraindication, Product Inputs, Supported Devices, Country Availability, Performance Target, Ongoing User Input.
*   Fill every row with specifics from the `knowledge/` files. No empty cells.

### 4. Market Positioning: The Personal Health Assistant (9 Things)
*   **Format:** **[REQUIRED: 2-COLUMN TABLE]**
*   **Left column (~1.5"):** Large blue number (20–24pt, bold) + tagline below (11pt, bold, blue) — stacked in same cell.
*   **Right column (~5"):** Description. Normal body font, black text.
*   Horizontal border between every row. Outer border on all sides. Exactly 9 rows.

### 5. Critical User Journeys (CUJ Maps)
*   **Format:** **[REQUIRED: TABLE + NARRATIVE]**
*   Minimum 4 CUJs (e.g., Onboarding, Reassuring Glance, Contextual Nudge, Informed Share).
*   Table format: `Goal (The "Why")` | `Task (The "How")` | `Product CUI`.
*   Include Health & Metrics per the `cuj-generator-skill.md`.

### 6. Algorithm Target Performance
*   **Format:** **[REQUIRED: TABLES]**
*   Table 1: `Metric` | `Target (low 95% CI)` | `Rationale`
*   Table 2: Current Performance: `Study Size` | `Sensitivity` | `Specificity` | `Adj. Specificity`

### 7. Feature Logic & Program Timeline
*   **Format:** **[REQUIRED: TABLE]** Table of Constants.
*   **Followed by:** **[REQUIRED: BULLETED LIST]** Program Timeline milestones.

### 8. Acceptance Criteria
*   **Format:** **[REQUIRED: GHERKIN SPEC]**
*   Must include detailed Functional Scenarios (Given/When/Then) covering Core Logic, State Transitions, Edge Cases, and Error Handling as defined in `acceptance-criteria-skill.md`.
*   Must include Non-Functional Requirements.

### 9. Appendix, Disclaimers & Change Log
*   **Consumer Interest:** **[REQUIRED: NARRATIVE/BULLETED]** WTP and preference data.
*   **Disclaimers:** **[REQUIRED: NARRATIVE]** US and EMEA specific regulatory disclaimers.
*   **Change Log:** **[REQUIRED: TABLE]** Date | Section | Old Copy | New Copy.

---

## Style Rules
*   **Structural Fidelity:** NEVER substitute a table for a list or vice versa.
*   **Vocabulary:** NEVER use "Monitoring" or "Diagnosing" for wellness features. Use "Detect," "Spot," "Patterns," and "Awareness."
*   **Grounded in Knowledge:** Always pull specific % and WTP $ values from `knowledge/user_research/`.

## Content Quality Rules
- **No fabricated numbers.** Every % and $ must trace to `knowledge/user_research/` or `knowledge/[feature]/`.
- **No diagnostic language.** "Estimate," "Spot," "Trends," "Patterns" only. Do not claim to "detect" a condition.
- **Medical Condition Framing.** Unless the product is explicitly defined as Software as a Medical Device (SaMD), do NOT frame the problem statement or overview around a specific medical condition (e.g., "Hypertension"). Frame it around the underlying physiological signal (e.g., "high blood pressure") or wellness goal.