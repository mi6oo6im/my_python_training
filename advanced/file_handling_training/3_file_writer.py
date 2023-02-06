file_name = 'my_first_file.txt'
file_path = 'files/' + file_name
with open(file_path, 'x') as file:
    file.write('I just created my first file!')

with open(file_path, 'r') as file:
    print(file.read())