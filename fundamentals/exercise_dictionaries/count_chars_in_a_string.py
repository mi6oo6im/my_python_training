string_list = list(input())
dictionary = {}
for letter in string_list:
    if letter != ' ':
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
for k, v in dictionary.items():
    print(f'{k} -> {v}')
