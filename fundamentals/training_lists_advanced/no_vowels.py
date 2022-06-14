vowels = ['a', 'o', 'u', 'e', 'i']


def no_vowel(string: str):
    if string.lower() not in vowels:
        return True
    else:
        return False


text = input()
text_wo_vowels = ''.join(list(filter(no_vowel, text)))
print(text_wo_vowels)