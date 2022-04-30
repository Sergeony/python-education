import pytest
from python.unittesting.to_test import sum_all


@pytest.mark.parametrize("items, expected",
                         [([1, 2, 3], 6),
                          ([-1, 0, 1], 0),
                          ([1.1, 1.9], 3.0)])
def test_sum_all(items, expected):
    """ Sum numbers with positive, negative and float values. """
    assert sum_all(*items) == expected


@pytest.mark.parametrize("nan_items",
                         [([1, ""]),
                          ([1, []]),
                          ([1, {}]),
                          ([1, ()])])
def test_sum_all_raises_exception_on_nan_args(nan_items):
    """ Check for exception if some items are Not A Number. """
    with pytest.raises(TypeError):
        sum_all(*nan_items)
