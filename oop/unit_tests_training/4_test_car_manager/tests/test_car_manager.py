import importlib
import unittest

my_module = importlib.import_module('.car_manager', 'project')


class CarManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.some_car = my_module.Car("Honda", "Civic", 7, 60)

    def test_initialization_is_correct(self):
        self.assertEqual(self.some_car.make, 'Honda')
        self.assertEqual(self.some_car.model, 'Civic')
        self.assertEqual(self.some_car.fuel_consumption, 7)
        self.assertEqual(self.some_car.fuel_capacity, 60)
        self.assertEqual(self.some_car.fuel_amount, 0)

    def test_make_cannot_be_null_or_empty_exception(self):
        with self.assertRaises(Exception) as context:
            self.some_car.make = ''
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_cannot_be_null_or_empty_exception(self):
        with self.assertRaises(Exception) as context:
            self.some_car.model = ''
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_capacity_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            self.some_car.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_cannot_negative(self):
        with self.assertRaises(Exception) as context:
            self.some_car.fuel_capacity = -1
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_consumption_cannot_be_zero(self):
        with self.assertRaises(Exception) as context:
            self.some_car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_cannot_negative(self):
        with self.assertRaises(Exception) as context:
            self.some_car.fuel_consumption = -1
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_amount_cannot_negative(self):
        with self.assertRaises(Exception) as context:
            self.some_car.fuel_amount = -1
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_increases_fuel_amount(self):
        self.some_car.refuel(10)
        self.assertEqual(self.some_car.fuel_amount, 10)

    def test_refuel_raises_error_for_zero(self):
        with self.assertRaises(Exception) as context:
            self.some_car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_raises_error_for_negative(self):
        with self.assertRaises(Exception) as context:
            self.some_car.refuel(-1)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_increases_fuel_amount_up_to_capacity(self):
        self.some_car.refuel(70)
        self.assertEqual(self.some_car.fuel_amount, 60)

    def test_drive_consumes_fuel(self):
        self.some_car.refuel(60)
        self.some_car.drive(100)
        self.assertEqual(self.some_car.fuel_amount, 53)

    def test_drive_raises_error_for_insufficient_fuel(self):
        with self.assertRaises(Exception) as context:
            self.some_car.drive(10)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
