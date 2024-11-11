"""File to define Bear class."""


class Bear:

    age: int  # bears age and hunger score
    hunger_score: int

    def __init__(self):
        self.age = 0  # initialize vals
        self.hunger_score = 0
        return None

    def one_day(self):
        "Adds 1 to the bears age"
        self.age += 1  # one to age each day
        self.hunger_score -= 1  # looses a hunger point each day
        return None

    def eat(self, num_fish: int):
        "hunger score increase by numfish"
        self.hunger_score += num_fish  # each fish one point
