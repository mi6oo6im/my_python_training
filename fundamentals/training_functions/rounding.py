def rounding(numbers: list):
    numbers_list = list(float(x) for x in numbers)
    rounded_list = list(map(round, numbers_list))
    return rounded_list


nums_list = input().split()
print(rounding(nums_list))
