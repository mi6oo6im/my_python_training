matrix = [x.split() for x in input().split('|')]
flat = []
for row in range(len(matrix) - 1, -1, -1):
    flat.extend(matrix[row])
print(*flat, sep=' ')
