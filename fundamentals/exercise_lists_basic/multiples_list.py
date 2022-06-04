factor = int(input())
numbers = int(input())
numbers_list = []
current_number = 0
for _ in range(numbers):
    current_number += factor
    numbers_list.append(current_number)
print(numbers_list)