"""List utility functions part 2."""

__author__ = "730236019"


def only_evens(x: list[int]) -> list[int]:
    """Returns only even numbers within a list."""
    even_list: list[int] = list()
    i: int = 0
    list_len: int = len(x)
    while i < list_len: 
        if x[i] % 2 == 0:
            even_list.append(x[i])
        i += 1
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns a sub list based on 2 index points."""
    subset: list[int] = list()
    list_len: int = len(input)
    if list_len == 0 or start > list_len or end <= 0:
        return subset
    if end > list_len:
        end = list_len
    if start < 0:
        start = 0
    while start < end:
        subset.append(input[start])
        start += 1
    return subset


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concatenates two lists together."""
    i: int = 0
    len_x: int = len(x)
    len_y: int = len(y)
    answer: list[int] = list()
    while i < len_x: 
        answer.append(x[i])
        i += 1
    h: int = 0
    while h < len_y:
        answer.append(y[h])
        h += 1
    return answer