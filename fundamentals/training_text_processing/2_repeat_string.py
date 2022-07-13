string_list = input().split()
res = ''
for i in string_list:
    res += i * len(i)
print(res)
