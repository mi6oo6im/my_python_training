def fibonacci_rec(num):
    if num <= 1:
        return 1

    if num not in fibonacci_rec.cache:
        result = fibonacci_rec(num - 1) + fibonacci_rec(num - 2)
        fibonacci_rec.cache[num] = result
        return result

    return fibonacci_rec.cache[num]


fibonacci_rec.cache = {}

n = int(input())
# print(fibonacci_rec(n))


def fibonacci_iter(num):
    fib_0 = 1
    fib_1 = 1
    res = 0
    for num in range(1, n):
        res = fib_1 + fib_0
        fib_0, fib_1 = fib_1, res

    return res


print(fibonacci_iter(n))
