text = input()
print(text[0] + ''.join([text[x] for x in range(1, len(text)) if text[x] != text[x - 1]]))
