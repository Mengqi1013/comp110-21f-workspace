"""Drawing forests in a loop."""

__author__ = "730485647"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
j: int = 1 
output: str = ""
if depth > 0: 
    while i < depth + 1:
        while j < depth + 1:
            output = output + TREE
            print(output)
            j = j + 1
        i = i + 1
    
