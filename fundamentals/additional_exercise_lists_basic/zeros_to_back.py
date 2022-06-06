numbers_list = input().split(', ')
for i in range(len(numbers_list) - 1, -1, -1):
    current_number = numbers_list[i]
    if current_number == '0':
        numbers_list.pop(i)
        numbers_list.append(current_number)
print(numbers_list)