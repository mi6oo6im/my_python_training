# "Bansko",  "Borovets", "Varna", "Burgas"
# "noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"
dictionary_price = {
            "BanskonoEquipment": 80,
            "BanskowithEquipment": 100,
            "BorovetsnoEquipment": 80,
            "BorovetswithEquipment": 100,
            "VarnanoBreakfast": 100,
            "VarnawithBreakfast": 130,
            "BurgasnoBreakfast": 100,
            "BurgaswithBreakfast": 130}

dictionary_vip_discount = {
            "BanskonoEquipment": 5,
            "BanskowithEquipment": 10,
            "BorovetsnoEquipment": 5,
            "BorovetswithEquipment": 10,
            "VarnanoBreakfast": 7,
            "VarnawithBreakfast": 12,
            "BurgasnoBreakfast": 7,
            "BurgaswithBreakfast": 12}
city = input()
vacation_package = input()
vip_discount = input()
days_vacation = int(input())
discount = 0

if days_vacation < 1:
    print("Days must be positive number!")
elif city not in ("Bansko", "Borovets", "Varna", "Burgas") or \
        vacation_package not in ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast"):
    print("Invalid input!")
else:
    price = dictionary_price[city+vacation_package]
    if vip_discount == "yes":
        discount = dictionary_vip_discount[city+vacation_package]
    if days_vacation > 7:
        days_vacation -= 1
    total_cost = price * days_vacation * (1 - discount / 100)
    print(f"The price is {total_cost:.2f}lv! Have a nice time!")
