def rate_func(_plants_dict: dict, _plant: str, _rating: int):
    if _plant in _plants_dict.keys():
        _plants_dict[_plant].append(_rating)
    else:
        print('error')
    return _plants_dict


def update_func(_plants_dict: dict, _plant: str, _new_rarity: str):
    if _plant in _plants_dict.keys():
        _plants_dict[plant] = _new_rarity
    else:
        print('error')
    return _plants_dict


def reset_func(_plants_dict: dict, _plant: str):
    if _plant in _plants_dict.keys():
        _plants_dict[_plant] = []
    else:
        print('error')
    return _plants_dict


number_of_plants = int(input())
plants_rarity = {}
plants_rating = {}
for _ in range(number_of_plants):
    input_line = input()
    plant, rarity = input_line.split('<->')
    plants_rarity[plant] = rarity
    plants_rating[plant] = []

command_line = input()
while command_line != 'Exhibition':
    if 'Rate' in command_line:
        plant, rating = command_line.replace('Rate: ', '').split(' - ')
        plants_rating = rate_func(plants_rating, plant, int(rating))
    elif 'Update' in command_line:
        plant, new_rarity = command_line.replace('Update: ', '').split(' - ')
        plants_rarity = update_func(plants_rarity, plant, new_rarity)
    elif 'Reset' in command_line:
        plant = command_line.replace('Reset: ', '')
        plants_rating = reset_func(plants_rating, plant)
    command_line = input()
if plants_rarity and plants_rating:
    print("Plants for the exhibition:")
    for k, v in plants_rarity.items():
        plant = k
        rarity = v
        if plants_rating[plant]:
            rating = sum(plants_rating[plant]) / len(plants_rating[plant])
            print(f'- {plant}; Rarity: {rarity}; Rating: {rating:.2f}')
        else:
            print(f'- {plant}; Rarity: {rarity}; Rating: {0:.2f}')
