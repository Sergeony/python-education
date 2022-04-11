"""Calculator

This module is designed to calculate simple mathematical operations.
Calculater - class with mathematical methods.
"""

class Calculater:
    """A class to calculate numbers.

    It's intended to do 4 operations: add, subtract, multiply, divide.
    All methods expect 2 numbers to calculate.
    """

    @staticmethod
    def add(term_1: float, term_2: float) -> float:
        """Add 2 numbers and return their sum."""
        return term_1 + term_2

    @staticmethod
    def subtract(minuend: float, subtrahend: float) -> float:
        """Subtract 2 numbers and return their difference."""
        return minuend - subtrahend

    @staticmethod
    def multiply(multiplicand: float, multiplier: float) -> float:
        """Multipy 2 numbers and return their product."""
        return multiplicand * multiplier

    @staticmethod
    def divide(dividend: float, divisor: float) -> float:
        """Divide 2 numbers and return their quotient.
        The divisor must be different from 0 otherwise an error will occur."""
        return dividend / divisor
