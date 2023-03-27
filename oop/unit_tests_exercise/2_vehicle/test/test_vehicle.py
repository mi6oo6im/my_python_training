import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(40.5, 70.2)

    def test_correct_initialization(self):
        self.assertEqual(self.car.fuel, 40.5)
        self.assertEqual(self.car.capacity, 40.5)
        self.assertEqual(self.car.horse_power, 70.2)
        self.assertEqual(self.car.fuel_consumption, 1.25)

    def test_drive_decreases_fuel(self):
        self.car.drive(20)
        self.assertEqual(self.car.fuel, 15.5)

    def test_drive_raises_not_enough_fuel_error(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(100)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_increases_fuel_value(self):
        self.car.drive(20)
        self.car.refuel(25)
        self.assertEqual(self.car.fuel, 40.5)

    def test_refuel_raises_too_much_fuel_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(10)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_string_representation_is_correct(self):
        self.assertEqual(str(self.car), "The vehicle has 70.2 horse power with 40.5 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()
