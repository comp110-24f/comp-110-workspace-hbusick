"""Intro to lists"""

# my_numbers: list[float] = []

# game_points: list[int] = [102, 86, 94]

# print(game_points[2])

# game_points[2] = 38

# print(game_points[2])


# def display(int_list):
#     for value in int_list:
#         print(value)


# print(display(game_points))


def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


display([1, 2, 3])
