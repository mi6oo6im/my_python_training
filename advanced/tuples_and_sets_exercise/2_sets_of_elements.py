set_1 = set()
set_2 = set()
len_1, len_2 = map(int, input().split())
for i in range(len_1 + len_2):
    current = int(input())
    if i < len_1:
        set_1.add(int(input()))
    else:
        set_2.add(int(input()))
print(*set_1.intersection(set_2), sep='\n')
