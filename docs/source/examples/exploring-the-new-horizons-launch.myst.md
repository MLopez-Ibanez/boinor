---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# New Horizons launch and trajectory

Main data source: Guo & Farquhar "New Horizons Mission Design" http://www.boulder.swri.edu/pkb/ssr/ssr-mission-design.pdf

```{code-cell} ipython3
from astropy import time
from astropy import units as u

from boinor import iod

from boinor.bodies import Sun, Earth, Jupiter
from boinor.ephem import Ephem
from boinor.frames import Planes
from boinor.plotting import OrbitPlotter
from boinor.plotting.orbit.backends import Matplotlib2D
from boinor.twobody import Orbit
from boinor.util import norm
```

## Parking orbit

Quoting from "New Horizons Mission Design":

> It was first inserted into an elliptical Earth parking orbit
of **perigee altitude 165 km** and **apogee altitude 215 km**. [Emphasis mine]

```{code-cell} ipython3
r_p = Earth.R + 165 * u.km
r_a = Earth.R + 215 * u.km

a_parking = (r_p + r_a) / 2
ecc_parking = 1 - r_p / a_parking

parking = Orbit.from_classical(
    Earth,
    a_parking,
    ecc_parking,
    0 * u.deg,
    0 * u.deg,
    0 * u.deg,
    0 * u.deg,  # We don't mind
    time.Time("2006-01-19", scale="utc"),
)

print(parking.v)
parking.plot()
```

## Hyperbolic exit

Hyperbolic excess velocity:

$$ v_{\infty}^2 = \frac{\mu}{-a} = 2 \varepsilon = C_3 $$

Relation between orbital velocity $v$, local escape velocity $v_e$ and hyperbolic excess velocity $v_{\infty}$:

$$ v^2 = v_e^2 + v_{\infty}^2 $$

### Option a): Insert $C_3$ from report, check $v_e$ at parking perigee:

```{code-cell} ipython3
C_3_A = 157.6561 * u.km**2 / u.s**2  # Designed

a_exit = -(Earth.k / C_3_A).to(u.km)
ecc_exit = 1 - r_p / a_exit

exit = Orbit.from_classical(
    Earth,
    a_exit,
    ecc_exit,
    0 * u.deg,
    0 * u.deg,
    0 * u.deg,
    0 * u.deg,  # We don't mind
    time.Time("2006-01-19", scale="utc"),
)

norm(exit.v).to(u.km / u.s)
```

Quoting "New Horizons Mission Design":

> After a short coast in the parking orbit, the spacecraft was then injected into
the desired heliocentric orbit by the Centaur second stage and Star 48B third
stage. At the Star 48B burnout, the New Horizons spacecraft reached the highest
Earth departure speed, **estimated at 16.2 km/s**, becoming the fastest spacecraft
ever launched from Earth.  [Emphasis mine]

```{code-cell} ipython3
v_estimated = 16.2 * u.km / u.s

print(
    "Relative error of {:.2f} %".format(
        (norm(exit.v) - v_estimated) / v_estimated * 100
    )
)
```

So it stays within the same order of magnitude. Which is reasonable, because real life burns are not instantaneous.

```{code-cell} ipython3
:tags: [nbsphinx-thumbnail]

from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
backend = Matplotlib2D(ax=ax)
op = OrbitPlotter(backend=backend)

op.plot(parking)
op.plot(exit)

ax.set_xlim(-8000, 8000)
ax.set_ylim(-20000, 20000)
```

### Option b): Compute $v_{\infty}$ using the Jupyter flyby

According to Wikipedia, the closest approach occurred at 05:43:40 UTC. We can use this data to compute the solution of the Lambert problem between the Earth and Jupiter:

```{code-cell} ipython3
nh_date = time.Time("2006-01-19 19:00", scale="utc").tdb
nh_flyby_date = time.Time("2007-02-28 05:43:40", scale="utc").tdb
nh_tof = nh_flyby_date - nh_date

nh_r_0, v_earth = Ephem.from_body(Earth, nh_date).rv(nh_date)
nh_r_f, v_jup = Ephem.from_body(Jupiter, nh_flyby_date).rv(nh_flyby_date)

nh_v_0, nh_v_f = iod.lambert(Sun.k, nh_r_0, nh_r_f, nh_tof)
```

The hyperbolic excess velocity is measured with respect to the Earth:

```{code-cell} ipython3
C_3_lambert = (norm(nh_v_0 - v_earth)).to(u.km / u.s) ** 2
C_3_lambert
```

```{code-cell} ipython3
print("Relative error of {:.2f} %".format((C_3_lambert - C_3_A) / C_3_A * 100))
```

Which again, stays within the same order of magnitude of the figure given to the Guo & Farquhar report.

+++

## From Earth to Jupiter

```{code-cell} ipython3
nh = Orbit.from_vectors(Sun, nh_r_0, nh_v_0, nh_date)

op = OrbitPlotter(plane=Planes.EARTH_ECLIPTIC)

op.plot_body_orbit(Jupiter, nh_flyby_date)
op.plot_body_orbit(Earth, nh_date)

op.plot(nh, label="New Horizons", color="k")
```
