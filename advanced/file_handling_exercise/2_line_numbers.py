#######################################################################################################################
# -------------------------------------- Please read before you test ------------------------------------------------ #
# The script works with project scope as a working directory and all files are stored in a separate folder 'files'    #
# To work in current directory replace 'files/' with ''                                                               #
#######################################################################################################################


file_path = 'files/text.txt'
file2_path = 'files/output.txt'
punctuations = ["-", ",", ".", "!", "?", "'"]
result_list = []
with open(file_path, 'r') as file:
    rows_list = file.readlines()

    for row in range(len(rows_list)):
        current_line = rows_list[row]
        if not row == len(rows_list) - 1:
            current_line = current_line[:-1]  # remove the new line character from all but last line
        chars = len(current_line)
        spaces = current_line.count(' ')
        punctuations_count = 0
        for char in current_line:
            if char in punctuations:
                punctuations_count += 1
        letters = chars - spaces - punctuations_count
        result_string = f'Line {row + 1}: {current_line} ({letters})({punctuations_count})'
        result_list.append(result_string)

with open(file2_path, 'w') as file:
    file.write('\n'.join(result_list))
