size = int(input())
matrix = [[x for x in list(input())] for _ in range(size)]
symbol = input()
for i in range(size):
    if symbol in matrix[i]:
        print((i, matrix[i].index(symbol)))
        break
else:
    print(f'{symbol} does not occur in the matrix')
