""" My own graph implementation. """
from algorithms_and_data_structures.data_structures.my_linked_list import LinkedList


class Vertex:
    """ An element of a graph. """

    def __init__(self, value: any):
        self.value = value
        self.edges = LinkedList()

    def add_edge(self, edge):
        """ Add an edge to the edge list.
        """
        self.edges.append(edge)

    def del_edges(self):
        """ Remove myself from the edge list of my edges.
        """
        for edge in self.edges:
            for i, his_edge in enumerate(edge.value.edges):
                if his_edge.value.value == self.value:
                    edge.value.edges.delete(i)

    def __str__(self):
        string = f"{self.value}: " + "{"
        for edge in self.edges:
            string += str(edge.value.value)
            if edge is not self.edges.tail:
                string += ", "
        return string + "}"


class Graph:
    """ Graph, like linked list with liked lists as self vertices. """

    def __init__(self):
        self.vertices = LinkedList()

    def insert(self, value: any, edges_values: list):
        """ Add a new vertex to the graph.

        -Do nothing, if a vertex with the given value already exits.
        -Add a vertex to other vertices whose values are indicated in edges_values.
        """
        for vertex in self.vertices:
            if vertex.value.value == value:
                return

        new_vertex = Vertex(value)
        for vertex in self.vertices:
            if vertex.value.value in edges_values:
                new_vertex.add_edge(vertex.value)
                vertex.value.add_edge(new_vertex)
        self.vertices.append(new_vertex)

    def delete(self, value: any):
        """ Remove the vertex with the given value from the graph
        and from other vertices that have an edge with it.
        """
        for i, vertex in enumerate(self.vertices):
            if vertex.value.value == value:
                self.vertices.delete(i)
                vertex.value.del_edges()

    def lookup(self, value: any) -> [Vertex, None]:
        """ Walk through all vertexes and
        get the first one with the given value.
        """
        for vertex in self.vertices:
            if vertex.value.value == value:
                return vertex.value
        return None

    def __str__(self):
        string = "["
        for vertex in self.vertices:
            string += str(vertex.value)
            if vertex is not self.vertices.tail:
                string += "; "
        return string + "]"


def main():
    """ How it works. """

    my_graph = Graph()
    print(my_graph)
    print("#" * 10)

    my_graph.insert(1, [])
    my_graph.insert(2, [])
    my_graph.insert(3, [1, 2])
    print(my_graph)
    print("#" * 10)

    my_graph.delete(3)
    my_graph.delete(1)
    print(my_graph)
    print("#" * 10)

    print(my_graph.lookup(2))


if __name__ == "__main__":
    main()
