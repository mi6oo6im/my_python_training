def absolute_values(num):
    num_list = list(float(x) for x in num.split())
    num_abs_list = list(map(abs, num_list))
    return num_abs_list


print(absolute_values(input()))
