""" My own hash table implementation. """
from algorithms_and_data_structures.data_structures.my_linked_list import LinkedList


class HashTable:
    """ A hash table, based on a tuple and singly linked lists. """

    def __init__(self, size=30):
        self._size = size
        self.hashes = tuple(LinkedList() for _ in range(size))

    def _get_hash(self, key: str) -> int:
        """ Calculate the hash of the key like this:
                1) Add all the key character codes.
                2) Find the remainder after dividing sum by the size of the table.
        """
        return sum(ord(char) for char in key) % self._size

    def insert(self, key: str, value: any):
        """ Add a new item to the table.

        -Add a new node to the end of the list of keys with the same hashes
        as the hash of the given key, if there is no such key.
        -Otherwise, update the existing key with the new value.
        -Note that the hash table stores keys as the node values, and
        values as the second node values.
        """
        key_hash = self._get_hash(key)

        if self.hashes[key_hash].lookup(key) is None:
            self.hashes[key_hash].append(key)
            self.hashes[key_hash].tail.second_value = value
        else:
            for node in self.hashes[key_hash]:
                if node.value == key:
                    node.second_value = value

    def delete(self, key: str):
        """ Remove a node from the list of keys with the same hashes
        as the hash of the given key.
        """
        nodes = self.hashes[self._get_hash(key)]

        for i, node in enumerate(nodes):
            if node.value == key:
                nodes.delete(i)

    def lookup(self, key: str) -> [any, None]:
        """ Find value of the node from the list with the same hashes
        as the hash of the given key and return it.
        """
        nodes = self.hashes[self._get_hash(key)]

        for node in nodes:
            if node.value == key:
                return node.second_value
        return None

    def __str__(self):
        string = "{"
        for key_hash in self.hashes:
            for key in key_hash:
                string += str(key) + ": " + str(key.second_value) + ", "
        return string + "}"


def main():
    """ How it works. """

    my_table = HashTable()
    print(my_table)
    print("#" * 10)

    my_table.insert("a", 12)
    my_table.insert("C", 10)
    my_table.insert("b", 10)
    print(my_table)
    print("#" * 10)

    my_table.delete("C")
    my_table.delete("a")
    print(my_table)
    print("#" * 10)

    print(my_table.lookup("b"))


if __name__ == "__main__":
    main()
