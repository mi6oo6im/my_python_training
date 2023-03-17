def squares(num):
    for n in range(1, num + 1):
        yield n*n


print(list(squares(5)))