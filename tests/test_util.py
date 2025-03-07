from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
from astropy.time import Time
import numpy as np
import pytest

from boinor.util import norm, time_range


def test_time_range_spacing_num_values():
    start_time = "2017-10-12 00:00:00"
    end_time = "2017-10-12 00:04:00"
    spacing = 1 * u.minute
    num_values = 5

    expected_scale = "utc"
    expected_duration = 4 * u.min

    result_1 = time_range(start_time, spacing=spacing, num_values=num_values)
    result_2 = time_range(start_time, end=end_time, num_values=num_values)
    result_3 = time_range(
        Time(start_time), end=Time(end_time), num_values=num_values
    )

    assert len(result_1) == len(result_2) == len(result_3) == num_values
    assert result_1.scale == result_2.scale == result_3.scale == expected_scale

    assert_quantity_allclose(
        (result_1[-1] - result_1[0]).to(u.s), expected_duration
    )
    assert_quantity_allclose(
        (result_2[-1] - result_2[0]).to(u.s), expected_duration
    )
    assert_quantity_allclose(
        (result_3[-1] - result_3[0]).to(u.s), expected_duration
    )


def test_time_range_requires_keyword_arguments():
    with pytest.raises(TypeError) as excinfo:
        time_range(0, 0)  # type: ignore
    assert (
        "TypeError: time_range() takes 1 positional argument but"
        in excinfo.exconly()
    )


def test_time_range_raises_error_wrong_arguments():
    exception_message = (
        "ValueError: Either 'end' or 'spacing' must be specified"
    )

    with pytest.raises(ValueError) as excinfo_1:
        time_range("2017-10-12 00:00")

    with pytest.raises(ValueError) as excinfo_2:
        time_range("2017-10-12 00:00", spacing=0, end=0, num_values=0)

    assert exception_message in excinfo_1.exconly()
    assert exception_message in excinfo_2.exconly()


def test_norm():
    # this is basically just a test for numpy/numba as the values
    # are just forwarded to the corresponding function
    # values taken from numpy example
    a = np.arange(9 * u.one) - 4
    av = a * u.one
    b = np.array([[1, 2, 3], [-1, 1, 4]])
    bv = b * u.one

    expected_norm = 7.745966692414834
    expected_norm_b0 = [1.41421356, 2.23606798, 5.0]
    expected_norm_b1 = [3.74165739, 4.24264069]

    norm_a = norm(av)
    assert_quantity_allclose(norm_a, expected_norm, atol=1e-10)

    norm_a = norm(av, axis=0)
    assert_quantity_allclose(norm_a, expected_norm, atol=1e-10)

    norm_b = norm(bv, axis=0)
    assert_quantity_allclose(norm_b, expected_norm_b0, atol=1e-10)

    norm_b = norm(bv, axis=1)
    assert_quantity_allclose(norm_b, expected_norm_b1, atol=1e-10)
