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
