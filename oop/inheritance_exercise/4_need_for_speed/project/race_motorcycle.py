from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)


ducati = RaceMotorcycle(50, 120)
print(ducati.DEFAULT_FUEL_CONSUMPTION)
print(ducati.fuel_consumption)
print(ducati.fuel)
ducati.drive(4)
print(ducati.fuel)