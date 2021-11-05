"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730485647"


# Begin your solution here...
input_letter: str = input("What letter do you want to search for?: ")
input_word: str = input("Enter a word: ")

counter: int = 0
i: int = -1
while i < len(input_word) - 1:
    i = i + 1 
    if input_word[i] == input_letter:
        counter = counter + 1
    
print("Count: " + str(counter))
=======
__author__ = "730243388"


# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
