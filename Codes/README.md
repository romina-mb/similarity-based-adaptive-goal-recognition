# Codebase for the Similarity-Based Adaptive Goal Recognition System

This directory contains all Python scripts required to run the full system, including:

- **Phase 1:** Processing domains and generating goal-state vectors  
- **Phase 2:** Goal recognition using process mining + similarity-based extension  
- **Full pipeline:** Automatic end-to-end execution

---


# How to Run

There are three execution modes:

**1. Step-by-Step Execution**

```bash
python "phase 1/process_goal_data.py"
python "phase 1/read_json_file_and_calc_sim_2.py"
python "phase 2/new_relearn_grsystems.py"
```

**2. Phase-Based Execution**

```bash
python "phase 1/run_phase1.py"
python "phase 2/new_relearn_grsystems.py"
```

**3. Full Pipeline (Recommended)**

```bash
python "run_new_sys.py"
```

**Note:** Phase 2 requires the JSON outputs generated in Phase 1.


# Configurable Parameters
- In `new_relearn_grsystems.py`:

testing_dataset

training_dataset

obs_percentage

option (default: -openloop)

add_new_goal_option (True/False)

output_dir

- In `read_json_file_and_calc_sim_2.py`:

num_new_goals (number of new goals to be tested)


Default settings reproduce the experiment configurations used in the paper.


# Output Files

The system stores recognition results in:

data results instance/


# Reference Code

This project extends the original system: [https://github.com/zihangs/Adaptive_GR_system](https://github.com/zihangs/Adaptive_GR_system)