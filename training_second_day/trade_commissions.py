city = input()
sales = float(input())
commission = 0
is_valid = city in ("Sofia", "Varna", "Plovdiv") and 0 <= sales

commission_0_to_500 = {
    "Sofia": 0.05,
    "Varna": 0.045,
    "Plovdiv": 0.055
}

commission_500_to_1000 = {
    "Sofia": 0.07,
    "Varna": 0.075,
    "Plovdiv": 0.08
}

commission_1000_to_10000 = {
    "Sofia": 0.08,
    "Varna": 0.10,
    "Plovdiv": 0.12
}

commission_above_10000 = {
    "Sofia": 0.12,
    "Varna": 0.13,
    "Plovdiv": 0.145
}

if not is_valid:
    print("error")
else:
    if sales <= 500:
        commission = commission_0_to_500[city] * sales
    elif sales <= 1000:
        commission = commission_500_to_1000[city] * sales
    elif sales <= 10000:
        commission = commission_1000_to_10000[city] * sales
    else:
        commission = commission_above_10000[city] * sales

    print(f"{commission:.2f}")
