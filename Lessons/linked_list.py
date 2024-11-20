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
