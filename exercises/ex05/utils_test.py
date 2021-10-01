"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730485647"


def test1_only_evens():
    """Tests if the only_evens function works as expected. A use case."""
    assert only_evens([1, 2, 3]) == [2]
   

def test2_only_evens():
    """Tests if the only_evens function works as expected. Another use case."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test3_only_evens():
    """Tests if the only_evens function works as expected. An edge case."""
    assert only_evens([]) == []


def test_sub():
    """Tests if the sub function works as expected. A use case."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]
   

def test2_sub():
    """Tests if the sub function works as expected. Another use case."""
    assert sub([10, 20, 30, 40], 1, 2) == [20]


def test3_sub():
    """Tests if the sub function works as expected. An edge case."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test1_concat():
    """Tests if the concat function works as expected. A use case."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
   

def test2_concat():
    """Tests if the concat function works as expected. Another use case."""
    assert concat([4, 1], [3, 5]) == [4, 1, 3, 5]


def test3_concat():
    """Tests if the concat function works as expected. An edge case."""
    assert concat([1, 2, 3, 4], []) == [1, 2, 3, 4]
