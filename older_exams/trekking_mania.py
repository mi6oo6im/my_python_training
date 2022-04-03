groups = int(input())
going_to_musala = 0
going_to_monblan = 0
going_to_kilimanjaro = 0
going_to_k2 = 0
going_to_everest = 0
total_climbers = 0
for group in range(groups):
    group_size = int(input())
    total_climbers += group_size
    if group_size <= 5:
        going_to_musala += group_size
    elif group_size <= 12:
        going_to_monblan += group_size
    elif group_size <= 25:
        going_to_kilimanjaro += group_size
    elif group_size <= 40:
        going_to_k2 += group_size
    else:
        going_to_everest += group_size

musala_percent = going_to_musala / total_climbers * 100
monblan_percent = going_to_monblan / total_climbers * 100
kilimanjaro_percent = going_to_kilimanjaro / total_climbers * 100
k2_percent = going_to_k2 / total_climbers * 100
everest_percent = going_to_everest / total_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
