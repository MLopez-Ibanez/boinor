import numpy as np

from boinor.core.thrust.change_a_inc import delta_V


def test_change():
    V_0 = 100
    V_f = 90
    beta_0 = 0

    inc_0 = 10
    inc_f = 10
    expected_dv = abs(V_f - V_0)
    dv = delta_V(V_0, V_f, beta_0, inc_0, inc_f)

    np.testing.assert_equal(dv, expected_dv)
