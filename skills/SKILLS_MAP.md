# Skills Directory Map

This map provides the routing logic and purpose for each agent skill.

---

## The Two PRD Modes

```
User Request
     │
     ├─── "mini PRD" / "mini product overview" / "short PRD" / "product narrative" / "one-pager"
     │         └──► MINI PRODUCT NARRATIVE MODE
     │
     └─── "PRD" / "write a PRD" / "full PRD" / any unqualified PRD request
               └──► FULL PRD MODE (default)
```

---

## Orchestrator

```
agents/prd_orchestrator_agent.md   [ORCHESTRATOR — START HERE]
    Purpose: Routes Full vs Mini mode. Reads knowledge/ first. Chains skills in order.
    Trigger: Any PRD or product narrative request.
```

---

## Full PRD Mode — Skill Chain

```
Step 1: product-narrative-skill.md  [VISIONARY]     — PR tone, 7-Star, Working Backwards
Step 2: marketing-skill.md          [MARKETER]      — 9 Things content + GTM positioning
Step 3: tidal-master-template-skill.md [FORMATTER]  — Structure, borders, column rules
Step 4: cuj-generator-skill.md      [STRATEGIST]    — CUJ Maps (4+ journeys)
Step 5: acceptance-criteria-skill.md [ARCHITECT]    — Gherkin AC, feature logic, NFRs
```

**Full PRD Sections:**
0. Metadata & Approvals
1. Press Release [PR] (border box)
2. Overview
3. Target Product Profile (Master Grid)
4. Market Positioning: 9 Things (2-column table)
5. Critical User Journeys (CUJ Maps)
6. Algorithm Target Performance
7. Feature Logic & Program Timeline
8. Acceptance Criteria (Gherkin)
9. Appendix, Disclaimers & Change Log

---

## Mini Product Narrative Mode — Skill Chain

```
Step 1: product-narrative-skill.md  [VISIONARY]     — PR tone, 7-Star, Working Backwards
Step 2: marketing-skill.md          [MARKETER]      — 9 Things content + GTM positioning
Step 3: tidal-master-template-skill.md [FORMATTER]  — Structure, borders, column rules
Step 4: prd-standard-skill.md       [MINI SPEC]     — Condensed structure + content rules
```

**Mini PRD Sections:**
1. Press Release [PR] (border box)
2. Overview (2–3 paragraphs)
3. Target Product Profile (Master Grid)
4. Market Positioning: 9 Things (2-column table)
5. Summary: What's Next (bullets)

---

## Shared Format Rules (Both Modes)

| Rule | Detail |
| :--- | :--- |
| PR Format | Single-cell bordered table, 1–1.5pt solid black, all four sides |
| 9 Things Format | 2-column table; left = large number (24pt, blue) + tagline stacked; right = description |
| Row Borders | Horizontal divider between every 9 Things row; outer border on all sides |
| Vocabulary | "Spot," "Estimate," "Patterns," "Trends" — NEVER "Monitor," "Diagnose" |
| Framing | Empowerment and opportunity — NEVER fear or danger |
| Data | Every % and $ must trace to knowledge/ files |

---

## Supporting Skills (Available On-Demand)

```
skills/cuj-generator-skill.md       [STRATEGIST]    — Full CUJ Maps (auto-used in Full PRD)
skills/acceptance-criteria-skill.md [ARCHITECT]     — Gherkin AC (auto-used in Full PRD)
skills/internal-comms-skill.md      [COMMUNICATOR]  — Launch emails, status updates
skills/presentation-skill.md        [DESIGNER]      — Pitch decks, strategy slides
skills/visualization-skill.md       [ILLUSTRATOR]   — Architecture diagrams, CUJ maps
skills/skill.md                     [TEMPLATE]      — Template for creating new skills
```

---

## Knowledge Reading Order (Before Any PRD)

```
1. knowledge/[feature-name]/          — Feature-specific data
2. knowledge/user_research/           — Conjoint, WTP, personas
3. knowledge/strategy/strategy_details.md
4. knowledge/Additional Context.md
5. FDA_wellness_guidelines/general_wellness_guideline.md
```
