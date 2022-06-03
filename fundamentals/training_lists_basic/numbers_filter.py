numbers_qty = int(input())
num_list = []
filtered_list = []

for _ in range(numbers_qty):
    current_number = int(input())
    num_list.append(current_number)
filter_text = input()
for number in num_list:
    if number % 2 == 0 and filter_text == 'even':
        filtered_list.append(number)
    elif number % 2 != 0 and filter_text == 'odd':
        filtered_list.append(number)
    if number >= 0 and filter_text == 'positive':
        filtered_list.append(number)
    elif number < 0 and filter_text == 'negative':
        filtered_list.append(number)
print(filtered_list)