list_a = input().split(', ')
list_b = input().split(', ')

list_of_substrings = [x for x in list_a if any(x in y for y in list_b)]
print(list_of_substrings)