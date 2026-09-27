import numpy as np
import matplotlib.pyplot as plt
import time

# Constants
G = 6.67430e-11             # Gravitational constant in m^3 kg^-1 s^-2
h = 6.62607015e-34          # Planck constant in J s
h_bar = h / (2 * np.pi)     # Reduced Planck constant in J s
me = 9.1093837139e-31       # Electron mass in kg
mn = 1.67492750056e-27      # Neutron mass in kg
m_u = 1.66053906892e-27     # Atomic mass constant in kg
solar_mass = 1.989e30       # Mass of the Sun in kg
solar_radius = 6.957e8      # radius of the Sun in m
c = 3e8                     # Speed of light in m/s

# self-defined parameters
xc = 0.1                    # Dimensionless central fermi momentum coefficient (Pf / mc)
Rho = []                    # Polytropic constant (determined by xc and star type)
P = [0]                     # Initial pressure (adjust as needed)
dr = 100                    # Grid spacing (adjust as needed)


# Determain K and density by star type and xc 
stars_selection = 0
while stars_selection not in (1, 2):
    stars_selection = int(input("You want to run a white dwarf simulation or a neutron star simulation? (Enter '1' for white dwarf or '2' for neutron star)\nYour answer:"))

if stars_selection == 1:    # white dwarf
    mf = me
    K = h_bar**2 / (5*me) * (3 * np.pi**2)**(2 / 3)*(2*m_u)**(-5 / 3)
    Rho.append((xc * mf*c)**3 / (3 * np.pi**2 * h_bar**3) * 2 * m_u)


elif stars_selection == 2:  # neutron star
    mf = mn
    K = h_bar**2 * (3 * np.pi**2) ** (2 / 3) / (5 * mn**(8 / 3))
    Rho.append((xc * mf*c)**3 / (3 * np.pi**2 * h_bar**3) * 1 * mn)

print(K, Rho)


# Initial conditions
P[0] = K * Rho[0]**(5/3)    # Initial pressure based on initial density
print(P)
dm = 0
m = [0]
r = [0]

# state dictionaries
inner_state = {
    "mass" : m[-1],
    "radius" : r[-1]
}

shell_state = {
    "pressure" : P[-1],
    "density" : Rho[-1],
    "change in mass" : dm,
    "change in radius" : dr,
}


#define functions for Polytropic constant, density, mass, pressure, and combined main function
def Rho_update(inner_state, shell_state):
    Rho.append((shell_state["pressure"] / K) ** (3 / 5))
    shell_state["density"] = Rho[-1]
    return Rho[-1]

def dm_update(inner_state, shell_state):
    dm = 4 * np.pi * inner_state["radius"]**2 * shell_state["density"] * shell_state["change in radius"]
    shell_state["change in mass"] = dm
    return dm

def P_update(inner_state, shell_state):
    P.append(shell_state["pressure"] - (G * inner_state["mass"] * shell_state["density"] * shell_state["change in radius"]) / (inner_state["radius"]**2))
    shell_state["pressure"] = P[-1]
    return P[-1]

def main():
    #radius update
    r.append(r[-1] + dr)
    inner_state["radius"] = r[-1]

    # density update
    Rho_update(inner_state, shell_state)

    # mass update
    m.append(m[-1] + dm_update(inner_state, shell_state))
    inner_state["mass"] = m[-1]

    # pressure update
    P_update(inner_state, shell_state)

    return None


print("simulation start")
# run the simulation until the pressure drops to zero
step = 0
while shell_state["pressure"] > 0:
    main()
    print(P[-1])
    step += 1


print("==========Simulation Over==========\n")
print(f"{step} steps used")

print(f"\nThe mass of this star is: {inner_state['mass']:.3e} Kg\nWhich is: {inner_state['mass']/solar_mass:.3e} solar masses\n\nThe radius of this star is: {inner_state['radius']:.3e} m\nWhich is: {inner_state['radius']/solar_radius:.3e} solar radius\n")
