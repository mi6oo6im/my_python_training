current_year = int(input())
is_happy = False
while not is_happy:
    year_set = set()
    current_year += 1
    year_to_string = str(current_year)
    for i in year_to_string:
        year_set.add(i)
    if len(year_set) == len(year_to_string):
        is_happy = True
    else:
        continue
print(current_year)