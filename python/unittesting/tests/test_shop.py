import pytest
from python.unittesting.to_test import Product
from python.unittesting.to_test import Shop


@pytest.fixture
def example_empty_shop():
    return Shop()


@pytest.fixture
def example_shop():
    return Shop([
        Product("phone", 1000),
        Product("laptop", 2000, 2),
        Product("tablet", 800),
    ])


@pytest.mark.parametrize("product_to_add",
                         [Product("iPhone", 100000000),
                          Product("nokia", 1)])
def test_add_product(example_empty_shop, product_to_add):
    example_empty_shop.add_product(product_to_add)
    assert product_to_add in example_empty_shop.products


@pytest.mark.parametrize("product_title, expected_index",
                         [("phone", 0),
                          ("laptop", 1),
                          ("tablet", 2),
                          ("sofa", None)])
def test__get_product_index(example_shop, product_title, expected_index):
    assert example_shop._get_product_index(product_title) == expected_index


@pytest.mark.parametrize("product_title, qty_to_sell, expected_receipt",
                         [("phone", 1, 1000),
                          ("laptop", 1, 2000),
                          ("tablet", 1, 800)])
def test_sell_product(example_shop, product_title, qty_to_sell, expected_receipt):
    assert example_shop.sell_product(product_title, qty_to_sell) == expected_receipt


@pytest.mark.parametrize("product_title, qty_to_sell",
                         [("phone", 2),
                          ("laptop", 3),
                          ("tablet", 2)])
def test_sell_product_exception_on_value_error(example_shop, product_title, qty_to_sell):
    with pytest.raises(ValueError):
        example_shop.sell_product(product_title, qty_to_sell)
