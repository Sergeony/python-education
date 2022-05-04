import pytest
from algorithms_and_data_structures.data_structures.my_stack import Stack


@pytest.fixture
def example_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(5)
    return stack


@pytest.mark.parametrize("value", [0, 9, 4])
def test_push(example_stack, value):
    example_stack.push(value)
    assert example_stack.peek() == value


@pytest.mark.parametrize("expected", [2])
def test_pop(example_stack, expected):
    example_stack.pop()
    assert example_stack.peek() == expected

