# 🐍 Python Guide

This file serves as a **general guide** to understand and work with the Python code in this repository, covering common issues and questions.

## ▶️ How to Run the Python Code?

> ⚡ Running the Python code will regenerate the graphs in the corresponding `simulations` folder.

This project includes Python implementations of various models.
You can run the code like any standard Python project by manually installing Python and the necessary dependencies.
It will likely work with any modern Python version.

However, the **recommended way** is to use [UV](https://docs.astral.sh/uv/), which ensures a reliable, reproducible environment with the correct Python version and tested dependencies.

### What is UV?

UV is a modern Python environment manager that automatically installs the correct Python version for the project and all required dependencies listed in `pyproject.toml`.

Using UV guarantees that your code runs exactly as intended, without worrying about mismatched package versions or Python incompatibilities.

### Steps to Run

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

## Why aren’t the physical constraints explicitly implemented in the code?

Some variables naturally have limits imposed by the physical properties of the system. For example, the liquid level in a tank cannot exceed its height.

These constraints are **not explicitly enforced in the code** because there is no fully correct way to implement them without creating artificial “hacks” or workarounds. For example, see this discussion in the SciPy repository: [scipy issue #9382](https://github.com/scipy/scipy/issues/9382).

In practice, systems are not operated under conditions where the variables lose their physical meaning. The recommended approach is to design and run simulations **within the safe operational limits**, which ensures realistic and reliable results without the need to enforce hard constraints in the model.
