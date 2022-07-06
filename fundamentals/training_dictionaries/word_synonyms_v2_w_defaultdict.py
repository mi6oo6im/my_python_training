from collections import defaultdict

word_count = int(input())
dictionary = defaultdict(list)
for _ in range(word_count):
    word = input()
    synonym = input()
    dictionary[word].append(synonym)

for k, v in dictionary.items():
    values = ', '.join(v)
    print(f'{k} - {values}')
