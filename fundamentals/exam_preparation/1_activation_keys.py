def contains_func(key: str, sub: str):
    if sub in key:
        return f'{key} contains {substring}'
    else:
        return "Substring not found!"


def flip_func(key: str, upper_lower: str, start_index: int, end_index: int):
    new_key = key
    if start_index >= 0 and end_index < len(key):
        _substring = key[start_index: end_index]
        upper_substring = _substring.upper()
        lower_substring = _substring.lower()
        if upper_lower == 'Upper':
            new_key = key.replace(_substring, upper_substring)
        else:
            new_key = key.replace(_substring, lower_substring)
        print(new_key)
    return new_key


def slice_func(key: str, start_index: int, end_index: int):
    _substring = key[start_index: end_index]
    new_key = key.replace(_substring, '')
    print(new_key)
    return new_key


raw_activation_key = input()
command_line = input()
while command_line != 'Generate':
    if 'Contains' in command_line:
        command, substring = command_line.split('>>>')
        print(contains_func(raw_activation_key, substring))
    elif 'Flip' in command_line:
        command, upper_lower_command, start_ind, end_ind = command_line.split('>>>')
        raw_activation_key = flip_func(raw_activation_key, upper_lower_command, int(start_ind), int(end_ind))
    elif 'Slice' in command_line:
        command, start_ind, end_ind = command_line.split('>>>')
        raw_activation_key = slice_func(raw_activation_key, int(start_ind), int(end_ind))
    command_line = input()
final_activation_key = raw_activation_key
print(f'Your activation key is: {final_activation_key}')
