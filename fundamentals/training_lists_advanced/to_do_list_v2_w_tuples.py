to_do_list = []
command = input()
while command != "End":
    command_list = command.split('-')
    index = int(command_list[0])
    note = command_list[1]
    command_tuple = (index, note)
    to_do_list.append(command_tuple)
    command = input()
to_do_list_sorted = [x[1] for x in sorted(to_do_list) if x != 0]
print(to_do_list_sorted)
