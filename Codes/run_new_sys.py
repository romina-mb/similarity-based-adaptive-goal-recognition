import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent

def run_script(script_relative_path):
    script_path = BASE_DIR / script_relative_path
    script_dir = script_path.parent

    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
        cwd=script_dir
    )
    return result.returncode

if __name__ == "__main__":
    print("Running phase 1...")
    run_script("phase 1/run_phase1.py")

    print("Running phase 2...")
    run_script("phase 2/new_relearn_grsystems.py")

    print("All scripts finished successfully.")
