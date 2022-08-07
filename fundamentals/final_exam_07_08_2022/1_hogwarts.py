def abjuration_func(_spell: str):
    new_spell = _spell.upper()
    print(new_spell)
    return new_spell


def necromancy_func(_spell: str):
    new_spell = _spell.lower()
    print(new_spell)
    return new_spell


def illusion_func(_spell: str, _index: int, _letter: str):
    if 0 <= _index < len(_spell):
        spell_list = list(_spell)
        spell_list.pop(_index)
        spell_list.insert(_index, _letter)
        _spell = ''.join(spell_list)
        print('Done!')
    else:
        print('The spell was too weak.')
    return _spell


def divination_func(_spell: str, _first_substring: str, _second_substring: str):
    new_spell = _spell
    if _first_substring in _spell:
        new_spell = _spell.replace(_first_substring, _second_substring)
        print(new_spell)
    return new_spell


def alteration_func(_spell: str, _substring: str):
    new_spell = _spell
    if _substring in _spell:
        new_spell = _spell.replace(_substring, '')
        print(new_spell)
    return new_spell


spell = input()
command_line = input()
while command_line != 'Abracadabra':
    if 'Abjuration' in command_line:
        spell = abjuration_func(spell)
    elif 'Necromancy' in command_line:
        spell = necromancy_func(spell)
    elif 'Illusion' in command_line:
        command, index, letter = command_line.split()
        spell = illusion_func(spell, int(index), letter)
    elif 'Divination' in command_line:
        command, first_string, second_string = command_line.split()
        spell = divination_func(spell, first_string, second_string)
    elif 'Alteration' in command_line:
        command, substring = command_line.split()
        spell = alteration_func(spell, substring)
    else:
        print('The spell did not work!')
    command_line = input()