start = int(input())
end = int(input())

for i in range(start, end + 1): # итерираме по числата от start до end
    odd_sum = 0
    even_sum = 0
    num_as_str = str(i) # превръщаме си числото в текстов стринг
    for index, digit in enumerate(num_as_str): # итерираме през отделните цифри в числата като си взимаме индекса и амата цифра съответно в index, digit
        if index % 2 == 0:
            odd_sum += int(digit) # index започва с 0, затова четните числа са нечетни (о е 1, 1 е 2 и т.н.)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum: # за всяко число си проверяваме дали сумата от четни и нечетни е равна
        print(i, end=" ")
