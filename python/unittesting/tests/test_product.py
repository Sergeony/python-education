import pytest
from python.unittesting.to_test import Product


@pytest.fixture
def example_product():
    """ Create Product instance with parameters. """
    return Product("phone", 1000, 2)


@pytest.mark.parametrize("added, expected",
                         [(1, 3),
                          (0, 2),
                          (-1, 1),
                          (-3, -1)])
def test_add_quantity(example_product, added, expected):
    """ Add positive and negative number of quantity. """
    example_product.add_quantity(added)
    assert example_product.quantity == expected


@pytest.mark.parametrize("subtracted, expected",
                         [(2, 0),
                          (1, 1),
                          (3, -1),
                          (-1, 3)])
def test_subtract_quantity(example_product, subtracted, expected):
    """ Subtract positive and negative number of quantity. """
    example_product.subtract_quantity(subtracted)
    assert example_product.quantity == expected


@pytest.mark.parametrize("new_price, expected",
                         [(2000, 2000),
                          (1500.1, 1500.1),
                          (-2000, -2000)])
def test_change_price(example_product, new_price, expected):
    """ Change the price to positive and negative value. """
    example_product.change_price(new_price)
    assert example_product.price == expected
