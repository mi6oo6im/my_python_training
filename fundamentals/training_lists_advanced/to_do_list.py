to_do_list = [0] * 10
command = input()
while command != "End":
    command_list = command.split('-')
    index = int(command_list[0]) - 1
    note = command_list[1]
    to_do_list.pop(index)
    to_do_list.insert(index, note)
    command = input()
to_do_list_sorted = [x for x in to_do_list if x != 0]
print(to_do_list_sorted)
