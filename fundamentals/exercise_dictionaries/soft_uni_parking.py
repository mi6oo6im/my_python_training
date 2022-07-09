def register_func(parking: dict, username: str, license_plate_number: str):
    if username in parking:
        print(f'ERROR: already registered with plate number {license_plate_number}')
    else:
        print(f'{username} registered {license_plate_number} successfully')
        parking[username] = license_plate_number
    return parking


def unregister_func(parking: dict, username: str):
    if username not in parking:
        print(f'ERROR: user {username} not found')
    else:
        print(f'{username} unregistered successfully')
        parking.pop(username)
    return parking


def get_parking_data_func(parking: dict):
    [print(f'{k} => {v}') for k, v in parking.items()]


commands = int(input())
garage_dict = {}
for _ in range(commands):
    command_line = input().split()
    command = command_line[0]
    if command == 'register':
        user = command_line[1]
        reg_num = command_line[2]
        garage_dict = register_func(garage_dict, user, reg_num)
    elif command == 'unregister':
        user = command_line[1]
        garage_dict = unregister_func(garage_dict, user)

get_parking_data_func(garage_dict)
