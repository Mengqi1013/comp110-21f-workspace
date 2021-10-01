"""List utility functions part 2."""

__author__ = "730485647"


# Define your functions below
def only_evens(xs: list[int]) -> list[int]:
    """Returns the even elements in a list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(xs): 
        item: int = 0
        if xs[i] // 2 == 0:
            item = item + xs[i]
            xs.append(item)
        else:
            popped_item: int = xs[i]
            xs.pop(popped_item)
        i = i + 1
    return even_list


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Returns a subset of the given list based on the starting and ending indexes."""
    new_list: list[int] = []
    i: int = a
    while i < (b - a):
        new_list.append(xs[i])
        i = i + 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates two lists given and returns a new list."""
    i: int = 0 
    string1: str = ""
    string2: str = ""
    new_list: list[int] = []
    while i < len(xs):
        string1 = str(xs[i])
        new_list.append(int(string1[i]))
        i = i + 1
    while i < len(ys):
        string2 = str(ys[i])
        new_list.append(int(string2[i]))
        i = i + 1   
    return new_list


print(concat([1, 2, 3], [4, 5, 6]))
            
