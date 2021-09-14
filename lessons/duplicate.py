"""Tell if a string has duplicate characters."""

string: str = input("Enter a word: ")
i: int = 0
j: int = 1 
counter: int = 0
while i < len(string) - 1:
    while j < len(string):
        if string[i] == string[j]:
            counter = counter + 1
        j = j + 1
    i = i + 1
if counter > 0:
    print("True")
else:
    print("False")
