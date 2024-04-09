from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.gle = SecondHandCar('GLE', '4WD', 100_000, 50_000.00)
        self.gtr = SecondHandCar('GT-R', '4WD', 50_000, 150_000.00)

    def test_correct_init(self):
        self.assertEqual('GLE', self.gle.model)
        self.assertEqual('4WD', self.gle.car_type)
        self.assertEqual(100_000, self.gle.mileage)
        self.assertEqual(50_000.00, self.gle.price)
        self.assertEqual([], self.gle.repairs)

    def test_init_price_less_than_1_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar('Octavia', 'FWD', 500, 0.05)

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_init_mileage_below_100_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar('Octavia', 'FWD', 50, 0.05)

        self.assertEqual(
            'Please, second-hand cars only! Mileage must be greater than 100!',
            str(ve.exception)
        )

    def test_set_promotional_price_with_new_price_higher_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.gle.set_promotional_price(55_000.00)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_expect_success(self):
        result = self.gle.set_promotional_price(45_000.00)
        expected_result = 'The promotional price has been successfully set.'

        self.assertEqual(expected_result, result)
        self.assertEqual(45_000.00, self.gle.price)

    def test_need_repair_expect_repair_is_impossible(self):
        expected_result = 'Repair is impossible!'

        result = self.gle.need_repair(30_000.00, 'Change Engine')

        self.assertEqual(expected_result, result)

    def test_need_repair_expect_success(self):
        expected_message = f'Price has been increased due to repair charges.'

        result_message = self.gle.need_repair(5_000.00, 'Change tires')

        self.assertEqual(expected_message, result_message)
        self.assertEqual(55_000.00, self.gle.price)
        self.assertEqual(['Change tires'], self.gle.repairs)

    def test_gt_method_different_car_types_expect_type_mismatch(self):
        self.gtr.car_type = 'FWD'

        expected_result = 'Cars cannot be compared. Type mismatch!'
        result = self.gle > self.gtr
        self.assertEqual(expected_result, result)

    def test_gt_method_same_car_types_expect_False(self):
        result = self.gle > self.gtr
        self.assertEqual(False, result)

    def test_gt_method_same_car_types_expect_True(self):
        result = self.gtr > self.gle
        self.assertEqual(True, result)

    def test_str_method(self):
        expected_result = f"""Model {self.gle.model} | Type {self.gle.car_type} | Milage {self.gle.mileage}km
Current price: {self.gle.price:.2f} | Number of Repairs: {len(self.gle.repairs)}"""

        result = self.gle.__str__()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()