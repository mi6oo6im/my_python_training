nums = [float(x) for x in input().split()]
numbers_dict = {num: f'{num:.1f} - {nums.count(num)} times' for num in nums}

print(*[num[1] for num in numbers_dict.items()], sep='\n')