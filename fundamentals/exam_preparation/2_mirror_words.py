import re


def extract_word_pairs(_input_string: str, _pattern: str):
    matches = re.finditer(_pattern, _input_string)
    word_list = []
    for match in matches:
        first_word = match.group('first_word')
        second_word = match.group('second_word')
        word_list.append([first_word, second_word])
    return word_list


def extract_mirror_words(_extracted_words_list: list):
    mirror_words = []
    for pair in _extracted_words_list:
        first_word = pair[0]
        second_word = pair[1]
        reversed_second_word = second_word[::-1]
        if first_word == reversed_second_word:
            mirror_words.append([first_word, second_word])
    return mirror_words


input_string = input()
pattern = r'(#|@)(?P<first_word>[A-z]{3,})\1(#|@)(?P<second_word>[A-z]{3,})\3'
extracted_words_list = extract_word_pairs(input_string, pattern)
mirrored_words_list = extract_mirror_words(extracted_words_list)
if extracted_words_list:
    extracted_words_count = len(extracted_words_list)
    print(f"{extracted_words_count} word pairs found!")
else:
    print("No word pairs found!")
if mirrored_words_list:
    mirrored_words_list = [f'{x[0]} <=> {x[1]}' for x in mirrored_words_list]
    mirrored_words = ', '.join(mirrored_words_list)
    print("The mirror words are:")
    print(f'{mirrored_words}')
else:
    print("No mirror words!")
