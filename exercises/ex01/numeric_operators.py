"""This program allows the user to input 2 variables and prints out messages with a specific format to demonstrate how certain math operators work in Python!"""

__author__ = "730485647"

left = int(input("Left-hand side: "))
right = int(input("Right-hand side: "))
power = int(left ** right)
quotient = float(left / right)
int_quotient = int(left // right)
modulo = int(left % right)

print(str(left) + " ** " + str(right) + " is " + str(power))
print(str(left) + " / " + str(right) + " is " + str(quotient))
print(str(left) + " // " + str(right) + " is " + str(int_quotient))
print(str(left) + " % " + str(right) + " is " + str(modulo))
