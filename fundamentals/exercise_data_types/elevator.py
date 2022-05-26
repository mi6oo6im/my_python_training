import math

persons = int(input())
capacity = int(input())
courses = math.ceil(persons / capacity)

print(courses)