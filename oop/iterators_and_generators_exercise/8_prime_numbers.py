import math
from typing import List


def get_primes(sequence: List[int]):
    for num in sequence:
        if num <= 1:
            continue

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
