from CQs.cq04.concatenation import concat  # Full file path
from CQs.cq04.coordinates import get_coords

"""Visualize imports for cq04"""

__author__ = "730563704"


x: str = "123"  # globals
y: str = "abc"

print(concat(x, y))  # Positional arguments no specification

get_coords(x, y)  # same here
