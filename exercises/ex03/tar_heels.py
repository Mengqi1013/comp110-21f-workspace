"""An exercise in remainders and boolean logic."""

__author__ = "730485647"


# Begin your solution here...

a: int = int(input("Enter an int: "))
if a % 2 == 0:
    if a % 7 != 0:
        print("TAR")
    else:
        print("TAR HEELS")
else:
    if a % 7 != 0:
        print("CAROLINA")
    else:
        print("HEELS")