# Product Guidelines

## 1. Prose Style & Tone
*   **Professional & Concise:** Information must be clear, direct, and actionable for engineering and product teams.
*   **Inspirational & Visionary:** Use evocative language ("magical," "guardian," "invisible") to sell the product dream and motivate the team.
*   **Empathetic & User-Centric:** Focus on the user's emotional state ("anxiety," "peace of mind," "intuition") to ensure features solve real human problems.

## 2. Terminology & Brand Language
*   **Preferred Terms:** "Wellness Range," "Lifestyle Trends," "Green/Amber Aura," "Shifted," "Check In."
*   **Prohibited Terms:** "Hypertension Diagnosis," "Stage 1/2 Hypertension," "Red Alarm/Alert," "Medical Device."
*   **Core Metaphors:**
    *   **"Invisible Guardian":** The product protects without intruding.
    *   **"Compass":** It guides directionally rather than measuring absolutely.
    *   **"Intuition":** It feels like a natural sense, not a data feed.

## 3. Documentation Standards
*   **Acceptance Criteria:** Must strictly follow the **Gherkin Syntax** (`Given/When/Then`) to ensure testability.
*   **Structured Data:** All lists of Critical User Journeys (CUJs), Metrics, and Requirements must be presented in **Markdown Tables**.
*   **Narrative First:** Every PRD must begin with a **"Working Backwards" Press Release** to ground the feature in customer value.
*   **File Structure:** Use `tree`-style visual diagrams to document folder hierarchies.

## 4. Regulatory Compliance
*   **Mandatory Disclaimer:** Every PRD must include the standard FDA General Wellness disclaimer in the "Intended Use" section.
*   **Contextual Guardrails:** The agent must actively warn and correct language that veers into "medical device" claims (e.g., diagnosing disease).

## 5. Success Metrics for Documentation
*   **Clarity:** A new engineer must be able to implement the feature without needing clarification.
*   **Inspiration:** The document should excite the reader about the product vision.
*   **Compliance:** Zero regulatory violations or "medical" claims.
*   **Actionability:** QA must be able to write test cases directly from the Acceptance Criteria.
