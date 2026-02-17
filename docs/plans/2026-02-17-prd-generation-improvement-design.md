# PRD Generation System Improvement Design

**Date:** February 17, 2026
**Author:** Design Session with User
**Status:** Approved for Implementation

---

## Executive Summary

This design transforms the PRD generation system from producing disconnected, technically-focused documents into creating unified narratives that inspire executives, engage stakeholders, and guide engineers with precision. The system will generate PRDs that deliver the **holy trinity**: Inspiration + Empathy + Clarity, while being scalable for any team to adopt.

**Key Innovations:**
1. **Narrative Thread Architecture** - Sections build on each other with context handoffs
2. **Three New Skills** - Strategy Ladder, Health Impact, Validation Rigor
3. **Context Manifest System** - Scalable, context-agnostic design for reusability
4. **Coherence Validation** - Automated checks ensure narrative consistency

**Expected Outcome:** PRDs that read like a journey document - starting with "why this matters to humanity," building through vision and validation, culminating in precise implementation specs - while serving executives, stakeholders, and engineers equally well.

---

## Problem Statement

### Current State Gaps

The existing PRD generation system produces technically accurate documents but fails in critical ways:

1. **❌ Weak Narrative** - Press releases lack "wow factor" and visionary energy despite having "7-Star Experience" methodology in skills
2. **❌ Disconnected Sections** - Each section (narrative, CUJs, specs) feels like separate documents stapled together
3. **❌ Vague Function Specs** - Requirements too high-level; engineers still need to ask "but how exactly?"
4. **❌ Missing Strategic Context** - No connection to company mission or market positioning
5. **❌ Missing Health Impact** - Doesn't articulate what changes in users' lives or health outcomes
6. **❌ Insufficient Validation Rigor** - Performance data and competitive analysis buried, leading to "it's just general wellness" perception
7. **❌ Not Scalable** - Hardcoded paths and context make it unusable by other teams

### User Requirements

PRDs must achieve:
- **A) Inspiration** - Steve Jobs keynote energy that makes builders want to change the world
- **B) Empathy** - Visceral user pain that drives urgency to solve
- **C) Clarity** - Crystal-clear specs enabling implementation without questions
- **D) Journey Document** - Progressive detail serving all audiences (execs → stakeholders → engineers)
- **E) Strategic Grounding** - Clear connection to mission and measurable health impact
- **F) Validation Credibility** - Clinical-grade rigor that dispels "lower bar" myths
- **G) Scalability** - Anyone can clone, add their context, and generate excellent PRDs

---

## Design Approach: The Narrative Thread

### Philosophy

Treat the PRD as a **single story with escalating detail**, not separate sections. Every section answers a natural question that flows from the previous insight, creating an emotional and intellectual journey.

### Architecture Overview

```
User Request
    ↓
Orchestrator Agent (Enhanced)
    ↓
┌─────────────────────────────────────────────────────┐
│  Context Discovery (NEW)                            │
│  - Reads CONTEXT_MANIFEST.md                        │
│  - Loads available context files                    │
│  - Resolves {{VARIABLES}}                           │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Story Arc Framework (NEW)                          │
│  - Defines narrative questions for each section     │
│  - Tracks context passed between skills             │
│  - Manages emotional progression                    │
└─────────────────────────────────────────────────────┘
    ↓
Sequential Skill Invocation with Context Handoff:
    ↓
0. Executive Summary (Orchestrator Direct)
1. Intended Use & Indications (Orchestrator Direct)
2. strategy-ladder-skill (NEW)
3. health-impact-skill (NEW)
4. product-narrative-skill (ENHANCED)
5. Problem & Opportunity (Orchestrator Direct)
6. validation-rigor-skill (NEW)
7. cuj-generator-skill (ENHANCED)
8. acceptance-criteria-skill (ENHANCED)
9. Success Metrics (Orchestrator Direct)
    ↓
┌─────────────────────────────────────────────────────┐
│  Coherence Validator (NEW)                          │
│  - Checks terminology consistency                   │
│  - Validates narrative references flow through      │
│  - Ensures strategic themes appear in all sections  │
│  - Verifies emotional arc progression              │
└─────────────────────────────────────────────────────┘
    ↓
Final PRD with Unified Narrative
```

### Key Design Decisions

1. **Sequential execution** (not parallel) - Each skill needs context from previous sections
2. **Orchestrator injects handoff prompts** - Ensures narrative continuity
3. **Some sections stay in orchestrator** - Executive Summary, Problem, Metrics synthesize multiple inputs
4. **Coherence validation at end** - Faster generation, cleaner validation
5. **Context manifest system** - Makes entire system reusable and scalable

---

## The Story Arc Framework

### Narrative Questions & Emotional Beats

Each section answers a specific question that naturally follows from the previous section:

```
┌──────────────────────────────────────────────────────────────┐
│ THE NARRATIVE ARC                                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ 0. EXECUTIVE SUMMARY                                        │
│    Question: "What is this and why does it matter?"         │
│    Content: • What we're building (1 sentence)              │
│             • Why we're building it (strategic rationale)   │
│             • Expected outcome (health + business impact)   │
│             • Owner, Status, Last Updated                   │
│    Emotional Beat: Instant Clarity                          │
│    Audience: Executives, Skip-Level Reviews                 │
│    Length: 3-4 sentences max                                │
│                                                              │
│ 1. INTENDED USE & INDICATIONS                               │
│    Question: "Who is this for and what can it claim?"       │
│    Content: • Intended Use statement (regulatory)           │
│             • Indications for use                           │
│             • Contraindications (who should NOT use)        │
│             • Regulatory classification                     │
│    Emotional Beat: Safety & Boundaries                      │
│    Audience: Regulatory, Legal, Medical Affairs             │
│    Length: ~1 paragraph with bullet list                    │
│                                                              │
│ 2. STRATEGY LADDER                                          │
│    Question: "Why does this matter to our mission?"         │
│    Content: • Mission alignment                             │
│             • Market positioning                            │
│             • Strategic differentiation                     │
│             • Success at scale                              │
│    Emotional Beat: Purpose & Ambition                       │
│    Audience: Executives, Team Motivation                    │
│    Length: 150-200 words                                    │
│                                                              │
│ 3. HEALTH IMPACT                                            │
│    Question: "What changes in users' lives?"                │
│    Content: • Target health outcomes (measurable)           │
│             • Behavior change goals                         │
│             • Downstream health effects                     │
│             • Clinical evidence base                        │
│    Emotional Beat: Hope & Human Impact                      │
│    Audience: Stakeholders, Medical Affairs                  │
│    Length: 200-250 words                                    │
│                                                              │
│ 4. PRESS RELEASE (7-Star Vision)                           │
│    Question: "What's the dream experience?"                 │
│    Content: • Problem (visceral)                            │
│             • Solution (7-Star magic)                       │
│             • Internal quote (mission)                      │
│             • Customer quote (delight)                      │
│    Emotional Beat: Inspiration & Desire                     │
│    Audience: Everyone - The North Star                      │
│    Length: ~1 page                                          │
│                                                              │
│ 5. PROBLEM & OPPORTUNITY                                    │
│    Question: "Why is the status quo broken?"                │
│    Content: • Current state (anxiety gap)                   │
│             • User insight                                  │
│             • Differentiation                               │
│    Emotional Beat: Frustration → Relief                     │
│    Audience: Product Team, Investors                        │
│    Length: 200-300 words                                    │
│                                                              │
│ 6. VALIDATION & COMPETITIVE RIGOR                           │
│    Question: "How do we know this actually works and        │
│               beats alternatives?"                          │
│    Content: • Target Performance (clinical benchmarks)      │
│             • Current Performance (where we are)            │
│             • Performance Gap (what to close)               │
│             • Validation Plan (studies, sample, GT)         │
│             • Competitive Analysis (head-to-head)           │
│    Emotional Beat: Credibility & Confidence                 │
│    Audience: Medical Affairs, Regulatory, Leadership,       │
│              Skeptical Engineers                            │
│    Length: 300-400 words + tables                           │
│                                                              │
│ 7. CRITICAL USER JOURNEYS                                   │
│    Question: "How do users experience the magic?"           │
│    Content: • CUJ header (user, goal, context)              │
│             • Journey map (tasks)                           │
│             • Health metrics                                │
│             • Emotional journey                             │
│    Emotional Beat: Clarity & Confidence                     │
│    Audience: Design, Product, UX Research                   │
│    Length: ~2 pages with tables                             │
│                                                              │
│ 8. FUNCTIONAL REQUIREMENTS                                  │
│    Question: "What exactly must we build?"                  │
│    Content: • Feature logic definitions                     │
│             • Gherkin scenarios (Given/When/Then)           │
│             • Requirements traceability                     │
│             • Non-functional requirements                   │
│    Emotional Beat: Precision & Feasibility                  │
│    Audience: Engineering, QA                                │
│    Length: 2-3 pages with structured tables                 │
│                                                              │
│ 9. SUCCESS METRICS                                          │
│    Question: "How do we know it worked?"                    │
│    Content: • HEART metrics                                 │
│             • Health outcome metrics                        │
│             • Business metrics                              │
│             • Launch gates                                  │
│    Emotional Beat: Accountability & Validation              │
│    Audience: Leadership, Analytics, Ops                     │
│    Length: ~1 page with table                               │
└──────────────────────────────────────────────────────────────┘
```

### Context Handoff Protocol

When the orchestrator invokes each skill, it includes:

**Input Context:**
- Summary of previous section (2-3 sentences)
- Key terms/concepts to reference
- The narrative question this section must answer
- Relevant context variables from manifest

**Output Requirements:**
- Opening sentence must reference previous section's insight
- Closing sentence must tee up next section's question
- Use consistent terminology from context

**Example Handoff (Strategy → Health Impact):**
```
Input to health-impact-skill:
"Given that this feature advances our mission to 'democratize
preventive care' and positions us as 'the only passive,
calibration-free solution,' what specific health outcomes
and behavior changes will users experience?"

Output from health-impact-skill must include:
- Opening: "To democratize preventive care at scale, we target..."
- Closing: "These health outcomes come to life through the
  following user experience..."
```

### Emotional Arc Mapping

The document follows an emotional journey:
- **Sections 0-3:** Inspiring (Purpose → Hope → Dream)
- **Section 4:** Grounding (The Real Problem)
- **Sections 5-6:** Building Confidence (Validation + Competition)
- **Sections 7-9:** Execution (How → What → Proof)

This ensures executives get inspired early, stakeholders gain confidence in rigor, then engineers get clarity for implementation.

---

## New Skills Design

### Skill 1: Strategy Ladder

**File:** `skills/strategy-ladder-skill.md`

**Purpose:** Connect the feature to company mission, market positioning, and strategic differentiation.

**Input Context:**
- `{{COMPANY_MISSION}}` - From context manifest
- `{{COMPANY_STRATEGY}}` - From context manifest
- `{{COMPETITIVE_LANDSCAPE}}` - Optional from context manifest
- User request

**Output Structure:**
```markdown
## Strategic Positioning

### Mission Alignment
[How this feature advances the company's core mission]

### Market Positioning
[Where this positions us in the competitive landscape]
- Category definition
- Unique positioning
- Strategic moat

### Strategic Differentiation
[What makes this approach different and better]

### Success at Scale
[What success looks like strategically]
```

**Key Characteristics:**
- 150-200 words (concise but meaty)
- Visionary language ("democratize", "reimagine", "unlock")
- References specific strategic docs when available
- Must answer: "If this works, what becomes possible that wasn't before?"

**Fallback Behavior:**
- If mission context missing → Ask user: "What is your company's core mission?"
- If strategy context missing → Use generic positioning language

---

### Skill 2: Health Impact

**File:** `skills/health-impact-skill.md`

**Purpose:** Define measurable health outcomes and behavior change goals.

**Input Context:**
- `{{STRATEGIC_POSITIONING}}` - From strategy-ladder-skill
- `{{USER_PERSONAS}}` - From context manifest
- `{{USER_PAIN_POINTS}}` - From context manifest
- Clinical literature (if available)

**Output Structure:**
```markdown
## Health Impact & Outcomes

### Target Health Outcomes
**Primary Outcome:**
- [Main health metric] - [Expected change]
- Measurement: [How we'll measure]
- Timeline: [When we expect to see impact]

**Secondary Outcomes:**
- [Supporting metrics with expected changes]

### Behavior Change Goals
| Current Behavior | Target Behavior | Intervention | Expected Adoption |
|:-----------------|:----------------|:-------------|:------------------|
| [Baseline] | [Desired] | [Mechanism] | [Metric] |

### Downstream Health Effects
[Longer-term population health implications]

### Clinical Evidence Base
[Research that supports these expectations]
```

**Key Characteristics:**
- 200-250 words
- Balances aspiration with evidence-based realism
- Includes equity lens (who might be excluded?)
- Must answer: "What changes in users' bodies/behaviors/lives?"

---

### Skill 3: Validation Rigor

**File:** `skills/validation-rigor-skill.md`

**Purpose:** Demonstrate clinical/scientific rigor through performance targets, validation plans, and competitive analysis.

**Input Context:**
- Product concept
- `{{CURRENT_PERFORMANCE}}` - From context manifest
- `{{VALIDATION_PLAN}}` - From context manifest
- `{{COMPETITIVE_LANDSCAPE}}` - From context manifest
- Regulatory classification

**Output Structure:**
```markdown
## Validation & Competitive Rigor

### Target Performance
[Clinical benchmarks we're measuring against]
[Table: Metric | Target | Clinical Rationale | Source]

### Current Performance
[Where we are today with full transparency]
[Table: Metric | Current | 95% CI | Status vs Target]

### Validation Plan
**Study Design:**
- Sample size & power
- Ground truth methodology
- Study duration
- Endpoints
- Subgroup analyses

**Timeline & Milestones:** [Key dates]

### Competitive Analysis
[Head-to-head comparison table]

**Differentiation Summary:** [3-5 bullets]
**Competitive Risks:** [What could close the gap?]
```

**Key Characteristics:**
- 300-400 words (most detailed skill)
- Includes tables for scannability
- Balances confidence with transparency about gaps
- Must answer: "Why should anyone believe this will work?"

---

## Enhancements to Existing Skills

### Enhanced: Product Narrative Skill

**File:** `skills/product-narrative-skill.md`

**Additions:**

```markdown
## Input Context (NEW)
- `{{STRATEGIC_POSITIONING}}` - From strategy-ladder-skill
- `{{HEALTH_OUTCOMES}}` - From health-impact-skill
- `{{USER_PERSONAS}}` - From context manifest
- `{{PROHIBITED_TERMS}}` - From regulatory context

**Handoff from Previous Section:**
"Given these health outcomes, the press release must..."

## Narrative Integration Requirements (NEW)

**Opening Connection:**
Your press release MUST reference the strategic positioning established earlier.

**7-Star Experience Selection:**
When choosing your 7-Star moment, ensure it connects to the primary health outcome.

**Prohibited Terms Check:**
Before outputting, validate against `{{PROHIBITED_TERMS}}` list.

## Output Handoff (NEW)
**Closing Sentence Template:**
"This vision addresses a critical problem: [tee up problem section]"

**Pass Forward:**
- Core metaphor (e.g., "Guardian", "Compass")
- Target emotion (e.g., "Peace of mind")
- Key differentiator (e.g., "Calibration-free")
```

---

### Enhanced: CUJ Generator Skill

**File:** `skills/cuj-generator-skill.md`

**Additions:**

```markdown
## Input Context (NEW)
- `{{PRESS_RELEASE_METAPHOR}}` - Core metaphor from narrative
- `{{HEALTH_OUTCOMES}}` - Behaviors we're changing
- `{{PROBLEM_STATEMENT}}` - Pain points the CUJ addresses
- `{{USER_PERSONAS}}` - Target user from context

**Handoff from Previous Section:**
"To deliver this experience, users must be able to..."

## Narrative Integration Requirements (NEW)

**CUJ Naming:**
Use language from the press release metaphor.

**Task-to-Outcome Mapping:**
For each CUJ, explicitly map tasks to health outcomes.

| Task | Health Outcome Enabled | Behavior Change |
|:-----|:-----------------------|:----------------|
| ... | ... | ... |

**Emotional Journey:**
Add a "User Emotion" column showing how the user feels at each step.

## Output Handoff (NEW)
**Closing Sentence Template:**
"To enable these journeys, the system must implement the following requirements..."

**Pass Forward:**
- Critical interactions (CUIs) that need detailed specs
- Edge cases discovered in journey mapping
- Performance expectations
```

---

### Enhanced: Acceptance Criteria Skill

**File:** `skills/acceptance-criteria-skill.md`

**Additions:**

```markdown
## Input Context (NEW)
- `{{CUJ_CRITICAL_INTERACTIONS}}` - CUIs that need specs
- `{{EDGE_CASES}}` - Scenarios from CUJ mapping
- `{{HEALTH_OUTCOMES}}` - What system must enable
- `{{REGULATORY_CONSTRAINTS}}` - Terms/behaviors to avoid

**Handoff from Previous Section:**
"To enable these user journeys, the system requires..."

## Narrative Integration Requirements (NEW)

**Requirements Traceability:**
Every functional requirement MUST trace back to:
1. A specific CUJ task
2. A health outcome it enables
3. A regulatory constraint it satisfies (if applicable)

**Traceability Table:**
| Req ID | CUJ Task | Health Outcome | Regulatory Note |
|:-------|:---------|:---------------|:----------------|
| ... | ... | ... | ... |

**Language Consistency:**
Use the same terminology from press release and CUJs.

**Gherkin Scenarios with Context:**
Enhance Given/When/Then with emotional/health context.

## Output Handoff (NEW)
**Closing Sentence Template:**
"Success for these requirements is measured by the following metrics..."
```

---

## Scalable Context Architecture

### The Problem
Current system has hardcoded paths that break when others try to use it.

### The Solution: Context Manifest System

#### Standardized Knowledge Folder Structure

```
PRD-generator/
├── knowledge/               # All project-specific context
│   ├── CONTEXT_MANIFEST.md # The "map" of available context
│   ├── company/            # Company-specific context
│   │   ├── mission.md      # Mission, vision, values
│   │   ├── strategy.md     # Market strategy, positioning
│   │   └── brand.md        # Brand guidelines, terminology
│   ├── product/            # Product-specific context
│   │   ├── overview.md     # Product description
│   │   ├── competitive.md  # Competitive landscape
│   │   └── tech-stack.md   # Technical constraints
│   ├── regulatory/         # Compliance & regulatory
│   │   ├── classification.md
│   │   └── prohibited-terms.md
│   ├── user-research/      # User insights
│   │   ├── personas.md
│   │   ├── pain-points.md
│   │   └── survey-data.md
│   └── validation/         # Performance & validation
│       ├── current-performance.md
│       └── validation-plan.md
```

#### Context Manifest File

**File:** `knowledge/CONTEXT_MANIFEST.md`

Acts as the "index" telling the orchestrator what context exists:

```markdown
---
# Context Manifest
# Maps context categories to files in knowledge/ directory
---

## Company Context
- **mission**: `knowledge/company/mission.md` - Company mission, vision
- **strategy**: `knowledge/company/strategy.md` - Market positioning
- **brand**: `knowledge/company/brand.md` - Brand voice, terminology

## Product Context
- **overview**: `knowledge/product/overview.md` - Product description
- **competitive**: `knowledge/product/competitive.md` - Competitors
- **tech-stack**: `knowledge/product/tech-stack.md` - Tech constraints

## Regulatory Context
- **classification**: `knowledge/regulatory/classification.md`
- **prohibited-terms**: `knowledge/regulatory/prohibited-terms.md`
- **indications**: `knowledge/regulatory/indications.md`

## User Research
- **personas**: `knowledge/user-research/personas.md`
- **pain-points**: `knowledge/user-research/pain-points.md`
- **insights**: `knowledge/user-research/insights.md`

## Validation Data
- **performance**: `knowledge/validation/current-performance.md`
- **validation-plan**: `knowledge/validation/validation-plan.md`
- **clinical-evidence**: `knowledge/validation/clinical-evidence.md`
```

#### Context-Aware Orchestrator

**Update:** `agents/prd_orchestrator_agent.md`

**New "Context Discovery" Protocol:**

```markdown
## Context Discovery Protocol

**CRITICAL FIRST STEP:** Before generating any PRD section:

1. **Read the Context Manifest:**
   - File: `{repo_root}/knowledge/CONTEXT_MANIFEST.md`
   - Tells you what context files exist

2. **Load Required Context:**
   - Load relevant context files based on manifest
   - If missing, note it and proceed with available context
   - DO NOT fail if context missing - adapt gracefully

3. **Context Variables:**
   Use these variables when invoking skills:
   - `{{COMPANY_MISSION}}` → Contents of mission file
   - `{{USER_PERSONAS}}` → Contents of personas file
   - `{{REGULATORY_TERMS}}` → Contents of prohibited-terms file
   - `{{COMPETITIVE_LANDSCAPE}}` → Contents of competitive file

4. **Graceful Degradation:**
   - If context doesn't exist, use generic language
   - If critical context missing, ask user for info
   - Document what context was missing in PRD footnote
```

#### Setup Script for New Users

**New file:** `setup.sh`

```bash
#!/bin/bash
# PRD Generator Setup Script

echo "🚀 Setting up PRD Generator for your project..."

# Create knowledge folder structure
if [ ! -d "knowledge" ]; then
    echo "Creating knowledge/ folder structure..."
    mkdir -p knowledge/{company,product,regulatory,user-research,validation,custom}
fi

# Create manifest template
if [ ! -f "knowledge/CONTEXT_MANIFEST.md" ]; then
    echo "Creating Context Manifest template..."
    cp templates/CONTEXT_MANIFEST.template.md knowledge/CONTEXT_MANIFEST.md
fi

# Create example files
if [ ! -f "knowledge/company/mission.md" ]; then
    echo "Creating example context files..."
    cp templates/examples/*.md knowledge/
fi

echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit knowledge/CONTEXT_MANIFEST.md to map your context files"
echo "2. Add your company/product context to knowledge/ folders"
echo "3. Run: claude agents/prd_orchestrator_agent.md"
```

### How This Makes It Scalable

✅ **Anyone can use it:** Clone → Run setup → Fill context
✅ **Context-agnostic:** Skills use `{{VARIABLES}}` not hardcoded paths
✅ **Graceful degradation:** Works with minimal or full context
✅ **Extensible:** Add new context categories to manifest
✅ **Self-documenting:** Manifest shows what context exists

---

## Coherence Validation Logic

After all sections are generated, the orchestrator runs automated coherence checks.

### Coherence Validator (New in Orchestrator)

```markdown
## Coherence Validation Protocol

After generating all PRD sections, validate narrative consistency:

### Check 1: Terminology Consistency
**Scan for:** Core metaphor appears in 80%+ of sections
- Strategy: "democratize preventive care"
- Health Impact: "preventive care at scale"
- Press Release: "democratize heart health"
- CUJs: "preventive protection"
- Requirements: "preventive care mode"

**Action if fails:** Highlight inconsistencies, offer batch replace

### Check 2: Forbidden Terms
**Scan for:** `{{PROHIBITED_TERMS}}` appearing anywhere
- "Monitor" → Flag and suggest "Track"
- "Diagnose" → Flag and suggest "Provide insights"

**Action if fails:** Auto-replace with approved alternatives

### Check 3: Narrative References
**Check that:**
- Health Impact section references Strategy
- Press Release references Health Outcomes
- Problem section references Press Release metaphor
- CUJs reference Problem pain points
- Requirements reference CUJ tasks

**Action if fails:** Insert connecting sentences

### Check 4: Metric Alignment
**Verify:**
- Health outcomes have corresponding success metrics
- CUJ tasks have instrumentation defined
- Requirements have acceptance criteria

**Action if fails:** Generate missing metrics/criteria

### Check 5: Audience Progression
**Verify emotional arc:**
- Sections 0-3: Inspiring tone (execs/stakeholders)
- Sections 4-6: Balanced (product team)
- Sections 7-9: Precise (engineering)

**Action if fails:** Adjust tone in flagged sections
```

---

## Implementation Plan

### Phase 1: Foundation (Week 1)
1. Create scalable context architecture
   - Set up knowledge/ folder structure
   - Write CONTEXT_MANIFEST.md template
   - Create setup.sh script
   - Build template files
2. Migrate existing context to new structure
3. Test context variable resolution

### Phase 2: New Skills (Week 2)
1. Write strategy-ladder-skill.md
2. Write health-impact-skill.md
3. Write validation-rigor-skill.md
4. Test each skill independently with sample context

### Phase 3: Skill Enhancements (Week 2-3)
1. Enhance product-narrative-skill.md with context integration
2. Enhance cuj-generator-skill.md with handoffs
3. Enhance acceptance-criteria-skill.md with traceability
4. Test skill chaining with handoffs

### Phase 4: Orchestrator Updates (Week 3)
1. Add Context Discovery Protocol
2. Add Story Arc Framework
3. Implement context handoff logic
4. Add section synthesis (Executive Summary, Problem, Metrics)

### Phase 5: Coherence Validation (Week 4)
1. Build terminology consistency checker
2. Build forbidden terms scanner
3. Build narrative reference validator
4. Build metric alignment checker
5. Build tone progression validator

### Phase 6: Integration Testing (Week 4)
1. Generate test PRD end-to-end
2. Validate all narrative connections
3. Check coherence validation catches issues
4. Refine based on results

### Phase 7: Documentation & Launch (Week 5)
1. Write comprehensive README
2. Create video walkthrough
3. Document context manifest system
4. Share with early adopters for feedback

---

## Success Metrics

### Quality Metrics (Per PRD Generated)
- **Narrative Coherence Score:** 90%+ (automated validation passes)
- **Terminology Consistency:** Core metaphor appears in 80%+ sections
- **Traceability:** 100% of requirements trace to CUJs/health outcomes
- **Forbidden Terms:** 0 violations in final output

### User Experience Metrics
- **Setup Time:** New user can generate first PRD in < 30 minutes
- **Context Reusability:** Same context used for 5+ PRDs without modification
- **Adoption:** 3+ teams using system within 3 months

### Document Quality (Subjective Review)
- **Inspiration:** 4.5/5 rating from executives on "makes me want to build this"
- **Clarity:** 4.5/5 rating from engineers on "I know exactly what to build"
- **Completeness:** 90%+ of PRD review comments are "nice-to-have" not "missing critical info"

---

## Risks & Mitigations

### Risk 1: Context Overload
**Risk:** Users don't know what context to provide
**Mitigation:** Setup script creates example files; skills work with minimal context

### Risk 2: Narrative Feels Forced
**Risk:** Handoffs feel artificial, not natural
**Mitigation:** Make handoffs optional; validate with test PRDs; iterate on prompts

### Risk 3: Too Complex for Simple PRDs
**Risk:** System is overkill for small features
**Mitigation:** Orchestrator detects "small feature" requests and uses lightweight mode

### Risk 4: Coherence Validation Too Strict
**Risk:** Validator flags false positives
**Mitigation:** Make validation warnings, not errors; allow user override

---

## Appendix: Example Context Files

### Example: mission.md

```markdown
# Company Mission

**Mission Statement:**
Democratize preventive healthcare by making advanced health monitoring
accessible, affordable, and anxiety-free for everyone.

**Vision:**
A world where people have intuitive, continuous insight into their health
without the burden of medical devices or clinical visits.

**Values:**
- User-first design
- Clinical rigor
- Regulatory responsibility
- Inclusive innovation
```

### Example: personas.md

```markdown
# Target User Personas

## Proactive Adopter (Primary)
- **Age:** 30-50
- **Behavior:** Health-conscious, tech-forward, anxiety-prone
- **Goal:** Prevention without medicalization
- **Pain Point:** Hates traditional medical experiences (white coat syndrome)
- **Motivation:** Peace of mind, control over health

## Motivated by Diagnosis (Secondary)
- **Age:** 45-65
- **Behavior:** Recently diagnosed, seeking management tools
- **Goal:** Track condition without daily burden
- **Pain Point:** Traditional cuffs are inconvenient
- **Motivation:** Stay out of doctor's office
```

---

**End of Design Document**
