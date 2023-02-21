def print_figure(spaces, asterisks):
    print(spaces * ' ' + asterisks * '* ')


def get_figure_info():
    size = int(input())
    return size


figure_size = get_figure_info()
for row in range(figure_size):
    spaces_num = figure_size - row - 1
    asterisks_num = row + 1
    print_figure(spaces_num, asterisks_num)

for row in range(figure_size - 2, -1, -1):
    spaces_num = figure_size - row - 1
    asterisks_num = row + 1
    print_figure(spaces_num, asterisks_num)
