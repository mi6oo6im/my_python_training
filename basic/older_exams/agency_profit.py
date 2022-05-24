airline = input()
adult_tickets = int(input())
kids_tickets = int(input())
adults_net_price = float(input())
kids_net_price = adults_net_price * 0.3
customer_service_price = float(input())
total_tickets = adult_tickets + kids_tickets
net_income = adult_tickets * adults_net_price + \
             kids_net_price * kids_tickets + customer_service_price * total_tickets

net_profit = 0.2 * net_income
print(f"The profit of your agency from {airline} tickets is {net_profit:.2f} lv.")
