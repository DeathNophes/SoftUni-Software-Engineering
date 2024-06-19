from unittest import TestCase, main
from ex3_list.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.i_list = IntegerList(5.5, 1, 2, 3, 'hello')

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_add_non_int_value_to_the_list_raises_value_error(self):

        with self.assertRaises(ValueError) as v:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(v.exception))

    def test_add_int_to_the_list(self):
        expected_list = self.i_list.get_data().copy() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_index_with_out_of_range_index_raises_index_error(self):

        with self.assertRaises(IndexError) as i:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(i.exception))

    def test_remove_index_with_valid_index(self):
        self.i_list.remove_index(1)
        self.assertEqual([1, 3], self.i_list.get_data())

    def test_get_out_of_range_index(self):

        with self.assertRaises(IndexError) as i:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(i.exception))

    def test_get_with_valid_index_returns_value_on_index(self):
        result = self.i_list.get(1)

        self.assertEqual(2, result)

    def test_insert_on_invalid_index_raises_index_error(self):

        with self.assertRaises(IndexError) as i:
            self.i_list.insert(1000, 5)

        self.assertEqual("Index is out of range", str(i.exception))

    def test_insert_on_valid_index_non_integer_raises_value_error(self):

        with self.assertRaises(ValueError) as v:
            self.i_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(v.exception))

    def test_insert_integer_on_valid_index(self):
        expected_list = self.i_list.get_data().copy()
        expected_list.insert(1, 5)
        self.i_list.insert(1, 5)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_get_biggest_number(self):
        result = self.i_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.i_list.get_index(1)

        self.assertEqual(0, result)


if __name__ == '__main__':
    main()