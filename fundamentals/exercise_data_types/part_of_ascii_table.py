first_char = int(input())
last_char = int(input())
set = ''
for i in range(first_char, last_char + 1):
    character = chr(i)
    set += character + ' '

print(set)
