def sail_preparation_func(_city: str, _cities_dict: dict, _population: int, _gold: int):
    if _city not in _cities_dict:
        _cities_dict[_city] = [_population, _gold]  # population on index 0, gold on index 1
    else:
        _cities_dict[_city][0] += _population
        _cities_dict[_city][1] += _gold
    return _cities_dict


def plunder_func(_city: str, _cities_dict: dict, _population: int, _gold: int):
    print(f"{_city} plundered! {_gold} gold stolen, {_population} citizens killed.")
    _cities_dict[_city][0] -= _population
    _cities_dict[_city][1] -= _gold
    new_cities_dict = _cities_dict
    if _cities_dict[_city][0] <= 0 or _cities_dict[_city][1] <= 0:
        new_cities_dict = disband_city_func(_city, _cities_dict)
        print(f"{_city} has been wiped off the map!")
    return new_cities_dict


def prosper_func(_city: str, _cities_dict: dict, _gold: int):
    new_cities_dict = _cities_dict
    if _city in _cities_dict.keys():
        if _gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            _cities_dict[city][1] += _gold
            print(f"{_gold} gold added to the city treasury. {_city} now has {_cities_dict[city][1]} gold.")
            new_cities_dict = _cities_dict
    return new_cities_dict


def disband_city_func(_city: str, _cities_dict: dict):
    _cities_dict.pop(_city)
    new_cities_dict = _cities_dict
    return new_cities_dict


cities_dict = {}
city_info = input()
while city_info != 'Sail':
    city, population, gold = city_info.split('||')
    city_info = input()
    cities_dict = sail_preparation_func(city, cities_dict, int(population), int(gold))

command_lne = input()
while command_lne != 'End':
    if 'Plunder' in command_lne:
        command, city, population, gold = command_lne.split('=>')
        cities_dict = plunder_func(city, cities_dict, int(population), int(gold))
    elif 'Prosper' in command_lne:
        command, city, gold = command_lne.split('=>')
        cities_dict = prosper_func(city, cities_dict, int(gold))
    command_lne = input()

if not cities_dict:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f'Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:')
    [print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg') for k, v in cities_dict.items()]
