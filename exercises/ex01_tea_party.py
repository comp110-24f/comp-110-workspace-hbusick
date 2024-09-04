"""Exercise 01 Tea Party"""

__author__: str = "730563704"


def main_planner(guests: int) -> None:
    "runs event plans"  # Values must all ultimately come from the guests input
    print("A Cozy Tea Party For", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print(
        "Treats:", treats(people=guests)
    )  # people = guests these are basically synonomous throughout
    print(
        "Cost: $"
        + str(
            cost(tea_bags(people=guests), treat_count=treats(people=guests))
        )  # nest the tea bag and treat functions within the cost function
    )  # Convert cost to a string to solve the empty space after "$"


def tea_bags(people: int) -> int:
    "number of tea bags for # attending"
    return int(people * 2)


def treats(people: int) -> int:
    "treats for given # of guests"
    return int(tea_bags(people=people) * 1.5)


# use people to get total tea bags first


def cost(tea_count: int, treat_count: int) -> float:
    "takes a given amount of teas and treats to calculate cost"
    return (tea_count * 0.5) + (treat_count * 0.75)


# how we get these values makes more sense later in the main planner

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
