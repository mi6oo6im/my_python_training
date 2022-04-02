floors = int(input())
rooms = int(input())
for i in range(floors, 0, -1):
    for y in range(rooms):
        if i == floors:
            print(f"L{i}{y}", end=" ")
        elif i % 2 == 0:
            print(f"O{i}{y}", end=" ")
        else:
            print(f"A{i}{y}", end=" ")
    print("")
