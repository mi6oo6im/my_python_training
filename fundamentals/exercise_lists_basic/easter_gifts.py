gifts_list = input().split()
command = input()
while command != 'No Money':
    command_list = command.split()
    command_line = command_list[0]
    if command_line == 'OutOfStock':
        gift_out_of_stock = command_list[1]
        if gift_out_of_stock in gifts_list:
            while gifts_list.count(gift_out_of_stock) > 0:
                out_of_stock_gift_index = gifts_list.index(gift_out_of_stock)
                gifts_list[out_of_stock_gift_index] = 'None'
    elif command_line == 'Required':
        required_gift = command_list[1]
        required_gift_index = int(command_list[2])
        if len(gifts_list) > required_gift_index >= 0:
            gifts_list[required_gift_index] = required_gift
    elif command_line == 'JustInCase':
        just_in_case_gift = command_list[1]
        gifts_list[-1] = just_in_case_gift
    command = input()
while gifts_list.count('None') > 0:
    gifts_list.remove('None')
gifts_string = ' '.join(gifts_list)
print(gifts_string)
