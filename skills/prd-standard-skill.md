---
name: prd-standard-skill
description: Generates high-fidelity, Staff-level PRDs following the "Blood Pressure Trends" master format, blending narrative storytelling with engineering rigor.
version: 1.1.0
---

# PRD Standard Skill (The "Tidal" Format)

## Capability
This skill allows the agent to produce a Product Requirements Document (PRD) that mirrors the exact structure, tone, and depth of the "Blood Pressure Trends" (Tidal) document. It balances consumer-facing value propositions with clinical validation and technical logic.

## Instructions

### 1. Document Structure
Every PRD must follow this exact sequence:
1.  **Press Release (PR) Narrative:** **[REQUIRED: NARRATIVE]**
    *   **Header 1 (Title):** The program name.
    *   **Header 2 (Subtitle):** "Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — [Program Name] Trends".
    *   **Dateline:** "[Month Day, Year]:"
    *   **Body Content (Paragraph 1):** Focus on the "Invisible" or "Silent" nature of the health signal.
    *   **Body Content (Paragraph 2):** Introduce "[Program Name], a new wellness feature for Pixel Watch and Fitbit devices." Emphasize "no behavior change required."
    *   **Body Content (Paragraph 3):** Describe the "Quiet Approach" (e.g., "Most months, users won’t hear from it...").
    *   **Quote 1:** Visionary quote from "Rishi Chandra (VP Google Health)" or relevant executive.
    *   **Quote 2:** Clinical quote from a relevant clinical lead or subject matter expert.
    *   **Closing:** Explicitly state the feature is "designed to start conversations, not replace care" and mention "one thoughtful insight a month."
2.  **Overview:** High-level problem definition, market urgency, and summary of the proposed solution.
3.  **Target Product Profile (Grid):** Category | Definition Table.
4.  **Product Overview (P0/P1):** Detailed feature requirements with priority tags.
5.  **Market Positioning (The 9 Things Table):** Item | Title | Description Table with exactly 9 points.
6.  **Performance Targets:** Clinical benchmarks (Sensitivity/Specificity) and Ground Truth references.
7.  **Critical User Journeys (CUJs):** Use the 3-column table format: **Goal (The "Why")** | **Task (The "How")** | **Product CUI**.
8.  **Feature Logic Definitions:** A table of constants (e.g., `MIN_WEAR_HOURS`, `SQI_MIN`).
9.  **Algorithm Validation:** Comparison of Study Size vs. Target vs. Status.
10. **Evaluation Questions (Ask Health):** Exhaustive FAQ categorized by:
    *   Understanding Trends vs. Readings
    *   Longitudinal Thinking
    *   Lifestyle Linkage
    *   Trust & Comprehension

### 2. Style & Design Rules
*   **Tone:** Senior, calm, authoritative, and regulatory-aware.
*   **Vocabulary:** NEVER use "Monitor" or "Diagnose." USE "Estimate," "Spot," "Patterns," and "Peace of Mind."
*   **Visuals:** Use Markdown tables for all specs. Use `[P0]` and `[P1]` tags to denote priority.
*   **Logic:** Always include "Data Sufficiency" (how much data is needed before a result is shown).

## Examples

### User Request:
"Create a PRD for Insulin Resistance using the new standard format."

### Action:
The agent will ingest `knowledge/insulin resistance/` and `knowledge/user_research/` and then output a document starting with:
"Insulin Resistance Trends
Google’s Personal Health Assistant Is Learning to Spot — and May Help Reverse — Insulin Resistance Trends
October 12th, 2026: Most people don’t think about their metabolism until it stops working..."
followed by the full structured PRD.
