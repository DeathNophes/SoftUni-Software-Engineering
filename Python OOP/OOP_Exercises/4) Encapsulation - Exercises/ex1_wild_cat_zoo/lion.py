from ex1_wild_cat_zoo.animal import Animal


class Lion(Animal):
    DEFAULT_MONEY_FOR_LION = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_FOR_LION)