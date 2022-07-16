def ticket_is_valid(ticket: str):
    if len(ticket) == 20:
        return True
    return False


def ticket_is_winning(ticket: str):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for i in range(10, 5, -1):
        for symbol in winning_symbols:
            if symbol * i in left_half and symbol * i in right_half:
                if i == 10:
                    print(f'ticket "{ticket}" - {i}{symbol} Jackpot!')
                    return
                else:
                    print(f'ticket "{ticket}" - {i}{symbol}')
                    return
    print(f'ticket "{ticket}" - no match')
    return


winning_symbols = ['@', '#', '$', '^']
tickets_list = input().split(', ')
for ticket in tickets_list:
    if not ticket_is_valid(ticket.strip()):
        print('invalid ticket')
    else:
        ticket_is_winning(ticket.strip())

