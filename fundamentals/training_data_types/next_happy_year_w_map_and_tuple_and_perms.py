from itertools import permutations

number = tuple(map(int, input()))
my_perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
list_perm = list(my_perm)
for digits in list_perm:
    if digits > number:
        result = ''.join(str(x) for x in digits)
        print(result)
        break
