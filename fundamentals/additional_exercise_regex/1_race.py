import re


def get_km_func(regex: str, text: str):
    km_list = re.findall(km_regex, race)
    km = sum(int(x) for x in km_list)
    return km


def get_racer_name_func(regex: str, text: str):
    name_list = re.findall(name_regex, race)
    name = ''.join(name_list)
    return name


racers_list = input().split(', ')
name_regex = r"[a-zA-Z]"
km_regex = r"\d"
ranking = {}
race = input()
sorted_ranking = {}
while race != 'end of race':
    racer = get_racer_name_func(name_regex, race)
    kilometers = get_km_func(km_regex, race)
    if racer in racers_list:
        if racer in ranking.keys():
            ranking[racer] += kilometers
        else:
            ranking[racer] = kilometers
    race = input()
sorted_ranking = dict(sorted(ranking.items(), key=lambda kv: kv[1], reverse=True))
place = 1
named_ranking = {}
for i in sorted_ranking.keys():
    if place == 1:
        named_ranking['1st'] = i
    elif place == 2:
        named_ranking['2nd'] = i
    elif place == 3:
        named_ranking['3rd'] = i
    place += 1
[print(f'{k} place: {v}') for k, v in named_ranking.items()]
