""" Recursive factorial implementation. """


def factorial(value: int) -> int:
    """ Multiply all natural numbers up to this one.

    -Raise an error, if value is not an integer or is a negative.
    """
    if not isinstance(value, int):
        raise TypeError(f"'{type(value)}' object cannot be interpreted as an integer")
    if value < 0:
        raise ValueError("factorial() not defined for negative values")
    if value < 2:
        return 1
    return value * factorial(value - 1)
