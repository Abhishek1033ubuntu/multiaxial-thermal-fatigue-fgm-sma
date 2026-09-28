"""
Multi-Axial High-Cycle Thermal Fatigue Simulator
Author: Abhishek Singh
Repository: multiaxial-thermal-fatigue-fgm-sma
"""

import numpy as np

def calculate_equivalent_strain(strain_tensor: np.ndarray) -> float:
    """
    Computes von Mises equivalent strain from a 3x3 strain tensor.
    """
    exx, eyy, ezz = strain_tensor[0, 0], strain_tensor[1, 1], strain_tensor[2, 2]
    exy, eyz, ezx = strain_tensor[0, 1], strain_tensor[1, 2], strain_tensor[2, 0]
    
    eq_strain = (np.sqrt(2) / 3.0) * np.sqrt(
        (exx - eyy)**2 + (eyy - ezz)**2 + (ezz - exx)**2 +
        6.0 * (exy**2 + eyz**2 + ezx**2)
    )
    return float(eq_strain)

def coffin_manson_life(strain_amp: float, sigma_f: float = 950e6, E: float = 210e9, 
                       b: float = -0.09, epsilon_f: float = 0.45, c: float = -0.6) -> float:
    """
    Estimates fatigue life cycles (N_f) using Coffin-Manson strain-life parameterization.
    """
    # Elastic and plastic strain partitioning iteration
    N_f = 1e5  # Initial estimate
    for _ in range(20):
        elastic = (sigma_f / E) * ((2 * N_f) ** b)
        plastic = epsilon_f * ((2 * N_f) ** c)
        total = elastic + plastic
        res = strain_amp - total
        if abs(res) < 1e-8:
            break
        N_f += res * 1e5
    return max(float(N_f), 1.0)

if __name__ == "__main__":
    test_strain = np.array([
        [0.003, 0.001, 0.000],
        [0.001, -0.0015, 0.0005],
        [0.000, 0.0005, -0.0015]
    ])
    eq_str = calculate_equivalent_strain(test_strain)
    cycles = coffin_manson_life(eq_str)
    print(f"Equivalent Von Mises Strain: {eq_str:.6f}")
    print(f"Estimated Cycles to Failure: {cycles:.2e}")
