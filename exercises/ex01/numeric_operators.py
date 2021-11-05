<<<<<<< HEAD
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
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
