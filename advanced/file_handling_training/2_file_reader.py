file_path = 'files/numbers.txt'

with open(file_path, 'r') as file:
    data = file.readlines()
    numbers = map(int, data)
    print(sum(numbers))
