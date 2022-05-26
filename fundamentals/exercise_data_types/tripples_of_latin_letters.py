from itertools import combinations

a = 97
list_strings = []
num_char = int(input())

for i in range(a, a + num_char):
    letter_i = chr(i)
    list_strings.append(letter_i)
for j in list_strings:
    for k in list_strings:
        for x in list_strings:
            print(j+k+x)