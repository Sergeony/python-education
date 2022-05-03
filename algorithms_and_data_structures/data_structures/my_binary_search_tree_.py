""" My own binary search tree implementation. """


class Node:
    """ An element of a binary search tree. """

    def __init__(self, value: int):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        left_node = self.left_node.value if self.left_node else "_"
        right_node = self.right_node.value if self.right_node else "_"
        return f"{self.value}: {left_node}, {right_node};"


class BinarySearchTree:
    """ A binary search tree """

    def __init__(self):
        self.root = None

    def insert(self, value: int):
        """ Add a new node to the tree with the given value.

        -Adding a root is different from adding other nodes.
        -Do nothing if the value already exists in the tree.
        """
        if self.root is None:
            self.root = Node(value)
            return

        current_node = self.root
        while True:
            if current_node.value < value:
                if current_node.right_node is None:
                    current_node.right_node = Node(value)
                    break
                current_node = current_node.right_node

            elif current_node.value > value:
                if current_node.left_node is None:
                    current_node.left_node = Node(value)
                    break
                current_node = current_node.left_node

            elif current_node.value == value:
                break

    def lookup(self, value: int) -> [Node, None]:
        """ Find the node in the tree.
        """
        current_node = self.root
        while True:
            if current_node is None:
                return None
            if current_node.value > value:
                current_node = current_node.left_node
            elif current_node.value < value:
                current_node = current_node.right_node
            else:
                return current_node

    def delete(self, value: int):
        """ Remove the node from the tree.

        -Removing a root is different from removing other nodes.
        -But anyway, there are 4 main cases:
            1) node to remove has no child nodes
            2) node to remove has only right child node
            3) node to remove has only left child node
            4) node to remove has both child nodes
        """
        del_node, parent_node = self._lookfor_node_to_remove(value)

        if del_node is self.root:
            self._delete_root()
        else:
            self._delete_other(del_node, parent_node)

    def _lookfor_node_to_remove(self, value: int):
        """ Check if node with given value exits
        and return it with its parent.

        -Raise an error, if value is not in tree.
        """
        parent_node = None
        del_node = self.root

        while del_node and del_node.value != value:
            parent_node = del_node
            if del_node.value > value:
                del_node = del_node.left_node
            else:
                del_node = del_node.right_node

        if del_node is None:
            raise ValueError(f"{value} is not in tree")

        return del_node, parent_node

    def _delete_root(self):
        # 1: root has no child nodes
        if self.root.left_node is None and self.root.right_node is None:
            self.root = None
            return

        # 2: root has only right child node
        if self.root.left_node is None and self.root.right_node:
            self.root = self.root.right_node
            return

        # 3: root has only left child node
        if self.root.left_node and self.root.right_node is None:
            self.root = self.root.left_node
            return

        # 4: root has both child nodes
        max_left_parent = self.root
        max_left = self.root.left_node
        while max_left.right_node:
            max_left_parent = max_left
            max_left = max_left.right_node

        self.root.value = max_left.value

        if max_left_parent.value >= max_left.value:
            max_left_parent.left_node = max_left.left_node
        else:
            max_left_parent.right_node = max_left.left_node
        return

    @staticmethod
    def _delete_other(del_node: Node, parent_node: Node):
        # 1: node to remove has no child
        if del_node.left_node is None and del_node.right_node is None:
            if del_node is parent_node.left_node:
                parent_node.left_node = None
            else:
                parent_node.right_node = None
            return

        # 2: node to remove has only right child
        if del_node.left_node is None and del_node.right_node:
            if del_node is parent_node.left_node:
                parent_node.left_node = del_node.right_node
            else:
                parent_node.right_node = del_node.right_node
            return

        # 3: node to remove has only left child
        if del_node.left_node and del_node.right_node is None:
            if del_node is parent_node.left_node:
                parent_node.left_node = del_node.left_node
            else:
                parent_node.right_node = del_node.left_node
            return

        # 4: node to remove has both child nodes
        max_left_parent = del_node
        max_left = del_node.left_node

        while max_left.right_node:
            max_left_parent = max_left
            max_left = max_left.right_node

        del_node.value = max_left.value

        if max_left_parent.value >= max_left.value:
            max_left_parent.left_node = max_left.left_node
        else:
            max_left_parent.right_node = max_left.left_node
        return

    def print_tree(self, node: Node = False, level=0):
        """ Graphical representation of the tree.
        """
        if node is False:
            node = self.root

        if node is not None:
            self.print_tree(node.left_node, level + 1)

            print(' ' * 4 * level + str(node.value), end="")
            if node.right_node and node.left_node:
                print('<')
            elif node.left_node:
                print("/")
            elif node.right_node:
                print("\\")
            else:
                print()

            self.print_tree(node.right_node, level + 1)


def main():
    """ How it works. """

    my_tree = BinarySearchTree()

    my_tree.insert(30)
    my_tree.insert(50)
    my_tree.insert(15)
    my_tree.insert(10)
    my_tree.insert(25)
    my_tree.insert(5)
    my_tree.insert(13)
    my_tree.insert(11)

    my_tree.print_tree()
    print("#" * 30)

    my_tree.delete(15)
    my_tree.delete(13)
    my_tree.delete(10)
    my_tree.delete(11)

    my_tree.print_tree()


if __name__ == "__main__":
    main()
