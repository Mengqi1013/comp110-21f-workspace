"""An example to demonstrate syntax for creating a function."""
"""name, argument(list of expressions), """


def my_min(a: int, b: int) -> int:
    if a <= b:
        return a
    else:
        return b


x: int = 6
y: int = 8
z: int = x * y
result: int = my_min(x, z)
print(result)
