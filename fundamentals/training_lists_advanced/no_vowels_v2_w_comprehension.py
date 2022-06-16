vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
print(''.join([x for x in text if x.lower() not in vowels]))
