# Skill: Presentation Generator (Health 2026 Style)

**Description:** Generates a structured presentation deck in Markdown format, mimicking the "Health 2026 working deck" style. This includes specific slide layouts for Title Slides, Section Dividers, Strategic Content, and Data Tables.
**Triggers:** "presentation", "deck", "slides"

---

## 1. Process
1.  **Analyze Context:** Infer the presentation topic, key audience, and primary goal from the user's request and any provided context files. **Only ask clarifying questions if the goal is completely ambiguous.**
2.  **Define Sections:** Break the narrative into clear sections (e.g., "Strategy", "Execution", "Metrics").
3.  **Generate Content:** Create slide content following the specific "Health 2026" formats described below.
4.  **Output:** Save the result as a Markdown file (e.g., `presentation.md`) using `---` to separate slides.

---

## 2. Slide Formats & Style Guidelines

### A. General Style
*   **Tone:** Professional, strategic, data-driven, and forward-looking.
*   **Headlines:** Use **Action-Oriented Titles** (full sentences that state the takeaway, not just "Update").
    *   *Bad:* "Q3 Metrics"
    *   *Good:* "We are improving our velocity with SWE productivity up 50% in 2025"
*   **Footer:** Include "Confidential & Proprietary" on internal strategy slides.

### B. Slide Types

#### 1. Title Slide
*   **Content:** Presentation Title, Subtitle/Context, Date.
*   **Format:** Minimalist.

#### 2. Section Divider (The "01, 02..." Slides)
*   **Content:**
    *   Large Section Number (e.g., "01")
    *   Section Title (e.g., "Top of funnel & positioning")
    *   **DRI:** "DRIs: [email@]" (Crucial detail from the reference deck)
*   **Purpose:** clearly delineate major shifts in topic.

#### 3. Strategic "3-Column" or "Grid" Slide
*   **Use for:** Pillars, Feature lists, Competitive Analysis.
*   **Format:**
    *   Action Headline
    *   3-4 Columns with Headers and bullet points.

#### 4. Quote/Feedback Slide
*   **Use for:** User research, press feedback, testimonials.
*   **Format:**
    *   Headline: "What we’ve learned so far..."
    *   Content: Grouped quotes ("The Good", "The Bad", "The Ugly") or distinct "Voice of User" blocks.

#### 5. Data/Table Slide
*   **Use for:** OKRs, Metrics, Roadmaps.
*   **Format:** Markdown tables with clear headers.
    *   *Columns:* Metric | Baseline | Target | Status

---

## 3. Output Template (Markdown)

```markdown
# [Presentation Title]
[Subtitle]
[Date]

---

# [Section Number e.g., 01]
## [Section Title]
**DRIs:** [names/emails]

---

# [Action-Oriented Headline for Slide 1]

*   **Key Point 1:** Detail...
*   **Key Point 2:** Detail...

> "Insert relevant quote or insight here."

*Footer: Confidential & Proprietary*

---

# [Action-Oriented Headline for Slide 2]

| Metric | Q1 Actual | Q2 Target |
| :--- | :--- | :--- |
| User Growth | 10% | 15% |
| Retention | 85% | 88% |

*Footer: Confidential & Proprietary*
```
