"CQ09 Point"


from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        "Init definition"
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        "Scales mutating"
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        "Scales without mutating"
        return Point(self.x * factor, self.y * factor)
