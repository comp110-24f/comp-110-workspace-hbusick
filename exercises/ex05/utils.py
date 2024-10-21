"""Utils for EX05"""

__author__: str = "730563704"


def only_evens(a: list[int]) -> list:
    "Returns only the even values in a list"
    evens = []
    for i in a:  # loop over entire list
        if i % 2 == 0:  # basic case for determining even
            evens.append(i)  # add this instance to even
    return evens


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    "generates a new list between the start and end index"
    new_list: list[int] = []  # initialize empty list
    if len(a_list) == 0:  # empty list case
        return new_list
    elif start_idx > len(a_list):  # if starting idx is greater than ent len
        return new_list
    elif end_idx <= 0:  # ending less than 0 case
        return new_list
    if start_idx < 0:  # case to set neg starts at 0
        start_idx = 0
    if end_idx > len(a_list):  # if range of end greater than list len
        end_idx = len(a_list)
    new_list: list[int] = []  # initialize new list
    for integer in a_list:  # look through the entire list to check if...
        if a_list.index(integer) >= start_idx and a_list.index(integer) < end_idx:
            # this just asks if the current index falls btwn start and end
            new_list.append(integer)  # append that val into if so
    return new_list


def add_at_index(a_list: list[int], element: int, index: int) -> None:
    "Takes element and adds to a_list at index"
    if index < 0 or index > len(a_list):  # index error case
        raise IndexError("Index is out of bounds for the input list")
    a_list.append(0)  # make room for additional value at right idx
    for idx in range(len(a_list) - 1, index, -1):
        a_list[idx] = a_list[idx - 1]  # shift all elements right into new space
    a_list[index] = element  # set new idx = element val
