""" My own singly linked list implementation. """


class Node:
    """ An element of a singly linked list and its derivatives. """

    def __init__(self, value: any, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        value = "'" + self.value + "'" if isinstance(self.value, str) else self.value
        return f"{value}"


class LinkedListIterator:
    """ Makes linked lists possible to iterate. """

    def __init__(self, current_node):
        self.current_node = current_node

    def __iter__(self):
        return self

    def __next__(self):
        node = self.current_node
        if node is None:
            raise StopIteration
        self.current_node = self.current_node.next_node
        return node


class LinkedList:
    """ A basic singly linked list. """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: any):
        """ Add a new node to the end of the list.

        -Assign a new node to the tail.
        -Also, assign it to the head, if it's the first time.
        """
        if self.tail is None:
            self.tail = Node(value)
            self.head = self.tail
            return

        self.tail.next_node = Node(value)
        self.tail = self.tail.next_node

    def prepend(self, value: any):
        """ Add a new node to the top of the list.

        -Assign a new node to the head.
        -Also, assign it to the tail, if it's the first time.
        """
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head

    def insert(self, pos: int, value: any):
        """ Add a new node to the list.

        -Raise an error, if pos of a node to be added is out of range.
        -Prepend, if it is the first one.
        -Otherwise, go to the element preceding the given pos and
        add a new node by moving the current one to the right.
        -Also, assign a new node to the tail, if it is the last one.
        """
        if pos == 0:
            self.prepend(value)
            return

        for i, node in enumerate(self):
            if i == pos - 1:
                node.next_node = Node(value, node.next_node)
                if node.next_node.next_node is None:
                    self.tail = node.next_node
                return

        raise IndexError("linked list index out or range")

    def delete(self, pos: int) -> any:
        """ Remove a node from the list.

        -Raise an error, if pos is out of range.
        -Assign the next node to the head, if the node to be removed is the first one.
        -Otherwise, move to the node preceding the given pos and
        remove its next_node by replacing it with next_node of the node to be removed.
        -Assign the prev node to the tail, if the node to be removed is the last one.
        """
        if pos == 0:
            if self.head is None:
                raise IndexError("linked list index out or range")

            temp = self.head.value
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return temp

        for i, node in enumerate(self):
            if node is self.tail:
                raise IndexError("linked list index out or range")

            if i == pos - 1:
                temp = node.next_node.value
                node.next_node = node.next_node.next_node
                if node.next_node is None:
                    self.tail = node
                return temp

    def lookup(self, value: any) -> [int, None]:
        """ Walk through the entire list and
        get pos of the first node with the given value.
        """
        for i, node in enumerate(self):
            if node.value == value:
                return i
        return None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __str__(self):
        string = "["
        for node in self:
            value = "'" + node.value + "'" if isinstance(node.value, str) else node.value
            string += f"{value}"
            if node is not self.tail:
                string += ", "
        return string + "]"


def main():
    """ How it works. """

    my_list = LinkedList()
    print(my_list)
    print("#" * 10)

    my_list.append(2)
    my_list.append(4)
    print(my_list)
    print("#" * 10)

    my_list.prepend(0)
    my_list.prepend(-2)
    print(my_list)
    print("#" * 10)

    my_list.delete(0)
    my_list.delete(2)
    my_list.delete(1)
    print(my_list)
    print("#" * 10)

    my_list.insert(0, 2)
    my_list.insert(1, "inserted to 1")
    my_list.insert(3, "inserted to 3")
    print(my_list)
    print("#" * 10)

    print(my_list.lookup(2))


if __name__ == "__main__":
    main()
