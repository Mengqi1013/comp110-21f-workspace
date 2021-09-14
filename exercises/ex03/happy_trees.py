"""Drawing forests in a loop."""

__author__ = "730485647"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
input: int = int(input("Depth: "))
i: int = 1
while i < input + 1:
    if input > 0:
        print(TREE * i)
        i = i + 1