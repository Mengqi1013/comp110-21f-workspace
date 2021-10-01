"""List utility functions part 2."""

__author__ = "730485647"


# Define your functions below
def only_evens(xs: list[int]) -> list[int]:
    """Returns the even elements in a list."""
    i: int = 0
    string: str = ""
    new_list: list[int] = []
    while i < len(xs): 
        if xs[i] % 2 == 0:
            string = str(xs[i])
            new_list.append(int(string))
        i = i + 1
    return new_list


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Returns a subset of the given list based on the starting and ending indexes."""
    new_list: list[int] = []
    if a < 0:
        a = a + len(xs)
    if a == len(xs):
        new_list = []
        return new_list
    if b < 0:
        b = b + len(xs)
    if b > len(xs):
        b = len((xs)) - 1
    if len(xs) == 0:
        new_list = []
        return new_list
    i: int = a
    string: str = ""
    while i < b:
        string = str(xs[i])
        new_list.append(int(string))
        i = i + 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates two lists given and returns a new list."""
    i: int = 0 
    j: int = 0
    string1: str = ""
    string2: str = ""
    new_list: list[int] = []
    while i < len(xs):
        string1 = str(xs[i])
        new_list.append(int(string1))
        i = i + 1
    while j < len(ys):
        string2 = str(ys[j])
        new_list.append(int(string2))
        j = j + 1   
    return new_list


            
