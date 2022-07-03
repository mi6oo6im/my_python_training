line_item = input()
dictionary = {}
while line_item != 'stop':
    key = line_item
    value = int(input())
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value
    line_item = input()

for k, v in dictionary.items():
    print(f'{k} -> {v}')
