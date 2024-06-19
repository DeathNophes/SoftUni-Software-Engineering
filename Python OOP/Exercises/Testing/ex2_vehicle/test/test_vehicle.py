from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.0, 150.0)

    def test_correct_init(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.assertEqual(10.0, self.vehicle.capacity)
        self.assertEqual(150.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_is_less_than_fuel_needed_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_when_fuel_is_enough(self):
        expected_result = self.vehicle.fuel - 1.25

        self.vehicle.drive(1)

        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_if_fuel_is_more_than_capacity_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_when_fuel_is_less_or_equal_to_capacity(self):
        self.vehicle.fuel = 0
        expected_result = self.vehicle.fuel + 5

        self.vehicle.refuel(5)

        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_string_method(self):
        expected_result = "The vehicle has 150.0 horse power with 10.0 fuel left and 1.25 fuel consumption"
        result = self.vehicle.__str__()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()