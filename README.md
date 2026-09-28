# Multi-Axial High-Cycle Thermal Fatigue Analysis (FGM-SMA Lattices)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Abhishek1033ubuntu/multiaxial-thermal-fatigue-fgm-sma/blob/main/notebooks/multiaxial_thermal_fatigue_sim.ipynb)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

## Overview
This repository implements a multi-physics computational framework designed to analyze and mitigate structural fatigue under multi-axial high-cycle thermal-mechanical loading ($N > 10^7$ cycles). It models Functionally Graded Material (FGM) integrated with Shape Memory Alloy (SMA) micro-vented 3D structures to sustain high thermal gradients while damping cyclic mechanical resonance.

### Technical Specifications & Physics Formulation
- **Stress-State Tensor:** Multi-axial fatigue damage mapping under severe thermal gradient cycling ($\Delta T > 800\text{ K}$).
- **Material Topology:** Functionally Graded Material (FGM) transition zones coupled with NiTi-based Shape Memory Alloy phase transformations.
- **Constitutive Law:** Modified Coffin-Manson relationship incorporating elastoplastic phase shifts and thermal creep coupling.

## Repository Structure
```text
├── LICENSE
├── README.md
├── docs/
│   └── DOSSIER-MA-HCTL-001.md
├── notebooks/
│   └── multiaxial_thermal_fatigue_sim.ipynb
└── src/
    └── fatigue_model.py

```

## Quick Start (Google Colab)

Click the **Open In Colab** badge above to launch the interactive simulation notebook directly in Google Colab.

## License

Distributed under the MIT License. See `LICENSE` for details.
