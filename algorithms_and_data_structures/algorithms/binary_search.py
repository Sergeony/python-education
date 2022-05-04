""" Iterative binary search implementation. """


def binary_search(collection: list, value: int or float) -> int:
    """ The algorithm to find a value in a list in logN operations.

    -It is useful only for sorted collections.
    -Raise an error, if value is not in list.
    """
    left_bound = 0
    right_bound = len(collection) - 1

    while left_bound <= right_bound:
        center = (left_bound + right_bound) // 2
        if value < collection[center]:
            right_bound = center - 1
        elif value > collection[center]:
            left_bound = center + 1
        else:
            return center

    raise ValueError(f"{value} is not in list")
