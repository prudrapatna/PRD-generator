# Track Specification: Refactor product-narrative-skill.md

## 1. Goal
Update the `skills/product-narrative-skill.md` file to explicitly incorporate the "Visionary Philosophy" of Steve Jobs, Brian Chesky, and Elon Musk. The skill must guide the agent to generate narratives that prioritize "7-Star Experiences" and "Insanely Great" simplicity.

## 2. Requirements
*   **Philosophy Integration:**
    *   **Jobs:** "Customer Experience First," "Insanely Great & Simple," "Design as 'How It Works'," "Focus & Courage."
    *   **Chesky:** "The 7-Star Experience" (Magical, not just expected).
    *   **Musk:** "First Principles" thinking and ruthless simplification ("Delete the Part").
*   **Structure Update:** The skill must include a specific section titled "The Visionary Philosophy" that outlines these principles.
*   **Tone:** The skill itself should be written in an inspirational, directive tone ("You are a visionary Product Leader...").
*   **Output Format:** The "Press Release" format instructions must remain but be reinforced by these new philosophical guardrails.

## 3. Acceptance Criteria (Gherkin)

**Functional**
*   **Given** the `product-narrative-skill` is activated
    *   **When** the agent generates a PRD narrative
    *   **Then** the output explicitly references a "7-Star Experience" in the Solution section.
    *   **And** the narrative focuses on user emotion ("dreams," "magic") rather than technical specs.
*   **Given** the skill definition file
    *   **When** reviewed
    *   **Then** it contains a section "2. The Visionary Philosophy (Jobs, Chesky, Musk)".

## 4. Technical Implementation
*   **File:** `skills/product-narrative-skill.md`
*   **Action:** Rewrite the content to inject the new philosophy section and refine the existing instructions to match the "Visionary" tone.
