# ▶️ How to Run the Python Code

> ⚡ Running the Python code will regenerate the graphs in the corresponding `simulations` folder.

This project includes Python implementations of various models.
You can run the code like any standard Python project by manually installing Python and the necessary dependencies.
It will likely work with any modern Python version.

However, the **recommended way** is to use [UV](https://docs.astral.sh/uv/), which ensures a reliable, reproducible environment with the correct Python version and tested dependencies.

## What is UV?

UV is a modern Python environment manager that automatically installs the correct Python version for the project and all required dependencies listed in `pyproject.toml`.

Using UV guarantees that your code runs exactly as intended, without worrying about mismatched package versions or Python incompatibilities.

## Steps to Run

> 🛠️ You do not need Python installed on your computer.
> UV will automatically download and manage the correct Python version for the project.

1. **Install UV**
   Follow the instructions in the [UV documentation](https://docs.astral.sh/uv/) to install UV on your system.

2. **Install dependencies**
   The project uses a `pyproject.toml` file to specify all required packages.
   After installing UV, run:

   ```bash
   uv sync
   ```

3. **Run the code**
   You can run Python scripts directly through UV to ensure the correct environment is used:

   ```bash
   uv run python_file.py
   ```

   For example, if you are in the repository root, to run the SciPy simulation of the cubic tank with a pump-controlled inlet and outlet:

   ```bash
   uv run models/tanks/cubic-pump-controlled/sim_scipy.py
   ```
