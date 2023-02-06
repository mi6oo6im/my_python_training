#######################################################################################################################
# -------------------------------------- Please read before you test ------------------------------------------------ #
# The script works with project scope as a working directory and all files are in a separate folder 'files/example'   #
# The script works with '.' for current working directory scope or with relative or absolute path                     #
#######################################################################################################################

import os

REPORT_NAME = 'report.txt'
path = input('Please input "." or the relative / absolute path to the directory to be traversed: ')
files = {}  # files dictionary {.txt : ['first.txt', 'second.txt']}
result_list = []  # list of sorted extensions and files


def traverse_directory(dir_path, first_level=False):  # using recursion to travers 0 and 1st level folders
    current_dir = os.listdir(dir_path)

    for file in current_dir:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1]
            if file_extension not in files:
                files[file_extension] = []
            files[file_extension].append(file)
        elif os.path.isdir(file_path) and not first_level:  # ensure that only first level sub-folders are traversed
            traverse_directory(file_path, first_level=True)


traverse_directory(path)

sorted_files = sorted(files.items(), key=lambda x: x[0])  # sorting the files dictionary

# for each extension we create a separate string with all files in the expected format and append to result_list
for extension, file_names in sorted_files:
    extension_string = f'.{extension} \n' + '\n'.join([f'- - - {x}' for x in sorted(file_names)])
    result_list.append(extension_string)

result = '\n'.join(result_list)
report_file = os.path.join(path, REPORT_NAME)
with open(report_file, 'w') as f:
    f.write(result)
print(f'"{REPORT_NAME}" created in folder {path}')