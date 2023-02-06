import os


file_name = 'my_first_file.txt'
file_path = 'files/' + file_name

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_name}' was deleted")
else:
    print(f"File '{file_name}' does not exist")
