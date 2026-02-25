---
name: prd-standard-skill
description: Generates high-fidelity, Staff-level PRDs following the "Blood Pressure Trends" master format, blending narrative storytelling with engineering rigor.
version: 1.0.0
---

# PRD Standard Skill (The "Tidal" Format)

## Capability
This skill allows the agent to produce a Product Requirements Document (PRD) that mirrors the exact structure, tone, and depth of the "Blood Pressure Trends" (Tidal) document. It balances consumer-facing value propositions with clinical validation and technical logic.

## Instructions

### 1. Document Structure
Every PRD must follow this exact sequence:
1.  **Narrative Lead (Press Release):** A dated, "August 2026" style news announcement that captures the emotional and strategic value of the feature.
2.  **Overview:** High-level problem definition, market urgency, and summary of the proposed solution.
3.  **Target Product Profile:**
    *   **Intended Use Statement:** Precise regulatory language (Wellness vs. Medical).
    *   **Problem Statement:** Detailed breakdown of "The Gap" (e.g., The Silent Killer, The Single-Reading Bias).
4.  **Product Specs:**
    *   **Product Output:** P0 (Binary) and P1 (Granular) outputs.
    *   **Positioning:** One-sentence "North Star."
    *   **Assessment Period:** Evaluation windows, data sufficiency (min wear time), and threshold logic.
5.  **Constraints & Eligibility:** Contraindications, Supported Devices, and Country Availability.
6.  **Performance Targets:** Clinical benchmarks (Sensitivity/Specificity) and Ground Truth references.
7.  **The PHA Narrative:** A 1-9 point breakdown of how the Personal Health Assistant "narrates" the feature to the user.
8.  **Critical User Journeys (CUJs):** Use the 3-column table format: **Goal (The "Why")** | **Task (The "How")** | **Product CUI**.
9.  **Feature Logic Definitions:** A table of constants (e.g., `MIN_WEAR_HOURS`, `SQI_MIN`).
10. **Algorithm Validation:** Comparison of Study Size vs. Target vs. Status.
11. **Evaluation Questions (Ask Health):** Exhaustive FAQ categorized by:
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
"October 12th, 2026: Google's Personal Health Assistant is helping users look beneath the surface of their metabolism..."
followed by the full structured PRD.
