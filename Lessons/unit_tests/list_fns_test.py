"""Test for list fns"""

from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    foods: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(foods) == "apples"


def test_remove_first_ret_value() -> None:
    """Test that remove first returns None"""
    foods: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(foods) == None


def test_remove_first__behavior() -> None:
    foods: list[str] = ["apples", "oranges", "bananas"]
    remove_first(foods)
    assert foods == ["oranges", "bananas"]
