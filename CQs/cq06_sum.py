"""Summing the elements of a list using different loops"""

__author__ = "730563704"


def w_sum(vals: list[float]) -> float:
    "Sums a list of floats into a single float value"
    initial_val: float = 0  # initialize empty float value
    idx: int = 0  # initialize index to loop over
    while idx < len(vals):
        initial_val += vals[idx]  # grab val at that index and add to empty
        idx += 1
    return initial_val


def f_sum(vals: list[float]) -> float:
    "Sums a list of floats into a single float value"
    empty_val: float = 0  # just need the initial empty value
    for val in vals:
        empty_val += val  # no need to index since we know where we are
    return empty_val


def f_range_sum(vals: list[float]) -> float:
    "Sums a list of floats into a single float value"
    empty_val: float = 0  # once again no need for an index value
    for val in range(len(vals)):
        empty_val += vals[val]  # [val] serves as our index value
    return empty_val
