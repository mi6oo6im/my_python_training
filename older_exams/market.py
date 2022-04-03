strawberry_price = float(input())
q_ty_bananas = float(input())
q_ty_oranges = float(input())
q_ty_raspberries = float(input())
q_ty_strawberries = float(input())

raspberry_price = strawberry_price * 0.5
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2


total_cost = raspberry_price * q_ty_raspberries + \
             orange_price * q_ty_oranges + \
             banana_price * q_ty_bananas + \
             strawberry_price * q_ty_strawberries

print(f"{total_cost:.2f}")
