import sys

input_lines = int(input())
longest_num = -sys.maxsize
longest_str = None
for _ in range(input_lines):
    first, second = input().split('-')
    first_range = set(range(int(first.split(',')[0]), int(first.split(',')[1]) + 1))
    second_range = set(range(int(second.split(',')[0]), int(second.split(',')[1]) + 1))
    intersect = first_range.intersection(second_range)
    if len(intersect) > longest_num:
        longest_str = sorted(intersect)
        longest_num = len(intersect)
print(f'Longest intersection is {longest_str} with length {longest_num}')