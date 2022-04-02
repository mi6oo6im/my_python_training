panelists = int(input())
total_score = 0
presentation_counter = 0
presentation_name = input()
while presentation_name != "Finish":
    presentation_counter += 1
    current_total_score = 0
    for each_panelist in range(panelists):
        score = float(input())
        current_total_score += score
    current_average_score = current_total_score / panelists
    print(f"{presentation_name} - {current_average_score:.2f}.")
    total_score += current_average_score
    presentation_name = input()

final_score = total_score / presentation_counter

print(f"Student's final assessment is {final_score:.2f}.")
