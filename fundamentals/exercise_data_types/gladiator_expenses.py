lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
helmet_repairs = 0
sword_repairs = 0
shield_repairs = 0
armor_repairs = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        helmet_repairs += 1
    if fight % 3 == 0:
        sword_repairs += 1
        if fight % 2 == 0:
            shield_repairs += 1

armor_repairs = shield_repairs // 2

expenses = helmet_repairs * helmet_price + \
           sword_repairs * sword_price + \
           shield_repairs * shield_price + \
           armor_repairs * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
