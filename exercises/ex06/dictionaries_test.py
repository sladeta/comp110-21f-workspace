"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730236019"


def test_invert_01() -> None:
    """Tests for inverts."""
    test_dict: dict[str, str] = [{'a': 'z', 'b': 'y', 'c': 'x'}]
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_02() -> None:
    """Test for empty dict."""
    test_dict: dict[str, str] = [{}]
    assert invert(test_dict) == {}


def test_invert_03() -> None:
    """Tests for short dict."""
    test_dict: dict[str, str] = [{'thomas': 'slade'}]
    assert invert(test_dict) == {'slade': 'thomas'}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_01() -> None:
    """Tests for dict with no repeated colors."""
    test_dict: dict[str, str] = [{'grace': 'pink', 'thomas': 'blue', 'chris': 'green'}]
    assert favorite_color(test_dict) == {'pink'}


def test_favorite_color_02() -> None:
    """Tests for favorite colors."""
    test_dict: dict[str, str] = [{'grace': 'pink', 'thomas': 'blue', 'chris': 'blue'}]
    assert favorite_color(test_dict) == {'blue'}


def test_favorite_color_03() -> None:
    """Tests for many colors."""
    test_dict: dict[str, str] = [{'grace': 'pink', 'thomas': 'blue', 'chris': 'blue', 'christian': 'green', 'mary': 'yellow'}]
    assert favorite_color(test_dict) == [{'blue'}]


def test_count_01() -> None:
    """Tests count for recurring strings."""
    test_list: list[str] = ['car', 'pig', 'cat', 'car']
    assert count(test_list) == [{'car': 2, 'pig': 1, 'cat': 1}]


def test_count_02() -> None:
    """Tests count for non-recurring strings."""
    test_list: list[str] = ['car', 'pig', 'cat']
    assert count(test_list) == [{'car': 1, 'pig': 1, 'cat': 1}]


def test_count_03() -> None:
    """Test with an empty list."""
    test_list: list[str] = []
    assert count(test_list) == [{}]