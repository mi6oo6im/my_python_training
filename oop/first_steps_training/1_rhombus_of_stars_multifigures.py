def print_figure(spaces, asterisks):
    print(spaces * ' ' + asterisks * '* ')


def rhombus_func(figure_size):
    for row in range(figure_size):
        spaces_num = figure_size - row - 1
        asterisks_num = row + 1
        print_figure(spaces_num, asterisks_num)

    for row in range(figure_size - 2, -1, -1):
        spaces_num = figure_size - row - 1
        asterisks_num = row + 1
        print_figure(spaces_num, asterisks_num)


def triangle_func(figure_size):
    for row in range(figure_size):
        spaces_num = 0
        asterisks_num = row + 1
        print_figure(spaces_num, asterisks_num)


def square_func(figure_size):
    for row in range(figure_size):
        spaces_num = 0
        asterisks_num = figure_size
        print_figure(spaces_num, asterisks_num)


def get_figure_info():
    figure_size = int(input('Input figure size: '))
    figure_type = input('Figures: \n- Rhombus; \n- Triangle; \n- Square. \nInput figure type: ')
    return figure_size, figure_type


size, f_type = get_figure_info()
if f_type == 'Rhombus':
    rhombus_func(size)
elif f_type == 'Triangle':
    triangle_func(size)
elif f_type == 'Square':
    square_func(size)

