invited_num = int(input())
invited_guests = {input() for _ in range(invited_num)}
arrived = input()
while not arrived == 'END':
    invited_guests.discard(arrived)
    arrived = input()

sorted_guests_not_arrived = sorted(invited_guests)
print(len(sorted_guests_not_arrived), *sorted_guests_not_arrived, sep='\n')
