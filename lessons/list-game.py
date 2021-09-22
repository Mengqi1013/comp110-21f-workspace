"""Example of using lists in a simple game."""

__author__ = "730485647"

from random import randint 

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)

# Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0 
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1
print(f"Total score: {sum}")
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))

# print(rolls)
# print(rolls[len(rolls)-1])
# Access an individual item 
# print(len(rolls))