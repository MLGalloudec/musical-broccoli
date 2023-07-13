"""
This module provides a function to assist with the collatz sequence

Functions:
    get_next(int) -> int
"""

def get_next(num: int) -> int:
    """
    A function to which returns the next number in the collatz sequence.

    Args:
        num: The number to find the next value in the collatz sequence after

    Returns:
        The next number in the collatz sequence

    Raises:
        No error criteria implemented yet

    TODO:
        Implement error raising
    """
    if num%2 == 0:
        return int(num/2)
    return int(3*num + 1)