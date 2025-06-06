from astropy import units as u

from boinor.core.thrust.change_ecc_inc import (
    change_ecc_inc as change_ecc_inc_fast,
)


def change_ecc_inc(orb_0, ecc_f, inc_f, f):
    """Simultaneous eccentricity and inclination changes. Guidance law from the model. Thrust is aligned with an inertially fixed direction perpendicular to the semimajor axis of the orbit.

    Parameters
    ----------
    orb_0 : Orbit
        Initial orbit, containing all the information.
    ecc_f : float
        Final eccentricity.
    inc_f : ~astropy.units.quantity.Quantity
        Final inclination.
    f : ~astropy.units.quantity.Quantity
        Magnitude of constant acceleration.

    Returns
    -------
    a_d, delta_V, t_f : tuple (function, ~astropy.units.quantity.Quantity, ~astropy.time.Time)

    References
    ----------
    * Pollard, J. E. "Simplified Analysis of Low-Thrust Orbital Maneuvers", 2000.
    """
    r, v = orb_0.rv()
    a_d, delta_V, t_f = change_ecc_inc_fast(
        k=orb_0.attractor.k.to_value(u.km**3 / u.s**2),
        a=orb_0.a.to_value(u.km),
        ecc_0=orb_0.ecc.value,
        ecc_f=ecc_f,
        inc_0=orb_0.inc.to_value(u.rad),
        inc_f=inc_f.to_value(u.rad),
        argp=orb_0.argp.to_value(u.rad),
        r=r.to_value(u.km),
        v=v.to_value(u.km / u.s),
        f=f.to_value(u.km / u.s**2),
    )
    return a_d, delta_V << (u.km / u.s), t_f << u.s
