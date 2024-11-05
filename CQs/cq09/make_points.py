"""Checking that Point#scale does not mutate original x and y"""

from CQs.cq09.point import Point

myPoint: Point = Point(1.0, 2.0)  # make a point
scaledPoint: Point = myPoint.scale(3)  # scale this point - shouldnt mutate
print(f"1st point coords: ({myPoint.x}, {myPoint.y})")
print(f"2st point coords: ({scaledPoint.x}, {scaledPoint.y})")
myPoint.scale_by(17)  # should mutate point 1
print(f"1st point coords after scaling by 17: ({myPoint.x}, {myPoint.y})")
