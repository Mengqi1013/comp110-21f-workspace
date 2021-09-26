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
    if counter == len(a) or counter == len(b):
        return True
    return False


def max(input: list[int]) -> int:
    """Return the biggest integer in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    while i < len(input) - 1:
        bigger_value = 0
        left_item: int = int(input[i])
        right_item: int = int(input[i + 1])
        if int(input[i]) >= int(input[i + 1]):
            bigger_value = left_item
        else:
            bigger_value = right_item
        i += 1
    return bigger_value
    
