num_integers = int(input())
list_positives = []
list_negatives = []
for _ in range(num_integers):
    current_num = int(input())
    if current_num < 0:
        list_negatives.append(current_num)
    else:
        list_positives.append(current_num)
count_positives = len(list_positives)
sum_of_negatives = sum(list_negatives)
print(f"{list_positives}\n{list_negatives}")
print(f"Count of positives: {count_positives} \nSum of negatives: {sum_of_negatives}")
