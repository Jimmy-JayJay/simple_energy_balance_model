import numpy as np
from model.parameters import STEFAN_BOLTZMANN, SOLAR_CONSTANT, CLIMATE_SENSITIVITY

def equilibrium_temperature(albedo, solar_constant, emissivity):
    incoming = (1 - albedo) * solar_constant / 4
    T_eq = (incoming / (STEFAN_BOLTZMANN * emissivity)) ** 0.25
    return T_eq

def radiative_forcing_co2(co2_current, co2_reference=280.0):
    return 5.35 * np.log(co2_current / co2_reference)

def temperature_change_from_forcing(forcing, sensitivity=CLIMATE_SENSITIVITY):
    return sensitivity * forcing

def calculate_temperature(albedo, solar_constant, emissivity, co2_concentration, co2_ref=280.0):
    T_base = equilibrium_temperature(albedo, solar_constant, emissivity)
    
    forcing = radiative_forcing_co2(co2_concentration, co2_ref)
    delta_T = temperature_change_from_forcing(forcing)
    
    return T_base + delta_T
