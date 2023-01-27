size = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]
flattened = []
[flattened.extend(row) for row in matrix]
print(flattened)