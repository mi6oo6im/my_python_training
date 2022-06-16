def multiply_and_filter(score_list: list, factor: int):
    multiplied_list = list(map(lambda x: x * factor, score_list))
    avg_happiness = sum(multiplied_list) / len(multiplied_list)
    happy_workers = len([x for x in multiplied_list if x >= avg_happiness])
    return happy_workers


happy_score_list = list(map(int, input().split()))
office_workers = len(happy_score_list)
happiness_factor = int(input())
happy_workers_count = multiply_and_filter(happy_score_list, happiness_factor)
if happy_workers_count/office_workers >= 0.5:
    print(f'Score: {happy_workers_count}/{office_workers}. Employees are happy!')
else:
    print(f'Score: {happy_workers_count}/{office_workers}. Employees are not happy!')
