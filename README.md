# Tanzania XDR-TB Genomics Case Study

## Project Overview

This project explores resistance-associated genetic variants reported in a published case study of extensively drug-resistant tuberculosis (XDR-TB) in Tanzania.

The practical uses Python, Biopython and Matplotlib to inspect a *Mycobacterium tuberculosis* reference sequence, examine selected genetic changes and organise published mutation findings.

## Objectives

- Explore the *Rv0678 (mmpR5)* reference gene sequence.
- Translate DNA sequences into protein sequences.
- Investigate the reported frameshift variants.
- Organise reported mutation findings into a structured dataset.
- Visualise selected reported allele frequencies.
- Interpret the potential significance of changes in resistance-associated variants over time.

## Tools and Technologies

- Python
- Biopython
- Matplotlib
- Linux
- NCBI reference genome and annotation

## Project Structure

```text
tanzania-xdr-tb-genomics/
├── data/
│   ├── reference/
│   └── variants/
├── scripts/
├── results/
├── reports/
└── README.md
```

## Key Findings Explored

- Two reported frameshift variants in *mmpR5 (Rv0678)*.
- Changes in reported *gyrA* variants.
- A reported frameshift variant in *ald*.
- Variation in selected allele frequencies across serial isolates.

## Important Scientific Limitation

The original patient's sequencing reads were not publicly available in the case study. Therefore, this project explores published findings and reference sequences; it does not independently reproduce the patient's whole-genome sequencing analysis.

## Reference

Katale et al. (2024). *Clinical application of whole-genome sequencing in the management of extensively drug-resistant tuberculosis: a case report.*

