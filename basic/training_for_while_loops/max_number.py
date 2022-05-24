import sys

max_num = -sys.maxsize
command_line = input()

while command_line != "Stop":
    if max_num < int(command_line):
        max_num = int(command_line)
    command_line = input()

print(max_num)
