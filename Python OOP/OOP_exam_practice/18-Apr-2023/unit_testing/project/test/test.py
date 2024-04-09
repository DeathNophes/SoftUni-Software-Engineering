from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot(1, 'Military', 100, 10)

    def test_correct_init(self):
        self.assertEqual(1, self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(10, self.robot.price)

    def test_wrong_category_init_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.wrong_robot = Robot(2, 'Wrong', 100, 10)

        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_less_than_zero_init_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.wrong_robot = Robot(2, "Military", 100, -1)

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_component_which_is_currently_on_our_robot_expect_message(self):
        self.robot.hardware_upgrades.append('Third hand')

        expected_result = f"Robot {self.robot.robot_id} was not upgraded."
        result = self.robot.upgrade('Third hand', 10)

        self.assertEqual(expected_result, result)

    def test_upgrade_expect_success(self):
        result = self.robot.upgrade('Third hand', 10)
        expected_message = f'Robot {self.robot.robot_id} was upgraded with Third hand.'

        self.assertEqual(expected_message, result)
        self.assertEqual(['Third hand'], self.robot.hardware_upgrades)
        self.assertEqual(25, self.robot.price)

    def test_update_with_less_than_required_version_expect_unsuccessful_message(self):
        self.robot.software_updates.append(10)

        expected_result = f"Robot {self.robot.robot_id} was not updated."
        result = self.robot.update(9, 10)

        self.assertEqual(expected_result, result)

    def test_update_with_less_required_capacity_expect_unsuccessful_message(self):
        expected_result = f"Robot {self.robot.robot_id} was not updated."
        result = self.robot.update(10, 110)

        self.assertEqual(expected_result, result)

    def test_update_with_adequate_resources_expect_success(self):
        self.robot.software_updates.append(9)

        expect_result = f'Robot {self.robot.robot_id} was updated to version {10}.'
        result = self.robot.update(10, 10)

        self.assertEqual(expect_result, result)
        self.assertEqual([9, 10], self.robot.software_updates)
        self.assertEqual(90, self.robot.available_capacity)

    def test_grater_than_method_expect_messages(self):
        self.greater_robot = Robot(2, 'Military', 1000, 100)
        self.equal_robot = Robot(3, 'Military', 100, 10)

        expected_result_greater = f'Robot with ID {self.greater_robot.robot_id} is more expensive than ' + \
                                  f'Robot with ID {self.robot.robot_id}.'

        expected_result_equal = f'Robot with ID {self.robot.robot_id} costs equal to ' + \
                                f'Robot with ID {self.equal_robot.robot_id}.'

        expected_result_lesser = f'Robot with ID {self.robot.robot_id} is cheaper than ' + \
                                 f'Robot with ID {self.greater_robot.robot_id}.'

        result1 = self.greater_robot > self.robot
        result2 = self.robot > self.equal_robot
        result3 = self.robot > self.greater_robot

        self.assertEqual(expected_result_greater, result1)
        self.assertEqual(expected_result_equal, result2)
        self.assertEqual(expected_result_lesser, result3)


if __name__ == '__main__':
    main()