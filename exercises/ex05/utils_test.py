"""Test for Utils EX05"""

__author__: str = "730563704"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens() -> None:
    "normal test"
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(a) == [2, 4, 6, 8, 10]


def test_mutation_only_evens() -> None:
    "Tests the mutation of only evens, a should not change"
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_edge_only_evens() -> None:
    "edge case with only odds and a negative"
    a = [-1, 1, 9999, 10001]
    assert only_evens(a) == []


def test_sub() -> None:
    "tests normal output use of sub"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx = 3
    end_idx = 9
    assert sub(a_list, start_idx, end_idx) == [4, 5, 6, 7, 8, 9]


def test_mutation_sub() -> None:
    "Test mutation, a_list should go uncahnged"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx = 3
    end_idx = 9
    sub(a_list, start_idx, end_idx)
    assert a_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_edge_sub() -> None:
    "tests an edge case with a negative beginning idx"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx = -5
    end_idx = 1
    assert sub(a_list, start_idx, end_idx) == [1]


def test_add_at_index() -> None:
    "Tests normal return use of add at index"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element = 99
    index = 5
    add_at_index(a_list, element, index)
    assert a_list == [1, 2, 3, 4, 5, 99, 6, 7, 8, 9, 10]


def test_type_add_at_index() -> None:
    "Tests what add at index returns"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element = 99
    index = 5
    assert add_at_index(a_list, element, index) is None  # cant use ==


def test_edge_add_at_index() -> None:
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element = 99
    index = 11
    with pytest.raises(IndexError):
        add_at_index(a_list, element, index)
