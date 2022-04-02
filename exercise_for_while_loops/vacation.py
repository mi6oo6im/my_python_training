money_needed = float(input())
money_in_hand = float(input())
spend_counter = 0
days_counter = 0

while money_in_hand < money_needed:
    spend_save = input()
    amount = float(input())
    days_counter += 1
    if spend_save == "save":
        money_in_hand += amount
        spend_counter = 0
    else:
        money_in_hand -= amount
        if money_in_hand < 0:
            money_in_hand = 0
        spend_counter += 1
        if spend_counter == 5:
            break
if money_in_hand >= money_needed:
    print(f"You saved the money for {days_counter} days.")
else:
    print("You can't save the money.")
    print(f"{days_counter}")
