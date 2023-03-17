def genrange(start, end):
    ranger = (x for x in range(start, end + 1))
    return ranger


print(list(genrange(1, 10)))