# Initial Concept
Autonomous Product Development Agent configuration and management.

# Product Definition

## 1. Overview
**Product Name:** Chief of Staff
**Mission:** To bridge the gap between visionary product strategy and rigorous engineering execution for Project Tidal. This repository serves as the "brain" and "memory" for an autonomous agent that generates high-fidelity product artifacts.

## 2. Target Audience
*   **Product Managers:** seeking to automate the heavy lift of PRD creation and ensure strategic alignment.
*   **Engineers:** needing detailed, implementation-ready specs grounded in technical reality.
*   **QA Engineers:** requiring rigorous, testable acceptance criteria to verify features.
*   **Executives/Stakeholders:** reviewing the high-level product vision and narrative.

## 3. Core Goals
*   **Standardization:** Provide a consistent, structured home for all product artifacts (User Research, Specs, Regulatory).
*   **Agent Capabilities:** Host and manage the specialized AI skills that power the autonomous workflow.
*   **Single Source of Truth:** Serve as the definitive reference for Project Tidal's development lifecycle.
*   **Methodology Enforcement:** Operationalize the "Working Backwards" approach to ensure customer-centricity.

## 4. Key Features

### Two PRD Modes (via `prd-agent-skill.md`)
*   **Full PRD (default):** Comprehensive spec with PR, Overview, Target Product Profile, 9 Things, CUJ Maps, Algorithm Performance, Acceptance Criteria (Gherkin), Feature Logic, and Appendix.
*   **Mini Product Narrative:** Condensed one-pager with PR, Overview, Target Product Profile, 9 Things, and Summary/Next Steps. Triggered by "mini PRD," "mini product overview," "short PRD," or "product narrative."

### Shared Across Both Modes
*   **Press Release First:** Every document opens with a "Working Backwards" PR enclosed in a bordered box — via `product-narrative-skill.md`.
*   **9 Things Table:** 2-column format with stacked number + tagline in the left cell — via `marketing-skill.md` + `tidal-master-template-skill.md`.
*   **Product Grid:** Full Target Product Profile table — via `tidal-master-template-skill.md`.

### Full PRD Only
*   **CUJ Maps:** 4+ Critical User Journeys — via `cuj-generator-skill.md`.
*   **Acceptance Criteria:** Gherkin-syntax specs for Engineering and QA — via `acceptance-criteria-skill.md`.
*   **Algorithm Validation:** Performance targets and study results grid.
*   **Compliance Guardrails:** Built-in checks against FDA General Wellness guidelines to ensure safety.

## 5. Constraints & Non-Functional Requirements
*   **Regulatory Compliance:** Strict adherence to FDA General Wellness guidance is mandatory (no diagnostic claims).
*   **Technical Feasibility:** All features must align with the constraints documented in the algorithm overview (e.g., 14-day calibration).
*   **Documentation Standards:** All generated artifacts must conform to the defined Markdown templates.

## 6. Design Philosophy (North Star)
*   **7-Star Experience:** We aim for "magical," intuitive interactions that exceed user expectations (Chesky).
*   **Working Backwards:** We define the customer benefit (Press Release) before writing a single line of spec (Amazon).
*   **Jobsian Simplicity:** We prioritize "insanely great" simplicity, ruthlessly removing friction and clutter.
