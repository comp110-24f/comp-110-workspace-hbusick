"""CQ07 Find Max Function"""


def find_and_remove_max(a: list[int]) -> int:
    "Finds and removes the max int from a list"
    if a == []:
        return -1  # case for empty list
    val = a[0]  # initialize first value to be evaluated
    for num in a:  # for each number in a
        if num > val:  # if that number is greater than given val
            val = num  # replace val with said number
    idx = 0  # initialize index for popping
    while idx < len(a):  # while withing range
        if a[idx] == val:  # if the value at a given index = our val
            a.pop(idx)  # pop that index
        else:
            idx += 1  # only do this if we dont pop something
    return val  # give greatest value back to user
