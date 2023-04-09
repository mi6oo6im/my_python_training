def gen_vector(idx, _vector):
    if idx >= len(_vector):
        print(*_vector, sep='')
        return

    for num in range(2):
        _vector[idx] = num
        gen_vector(idx + 1, _vector)


n = int(input())
vector = [0] * n
gen_vector(0, vector)