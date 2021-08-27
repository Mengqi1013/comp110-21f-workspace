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
