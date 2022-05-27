companions_count = int(input())
days_of_the_adventure = int(input())
coins = 0

for day in range(1, days_of_the_adventure + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    coins += 50
    coins -= companions_count * 2
    if day % 3 == 0:
        coins -= companions_count * 3
    if day % 5 == 0:
        coins += companions_count * 20
        if day % 3 == 0:
            coins -= companions_count * 2
coins //= companions_count
print(f"{companions_count} companions received {coins} coins each.")
