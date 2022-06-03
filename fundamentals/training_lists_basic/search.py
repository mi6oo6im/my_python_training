number_of_lines = int(input())
filter_str = input()
list_of_all_texts = []
list_of_filtered_texts = []
for _ in range(number_of_lines):
    current_text = input()
    list_of_all_texts.append(current_text)
    if filter_str in current_text:
        list_of_filtered_texts.append(current_text)
print(list_of_all_texts)
print(list_of_filtered_texts)