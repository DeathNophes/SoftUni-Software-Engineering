from ex3_multiple_inheritance.person import Person
from ex3_multiple_inheritance.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."