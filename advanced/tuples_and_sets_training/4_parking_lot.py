cars = int(input())
parking = {}
for _ in range(cars):
    direction, plate = input().split(', ')
    parking[plate] = direction

cars_in = {car for car, direction in parking.items() if direction == 'IN'}
if cars_in:
    print(*cars_in, sep='\n')
else:
    print('Parking Lot is Empty')