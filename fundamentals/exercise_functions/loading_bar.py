def loading_bar(single_number: int):
    if single_number == 100:
        print('100% Complete!\n[%%%%%%%%%%]')
    else:
        percents = (single_number // 10) * '%'
        points = (10 - (single_number // 10)) * '.'
        print(f'{single_number}% [{percents}{points}]\nStill loading...')


single_number = int(input())
loading_bar(single_number)
