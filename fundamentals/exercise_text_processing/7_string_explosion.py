text = input()
new_text = ''
strength = 0
for i in range(len(text)):
    current_char = text[i]
    if current_char != '>':
        if strength > 0:
            strength -= 1
            continue
        new_text += current_char
    else:
        new_text += current_char
        if i == len(text) - 1:
            continue
        strength += int(text[i + 1])
print(new_text)