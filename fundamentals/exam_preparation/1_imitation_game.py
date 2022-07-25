def move_func(text: str, num_letters: int):
    text_list = list(text)
    for _ in range(num_letters):
        letter_to_move = text_list.pop(0)
        text_list.append(letter_to_move)
    new_text = ''.join(text_list)
    return new_text


def insert_func(text: str, _index: int, _value: str):
    text_list = list(text)
    text_list.insert(_index, _value)
    new_text = ''.join(text_list)
    return new_text


def change_all_func(text: str, _substring: str, _replacement: str):
    new_text = text.replace(_substring, _replacement)
    return new_text


coded_message = input()
command_line = input()
while command_line != 'Decode':
    if 'Move' in command_line:
        command, number_of_letters = command_line.split('|')
        coded_message = move_func(coded_message, int(number_of_letters))
    elif 'Insert' in command_line:
        command, index, value = command_line.split('|')
        coded_message = insert_func(coded_message, int(index), value)
    elif 'ChangeAll' in command_line:
        command, substring, replacement = command_line.split('|')
        coded_message = change_all_func(coded_message, substring, replacement)
    command_line = input()
decoded_message = coded_message
print(f'The decrypted message is: {decoded_message}')
