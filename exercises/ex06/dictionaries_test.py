"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730485647"


def test1_invert():
    """Tests if the invert function works as expected. A use case."""
    assert invert({'a': 'x', 'b': 'y', 'c': 'z'}) == {'x': 'a', 'y': 'b', 'z': 'c'}


def test2_invert():
    """Tests if the invert function works as expected. Another use case."""
    assert invert({'S': 'small', 'M': 'medium', 'L': 'large'}) == {'small': 'S', 'medium': 'M', 'large': 'L'}


def test3_invert():
    """Tests if the invert function works as expected. An edge case."""
    assert invert({}) == {}


def test1_favorite_color():
    """Tests if the favorite_color function works as expected. A use case."""
    assert favorite_color({'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}) == "blue"


def test2_favorite_color():
    """Tests if the favorite_color function works as expected. Another use case."""
    assert favorite_color({'Mandy': 'blue', 'Bob': 'red', 'John': 'yellow', 'George': 'blue'}) == "blue"


def test3_favorite_color():
    """Tests if the favorite_color function works as expected. An edge case."""
    assert favorite_color({'Kris': 'green'}) == "green"


def test1_count():
    """Tests if the count function works as expected. A use case."""
    assert count(['small', 'large', 'small', 'large', 'large', 'small', 'large', 'large', 'large', 'small']) == {'small': 4, 'large': 6}


def test2_count():
    """Tests if the count function works as expected. Another use case."""
    assert count(['up', 'down', 'left', 'right']) == {'up': 1, 'down': 1, 'left': 1, 'right': 1}


def test3_count():
    """Tests if the count function works as expected. An edge case."""
    assert count([]) == {}
