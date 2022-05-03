""" My own queue realisation. """
from algorithms_and_data_structures.data_structures.my_linked_list import LinkedList


class Queue(LinkedList):
    """ A queue, based on a singly linked list. """

    def enqueue(self, value: any):
        """ Add a node to the end of the queue. """
        super().append(value)

    def dequeue(self) -> any:
        """ Remove a node from the top of the queue. """
        return super().delete(0)

    def peek(self) -> any:
        """ Get a node from the top of the queue. """
        return self.head.value if self.head else None


def main():
    """ How it works. """

    my_queue = Queue()
    print(my_queue)
    print("#" * 10)

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(1.2)
    print(my_queue)
    print("#" * 10)

    my_queue.dequeue()
    my_queue.dequeue()
    print(my_queue)
    print("#" * 10)

    print(my_queue.peek())


if __name__ == "__main__":
    main()
