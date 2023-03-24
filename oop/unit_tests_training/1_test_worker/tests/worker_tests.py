from project.worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def test_name_salary_and_energy_are_correctly_initialized(self):
        worker = Worker('John Smith', 1000, 12)
        self.assertEqual(worker.name, 'John Smith')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 12)
        self.assertEqual(worker.money, 0)

    def test_energy_is_correctly_incremented_after_rest_is_called(self):
        worker = Worker('John Smith', 1000, 12)
        worker.rest()
        self.assertEqual(worker.energy, 13)

    def test_error_if_worker_works_with_zero_energy(self):
        worker = Worker('John Smith', 1000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_error_if_worker_works_with_negative_energy(self):
        worker = Worker('John Smith', 1000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_worker_money_increase_with_salary_when_working(self):
        worker = Worker('John Smith', 1000, 12)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_worker_energy_decreases_when_working(self):
        worker = Worker('John Smith', 1000, 12)
        worker.work()
        self.assertEqual(worker.energy, 11)

    def test_worker_get_info_returns_correct_value(self):
        worker = Worker('John Smith', 1000, 12)
        self.assertEqual(worker.get_info(), 'John Smith has saved 0 money.')


if __name__ == '__main__':
    unittest.main()