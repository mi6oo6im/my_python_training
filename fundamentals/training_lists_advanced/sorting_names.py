names_list = input().split(', ')
sorted_names_list = sorted(names_list, key= lambda x: (-len(x), x))
print(sorted_names_list)