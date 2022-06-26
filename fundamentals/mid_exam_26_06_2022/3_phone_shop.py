def add_func(inventory: list, phone_to_add: str):
    if phone_to_add not in inventory:
        inventory.append(phone_to_add)
    return inventory


def remove_func(inventory: list, phone_to_remove: str):
    if phone_to_remove in inventory:
        inventory.remove(phone_to_remove)
    return inventory


def bonus_func(inventory: list, old_new_phone: str):
    old_new_phone_list = old_new_phone.split(':')
    old_phone = old_new_phone_list[0]
    new_phone = old_new_phone_list[1]
    if old_phone in inventory:
        old_phone_index = inventory.index(old_phone)
        inventory.insert(old_phone_index + 1, new_phone)
    return inventory


def last_func(inventory: list, phone_to_put_last: str):
    if phone_to_put_last in inventory:
        phone_index = inventory.index(phone_to_put_last)
        inventory.append(phone_to_put_last)
        inventory.pop(phone_index)
    return inventory


def phone_shop_func(inventory: list):
    command_line = input()
    while command_line != 'End':
        command_line = command_line.split(' - ')
        command = command_line[0]
        parameter = command_line[1]
        if command == 'Add':
            phone_to_add = parameter
            add_func(inventory, phone_to_add)
        elif command == 'Remove':
            phone_to_remove = parameter
            remove_func(inventory, phone_to_remove)
        elif command == 'Bonus phone':
            old_new_phone = parameter
            bonus_func(inventory, old_new_phone)
        elif command == 'Last':
            phone_to_put_last = parameter
            last_func(inventory, phone_to_put_last)
        command_line = input()
    print(*inventory, sep=', ')


inventory_phones = input().split(', ')
phone_shop_func(inventory_phones)
