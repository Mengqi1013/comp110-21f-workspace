"""Counting letters in a string."""

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