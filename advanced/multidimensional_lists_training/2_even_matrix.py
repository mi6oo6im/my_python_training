size = int(input())
matrix = []
for row in range(size):
    matrix.append([])
    for col in input().split(', '):
        if int(col) % 2 == 0:
            matrix[row].append(int(col))
print(matrix)
