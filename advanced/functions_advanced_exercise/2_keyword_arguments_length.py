def kwargs_length(**kvargs):
    personal_data = kvargs
    return len(personal_data)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))


# dictionary = {}
#
# print(kwargs_length(**dictionary))
#
