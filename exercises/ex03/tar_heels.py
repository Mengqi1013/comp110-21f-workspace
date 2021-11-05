"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
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
=======
__author__ = "730243388"


# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
