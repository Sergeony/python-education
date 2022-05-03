import pytest
from algorithms_and_data_structures.data_structures.my_hash_table import HashTable


@pytest.fixture
def example_table():
    table = HashTable()
    table.insert("a", 1)
    table.insert("C", 2)
    table.insert("b", 5)
    return table


@pytest.mark.parametrize("key, value", [("abc", 12,),
                                        ("dsfsdf", 23),
                                        ("a", 10)])
def test_insert(example_table, key, value):
    example_table.insert(key, value)
    assert example_table.lookup(key) == value


@pytest.mark.parametrize("key", ["a", "C", "b"])
def test_delete(example_table, key):
    example_table.delete(key)
    assert example_table.lookup(key) is None
