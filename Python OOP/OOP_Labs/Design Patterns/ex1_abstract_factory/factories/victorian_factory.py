from ex1_abstract_factory.factories.abstract_furniture_factory import AbstractFactory
from ex1_abstract_factory.furniture.sofa import Sofa
from ex1_abstract_factory.furniture.table import Table
from ex1_abstract_factory.furniture.chair import Chair


class VictorianFactory(AbstractFactory):
    def create_sofa(self):
        return Sofa('Victorian')

    def create_chair(self):
        return Chair('Victorian')

    def create_table(self):
        return Table('Victorian')