text = input()

while text != 'End':
    repeated_text = ''
    if text == 'SoftUni':
        text = input()
        continue
    for i in text:
        repeated_text += 2 * i
    print(repeated_text)
    text = input()