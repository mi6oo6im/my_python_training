discount_percent = 15
tshirt_price = float(input())
needed_for_ball = float(input())
ball_is_won = False
shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
football_shoes = 2 * (tshirt_price + shorts_price)
total_cost_net = tshirt_price + shorts_price + socks_price + football_shoes
total_cost_gross = total_cost_net * (1 - discount_percent / 100)

if needed_for_ball <= total_cost_gross:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_cost_gross:.2f} lv.")
else:
    difference = abs(needed_for_ball - total_cost_gross)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
