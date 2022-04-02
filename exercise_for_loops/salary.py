num_tabs = int(input())
salary = float(input())

web_deduction = {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50
}

for i in range(num_tabs):
    web_page = input()
    if web_page in ("Facebook", "Instagram", "Reddit"):
        salary -= web_deduction[web_page]
        if salary <= 0:
            print("You have lost your salary.")
            break
if salary > 0:
    print(f"{salary:.0f}")
