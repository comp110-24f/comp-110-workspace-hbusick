"""Testing CQ07"""

from CQs.cq07.find_max import find_and_remove_max


def test_return_find_and_remove_max() -> None:
    "General test of rv finding and removing the max"
    nums: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(nums) == 5


def test_list_find_and_remove_max() -> None:
    "test that find and remove max alters str correctly"
    nums: list[int] = [1, 2, 3, 4, 5, 5]
    find_and_remove_max(nums)
    assert nums == [1, 2, 3, 4]


def test_edge_find_and_remove_max() -> None:
    "Edge case with neg nums"
    nums: list[int] = [-1111, -111, -11, -1, 0]
    assert find_and_remove_max(nums) == 0
