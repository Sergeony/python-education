""" My own stack implementation. """
from data_structures.my_linked_list import LinkedList


class Stack(LinkedList):
    """ A stack, based on a singly linked list. """

    def push(self, value: any):
        """ Add a node to the top of the stack. """
        super().prepend(value)

    def pop(self) -> any:
        """ Remove a node from the top of the stack. """
        return super().delete(0)

    def peek(self) -> any:
        """ Get a node from the top of the stack """
        return self.head.value if self.head else None


def main():
    """ How it works. """

    my_stack = Stack()
    print(my_stack)
    print("#" * 10)

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(5)
    print(my_stack)
    print("#" * 10)

    my_stack.pop()
    my_stack.pop()
    print(my_stack)
    print("#" * 10)

    print(my_stack.peek())


if __name__ == "__main__":
    main()
