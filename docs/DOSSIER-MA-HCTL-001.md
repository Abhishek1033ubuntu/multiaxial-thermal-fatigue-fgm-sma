# Technical Dossier: DOSSIER-MA-HCTL-001
## High-Cycle Multi-Axial Thermal Fatigue Mitigation via FGM-SMA Architectures

### 1. Mathematical Formulation
The von Mises equivalent strain amplitude under thermal-mechanical loading is given by:

$$\Delta \varepsilon_{\text{eq}} = \frac{\sqrt{2}}{3} \left[ (\Delta \varepsilon_{xx} - \Delta \varepsilon_{yy})^2 + (\Delta \varepsilon_{yy} - \Delta \varepsilon_{zz})^2 + (\Delta \varepsilon_{zz} - \Delta \varepsilon_{xx})^2 + 6(\Delta \varepsilon_{xy}^2 + \Delta \varepsilon_{yz}^2 + \Delta \varepsilon_{zx}^2) \right]^{1/2}$$

The fatigue life calculation incorporates damage accumulation under cyclic thermal shock:

$$\frac{\Delta \varepsilon_{\text{eq}}}{2} = \frac{\sigma'_f}{E} (2N_f)^b + \varepsilon'_f (2N_f)^c$$

### 2. Microstructural Energy Dissipation
The integration of phase-transforming pseudoelastic SMA inserts dissipates strain energy density $W_{\text{diss}}$ through hysteresis:

$$W_{\text{diss}} = \oint \sigma_{ij} \, d\varepsilon_{ij}^{\text{trans}}$$

### 3. Computational Boundary Conditions
- **Thermal Cycle:** $300\text{ K} \rightarrow 1200\text{ K} \rightarrow 300\text{ K}$ at $100\text{ Hz}$.
- **Constraint Matrix:** Fixed-free cantilever lattice with micro-venting channels for internal pressure release.
