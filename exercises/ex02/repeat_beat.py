"""Repeating a beat in a loop."""

<<<<<<< HEAD
__author__ = "730485647"


# Begin your solution here...
input_string: str = input("What beat do you want to repeat? ")
input_number: int = int(input("How many times do you want to repeat it? "))

i: int = 0
new_string: str = ""

if input_number <= 0:
    print("No beat...")
else:
    while i < input_number:
        if i < input_number - 1:
            new_string = new_string + input_string + " "
        else:
            if i == input_number - 1:
                new_string = new_string + input_string
        i = i + 1

print(new_string)
=======
__author__ = "730243388"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
