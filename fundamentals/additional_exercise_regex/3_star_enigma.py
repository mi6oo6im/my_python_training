import re


def get_decrypter_key(text: str):
    regex = r'[SsTtAaRr]'
    matches = re.findall(regex, text)
    return len(matches)


def decrypter_func(text: str, decrypter_key: int):
    return ''.join([chr(ord(x) - decrypter_key) for x in text])


def extractor_func(text: str, regex: str):
    matches = re.search(regex, text)
    return matches.group('planet'), matches.group('attack')


pattern = r'@(?P<planet>[A-Z][a-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<attack>[AD])![^@\-!:>]*->(?P<soldiers>\d+)'
attacked_planets = []
destroyed_planets = []
number_of_messages = int(input())
for _ in range(number_of_messages):
    encrypted_message = input()
    key = get_decrypter_key(encrypted_message)
    decrypted_message = decrypter_func(encrypted_message, key)
    if re.search(pattern, decrypted_message):
        planet, attack = extractor_func(decrypted_message, pattern)
        if attack == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)
        attacked_planets = sorted(attacked_planets)
        destroyed_planets = sorted(destroyed_planets)

print(f'Attacked planets: {len(attacked_planets)}')
[print(f'-> {x}') for x in attacked_planets]
print(f'Destroyed planets: {len(destroyed_planets)}')
[print(f'-> {x}') for x in destroyed_planets]
