"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730485647"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
random_number = randint(1, 9)

if random_number < 3:
    print("Your fortune cookie says...")
    print("You are doing excellent!")
    print("Now, go spread positive vibes!")
else:
    if random_number < 5:
        print("Your fortune cookie says...")
        print("You are such a brilliant and beautiful individual.")
        print("Now, go spread positive vibes!")
    else:
        if random_number < 7:
            print("Your fortune cookie says...")
            print("Don't stress. Life goes on!")
            print("Now, go spread positive vibes!")
        else:
            print("Your fortune cookie says...")
            print("Work harder and you'll achieve your goal!")
            print("Now, go spread positive vibes!")
