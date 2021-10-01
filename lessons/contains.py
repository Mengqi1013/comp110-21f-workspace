"""Example of writing a function to process a list."""

__author__ = "730485647"


def contains(needle: str, haystack: list[str]) -> bool:
    """Return value iff needle is found in the haystack. False otherwise."""
    # Move through each item in list until needle is found 
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False
           