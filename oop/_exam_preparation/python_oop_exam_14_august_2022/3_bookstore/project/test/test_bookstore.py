from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.books = Bookstore(10)

    def test_correct_init_(self):
        self.assertEqual(self.books.books_limit, 10)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {})
        self.assertIsInstance(self.books.availability_in_store_by_book_titles, dict)
        self.assertEqual(self.books.total_sold_books, 0)
        self.assertEqual(self.books._Bookstore__total_sold_books, 0)

    def test_total_sold_books_return_correct_value(self):
        self.assertEqual(self.books.total_sold_books, 0)

    def test_books_limit_returns_correct_value(self):
        self.books.books_limit = 12
        self.assertEqual(self.books.books_limit, 12)

    def test_book_limit_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.books.books_limit = -1
        self.assertEqual(str(ex.exception), "Books limit of -1 is not valid")

    def test_book_limit_zero_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.books.books_limit = 0
        self.assertEqual(str(ex.exception), "Books limit of 0 is not valid")

    def test_len_returns_number_of_books_available(self):
        self.books.availability_in_store_by_book_titles = {"Great Gatsby": 12}
        result = len(self.books)
        self.assertEqual(result, 12)

    def test_receive_book_raises_exception_if_not_enough_room(self):
        with self.assertRaises(Exception) as ex:
            self.books.receive_book("1001 nights", 12)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {})
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_that_is_available_already_adds_qty_and_returns_correctly(self):
        self.books.availability_in_store_by_book_titles = {"101 Dalmatians": 4}
        result = self.books.receive_book("101 Dalmatians", 6)
        self.assertEqual(self.books.availability_in_store_by_book_titles["101 Dalmatians"], 10)
        self.assertEqual(result, "10 copies of 101 Dalmatians are available in the bookstore.")

    def test_receive_book_new_to_the_bookstore_returns_correctly(self):
        self.books.availability_in_store_by_book_titles = {"1001 nights": 2}
        self.assertEqual(self.books.availability_in_store_by_book_titles, {"1001 nights": 2})
        result = self.books.receive_book("101 Dalmatians", 6)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {"1001 nights": 2, "101 Dalmatians": 6})
        self.assertEqual(result, "6 copies of 101 Dalmatians are available in the bookstore.")
        self.assertEqual(len(self.books), 8)

    def test_sell_book_raises_exception_if_the_book_is_unavailable(self):
        with self.assertRaises(Exception) as ex:
            self.books.sell_book("Pinocchio", 3)
        self.assertEqual(str(ex.exception), "Book Pinocchio doesn't exist!")

    def test_sell_book_raises_exception_if_insufficient_quantity(self):
        self.books.availability_in_store_by_book_titles = {"Pinocchio": 2}
        with self.assertRaises(Exception) as ex:
            self.books.sell_book("Pinocchio", 3)
        self.assertEqual(str(ex.exception), "Pinocchio has not enough copies to sell. Left: 2")

    def test_sell_book_successful_returns_correct_string_removes_the_sold_quantity_and_adds_to_sold_books(self):
        self.books.availability_in_store_by_book_titles = {"Pinocchio": 5, "101 Dalmatians": 4}
        result = self.books.sell_book("Pinocchio", 3)
        self.assertEqual(result, "Sold 3 copies of Pinocchio")
        self.assertEqual(self.books.total_sold_books, 3)
        self.books.sell_book("101 Dalmatians", 2)
        self.assertEqual(self.books.total_sold_books, 5)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {"Pinocchio": 2, "101 Dalmatians": 2})
        self.assertEqual(len(self.books), 4)
        self.books.sell_book("Pinocchio", 2)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {"Pinocchio": 0, "101 Dalmatians": 2})
        self.assertEqual(self.books.total_sold_books, 7)
        self.assertEqual(len(self.books), 2)

    def test_correct_str_(self):
        self.books.availability_in_store_by_book_titles = {"Pinocchio": 5, "101 Dalmatians": 4}
        self.books.sell_book("Pinocchio", 3)
        expected = "Total sold books: 3\n" \
                   "Current availability: 6\n" \
                   " - Pinocchio: 2 copies\n" \
                   " - 101 Dalmatians: 4 copies"
        self.assertEqual(str(self.books), expected)


if __name__ == '__main__':
    main()
