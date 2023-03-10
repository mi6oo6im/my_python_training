from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    _additional_fuel_consumption = 0.9
    _fuel_refill_coefficient = 1

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        consumption = self.fuel_consumption + self._additional_fuel_consumption
        fuel_needed = consumption * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += self._fuel_refill_coefficient * fuel


class Truck(Vehicle):
    _additional_fuel_consumption = 1.6
    _fuel_refill_coefficient = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        consumption = self.fuel_consumption + self._additional_fuel_consumption
        fuel_needed = consumption * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += self._fuel_refill_coefficient * fuel


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

