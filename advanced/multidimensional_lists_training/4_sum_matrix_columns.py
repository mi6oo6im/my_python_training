rows, cols = [int(x) for x in input().split(',')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
for col in range(cols):
    subtotal = 0
    for row in range(rows):
        subtotal += matrix[row][col]
    print(subtotal)
