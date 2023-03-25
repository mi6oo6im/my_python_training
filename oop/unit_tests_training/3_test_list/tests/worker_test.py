from project.extended_list import IntegerList

import unittest


class ListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.some_list = IntegerList(1, 2, 3, 4, 5)

    def test_add_method_adds_element_and_returns_list(self):
        result = self.some_list.add(6)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_if_add_method_raises_value_error_for_non_integer_value(self):
        with self.assertRaises(ValueError) as context:
            self.some_list.add('Pesho')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_index_method_removes_the_element_and_returns_it(self):
        result = self.some_list.remove_index(3)
        self.assertEqual(result, 4)

    def test_remove_index_raises_error_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.some_list.remove_index(10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_if_initialisation_takes_only_integers_and_store_them(self):
        result = self.some_list.get_data()
        self.assertTrue(all([isinstance(x, int) for x in result]))

    def test_if_get_returns_the_element_on_the_index(self):
        result = self.some_list.get(3)
        self.assertEqual(result, 4)

    def test_if_get_raises_error_index_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.some_list.get(10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_if_insert_method_inserts_element_on_correct_index(self):
        self.some_list.insert(4, 7)
        result = self.some_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4, 7, 5])

    def test_if_insert_raises_index_error_for_index_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.some_list.insert(10, 10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_if_insert_raises_value_error_for_non_integer_value(self):
        with self.assertRaises(ValueError) as context:
            self.some_list.insert(4, 'Pesho')
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_if_get_biggest_returns_the_biggest_number(self):
        result = self.some_list.get_biggest()
        self.assertEqual(result, 5)

    def test_if_get_index_returns_the_correct_element_index(self):
        result = self.some_list.get_index(5)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
