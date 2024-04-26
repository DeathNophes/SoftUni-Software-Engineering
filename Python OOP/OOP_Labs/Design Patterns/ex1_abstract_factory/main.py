from ex1_abstract_factory.factories.victorian_factory import VictorianFactory
from ex1_abstract_factory.factories.modern_factory import ModernFactory


victorian_factory = VictorianFactory()

print(victorian_factory.create_sofa())
print(victorian_factory.create_chair())
print(victorian_factory.create_table())

modern_factory = ModernFactory()

print(modern_factory.create_sofa())
print(modern_factory.create_chair())
print(modern_factory.create_table())
