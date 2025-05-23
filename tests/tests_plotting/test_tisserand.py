from astropy import units as u
from matplotlib import pyplot as plt
import pytest

from boinor.bodies import Earth, Mars, Venus
from boinor.plotting.tisserand import TisserandKind, TisserandPlotter
from boinor.plotting.util import BODY_COLORS


@pytest.mark.mpl_image_compare
def test_tisserand_plotting():
    fig, ax = plt.subplots()

    # Build custom axis
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    ax.set_title("Energy Tisserand for Venus, Earth and Mars")
    ax.set_xlabel("$R_{p} [AU]$")
    ax.set_ylabel("Heliocentric Energy [km2 / s2]")
    ax.set_xscale("log")
    ax.set_xlim(10**-0.4, 10**0.15)
    ax.set_ylim(-700, 0)

    # Generate a Tisserand plotter
    tp = TisserandPlotter(axes=ax, kind=TisserandKind.ENERGY)

    # Plot Tisserand lines within 1km/s and 10km/s
    for planet in [Venus, Earth, Mars]:
        ax = tp.plot(planet, (1, 14) * u.km / u.s, num_contours=14)

    # Let us label previous figure
    tp.ax.text(0.70, -650, "Venus", color=BODY_COLORS["Venus"])
    tp.ax.text(0.95, -500, "Earth", color=BODY_COLORS["Earth"])
    tp.ax.text(1.35, -350, "Mars", color=BODY_COLORS["Mars"])

    return fig


# TODO: @pytest.mark.mpl_image_compare
@pytest.mark.parametrize(
    "kind",
    [
        TisserandKind.ENERGY,
        TisserandKind.APSIS,
        TisserandKind.PERIOD,
    ],
)
def test_tisserand_plotting_kind(kind):
    fig, ax = plt.subplots()

    # Build custom axis
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    ax.set_title("Energy Tisserand for Venus, Earth and Mars")
    ax.set_xlabel("$R_{p} [AU]$")
    ax.set_ylabel("Heliocentric Energy [km2 / s2]")
    ax.set_xscale("log")
    ax.set_xlim(10**-0.4, 10**0.15)
    ax.set_ylim(-700, 0)

    # Generate a Tisserand plotter
    tp = TisserandPlotter(axes=ax, kind=kind)

    # Plot Tisserand lines within 1km/s and 10km/s
    for planet in [Venus, Earth, Mars]:
        ax = tp.plot(planet, (1, 14) * u.km / u.s, num_contours=14)

    # Let us label previous figure
    tp.ax.text(0.70, -650, "Venus", color=BODY_COLORS["Venus"])
    tp.ax.text(0.95, -500, "Earth", color=BODY_COLORS["Earth"])
    tp.ax.text(1.35, -350, "Mars", color=BODY_COLORS["Mars"])


# this test only checks whether there is no exception in this code
# see TODO above
#    return fig


# TODO: @pytest.mark.mpl_image_compare
@pytest.mark.parametrize(
    "color",
    [
        None,
        "orange",
        "blue",
    ],
)
def test_tisserand_plotting_line(color):
    fig, ax = plt.subplots()

    # Build custom axis
    fig, ax = plt.subplots(1, 1, figsize=(15, 7))
    ax.set_title("Energy Tisserand for Venus, Earth and Mars")
    ax.set_xlabel("$R_{p} [AU]$")
    ax.set_ylabel("Heliocentric Energy [km2 / s2]")
    ax.set_xscale("log")
    ax.set_xlim(10**-0.4, 10**0.15)
    ax.set_ylim(-700, 0)

    # Generate a Tisserand plotter
    tp = TisserandPlotter(axes=ax, kind=TisserandKind.ENERGY)

    # just check that everything works
    ax = tp.plot_line(Earth, 14 * u.km / u.s, color=color)


# this test only checks whether there is no exception in this code
# see TODO above
#    return fig
