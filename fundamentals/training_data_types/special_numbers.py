n_number = int(input())
special_numbers = [5, 7, 11]

for i in range(1, n_number + 1):
    sum_n = 0
    num_to_string = str(i)
    for j in num_to_string:
        sum_n += int(j)
    if sum_n in special_numbers:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

