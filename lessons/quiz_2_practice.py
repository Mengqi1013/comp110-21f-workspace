"""Question 15. A function called odd-and_even."""


def odd_and_even(xs: list[int]) -> list[int]:
    i: int = 0
    while i < len(xs):
        item: int = xs[i]
        if item % 2 == 0:
            xs.pop(i)
            i = i + 1  
    return xs


print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))
print(odd_and_even([1, 1, 1, 0, 1]))

print("5")