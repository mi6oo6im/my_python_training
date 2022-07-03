bakery_list = input().split()
bakery_dict = {}
for i in range(0, len(bakery_list), 2):
    key = bakery_list[i]
    value = int(bakery_list[i + 1])
    bakery_dict[key] = value

print(bakery_dict)