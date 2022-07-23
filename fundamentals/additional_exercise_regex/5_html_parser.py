import re


def get_title_func(text: str, pattern: str):
    matches = re.findall(pattern, text)
    return matches[0]


def get_content_func(text: str, pattern1: str, pattern2: str):
    matches_body = re.findall(pattern1, text)
    body_text = matches_body[0]
    matches = re.findall(pattern2, body_text)
    res = ''.join(matches)
    final = res.replace(r'\n', '')
    return final


html_code = input()
title_regex = r'<title>(.*)<\/title>'
body_regex = r'<body>(.*)<\/body>'
remove_tags_regex = r'(?:(?<=^)|(?<=>))([^<>]*?)(?=<|$)'
title = get_title_func(html_code, title_regex)
content = get_content_func(html_code, body_regex, remove_tags_regex)
print(f'Title: {title}')
print(f'Content: {content}')
