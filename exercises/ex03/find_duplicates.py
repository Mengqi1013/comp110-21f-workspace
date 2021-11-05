"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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


    
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
