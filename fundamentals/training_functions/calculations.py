def calculator(a_num, b_num, opp):
    """"multiply", "divide", "add", "subtract". """
    result = None
    if opp == "multiply":
        result = a_num * b_num
    elif opp == "divide":
        result = int(a_num / b_num)
    elif opp == "add":
        result = a_num + b_num
    elif opp == "subtract":
        result = a_num - b_num
    return result


operator = input()
a = int(input())
b = int(input())

print(calculator(a, b, operator))
