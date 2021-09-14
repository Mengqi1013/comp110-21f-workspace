"""Drawing forests in a loop."""

__author__ = "730485647"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
input: int = int(input("Depth: "))
i: int = 0
j: int = 1 
output: str = ""
if input > 0: 
    while i < input + 1:
        while j < input + 1:
            output = output + TREE
            print(output)
            j = j + 1
        i = i + 1
    
