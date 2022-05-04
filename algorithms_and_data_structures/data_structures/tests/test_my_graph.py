import pytest
from algorithms_and_data_structures.data_structures.my_graph import Graph


@pytest.fixture
def example_graph():
    graph = Graph()
    graph.insert(1, [])
    graph.insert(2, [1])
    graph.insert(3, [2, 1])
    graph.insert(4, [2, 3])
    return graph


@pytest.mark.parametrize("value, relations", [(5, [1, 3]),
                                              (7, [2, 4]),
                                              (9, [3, 4])])
def test_insert(example_graph, value, relations):
    example_graph.insert(value, [])

    new_vertex = example_graph.lookup(value)

    for edge in new_vertex.edges:
        assert edge.value.value in relations


@pytest.mark.parametrize("value", [1, 2, 3, 4])
def test_delete(example_graph, value):
    example_graph.delete(value)

    assert example_graph.lookup(value) is None

    for vertex in example_graph.vertices:
        for edge in vertex.value.edges:
            assert edge.value.value != value
