list_of_numbers = input().split()
numbers_to_remove = int(input())
list_of_integers = [int(x) for x in list_of_numbers]
for _ in range(numbers_to_remove):
    smallest_number = min(list_of_integers)
    list_of_numbers.remove(str(smallest_number))
    list_of_integers.remove(smallest_number)
numbers_left_string = ', '.join(list_of_numbers)
print(numbers_left_string)
