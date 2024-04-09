from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.alone_trip = Trip(10_000.00, 1, False)
        self.family_trip = Trip(10_000.00, 2, True)

    def test_alone_trip_correct_init(self):
        self.assertEqual(10_000.00, self.alone_trip.budget)
        self.assertEqual(1, self.alone_trip.travelers)
        self.assertEqual(False, self.alone_trip.is_family)

    def test_family_trip_correct_init(self):
        self.assertEqual(10_000.00, self.family_trip.budget)
        self.assertEqual(2, self.family_trip.travelers)
        self.assertEqual(True, self.family_trip.is_family)

    def test_family_trip_wrong_init(self):
        self.fake_family_trip = Trip(10_000.00, 1, True)
        self.assertEqual(False, self.fake_family_trip.is_family)

    def test_wrong_trip_init_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.no_trip = Trip(10_000.00, 0, False)

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_book_a_trip_to_wrong_destination_expect_string(self):
        expected_result = 'This destination is not in our offers, please choose a new one!'
        result = self.alone_trip.book_a_trip('Canada')
        result2 = self.family_trip.book_a_trip('Canada')

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result, result2)

    def test_book_a_trip_not_enough_budget_expect_string(self):
        self.alone_trip.budget = 10
        self.family_trip.budget = 200

        expected_result = 'Your budget is not enough!'
        result = self.alone_trip.book_a_trip('Bulgaria')
        result2 = self.family_trip.book_a_trip('Bulgaria')

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result, result2)

    def test_book_a_trip_expect_success(self):
        expected_result_alone = f'Successfully booked destination Bulgaria! Your budget left is 9500.00'
        expected_result_family = f'Successfully booked destination Bulgaria! Your budget left is 9100.00'

        result_alone = self.alone_trip.book_a_trip('Bulgaria')
        result_family = self.family_trip.book_a_trip('Bulgaria')

        self.assertEqual(expected_result_alone, result_alone)
        self.assertEqual(expected_result_family, result_family)
        self.assertEqual(9500.00, self.alone_trip.budget)
        self.assertEqual(9100.00, self.family_trip.budget)

    def test_booking_status_expect_no_bookings(self):
        expected_result = 'No bookings yet. Budget: 10000.00'
        result = self.alone_trip.booking_status()
        result2 = self.family_trip.booking_status()

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result, result2)

    def test_booking_status_alone_trip_expect_success(self):
        self.alone_trip.book_a_trip('Bulgaria')

        expected_result = """Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 9500.00"""

        result = self.alone_trip.booking_status()

        self.assertEqual(expected_result, result)
        self.assertEqual(9500.00, self.alone_trip.budget)

    def test_booking_status_family_trip_expect_success(self):
        self.family_trip.book_a_trip('Bulgaria')

        expected_result = """Booked Destination: Bulgaria
Paid Amount: 900.00
Number of Travelers: 2
Budget Left: 9100.00"""

        result = self.family_trip.booking_status()

        self.assertEqual(expected_result, result)
        self.assertEqual(9100.00, self.family_trip.budget)


if __name__ == '__main__':
    main()
