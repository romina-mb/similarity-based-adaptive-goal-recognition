# Evaluation Pipeline

This directory contains all scripts used to reproduce the evaluation reported in the paper.

---


# How to Run the Evaluation
- Step 1
```bash
python system_evaluation.py
```

- Step 2
```bash
python combine_measure_table.py
```

- Step 3
```bash
python evaluation_analysis.py
```

- Step 4
```bash
python "t-test or wilcoxon-test based on distribution.py"
```

- Step 5

Open and run all cells in:
`chart_eval_analysis.ipynb`



# Input

The evaluation uses recognition results stored in:

gradual/
occ/
sudden/

> (each containing results for 13 domains × 76 categories × 3 modes)


# Output

Final aggregated metrics and statistical test results are saved in:

final results/