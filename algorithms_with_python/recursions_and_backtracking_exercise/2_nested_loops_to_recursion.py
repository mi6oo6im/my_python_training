def nested_loops_recursion(idx, vector):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return

    for num in range(1, len(vector) + 1):
        vector[idx] = num
        nested_loops_recursion(idx + 1, vector)


n = int(input())
arr = [None] * n

nested_loops_recursion(0, arr)
