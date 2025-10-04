import subprocess
from pathlib import Path

# Path to models folder
models_dir = Path("models")

# Loop through all sim_*.py files
for script in models_dir.rglob("sim*.py"):
    print(f"Running {script}...")
    subprocess.run(["python", str(script)], check=True)
    print(f"Finished {script}.\n")
