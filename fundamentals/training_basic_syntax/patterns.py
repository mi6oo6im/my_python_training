num_symbols = 11

for i in range(1, num_symbols + 1, 2):
    print(int((num_symbols - i)/2) * ' ' + i * '*' + int((num_symbols - i)/2) * ' ')

for i in range(num_symbols - 2, 0, -2):
    print(int((num_symbols - i)/2) * ' ' + i * '*' + int((num_symbols - i)/2) * ' ')

