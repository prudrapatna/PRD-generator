---
name: prd-standard-skill
description: Defines the structure and content rules for a Mini/Short PRD (also called "Mini Product Narrative"). Used by the prd-agent orchestrator when the user asks for a condensed overview rather than a full PRD.
version: 2.0.0
---

# PRD Standard Skill — Mini Product Narrative Format

## Scope
This skill defines the **Mini PRD** format. It is invoked by `prd-agent-skill.md` when the user requests a "mini product overview," "short PRD," "product narrative," or "one-pager." It produces a crisp, board-ready document: a PR + product grid + 9 Things + next steps. No acceptance criteria. No CUJ maps. No algorithm grids.

---

## When This Skill is Active

Triggered by `prd-agent-skill.md` in Mini mode. Do NOT use this skill for full PRDs.

---

## Output Structure

### 1. Press Release [PR]
**[REQUIRED: NARRATIVE — FULL BORDER BOX]**
- The entire PR is enclosed in a single-cell bordered table (1–1.5pt solid black, all four sides).
- Header 1: Program name.
- Header 2: "Google's Personal Health Assistant Is Learning to Spot — and May Help Reverse — [Program Name] Trends."
- Dateline: "[Month Day, Year]:"
- Paragraph 1: The invisible/silent nature of the health signal. Positive framing — opportunity, not fear.
- Paragraph 2: "[Program Name], a new wellness feature for Pixel Watch and Fitbit devices." No behavior change required.
- Paragraph 3: "Most months, users won't hear from it..." Quiet approach.
- Quote 1: Rishi Chandra, VP Google Health — visionary mission quote.
- Quote 2: Relevant clinical expert — clinical validation quote.
- Closing: "Designed to start conversations, not replace care." "One thoughtful insight a month."

### 2. Overview
**[REQUIRED: NARRATIVE — 2–3 paragraphs]**
- Paragraph 1: The problem. Why is this signal invisible? What % of people are affected? (Use data from `knowledge/user_research/`.)
- Paragraph 2: The solution summary. What does this feature do and not do?
- Paragraph 3: Why now / why Google / why wearables?

### 3. Target Product Profile (The Master Grid)
**[REQUIRED: TABLE]** Two columns: Category | Definition

| Category | Definition |
| :--- | :--- |
| Intended Use Statement | ... |
| Disclaimer | ... |
| Problem Statement | ... |
| Product Overview (P0/P1) | ... |
| Product Output (P0/P1) | ... |
| Positioning (The "North Star") | ... |
| Product Type | ... |
| Assessment Period | ... |
| Regulated or Wellness? | ... |
| Target Segment | ... |
| Contraindication | ... |
| Product Inputs | ... |
| Supported Devices | ... |
| Country Availability | ... |

Fill every row with specifics from the knowledge/ files. No empty cells.

### 4. Market Positioning: The Personal Health Assistant (9 Things)
**[REQUIRED: 2-COLUMN TABLE]**
Apply `tidal-master-template-skill.md` §4 format exactly:
- Left column (~1.5"): Large blue number (20–24pt, bold) + tagline below (11pt, bold, blue) — stacked in same cell.
- Right column (~5"): Description. Normal body font, black text.
- Horizontal border between every row. Outer border on all sides.

Exactly 9 rows:
1. [Program Name] on PHA — what PHA is learning to spot
2. [Program Name] Significance — the awareness gap and why it matters
3. A First-of-its-Kind [feature type] — the innovation claim (verify against competitor_analysis.md)
4. How [Program Name] on PHA Works — mechanics (sensors, AI, monthly cadence)
5. Rigorous Testing & Validation — study size, gold-standard benchmark
6. AI in [Program Name] — model architecture, multimodal signals, false positive minimization
7. Launch Markets — countries and regulatory context
8. Enhanced Peace of Mind with PHA — ecosystem integration (BP Trends, heart rhythm, sleep)
9. [Program Name] Partners — clinical collaborators and expert validators

### 5. Summary: What's Next
**[REQUIRED: BULLETED LIST — 3–5 bullets]**
- Open questions to resolve before full PRD
- Key dependencies or risks
- Recommended immediate next steps

---

## Content Quality Rules
- **PR first.** Working Backwards is non-negotiable, even in mini mode.
- **No fabricated numbers.** Every % and $ must trace to `knowledge/user_research/` or `knowledge/[feature]/`.
- **No diagnostic language.** "Estimate," "Spot," "Trends," "Patterns" only.
- **Positive framing.** Opportunity and empowerment, not fear.
- **9 Things must be substantive.** Each description paragraph must be 2–4 sentences of real content, not placeholder text.
