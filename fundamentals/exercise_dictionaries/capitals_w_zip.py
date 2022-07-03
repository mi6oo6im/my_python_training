countries_list = input().split(', ')
capitals_list = input().split(', ')
country_capital = tuple(zip(countries_list, capitals_list))
dictionary = {country_capital[x][0]: country_capital[x][1] for x in range(len(countries_list))}
for k, v in dictionary.items():
    print(f'{k} -> {v}')
