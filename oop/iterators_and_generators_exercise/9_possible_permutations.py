from itertools import permutations


def possible_permutations(sequence):
    for perm in permutations(sequence):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]