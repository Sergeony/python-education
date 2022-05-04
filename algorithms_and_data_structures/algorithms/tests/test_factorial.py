import pytest
from math import factorial
from algorithms_and_data_structures.algorithms.factorial import factorial as my_fac


@pytest.mark.parametrize("value", [0, 1, 2, 4, 5, 10, 30, 65, 90])
def test_factorial(value):
    assert my_fac(value) == factorial(value)


@pytest.mark.parametrize("neg_value", [-1, -2, -3, -50])
def test_factorial_raises_on_negative(neg_value):
    with pytest.raises(ValueError):
        my_fac(neg_value)


@pytest.mark.parametrize("nan_value", ["", [], {}, .0, ()])
def test_factorial_raises_on_nan(nan_value):
    with pytest.raises(TypeError):
        my_fac(nan_value)
