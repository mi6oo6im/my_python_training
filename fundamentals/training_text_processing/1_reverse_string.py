def reverse_func(text: str):
    text = text[-1::-1]
    return text


command = input()
while command != 'end':
    print(f'{command} = {reverse_func(command)}')
    command = input()
