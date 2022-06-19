def decode(word: str):
    ascii_index = int(''.join([x for x in word if x.isnumeric()]))
    ascii_symbol = chr(ascii_index)
    new_word = word.replace(str(ascii_index), ascii_symbol)
    word_list = list(new_word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    decoded_word = ''.join(word_list)
    return decoded_word


coded_list = input().split()
decoded_list = list()
for word in coded_list:
    decoded_list.append(decode(word))

print(*decoded_list, sep=' ')
