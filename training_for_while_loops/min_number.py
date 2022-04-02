import sys

min_num = sys.maxsize
command_line = input()

while command_line != "Stop":
    if min_num > int(command_line):
        min_num = int(command_line)
    command_line = input()

print(min_num)
