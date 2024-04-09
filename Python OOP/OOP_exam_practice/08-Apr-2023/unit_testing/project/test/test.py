from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Iliyan', 22, 100.0)
        self.player2 = TennisPlayer('Darin', 22, 95.0)

    def test_correct_init(self):
        self.assertEqual('Iliyan', self.player.name)
        self.assertEqual(22, self.player.age)
        self.assertEqual(100.0, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_wrong_name_init_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.new_player = TennisPlayer('aa', 22, 100)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_wrong_age_init_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.new_player = TennisPlayer('aaa', 17, 100)

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_expect_tournament_already_added(self):
        self.player.wins.append('Bulgaria1')

        expected_result = f"Bulgaria1 has been already added to the list of wins!"
        result = self.player.add_new_win('Bulgaria1')

        self.assertEqual(expected_result, result)

    def test_add_new_win_expect_success(self):
        self.player.wins.append('Bulgaria1')

        self.assertEqual(["Bulgaria1"], self.player.wins)

    def test_less_than_method(self):
        expected_result1 = f'Iliyan is a top seeded player and he/she is better than Darin'
        expected_result2 = f'Iliyan is a better player than Darin'

        result1 = self.player2 < self.player
        result2 = self.player < self.player2

        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)

    def test_str_method(self):
        self.player.wins = ['Bulgaria1', 'Wimboldom']

        expected_result = f"Tennis Player: Iliyan\n" + \
                          f"Age: 22\n" + \
                          f"Points: 100.0\n" + \
                          f"Tournaments won: Bulgaria1, Wimboldom"

        result = self.player.__str__()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
