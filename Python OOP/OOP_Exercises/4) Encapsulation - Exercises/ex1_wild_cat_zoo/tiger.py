from ex1_wild_cat_zoo.animal import Animal


class Tiger(Animal):
    DEFAULT_MONEY_FOR_TIGER = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_FOR_TIGER)