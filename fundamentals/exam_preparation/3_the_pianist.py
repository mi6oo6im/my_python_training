def add_func(dictionary: dict, _piece: str, _composer: str, _key: str):
    if _piece in dictionary:
        print(f"{_piece} is already in the collection!")
    else:
        dictionary[_piece] = {}
        dictionary[_piece][_composer] = _key
        print(f"{_piece} by {_composer} in {_key} added to the collection!")
    return dictionary


def remove_func(dictionary: dict, _piece: str):
    if _piece in dictionary.keys():
        dictionary.pop(_piece)
        print(f'Successfully removed {_piece}!')
    else:
        print(f"Invalid operation! {_piece} does not exist in the collection.")
    return dictionary


def change_key_func(dictionary: dict, _piece: str, _new_key: str):
    if _piece in dictionary.keys():
        for _composer in dictionary[_piece].keys():
            dictionary[_piece][_composer] = _new_key
        print(f"Changed the key of {_piece} to {_new_key}!")
    else:
        print(f"Invalid operation! {_piece} does not exist in the collection.")
    return dictionary


pieces_dictionary = {}
number_of_pieces = int(input())
for _ in range(number_of_pieces):
    command_line = input()
    piece, composer, key = command_line.split('|')
    pieces_dictionary[piece] = {}
    pieces_dictionary[piece][composer] = key
command_line = input()

while command_line != 'Stop':
    if 'Add' in command_line:
        command, piece, composer, key = command_line.split('|')
        pieces_dictionary = add_func(pieces_dictionary, piece, composer, key)
    elif 'Remove' in command_line:
        command, piece = command_line.split('|')
        pieces_dictionary = remove_func(pieces_dictionary, piece)
    elif 'ChangeKey' in command_line:
        command, piece, key = command_line.split('|')
        pieces_dictionary = change_key_func(pieces_dictionary, piece, key)
    command_line = input()

for k, v in pieces_dictionary.items():
    for composer, key in v.items():
        print(f"{k} -> Composer: {composer}, Key: {key}")
