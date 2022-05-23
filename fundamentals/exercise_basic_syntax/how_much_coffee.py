command = input()
coffees_needed = 0
while command != 'END':
    if command.lower() in ("coding", "dog", "cat", "movie"):
        if command.isupper():
            coffees_needed += 2
        else:
            coffees_needed += 1
    if coffees_needed > 5:
        print('You need extra sleep')
        break
    command = input()
else:
    print(coffees_needed)