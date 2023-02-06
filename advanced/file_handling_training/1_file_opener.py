file_path = 'files/text.txt'

try:
    with open(file_path, 'r') as file:
        print('File found')
except FileNotFoundError:
    print('File not found')
