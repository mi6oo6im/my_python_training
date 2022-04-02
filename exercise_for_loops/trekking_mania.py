# input

num_groups = int(input())
mussala_climbers = 0
montblan_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

mussala_percent = 0
montblan_percent = 0
kilimanjaro_percent = 0
k2_percent = 0
everest_percent = 0

for i in range(num_groups):
    group_size = int(input())
    total_climbers += group_size
    if group_size <= 5:
        mussala_climbers += group_size
    elif group_size <= 12:
        montblan_climbers += group_size
    elif group_size <= 25:
        kilimanjaro_climbers += group_size
    elif group_size <= 40:
        k2_climbers += group_size
    else:
        everest_climbers += group_size

if mussala_climbers == 0:
    mussala_percent = 0
else:
    mussala_percent = mussala_climbers / total_climbers * 100
print(f"{mussala_percent:.2f}%")
if montblan_climbers == 0:
    montblan_percent = 0
else:
    montblan_percent = montblan_climbers / total_climbers * 100
print(f"{montblan_percent:.2f}%")
if kilimanjaro_climbers == 0:
    kilimanjaro_percent = 0
else:
    kilimanjaro_percent = kilimanjaro_climbers / total_climbers * 100
print(f"{kilimanjaro_percent:.2f}%")
if k2_climbers == 0:
    k2_percent = 0
else:
    k2_percent = k2_climbers / total_climbers * 100
print(f"{k2_percent:.2f}%")
if everest_climbers == 0:
    everest_percent = 0
else:
    everest_percent = everest_climbers / total_climbers * 100
print(f"{everest_percent:.2f}%")
