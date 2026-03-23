---
name: labclaw
description: Use when doing autonomous biomedical research across biology, pharma, medical, data science, or literature search, leveraging the LabClaw skill library.
---

# LabClaw Skill

## Capability
LabClaw is a skill library for autonomous biomedical research with 206 agentic skills spanning the full biomedical stack. It can be deployed as an always-on lab agent that continuously monitors instrument feeds, interprets multimodal signals, and triggers agentic responses.

## Domains of Biomedical AI
The LabClaw skill library spans 5 primary domains (+ XR):
1. **Biology & Life Sciences (73 skills):** Bioinformatics, single-cell, genomics, proteomics, multi-omics, structural biology.
2. **Pharmacy & Drug Discovery (36 skills):** Cheminformatics, molecular ML, docking, target discovery, pharmacovigilance.
3. **Medical & Clinical (20 skills):** Clinical trials, precision medicine, oncology, rare disease diagnosis, imaging.
4. **General & Data Science (48 skills):** Statistics, ML, data management, scientific visualization, reproducibility.
5. **Literature & Search (29 skills):** Academic search, biomedical databases, patents, grants, citation management.

## Representative Workflows
Each workflow chains multiple skills into end-to-end research automation:
- **Single-cell & Spatial Omics**: `anndata`, `scanpy`, `tooluniverse-spatial-transcriptomics`
- **Drug Discovery & Design**: `rdkit`, `diffdock`, `tooluniverse-drug-repurposing`
- **Clinical & Precision Medicine**: `clinical`, `tooluniverse-precision-oncology`, `clinicaltrials-database`
- **Statistics, ML & Figures**: `statistics`, `scikit-learn`, `scientific-visualization`
- **Literature Review & Reporting**: `pubmed-search`, `citation-management`, `scientific-writing`

## Installation
If the user wants to install the full LabClaw skill library into their OpenClaw agent, instruct them to send the following command to OpenClaw:

```bash
install https://github.com/wu-yc/LabClaw
```

## Related Projects
- **LabOS (ai4labos.com):** AI-powered operating system for autonomous laboratory research.
- **MedOS (medos-ai.github.io):** AI-XR-Cobot World Model for clinical perception and action.
- **OpenClaw (github.com/openclaw/openclaw):** Main runtime that loads workspace skills.

## Authors & Maintainers
Principal Investigators:
- Le Cong (Stanford)
- Mengdi Wang (Princeton)

Contributors include:
- Yingcheng Charles Wu
- Zhe Zhao
- Jinglin Jian
