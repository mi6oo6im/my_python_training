number_to_check = int(input())

for digit in range(1111, 9999 + 1):
    digit_as_string = str(digit)
    if "0" in digit_as_string:
        continue
    is_special = False
    for num in digit_as_string:
        if number_to_check % int(num) != 0:
            is_special = False
            break
        else:
            is_special = True
    if is_special:
        print(digit, end=" ")
