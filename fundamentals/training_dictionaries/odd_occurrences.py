word_list_lower = [x.lower() for x in input().split()]
dictionary = {}
for i in range(len(word_list_lower)):
    key = word_list_lower[i]
    if key not in dictionary:
        dictionary[key] = 1
    else:
        dictionary[key] += 1
odd_dict = {k: v for k, v in dictionary.items() if v % 2 != 0}
print(*odd_dict.keys())