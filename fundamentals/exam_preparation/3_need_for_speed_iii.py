def drive_func(_car_mileage_dict: dict, _car_fuel_dict: dict, _car: str, _distance: int, _fuel: int):
    if _car in _car_mileage_dict.keys():
        current_fuel = _car_fuel_dict[car]
        if current_fuel < _fuel:
            print("Not enough fuel to make that ride")
        else:
            _car_fuel_dict[car] -= _fuel
            _car_mileage_dict[car] += _distance
            print(f"{_car} driven for {_distance} kilometers. {_fuel} liters of fuel consumed.")
            if _car_mileage_dict[car] >= maximum_mileage:
                print(f"Time to sell the {_car}!")
                _car_mileage_dict.pop(_car)
                _car_fuel_dict.pop(_car)
    return _car_mileage_dict, _car_fuel_dict


def refuel_func(_car_fuel_dict: dict, _car: str, _fuel: int):
    if _car in _car_fuel_dict.keys():
        current_fuel = _car_fuel_dict[_car]
        if current_fuel <= maximum_fuel - _fuel:
            _car_fuel_dict[_car] += _fuel
        else:
            _fuel = maximum_fuel - current_fuel
            _car_fuel_dict[_car] = maximum_fuel
    print(f"{_car} refueled with {_fuel} liters")
    return _car_fuel_dict


def revert_func(_car_mileage_dict: dict, _car: str, _kilometers: int):
    if _car in _car_mileage_dict.keys():
        current_mileage = _car_mileage_dict[_car]
        if current_mileage - minimum_mileage < _kilometers:
            _car_mileage_dict[car] = minimum_mileage
        else:
            print(f"{_car} mileage decreased by {_kilometers} kilometers")
            _car_mileage_dict[car] -= _kilometers
    return _car_mileage_dict


number_of_cars = int(input())
car_mileage_dict = {}
car_fuel_dict = {}
maximum_fuel = 75
minimum_mileage = 10000
maximum_mileage = 100000
for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    car_mileage_dict[car] = int(mileage)
    car_fuel_dict[car] = int(fuel)
command_line = input()
while command_line != 'Stop':
    if 'Drive' in command_line:
        command, car, distance, fuel = command_line.split(' : ')
        car_mileage_dict, car_fuel_dict = drive_func(car_mileage_dict, car_fuel_dict, car, int(distance), int(fuel))
    elif 'Refuel' in command_line:
        command, car, fuel = command_line.split(' : ')
        car_fuel_dict = refuel_func(car_fuel_dict, car, int(fuel))
    elif 'Revert' in command_line:
        command, car, kilometers = command_line.split(' : ')
        car_mileage_dict = revert_func(car_mileage_dict, car, int(kilometers))
    command_line = input()
if car_mileage_dict and car_fuel_dict:
    for k, v in car_mileage_dict.items():
        print(f"{k} -> Mileage: {v} kms, Fuel in the tank: {car_fuel_dict[k]} lt.")
