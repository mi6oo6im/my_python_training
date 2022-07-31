def insert_space_func(_message: str, _index: int):
    new_message = _message
    message_list = list(_message)
    if 0 <= _index < len(_message):
        message_list.insert(_index, ' ')
        new_message = ''.join(message_list)
        print(new_message)
    return new_message


def reverse_func(_message: str, _substring: str):
    if _substring in _message:
        reversed_substring = _substring[::-1]
        new_message = _message.replace(_substring, '', 1)
        _message = new_message + reversed_substring
        print(_message)
    else:
        print('error')
    return _message


def change_all_func(_message: str, _substring: str, _replacement_string: str):
    new_message = _message.replace(_substring, _replacement_string)
    print(new_message)
    return new_message


encrypted_message = input()
command_line = input()
while command_line != 'Reveal':
    if 'InsertSpace' in command_line:
        command, index = command_line.split(':|:')
        encrypted_message = insert_space_func(encrypted_message, int(index))
    elif 'Reverse' in command_line:
        command, substring = command_line.split(':|:')
        encrypted_message = reverse_func(encrypted_message, substring)
    elif 'ChangeAll' in command_line:
        command, substring, replacement_string = command_line.split(':|:')
        encrypted_message = change_all_func(encrypted_message, substring, replacement_string)
    command_line = input()
decrypted_message = encrypted_message
print(f'You have a new text message: {decrypted_message}')
