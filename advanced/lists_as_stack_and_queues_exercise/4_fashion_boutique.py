clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
current_rack = rack_capacity
while clothes:
    current = clothes[-1]
    if current <= current_rack:
        current_rack -= clothes.pop()
    else:
        current_rack = rack_capacity
        racks += 1

print(racks)
