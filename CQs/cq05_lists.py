"""Mutating functions"""

__author__ = "730563704"


def manual_append(a: list[int], b: int) -> None:
    "adds a int to the end of a list of ints"
    a.append(b)  # append a by adding b to the end of it
    print(a)


def double(a: list[int]) -> None:
    "takes all values and multiplies them by two at their index"
    idx: int = 0  # initialize index
    while len(a) >= idx:  # while we are within the length of a
        a[idx] *= 2  # times equal
        idx += 1
    print(a)


list1: list[int] = [1, 2, 3]
list2 = list1

double(list2)

print(list1)
print(list2)
