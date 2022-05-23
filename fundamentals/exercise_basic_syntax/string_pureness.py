symbols = [',', '.', '_']

num_strings = int(input())
string = ''
for _ in range(num_strings):
    string = input()
    for s in symbols:
        if s in string:
            print(f'{string} is not pure!')
            break
    else:
        print(f"{string} is pure.")