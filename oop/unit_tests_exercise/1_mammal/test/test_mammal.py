from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Tony', "cat", 'Pr-r-r')

    def test_correct_initialization(self):
        self.assertEqual(self.mammal.name, 'Tony')
        self.assertEqual(self.mammal.type, 'cat')
        self.assertEqual(self.mammal.sound, 'Pr-r-r')
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_make_sound_returns_correct_string(self):
        self.assertEqual(self.mammal.make_sound(), "Tony makes Pr-r-r")

    def test_info_returns_correct_string(self):
        self.assertEqual(self.mammal.info(), "Tony is of type cat")


if __name__ == '__main__':
    unittest.main()