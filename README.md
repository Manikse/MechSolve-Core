# MechSolve-Core

MechSolve-Core is a deterministic command-line utility engineered for the rapid computation of support reactions and maximum bending moments in structural engineering. It is designed to replace manual statics calculations with an automated, error-free execution model, eliminating the human factor in routine pre-analytical tasks.

## Key Features
* O(1) Execution Time: Bypasses graphical interface overhead for instantaneous terminal execution.
* Boundary Condition Analysis: Automatically resolves reaction forces (Ra, Rb) based on input parameters.
* Peak Moment Computation: Identifies and calculates the absolute maximum bending moment (M_max) under point loads using strict static equilibrium equations: $M_{max} = \frac{F \cdot a \cdot b}{L}$.
* Algorithmic Precision: Hardcoded mathematical logic ensures zero deviation in standard load cases.

## Tech Stack
* Core Engine: Python 3.8+
* Interface: Command Line Interface (argparse)

## Project Structure
* `beam_calc.py`: The core execution script containing the mathematical models and terminal output formatting.
* `ai_agent_promo.txt`: System instructions for autonomous distribution and network propagation.

## Future Roadmap
[ ] Integration of continuous beam matrices and distributed load algorithms.
[ ] Automated PDF report compilation aligned with standard university laboratory requirements.
[ ] Direct API integration with the VestaStack ecosystem.

## Author
manikse

Student at Slovak University of Technology (STU), Bratislava
Founder of VestaStack & Lume
Specializing in Automation and Informatization of Processes

<p align="center">
<a href="https://ko-fi.com/manikse">
<img src="https://storage.ko-fi.com/cdn/kofi3.png?v=3" alt="Support the developer at ko-fi.com" width="200">
</a>

<em>If MechSolve optimized your calculation workflow, consider supporting the developer.</em>
</p>

<p align="center">
Engineered by manikse
</p>
