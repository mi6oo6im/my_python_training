num_of_strings = int(input())
char = [',', '.', '_']

for i in range(num_of_strings):
    word = input()

    if any(x in char for x in word):
        print(f"{word} is not pure!")

    else:
        print(f"{word} is pure.")