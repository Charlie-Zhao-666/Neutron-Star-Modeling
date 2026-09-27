# Neutron-Star-Modeling

Static structure modeling of degenerate stars (white dwarfs and
idealized neutron stars) in Python. The program integrates the stellar
structure equations outward from the center under Newtonian gravity
with a non-relativistic, zero-temperature ideal Fermi gas equation of
state (an n = 3/2 polytrope), stops when the pressure drops to zero,
and reports the star's mass and radius.

This is a static structure calculation: it computes how pressure,
density and enclosed mass vary with radius. It is not a time-evolution
simulation of a star.

Sister project: [N-Body-Simulation](https://github.com/Charlie-Zhao-666/N-Body-Simulation)

## Repository contents

| File | Description |
|---|---|
| `non_relativistic_simulation.py` | First version of the stellar-structure integrator. Offers two star types at runtime - white dwarf (electron degeneracy pressure; two atomic mass units of matter per electron) or an idealized neutron star (pure neutrons, zero temperature, no nuclear interactions). The central density is set by the dimensionless central Fermi momentum xc = Pf/(mc), currently xc = 0.1. Integrates outward from the center with radial step dr = 100 m until the pressure reaches zero, then prints the total mass and radius in SI and in solar units. |
| `.gitignore` | Standard Python ignore rules. |
| `README.md` | This file. |

## Completed work so far

- Non-relativistic ideal Fermi gas equation of state (n = 3/2
  polytrope, P = K * rho^(5/3)), with K derived from fundamental
  constants for each star type.
- Newtonian hydrostatic integration from the center outward, tracking
  pressure, density, enclosed mass and radius shell by shell.
- Two star types selectable at runtime: white dwarf / ideal neutron
  star.
- Mass and radius output in kg / m and in solar units.

## Planned / future work

- Verification against the n = 3/2 Lane-Emden reference solution.
- Radial-step (dr) convergence study, and interpolation of the
  zero-pressure surface instead of overshooting it by up to one step.
- Scanning the central parameter xc to produce a mass-radius relation
  (including the white-dwarf mass-limit behavior).
- Profile plotting (density, pressure, enclosed mass, gravity versus
  radius) and saved result figures.
- Relativistic degenerate-gas EOS (the xc parametrization already
  supports the transition Pf ~ mc).
- Tolman-Oppenheimer-Volkoff (general-relativistic) structure
  equations.
- A written project report.

## How to run

```
pip install numpy
python non_relativistic_simulation.py
```

Choose the star type at the prompt (1 = white dwarf, 2 = neutron
star).

## Physics assumptions and limitations

- Newtonian gravity; no general relativity.
- Zero-temperature, non-relativistic ideal Fermi gas. The neutron-star
  option uses pure neutrons and ignores nuclear interactions, so its
  mass and radius values are idealized and are not expected to match
  real neutron stars.
- The integration stops at the first grid point with non-positive
  pressure, so the surface radius is overshot by up to one radial
  step.

## Verification status

Systematic verification (Lane-Emden benchmark, dr convergence) is
planned and has not been completed yet. Current results should be read
as a first working version.

## References

- R. R. Silbar & S. Reddy, "Neutron Stars for Undergraduates",
  Am. J. Phys. 72, 892 (2004).
- D. J. Griffiths & D. F. Schroeter, "Introduction to Quantum
  Mechanics" (degenerate Fermi gas background).
