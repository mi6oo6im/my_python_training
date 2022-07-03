word_count = int(input())
dictionary = {}
for _ in range(word_count):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = [synonym]
    else:
        if synonym not in dictionary.values():
            dictionary[word].append(synonym)

for k, v in dictionary.items():
    values = ', '.join(v)
    print(f'{k} - {values}')
