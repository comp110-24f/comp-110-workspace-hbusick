"""Simulation runner for EX07"""

__author__: str = "730563704"

from .river import River

my_river = River(10, 2)  # make a river

my_river.view_river()  # view the river

my_river.one_river_week()  # spend a week in the river

if __name__ == "main":
    my_river = River(10, 2)
