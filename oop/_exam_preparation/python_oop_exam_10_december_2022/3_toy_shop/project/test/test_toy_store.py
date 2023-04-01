from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoryTest(TestCase):

    def setUp(self) -> None:
        self.toy_shop = ToyStore()

    def test_correct_initialisation(self):
        for shelf in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.toy_shop.toy_shelf[chr(shelf)])

    def test_add_toy_shelf_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shop.add_toy('X', 'Some Toy')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_on_shelf_where_the_toy_already_is_raises_exception(self):
        self.toy_shop.add_toy('A', 'Some Toy')
        with self.assertRaises(Exception) as ex:
            self.toy_shop.add_toy('A', 'Some Toy')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_on_occupied_shelf_raises_exception(self):
        self.toy_shop.add_toy('A', 'Some Toy')
        with self.assertRaises(Exception) as ex:
            self.toy_shop.add_toy('A', 'Another Toy')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_successful_add_toy_adds_the_toy_and_returns_string(self):
        result = self.toy_shop.add_toy('A', 'Some Toy')
        self.assertEqual(result, "Toy:Some Toy placed successfully!")
        self.assertEqual(self.toy_shop.toy_shelf["A"], 'Some Toy')

    def test_remove_toy_raises_exception_if_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shop.remove_toy('X', 'Some Toy')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_raises_exception_if_toy_to_remove_is_not_on_the_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shop.remove_toy('A', 'Some Toy')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successful_removes_the_toy_and_returns_string(self):
        self.toy_shop.add_toy('A', 'Some Toy')
        result = self.toy_shop.remove_toy('A', 'Some Toy')
        self.assertEqual(result, "Remove toy:Some Toy successfully!")
        self.assertEqual(self.toy_shop.toy_shelf["A"], None)


if __name__ == '__main__':
    main()
