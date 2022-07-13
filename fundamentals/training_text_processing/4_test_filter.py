def censure_func(text: str, censure_list: list):
    for word in censure_list:
        new_text = text.replace(word, '*' * len(word))
        text = new_text
    return text


words_to_censure = input().split(', ')
text_to_censure = input()

print(censure_func(text_to_censure, words_to_censure))
