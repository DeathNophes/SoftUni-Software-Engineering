from ex4_wild_farm.animals.animal import Bird
from ex4_wild_farm.food import Fruit, Vegetable, Meat, Seed


class Owl(Bird):

    @ property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self) -> list:
        return [Fruit, Vegetable, Meat, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
