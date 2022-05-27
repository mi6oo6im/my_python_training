lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_repairs = lost_fights_count // 2
sword_repairs = lost_fights_count // 3
shield_repairs = lost_fights_count // 6
armor_repairs = shield_repairs // 2
expenses = helmet_repairs * helmet_price + \
           sword_repairs * sword_price + \
           shield_repairs * shield_price + \
           armor_repairs * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
