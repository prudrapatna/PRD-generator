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
- **competitive**: `knowledge/target_performance/competitor_analysis.md` - Competitor analysis, differentiation
- **tech-stack**: `knowledge/product/tech-stack.md` - Technical constraints, architecture

## Regulatory Context
- **classification**: `knowledge/regulatory/classification.md` - Product regulatory classification
- **prohibited-terms**: `knowledge/regulatory/prohibited-terms.md` - Terms to avoid in documentation
- **indications**: `knowledge/regulatory/indications.md` - Intended use, contraindications

## User Research
- **personas**: `knowledge/user_research/proactive_adopter_profile.md` - Target user profiles and behaviors
- **pain-points**: `knowledge/user_research/hypertension_problem_definition.md` - User problems and frustrations
- **insights**: `knowledge/user_research/insights.md` - Research findings and key insights

## Validation Data
- **performance**: `knowledge/algorithm_overview_and_target_performance/algorithm_overview_and_target_performance.md` - Current performance metrics
- **validation-plan**: `knowledge/target_performance/target_performance.md` - Clinical study design, timeline
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
