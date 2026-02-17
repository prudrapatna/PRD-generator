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
