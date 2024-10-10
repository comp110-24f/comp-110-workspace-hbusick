"""Exercise 4 Utils"""

__author__: str = "730563704"


def all(input_list: list[int], b: int) -> bool:
    "Checks if the values in a list all equal an int"
    if len(input_list) == 0:  # if nothing in input lst
        return False  # return false. Check this before checking actual nums
    for num in range(len(input_list)):  # for every int in input list
        if (
            input_list[num] != b
        ):  # if that given number is not the same as the target int
            return False
    return True  # if false doesnt occur for any num


def max(input: list[int]) -> int:
    "Finds the largest value in a list"
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # value error arg
    initial_val = input[
        0
    ]  # grab the first value of input to compare other values against
    for num in range(
        1, len(input)  # start at 1 becuase we do not want to compare 0 to 0
    ):  # starting at 1 because we already indexed initial val as the 0th element
        if (
            input[num] > initial_val
        ):  # if the given num is greater than our recent compare num
            initial_val = input[
                num
            ]  # replace initial val with this number only if it is greater
    return initial_val  # we basically just do a series of appends to initial val that
    # only changes when it encounters a number larger than its own


def is_equal(a: list[int], b: list[int]) -> bool:
    "checks if two lists of ints are identical"
    if len(a) != len(b):  # not assuming they are the same length so manually check
        return False  # if not same length cannot be identical
    for num in range(len(a)):  # over all indexes
        if a[num] != b[num]:  # since we know len a=b we use 'num' for both
            return False  # False if any pairs not the same
    return True  # if pass through all above must be True


def extend(a: list[int], b: list[int]) -> None:
    "Adds the values of b to the end of a"
    for num in range(len(b)):  # for each value in b
        a.append(b[num])  # add this value to the end of a
