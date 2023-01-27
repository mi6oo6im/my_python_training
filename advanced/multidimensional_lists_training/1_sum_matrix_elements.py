rows, cols = [int(x) for x in input().split(', ')]
matrix = []
result = 0
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    result += sum(matrix[row])
print(result)
print(matrix)
