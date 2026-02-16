# Chief of Staff: Autonomous Product Development Agent

## Overview

This repository defines the **Chief of Staff** agent—a specialized AI system designed to autonomously generate high-fidelity Product Requirements Documents (PRDs), User Journeys (CUJs), and Visuals. 

It synthesizes visionary product thinking (Jobs/Chesky/Musk) with rigorous technical and regulatory constraints.

---

## 🚀 How to Use This Agent

To unleash the full potential of the Chief of Staff agent, you **MUST** provide the following four key inputs. The quality of the output PRD is directly proportional to the quality of these inputs.

### 1. User Research (The "Why")
*   **Location:** `/user_research`
*   **Required Content:**
    *   **Detailed Personas:** Who are we building for? (e.g., "Proactive Adopters," "Data Skeptics").
    *   **Pain Points:** What keeps them up at night? (e.g., "Anxiety about medical devices," "Motivation barriers").
    *   **Validation Data:** Survey results, interview synthesis, or problem definition documents.
*   **Why:** The agent uses this to challenge assumptions and ensure the product solves a *real* human problem, not just a technical one.

### 2. Algorithm Overview & Target Performance (The "Reality")
*   **Location:** `/algorithm_overview_and_target_performance`
*   **Required Content:**
    *   **Capabilities:** What can the technology actually do? (e.g., "Passive PPG sensing").
    *   **Constraints:** What are the limitations? (e.g., "Requires 14 days of wear," "Must input height").
    *   **Accuracy Metrics:** Sensitivity, Specificity, and Validation data (Ground Truth vs. Prediction).
*   **Why:** The agent reads this to ensure the PRD is *feasible*. It prevents hallucinating "magic" features that the algorithm cannot support (e.g., "Instant BP reading without calibration").

### 3. Competitor Analysis (The "Benchmark")
*   **Location:** `/product_specs/target_performance`
*   **Required Content:**
    *   **Competitor Data:** Performance metrics of key rivals (e.g., Apple Watch Hypertension Validation Paper).
    *   **Feature Gaps:** Where do they succeed? Where do they fail?
    *   **Regulatory Status:** Are they FDA-cleared (SaMD) or General Wellness?
*   **Why:** The agent uses this to position your product strategically. It will highlight where you outperform (e.g., "Higher Sensitivity") and where you differentiate (e.g., "Zero Calibration").

### 4. Regulatory Guidelines (The "Rules")
*   **Location:** `/FDA_wellness_guidelines`
*   **Required Content:**
    *   **Current Guidance:** The definitive rulebook for your product category (e.g., "FDA General Wellness Policy for Low Risk Devices").
    *   **Updates:** Any recent changes (e.g., "Jan 2026 Update").
*   **Why:** The agent strictly adheres to these rules to ensure the PRD is *compliant*. It will automatically adjust language (e.g., using "Wellness Range" instead of "Hypertension Diagnosis") to avoid regulatory pitfalls.

---

## 🧠 The "Chief of Staff" Brain (Skills)

This repository is powered by a set of specialized AI skills located in `/skills`:

*   **`feature-spec-skill.md`:** The master orchestrator. It synthesizes all the above inputs to generate the final PRD.
*   **`product-narrative-skill.md`:** Channels Steve Jobs/Brian Chesky to write a "Working Backwards" press release that sells the *dream*.
*   **`acceptance-criteria-skill.md`:** Writes rigorous, Gherkin-style acceptance criteria (Given/When/Then) to ensure engineering feasibility.
*   **`cuj-generator-skill.md`:** Creates detailed Critical User Journeys with priorities and requirements.
*   **`visualization-skill.md`:** Generates code to visualize the user experience.

---

## Getting Started

1.  **Populate the Folders:** Add your specific project documents to the 4 input directories above.
2.  **Activate the Skill:** Ask the agent: *"Create a PRD for [Your Feature Name]."*
3.  **Iterate:** The agent will ask clarifying questions, then generate a comprehensive PRD that balances Vision, Reality, and Compliance.
