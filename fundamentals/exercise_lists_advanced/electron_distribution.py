number_of_electrons = int(input())
distribution_list = list()
index = 0
while number_of_electrons > 0:
    index += 1
    current_electrons = 2 * index ** 2
    if current_electrons > number_of_electrons:
        current_electrons = number_of_electrons
    distribution_list.append(current_electrons)
    number_of_electrons -= current_electrons

print(distribution_list)