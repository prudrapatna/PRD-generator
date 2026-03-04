# Design: Tidal Executive Summary PRD
**Date:** 2026-02-25

## Context
User requested an executive summary PRD for Project Tidal (Blood Pressure General Wellness Notification). Previous PRD iterations (v1–v8) were deleted from the working tree. This is a fresh synthesis from all knowledge sources.

## Requirements
- **Type:** Executive Summary (not full PRD)
- **Audience:** Cross-functional partners — Engineering, Legal, Marketing
- **Source:** Regenerated from all knowledge (v8 PRD, algorithm docs, user research, strategy)

## Chosen Approach: Organized by Function
Structure document by functional area so each partner reads their section without needing the whole doc.

**Sections:**
1. **TL;DR / One-Page Brief** — Metadata + 3-paragraph summary
2. **Product & Vision** — Press release, problem, competitive positioning, performance targets
3. **Legal & Regulatory** — Intended use verbatim, classification, bright lines, disclaimers, contraindications
4. **Engineering & Technical** — Architecture diagram, feature logic constants, SQI requirements, algorithm model summary, data models
5. **UX & Marketing** — Brand language rules, 3 CUJs, HEART metrics, 7-star experience benchmark

## Output
`product_specs/blood-pressure-trends/Tidal-Executive-Summary-v2.md`

## Key Design Decisions
- Verbatim intended use statement surfaces prominently in Legal section
- Algorithm pipeline rendered as ASCII diagram for Engineering readability
- All regulatory bright lines as explicit table (not prose) for Legal reference
- 7-star experience benchmark included for Marketing/Design team alignment on the "right" notification experience
