from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
import pytest

from boinor.core.propagation import (
    danby_coe,
    gooding_coe,
    markley_coe,
    mikkola_coe,
    pimienta_coe,
)
from boinor.core.propagation.farnocchia import (
    M_to_D_near_parabolic,
    _kepler_equation_near_parabolic,
    _kepler_equation_prime_near_parabolic,
    d2S_x_alt,
    dS_x_alt,
    farnocchia_coe,
    nu_from_delta_t,
)
from boinor.examples import iss


@pytest.mark.parametrize(
    "propagator_coe",
    [
        danby_coe,
        markley_coe,
        pimienta_coe,
        mikkola_coe,
        farnocchia_coe,
        gooding_coe,
    ],
)
def test_propagate_with_coe(propagator_coe):
    period = iss.period
    a, ecc, inc, raan, argp, nu = iss.classical()
    p = a * (1 - ecc**2)

    # Delete the units
    p = p.to_value(u.km)
    ecc = ecc.value
    period = period.to_value(u.s)
    inc = inc.to_value(u.rad)
    raan = raan.to_value(u.rad)
    argp = argp.to_value(u.rad)
    nu = nu.to_value(u.rad)
    k = iss.attractor.k.to_value(u.km**3 / u.s**2)

    nu_final = propagator_coe(k, p, ecc, inc, raan, argp, nu, period)

    assert_quantity_allclose(nu_final, nu)


def test_farnocchia_stuff():
    D = 1.1
    M = 1.3
    ecc = 0.999

    expected_value = 0.24328683542064818
    value = _kepler_equation_near_parabolic(D, M, ecc)
    assert_quantity_allclose(expected_value, value)

    expected_value = 2.2078790282669667
    value = _kepler_equation_prime_near_parabolic(D, M, ecc)
    assert_quantity_allclose(expected_value, value)

    x = 1.0
    with pytest.raises(AssertionError, match=""):
        value = dS_x_alt(ecc, x)

    x = 0.5
    expected_value = 7.99
    value = dS_x_alt(ecc, x)
    assert_quantity_allclose(expected_value, value)

    x = 1.0
    with pytest.raises(AssertionError, match=""):
        value = d2S_x_alt(ecc, x)

    x = 0.5
    expected_value = 47.944
    value = d2S_x_alt(ecc, x)
    assert_quantity_allclose(expected_value, value)

    expected_value = 0.9832822210139998
    value = M_to_D_near_parabolic(M, ecc)
    assert_quantity_allclose(expected_value, value)

    expected_value = 0.5381960297002113
    value = nu_from_delta_t(0.4, ecc)
    assert_quantity_allclose(expected_value, value)

    ecc = 1.00001  # needs to be hyperbolic
    expected_value = 0.5383066383929812
    value = nu_from_delta_t(0.4, ecc)
    assert_quantity_allclose(expected_value, value)
