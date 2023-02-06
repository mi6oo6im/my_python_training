#######################################################################################################################
# -------------------------------------- Please read before you test ------------------------------------------------ #
# The script works with project scope as a working directory and all files are stored in a separate folder 'files'    #
# To work in current directory replace 'files/' with ''                                                               #
#######################################################################################################################


file_path = 'files/text.txt'

even_rows = []
chars = ["-", ",", ".", "!", "?"]
replacement = '@'
with open(file_path, 'r') as file:
    row = 0
    for line in file:
        if row % 2 == 0:
            even_rows.append(line)
        row += 1

for row in range(len(even_rows)):
    for char in chars:
        if char in even_rows[row]:
            even_rows[row] = even_rows[row].replace(char, replacement)

for row in even_rows:
    reversed_list = reversed(row.split())
    print(' '.join(reversed_list))
