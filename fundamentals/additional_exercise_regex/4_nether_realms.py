import re


def valid_name_func(name: str, pattern: str):
    matches = re.findall(pattern, name)
    if len(matches) > 0:
        if matches[0]:
            return True
    return False


def health_func(name: str, pattern: str):
    matches = re.findall(pattern, name)
    health = 0
    for match in matches:
        health += ord(match)
    return health


def damage_func(name: str, pattern: str):
    matches = re.findall(pattern, name)
    damage = 0
    for match in matches:
        damage += float(match[0])
    multiplier = name.count('*')
    divider = name.count('/')
    if multiplier:
        damage *= (2 ** multiplier)
    if divider:
        damage /= (2 ** divider)
    return damage


health_regex = r'[^0-9+\-*\/\.]'
damage_regex = r'\+?((\-)?(\d+)+(\.\d+)?)'
demons = input()
delimiter = r',+\s*'
demon_book = sorted(re.split(delimiter, demons))
name_regex = r'^[^\s,]*$'
demon_book = [x.strip() for x in demon_book]
for demon in demon_book:
    if valid_name_func(demon, name_regex):
        print(f'{demon} - {health_func(demon, health_regex)} health, {damage_func(demon, damage_regex):.2f} damage')
