"""EX08 Linked List Utils"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list"""
        rest: str = "TODO"
        # figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# innermost parenthesis get constructed first, thus Node(301, None) is first


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a nonempty list"""
    # Base case
    if head.next is None:
        return head.value
    # Recursive case
    else:
        rest: int = last(head.next)
        return rest


print(last(courses))


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end"""
    # Handle the edge case where start is greater than end
    if start > end:
        raise ValueError("Invalid aguments, start greather than end")
    # Base
    if start == end:
        return None
    # recursive
    else:
        # step 1 handle first value
        first: int = start
        # then let the rest of the list be handled recursively
        rest: Node | None = recursive_range(start + 1, end)
        # finally return the new node which is first followed by rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 120)
print(a_list)


def value_at(head: Node | None, index: int) -> int:
    """recursievely returns val of node at an index"""
    if head is None:  # edge case for an empty list
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # base case when index = 0, return that val
        return head.value
    else:  # call value at recursively to go to next node
        # decrease index val to move closer to base case
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """returns maximum value of a linked list"""
    if head is None:  # edge case for an empty list
        raise IndexError("Cannot call max with None")
    if head.next is None:  # if we do not have a further node to move to
        return head.value  # return the val we are currently at, no change
    rest_val: int = max(head.next)  # recursively call max on the rest of the list
    # define the varialbe rest to be the result of the next value
    # we can then use an if statement to check whether or not this value is less than
    # the current head.value
    if head.value > rest_val:  # if our current val is the greatest out of the list
        return head.value  # our max is then the val we are at
    else:  # otherwise our maximum value is just the number we found calling max within
        return rest_val
