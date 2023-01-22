string = input()
letters = {char: f'{char}: {string.count(char)} time/s' for char in string}
sorted_chars = sorted(letters.values())
print(*sorted_chars, sep='\n')
