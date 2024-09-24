"""Fourth Problem Set"""

# Using your last homework as a guide, create 2 functions: one that takes a list
# input and returns the sum of the list, and one that takes a list as input and
# returns its average '''(use a for loop for at least one of these, please!)'''


def list_sum(numbers: list) -> int:
    "Takes a list of numbers and sums the values"
    value = 0
    for i in numbers:
        value += i
    return value


def list_avg(numbers: list) -> float:
    "Takes a list of numbers and returns the average"
    value = 0
    top_frac = 0
    for i in numbers:
        top_frac += i
    value = top_frac / len(numbers)
    return value


# Now, do the following tasks using your functions from above:

# 1 - create a function that returns the total sum of items in 3 inputted lists

# 2 - create a function that returns the difference in the average value of any
#     2 inputted lists (always does first list - second list)

# 3 - create a function that takes in 2 lists of numbers and returns 2 lists
#     that have equal sums. Specifically, you should add a value to the list with
#     the lower total sum such that the two sums are now equal
#     Hint: You can return two items by simply putting a comma between them, e.g.
#           return x, y


def sum_three_lists(list1: list, list2: list, list3: list) -> int:
    "Sums the values from three lists"
    value = 0
    list1_val = list_sum(list1)
    list2_val = list_sum(list2)
    list3_val = list_sum(list3)
    value = list1_val + list2_val + list3_val
    return value


def difference_in_lists(list1: list, list2: list) -> float:
    "Finds the absolute difference between the average of 2 lists"
    value = 0
    list1_val = list_avg(list1)
    list2_val = list_avg(list2)
    value = abs(list1_val - list2_val)
    return value


def make_list_equal(list1: list, list2: list):
    "appends list 1 such that its sum then equals the sum of list2"
    list1_val = list_sum(list1)
    list2_val = list_sum(list2)
    addto1 = abs(list1_val - list2_val)
    list1.append(addto1)
    list1_val2 = list_sum(list1)
    list2_val2 = list_sum(list2)
    if list1_val2 == list2_val2:
        return list1, list2, addto1


# Using your hypotenuse homework assignment as a guide:
# Create a function that calculates the distance between two points
# Inputs should be x1, y1, x2, y2
# Output: the distance between these two points
# Pseudocode:
# find the the difference between the two x values, between the 2 y values
# treat these like the two sides of a triangle
# find the length of the hypotenuse (aka the distance between these points)
# return this value


def dist(x1: float, x2: float, y1: float, y2: float) -> float:
    x_dist = abs(x2 - x1)
    y_dist = abs(y2 - y1)
    hypotenuse = (x_dist**2 + y_dist**2) ** 0.5
    return hypotenuse


# Using your function from above:
# Create a game of battleship (just in your script, not in a function)
# This is your Main Code Chunk!
# Choose a spot for your ship to be (an x and y coordinate)
# Ask the user for an x and a y value
# If they are within distance 3 from your value, they sunk your ship
# Otherwise, tell them they are wrong, tell them how far away they are
# Let them try until they sink your ship
# If you'd like, you can add limits (board is only 25 x 25, for example)
# or you can tell them when they're getting hotter or colder, etc.

my_ship_x = 4
my_ship_y = 7

initial_x = int(input("X Coordinate for Guess"))
initial_y = int(input("Y Coordinate for Guess"))

distance = dist(my_ship_x, initial_x, my_ship_y, initial_y)

if distance <= 3:
    print("Ship Sunk!")
else:
    while distance > 3:
        print("Too far, guess again")
        next_guess_x = int(input("Next X Guess"))
        next_guess_y = int(input("Next Y Guess"))
        distance = dist(my_ship_x, next_guess_x, my_ship_y, next_guess_y)
        print("You are", distance, "spaces away")
        if distance <= 3:
            print("Ship Sunk!")
