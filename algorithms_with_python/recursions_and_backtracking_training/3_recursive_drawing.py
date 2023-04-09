def draw_func(n):
    if n == 0:
        return

    print('*' * n)
    draw_func(n - 1)
    print('#' * n)


n = int(input())
draw_func(n)
