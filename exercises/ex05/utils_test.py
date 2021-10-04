"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730236019"


def test_only_evens_01() -> None:
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_only_evens_02() -> None:
    test_list: list[int] = [0, 2, 4]
    assert only_evens(test_list) == [0, 2, 4]


def test_only_evens_03() -> None:
    test_list: list[int] = [3, 5, 7]
    assert only_evens(test_list) == []


def test_sub_01() -> None:
    test_list: list[int] = [10, 20]
    assert sub(test_list, 1, 2) == [20]


def test_sub_02() -> None:
    test_list: list[int] = [10, 20, 30]
    assert sub(test_list, 0, 1) == [10]


def test_sub_03() -> None:
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, 0, 4) == [10, 20, 30, 40]


def test_concat_01() -> None:
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_02() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_03() -> None:
    x: list[int] = []
    y: list[int] = [6, 9]
    assert concat(x, y) == [6, 9]
