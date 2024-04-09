from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver('Ivan', 5.00)

    def test_correct_init(self):
        self.assertEqual('Ivan', self.truck_driver.name)
        self.assertEqual(5.00, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_add_cargo_offer_with_already_added_offer_raises_exception(self):
        self.truck_driver.available_cargos = {'Bulgaria': 1000}

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer('Bulgaria', 1000)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_expect_success(self):
        expected_message = f"Cargo for 1000 to Bulgaria was added as an offer."
        message = self.truck_driver.add_cargo_offer('Bulgaria', 1000)

        self.assertEqual(expected_message, message)
        self.assertEqual({'Bulgaria': 1000}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer_expect_no_offers_available_message(self):
        expected_message = "There are no offers available."
        message = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(expected_message, message)

    def test_drive_best_cargo_offer_expect_success(self):
        self.truck_driver.available_cargos = {'Bulgaria': 10000, 'Russia': 5000}

        expected_message = f"Ivan is driving 10000 to Bulgaria."
        message = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(expected_message, message)
        self.assertEqual(38250.0, self.truck_driver.earned_money)
        self.assertEqual(10000, self.truck_driver.miles)

    def test_drive_best_cargo_expect_bankrupt(self):
        self.truck_driver.money_per_mile = 1.00
        self.truck_driver.available_cargos = {'Bulgaria': 10000}

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(f"Ivan went bankrupt.", str(ve.exception))

    def test_represent_method(self):
        expected_message = f"Ivan has 0 miles behind his back."
        message = self.truck_driver.__repr__()

        self.assertEqual(expected_message, message)


if __name__ == '__main__':
    main()