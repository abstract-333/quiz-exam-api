from src.cal import Calculator
import pytest
from contextlib import nullcontext as does_not_raise


class TestCalculator:

    @pytest.mark.parametrize(
        argnames="x, y, res, expectation",
        argvalues=[
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, -5, pytest.raises(ZeroDivisionError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        argnames="x, y, res, expectation",
        argvalues=[
            (-5.0, 2.0, int(-3), does_not_raise()),
            (5, "None", 4, pytest.raises(TypeError)),

        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res
