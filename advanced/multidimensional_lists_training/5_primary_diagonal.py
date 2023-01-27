size = int(input())
matrix = []
prime_diagonal_sum = 0
for i in range(size):
    matrix.append([])
    matrix[i].extend([int(x) for x in input().split()])
    prime_diagonal_sum += matrix[i][i]
print(prime_diagonal_sum)