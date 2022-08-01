def take_odd_func(_password: str):
    new_password = _password[1::2]
    print(new_password)
    return new_password


def cut_func(_password: str, _index: int, _length: int):
    if 0 <= _index < len(_password):
        start_index = _index
        end_index = _index + _length
        _substring = _password[start_index:end_index]
        _password = _password.replace(_substring, '', 1)
        print(_password)
    return _password


def substitute_func(_password: str, _substring: str, _substitute: str):
    if _substring in _password:
        _password = _password.replace(_substring, _substitute)
        print(_password)
    else:
        print("Nothing to replace!")
    return _password


password = input()
command_line = input()
while command_line != "Done":
    if 'TakeOdd' in command_line:
        password = take_odd_func(password)
    elif 'Cut' in command_line:
        command, index, length = command_line.split()
        password = cut_func(password, int(index), int(length))
    elif 'Substitute' in command_line:
        command, substring, substitute = command_line.split()
        password = substitute_func(password, substring, substitute)
    command_line = input()
print(f'Your password is: {password}')
