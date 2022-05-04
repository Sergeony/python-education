import pytest
from random import randint
from algorithms_and_data_structures.algorithms.quick_sort import quick_sort


@pytest.fixture
def rand_list():
    size = randint(1, 100)
    return [randint(-100, 100) for i in range(size)]


def test_quick_sort(rand_list):
    for i in range(5):
        assert quick_sort(rand_list) == sorted(rand_list)
