import pytest
from python.unittesting.to_test import even_odd


@pytest.mark.parametrize("number_to_check, expected",
                         [(0, "even"),
                          (2, "even"),
                          (-2, "even"),
                          (1, "odd"),
                          (-1, "odd"),
                          (2.1, "odd")])
def test_even_odd(number_to_check, expected):
    """ Check if the number is for positive, negative and float values. """
    assert even_odd(number_to_check) == expected


@pytest.mark.parametrize("nan", ["", {}, [], ()])
def test_even_odd_raises_exception_on_nan_args(nan):
    """ Check for exception if the number is Not A Number. """
    with pytest.raises(TypeError):
        even_odd(nan)
