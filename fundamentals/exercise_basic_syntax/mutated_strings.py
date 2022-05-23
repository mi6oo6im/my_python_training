init_string = input()
into_string = input()
old_string = init_string
for i in range(len(init_string)):
    left_string = into_string[:i+1:]
    right_string = init_string[i+1::]
    new_string = left_string + right_string
    if new_string == old_string:
        continue
    print(left_string + right_string)
    old_string = new_string
