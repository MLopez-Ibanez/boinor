from matplotlib import pyplot as plt
from numpy.testing import assert_allclose
import pytest

from boinor.bodies import Earth, Mars
from boinor.plotting.porkchop import PorkchopPlotter
from boinor.util import time_range


@pytest.mark.mpl_image_compare
def test_porkchop_plotting():
    """compare pictures with generated reference pictures

    This test generates a plot and compares the resulting picture
    with a previously generated one.
    """
    fig, ax = plt.subplots()

    launch_span = time_range("2005-04-30", end="2005-10-07")
    arrival_span = time_range("2005-11-16", end="2006-12-21")
    porkchop_plot = PorkchopPlotter(
        Earth, Mars, launch_span, arrival_span, ax=ax
    )
    dv_dpt, dv_arr, c3dpt, c3arr, tof = porkchop_plot.porkchop()

    return fig


def test_porkchop_deprecated_function():
    """deprecated method in PorkchopPlotter

    All plotting classes shall have similar user experience (-> poliasto/poliastro#1589)
    So the method PorkchopPlotter.porkchop() will be deprecated and replaced by
    PorkchopPlotter.plot()

    This test is needed to ensure that both methods still have the same results.
    """
    fig, ax = plt.subplots()

    launch_span = time_range("2005-04-30", end="2005-10-07")
    arrival_span = time_range("2005-11-16", end="2006-12-21")
    porkchop_plot = PorkchopPlotter(
        Earth, Mars, launch_span, arrival_span, ax=ax
    )
    dv_dpt, dv_arr, c3dpt, c3arr, tof = porkchop_plot.porkchop()
    dv_dpt_pl, dv_arr_pl, c3dpt_pl, c3arr_pl, tof_pl = porkchop_plot.plot()

    assert_allclose(dv_dpt, dv_dpt_pl, rtol=1e-10)
    assert_allclose(dv_arr, dv_arr_pl, rtol=1e-10)
    assert_allclose(c3dpt, c3dpt_pl, rtol=1e-10)
    assert_allclose(c3arr, c3arr_pl, rtol=1e-10)
    assert_allclose(tof, tof_pl, rtol=1e-10)
