actor = input()
academy_score = float(input())
appraisers = int(input())

for i in range(appraisers):
    appraiser_name = input()
    individual_score = float(input())
    incremental_score = individual_score * len(appraiser_name) / 2
    academy_score += incremental_score
    if academy_score > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {academy_score}!")
        break
if academy_score <= 1250.5:
    print(f"Sorry, {actor} you need {1250.5 - academy_score:.1f} more!")
