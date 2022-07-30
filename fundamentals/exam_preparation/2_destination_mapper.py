import re

destinations = input()
pattern = r'(=|\/)(?P<destination>[A-Z][A-z]{2,})\1'
matches = re.finditer(pattern, destinations)
travel_points = 0
destinations_list = []
for match in matches:
    destination = match.group('destination')
    destinations_list.append(destination)
    travel_points += len(destination)
destinations_str = ', '.join(destinations_list)
print(f'Destinations: {destinations_str}')
print(f'Travel Points: {travel_points}')
