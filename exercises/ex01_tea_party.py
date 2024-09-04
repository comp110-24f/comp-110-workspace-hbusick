"""Exercise 01 Tea Party"""

__author__: str = "730563704"


def main_planner(guests: int) -> None:
    "runs event plans"
    print("A Cozy Tea Party For", guests, "People!")
    print("Tea Bags: ", tea_bags(people=guests))
    print("Treats: ", treats(people=guests))
    print("Cost: $", cost(tea_bags(people=guests), treat_count=treats(people=guests)))
    # The only input for this function is guests...
    # so tea and treat count must = guests?
    # Work backwards from initial tea_bags and treats functions to get a value that you
    # then use in the cost function


def tea_bags(people: int) -> int:
    "number of tea bags for # attending"
    tea_bags = int(people * 2)
    return tea_bags


def treats(people: int) -> int:
    "treats for given # of guests"
    teas = tea_bags(people)
    # call the tea bag function to get number of teas
    # define as its own new variable
    treats = int(teas * 1.5)
    return treats


def cost(tea_count: int, treat_count: int) -> float:
    "takes a given amount of teas and treats to calculate cost"
    tea_cost = tea_count * 0.5
    treat_cost = treat_count * 0.75
    # define new variables for storing calculations
    cost = tea_cost + treat_cost
    # define total cost
    return cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
