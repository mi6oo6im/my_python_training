steps_are_made = False
steps = 0
command = input()

while steps <= 10000:
    if command == "Going home":
        steps += int(input())
        break
    steps += int(command)
    command = input()

if steps >= 10000:
    steps_are_made = True

difference = abs(10000 - steps)

if steps_are_made:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
