import pytest

from boinor.plotting.orbit.backends._base import OrbitPlotterBackend


def test_orbit_backends_base():
    dummyScene = 1
    wrongName = "nothing"
    with pytest.raises(
        ValueError, match="Backend name must end with '2D' or '3D'."
    ):
        opb = OrbitPlotterBackend(dummyScene, wrongName)

    goodName = "Matplotlib2D"
    opb = OrbitPlotterBackend(dummyScene, goodName)
    assert opb.is_3D is False

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb._get_colors(
            "0x000000", False
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_marker(
            1, color=2, label=3, marker_symbol=4, size=5
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_position(
            1, color=2, label=3, size=4
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_impulse(
            1, color=2, label=3, size=4
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_sphere(
            1, color=2, label=3, radius=4
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.undraw_attractor()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.draw_coordinates(
            1, colors=2, label=3, size=4
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.draw_axes_labels_with_length_scale_units(
            1
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.update_legend()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.resize_limits()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.generate_labels(
            1, 2, 3
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.show()
