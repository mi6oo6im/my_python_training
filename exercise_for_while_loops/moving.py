width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

command = input()

no_more_room = False

while command != "Done":
    volume -= int(command)
    if volume < 0:
        no_more_room = True
        break
    command = input()

if no_more_room:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
else:
    print(f"{abs(volume)} Cubic meters left.")
