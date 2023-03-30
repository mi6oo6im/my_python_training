import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Florian", 10, 100, 10)
        self.equal_enemy = Hero("Jon", 10, 100, 10)
        self.weaker_enemy = Hero("Denis", 7, 90, 2)
        self.stronger_enemy = Hero("The Mountain", 15, 200, 12)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "Florian")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 10)

    def test_battle_raises_exception_you_cannot_battle_yourself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_raise_value_error_when_health_is_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.equal_enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_raise_value_error_when_health_is_below_zero(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.equal_enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_raise_value_error_when_enemy_health_is_zero(self):
        self.equal_enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.equal_enemy)
        self.assertEqual(str(context.exception), "You cannot fight Jon. He needs to rest")

    def test_battle_raise_value_error_when_enemy_health_is_below_zero(self):
        self.equal_enemy.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.equal_enemy)
        self.assertEqual(str(context.exception), "You cannot fight Jon. He needs to rest")

    def test_draw_if_neither_health_is_equal_to_zero_and_decrease_health(self):
        result = self.hero.battle(self.equal_enemy)
        self.assertEqual(result, "Draw")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.equal_enemy.health, 0)

    def test_draw_if_neither_health_is_below_zero_and_decrease_health(self):
        self.hero.health = 10
        self.equal_enemy.health = 10
        result = self.hero.battle(self.equal_enemy)
        self.assertEqual(result, "Draw")
        self.assertEqual(self.hero.health, -90)
        self.assertEqual(self.equal_enemy.health, -90)

    def test_win_if_enemy_health_is_below_zero_and_stats_increase(self):
        result = self.hero.battle(self.weaker_enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 91)
        self.assertEqual(self.hero.damage, 15)

    def test_win_if_enemy_health_is_below_equal_to_zero_and_stats_increase(self):
        self.weaker_enemy.health = 100
        result = self.hero.battle(self.weaker_enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 91)
        self.assertEqual(self.hero.damage, 15)

    def test_loss_if_hero_health_is_below_zero_and_enemy_stats_increase(self):
        result = self.hero.battle(self.stronger_enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.stronger_enemy.level, 16)
        self.assertEqual(self.stronger_enemy.health, 105)

    def test_loss_if_hero_health_is_equal_to_zero(self):
        self.stronger_enemy.damage = 10
        result = self.hero.battle(self.stronger_enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.stronger_enemy.level, 16)
        self.assertEqual(self.stronger_enemy.health, 105)

    def test_correct_string_representation(self):
        result = str(self.hero)
        self.assertEqual(result, "Hero Florian: 10 lvl\nHealth: 100\nDamage: 10\n")


if __name__ == '__main__':
    unittest.main()
