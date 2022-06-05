fire_cell_list = input().split('#')
water = int(input())
fire_levels_dictionary = {
    'High': {'min': 81,
             'max': 125
             },
    'Medium': {'min': 51,
               'max': 80
               },
    'Low': {'min': 1,
            'max': 50
            }
}
buff = 'Cells:'
total_effort = 0
total_fire = 0
for cell in fire_cell_list:
    current_value_list = cell.split(' = ')
    fire_type = current_value_list[0]
    cell_value = int(current_value_list[1])
    if fire_levels_dictionary[fire_type]['min'] <= cell_value <= fire_levels_dictionary[fire_type]['max']:
        if water >= cell_value:
            water -= cell_value
            total_effort += cell_value * 0.25
            buff += f'\n- {cell_value}'
            total_fire += cell_value
print(buff)
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
