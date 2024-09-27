"""Coordinates function for cq04"""

__author__ = "730563704"


def get_coords(xs: str, ys: str) -> None:
    idxx = 0  # xs index counter
    while idxx < len(xs):
        idxy = 0  # xy index counter
        while idxy < len(ys):
            print(xs[idxx], ys[idxy])  # print the pair
            idxy = idxy + 1  # add to y index within second while
        idxx = idxx + 1  # add to x within first while
