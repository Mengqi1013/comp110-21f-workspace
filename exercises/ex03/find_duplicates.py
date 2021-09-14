"""Finding duplicate letters in a word."""

__author__ = "730485647"

word: str = input("Enter a word: ")
i: int = 0
j: int = 1
letter_found: str = ""
while i < len(word) - 1:
    while j < len(word):
        if word[i] == word[j]:
            letter_found = letter_found + word[i]
        j = j + 1
    i = i + 1
    j = i + 1

if len(letter_found) > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")


    
