vowels = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5
}
result = 0

string = input()

for i in string:
    if i in "aeiou":
        result += vowels[i]

print(result)
