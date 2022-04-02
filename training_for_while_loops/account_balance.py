command_line = input()
total = 0

while command_line != "NoMoreMoney":
    amount = float(command_line)
    if amount < 0:
        print("Invalid operation!")
        break
    total += amount
    print(f"Increase: {amount:.2f}")
    command_line = input()

print(f"Total: {total:.2f}")
