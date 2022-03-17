first_num = int(input())
second_num = int(input())
sign = input()
even_odd = "odd"
result = 0

if sign in ("+", "-", "*"):
    if sign == "+":
        result = first_num + second_num
        if result % 2 == 0:
            even_odd = "even"
    elif sign == "-":
        result = first_num - second_num
        if result % 2 == 0:
            even_odd = "even"
    else:
        result = first_num * second_num
        if result % 2 == 0:
            even_odd = "even"
    print(f"{first_num} {sign} {second_num} = {result} - {even_odd}")
elif sign in ("/", "%"):
    if second_num == 0:
        print(f"Cannot divide {first_num} by zero")
    elif sign == "/":
        result = first_num / second_num
        print(f"{first_num} / {second_num} = {result:.2f}")
    else:
        result = first_num % second_num
        print(f"{first_num} % {second_num} = {result}")
