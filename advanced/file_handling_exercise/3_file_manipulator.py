#######################################################################################################################
# -------------------------------------- Please read before you test ------------------------------------------------ #
# The script works with project scope as a working directory and all files are stored in a separate folder 'files'    #
# To work in current directory replace 'files/' with ''                                                               #
#######################################################################################################################


import os

FOLDER = 'files/'  # files directory within project scope. Replace with '' to work in current directory


def create_file(file_name):  # creates a new file or wipes the content of an existing file with the same name
    file_name = FOLDER + file_name

    with open(file_name, 'w'):
        return f'{file_name} was created'


def add_file_content(file_name, content):  # appends content to existing file or creates the file if it doesn't exist
    file_name = FOLDER + file_name

    with open(file_name, 'a') as file:
        file.write(content)
        return f'Content "{content}" was added to file "{file_name}"'


def replace_file_content(file_name, old_content, new_content):  # replaces old with new content in existing file
    file_name = FOLDER + file_name                              # or error will be returned "An error occurred"

    try:  # handle FileNotFoundError error
        with open(file_name, 'r') as file:
            file_content = file.read()
            while old_content in file_content:
                file_content = file_content.replace(old_content, new_content)

        with open(file_name, 'w') as file:
            file.write(file_content)
            return f'Content "{old_content}" was replaced with new content "{new_content}" in file "{file_name}"'
    except FileNotFoundError:
        return "An error occurred"


def delete_file(file_name):  # deletes an existing file or error will be returned "An error occurred"
    try:  # handle FileNotFoundError error
        file_name = FOLDER + file_name
        os.remove(file_name)
        return f'{file_name} was deleted'
    except FileNotFoundError:
        return "An error occurred"


def control_flow(command, *args):
    result = None
    if command == 'Create':
        file_name = args[0]
        result = create_file(file_name)
    elif command == 'Add':
        file_name, content = args
        result = add_file_content(file_name, content)
    elif command == 'Replace':
        file_name, old_content, new_content = args
        result = replace_file_content(file_name, old_content, new_content)
    elif command == 'Delete':
        file_name = args[0]
        result = delete_file(file_name)
    return result


while True:
    command_line = input()
    if command_line == 'End':
        break
    else:
        command_word, *params = command_line.split('-')
        print(control_flow(command_word, *params))
