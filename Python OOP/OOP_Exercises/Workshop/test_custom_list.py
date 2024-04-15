from unittest import TestCase, main
from custom_list import CustomList
from custom_exceptions import EmptyListException


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.l = CustomList()

    def test_init(self):
        self.assertEqual([], self.l._CustomList__values)

    def test_add(self):
        self.l.append(5)

        self.assertEqual([5], self.l._CustomList__values)

    def test_add_element_to_multiple_existing_elements_collection(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual([1, 2, 3], self.l._CustomList__values)
        self.assertEqual(len(self.l._CustomList__values), 3)

        self.l.append(5)
        self.assertEqual([1, 2, 3, 5], self.l._CustomList__values)
        self.assertEqual(len(self.l._CustomList__values), 4)

        last_element = self.l._CustomList__values[-1]
        self.assertEqual(5, last_element)

    def test_add_returns_the_same_list(self):
        self.l._CustomList__values = [1, 2, 3]

        result = self.l.append(5)

        self.assertEqual(result, self.l._CustomList__values)

    def test_remove_type_of_index_is_not_integer_raises(self):
        invalid_args = [0.5, 'asd', [1, 23], {1: 2}]

        for arg in invalid_args:
            with self.assertRaises(TypeError) as te:
                self.l.remove(arg)
            self.assertEqual('Index must be of type integer', str(te.exception))

    def test_remove_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1

        with self.assertRaises(ValueError) as ve:
            self.l.remove(invalid_value)

        self.assertEqual('Integer must be 0 or positive', str(ve.exception))

    def test_remove_index_is_not_in_array_boundary_raises(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(3, len(self.l._CustomList__values))

        index_out_of_range = [3, 4]
        for index in index_out_of_range:
            with self.assertRaises(IndexError) as ie:
                self.l.remove(index)
            self.assertEqual('Index is out of range', str(ie.exception))

    def test_remove_value_from_valid_index(self):
        self.l._CustomList__values = [1, 2, 3, 1]
        self.assertEqual([1, 2, 3, 1], self.l._CustomList__values)

        result = self.l.remove(0)

        self.assertEqual([2, 3, 1], self.l._CustomList__values)
        self.assertEqual(1, result)

    def test_get_type_of_index_is_not_integer_raises(self):
        invalid_args = [0.5, 'asd', [1, 23], {1: 2}]

        for arg in invalid_args:
            with self.assertRaises(TypeError) as te:
                self.l.get(arg)
            self.assertEqual('Index must be of type integer', str(te.exception))

    def test_get_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1

        with self.assertRaises(ValueError) as ve:
            self.l.get(invalid_value)

        self.assertEqual('Integer must be 0 or positive', str(ve.exception))

    def test_get_index_is_not_in_array_boundary_raises(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(3, len(self.l._CustomList__values))

        index_out_of_range = [3, 4]
        for index in index_out_of_range:
            with self.assertRaises(IndexError) as ie:
                self.l.get(index)
            self.assertEqual('Index is out of range', str(ie.exception))

    def test_get_element_index_returns_element(self):
        self.l._CustomList__values = [1, 2, 3]

        result = self.l.get(0)

        self.assertEqual(result, 1)

    def test_extend_args_is_not_iterable_raises_value_error(self):
        self.l._CustomList__values = [1, 2, 3, 1]
        self.assertEqual([1, 2, 3, 1], self.l._CustomList__values)

        not_iterable_values = [1, 1.1]

        for value in not_iterable_values:
            with self.assertRaises(ValueError) as ve:
                self.l.extend(value)
            self.assertEqual('Value is not iterable', str(ve.exception))

        self.assertEqual([1, 2, 3, 1], self.l._CustomList__values)

    def test_extend_extends_list_with_values_by_unpacking_them(self):
        self.l._CustomList__values = [1, 2, 3, 1]
        self.assertEqual([1, 2, 3, 1], self.l._CustomList__values)

        result = self.l.extend([3, 4])

        self.assertEqual([1, 2, 3, 1, 3, 4], result)
        self.assertIs(self.l._CustomList__values, result)

    def test_insert_type_of_index_is_not_integer_raises(self):
        invalid_args = [0.5, 'asd', [1, 23], {1: 2}]

        for arg in invalid_args:
            with self.assertRaises(TypeError) as te:
                self.l.insert(arg, 5)
            self.assertEqual('Index must be of type integer', str(te.exception))

    def test_insert_index_argument_is_not_positive_or_zero_integer_raises(self):
        invalid_value = -1

        with self.assertRaises(ValueError) as ve:
            self.l.insert(invalid_value, 5)

        self.assertEqual('Integer must be 0 or positive', str(ve.exception))

    def test_insert_index_is_not_in_array_boundary_raises(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(3, len(self.l._CustomList__values))

        index_out_of_range = [3, 4]
        for index in index_out_of_range:
            with self.assertRaises(IndexError) as ie:
                self.l.insert(index, 5)
            self.assertEqual('Index is out of range', str(ie.exception))

    def test_insert_adds_value_at_correct_index(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(3, len(self.l._CustomList__values))

        result = self.l.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.l._CustomList__values)
        self.assertIs(result, self.l._CustomList__values)

        result = self.l.insert(2, 100)
        self.assertEqual([5, 1, 100, 2, 3], self.l._CustomList__values)
        self.assertIs(result, self.l._CustomList__values)

    def test_pop_empty_list_raises_empty_list_exception(self):
        self.assertEqual([], self.l._CustomList__values)

        with self.assertRaises(EmptyListException) as ele:
            self.l.pop()
        self.assertEqual("List is empty", str(ele.exception))

    def test_pop_last_element_leaves_list_empty(self):
        self.l._CustomList__values = [1]
        self.assertEqual([1], self.l._CustomList__values)

        result = self.l.pop()
        self.assertEqual(1, result)

        self.assertEqual([], self.l._CustomList__values)

    def test_pop_only_last_element(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.pop()
        self.assertEqual(100, result)
        self.assertEqual([1, 2], self.l._CustomList__values)

    def test_clear_empty_list_raises_empty_list_exception(self):
        self.assertEqual([], self.l._CustomList__values)

        with self.assertRaises(EmptyListException) as ele:
            self.l.clear()
        self.assertEqual("Cannot clear an empty list", str(ele.exception))

    def test_clear_delete_all_elements(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.clear()

        self.assertIsNone(result)
        self.assertEqual([], self.l._CustomList__values)

    def test_index_value_does_not_exist_raises_value_error(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        with self.assertRaises(ValueError) as ve:
            self.l.index(3)

        self.assertEqual('Value is not in the list', str(ve.exception))

    def test_index_returns_first_occurrence_of_the_value(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.index(100)
        self.assertEqual(2, result)
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

    def test_count_value_is_not_in_the_list_returns_zero(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.count(5)
        self.assertEqual(0, result)

    def test_count_value_returns_count(self):
        self.l._CustomList__values = [1, 2, 100, 2]
        self.assertEqual([1, 2, 100, 2], self.l._CustomList__values)

        result = self.l.count(2)
        self.assertEqual(2, result)

    def test_reverse_empty_list(self):
        self.assertEqual([], self.l._CustomList__values)

        with self.assertRaises(EmptyListException) as ele:
            self.l.reverse()

        self.assertEqual("List is empty", str(ele.exception))

    def test_reverse_returns_new_list_with_reversed_value_order(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.reverse()
        self.assertEqual([100, 2, 1], result)

        self.assertIsNot(result, self.l._CustomList__values)

    def test_copy_empty_list(self):
        self.assertEqual([], self.l._CustomList__values)

        with self.assertRaises(EmptyListException) as ele:
            self.l.copy()

        self.assertEqual("We can't copy an empty list", str(ele.exception))

    def test_copy_returns_same_values_different_list(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.copy()

        self.assertEqual([1, 2, 100], result)
        self.assertIsNot(result, self.l._CustomList__values)

    def test_size_empty_list_returns_zero(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.size()
        self.assertEqual(0, result)

    def test_size_returns_length(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.size()
        self.assertEqual(3, result)

    def test_add_first_empty_list_ends_up_with_one_element(self):
        self.assertEqual([], self.l._CustomList__values)

        self.l.add_first(5)

        self.assertEqual([5], self.l._CustomList__values)

    def test_add_first_list_ends_up_with_element_at_index_zero(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        self.l.add_first(5)
        self.assertEqual([5, 1, 2, 100], self.l._CustomList__values)

    def test_dictionize_empty_list_returns_empty_dict(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.dictionize()

        self.assertDictEqual({}, result)

    def test_dictionize_odd_count_append_space_as_value(self):
        self.l._CustomList__values = [1, 2, 100]
        self.assertEqual([1, 2, 100], self.l._CustomList__values)

        result = self.l.dictionize()

        self.assertDictEqual({1: 2, 100: ' '}, result)

    def test_dictionize_even_count_returns_dict(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.dictionize()

        self.assertDictEqual({1: 2, 100: 5}, result)

    def test_move_empty_list_raises_error(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.move(2)

        self.assertIs(self.l._CustomList__values, result)
        self.assertEqual([], result)

    def test_move(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.move(2)
        self.assertEqual([100, 5, 1, 2], self.l._CustomList__values)
        self.assertIs(self.l._CustomList__values, result)

    def test_move_zero_does_not_change_list(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.move(0)
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)
        self.assertIs(self.l._CustomList__values, result)

    def test_move_with_length_of_the_list_does_not_change_list(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.move(len(self.l._CustomList__values))
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)
        self.assertIs(self.l._CustomList__values, result)

    def test_move_length_plus_one_of_the_list_does_not_change_list(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.move(len(self.l._CustomList__values) + 1)
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)
        self.assertIs(self.l._CustomList__values, result)

    def test_move_invalid_or_negative_integer_raises_value_error(self):
        self.assertEqual([], self.l._CustomList__values)
        invalid_args = [0.5, 'asd', [1, 23], {1: 2}, -1]

        for arg in invalid_args:
            with self.assertRaises(ValueError) as ve:
                self.l.move(arg)

            self.assertEqual('Value is not a valid int', str(ve.exception))

    def test_sum_empty_list_returns_zero(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.sum()

        self.assertEqual(0, result)
        self.assertEqual([], self.l._CustomList__values)

    def test_sum_only_numeric(self):
        self.l._CustomList__values = [1, 2, 100, 5]
        self.assertEqual([1, 2, 100, 5], self.l._CustomList__values)

        result = self.l.sum()
        self.assertEqual(108, result)

    def test_sum_non_numeric_returns_lens_amount(self):
        self.l._CustomList__values = [1, 2, 100, 5, 'asd', (1, 2), [1, 2, 3], {1: 2}]
        self.assertEqual([1, 2, 100, 5, 'asd', (1, 2), [1, 2, 3], {1: 2}], self.l._CustomList__values)

        result = self.l.sum()
        self.assertEqual(117, result)

    def test_overbound_empty_list(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.overbound()

        self.assertEqual(None, result)
        self.assertEqual([], self.l._CustomList__values)

    def test_overbound_only_numeric(self):
        self.l._CustomList__values = [100, 2, 100, 5]
        self.assertEqual([100, 2, 100, 5], self.l._CustomList__values)

        result = self.l.overbound()

        self.assertEqual(0, result)
        self.assertEqual([100, 2, 100, 5], self.l._CustomList__values)

    def test_overbound_numeric_and_other_iterables(self):
        self.l._CustomList__values = [1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}]
        self.assertEqual([1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}], self.l._CustomList__values)

        result = self.l.overbound()
        self.assertEqual(2, result)
        self.assertEqual([1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}], self.l._CustomList__values)

    def test_underbound_empty_list(self):
        self.assertEqual([], self.l._CustomList__values)

        result = self.l.underbound()

        self.assertEqual(None, result)
        self.assertEqual([], self.l._CustomList__values)

    def test_underbound_only_numeric(self):
        self.l._CustomList__values = [100, 2, 100, 5]
        self.assertEqual([100, 2, 100, 5], self.l._CustomList__values)

        result = self.l.underbound()

        self.assertEqual(1, result)
        self.assertEqual([100, 2, 100, 5], self.l._CustomList__values)

    def test_underbound_numeric_and_other_iterables(self):
        self.l._CustomList__values = [1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}]
        self.assertEqual([1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}], self.l._CustomList__values)

        result = self.l.underbound()
        self.assertEqual(0, result)
        self.assertEqual([1, 2, 'asd', (1, 2), [1, 2, 3], {1: 2}], self.l._CustomList__values)


if __name__ == '__main__':
    main()