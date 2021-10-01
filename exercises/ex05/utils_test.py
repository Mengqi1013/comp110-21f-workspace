"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730485647"


def test_only_evens():
    """Tests if the only_evens function works as expected."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([1, 5, 3]) == []
    assert only_evens([4, 4, 4]) == [4]


def test_sub():
    """Tests if the sub function works as expected."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]
    assert sub([1, 4, 8, 2], 0, 3) == [1, 4, 8]
    assert sub([14, 18, 54, 13, 12, 65, 15], 2, 6) == [54, 13, 12, 65]


def test_concat():
    """Tests if the concat function works as expected."""
    assert concat([], []) == []
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert concat([4, 1], [3, 5]) == [4, 1, 3, 5]