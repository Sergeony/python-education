import pytest
from algorithms_and_data_structures.data_structures.my_linked_list import LinkedList


@pytest.fixture
def example_empty_linked_list():
    return LinkedList()


@pytest.fixture
def example_linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(5)
    return linked_list


@pytest.mark.parametrize("value", [1, 2, 5, 2])
def test_append(example_empty_linked_list, example_linked_list, value):
    example_empty_linked_list.append(value)
    assert example_empty_linked_list.tail.value == value
    example_linked_list.append(value)
    assert example_linked_list.tail.value == value


@pytest.mark.parametrize("value", [1, 2, 5, 2])
def test_prepend(example_empty_linked_list, example_linked_list, value):
    example_empty_linked_list.prepend(value)
    assert example_empty_linked_list.head.value == value
    example_linked_list.prepend(value)
    assert example_linked_list.head.value == value


@pytest.mark.parametrize("pos, value", [(0, 3),
                                        (3, "last"),
                                        (1, 0)])
def test_insert(example_linked_list, pos, value):
    example_linked_list.insert(pos, value)
    assert example_linked_list.lookup(value) == pos


def test_insert_on_raises_exception_on_out_of_range(example_empty_linked_list):
    with pytest.raises(IndexError):
        example_empty_linked_list.insert(1, 2)


@pytest.mark.parametrize("pos, expected", [(0, [2, 5]),
                                           (1, [1, 5]),
                                           (2, [1, 2])])
def test_delete(example_linked_list, pos, expected):
    example_linked_list.delete(pos)
    assert [node.value for node in example_linked_list] == expected
