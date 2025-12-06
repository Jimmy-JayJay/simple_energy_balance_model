# Energy Balance Climate Model

Interactive climate model demonstrating how Earth's temperature responds to changes in solar radiation, albedo, and greenhouse gas concentrations.

## Model Description

This is a zero-dimensional energy balance model based on fundamental physics:

**Energy Balance Equation:**

```
(1 - α) × S / 4 = σ × ε × T⁴
```

Where:

- α = albedo (planetary reflectivity)
- S = solar constant (~1361 W/m²)
- σ = Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²/K⁴)
- ε = emissivity (greenhouse effect parameter)
- T = equilibrium temperature

**Radiative Forcing from CO₂:**

```
ΔF = 5.35 × ln(CO₂ / CO₂_ref)
```

**Temperature Response:**

```
ΔT = λ × ΔF
```

Where λ is the climate sensitivity parameter (~0.8 K/(W/m²))

## Features

- Interactive parameter adjustment (solar constant, albedo, emissivity, CO₂)
- Real-time temperature calculations
- Visualization of temperature-CO₂ relationship
- Display of radiative forcing and temperature changes

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Project Structure

```
energy-balance-model/
├── app.py                    # Main Streamlit application
├── model/
│   ├── energy_balance.py     # Core physics calculations
│   └── parameters.py         # Physical constants
├── data/                     # Data files (future)
├── utils/                    # Utility functions (future)
├── requirements.txt
└── README.md
```

## Scientific Background

This model implements a simplified version of Earth's energy balance. While real climate models are far more complex (3D, time-dependent, with detailed atmospheric physics), this zero-dimensional model captures the fundamental relationship between greenhouse gases and temperature.

**Limitations:**

- No spatial variation
- No time dependence (instantaneous equilibrium)
- Simplified greenhouse effect representation
- No ocean heat uptake
- No detailed cloud physics

**Appropriate for:**

- Understanding basic climate physics
- Exploring parameter sensitivity
- Educational demonstrations
- First-order temperature estimates

## References

- Myhre et al. (1998): Radiative forcing formula for CO₂
- IPCC AR6 WG1: Climate sensitivity estimates
- Pierrehumbert (2010): Principles of Planetary Climate

## Author

[Jimmy Matewere](https://github.com/Jimmy-JayJay)
-Climate Scientist & Data Analyst
