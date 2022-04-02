goal_is_reached = False
steps = 0
command = input()

while command != "Going home":
    steps += int(command)
    if steps >= 10000:
        goal_is_reached = True
        break
    command = input()
else:
    steps += int(input())
    if steps >= 10000:
        goal_is_reached = True

difference = abs(10000 - steps)

if goal_is_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
