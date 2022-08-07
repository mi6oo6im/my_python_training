def hand_over_func(_dictionary: dict):
    res = []
    for _word in dictionary.keys():
        res.append(_word)
    return ' '.join(res)


def test_func(_dictionary: dict, _words_list: list):
    res = ''
    for _word in _words_list:
        if _word in _dictionary.keys():
            definitions = '\n -'.join(_dictionary[_word])
            res += f'{_word}:\n -{definitions}'
    return res


list_words_def = input().split(' | ')
dictionary = {}
for word_def in list_words_def:
    word, definition = word_def.split(': ')
    if word in dictionary.keys():
        dictionary[word].append(definition)
    else:
        dictionary[word] = [definition]
words_for_test_list = input().split(' | ')
command = input()
if command == 'Hand Over':
    print(hand_over_func(dictionary))
elif command == 'Test':
    print(test_func(dictionary, words_for_test_list))
