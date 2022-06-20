def find_top_five(numbers_list: list):
    average_number = sum(numbers_list) / len(numbers_list)
    bigger_than_average = [x for x in numbers_list if x > average_number]
    if len(bigger_than_average) > 0:
        ordered_list = sorted(bigger_than_average, reverse=True)
        if len(ordered_list) > 5:
            top_five = ordered_list[0:5]
        else:
            top_five = ordered_list
        return ' '.join(list(map(str, top_five)))
    else:
        return 'No'


numbers = list(map(int, input().split()))
print(find_top_five(numbers))
