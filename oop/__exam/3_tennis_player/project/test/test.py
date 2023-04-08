from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTest(TestCase):
    def setUp(self) -> None:
        self.player1 = TennisPlayer("Player1", 18, 10.0)
        self.player2 = TennisPlayer("Player2", 19, 8.0)

    def test_correct_initialization(self):
        self.assertEqual(self.player1.name, "Player1")
        self.assertEqual(self.player1.age, 18)
        self.assertEqual(self.player1.points, 10.0)
        self.assertEqual(self.player1.wins, [])
        self.assertIsInstance(self.player1.wins, list)

    def test_name_with_2_or_less_chars_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.name = 'A'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.player1.name = 'A1'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_age_less_than_18_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 10
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_returns_string_if_tournament_already_won(self):
        self.player1.add_new_win('Tournament1')
        result = self.player1.add_new_win('Tournament1')
        self.assertEqual(result, "Tournament1 has been already added to the list of wins!")

    def test_add_new_win_adds_tournament_in_list_of_wins(self):
        result = self.player1.add_new_win('Tournament1')
        self.assertEqual(result, None)
        self.assertEqual(self.player1.wins, ['Tournament1'])

    def test_less_than_returns_correct_string_for_less_points(self):
        self.player1.points = 5
        self.player2.points = 10
        result = self.player1 < self.player2
        self.assertEqual(result, 'Player2 is a top seeded player and he/she is better than Player1')

    def test_less_than_returns_correct_string_for_more_points(self):
        self.player1.points = 10
        self.player2.points = 5
        result = self.player1 < self.player2
        self.assertEqual(result, 'Player1 is a better player than Player2')

    def test_correct_string_representation(self):
        result = str(self.player1)
        self.assertEqual(result, "Tennis Player: Player1\n"
                                 "Age: 18\n"
                                 "Points: 10.0\n"
                                 "Tournaments won: ")

    def test_correct_string_representation_with_wins(self):
        self.player1.add_new_win('Tournament1')
        self.player1.add_new_win('Tournament2')
        result = str(self.player1)
        self.assertEqual(result, "Tennis Player: Player1\n"
                                 "Age: 18\n"
                                 "Points: 10.0\n"
                                 "Tournaments won: Tournament1, Tournament2")


if __name__ == '__main__':
    main()
