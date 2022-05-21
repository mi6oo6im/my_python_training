number = float(input())

if number == 0:
    print('zero')
elif number < 0:
    if abs(number) > 1000000:
        print('large negative')
    elif abs(number) >= 1:
        print('negative')
    else:
        print('small negative')
else:
    if abs(number) > 1000000:
        print('large positive')
    elif abs(number) >= 1:
        print('positive')
    else:
        print('small positive')
