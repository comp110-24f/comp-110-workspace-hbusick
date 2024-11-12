"""File to define River class."""

from .fish import Fish
from .bear import Bear

__author__: str = "730563704"


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        "Only bears younger than 6 days, fish 4"
        fish_alive: list = []  # initialize list for fish w/ correct age
        bears_alive: list = []  # initialize list for bears w/ correct age
        for fish in self.fish:  # for each fish in the river
            if fish.age <= 3:  # evaluate their age | if satisfied
                fish_alive.append(fish)  # add them to the living string
        for bear in self.bears:  # same as above but a different age
            if bear.age <= 5:
                bears_alive.append(bear)
        self.fish = fish_alive  # update attributes
        self.bears = bears_alive  # same

        return None

    def bears_eating(self):
        "Bears eating fish if lenfish is sufficient"
        for bear in self.bears:  # for each bear
            if len(self.fish) >= 5:  # if there are equal to or more
                self.remove_fish(3)  # remove the three fish that ->
                bear.eat(3)  # are eaten by the bear
        return None

    def check_hunger(self):
        "check the hunger score of all bears in the river"
        bears_to_live: list = []  # initialize list for bears that survive
        for bear in self.bears:  # for each bear in the river
            if bear.hunger_score >= 0:  # if their hunger score is nonneg
                bears_to_live.append(bear)  # add that bear to the live list
        self.bears = bears_to_live  # update the list of bears with only the surviving

    def repopulate_fish(self):
        "repopulate fish at a ratio of 4 new to 2 existing"
        new_fish: int = (len(self.fish) // 2) * 4  # get num of new fish created
        while new_fish > 0:  # while there are still fish to be added
            self.fish.append(Fish())  # add new fish by calling Fish()
            new_fish = -1  # deduct this fish from the value calc for new_fish
        return None

    def repopulate_bears(self):
        "repopulate bears at a ratio of 1 new to 2 existing"
        new_bears: int = len(self.bears) // 2  # get the num of new bears to be created
        while new_bears > 0:  # while there are still bears left to be added
            self.bears.append(Bear())  # add them to self.bears by running Bear()
            new_bears -= (
                1  # once added, remove that bear by subtracting 1 from new bear
            )
        return None

    def view_river(self):
        "Prints current status of the river"
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")  # j print stmts
        print(f"Bear population: {len(self.bears)}")

        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        "Simulates one week in the river"
        river_days: int = 0  # counter for number of days surpassed
        while river_days < 7:  # for all days less than 7 since 0-6
            self.one_river_day()  # run one river day
            river_days += 1  # add one each time

    def remove_fish(self, amount: int):
        "removes the frontmost amount of fish"
        count: int = 0  # initialize a counter | think of as num fish removed
        while (
            count < amount and self.fish
        ):  # while we have not removed more than told/allowed
            self.fish.pop(0)  # remove the frontmost fish
            count += 1  # Add 1 to the indexing variable
