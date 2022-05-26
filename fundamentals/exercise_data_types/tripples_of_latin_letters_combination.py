from itertools import combinations_with_replacement

a = 97
end_char = int(input())
char_set = []
for i in range(a, a + end_char):
    letter = chr(i)
    char_set.append(letter)
char_set_string = ''.join(str(x) for x in char_set)

combo_char = combinations_with_replacement(char_set_string, 3)
for set_chr in combo_char:
    set_chr_string = ''.join(str(y) for y in set_chr)
    print(set_chr_string)