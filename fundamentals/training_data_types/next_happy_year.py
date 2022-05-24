current_year = int(input())
is_happy = False
while not is_happy:
    current_year += 1
    current_year_str = str(current_year)
    for figure in current_year_str:
        if current_year_str.count(figure) > 1:
            break
    else:
        is_happy = True
        break
print(current_year)