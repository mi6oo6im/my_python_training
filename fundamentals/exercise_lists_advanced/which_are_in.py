list_a = input().split(', ')
list_b = input().split(', ')

list_of_substrings = list()
for word_a in list_a:
    for word_b in list_b:
        if word_a in word_b:
            list_of_substrings.append(word_a)

list_of_unique_substrings = list(set(list_of_substrings))
result_list = list(filter(lambda x: x in list_of_unique_substrings, list_a))
print(result_list)