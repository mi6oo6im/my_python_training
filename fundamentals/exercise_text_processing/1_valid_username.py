def check_username_def(text_list: list):
    res = []
    for word in text_list:
        newer_text = word.replace('-', '').replace('_', '')
        if newer_text.isalnum() and 3 < len(word) <= 16:
            res.append(word)
    return '\n'.join(res)


text = input().split(', ')
print(check_username_def(text))
