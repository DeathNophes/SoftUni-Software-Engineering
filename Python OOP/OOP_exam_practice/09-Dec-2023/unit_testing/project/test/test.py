from unittest import TestCase, main
from collections import deque
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation('Station')

    def test_correct_init(self):
        self.assertEqual('Station', self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_wrong_init_expect_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.invalid_station = RailwayStation('Sta')

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_expect_success(self):
        self.station.new_arrival_on_board('Plovdiv-Sofia')

        self.assertEqual(
            deque(['Plovdiv-Sofia']),
            self.station.arrival_trains
        )

    def test_train_has_to_arrive_but_there_are_other_trains_before_expect_string(self):
        self.station.arrival_trains.append('Burgas-Sofia')
        self.station.arrival_trains.append('Plovdiv-Sofia')

        expected_result = f"There are other trains to arrive before Plovdiv-Sofia."

        result = self.station.train_has_arrived('Plovdiv-Sofia')

        self.assertEqual(expected_result, result)

    def test_train_has_to_arrive_expect_success(self):
        self.station.arrival_trains.append('Burgas-Sofia')
        self.station.arrival_trains.append('Plovdiv-Sofia')

        expected_result = f"Burgas-Sofia is on the platform and will leave in 5 minutes."

        result = self.station.train_has_arrived('Burgas-Sofia')

        self.assertEqual(expected_result, result)

        self.assertEqual(
            self.station.departure_trains,
            deque(['Burgas-Sofia'])
        )

        self.assertEqual(
            deque(['Plovdiv-Sofia']),
            self.station.arrival_trains
        )

    def test_train_has_left_with_the_right_train_expect_True(self):
        self.station.departure_trains.append('Plovdiv-Sofia')

        result = self.station.train_has_left('Plovdiv-Sofia')

        self.assertEqual(True, result)

    def test_train_has_left_with_the_wrong_train_expect_False(self):
        self.station.departure_trains.append('Plovdiv-Sofia')

        result = self.station.train_has_left('Burgas-Sofia')

        self.assertEqual(False, result)


if __name__ == '__main__':
    main()