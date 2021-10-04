"""List utility functions."""

__author__ = "730236019"


def all(x: list[int], y: int) -> bool:
    """Determines whether an integer is repeated in a list."""
    i: int = 0 
    list_len: int = len(x)
    if list_len == 0:
        return False
    while i < list_len - 1:
        if y == x[i]:
            i += 1
        else:
            return False
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Determines whether two lists are the same."""
    i: int = 0
    len_x: int = len(x)
    len_y: int = len(y)
    if len_x != len_y:
        return False
    while i < len_x: 
        if x[i] == y[i]:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the integer within a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        x: int = 0
        while i < len(input) - 1:
            if input[i] >= input[i + 1]:
                x = input[i]
            else:
                x = input[i + 1]
            i += 1
        return x
