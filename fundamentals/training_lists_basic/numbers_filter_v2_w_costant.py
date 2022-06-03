numbers_qty = int(input())
num_list = []
filtered_list = []


for _ in range(numbers_qty):
    current_number = int(input())
    num_list.append(current_number)
filter_text = input()

FILTER_EVEN = filter_text == 'even'
FILTER_ODD = filter_text == 'odd'
FILTER_POSITIVE = filter_text == 'positive'
FILTER_NEGATIVE = filter_text == 'negative'

for number in num_list:
    filter_command = (
        FILTER_EVEN and number % 2 == 0 or
        FILTER_ODD and number % 2 != 0 or
        FILTER_POSITIVE and number >= 0 or
        FILTER_NEGATIVE and number < 0
    )
    if filter_command:
        filtered_list.append(number)
print(filtered_list)