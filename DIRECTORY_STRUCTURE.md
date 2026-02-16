# Project Tidal Directory Structure

This document outlines the organization of the **Chief of Staff** repository.

## 📂 Visual Directory Tree

```
/Users/prudrapatna/Development/Chief of Staff/
├── FDA_wellness_guidelines/                   # Regulatory Guidance
│   ├── general_wellness_guideline.md
│   └── jan_2026_updates.md
│
├── algorithm_overview_and_target_performance/ # Technical Specs
│   └── algorithm_overview_and_target_performance.md
│
├── product_specs/                             # Product Artifacts
│   ├── prds/
│   │   ├── blood_pressure_wellness_v11.md     # Latest Visionary PRD
│   │   ├── design_system_rules.md             # Visual Language Rules
│   │   └── cujs/                              # Critical User Journeys
│   │       ├── blood_pressure_cuj_v9.md
│   │       └── blood_pressure_cuj_v9_visual.png
│   │
│   └── target_performance/                    # Benchmarks
│       ├── apple_hypertension_validation.pdf
│       └── target_performance.md
│
├── skills/                                    # AI Agent Capabilities
│   ├── feature-spec-skill.md                  # PRD Generator
│   ├── product-narrative-skill.md             # Visionary Writer
│   ├── acceptance-criteria-skill.md           # QA/Gherkin Writer
│   ├── cuj-generator-skill.md                 # User Journey Creator
│   ├── visualization-skill.md                 # UI/UX Visualizer
│   └── visual_gen_v9.py                       # Visual Generation Script
│
└── user_research/                             # User Insights
    ├── proactive_adopter_profile.md
    ├── hypertension_problem_definition.md
    └── survey_synthesis.md
```

---

## 📂 Folder Descriptions

### 1. `FDA_wellness_guidelines/`
*   **Purpose:** The "Rule Book." Contains definitive regulatory guidance documents.
*   **Key Files:**
    *   `general_wellness_guideline.md`: Core FDA policy for low-risk devices.
    *   `jan_2026_updates.md`: Latest compliance rules (e.g., "Wellness Range" language).

### 2. `algorithm_overview_and_target_performance/`
*   **Purpose:** The "Reality Check." Contains technical specifications, capabilities, and constraints.
*   **Key Files:**
    *   `algorithm_overview_and_target_performance.md`: Detailed specs (e.g., 14-day wear requirement, height input dependency, accuracy metrics).

### 3. `product_specs/`
*   **Purpose:** The "Output." Where all generated product artifacts live.
*   **Sub-directories:**
    *   `prds/`: Final Product Requirements Documents (e.g., `blood_pressure_wellness_v11.md`).
    *   `prds/cujs/`: Detailed Critical User Journeys and visuals.
    *   `target_performance/`: Competitive benchmarks (e.g., Apple Watch validation data).

### 4. `skills/`
*   **Purpose:** The "Brain." Contains the specialized instructions for the AI agent.
*   **Key Skills:**
    *   `feature-spec-skill.md`: The master skill for generating PRDs (Integrates Vision + Tech + FDA).
    *   `product-narrative-skill.md`: Generates "Jobsian/Chesky" visionary narratives.
    *   `acceptance-criteria-skill.md`: Generates rigorous Gherkin-style acceptance criteria.
    *   `cuj-generator-skill.md`: Creates detailed user journeys.
    *   `visualization-skill.md`: Generates UI/UX diagrams and visuals.

### 5. `user_research/`
*   **Purpose:** The "Why." Contains synthesized user insights and personas.
*   **Key Files:**
    *   `proactive_adopter_profile.md`: Target persona definition.
    *   `hypertension_problem_definition.md`: The core user problem we are solving.
    *   `survey_synthesis.md`: Findings from user validation.
