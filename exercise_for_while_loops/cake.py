width = int(input())
length = int(input())
total_cake_pieces = width * length
cake_is_over = False

command = input()
current_number_of_pieces = 0

while command != "STOP":
    current_number_of_pieces = int(command)
    total_cake_pieces -= current_number_of_pieces
    if total_cake_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
else:
    print(f"{abs(total_cake_pieces)} pieces are left.")
