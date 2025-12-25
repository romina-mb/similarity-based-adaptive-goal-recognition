import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent

def run_script(script_name):
    script_path = BASE_DIR / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
        cwd=BASE_DIR
    )
    return result.returncode

if __name__ == "__main__":
    print("Running process_goal_data.py ...")
    run_script("process_goal_data.py")

    print("Running read_json_file_and_calc_sim_2.py ...")
    run_script("read_json_file_and_calc_sim_2.py")
