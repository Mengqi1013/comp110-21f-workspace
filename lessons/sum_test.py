"""Test for the sum function."""

__author__ = "730485647"

from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0 


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_item() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_many_items_again() -> None:
    xs: list[float] = [-1.0, 1.0, -2.0, 2.0]
    assert sum(xs) == 0