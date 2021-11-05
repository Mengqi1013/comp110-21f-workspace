<<<<<<< HEAD
"""This program allows the user to input two number variables and then prints out messages with a specific format to demonstrate how four relational operators work in Python."""

__author__ = "730485647"

left = int(input("Left-hand side: "))
right = int(input("Right-hand side: "))
result_one = bool(left < right)
result_two = bool(left >= right)
result_three = bool(left == right)
result_four = bool(left != right)

print(str(left) + " < " + str(right) + " is " + str(result_one))
print(str(left) + " >= " + str(right) + " is " + str(result_two))
print(str(left) + " == " + str(right) + " is " + str(result_three))
print(str(left) + " != " + str(right) + " is " + str(result_four))
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
