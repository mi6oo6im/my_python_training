integer_list = [x for x in input().split(', ')]
positive_list = [x for x in integer_list if int(x) >= 0]
negative_list = [x for x in integer_list if int(x) < 0]
even_list = [x for x in integer_list if int(x) % 2 == 0]
odd_list = [x for x in integer_list if int(x) % 2 != 0]
positive_string = ', '.join(positive_list)
negative_string = ', '.join(negative_list)
even_string = ', '.join(even_list)
odd_string = ', '.join(odd_list)
print(f'Positive: {positive_string}\nNegative: {negative_string}\nEven: {even_string}\nOdd: {odd_string}')
