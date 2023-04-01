from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTest(TestCase):
    def setUp(self) -> None:
        self.trucker = TruckDriver("SomeName", 1)

    def test_correct_initialization(self):
        self.assertEqual(self.trucker.name, "SomeName")
        self.assertEqual(self.trucker.money_per_mile, 1)
        self.assertIsInstance(self.trucker.available_cargos, dict)
        self.assertEqual(self.trucker.available_cargos, {})
        self.assertEqual(self.trucker.earned_money, 0)
        self.assertEqual(self.trucker.miles, 0)

    def test_negative_earned_money_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.trucker.earned_money = -1
        self.assertEqual(str(ex.exception), "SomeName went bankrupt.")

    def test_positive_earned_money(self):
        self.assertEqual(self.trucker.earned_money, 0)
        self.trucker.earned_money = 5
        self.assertEqual(self.trucker.earned_money, 5)

    def test_add_cargo_offer_raises_exception_if_already_added(self):
        self.trucker.add_cargo_offer("Location_1", 100)
        with self.assertRaises(Exception) as ex:
            self.trucker.add_cargo_offer("Location_1", 100)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_returns_correct_string_and_adds_to_available_cargos(self):
        result = self.trucker.add_cargo_offer("Location_1", 100)
        self.assertEqual(result, "Cargo for 100 to Location_1 was added as an offer.")

    def test_drive_best_cargo_offer_raises_value_if_there_are_no_offers(self):
        result = self.trucker.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_returns_correct_string_and_adds_miles_and_money(self):
        self.trucker.add_cargo_offer("Location_1", 100)
        self.trucker.add_cargo_offer("Location_2", 300)
        self.trucker.add_cargo_offer("Location_3", 200)
        result = self.trucker.drive_best_cargo_offer()
        self.assertEqual(result, "SomeName is driving 300 to Location_2.")
        self.assertEqual(self.trucker.earned_money, 280)
        self.assertEqual(self.trucker.miles, 300)

    def test_eat(self):
        self.trucker.earned_money = 100
        self.trucker.eat(250)
        self.assertEqual(self.trucker.earned_money, 80)

    def test_sleep(self):
        self.trucker.earned_money = 100
        self.trucker.sleep(1000)
        self.assertEqual(self.trucker.earned_money, 55)

    def test_pump_gas(self):
        self.trucker.earned_money = 1000
        self.trucker.pump_gas(1500)
        self.assertEqual(self.trucker.earned_money, 500)

    def test_repair_truck(self):
        self.trucker.earned_money = 10_000
        self.trucker.repair_truck(10_000)
        self.assertEqual(self.trucker.earned_money, 2500)

    def test_check_for_activities(self):
        self.trucker.check_for_activities(0)
        self.assertEqual(self.trucker.earned_money, 0)

    def test_drive_best_cargo_offer_with_check_for_activities(self):
        self.trucker.earned_money = 1760
        self.trucker.add_cargo_offer("Location_1", 100)
        self.trucker.add_cargo_offer("Location_2", 10_000)
        self.trucker.add_cargo_offer("Location_3", 200)
        self.trucker.drive_best_cargo_offer()
        self.assertEqual(self.trucker.earned_money, 10)

    def test_correct__repr__(self):
        self.assertEqual(str(self.trucker), "SomeName has 0 miles behind his back.")
        self.assertEqual(repr(self.trucker), "SomeName has 0 miles behind his back.")
        self.assertEqual(repr(self.trucker), repr(self.trucker))


if __name__ == '__main__':
    main()
