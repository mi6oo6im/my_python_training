def even_odd(*args):
    *numbers, even_or_odd = args
    if even_or_odd == 'even':
        filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
    else:
        filtered_list = list(filter(lambda x: x % 2 == 1, numbers))
    return filtered_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
