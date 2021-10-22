"""Practice with dictionaries."""

__author__ = "730236019"


def invert(first_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    invert_dict: dict[str, str] = {}
    for key in first_dict:
        if first_dict[key] in invert_dict:
            raise KeyError("Keys cannot be identical.")
        invert_dict[first_dict[key]] = key
    return invert_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns the most repeated color within a dictionary."""
    repeat_color: str = ""
    i: int = 0
    new_dict: dict[str, int] = {}
    for name in color:
        new_dict[color[name]] = 1
    for name in color:
        if color[name] in new_dict:
            new_dict[color[name]] += 1
            repeat_color = color[name]
    for name in new_dict:
        if new_dict[name] > i:
            i = new_dict[name]
            repeat_color = name
    return repeat_color


def count(x: list[str]) -> dict[str, int]:
    """Counts the number of times every string in a list is given."""
    result: dict[str, int] = {}
    for string in x:
        result[string] = 0
    for string in x:
        if string in result:
            result[string] += 1
    return result