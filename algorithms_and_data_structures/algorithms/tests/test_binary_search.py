import pytest
from algorithms_and_data_structures.algorithms.binary_search import binary_search


@pytest.mark.parametrize("search_value, sorted_list", [(3, [1, 3, 5, 7]),
                                                       (-2, [-2, 4, 8, 10]),
                                                       (11, [4, 6, 11]),
                                                       (-13, [-13, -2, 11])])
def test_binary_search(sorted_list: list, search_value):
    assert binary_search(sorted_list, search_value) == sorted_list.index(search_value)


@pytest.mark.parametrize("miss_value, sorted_list", [(1, []),
                                                     (2, [1]),
                                                     (3, [1, 2, 4])])
def test_binary_search_raises_on_does_not_exit_value(miss_value, sorted_list):
    with pytest.raises(ValueError):
        binary_search(sorted_list, miss_value)
