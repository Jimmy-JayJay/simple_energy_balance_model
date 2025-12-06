import streamlit as st
import numpy as np
import plotly.graph_objects as go
from model.energy_balance import calculate_temperature, equilibrium_temperature, radiative_forcing_co2
from model.parameters import (
    SOLAR_CONSTANT, EARTH_ALBEDO, EMISSIVITY_PREINDUSTRIAL,
    CO2_PREINDUSTRIAL, CO2_PRESENT, CLIMATE_SENSITIVITY
)

st.set_page_config(page_title="Energy Balance Climate Model", layout="wide")

st.title("Interactive Energy Balance Climate Model")
st.markdown("Explore how Earth's temperature responds to changes in solar radiation, albedo, and greenhouse gas concentrations.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Model Parameters")
    
    solar = st.slider(
        "Solar Constant (W/m²)",
        min_value=1200.0,
        max_value=1500.0,
        value=SOLAR_CONSTANT,
        step=10.0
    )
    
    albedo = st.slider(
        "Albedo (Reflectivity)",
        min_value=0.1,
        max_value=0.5,
        value=EARTH_ALBEDO,
        step=0.01
    )
    
    emissivity = st.slider(
        "Emissivity (Greenhouse Effect)",
        min_value=0.5,
        max_value=0.8,
        value=EMISSIVITY_PREINDUSTRIAL,
        step=0.01
    )
    
    co2 = st.slider(
        "CO₂ Concentration (ppm)",
        min_value=200.0,
        max_value=800.0,
        value=CO2_PRESENT,
        step=10.0
    )
    
    st.markdown("---")
    st.markdown("**Reference Values:**")
    st.markdown(f"Pre-industrial CO₂: {CO2_PREINDUSTRIAL} ppm")
    st.markdown(f"Present-day CO₂: {CO2_PRESENT} ppm")

with col2:
    st.subheader("Model Output")
    
    T_kelvin = calculate_temperature(albedo, solar, emissivity, co2)
    T_celsius = T_kelvin - 273.15
    
    T_base = equilibrium_temperature(albedo, solar, emissivity) - 273.15
    forcing = radiative_forcing_co2(co2, CO2_PREINDUSTRIAL)
    delta_T = T_celsius - T_base
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric("Equilibrium Temperature", f"{T_celsius:.2f} °C")
    
    with metric_col2:
        st.metric("Radiative Forcing", f"{forcing:.2f} W/m²")
    
    with metric_col3:
        st.metric("Temperature Change", f"{delta_T:+.2f} °C")
    
    st.markdown("---")
    
    co2_range = np.linspace(200, 800, 100)
    temps = [calculate_temperature(albedo, solar, emissivity, c) - 273.15 for c in co2_range]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=co2_range,
        y=temps,
        mode='lines',
        name='Model',
        line=dict(color='#64ffda', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=[co2],
        y=[T_celsius],
        mode='markers',
        name='Current',
        marker=dict(size=12, color='#ff6b6b')
    ))
    
    fig.update_layout(
        title="Temperature vs CO₂ Concentration",
        xaxis_title="CO₂ Concentration (ppm)",
        yaxis_title="Temperature (°C)",
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#e6f1ff")
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("""
**Model Equations:**
- Energy Balance: (1-α)S/4 = σεT⁴
- Radiative Forcing: ΔF = 5.35 × ln(CO₂/CO₂_ref)
- Temperature Response: ΔT = λ × ΔF

Where α = albedo, S = solar constant, σ = Stefan-Boltzmann constant, ε = emissivity, λ = climate sensitivity
""")

st.caption("Built by [Jimmy Matewere](https://github.com/Jimmy-JayJay)")
