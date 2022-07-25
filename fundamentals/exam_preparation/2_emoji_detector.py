import re


def cool_threshold_func(pattern: str, _text: str):
    _cool_threshold = 1
    matches_number = re.findall(pattern, _text)
    for _match in matches_number:
        _cool_threshold *= int(_match)
    return _cool_threshold


def emoji_detector_func(pattern: str, _text: str, _cool_threshold: int):
    matches_emoji = re.findall(pattern, _text)
    _emoji_list = []
    _emoji_counter = 0
    for match in matches_emoji:
        _emoji_counter += 1
        coolness = sum([ord(x) for x in match[1]])
        if coolness > cool_threshold:
            _emoji_list.append(match[0] + match[1] + match[0])
    return _emoji_counter, _emoji_list


emoji_regex = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
numbers_regex = r'\d'
text = input()
cool_threshold = cool_threshold_func(numbers_regex, text)
emoji_counter, emoji_list = emoji_detector_func(emoji_regex, text, cool_threshold)

print(f'Cool threshold: {cool_threshold}')
print(f'{emoji_counter} emojis found in the text. The cool ones are:')
print(*emoji_list, sep='\n')
