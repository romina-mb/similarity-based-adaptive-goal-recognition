# Similarity-Based Adaptive Goal Recognition System
Source Code • Dataset • Evaluation Pipeline

This repository contains the full implementation, datasets, and evaluation scripts for the paper:

**Adaptive Goal Recognition Using Process Mining Techniques in Dynamic Environments and Its Development to Recognize New Goals**
*(currently under review)*

This work extends the Adaptive GR System by introducing a **similarity-based mechanism** that enables recognizing previously unseen goals before sufficient data is available to learn their Petri Nets.  
The experiments cover **13 IPC domains** and **76 problem categories**.

---

# How to Run the System

The recommended full execution:

```bash
python "run_new_sys.py"
```

**Detailed execution instructions and parameters are provided in:**

codes/README.md


# Dataset

**Located in:**

dataset/

**Includes:**

- domains.zip (used in Phase 1)

- experimental_data.zip (used in Phase 2)


**Details and instructions:**

dataset/README.md


# Experimental Results

The system outputs CSV files in:

data results instance/


> These files contain recognition results for:

- Normal mode

- New-goal mode without similarity

- New-goal mode with similarity


**Evaluation scripts for generating tables, statistical tests, and plots:**

evaluation/README.md


# Requirements

- Python 3.12 (tested on Windows)

- Install packages manually


# References

- Original Adaptive GR System: [https://github.com/zihangs/Adaptive_GR_system](https://github.com/zihangs/Adaptive_GR_system)


- Original IPC Domains Dataset: [https://github.com/pucrs-automated-planning/goal-plan-recognition-dataset](https://github.com/pucrs-automated-planning/goal-plan-recognition-dataset)  

- Original Continuous GR dataset: [https://figshare.unimelb.edu.au/articles/dataset/Continuous_GR_experimental_data_for_PM-based_systems/21802081](https://figshare.unimelb.edu.au/articles/dataset/Continuous_GR_experimental_data_for_PM-based_systems/21802081)