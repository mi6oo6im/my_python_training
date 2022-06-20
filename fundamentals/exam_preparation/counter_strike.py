def counter_strike_func(energy_level: int):
    command = input()
    confirmed_kills = 0
    while command != 'End of battle':
        distance_to_cover = int(command)
        if energy_level >= distance_to_cover:
            energy_level -= distance_to_cover
            confirmed_kills += 1
            if confirmed_kills % 3 == 0:
                energy_level += confirmed_kills
        else:
            print(f'Not enough energy! Game ends with {confirmed_kills} won battles and {energy_level} energy')
            break
        command = input()
    else:
        print(f'Won battles: {confirmed_kills}. Energy left: {energy_level}')


initial_energy = int(input())
counter_strike_func(initial_energy)
