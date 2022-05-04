""" Iterative quick sort implementation. """
from algorithms_and_data_structures.data_structures.my_stack import Stack


def quick_sort(collection: list) -> list:
    """ Algorithm for sorting a number list on average over NlogN operations.

    -unsorted_range is a stack with left and right bounds of the list,
    where the list is not yet sorted.
    -Steps of sorting:
        1) appoint center in bounds as pivot, and pointers as left bound and right bound
        2) compare items on the left side with items on the right side, swap them in sort order
        3) push to unsorted_range the greater range, after comparison
        4) decrement current range with changed pointers, after comparison
    """
    unsorted_range = Stack()
    unsorted_range.push(0)
    unsorted_range.push(len(collection) - 1)

    while unsorted_range.peek():
        right_bound, left_bound = unsorted_range.pop(), unsorted_range.pop()

        while left_bound < right_bound:
            # step 1:
            center = (right_bound + left_bound) // 2
            pivot = collection[center]
            i = left_bound
            j = right_bound

            # step 2:
            while i <= j:
                while collection[i] < pivot:
                    i += 1
                while collection[j] > pivot:
                    j -= 1

                if i <= j:
                    collection[i], collection[j] = collection[j], collection[i]
                    i += 1
                    j -= 1

            # step 3 and 4:
            if i < center:
                if i < right_bound:
                    unsorted_range.push(i)
                    unsorted_range.push(right_bound)
                right_bound = j
            else:
                if j > left_bound:
                    unsorted_range.push(left_bound)
                    unsorted_range.push(j)
                left_bound = i

    return collection
