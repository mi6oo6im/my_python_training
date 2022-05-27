a = 97
number_of_letters = int(input())

for i in range(a, a+number_of_letters):
    for j in range(a,  a+number_of_letters):
        for k in range(a, a + number_of_letters):
            print(f'{chr(i)}{chr(j)}{chr(k)}')