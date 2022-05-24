voucher = int(input())

line_command = input()
tickets = 0
items = 0
price = 0

while line_command != "End":
    if len(line_command) > 8:
        price = ord(line_command[0]) + ord(line_command[1])
        if voucher < price:
            break
        tickets += 1
        voucher -= price
    else:
        price = ord(line_command[0])
        if voucher < price:
            break
        items += 1
        voucher -= price
    line_command = input()

print(tickets)
print(items)
