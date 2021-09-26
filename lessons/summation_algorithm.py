"""Example of list and loop algorithm."""


def sum_algo(xs: list[int]) -> int:
    """Summation of a list is returned."""
    # 1. Initalize total and index to 0
    i: int = 0
    total: int = 0
    # 2. While i is valid, meaning i < len(xs) 
    while i < len(xs):
        total += xs[i]
    i += 1
    print(f"The sum is: {total}")
    return total