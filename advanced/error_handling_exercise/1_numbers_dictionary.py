numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:  # if a non-number value is input - handle ValueError exception
        print('The variable number must be an integer')
    except KeyError:  # if a non-existing key in the dictionary is input - handle KeyError exception
        print('Number does not exist in dictionary')
    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:  # if a non-existing key in the dictionary is input - handle KeyError exception
        print('Number does not exist in dictionary')
    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:  # if a non-existing key in the dictionary is input - handle KeyError exception
        print('Number does not exist in dictionary')
    line = input()
print(numbers_dictionary)
