def cast_spell_func(_party_dict: dict, _name: str, _mana_needed: int, _spell: str):
    current_mana = _party_dict[_name][1]
    if current_mana >= _mana_needed:
        _party_dict[_name][1] -= _mana_needed
        print(f"{_name} has successfully cast {_spell} and now has {_party_dict[_name][1]} MP!")
    else:
        print(f"{_name} does not have enough MP to cast {_spell}!")
    return _party_dict


def take_damage_func(_party_dict: dict, _name: str, _damage: int, _attacker: str):
    current_health = _party_dict[_name][0]
    if current_health > _damage:
        _party_dict[_name][0] -= _damage
        new_health = _party_dict[_name][0]
        print(f"{_name} was hit for {_damage} HP by {_attacker} and now has {new_health} HP left!")
    else:
        _party_dict.pop(_name)
        print(f"{_name} has been killed by {_attacker}!")
    return _party_dict


def recharge_func(_party_dict: dict, _name: str, _mana: int):
    current_mana = _party_dict[_name][1]
    if current_mana + _mana > maximum_mana:
        _party_dict[_name][1] = maximum_mana
        _mana = maximum_mana - current_mana
    else:
        _party_dict[_name][1] += _mana
    print(f"{_name} recharged for {_mana} MP!")
    return _party_dict


def heal_func(_party_dict: dict, _name: str, _health: int):
    current_health = _party_dict[_name][0]
    if current_health + _health > maximum_health:
        _party_dict[_name][0] = maximum_health
        _health = maximum_health - current_health
    else:
        _party_dict[_name][0] += _health
    print(f"{_name} healed for {_health} HP!")
    return _party_dict


def get_party_info_func(_party_dict: dict):
    return '\n'.join([f'{k}\n  HP: {v[0]}\n  MP: {v[1]}' for k, v in _party_dict.items()])


party_dict = {}
members = int(input())
maximum_health = 100
maximum_mana = 200
for _ in range(members):
    name, health, mana = input().split()
    party_dict[name] = [int(health), int(mana)]
command_line = input()
while command_line != 'End':
    if 'CastSpell' in command_line:
        command, name, mana_needed, spell = command_line.split(' - ')
        party_dict = cast_spell_func(party_dict, name, int(mana_needed), spell)
    elif 'TakeDamage' in command_line:
        command, name, damage, attacker = command_line.split(' - ')
        party_dict = take_damage_func(party_dict, name, int(damage), attacker)
    elif 'Recharge' in command_line:
        command, name, mana_gained = command_line.split(' - ')
        party_dict = recharge_func(party_dict, name, int(mana_gained))
    elif 'Heal' in command_line:
        command, name, health_gained = command_line.split(' - ')
        party_dict = heal_func(party_dict, name, int(health_gained))
    command_line = input()

print(get_party_info_func(party_dict))
