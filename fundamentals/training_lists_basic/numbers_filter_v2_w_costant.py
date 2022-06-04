numbers_qty = int(input())
num_list = []
filtered_list = []
FILTER_EVEN = 'even'
FILTER_ODD = 'odd'
FILTER_POSITIVE = 'positive'
FILTER_NEGATIVE = 'negative'

for _ in range(numbers_qty):
    current_number = int(input())
    num_list.append(current_number)
filter_text = input()

for number in num_list:
    filter_command = (
        filter_text == FILTER_EVEN and number % 2 == 0 or
        filter_text == FILTER_ODD and number % 2 != 0 or
        filter_text == FILTER_POSITIVE and number >= 0 or
        filter_text == FILTER_NEGATIVE and number < 0
    )
    if filter_command:
        filtered_list.append(number)
print(filtered_list)