import pytest
from algorithms_and_data_structures.data_structures.my_binary_search_tree_ import BinarySearchTree


@pytest.fixture
def example_tree():
    tree = BinarySearchTree()
    tree.insert(30)
    tree.insert(50)
    tree.insert(15)
    tree.insert(10)
    tree.insert(25)
    tree.insert(5)
    tree.insert(27)
    tree.insert(60)
    tree.insert(40)
    tree.insert(45)
    tree.insert(55)
    return tree


@pytest.mark.parametrize("value", [30, 50, 15, 10, 25, 5, 27, 60, 40, 45, 55])
def test_delete(example_tree, value):
    example_tree.delete(value)
    assert example_tree.lookup(value) is None


@pytest.mark.parametrize("value", [2, 3, 4, 5])
def test_insert(example_tree, value):
    example_tree.insert(value)
    assert example_tree.lookup(value).value == value

