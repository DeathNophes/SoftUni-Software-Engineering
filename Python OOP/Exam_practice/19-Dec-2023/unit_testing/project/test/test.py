from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self) -> None:

        self.robot = ClimbingRobot(
            'Mountain',
            'helper',
            100,
            200
        )

        self.robot_with_software = ClimbingRobot(
            'Mountain',
            'helper',
            100,
            200,
        )

        self.robot_with_software.installed_software = [
            {'name': 'PyCharm', 'capacity_consumption': 50, 'memory_consumption': 49},
            {'name': 'CLion', 'capacity_consumption': 49, 'memory_consumption': 51}
        ]

    def test_correct_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('helper', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_create_robot_with_invalid_category_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Invalid'

        self.assertEqual(
            f"Category should be one of {self.ALLOWED_CATEGORIES}",
            str(ve.exception)
        )

    def test_get_used_capacity_expect_success(self):
        result = self.robot_with_software.get_used_capacity()
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)

        self.assertEqual(expected_result, result)

    def test_get_available_capacity_expect_success(self):
        result = self.robot_with_software.get_available_capacity()
        expected_result = self.robot.capacity - sum(s['capacity_consumption'] for s in
                                                    self.robot_with_software.installed_software)

        self.assertEqual(expected_result, result)

    def test_get_used_memory_expect_success(self):
        result = self.robot_with_software.get_used_memory()
        expected_result = sum(s['memory_consumption'] for s in
                              self.robot_with_software.installed_software)

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        result = self.robot_with_software.get_available_memory()
        expected_result = self.robot.memory - sum(s['memory_consumption'] for s in
                                                  self.robot_with_software.installed_software)

        self.assertEqual(expected_result, result)

    def test_install_software_with_max_equal_values_expect_success(self):
        result = self.robot.install_software(
            {'name': 'PyCharm', 'capacity_consumption': 100, 'memory_consumption': 200}
        )

        expected_result = "Software 'PyCharm' successfully " \
                          "installed on Mountain part."

        self.assertEqual(expected_result, result)

        self.assertEqual(
            self.robot.installed_software,
            [{'name': 'PyCharm', 'capacity_consumption': 100, 'memory_consumption': 200}]
        )

    def test_install_software_with_less_than_max_values_expect_success(self):
        result = self.robot.install_software(
            {'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 20}
        )

        expected_result = "Software 'PyCharm' successfully " \
                          "installed on Mountain part."

        self.assertEqual(expected_result, result)

        self.assertEqual(
            self.robot.installed_software,
            [{'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 20}]
        )

    def test_install_software_with_one_greater_than_max_equal_values_expect_error_message(self):
        result = self.robot.install_software(
            {'name': 'PyCharm', 'capacity_consumption': 10, 'memory_consumption': 2000}
        )

        expected_result = "Software 'PyCharm' cannot be installed on Mountain part."

        self.assertEqual(expected_result, result)

        self.assertEqual(
            self.robot.installed_software,
            []
        )

    def test_install_software_with_both_values_greater_than_max_return_error_message(self):
        result = self.robot_with_software.install_software(
            {'name': 'PyCharm1', 'capacity_consumption': 49, 'memory_consumption': 50}
        )

        expected_result = "Software 'PyCharm1' cannot be installed on Mountain part."

        self.assertEqual(expected_result, result)

        self.assertEqual(
            self.robot_with_software.installed_software,
            [
                {'name': 'PyCharm', 'capacity_consumption': 50, 'memory_consumption': 49},
                {'name': 'CLion', 'capacity_consumption': 49, 'memory_consumption': 51}
            ]
        )


if __name__ == '__main__':
    main()