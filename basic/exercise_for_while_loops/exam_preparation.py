unacceptable_score = int(input())
unacceptable_counter = 0
is_unacceptable = False
total_score = 0
exercise_counter = 0
exercise_name = input()
current_score = 0
last_exercise = ""

while exercise_name != "Enough":
    last_exercise = exercise_name
    exercise_counter += 1
    current_score = int(input())
    total_score += current_score
    if current_score <= 4:
        unacceptable_counter += 1
        if unacceptable_counter == unacceptable_score:
            is_unacceptable = True
            break
    exercise_name = input()

average_score = total_score / exercise_counter

if is_unacceptable:
    print(f"You need a break, {unacceptable_counter} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {exercise_counter}")
    print(f"Last problem: {last_exercise}")
