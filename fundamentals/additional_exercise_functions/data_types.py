def data_type(str1: str, str2: str):
    result = 0
    if str1 == 'int':
        result = int(str2) * 2
    elif str1 == 'real':
        result = f'{float(str2) * 1.5:.2f}'
    elif str1 == 'string':
        result = f"${str2}$"
    return result


input_one = input()
input_two = input()
print(data_type(input_one, input_two))
