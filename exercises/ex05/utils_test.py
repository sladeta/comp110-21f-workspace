"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_sub_01() -> None:
    test_list: list[int] = [10, 20]
    assert sub(test_list, 1, 2) == [20]


def test_sub_02() -> None:
    test_list: list[int] = [10, 20, 30]
    assert sub(test_list, 0, 1) == [10]


def test_sub_03() -> None:
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, 0, 4) == [10, 20, 30, 40]