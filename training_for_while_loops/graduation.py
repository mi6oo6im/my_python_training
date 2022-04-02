pupil_name = input()
grade = 1
flag = 0
total_score = 0

while grade <= 12:
    score = float(input())
    if score < 4:
        flag += 1
        if flag == 2:
            break
        continue
    grade += 1
    total_score += score
average_score = total_score / 12
if flag == 2:
    print(f"{pupil_name} has been excluded at {grade} grade")
else:
    print(f"{pupil_name} graduated. Average grade: {average_score:.2f}")
