"""Example of writing a function to process a list."""

__author__ = "730485647"


def main() -> None:
    """Entry of the program."""
    contains("Kris", ["Kris", "Kaki", "Mandy"])


def contains(needle: str, haystack: list[str]):
    """Returns True if needle is found in our list, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i = i + 1
    return False


if __name__ == "__main__":
    main()