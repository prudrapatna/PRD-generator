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
