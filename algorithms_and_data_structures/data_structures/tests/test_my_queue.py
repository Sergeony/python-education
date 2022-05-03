import pytest
from algorithms_and_data_structures.data_structures.my_queue import Queue


@pytest.fixture
def example_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(5)
    return queue


@pytest.mark.parametrize("value", [0, 3, 7])
def test_enqueue(example_queue, value):
    example_queue.enqueue(value)
    assert example_queue.tail.value == value


@pytest.mark.parametrize("expected", [2])
def test_dequeue(example_queue, expected):
    example_queue.dequeue()
    assert example_queue.peek() == expected
