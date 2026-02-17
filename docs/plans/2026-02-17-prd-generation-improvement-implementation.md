# PRD Generation System Improvement - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform PRD generation system to produce unified narratives with Inspiration + Empathy + Clarity, making it scalable for any team.

**Architecture:** Narrative Thread Architecture with sequential skill invocation, context handoffs, and coherence validation. Context Manifest System enables scalability. Three new skills (Strategy Ladder, Health Impact, Validation Rigor) plus enhancements to three existing skills.

**Tech Stack:** Markdown-based skills, Claude Code agents, bash scripting for setup

---

## Phase 1: Foundation - Context Architecture

### Task 1: Create Knowledge Folder Structure

**Files:**
- Create: `knowledge/company/.gitkeep`
- Create: `knowledge/product/.gitkeep`
- Create: `knowledge/regulatory/.gitkeep`
- Create: `knowledge/user-research/.gitkeep`
- Create: `knowledge/validation/.gitkeep`
- Create: `knowledge/custom/.gitkeep`

**Step 1: Create knowledge folder structure**

```bash
mkdir -p knowledge/{company,product,regulatory,user-research,validation,custom}
touch knowledge/company/.gitkeep
touch knowledge/product/.gitkeep
touch knowledge/regulatory/.gitkeep
touch knowledge/user-research/.gitkeep
touch knowledge/validation/.gitkeep
touch knowledge/custom/.gitkeep
```

**Step 2: Verify folder structure**

Run: `tree knowledge -L 2`

Expected output:
```
knowledge
├── company
│   └── .gitkeep
├── product
│   └── .gitkeep
├── regulatory
│   └── .gitkeep
├── user-research
│   └── .gitkeep
├── validation
│   └── .gitkeep
└── custom
    └── .gitkeep
```

**Step 3: Commit folder structure**

```bash
git add knowledge/
git commit -m "feat: create knowledge folder structure for context files

Establishes standardized folder structure for project-specific context:
- company/ - Mission, strategy, brand guidelines
- product/ - Product overview, competitive analysis
- regulatory/ - Compliance, prohibited terms
- user-research/ - Personas, pain points, insights
- validation/ - Performance data, validation plans
- custom/ - Custom context categories

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 2: Create Context Manifest Template

**Files:**
- Create: `knowledge/CONTEXT_MANIFEST.md`

**Step 1: Write Context Manifest template**

Create file `knowledge/CONTEXT_MANIFEST.md`:

```markdown
---
# Context Manifest
# This file maps context categories to actual files in the knowledge/ directory.
# The PRD Orchestrator and Skills read this file to discover available context.
#
# To use this system:
# 1. Add your context files to the appropriate knowledge/ subdirectories
# 2. Update the paths below to point to your files
# 3. Leave entries blank or comment out if you don't have that context yet
---

## Company Context
- **mission**: `knowledge/company/mission.md` - Company mission, vision, values
- **strategy**: `knowledge/company/strategy.md` - Market positioning, strategic goals
- **brand**: `knowledge/company/brand.md` - Brand voice, terminology, guidelines

## Product Context
- **overview**: `knowledge/product/overview.md` - Product description, key features
- **competitive**: `knowledge/product/competitive.md` - Competitor analysis, differentiation
- **tech-stack**: `knowledge/product/tech-stack.md` - Technical constraints, architecture

## Regulatory Context
- **classification**: `knowledge/regulatory/classification.md` - Product regulatory classification
- **prohibited-terms**: `knowledge/regulatory/prohibited-terms.md` - Terms to avoid in documentation
- **indications**: `knowledge/regulatory/indications.md` - Intended use, contraindications

## User Research
- **personas**: `knowledge/user-research/personas.md` - Target user profiles and behaviors
- **pain-points**: `knowledge/user-research/pain-points.md` - User problems and frustrations
- **insights**: `knowledge/user-research/insights.md` - Research findings and key insights

## Validation Data
- **performance**: `knowledge/validation/current-performance.md` - Current performance metrics
- **validation-plan**: `knowledge/validation/validation-plan.md` - Clinical study design, timeline
- **clinical-evidence**: `knowledge/validation/clinical-evidence.md` - Supporting research and literature

## Custom Context
# Add your own context categories here as needed
# - **custom-name**: `knowledge/custom/file.md` - Description of what this contains

---

## Usage Notes

**For PRD Orchestrator:**
- Read this manifest first to discover available context
- Use `{{VARIABLE_NAME}}` syntax to reference context in skills
- Gracefully degrade if context files don't exist

**For New Users:**
- Run `./setup.sh` to create example context files
- Fill in your company/product-specific information
- Leave sections blank if not applicable to your product

**Variable Naming Convention:**
- Use UPPER_SNAKE_CASE for context variables
- Example: `{{COMPANY_MISSION}}`, `{{USER_PERSONAS}}`
```

**Step 2: Verify manifest is readable**

Run: `cat knowledge/CONTEXT_MANIFEST.md | head -20`

Expected: Should display the manifest header and first few sections

**Step 3: Commit Context Manifest**

```bash
git add knowledge/CONTEXT_MANIFEST.md
git commit -m "feat: add Context Manifest template for scalable context system

Creates manifest that maps context categories to files, enabling:
- Context-agnostic skill design
- Graceful degradation when context missing
- Self-documenting context structure
- Easy onboarding for new teams

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 3: Create Templates Directory and Example Files

**Files:**
- Create: `templates/examples/mission-example.md`
- Create: `templates/examples/personas-example.md`
- Create: `templates/examples/prohibited-terms-example.md`
- Create: `templates/CONTEXT_MANIFEST.template.md`

**Step 1: Create templates directory**

```bash
mkdir -p templates/examples
```

**Step 2: Create mission example**

Create file `templates/examples/mission-example.md`:

```markdown
# Company Mission

**Mission Statement:**
[Your company's core mission - the fundamental reason you exist]

Example: "Democratize preventive healthcare by making advanced health monitoring accessible, affordable, and anxiety-free for everyone."

**Vision:**
[Your long-term vision - the world you want to create]

Example: "A world where people have intuitive, continuous insight into their health without the burden of medical devices or clinical visits."

**Values:**
[3-5 core values that guide your decisions]

Example:
- User-first design
- Clinical rigor
- Regulatory responsibility
- Inclusive innovation
```

**Step 3: Create personas example**

Create file `templates/examples/personas-example.md`:

```markdown
# Target User Personas

## [Persona Name] (Primary/Secondary)

- **Age:** [Age range]
- **Behavior:** [Key behavioral characteristics]
- **Goal:** [What they're trying to achieve]
- **Pain Point:** [Their biggest frustration]
- **Motivation:** [What drives them]

**Example:**

## Proactive Adopter (Primary)

- **Age:** 30-50
- **Behavior:** Health-conscious, tech-forward, anxiety-prone
- **Goal:** Prevention without medicalization
- **Pain Point:** Hates traditional medical experiences (white coat syndrome)
- **Motivation:** Peace of mind, control over health

---

## [Second Persona Name] (Secondary)

- **Age:** [Age range]
- **Behavior:** [Key behavioral characteristics]
- **Goal:** [What they're trying to achieve]
- **Pain Point:** [Their biggest frustration]
- **Motivation:** [What drives them]
```

**Step 4: Create prohibited terms example**

Create file `templates/examples/prohibited-terms-example.md`:

```markdown
# Prohibited Terms (Regulatory Compliance)

**Context:** [Explain why certain terms are prohibited - e.g., FDA classification, regulatory constraints]

## Forbidden Terms

Terms that must NEVER appear in product documentation:

| Prohibited Term | Why Forbidden | Approved Alternative |
|:----------------|:--------------|:---------------------|
| Monitor | Implies medical device | Track, Observe, Check |
| Diagnose | Implies medical diagnosis | Provide insights, Estimate |
| Detect | Implies medical detection | Identify patterns, Notice |
| Medical Grade | Implies clinical use | High quality, Precise |
| Condition | Implies medical condition | Pattern, Range |
| Hypertension | Specific medical diagnosis | High blood pressure, Elevated readings |
| Treatment | Implies medical intervention | Lifestyle coaching, Guidance |

## Approved Terminology

Preferred terms for our product category:

| Approved Term | Usage Context | Example |
|:--------------|:--------------|:--------|
| General Wellness | Product classification | "A general wellness tool intended to..." |
| Educational | Purpose statement | "For informational and educational purposes only" |
| Out of Range | Status indicator | "Values outside typical wellness range" |
| Peace of Mind | User benefit | "Provides peace of mind about health trends" |
| Health Patterns | Data description | "Helps you understand health patterns" |
```

**Step 5: Copy manifest as template**

```bash
cp knowledge/CONTEXT_MANIFEST.md templates/CONTEXT_MANIFEST.template.md
```

**Step 6: Verify templates created**

Run: `tree templates`

Expected output:
```
templates
├── CONTEXT_MANIFEST.template.md
└── examples
    ├── mission-example.md
    ├── personas-example.md
    └── prohibited-terms-example.md
```

**Step 7: Commit templates**

```bash
git add templates/
git commit -m "feat: add context template files for new users

Creates example templates for:
- Company mission and values
- User personas
- Regulatory prohibited terms
- Context manifest

New users can copy these templates to bootstrap their knowledge base.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 4: Create Setup Script

**Files:**
- Create: `setup.sh`
- Modify: `README.md` (will create in Phase 7)

**Step 1: Write setup script**

Create file `setup.sh`:

```bash
#!/bin/bash
# PRD Generator Setup Script
# Initializes the knowledge folder structure and templates for a new project

set -e  # Exit on error

echo "🚀 Setting up PRD Generator for your project..."
echo ""

# Check if knowledge folder exists
if [ ! -d "knowledge" ]; then
    echo "✅ Creating knowledge/ folder structure..."
    mkdir -p knowledge/{company,product,regulatory,user-research,validation,custom}
else
    echo "ℹ️  knowledge/ folder already exists"
fi

# Check if manifest exists
if [ ! -f "knowledge/CONTEXT_MANIFEST.md" ]; then
    echo "✅ Creating Context Manifest from template..."
    cp templates/CONTEXT_MANIFEST.template.md knowledge/CONTEXT_MANIFEST.md
else
    echo "ℹ️  Context Manifest already exists"
fi

# Ask if user wants example files
echo ""
read -p "📝 Copy example context files to knowledge/? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "✅ Copying example files..."
    cp templates/examples/mission-example.md knowledge/company/mission.md
    cp templates/examples/personas-example.md knowledge/user-research/personas.md
    cp templates/examples/prohibited-terms-example.md knowledge/regulatory/prohibited-terms.md
    echo "   📄 mission.md → knowledge/company/"
    echo "   📄 personas.md → knowledge/user-research/"
    echo "   📄 prohibited-terms.md → knowledge/regulatory/"
else
    echo "⏭️  Skipping example files"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Next steps:"
echo "1. Edit knowledge/CONTEXT_MANIFEST.md to map your context files"
echo "2. Add your company/product context to knowledge/ folders"
echo "3. Invoke the PRD orchestrator: Use skill or direct invocation"
echo ""
echo "💡 Tips:"
echo "- Not all context is required - the system gracefully degrades"
echo "- Start with mission.md and personas.md for best results"
echo "- See templates/examples/ for guidance on each context type"
echo ""
```

**Step 2: Make script executable**

Run: `chmod +x setup.sh`

Expected: Script is now executable

**Step 3: Test setup script (dry run)**

Run: `bash -n setup.sh`

Expected: No syntax errors

**Step 4: Commit setup script**

```bash
git add setup.sh
git commit -m "feat: add setup.sh script for new user onboarding

Creates interactive setup script that:
- Initializes knowledge/ folder structure
- Copies Context Manifest template
- Optionally copies example context files
- Provides clear next steps for users

Makes system immediately usable by new teams.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 2: New Skills

### Task 5: Create Strategy Ladder Skill

**Files:**
- Create: `skills/strategy-ladder-skill.md`

**Step 1: Write strategy-ladder-skill**

Create file `skills/strategy-ladder-skill.md`:

```markdown
---
name: strategy-ladder
description: Connect feature to company mission, market positioning, and strategic differentiation. Use this skill to establish why a feature matters strategically before diving into details.
triggers: strategy, strategic positioning, mission alignment, market positioning
---

# Strategy Ladder Skill

## Purpose

Establish the strategic context for a product or feature by connecting it to company mission, market positioning, and competitive differentiation. This section answers: "Why does this matter to our mission and the market?"

## Input Context Requirements

**Required Context (from CONTEXT_MANIFEST.md):**
- `{{COMPANY_MISSION}}` - Used to align feature with company's core mission
- `{{COMPANY_STRATEGY}}` - Used to position feature in market context

**Optional Context:**
- `{{COMPETITIVE_LANDSCAPE}}` - Used for differentiation analysis
- `{{BRAND_GUIDELINES}}` - Used for tone and terminology consistency

**Fallback Behavior:**
- If mission context missing → Ask user: "What is your company's core mission?"
- If strategy context missing → Use generic positioning language
- If competitive context missing → Focus only on internal strategic value

## Narrative Handoff

**Input from Previous Section:** (None - this is typically section 2, after Intended Use)

**Output to Next Section:**
"Given this strategic positioning [summarize key positioning], what specific health outcomes and user impacts will this feature drive?"

## Process

### Step 1: Load Context

Read the Context Manifest to locate mission and strategy files. If files exist, load and parse them. If missing, use fallback prompts.

### Step 2: Generate Strategic Positioning

Output the following structure:

```markdown
## Strategic Positioning

### Mission Alignment
[Explain how this feature advances the company's core mission. Reference specific mission statements from context. Be concrete about the advancement, not generic.]

**Example:**
Our mission is to "democratize preventive healthcare." This feature advances that mission by removing the two largest barriers to blood pressure monitoring: cost (no separate device needed) and friction (no cuffs, no calibration). By making monitoring passive and continuous, we expand the addressable market from the diagnosed to the prevention-focused.

### Market Positioning
[Define where this positions the company in the competitive landscape. Answer: Are we creating a new category, entering an existing one, or redefining one?]

**Category Definition:** [What category does this create/enter/redefine?]

**Unique Positioning:** [What can we claim that competitors cannot? Be specific.]

**Strategic Moat:** [What makes this positioning defensible? Technology? Data? Network effects?]

**Example:**
We are creating a new category: "Passive Cardiovascular Intelligence." Unlike cuff-based monitors (Omron, Withings) that require active measurement, or calibration-dependent wearables (Samsung), we are the only solution that is both passive AND calibration-free. Our moat is the Waveform Foundation Model trained on 24-hour ABPM data - a data set competitors don't have access to.

### Strategic Differentiation
[Explain what makes this approach fundamentally different and better than alternatives]

**Technology Differentiation:** [What's novel about the tech approach?]

**Experience Differentiation:** [How is the user experience categorically different?]

**Business Model Differentiation:** [Any novel business model aspects?]

### Success at Scale
[Paint the picture of what success looks like strategically]

**Market Impact:** [TAM/SAM/SOM if applicable, or market penetration goals]

**Ecosystem Effects:** [Does this create platform value? Enable other products?]

**Strategic Optionality:** [What does this unlock next that wasn't possible before?]

**Example:**
If successful, this feature transforms Pixel Watch from a fitness tracker into a health guardian, unlocking a $50B preventive health market. The continuous cardiovascular data becomes a platform for additional models (AFib, sleep apnea), and the "passive protection" paradigm extends to other conditions. Success here proves we can do preventive medicine at consumer scale.
```

### Step 3: Validate Output

**Quality Checks:**
- ✅ References specific mission statements (not generic "we care about health")
- ✅ Names specific competitors and explains differentiation
- ✅ Includes concrete metrics or market sizing where possible
- ✅ Explains "what becomes possible next"
- ✅ Length: 150-200 words (concise but meaty)
- ✅ Tone: Visionary but grounded ("democratize", "unlock", "transform")

### Step 4: Output Handoff

**Closing Sentence Template:**
"To realize this strategic vision at scale, we must deliver measurable changes in users' health and behavior. [Next skill: health-impact]"

**Pass Forward to Next Skill:**
- Core strategic positioning statement
- Key differentiation claim
- Success metrics mentioned

## Examples

### Example 1: Blood Pressure Monitoring

**Input Context:**
- Mission: "Democratize preventive healthcare"
- Market: Wearables + Blood pressure monitoring

**Output:**

## Strategic Positioning

### Mission Alignment
Our mission is to "democratize preventive healthcare by making advanced health monitoring accessible, affordable, and anxiety-free." This feature advances that mission by eliminating the two largest barriers to blood pressure monitoring: economic (no $100+ cuff required) and psychological (no white coat anxiety). We shift from episodic checking to continuous protection.

### Market Positioning
**Category Definition:** We are creating "Passive Cardiovascular Intelligence" - a new category between fitness trackers and medical devices.

**Unique Positioning:** The only wearable solution that is both passive (no user action) and calibration-free (no setup). Apple requires monthly home BP checks. Samsung requires cuff calibration. We require nothing.

**Strategic Moat:** Our Waveform Foundation Model trained on 24-hour ABPM ground truth - a dataset competitors cannot easily replicate.

### Strategic Differentiation
**Technology:** Foundation model approach vs traditional signal processing
**Experience:** "Invisible Guardian" that protects without medicalization
**Business Model:** Integrated into existing hardware (Pixel Watch), not standalone device

### Success at Scale
Success means 10M+ users with passive cardiovascular monitoring within 2 years, creating a platform for additional cardiovascular models (AFib, HRV trends) and establishing Google as the leader in preventive health at consumer scale.

---

**Closing:** To realize this strategic vision at scale, we must deliver measurable changes in users' health and behavior.
```

## Guidelines for Success

1. **Be Specific, Not Generic:**
   - Bad: "This aligns with our mission to help users"
   - Good: "This advances our mission to 'democratize preventive care' by removing the $100 cost barrier"

2. **Name Competitors:**
   - Bad: "Better than existing solutions"
   - Good: "Unlike Omron's cuff or Samsung's calibration-dependent wearable..."

3. **Connect to Business Outcomes:**
   - Include TAM/SAM, market penetration goals, or ecosystem value

4. **Paint the "If This Works" Picture:**
   - What becomes possible that wasn't before?
   - What's the next product this enables?

5. **Use Visionary Language (But Stay Grounded):**
   - ✅ "democratize", "unlock", "transform", "reimagine"
   - ❌ "synergize", "leverage", "utilize" (corporate speak)

6. **YAGNI:**
   - Keep to 150-200 words total
   - Don't elaborate on strategy not relevant to this feature
```

**Step 2: Verify skill file is readable**

Run: `head -50 skills/strategy-ladder-skill.md`

Expected: Should show skill metadata and purpose

**Step 3: Commit strategy-ladder skill**

```bash
git add skills/strategy-ladder-skill.md
git commit -m "feat: add strategy-ladder-skill for strategic positioning

Creates new skill that establishes strategic context for PRDs by:
- Connecting feature to company mission
- Defining market positioning and category
- Articulating strategic differentiation
- Painting success-at-scale vision

Includes context-aware fallbacks and narrative handoff protocol.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 6: Create Health Impact Skill

**Files:**
- Create: `skills/health-impact-skill.md`

**Step 1: Write health-impact-skill**

Create file `skills/health-impact-skill.md`:

```markdown
---
name: health-impact
description: Define measurable health outcomes and behavior change goals that a health/wellness feature will drive. Use this skill to articulate what actually changes in users' lives and bodies.
triggers: health outcomes, health impact, behavior change, clinical outcomes, user health
---

# Health Impact Skill

## Purpose

Articulate the specific, measurable changes in users' health, behaviors, and lives that this feature will drive. This section answers: "What changes in users' bodies, behaviors, and lived experience?"

## Input Context Requirements

**Required Context (from CONTEXT_MANIFEST.md):**
- `{{STRATEGIC_POSITIONING}}` - From strategy-ladder-skill (what we're trying to achieve strategically)
- `{{USER_PERSONAS}}` - Target user profiles and behaviors
- `{{USER_PAIN_POINTS}}` - What users struggle with today

**Optional Context:**
- `{{CLINICAL_EVIDENCE}}` - Research supporting expected outcomes
- `{{VALIDATION_PLAN}}` - How we'll measure these outcomes

**Fallback Behavior:**
- If personas missing → Ask user: "Who is the target user and what are they trying to achieve?"
- If pain points missing → Ask user: "What problem does this solve?"
- If evidence missing → Note that claims are hypothetical/to-be-validated

## Narrative Handoff

**Input from Previous Section:** (Strategy Ladder)
"Given this strategic positioning [summary], what specific health outcomes will users experience?"

**Output to Next Section:** (Press Release)
"These health outcomes come to life through the following user experience: [tee up press release]"

## Process

### Step 1: Load Context

Read strategic positioning from previous section and user research from context manifest.

### Step 2: Generate Health Impact

Output the following structure:

```markdown
## Health Impact & Outcomes

### Target Health Outcomes

**Primary Outcome:**
- **Health Metric:** [Specific measurable health change]
- **Expected Change:** [Magnitude and direction of change]
- **Measurement Method:** [How we'll measure this]
- **Timeline:** [When we expect to see this impact]

**Secondary Outcomes:**
- **[Outcome 2]:** [Expected change and measurement]
- **[Outcome 3]:** [Expected change and measurement]

**Example:**
**Primary Outcome:**
- **Health Metric:** Blood pressure awareness and lifestyle modification
- **Expected Change:** 30% of "out of range" users adopt at least one lifestyle intervention (sleep, stress, activity) within 60 days of notification
- **Measurement Method:** In-app surveys + behavior tracking (sleep duration, activity logs)
- **Timeline:** 60-90 days post-notification

**Secondary Outcomes:**
- **Reduced Anxiety:** 40% decrease in self-reported health anxiety scores (validated scale) among users
- **Healthcare Engagement:** 15% of persistently elevated users consult healthcare provider within 30 days (with our data as conversation starter)

### Behavior Change Goals

[Specific behaviors we aim to shift]

| Current Behavior | Target Behavior | Intervention Mechanism | Expected Adoption Rate |
|:-----------------|:----------------|:-----------------------|:-----------------------|
| [Baseline behavior] | [Desired behavior] | [How feature drives change] | [% or metric] |

**Example:**
| Current Behavior | Target Behavior | Intervention Mechanism | Expected Adoption Rate |
|:-----------------|:----------------|:-----------------------|:-----------------------|
| Reactive: Only check BP when feeling unwell | Proactive: Weekly glance at wellness range | Weekly summary notifications + calm visualization | 60% check weekly summary |
| Avoidance: Don't think about BP due to cuff anxiety | Engagement: Comfortable monitoring trends | Passive data collection, no cuffs | 80% enable feature and keep enabled |
| Isolated data: BP numbers without context | Informed action: Connect BP to sleep/stress | LLM-generated contextual insights | 40% explore lifestyle correlations |

### Downstream Health Effects

[Longer-term population health implications]

**If We Achieve Target Behavior Change:**
- [Specific outcome 1 with projected numbers]
- [Specific outcome 2 with projected numbers]

**Connection to Public Health Goals:**
- [How this ladders up to societal health priorities]

**Equity Considerations:**
- [Who benefits most? Who might be excluded? How do we address gaps?]

**Example:**
If we achieve 30% lifestyle modification adoption among the 5M users with out-of-range notifications, we project:
- ~150K users improve sleep habits (7+ hours/night)
- ~100K users reduce sedentary time (10K+ steps/day)
- ~50K users engage with stress management tools

**Connection to Public Health:**
Early identification and lifestyle intervention for pre-hypertension can delay or prevent progression to Stage 1 hypertension, reducing cardiovascular disease risk. If scaled to 50M users globally, could contribute to AHA's 2030 goal of 20% reduction in CVD mortality.

**Equity Considerations:**
Algorithm validated across Fitzpatrick skin tones I-VI to ensure equitable performance. Free feature (no subscription) removes economic barrier. However, requires owning a Pixel Watch ($300+), limiting access to higher-income users. Mitigation: Partner with healthcare systems to subsidize devices for high-risk populations.

### Clinical Evidence Base

[Research that supports these expectations]

**Relevant Studies:**
- [Study 1]: [Finding and relevance]
- [Study 2]: [Finding and relevance]

**Effect Sizes from Literature:**
- [Intervention type]: [Effect size] on [outcome]

**Confidence Level:**
[High/Medium/Low confidence in projections and why]

**Example:**
**Relevant Studies:**
- Chandrasekhar et al. (2023): Sleep improvement (30min increase) associated with 2-3mmHg SBP reduction in pre-hypertensive adults
- Lim et al. (2024): Home BP monitoring + lifestyle coaching led to 25% adoption of at least 1 intervention within 90 days

**Effect Sizes:**
- Sleep interventions: -2.5mmHg SBP per 1hr increase (meta-analysis)
- Physical activity: -3.5mmHg SBP for 150min/week moderate activity

**Confidence Level:**
Medium-High. Our intervention mechanism (passive monitoring + contextual nudging) is novel, so direct evidence is limited. However, components (home monitoring, lifestyle interventions) have strong evidence base.
```

### Step 3: Validate Output

**Quality Checks:**
- ✅ Primary outcome is specific and measurable (not "better health")
- ✅ Behavior change table has concrete percentages or metrics
- ✅ Downstream effects tied to public health goals or population scale
- ✅ Equity considerations explicitly addressed
- ✅ Clinical evidence cited with sources (or noted as to-be-validated)
- ✅ Length: 200-250 words
- ✅ Tone: Aspirational but evidence-based (not hype)

### Step 4: Output Handoff

**Closing Sentence Template:**
"These health outcomes come to life through the following user experience: [brief 1-sentence tease of the vision, setting up press release]"

**Pass Forward to Next Skill:**
- Primary health outcome (for press release to highlight)
- Key behavior change (for CUJs to enable)
- User emotion/benefit (e.g., "peace of mind", "empowerment")

## Guidelines for Success

1. **Be Measurable:**
   - Bad: "Users will be healthier"
   - Good: "30% adopt lifestyle intervention within 60 days"

2. **Balance Aspiration with Realism:**
   - Include confidence levels
   - Cite evidence or note when projections are hypothetical
   - Don't overpromise

3. **Connect Individual to Population:**
   - Start with individual outcomes
   - Scale up to population health impact
   - Show public health relevance

4. **Address Equity Explicitly:**
   - Who benefits?
   - Who might be left out?
   - How do we close gaps?

5. **Use Behavior Change Framework:**
   - Current state → Target state → Mechanism → Metric

6. **Link to Strategy:**
   - Reference strategic positioning from previous section
   - Show how health outcomes achieve strategic goals
```

**Step 2: Verify skill is readable**

Run: `wc -l skills/health-impact-skill.md`

Expected: File should be ~200-250 lines

**Step 3: Commit health-impact skill**

```bash
git add skills/health-impact-skill.md
git commit -m "feat: add health-impact-skill for health outcomes

Creates new skill that defines measurable health impact by:
- Articulating primary/secondary health outcomes
- Mapping behavior change goals with metrics
- Projecting downstream population health effects
- Addressing equity considerations
- Citing clinical evidence base

Includes context-aware design and narrative handoffs.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 7: Create Validation Rigor Skill

**Files:**
- Create: `skills/validation-rigor-skill.md`

**Step 1: Write validation-rigor-skill** (Due to length, showing condensed version)

Create file `skills/validation-rigor-skill.md`:

```markdown
---
name: validation-rigor
description: Demonstrate clinical/scientific rigor through performance targets, current validation data, validation plans, and competitive analysis. Use this skill to counter "just general wellness" perceptions with evidence of rigorous validation.
triggers: validation, performance, competitive analysis, clinical rigor, evidence
---

# Validation Rigor Skill

## Purpose

Establish credibility through transparent reporting of performance targets, current validation data, validation plans, and competitive analysis. This section answers: "How do we know this actually works and beats alternatives?"

## Input Context Requirements

**Required Context (from CONTEXT_MANIFEST.md):**
- `{{CURRENT_PERFORMANCE}}` - Existing validation data and metrics
- `{{VALIDATION_PLAN}}` - Study design, timeline, endpoints
- `{{COMPETITIVE_LANDSCAPE}}` - Competitor products and performance

**Optional Context:**
- `{{CLINICAL_EVIDENCE}}` - Supporting research
- `{{REGULATORY_CLASSIFICATION}}` - Classification and path

**Fallback Behavior:**
- If performance data missing → State "Validation in progress, targets defined"
- If validation plan missing → Ask user for study design details
- If competitive data missing → Focus on internal validation only

## Narrative Handoff

**Input from Previous Section:** (Problem & Opportunity)
"Given these challenges with existing solutions, how do we know our approach works better?"

**Output to Next Section:** (Critical User Journeys)
"With this validation in progress/complete, users experience the following journeys:"

## Process

### Step 1: Load Context

Read validation data and competitive intelligence from context manifest.

### Step 2: Generate Validation & Competitive Rigor

**Section Structure:**

```markdown
## Validation & Competitive Rigor

### Target Performance
[Clinical or technical benchmarks we're measuring against]

We are targeting performance **comparable to [Gold Standard]** for [specific use case].

| Metric | Target Value | 95% CI | Clinical Rationale | Source |
|:-------|:-------------|:-------|:-------------------|:-------|
| [Metric 1] | [Value] | [CI] | [Why this matters clinically] | [Standard/Study] |
| [Metric 2] | [Value] | [CI] | [Why this matters] | [Source] |

**Ground Truth Definition:**
[What we're comparing against and why it's appropriate]

### Current Performance
[Where we are now with full transparency]

| Metric | Current (V1) | 95% CI | Status vs Target |
|:-------|:-------------|:-------|:-----------------|
| [Metric 1] | [Value] | [CI] | ✅ Within Margin / ⚠️ Approaching / ❌ Gap |
| [Metric 2] | [Value] | [CI] | [Status] |

**Interpretation:**
[Honest assessment: What's working? What gaps remain? What's the path to close them?]

### Validation Plan
[How we'll prove it works at scale]

**Study Design:**
- **Sample Size:** N=[number] ([rationale for power calculation])
- **Ground Truth:** [Method] ([why this is appropriate])
- **Study Sites:** [Number] sites across [regions]
- **Duration:** [Timeline]
- **Primary Endpoint:** [What we're measuring]
- **Secondary Endpoints:** [Additional measures]
- **Subgroup Analyses:** [Ensuring equity - age, BMI, skin tone, sex, etc.]
- **Statistical Power:** [Power calculation details]

**Timeline & Milestones:**
- [Date]: Study launch
- [Date]: Interim analysis
- [Date]: Primary completion
- [Date]: Regulatory submission (if applicable)

**Regulatory Strategy:**
[How validation aligns with regulatory classification]

### Competitive Analysis
[Head-to-head comparison across key dimensions]

| Competitor | Method | Calibration | Ground Truth | Performance | Regulatory | User Effort |
|:-----------|:-------|:------------|:-------------|:------------|:-----------|:------------|
| **[Our Product]** | **[Method]** | **[Cal]** | **[GT]** | **[Perf]** | **[Reg]** | **[Effort]** |
| [Competitor 1] | [Method] | [Cal] | [GT] | [Perf] | [Reg] | [Effort] |
| [Competitor 2] | [Method] | [Cal] | [GT] | [Perf] | [Reg] | [Effort] |

**Key Differentiators:**
1. [Specific advantage 1 with evidence]
2. [Specific advantage 2 with evidence]
3. [Specific advantage 3 with evidence]

**Competitive Risks:**
[What could competitors do to close the gap? How do we maintain advantage?]

**Example:**
1. **Only passive, calibration-free solution** - Apple requires periodic home BP checks, Samsung requires monthly cuff calibration, we require nothing
2. **Only 24h ABPM ground truth** - Competitors validate against home/office BP (waking hours only), we capture full circadian cycle including nocturnal dipping
3. **Foundation model approach** - Traditional signal processing hits accuracy ceiling, our model improves with more data

**Competitive Risks:**
- Apple could add calibration-free mode if they invest in ABPM validation dataset
- Samsung could reduce calibration frequency from monthly to quarterly
- Mitigation: Speed of data accumulation and model improvements; regulatory path diversification
```

### Step 3: Validate Output

**Quality Checks:**
- ✅ Performance targets include confidence intervals
- ✅ Current performance reported transparently (including gaps)
- ✅ Validation plan includes sample size rationale and subgroup analyses
- ✅ Competitive table compares across 5+ dimensions
- ✅ Competitive risks honestly assessed
- ✅ Length: 300-400 words + tables
- ✅ Tone: Confident but transparent about limitations

## Guidelines for Success

1. **Be Transparent:**
   - Show gaps, not just wins
   - Include confidence intervals
   - Note limitations

2. **Compare Apples to Apples:**
   - Same ground truth, same metrics across competitors
   - Note when comparisons aren't direct

3. **Justify Sample Sizes:**
   - Don't just say "N=1600"
   - Explain power calculation or precedent

4. **Address Equity in Validation:**
   - Subgroup analyses across demographics
   - Show algorithm works for all users

5. **Explain the "Why":**
   - Why this ground truth?
   - Why this target performance?
   - Why this matters clinically?
```

**Step 2: Verify skill file**

Run: `grep -c "^#" skills/validation-rigor-skill.md`

Expected: Should show multiple section headers

**Step 3: Commit validation-rigor skill**

```bash
git add skills/validation-rigor-skill.md
git commit -m "feat: add validation-rigor-skill for credibility

Creates skill that establishes clinical/scientific credibility through:
- Target performance benchmarks with rationale
- Transparent current performance reporting
- Detailed validation plan with power calculations
- Head-to-head competitive analysis
- Honest assessment of competitive risks

Counters 'just general wellness' perception with rigorous validation evidence.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 3: Skill Enhancements

### Task 8: Enhance Product Narrative Skill

**Files:**
- Modify: `skills/product-narrative-skill.md`

**Step 1: Read current product-narrative-skill**

Run: `head -100 skills/product-narrative-skill.md`

Expected: See current skill structure

**Step 2: Add context integration section**

Add after line 10 (after Purpose):

```markdown
## Input Context Requirements (NEW)

**From Previous Sections:**
- `{{STRATEGIC_POSITIONING}}` - From strategy-ladder-skill (why this matters strategically)
- `{{HEALTH_OUTCOMES}}` - From health-impact-skill (what changes for users)
- `{{USER_PERSONAS}}` - From context manifest (who we're building for)
- `{{USER_PAIN_POINTS}}` - From context manifest (what problem we're solving)

**From Context Manifest:**
- `{{PROHIBITED_TERMS}}` - Regulatory terms to avoid
- `{{BRAND_GUIDELINES}}` - Tone and terminology preferences

**Handoff from Previous Section:**
"These health outcomes come to life through the following user experience:"

## Narrative Integration Requirements (NEW)

### Opening Connection
Your press release MUST reference the strategic positioning established in the Strategy Ladder section.

**Example:**
- Strategy said: "Democratize preventive care"
- Press Release opens with: "Google today democratizes preventive care with..."

### 7-Star Experience Selection
When choosing your 7-Star moment, ensure it connects directly to the **primary health outcome** from the Health Impact section.

**Example:**
- Health Outcome: "Reduce anxiety around BP monitoring"
- 7-Star Moment: "The Invisible Guardian - no cuffs, no calibration, no anxiety, just peace of mind"

### Problem Statement Alignment
The "Problem" section of the press release must reflect the **user pain points** from context.

**Example:**
- Pain Point from Context: "White coat syndrome, cuff anxiety"
- Press Release Problem: "For decades, tracking blood pressure meant stopping your life, putting on a tight, uncomfortable cuff, and waiting in anxious silence for a judgment."

### Prohibited Terms Check
Before outputting, validate against `{{PROHIBITED_TERMS}}` list:
- Auto-replace: "Monitor" → "Track" or "Observe"
- Auto-replace: "Diagnose" → "Provide insights" or "Estimate"
- Auto-replace: "Detect" → "Identify patterns" or "Notice"
- Flag for review if uncertain

## Output Handoff (NEW)

### Closing Sentence Template
"This vision addresses a critical problem in the current landscape: [1-sentence problem tee-up for next section]"

### Pass Forward to Next Section
- **Core Metaphor:** (e.g., "Guardian", "Compass", "Invisible Protection")
- **Target Emotion:** (e.g., "Peace of mind", "Empowerment", "Control")
- **Key Differentiator:** (e.g., "Calibration-free", "Passive", "No cuffs")
- **User Benefit:** (e.g., "Freedom from medical anxiety")
```

**Step 3: Verify changes**

Run: `grep -A 5 "Input Context Requirements" skills/product-narrative-skill.md`

Expected: Should show the new section

**Step 4: Commit enhanced narrative skill**

```bash
git add skills/product-narrative-skill.md
git commit -m "feat: enhance product-narrative-skill with context integration

Adds narrative handoff protocol:
- Receives context from strategy and health impact skills
- References strategic positioning in opening
- Connects 7-Star experience to health outcomes
- Validates against prohibited regulatory terms
- Passes forward core metaphor and differentiators

Ensures press release builds on previous sections coherently.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 9: Enhance CUJ Generator Skill

**Files:**
- Modify: `skills/cuj-generator-skill.md`

**Step 1: Add context and handoff sections to CUJ skill**

Add after Purpose section in `skills/cuj-generator-skill.md`:

```markdown
## Input Context Requirements (NEW)

**From Previous Sections:**
- `{{PRESS_RELEASE_METAPHOR}}` - Core metaphor to maintain consistency (e.g., "Guardian")
- `{{HEALTH_OUTCOMES}}` - Specific behaviors we're trying to change
- `{{PROBLEM_STATEMENT}}` - Pain points the CUJ must address
- `{{USER_PERSONAS}}` - Target user characteristics and goals

**Handoff from Previous Section:**
"To deliver this experience, users must be able to [high-level goal]."

## Narrative Integration Requirements (NEW)

### CUJ Naming Convention
Use language from the press release metaphor to name CUJs.

**Example:**
- Press Release Metaphor: "Invisible Guardian"
- CUJ Names:
  - "Enable the Invisible Guardian"
  - "Experience Passive Protection"
  - "Receive Contextual Guidance from Guardian"

### Task-to-Outcome Mapping
For each CUJ, explicitly map tasks to health outcomes from the Health Impact section.

Add this table after the journey map:

| Task | Health Outcome Enabled | Behavior Change Driven |
|:-----|:-----------------------|:-----------------------|
| [Task name] | [Which health outcome this task enables] | [What behavior change this supports] |

**Example:**
| Task | Health Outcome Enabled | Behavior Change Driven |
|:-----|:-----------------------|:-----------------------|
| Enable Guardian in Settings | Anxiety reduction | Shift from avoidance to comfortable monitoring |
| Review Weekly Summary | Lifestyle awareness | Shift from reactive (only check when sick) to proactive |
| Explore Lifestyle Correlations | Informed action | Connect health patterns to daily habits |

### Emotional Journey Column
Add a "User Emotion" column to your journey map showing how the user feels at each step. This ensures the CUJ delivers on the press release's emotional promise.

| Task | User Emotion | Notes |
|:-----|:-------------|:------|
| [Task] | [Emotion] | [Why this emotion matters] |

**Example:**
| Task | User Emotion | Notes |
|:-----|:-------------|:------|
| Enable Guardian | Curious, slightly uncertain | First interaction - needs to feel easy |
| See calibration status | Reassured | Wants confirmation it's working |
| Receive first weekly summary | Delighted, validated | Aha moment - "this is actually useful" |

## Output Handoff (NEW)

### Closing Sentence Template
"To enable these user journeys reliably, the system must implement the following functional requirements:"

### Pass Forward to Next Section
- **Critical User Interactions (CUIs):** [List of key interactions that need detailed specs]
- **Edge Cases Discovered:** [Scenarios that need handling in requirements]
- **Performance Expectations:** [Latency/reliability requirements surfaced by CUJ analysis]
- **Error States:** [Failure modes that need graceful handling]

**Example Pass Forward:**
- **CUIs:** "Enable Guardian Toggle", "View Weekly Summary Card", "Start Coaching Plan"
- **Edge Cases:** "User enables but never wears watch", "User changes height mid-calibration"
- **Performance:** "< 200ms dashboard load", "Weekly summary generated by 8am local time"
- **Error States:** "Insufficient data for summary", "Bluetooth disconnected during sync"
```

**Step 2: Verify enhancement**

Run: `grep "Task-to-Outcome Mapping" skills/cuj-generator-skill.md`

Expected: Should find the new section

**Step 3: Commit enhanced CUJ skill**

```bash
git add skills/cuj-generator-skill.md
git commit -m "feat: enhance cuj-generator-skill with narrative integration

Adds handoff protocol to CUJ generator:
- Uses press release metaphor in CUJ naming
- Maps tasks to health outcomes explicitly
- Includes emotional journey tracking
- Surfaces edge cases and performance requirements

Ensures CUJs connect to strategic narrative and health goals.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 10: Enhance Acceptance Criteria Skill

**Files:**
- Modify: `skills/acceptance-criteria-skill.md`

**Step 1: Add traceability and context sections**

Add after Purpose in `skills/acceptance-criteria-skill.md`:

```markdown
## Input Context Requirements (NEW)

**From Previous Sections:**
- `{{CUJ_CRITICAL_INTERACTIONS}}` - The CUIs that need detailed specifications
- `{{EDGE_CASES}}` - Scenarios discovered during CUJ mapping
- `{{HEALTH_OUTCOMES}}` - What the system must enable for users
- `{{PERFORMANCE_EXPECTATIONS}}` - Latency/reliability requirements from CUJs
- `{{REGULATORY_CONSTRAINTS}}` - Terms and behaviors to avoid

**Handoff from Previous Section:**
"To enable these user journeys reliably, the system must implement:"

## Requirements Traceability (NEW)

Every functional requirement MUST trace back to:
1. **A specific CUJ task** - Which user journey does this enable?
2. **A health outcome** - Which health goal does this support?
3. **A regulatory constraint** - Does this satisfy/avoid any regulatory requirement?

### Traceability Table

Add this table before your Gherkin scenarios:

| Req ID | CUJ Task | Health Outcome Enabled | Regulatory Note |
|:-------|:---------|:-----------------------|:----------------|
| FR-01 | [Task from CUJ] | [Outcome from Health Impact] | [Constraint if applicable] |
| FR-02 | [Task] | [Outcome] | [Constraint] |

**Example:**
| Req ID | CUJ Task | Health Outcome Enabled | Regulatory Note |
|:-------|:---------|:-----------------------|:----------------|
| FR-01 | "Enable Guardian in Settings" | Anxiety reduction (passive setup) | Must show disclaimer before enabling |
| FR-02 | "View Weekly Summary" | Lifestyle awareness | No absolute BP values, only "ranges" |
| FR-03 | "Receive Persistent Notification" | Healthcare engagement | Must include disclaimer, not alarm language |

## Language Consistency (NEW)

Use the **same terminology** from press release and CUJs.

**Example:**
- If CUJ says "Wellness Range" → Don't say "BP Range" in requirements
- If Press Release says "Guardian" → Use in error messages: "Guardian needs more data"
- If prohibited terms list says avoid "Monitor" → Use "Track" or "Check" instead

## Gherkin Scenarios with Context (NEW)

Enhance your Given/When/Then scenarios with emotional and health context:

```gherkin
Scenario: [ID] - [Name] ([Emotional Context])
  Given [User state and emotional context]
  And [System state]
  And [Connection to health outcome: Why this matters]
  When [User action or system trigger]
  Then [Primary system response]
  And [UI feedback with appropriate tone]
  And [Health outcome enabled or behavior nudged]
  And [What does NOT happen - negative case]
```

**Example:**
```gherkin
Scenario: FR-01 - First Time Setup (The "Effortless Onboarding")
  Given User is in OOBE flow (emotional state: curious but time-pressed)
  And User's goal is "enable protection without friction" (from CUJ)
  And This supports Health Outcome: "Anxiety reduction through passive setup"
  When User taps "Enable Guardian" toggle
  Then System begins background calibration (no progress bar to watch)
  And User sees message: "Guardian is learning your baseline. Just keep wearing your watch." (reassuring, not medical)
  And System does NOT ask for cuff calibration or height verification yet
  And Health Outcome: User feels protected without burden or setup friction
```

## Output Handoff (NEW)

### Closing Sentence Template
"Success for these requirements is measured by the following metrics:"

### Pass Forward to Next Section
- **Instrumentation Events:** [Analytics events needed for success metrics]
- **Performance SLAs:** [Service level agreements defined in requirements]
- **Error Analytics:** [Error states that need tracking in metrics section]

**Example Pass Forward:**
- **Instrumentation:** "guardian_enabled_event", "weekly_summary_viewed_event", "coaching_plan_started_event"
- **Performance SLAs:** "Weekly summary generated by 8am local time (99% SLA)", "Dashboard loads < 200ms (95th percentile)"
- **Error Analytics:** Track "insufficient_data_for_summary" rate, "bluetooth_disconnect_during_sync" rate
```

**Step 2: Verify enhancement**

Run: `grep "Requirements Traceability" skills/acceptance-criteria-skill.md`

Expected: Should find the new section

**Step 3: Commit enhanced acceptance criteria skill**

```bash
git add skills/acceptance-criteria-skill.md
git commit -m "feat: enhance acceptance-criteria-skill with traceability

Adds traceability and narrative integration:
- Every requirement traces to CUJ task and health outcome
- Language consistency with press release terminology
- Gherkin scenarios include emotional and health context
- Surfaces instrumentation needs for metrics section

Ensures requirements connect to user journeys and health goals.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 4: Orchestrator Updates

### Task 11: Add Context Discovery Protocol to Orchestrator

**Files:**
- Modify: `agents/prd_orchestrator_agent.md`

**Step 1: Read current orchestrator structure**

Run: `head -50 agents/prd_orchestrator_agent.md`

Expected: See current orchestrator metadata and role

**Step 2: Add Context Discovery Protocol**

Add after the "Strategic Context (MANDATORY)" section (around line 20):

```markdown
## Context Discovery Protocol (NEW)

**CRITICAL FIRST STEP:** Before generating any PRD section, you MUST discover and load context.

### Step 1: Read the Context Manifest

**File Location:** `knowledge/CONTEXT_MANIFEST.md`

This manifest tells you:
- What context files exist in the knowledge/ folder
- Where each file is located
- What type of information each file contains

If the manifest doesn't exist, gracefully degrade (see Step 4).

### Step 2: Load Required Context Files

Based on what the manifest indicates, load the relevant context files for this PRD:

**For All PRDs (if available):**
- `{{COMPANY_MISSION}}` → Load from path in manifest (company context)
- `{{USER_PERSONAS}}` → Load from path in manifest (user research)
- `{{PROHIBITED_TERMS}}` → Load from path in manifest (regulatory)

**For Validation-Heavy PRDs (if available):**
- `{{CURRENT_PERFORMANCE}}` → Load from path in manifest (validation data)
- `{{VALIDATION_PLAN}}` → Load from path in manifest (validation data)
- `{{COMPETITIVE_LANDSCAPE}}` → Load from path in manifest (product context)

### Step 3: Resolve Context Variables

When invoking skills, use context variables that you've loaded:

**Syntax:** `{{VARIABLE_NAME}}`

**Example Invocation:**
```
Invoke strategy-ladder-skill with:
- User request: [what user asked for]
- Company Mission: {{COMPANY_MISSION}}
- Company Strategy: {{COMPANY_STRATEGY}}
```

**Available Variables:**
- `{{COMPANY_MISSION}}` - Mission, vision, values
- `{{COMPANY_STRATEGY}}` - Market positioning, strategic goals
- `{{BRAND_GUIDELINES}}` - Brand voice, approved terminology
- `{{USER_PERSONAS}}` - Target user profiles
- `{{USER_PAIN_POINTS}}` - User problems and frustrations
- `{{PROHIBITED_TERMS}}` - Regulatory terms to avoid
- `{{CURRENT_PERFORMANCE}}` - Performance metrics and validation data
- `{{VALIDATION_PLAN}}` - Study design and timeline
- `{{COMPETITIVE_LANDSCAPE}}` - Competitor products and positioning

### Step 4: Graceful Degradation

If context files don't exist, **do not fail**. Instead:

1. **Note what's missing:** Keep track of which context was unavailable
2. **Ask user for critical info:** If mission or personas missing, ask user:
   - "What is your company's core mission?"
   - "Who is the target user for this feature?"
3. **Use generic language:** If brand guidelines missing, use standard professional tone
4. **Document in footnote:** At end of PRD, include:
   ```
   ---
   **Context Note:** This PRD was generated with partial context. Missing context:
   - Company mission statement
   - User persona profiles
   For richer, more tailored PRDs, add these files to knowledge/ folder.
   ```

### Example: Context Discovery in Action

```markdown
## Context Discovery Results

**Context Loaded:**
✅ Company Mission: knowledge/company/mission.md
✅ User Personas: knowledge/user-research/personas.md
✅ Prohibited Terms: knowledge/regulatory/prohibited-terms.md
⚠️  Company Strategy: File not found → Will ask user
❌ Validation Plan: Not applicable for this feature

**Proceeding with available context...**
```
```

**Step 3: Verify addition**

Run: `grep -A 10 "Context Discovery Protocol" agents/prd_orchestrator_agent.md`

Expected: Should show the new section

**Step 4: Commit context discovery addition**

```bash
git add agents/prd_orchestrator_agent.md
git commit -m "feat: add Context Discovery Protocol to orchestrator

Adds first step of narrative thread architecture:
- Reads CONTEXT_MANIFEST.md to discover available context
- Loads context files based on manifest paths
- Resolves {{VARIABLES}} when invoking skills
- Gracefully degrades when context missing
- Documents what context was used/missing

Enables context-agnostic, scalable PRD generation.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 12: Add Story Arc Framework to Orchestrator

**Files:**
- Modify: `agents/prd_orchestrator_agent.md`

**Step 1: Add Story Arc Framework section**

Add after Context Discovery Protocol:

```markdown
## Story Arc Framework (NEW)

The PRD is not a collection of disconnected sections. It is a **narrative journey** that builds progressively from inspiration to implementation.

### The Narrative Arc

Each section answers a natural question that flows from the previous insight:

```
0. EXECUTIVE SUMMARY → "What is this and why does it matter?"
1. INTENDED USE → "Who is this for and what can it claim?"
2. STRATEGY LADDER → "Why does this matter to our mission?"
3. HEALTH IMPACT → "What changes in users' lives?"
4. PRESS RELEASE → "What's the dream experience?"
5. PROBLEM & OPPORTUNITY → "Why is the status quo broken?"
6. VALIDATION RIGOR → "How do we know this works and beats alternatives?"
7. CRITICAL USER JOURNEYS → "How do users experience the magic?"
8. FUNCTIONAL REQUIREMENTS → "What exactly must we build?"
9. SUCCESS METRICS → "How do we know it worked?"
```

### Context Handoff Protocol

When invoking each skill, provide:

**1. Input Context:**
- Summary of previous section (2-3 sentences)
- Key terms/concepts to reference
- The narrative question this section must answer

**2. Output Requirements:**
- Opening sentence must reference previous section's insight
- Closing sentence must tee up next section's question
- Use consistent terminology from prior sections

### Emotional Progression

The document follows an emotional arc:

- **Sections 0-3:** INSPIRING (Purpose → Hope → Dream)
  - Tone: Visionary, aspirational, mission-driven
  - Audience: Executives, stakeholders

- **Section 4:** GROUNDING (The Real Problem)
  - Tone: Empathetic, urgent, honest
  - Audience: Product team, investors

- **Sections 5-6:** CONFIDENCE BUILDING (Validation + Competition)
  - Tone: Credible, rigorous, evidence-based
  - Audience: Medical affairs, skeptical engineers

- **Sections 7-9:** EXECUTION (How → What → Proof)
  - Tone: Precise, actionable, measurable
  - Audience: Engineering, QA, analytics

### Handoff Templates

Use these templates when transitioning between sections:

**Strategy Ladder → Health Impact:**
```
"Given this strategic positioning [1-sentence summary], what specific health outcomes and behavior changes will users experience?"
```

**Health Impact → Press Release:**
```
"These health outcomes come to life through the following user experience:"
```

**Press Release → Problem & Opportunity:**
```
"This vision addresses a critical problem: [brief problem statement]"
```

**Problem → Validation Rigor:**
```
"To solve this problem better than existing alternatives, we must demonstrate:"
```

**Validation → CUJs:**
```
"With this validation establishing credibility, users experience the following journeys:"
```

**CUJs → Requirements:**
```
"To enable these user journeys reliably, the system must implement the following requirements:"
```

**Requirements → Metrics:**
```
"Success for these requirements is measured by:"
```

### Section Sequencing

**Sequential Invocation Order:**

1. **Generate Executive Summary** (Orchestrator direct - synthesizes user request)
2. **Generate Intended Use** (Orchestrator direct - uses regulatory context)
3. **Invoke strategy-ladder-skill** with mission/strategy context
4. **Invoke health-impact-skill** with strategy output + personas
5. **Invoke product-narrative-skill** with strategy + health impact output
6. **Generate Problem & Opportunity** (Orchestrator direct - synthesizes narrative + competitive)
7. **Invoke validation-rigor-skill** with performance + competitive data
8. **Invoke cuj-generator-skill** with narrative metaphor + health outcomes
9. **Invoke acceptance-criteria-skill** with CUJ output + health outcomes
10. **Generate Success Metrics** (Orchestrator direct - synthesizes all outputs)

**CRITICAL:** Skills must execute **sequentially**, not in parallel, because each depends on context from previous sections.
```

**Step 2: Verify addition**

Run: `grep "Story Arc Framework" agents/prd_orchestrator_agent.md`

Expected: Should find the section

**Step 3: Commit Story Arc Framework**

```bash
git add agents/prd_orchestrator_agent.md
git commit -m "feat: add Story Arc Framework to orchestrator

Defines narrative journey structure for PRDs:
- 9-section arc with clear narrative questions
- Context handoff protocol between sections
- Emotional progression (inspiring → grounding → execution)
- Sequential skill invocation with templates
- Ensures sections build on each other coherently

Core innovation of narrative thread architecture.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 13: Update PRD Structure Section in Orchestrator

**Files:**
- Modify: `agents/prd_orchestrator_agent.md`

**Step 1: Update PRD Structure section**

Find the "PRD Structure & Requirements" section (around line 45) and update it to match the new story arc:

```markdown
## PRD Structure & Requirements (Updated)

Generate the PRD following the Story Arc Framework defined above. Use **Markdown** format.

### 0. Executive Summary

**Purpose:** Instant clarity - what is this and why does it matter?
**Length:** 3-4 sentences
**Audience:** Executives, skip-level reviews

**Template:**
```markdown
## Executive Summary

**[Product/Feature Name]** is a [regulatory classification] that [what it does in user terms]. We're building this to [strategic rationale from strategy-ladder] and expect to [health outcome + business metric].

**Owner:** [Team/Name]
**Status:** [Draft/Review/Approved]
**Last Updated:** [Date]
```

**Source:** Synthesize from user request + context

---

### 1. Intended Use & Indications

**Purpose:** Define who this is for, what it can claim, regulatory boundaries
**Length:** ~1 paragraph + bullets
**Audience:** Regulatory, legal, medical affairs

**Template:**
```markdown
## Intended Use & Indications

**Intended Use:** [Product Name] is a [classification] intended to [primary purpose] for [target population]. It provides [information type] for [use case].

**Indications for Use:**
- [Population segment 1]
- [Population segment 2]

**Contraindications:**
- [Who should NOT use]
- [Medical conditions that exclude use]

**Regulatory Classification:** [FDA category] under [guidance document]

**Mandatory Disclaimer:** [Standard FDA General Wellness language from context]
```

**Source:** Use regulatory context from `{{REGULATORY_CLASSIFICATION}}` and `{{INDICATIONS}}`

---

### 2. Strategic Positioning

**Purpose:** Connect to mission, market positioning, strategic differentiation
**Length:** 150-200 words
**Audience:** Executives, team motivation

**ACTION:** Invoke `strategy-ladder-skill` with:
- User request
- `{{COMPANY_MISSION}}`
- `{{COMPANY_STRATEGY}}`
- `{{COMPETITIVE_LANDSCAPE}}`

---

### 3. Health Impact & Outcomes

**Purpose:** Define measurable health changes and behavior goals
**Length:** 200-250 words
**Audience:** Stakeholders, medical affairs

**ACTION:** Invoke `health-impact-skill` with:
- Strategic positioning output from previous section
- `{{USER_PERSONAS}}`
- `{{USER_PAIN_POINTS}}`
- `{{CLINICAL_EVIDENCE}}` (if available)

---

### 4. The Press Release (Narrative)

**Purpose:** Paint the 7-Star vision that inspires
**Length:** ~1 page
**Audience:** Everyone - the north star

**ACTION:** Invoke `product-narrative-skill` with:
- Strategic positioning summary
- Primary health outcome from previous section
- `{{USER_PERSONAS}}`
- `{{PROHIBITED_TERMS}}`
- `{{BRAND_GUIDELINES}}`

**Constraint:** Must use "7-Star Experience" methodology. Must connect to strategic positioning and health outcomes.

---

### 5. Problem & Opportunity

**Purpose:** Visceral problem definition + differentiation
**Length:** 200-300 words
**Audience:** Product team, investors

**Template:**
```markdown
## Problem & Opportunity

### The [Problem Name] Gap

**Current State:** [Status quo and its failures]

**Insight:** [User research insight from personas/pain points]

**Differentiation:** [How we're different from competitors - reference validation rigor section]

[Include competitive comparison table if competitive context available]
```

**Source:** Synthesize from:
- `{{USER_PAIN_POINTS}}`
- `{{COMPETITIVE_LANDSCAPE}}`
- Press release metaphor

---

### 6. Validation & Competitive Rigor

**Purpose:** Demonstrate clinical/scientific credibility
**Length:** 300-400 words + tables
**Audience:** Medical affairs, regulatory, skeptical engineers

**ACTION:** Invoke `validation-rigor-skill` with:
- `{{CURRENT_PERFORMANCE}}`
- `{{VALIDATION_PLAN}}`
- `{{COMPETITIVE_LANDSCAPE}}`
- `{{REGULATORY_CLASSIFICATION}}`

**Must Include:**
- Target performance table
- Current performance table
- Validation plan with sample size rationale
- Competitive analysis table
- Honest assessment of gaps

---

### 7. Critical User Journeys

**Purpose:** Map how users experience the magic
**Length:** ~2 pages with tables
**Audience:** Design, product, UX research

**ACTION:** Invoke `cuj-generator-skill` with:
- Press release metaphor
- Health outcomes
- `{{USER_PERSONAS}}`
- Problem statement

**Must Include:**
- CUJ header (user, goal, context)
- Journey map with tasks
- Task-to-outcome mapping table
- Emotional journey column
- Health metrics

---

### 8. Functional Requirements

**Purpose:** Crystal-clear specs for implementation
**Length:** 2-3 pages with tables
**Audience:** Engineering, QA

**ACTION:** Invoke `acceptance-criteria-skill` with:
- CUJ outputs (critical interactions, edge cases)
- Health outcomes
- `{{REGULATORY_CONSTRAINTS}}`
- Performance expectations from CUJs

**Must Include:**
- Requirements traceability table
- Feature logic definitions (constants)
- Gherkin scenarios with context
- Non-functional requirements
- Error handling specs

---

### 9. Success Metrics

**Purpose:** Define how we measure success
**Length:** ~1 page with table
**Audience:** Leadership, analytics, ops

**Template:**
```markdown
## Success Metrics

### HEART Framework

| Metric Category | Metric | Target | Measurement Method |
|:----------------|:-------|:-------|:-------------------|
| **Happiness** | [User satisfaction] | [Target] | [Method] |
| **Engagement** | [Usage frequency] | [Target] | [Method] |
| **Adoption** | [Enablement rate] | [Target] | [Method] |
| **Retention** | [Continued use] | [Target] | [Method] |
| **Task Success** | [Completion rate] | [Target] | [Method] |

### Health Outcome Metrics

[Map back to health outcomes from Section 3]

| Health Outcome | Metric | Target | Timeline |
|:---------------|:-------|:-------|:---------|
| [Outcome] | [How measured] | [Target] | [When] |

### Business Metrics

[Revenue, cost savings, strategic value]

### Launch Gates

[What must be true before launch?]
```

**Source:** Synthesize from:
- Health outcomes (Section 3)
- CUJ metrics (Section 7)
- Requirements instrumentation (Section 8)
- Strategic success criteria (Section 2)

---
```

**Step 2: Verify updated structure**

Run: `grep -c "^### [0-9]\\." agents/prd_orchestrator_agent.md`

Expected: Should find 10 section markers (0-9)

**Step 3: Commit updated PRD structure**

```bash
git add agents/prd_orchestrator_agent.md
git commit -m "feat: update PRD structure to match Story Arc Framework

Updates orchestrator's PRD structure section:
- Adds Executive Summary and Intended Use up front
- Reorders sections to follow narrative arc
- Specifies which sections are orchestrator-direct vs skill-invoked
- Includes templates for orchestrator-direct sections
- Maps each section to its inputs and audience

Completes narrative thread architecture in orchestrator.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 5: Coherence Validation

### Task 14: Add Coherence Validation to Orchestrator

**Files:**
- Modify: `agents/prd_orchestrator_agent.md`

**Step 1: Add Coherence Validation Protocol**

Add after the PRD Structure section:

```markdown
## Coherence Validation Protocol (NEW)

After generating all PRD sections, run these automated coherence checks to ensure narrative consistency.

### Check 1: Terminology Consistency

**Goal:** Verify that core metaphors and terminology appear consistently across sections.

**Process:**
1. Extract core metaphor from Press Release (Section 4)
   - Example: "Guardian", "Compass", "Invisible Protection"
2. Scan all sections for references to this metaphor
3. Target: Core metaphor should appear in 80%+ of sections

**Expected Appearances:**
- Strategy Ladder: Reference to strategic vision
- Health Impact: Connection to user benefit
- Press Release: Central metaphor defined
- Problem: Problem framed in metaphor terms
- CUJs: Journey names use metaphor
- Requirements: Error messages use metaphor
- Metrics: Success defined in metaphor terms

**If Check Fails:**
- Highlight inconsistencies
- Offer batch replace (e.g., replace "feature" with "Guardian" in sections X, Y, Z)

---

### Check 2: Forbidden Terms Scanner

**Goal:** Ensure no prohibited regulatory terms appear anywhere in the PRD.

**Process:**
1. Load `{{PROHIBITED_TERMS}}` from context
2. Scan entire PRD text for any forbidden terms
3. For each violation found:
   - Flag the location
   - Suggest approved alternative from prohibited terms list

**Common Violations:**
- "Monitor" → Suggest "Track" or "Observe"
- "Diagnose" → Suggest "Provide insights" or "Estimate"
- "Detect" → Suggest "Identify patterns" or "Notice"
- "Medical grade" → Suggest "High quality" or "Precise"
- "Hypertension" → Suggest "High blood pressure" or "Elevated readings"

**Action:**
- Auto-replace violations with approved alternatives
- Flag for user review if context suggests manual review needed

---

### Check 3: Narrative Reference Validation

**Goal:** Verify that sections reference previous sections' insights.

**Expected Narrative Flow:**
1. Health Impact section references Strategy Ladder
   - Should mention strategic positioning or mission
2. Press Release references Health Outcomes
   - Should highlight primary health outcome in solution
3. Problem section references Press Release metaphor
   - Should use consistent language/framing
4. CUJs reference Problem pain points
   - Should address problems identified
5. Requirements reference CUJ tasks
   - Traceability table should be complete
6. Metrics reference Health Outcomes
   - Health outcome metrics should map back to Section 3

**Process:**
1. For each expected reference, scan for connecting language
2. If missing, flag the gap
3. Suggest insertion point for connecting sentence

**If Check Fails:**
- Insert connecting sentences using handoff templates
- Example: "Given the strategic importance of [x from Section 2], this feature will drive [y health outcome]..."

---

### Check 4: Metric Alignment

**Goal:** Verify that outcomes have corresponding measurements.

**Process:**
1. Extract all health outcomes from Health Impact section
2. Check that each appears in Success Metrics section
3. Extract all CUJ tasks from CUJ section
4. Check that CUIs are instrumented in Requirements section
5. Verify requirements have acceptance criteria

**Expected Mappings:**
- Health Outcome → Success Metric
- CUJ Task → Instrumentation Event
- Requirement ID → Acceptance Criteria

**If Check Fails:**
- Generate missing metrics for unmeasured outcomes
- Generate missing instrumentation for unmeasured tasks
- Flag incomplete requirements

---

### Check 5: Emotional Arc Progression

**Goal:** Verify tone shifts appropriately across sections.

**Process:**
1. Analyze tone of Sections 0-3 (should be inspiring, visionary)
2. Analyze tone of Section 4 (should be empathetic, urgent)
3. Analyze tone of Sections 5-6 (should be confident, evidence-based)
4. Analyze tone of Sections 7-9 (should be precise, actionable)

**Tone Indicators:**
- Inspiring: Words like "democratize", "transform", "unlock", "revolutionary"
- Empathetic: Words like "frustration", "anxiety", "burden", "struggle"
- Confident: Words like "demonstrates", "validates", "evidence", "rigorously"
- Precise: Quantifiable specs, Gherkin syntax, metrics

**If Check Fails:**
- Flag sections with inappropriate tone
- Suggest tone adjustments:
  - Too technical in early sections → Add visionary framing
  - Too vague in requirements → Add specific metrics/specs
  - Too aspirational in requirements → Ground in implementation details

---

### Validation Output

After running all checks, output:

```markdown
## Coherence Validation Report

✅ **Terminology Consistency:** Core metaphor "[X]" appears in 9/9 sections
✅ **Forbidden Terms:** No violations found
⚠️  **Narrative References:** Missing connection in Section 7 → 8
✅ **Metric Alignment:** All outcomes have metrics, all CUIs instrumented
✅ **Emotional Arc:** Tone progression appropriate

**Recommended Actions:**
1. Add connecting sentence in Requirements section: "To enable the journeys described above..."

**PRD Quality Score:** 95/100
```

If any checks fail critically (forbidden terms violations, missing metrics), offer to fix automatically.
```

**Step 2: Verify coherence validation added**

Run: `grep "Coherence Validation Protocol" agents/prd_orchestrator_agent.md`

Expected: Should find the section

**Step 3: Commit coherence validation**

```bash
git add agents/prd_orchestrator_agent.md
git commit -m "feat: add Coherence Validation Protocol to orchestrator

Adds automated quality checks for PRD consistency:
- Check 1: Terminology consistency (core metaphor usage)
- Check 2: Forbidden terms scanner (regulatory compliance)
- Check 3: Narrative reference validation (sections connect)
- Check 4: Metric alignment (outcomes are measured)
- Check 5: Emotional arc progression (tone shifts appropriately)

Generates validation report with quality score and recommended fixes.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 6: Integration Testing

### Task 15: Create End-to-End Test Plan

**Files:**
- Create: `docs/testing/prd-generation-test-plan.md`

**Step 1: Create testing directory**

```bash
mkdir -p docs/testing
```

**Step 2: Write test plan**

Create file `docs/testing/prd-generation-test-plan.md`:

```markdown
# PRD Generation System - Integration Test Plan

## Purpose

Validate that the complete PRD generation system produces coherent, high-quality PRDs with proper narrative flow, context integration, and coherence validation.

## Test Scenarios

### Test 1: Full Context Available

**Setup:**
1. Populate all context files in knowledge/ folder:
   - company/mission.md
   - user-research/personas.md
   - regulatory/prohibited-terms.md
   - validation/current-performance.md
   - product/competitive.md

**Execution:**
1. Invoke prd_orchestrator_agent
2. Request: "Generate PRD for passive blood pressure monitoring feature"

**Expected Outputs:**
- ✅ All 9 sections generated
- ✅ Strategic positioning references mission
- ✅ Health impact maps to personas
- ✅ Press release uses compelling metaphor
- ✅ Validation section includes competitive table
- ✅ Requirements include prohibited terms check
- ✅ Coherence validation passes all checks
- ✅ Quality score > 90/100

**Validation:**
- Read generated PRD
- Check narrative flow (does each section reference previous?)
- Verify core metaphor appears throughout
- Confirm no prohibited terms used

---

### Test 2: Minimal Context (Graceful Degradation)

**Setup:**
1. Empty knowledge/ folder (or only manifest with no files)

**Execution:**
1. Invoke prd_orchestrator_agent
2. Request: "Generate PRD for meditation feature"

**Expected Outputs:**
- ✅ All 9 sections generated
- ✅ Orchestrator asks for mission/persona info
- ✅ Uses user-provided info instead of context files
- ⚠️  Generic tone (no brand-specific language)
- ✅ Coherence validation still runs
- ✅ Footnote documents missing context

**Validation:**
- Confirm PRD is still useful despite missing context
- Check that footnote lists what context was unavailable
- Verify no hard failures due to missing files

---

### Test 3: Narrative Coherence Test

**Goal:** Verify sections build on each other

**Setup:**
1. Standard context files populated

**Execution:**
1. Generate PRD for any feature
2. Extract key terms/metaphors from each section

**Validation Checks:**
- Strategic positioning term (e.g., "democratize") appears in:
  - Health Impact section
  - Press Release
  - Success Metrics
- Primary health outcome (from Section 3) appears in:
  - Press Release solution
  - CUJ task-to-outcome mapping
  - Success Metrics
- Core metaphor (from Press Release) appears in:
  - CUJ names
  - Requirements error messages
  - Metrics descriptions

**Expected:**
- ✅ Coherence Check 1 (Terminology) passes
- ✅ All narrative handoffs present

---

### Test 4: Regulatory Compliance Test

**Goal:** Ensure no prohibited terms appear

**Setup:**
1. Populate prohibited-terms.md with test terms:
   - "Monitor"
   - "Diagnose"
   - "Detect"
   - "Hypertension"

**Execution:**
1. Generate PRD for health feature
2. Run coherence validation

**Expected:**
- ✅ Coherence Check 2 (Forbidden Terms) runs
- ✅ If any violations, they are flagged
- ✅ Approved alternatives suggested
- ✅ Auto-replace option offered

**Validation:**
- Search generated PRD for forbidden terms
- Confirm none appear in final output
- Check that alternatives were used correctly

---

### Test 5: Traceability Test

**Goal:** Verify requirements trace to CUJs and outcomes

**Setup:**
1. Standard context files

**Execution:**
1. Generate PRD
2. Extract:
   - Health outcomes from Section 3
   - CUJ tasks from Section 7
   - Requirement IDs from Section 8

**Validation:**
- Check that Requirements section includes traceability table
- Verify each Requirement ID maps to:
  - A CUJ task
  - A health outcome
  - A regulatory note (if applicable)

**Expected:**
- ✅ Coherence Check 4 (Metric Alignment) passes
- ✅ Traceability table is complete
- ✅ No orphaned requirements (unconnected to CUJs)

---

## Success Criteria

**System passes if:**
1. All 5 test scenarios pass
2. Coherence validation catches intentional violations (forbidden terms, missing references)
3. Generated PRDs score > 90/100 on quality
4. Narrative flow is evident (not disconnected sections)
5. Graceful degradation works (minimal context still produces useful PRD)

## Test Execution Log

| Test # | Date | Result | Notes |
|:-------|:-----|:-------|:------|
| 1 | [Date] | [Pass/Fail] | [Observations] |
| 2 | [Date] | [Pass/Fail] | [Observations] |
| 3 | [Date] | [Pass/Fail] | [Observations] |
| 4 | [Date] | [Pass/Fail] | [Observations] |
| 5 | [Date] | [Pass/Fail] | [Observations] |
```

**Step 3: Commit test plan**

```bash
git add docs/testing/
git commit -m "test: add end-to-end PRD generation test plan

Creates integration test plan covering:
- Test 1: Full context available
- Test 2: Minimal context (graceful degradation)
- Test 3: Narrative coherence
- Test 4: Regulatory compliance
- Test 5: Requirements traceability

Defines success criteria and execution log template.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 7: Documentation

### Task 16: Create Comprehensive README

**Files:**
- Modify: `README.md`

**Step 1: Write comprehensive README**

Replace existing README.md with:

```markdown
# PRD Generator

A scalable, narrative-driven system for generating exceptional Product Requirement Documents (PRDs) that deliver **Inspiration + Empathy + Clarity**.

## What Makes This Different

Traditional PRD generators produce disconnected sections. This system creates **unified narratives** where each section builds on the previous one, taking readers on a journey from "why this matters to humanity" through validation rigor to precise implementation specs.

### Key Innovations

1. **Narrative Thread Architecture** - Sections hand off context to each other, creating coherent story
2. **Three New Skills** - Strategy Ladder, Health Impact, Validation Rigor fill critical gaps
3. **Context Manifest System** - Scalable, plug-and-play design for any team
4. **Coherence Validation** - Automated checks ensure consistency and quality
5. **Emotional Progression** - Tone shifts from inspiring → empathetic → rigorous → precise

### What You Get

**Generated PRDs deliver:**
- ✅ **Inspiration** - Steve Jobs keynote energy for executives and builders
- ✅ **Empathy** - Visceral user pain that drives urgency
- ✅ **Clarity** - Crystal-clear specs for engineers
- ✅ **Strategic Grounding** - Clear connection to mission and outcomes
- ✅ **Validation Credibility** - Clinical-grade rigor
- ✅ **Journey Document** - Progressive detail serving all audiences

## Quick Start

### 1. Clone and Setup

```bash
git clone <repo-url>
cd PRD-generator
./setup.sh
```

The setup script will:
- Create `knowledge/` folder structure
- Copy Context Manifest template
- Optionally add example context files

### 2. Add Your Context

Edit files in `knowledge/` folder:

```
knowledge/
├── CONTEXT_MANIFEST.md        # Edit this to map your files
├── company/
│   └── mission.md              # Add your company mission
├── user-research/
│   └── personas.md             # Add your user personas
└── regulatory/
    └── prohibited-terms.md     # Add any regulatory constraints
```

**Minimum Required Context:**
- Company mission (knowledge/company/mission.md)
- User personas (knowledge/user-research/personas.md)

**Recommended Context:**
- Prohibited terms (for regulated products)
- Current performance (for validation-heavy products)
- Competitive landscape (for positioning)

### 3. Generate Your PRD

Invoke the orchestrator agent:

```
claude agents/prd_orchestrator_agent.md
```

Or use as a skill in your Claude Code workflow.

**Request Example:**
"Generate a PRD for [your feature description]"

The system will:
1. Discover your context
2. Generate 9 coherent sections
3. Run coherence validation
4. Output a complete, narrative-driven PRD

## System Architecture

```
User Request → Orchestrator Agent
                    ↓
              Context Discovery
         (reads CONTEXT_MANIFEST.md)
                    ↓
              Story Arc Framework
      (defines narrative questions)
                    ↓
        Sequential Skill Invocation:
                    ↓
    1. strategy-ladder-skill
    2. health-impact-skill
    3. product-narrative-skill (enhanced)
    4. validation-rigor-skill
    5. cuj-generator-skill (enhanced)
    6. acceptance-criteria-skill (enhanced)
                    ↓
          Coherence Validation
      (checks consistency & quality)
                    ↓
           Final PRD Output
```

## Context System

### How It Works

The Context Manifest (`knowledge/CONTEXT_MANIFEST.md`) maps context categories to files:

```markdown
## Company Context
- **mission**: `knowledge/company/mission.md`
- **strategy**: `knowledge/company/strategy.md`
```

Skills reference context using variables:
```
{{COMPANY_MISSION}} → Contents of mission file
{{USER_PERSONAS}} → Contents of personas file
```

### Graceful Degradation

If context is missing:
- System adapts (uses generic language or asks for info)
- PRD still generates
- Footnote documents what context was unavailable

**This means:** You can start with minimal context and add more over time.

## PRD Structure (The Story Arc)

Generated PRDs follow this narrative progression:

| Section | Question | Audience | Tone |
|:--------|:---------|:---------|:-----|
| 0. Executive Summary | What is this and why does it matter? | Executives | Clarity |
| 1. Intended Use | Who is this for? What can it claim? | Regulatory | Safety |
| 2. Strategy Ladder | Why does this matter to our mission? | Executives | Inspiring |
| 3. Health Impact | What changes in users' lives? | Stakeholders | Hope |
| 4. Press Release | What's the dream experience? | Everyone | Inspiring |
| 5. Problem & Opportunity | Why is the status quo broken? | Product Team | Empathetic |
| 6. Validation Rigor | How do we know this works? | Engineers | Confident |
| 7. Critical User Journeys | How do users experience it? | Design/PM | Clear |
| 8. Functional Requirements | What exactly must we build? | Engineering | Precise |
| 9. Success Metrics | How do we know it worked? | Leadership | Accountable |

## Skills Overview

### New Skills (Added by This System)

- **strategy-ladder-skill** - Connects feature to mission and market positioning
- **health-impact-skill** - Defines measurable health outcomes and behavior change
- **validation-rigor-skill** - Demonstrates clinical/scientific credibility

### Enhanced Skills (Upgraded)

- **product-narrative-skill** - Now integrates context and hands off metaphors
- **cuj-generator-skill** - Now maps tasks to health outcomes
- **acceptance-criteria-skill** - Now includes traceability to CUJs/outcomes

## Coherence Validation

After generation, the system automatically checks:

1. **Terminology Consistency** - Core metaphor appears throughout
2. **Forbidden Terms** - No prohibited regulatory terms
3. **Narrative References** - Sections connect to each other
4. **Metric Alignment** - Outcomes have measurements
5. **Emotional Arc** - Tone progresses appropriately

**Output:** Quality score + recommended fixes

## Customization

### For Your Team

1. **Add team-specific context** to knowledge/ folder
2. **Update Context Manifest** to point to your files
3. **Customize templates** in templates/examples/
4. **Adjust prohibited terms** for your regulatory environment

### For Your Product

- Add product-specific personas
- Document your competitive landscape
- Include your validation data
- Define your strategic positioning

## Testing

Run integration tests:

```bash
# See docs/testing/prd-generation-test-plan.md
```

Tests cover:
- Full context available
- Minimal context (graceful degradation)
- Narrative coherence
- Regulatory compliance
- Requirements traceability

## Examples

See `product_specs/prds/` for example generated PRDs.

## Contributing

We welcome contributions! Areas for improvement:
- Additional skills for specific domains
- Enhanced coherence validation checks
- Alternative narrative arcs
- Context templates for specific industries

## License

[Add your license]

## Support

For questions or issues:
- See `/help` in Claude Code
- Check docs/ folder for detailed guides
- Open an issue on GitHub

---

**Built with ❤️ for Product Managers who believe PRDs should inspire, not just inform.**
```

**Step 2: Verify README**

Run: `head -50 README.md`

Expected: Should show new README content

**Step 3: Commit comprehensive README**

```bash
git add README.md
git commit -m "docs: create comprehensive README for PRD generation system

Adds complete documentation covering:
- What makes this system different
- Quick start guide (3 steps)
- System architecture overview
- Context system explanation
- PRD structure (story arc)
- Skills overview
- Coherence validation
- Customization guide
- Testing instructions

Makes system immediately usable by new teams.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Summary & Execution Options

This implementation plan transforms your PRD generation system through:

**Phase 1: Foundation** - Scalable context architecture (Tasks 1-4)
**Phase 2: New Skills** - Strategy, Health Impact, Validation Rigor (Tasks 5-7)
**Phase 3: Enhancements** - Upgrade existing skills with narrative integration (Tasks 8-10)
**Phase 4: Orchestrator** - Add Context Discovery, Story Arc, updated structure (Tasks 11-13)
**Phase 5: Validation** - Add coherence checks (Task 14)
**Phase 6: Testing** - Integration test plan (Task 15)
**Phase 7: Documentation** - Comprehensive README (Task 16)

**Total Tasks:** 16 tasks
**Estimated Time:** 4-5 weeks for full implementation

---
