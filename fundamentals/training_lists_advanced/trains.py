wagons = int(input())
train = [0 for x in range(wagons)]
command = input()
while command != "End":
    command_list = command.split()
    action = command_list[0]
    if action == 'add':
        added_people = int(command_list[1])
        train[-1] += added_people
    elif action == 'insert':
        index = int(command_list[1])
        inserted_people = int(command_list[2])
        train[index] += inserted_people
    elif action == 'leave':
        index = int(command_list[1])
        people_left = int(command_list[2])
        train[index] -= people_left
    command = input()
print(train)
