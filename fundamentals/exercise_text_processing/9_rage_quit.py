def counter_unique_func(string: str):
    unique_list = []
    counter = 0
    for char in string:
        if char not in unique_list and not char.isdigit():
            counter += 1
            unique_list.append(char)
    return counter


input_string = input()
upper_string = ''.join([x.upper() for x in input_string])
unique_counter = counter_unique_func(upper_string)
print(f'Unique symbols used: {unique_counter}')
new_string = ''
current_string = ''
repeater = ''
previous_is_num = False
for i in range(len(upper_string)):
    current_char = upper_string[i]
    if current_char.isdigit():
        repeater += current_char
        if i == len(upper_string) - 1:
            new_string += current_string * int(repeater)
        previous_is_num = True
    else:
        if previous_is_num:
            new_string += current_string * int(repeater)
            current_string = ''
            repeater = ''
        current_string += current_char
        previous_is_num = False
print(new_string)
