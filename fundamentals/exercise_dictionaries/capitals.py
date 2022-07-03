countries_list = input().split(', ')
capitals_list = input().split(', ')
dictionary = {countries_list[x]: capitals_list[x] for x in range(len(countries_list))}
for k, v in dictionary.items():
    print(f'{k} -> {v}')
