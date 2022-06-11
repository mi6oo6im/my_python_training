unsorted_numbers_list = input().split()
sorted_numbers_list = sorted(list(int(x) for x in unsorted_numbers_list))
print(sorted_numbers_list)