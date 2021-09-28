"""List utility functions."""

__author__ = "730485647"


# TODO: Implement your functions here.
def all(my_list: list[int], number: int) -> bool:
    """Return True if an input value is found, false otherwise."""
    i: int = 0
    while i < len(my_list):
        item: int = my_list[i]
        if item == number:
            return True
        i += 1

    return False


def is_equal(a: list[int], b: list[int]) -> bool:
    """Return True if two lists are equal, false otherwise."""
    i: int = 0
    j: int = 0
    counter: int = 0
    while i < len(a) and j < len(b):
        a_item: int = a[i]
        b_item: int = b[j]
        if a_item == b_item:
            counter = counter + 1
        i += 1
        j += 1
    if counter == len(a) or counter == len(b) - 1 and counter != 0:
        return True
    return False


def max(input: list[int]) -> int:
    """Return the biggest integer in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = input[0]
    while i < len(input):
        if input[i] >= max:
            max = input[i]
        i += 1
    return max
    
