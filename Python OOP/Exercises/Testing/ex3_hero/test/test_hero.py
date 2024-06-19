from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Hero', 10, 200.0, 15.0)
        self.enemy = Hero('Enemy', 8, 100.0, 10.0)

    def test_correct_init(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(200.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

    def test_fight_hero_with_himself_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_is_lower_or_equal_to_zero_raises_exception(self):
        self.hero.health = 0
        expected_result = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_battle_if_enemy_health_is_lower_or_equal_to_zero_raises_exception(self):
        self.enemy.health = 0
        expected_result = "You cannot fight Enemy. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_result, str(ve.exception))

    def test_battle_both_health_bars_are_equal_or_below_zero_expect_draw(self):
        self.enemy.damage = 30

        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_battle_enemy_Health_bar_is_equal_or_below_zero_expect_win_and_increases_stats(self):
        self.assertEqual('You win', self.hero.battle(self.enemy))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(125, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_enemy_is_not_defeated_expect_you_lose_and_enemy_increase_stats(self):
        self.enemy.health = 200

        self.assertEqual('You lose', self.hero.battle(self.enemy))
        self.assertEqual(9, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_string_method(self):
        expected_result = "Hero Hero: 10 lvl\n" \
               "Health: 200.0\n" \
               "Damage: 15.0\n"
        result = self.hero.__str__()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()