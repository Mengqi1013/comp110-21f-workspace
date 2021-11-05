"""Drawing forests in a loop."""

__author__ = "730485647"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
<<<<<<< HEAD
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
    
=======

depth: int = int(input("Depth: "))

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
