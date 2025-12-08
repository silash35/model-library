import subprocess
from pathlib import Path

print("--- Running all simulations ---")
sim_scripts = Path("models").rglob("sim*.py")
for script in sim_scripts:
    print(f"Running {script}...")
    subprocess.run(["python", str(script)], check=True)
    print(f"Finished {script}.\n")


print("--- Running all experiments ---")
exp_scripts = sorted(Path("experiments").rglob("exp*.py"))
for script in exp_scripts:
    print(f"Running {script}...")
    subprocess.run(["python", str(script)], check=True)
    print(f"Finished {script}.\n")
