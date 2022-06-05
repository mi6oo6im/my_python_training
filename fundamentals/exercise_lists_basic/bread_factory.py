energy = 100
coins = 100
work_day_events_list = input().split('|')
day_is_completed = True
for event in work_day_events_list:
    event_list = event.split('-')
    event_or_ingredient = event_list[0]
    value = int(event_list[1])
    if event_or_ingredient == 'rest':
        if energy + value > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += value
            gained_energy = value
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_or_ingredient == 'order':
        if energy >= 30:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= value:
            coins -= value
            print(f'You bought {event_or_ingredient}.')
        else:
            print(f'Closed! Cannot afford {event_or_ingredient}.')
            day_is_completed = False
            break
if day_is_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
